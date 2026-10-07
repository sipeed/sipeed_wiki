#!/usr/bin/env python3
"""Check that every image referenced by the docs actually exists.

Broken image links are easy to introduce (moving an assets/ folder, deleting a
file without touching the pages that use it) and hard to notice, because the
published site keeps serving stale copies that were uploaded by earlier builds.
This script catches them at CI time instead.

Only real image references are checked: markdown ``![alt](path)`` and HTML
``<img src=...>``. Fenced and inline code is stripped first, so example commands
like ``convert in.jpg out.jpg`` are not mistaken for links.

Usage:
    python3 tools/check_image_links.py            # fail on anything not in the baseline
    python3 tools/check_image_links.py --list     # print every broken link
    python3 tools/check_image_links.py --update-baseline
"""

import argparse
import json
import os
import re
import sys
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASELINE = os.path.join(ROOT, "tools", "known_broken_images.txt")
SCAN_DIRS = ["docs", "news", "pages", "layout"]
SKIP_DIRS = {".git", "out", ".venv", "node_modules", "__pycache__"}
PAGE_EXTS = {".md", ".html"}
IMG_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp", ".ico"}

FENCED = re.compile(r"```.*?```|~~~.*?~~~", re.S)
# HTML 注释里的引用不会渲染，不算断链
HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
INLINE_CODE = re.compile(r"`[^`\n]*`")
MD_IMG = re.compile(r"!\[[^\]]*\]\(\s*<?([^)\s>]+)")
HTML_IMG = re.compile(r"<img\b[^>]*?\bsrc\s*=\s*[\"']([^\"']+)", re.I)


def load_routes():
    """Map URL prefixes to on-disk directories, as teedoc does when building."""
    with open(os.path.join(ROOT, "site_config.json"), encoding="utf-8") as f:
        cfg = json.load(f)
    routes = {}
    for group in ("docs", "pages", "assets"):
        for url, path in (cfg.get("route", {}).get(group) or {}).items():
            routes[url] = path
    for url, targets in (cfg.get("translate", {}).get("docs") or {}).items():
        for t in targets:
            routes[t["url"]] = t["src"]
    # news/ 由 blog 插件发布在 /news/ 下，site_config 的 route 里没有登记
    routes.setdefault("/news/", "news")
    return dict(sorted(routes.items(), key=lambda kv: -len(kv[0])))


def resolve(ref, page_path, routes):
    """Return the on-disk path a reference points at, or None if it is external."""
    ref = ref.strip().strip("'\"")
    if ref.startswith(("http://", "https://", "//", "data:", "mailto:")):
        return None
    ref = urllib.parse.unquote(ref.split("#")[0].split("?")[0])
    if not ref or os.path.splitext(ref)[1].lower() not in IMG_EXTS:
        return None
    if ref.startswith("/"):
        for url, path in routes.items():
            if ref.startswith(url):
                return os.path.normpath(os.path.join(ROOT, path, ref[len(url):]))
        # 不匹配任何路由时，teedoc 把绝对路径按「该文档所属路由的根」解析，
        # 而不是站点根。例如 /assets/x.jpg 出现在 docs/soft/maixpy/en/ 下的页面里，
        # 实际指向 docs/soft/maixpy/assets/x.jpg。
        rel_page = os.path.relpath(page_path, ROOT)
        for _url, path in routes.items():
            if rel_page.startswith(path + os.sep):
                cand = os.path.normpath(
                    os.path.join(ROOT, os.path.dirname(path), ref.lstrip("/")))
                if os.path.exists(cand):
                    return cand
        return os.path.normpath(os.path.join(ROOT, ref.lstrip("/")))
    return os.path.normpath(os.path.join(os.path.dirname(page_path), ref))


def scan():
    routes = load_routes()
    broken = []
    for top in SCAN_DIRS:
        for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, top)):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for name in filenames:
                if os.path.splitext(name)[1].lower() not in PAGE_EXTS:
                    continue
                page = os.path.join(dirpath, name)
                try:
                    text = open(page, encoding="utf-8").read()
                except (OSError, UnicodeDecodeError):
                    continue
                text = INLINE_CODE.sub(" ", FENCED.sub(" ", HTML_COMMENT.sub(" ", text)))
                rel_page = os.path.relpath(page, ROOT)
                for ref in set(MD_IMG.findall(text) + HTML_IMG.findall(text)):
                    if "{{" in ref or "{%" in ref:  # jinja template expression
                        continue
                    target = resolve(ref, page, routes)
                    if target and not os.path.exists(target):
                        broken.append(f"{rel_page}\t{ref}")
    return sorted(set(broken))


def read_baseline():
    if not os.path.exists(BASELINE):
        return set()
    with open(BASELINE, encoding="utf-8") as f:
        return {l.rstrip("\n") for l in f if l.strip() and not l.startswith("#")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true", help="print all broken links")
    ap.add_argument("--update-baseline", action="store_true",
                    help="record the current broken links as accepted")
    args = ap.parse_args()

    broken = scan()
    if args.update_baseline:
        with open(BASELINE, "w", encoding="utf-8") as f:
            f.write("# Image links that are already broken and not yet fixed.\n"
                    "# CI fails on anything NOT listed here, so this file may shrink\n"
                    "# but must never grow. Regenerate with:\n"
                    "#     python3 tools/check_image_links.py --update-baseline\n")
            f.write("\n".join(broken) + "\n")
        print(f"baseline updated: {len(broken)} known broken links")
        return 0

    baseline = read_baseline()
    new = [b for b in broken if b not in baseline]
    fixed = [b for b in baseline if b not in broken]

    if args.list:
        for b in broken:
            page, ref = b.split("\t")
            print(f"{page}: {ref}")

    print(f"{len(broken)} broken image links "
          f"({len(baseline)} known, {len(new)} new, {len(fixed)} fixed since baseline)")

    if fixed:
        print(f"\n{len(fixed)} link(s) in the baseline are fixed - please run "
              f"`python3 tools/check_image_links.py --update-baseline` and commit.")
    if new:
        print(f"\nNew broken image links introduced by this change:\n")
        for b in new:
            page, ref = b.split("\t")
            print(f"  {page}\n      -> {ref}")
        print("\nFix the path, add the missing image, or remove the reference.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
