#!/usr/bin/env python3
"""Sync the built wiki into a Qiniu bucket, concurrently.

Compares against what is actually in the bucket (key + Qiniu etag), not against
the previous gh-pages build, so a failed or partial run is repaired by the next
one, and an empty bucket gets a full upload. Never deletes.

A Qiniu bucket does not behave like the Tencent COS static website we migrate
from, so this also uploads (to the bucket only, not to the build dir):
  - <dir>.html for every <dir>/index.html without a sibling <dir>.html: a stub
    that sends the browser to <dir>/ (COS answered /dir with a 302). The CDN
    rewrites /X to /X.html, matching COS serving X.html for /X.
  - errno-404: copy of 404.html, the bucket's custom 404 page.

Non-HTML first, HTML last, so pages never go live before their assets.

Usage:
  QINIU_ACCESS_KEY=... QINIU_SECRET_KEY=... python3 upload_qiniu.py --bucket <b> <build_dir>
Exit code is non-zero if any upload fails after retries.
"""
import argparse
import html
import io
import mimetypes
import os
import sys
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

import qiniu
from qiniu.utils import etag_stream

RETRIES = 3
WORKERS = 16

STUB = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="robots" content="noindex">
<title>Redirecting</title>
<script>
(function () {
  var l = window.location, p = l.pathname.replace(/\\.html$/, '');
  l.replace(p + '/' + l.search + l.hash);
})();
</script>
<noscript><meta http-equiv="refresh" content="0;url=./{href}/"></noscript>
</head><body><a href="./{href}/">{text}/</a></body></html>
"""


def local_files(root):
    """Relative paths of all files, skipping dot files/dirs (like teedoc-upload)."""
    out = []
    for d, ds, fs in os.walk(root):
        ds[:] = [x for x in ds if not x.startswith(".")]
        for f in fs:
            if not f.startswith("."):
                out.append(os.path.relpath(os.path.join(d, f), root).replace(os.sep, "/"))
    return out


def stub_bytes(dirname):
    href = html.escape(urllib.parse.quote(dirname), quote=True)
    return STUB.replace("{href}", href).replace("{text}", html.escape(dirname)).encode("utf-8")


def mime_of(key):
    if key == "errno-404" or key.endswith((".html", ".htm")):
        return "text/html; charset=utf-8"
    return mimetypes.guess_type(key)[0]  # None -> SDK default (application/octet-stream)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bucket", required=True)
    ap.add_argument("build_dir")
    args = ap.parse_args()

    ak = os.environ.get("QINIU_ACCESS_KEY", "")
    sk = os.environ.get("QINIU_SECRET_KEY", "")
    if not ak or not sk:
        sys.exit("QINIU_ACCESS_KEY / QINIU_SECRET_KEY not set")
    root = args.build_dir
    if not os.path.isfile(os.path.join(root, "index.html")):
        sys.exit("refusing to upload: %s/index.html not found" % root)
    auth = qiniu.Auth(ak, sk)

    # what should be in the bucket: key -> ("file", path) | ("data", bytes)
    want = {k: ("file", os.path.join(root, k)) for k in local_files(root)}
    for k in list(want):
        if k.endswith("/index.html"):
            d = k[: -len("/index.html")]
            if d + ".html" not in want:
                want[d + ".html"] = ("data", stub_bytes(d.rsplit("/", 1)[-1]))
    if "404.html" in want:
        want["errno-404"] = want["404.html"]

    # what is in the bucket
    have, marker = {}, None
    bm = qiniu.BucketManager(auth)
    while True:
        ret, eof, info = bm.list(args.bucket, marker=marker, limit=1000)
        if ret is None:
            sys.exit("cannot list bucket %s: %s" % (args.bucket, info))
        for it in ret.get("items", []):
            have[it["key"]] = (it["hash"], it.get("mimeType", ""))
        if eof:
            break
        marker = ret.get("marker")

    def etag(src):
        kind, v = src
        return qiniu.etag(v) if kind == "file" else etag_stream(io.BytesIO(v))

    with ThreadPoolExecutor(WORKERS) as ex:
        hashes = dict(zip(want, ex.map(etag, want.values())))
    def stale(k):
        if k not in have or have[k][0] != hashes[k]:
            return True
        mime = mime_of(k)  # also repair objects stored with a wrong Content-Type
        return bool(mime) and have[k][1] != mime

    todo = sorted((k for k in want if stale(k)),
                  key=lambda k: (k.endswith((".html", ".htm")) or k == "errno-404", k))
    print("%d files in build (+stubs), %d in bucket, %d to upload to %s"
          % (len(want), len(have), len(todo), args.bucket), flush=True)

    def upload(key):
        kind, v = want[key]
        mime = mime_of(key)
        extra = {"mime_type": mime} if mime else {}
        err = None
        for attempt in range(RETRIES):
            try:
                token = auth.upload_token(args.bucket, key, 3600)
                if kind == "file":
                    ret, info = qiniu.put_file(token, key, v, version="v2", **extra)
                else:
                    ret, info = qiniu.put_data(token, key, v, **extra)
                if ret and ret.get("key") == key and ret.get("hash") == hashes[key]:
                    return None
                err = "status %s" % getattr(info, "status_code", "?")
            except Exception as e:  # network errors: retry
                err = str(e)
            if attempt + 1 < RETRIES:
                time.sleep(2 * (attempt + 1))
        return "%s: %s" % (key, err)

    start = time.time()
    is_page = lambda k: k.endswith((".html", ".htm")) or k == "errno-404"
    failures, attempted = [], 0
    with ThreadPoolExecutor(WORKERS) as ex:
        for name, batch in (("assets", [k for k in todo if not is_page(k)]),
                            ("pages", [k for k in todo if is_page(k)])):
            attempted += len(batch)
            failures += [r for r in ex.map(upload, batch) if r]
            if failures:
                if name == "assets":
                    print("asset upload failed, pages not uploaded")
                break
    print("uploaded %d/%d in %.0fs" % (attempted - len(failures), len(todo), time.time() - start))
    for f in failures[:50]:
        print("FAILED", f)
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
