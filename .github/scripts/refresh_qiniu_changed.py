#!/usr/bin/env python3
"""Refresh Qiniu CDN cache for long-cached files that a publish overwrote.

wiki.sipeed.com is served by Qiniu CDN in front of the Tencent COS origin.
Qiniu keeps HTML/JSON/XML and suffix-less URLs for only 10 minutes, so pages
pick up a publish on their own. Images, JS, CSS, media and archives are kept
for a day or longer, so when a publish overwrites one of them under the same
name, users would keep getting the old copy. This script refreshes exactly
those URLs.

New files need no refresh (nothing is cached yet), and HTML is left to expire
by itself: teedoc rewrites hundreds of unchanged pages per build, which would
exhaust the account-wide quota (500 URLs/day, shared with other Sipeed sites).

Usage: refresh_qiniu_changed.py <old_dir> <new_dir> [overwritten_list]
  old_dir           previous site (the gh-pages checkout)
  new_dir           freshly built site
  overwritten_list  optional file, one key per line, of objects whose content
                    the Qiniu bucket upload replaced (upload_qiniu.py
                    --overwritten-list). Covers files a previous failed run
                    left stale, which the gh-pages diff cannot see.
Env: QINIU_ACCESS_KEY, QINIU_SECRET_KEY (never printed)

Best-effort: always exits 0 so a CDN problem never fails the deploy.
"""

import base64
import filecmp
import hashlib
import hmac
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

SITE = "https://wiki.sipeed.com/"
API = "https://fusion.qiniuapi.com/v2/tune/refresh"
MAX_URLS = 100  # one API call; keep most of the daily quota for other sites

# Suffixes Qiniu caches for 1 day or longer on wiki.sipeed.com. Keep in sync
# with the domain's cache rules (Qiniu console > CDN > wiki.sipeed.com > cache
# settings, or GET https://api.qiniu.com/domain/wiki.sipeed.com -> cache);
# anything else expires within 10 minutes.
LONG_CACHED = {
    ".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp", ".ico",
    ".js", ".css", ".txt", ".shtml", ".csv", ".bat",
    ".m3u8",
    ".avi", ".mkv", ".mp4", ".mov", ".flv", ".rm", ".rmvb", ".swf",
    ".mp3", ".wav", ".wmv", ".rmi", ".aac",
    ".rar", ".7z", ".zip", ".gzip", ".dmg", ".gz", ".ios", ".tar", ".jar",
    ".exe", ".deb", ".ipa", ".apk", ".sis", ".psd", ".dat",
}


def overwritten_files(old_dir, new_dir):
    """Relative paths that exist in both trees with different content."""
    changed = []
    for root, dirs, files in os.walk(new_dir):
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in files:
            if os.path.splitext(name)[1].lower() not in LONG_CACHED:
                continue
            new_path = os.path.join(root, name)
            rel = os.path.relpath(new_path, new_dir)
            old_path = os.path.join(old_dir, rel)
            if not os.path.isfile(new_path) or not os.path.isfile(old_path):
                continue
            try:
                if not filecmp.cmp(old_path, new_path, shallow=False):
                    changed.append(rel.replace(os.sep, "/"))
            except OSError as e:
                print("WARN: cannot compare %s: %s" % (rel, e))
    # Main-site files first: MaixPy/MaixCDK sub-sites are rebuilt by their own
    # repos and must not crowd main-site files out of the per-run cap.
    return sorted(changed, key=lambda p: (p.startswith(("maixpy/", "maixcdk/")), p))


def refresh(urls, ak, sk):
    # QBox signs "<path>\n" only; a JSON body is not part of the signature.
    path = urllib.parse.urlparse(API).path
    sign = hmac.new(sk.encode(), (path + "\n").encode(), hashlib.sha1).digest()
    req = urllib.request.Request(
        API,
        data=json.dumps({"urls": urls}).encode(),
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Authorization": "QBox %s:%s" % (ak, base64.urlsafe_b64encode(sign).decode()),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        return {"code": e.code, "error": e.read().decode(errors="replace")[:300]}


def main():
    if len(sys.argv) not in (3, 4):
        print("WARN: usage: refresh_qiniu_changed.py <old_dir> <new_dir> [overwritten_list];"
              " skipping CDN refresh.")
        return
    old_dir, new_dir = sys.argv[1], sys.argv[2]
    for d in (old_dir, new_dir):
        if not os.path.isdir(d):
            print("WARN: directory not found: %s; skipping CDN refresh." % d)
            return

    changed = overwritten_files(old_dir, new_dir)
    if len(sys.argv) == 4:
        try:
            with open(sys.argv[3], encoding="utf-8") as f:
                extra = [l.strip() for l in f if l.strip()]
        except (OSError, ValueError) as e:
            print("WARN: cannot read %s: %s" % (sys.argv[3], e))
            extra = []
        extra = [p for p in extra if os.path.splitext(p)[1].lower() in LONG_CACHED]
        merged = set(changed) | set(extra)
        print("%d long-cached file(s) from the bucket upload, %d not in the gh-pages diff."
              % (len(extra), len(merged) - len(changed)))
        changed = sorted(merged, key=lambda p: (p.startswith(("maixpy/", "maixcdk/")), p))
    print("%d long-cached file(s) overwritten by this publish." % len(changed))
    if not changed:
        return
    # Leave sub-delims raw like browsers do, so the URL matches the cache key.
    urls = [SITE + urllib.parse.quote(p, safe="/!$&'()*+,;=:@") for p in changed]
    if len(urls) > MAX_URLS:
        print("WARN: %d URLs exceed the per-run cap of %d; refreshing the first %d."
              " Refresh the rest by hand (e.g. a directory refresh) if needed."
              % (len(urls), MAX_URLS, MAX_URLS))
        for u in urls[MAX_URLS:]:
            print("  not refreshed: " + u)
        urls = urls[:MAX_URLS]
    for u in urls:
        print("  refresh: " + u)

    ak = os.environ.get("QINIU_ACCESS_KEY", "")
    sk = os.environ.get("QINIU_SECRET_KEY", "")
    if not ak or not sk:
        print("WARN: QINIU_ACCESS_KEY / QINIU_SECRET_KEY not set; skipping CDN refresh.")
        return

    result = refresh(urls, ak, sk)
    if result.get("code") == 200:
        print("CDN refresh accepted; URL quota left today: %s/%s."
              % (result.get("urlSurplusDay"), result.get("urlQuotaDay")))
    else:
        print("WARN: CDN refresh not accepted (continuing): code=%s error=%s"
              % (result.get("code"), result.get("error")))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # best-effort: never fail the deploy
        print("WARN: CDN refresh failed (continuing): %s: %s" % (type(e).__name__, e))
    sys.exit(0)
