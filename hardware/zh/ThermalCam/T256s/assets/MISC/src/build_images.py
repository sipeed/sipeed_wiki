#!/usr/bin/env python3
"""Generate the MS-T256S wiki images from real device data.

Every thermal picture comes from a real T256S: frames captured over its HTTP API, its own web
page (served back by mock_device.py), and the screen recording already in assets/Screenshots.
Palettes are exact copies of the firmware tables (palettes.py).

    # 1. once, with a T256S connected (firmware 26.40.0 or later)
    python3 build_images.py capture --device http://192.168.17.1 --out ~/t256s-capture

    # 2. render every image (zh and _en) into the assets folder this script lives in
    python3 build_images.py build --capture ~/t256s-capture

Needs Python 3 with numpy, scipy, Pillow and websocket-client, Chromium or Chrome, ImageMagick 7,
and the Noto Sans / Noto Sans CJK SC / Noto Sans Mono fonts.
"""
import argparse
import json
import subprocess
import tempfile
import time
import urllib.request
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
ASSETS = HERE.parents[1]                         # .../T256s/assets
RENDER_URL = "https://sipeed.com/pre-order/t256s/cover.png"


# ---------------------------------------------------------------- capture

def capture(device, out):
    out = Path(out)
    (out / "page").mkdir(parents=True, exist_ok=True)

    def get(path):
        with urllib.request.urlopen(device.rstrip("/") + path, timeout=10) as response:
            return response.read(), response.headers

    (out / "page/protocol-v1.html").write_bytes(get("/")[0])
    (out / "page/protocol-v1.js").write_bytes(get("/protocol-v1.js")[0])
    palette = json.loads(get("/api/cmap")[0]).get("index", 2)
    (out / "palette.txt").write_text(f"{palette}\n")
    import base64
    for source in ("sr", "native"):
        jpeg, headers = get(f"/frame.jpg?source={source}")
        (out / f"frame-{source}.jpg").write_bytes(jpeg)
        (out / f"frame-{source}.meta").write_bytes(base64.b64decode(headers["X-Sipeed-Meta"]))
    for index in (1, 2, 3):
        (out / f"frame-temp16-{index}.bin").write_bytes(get("/frame.temp16")[0])
        time.sleep(0.2)
    print(f"capture saved to {out}")


# ---------------------------------------------------------------- encoding

MAX_WIDTH = {                                   # pixels; the wiki shows these at 360 - 700 px
    "MISC/palettes": 1160, "MISC/screen-gestures": 1000, "Screenshots/screen-live": 1000,
    "Screenshots/screen-status-panel": 1000, "Screenshots/web-ui": 820,
}


def encode(png, target, quality=86):
    """Write the final asset: JPEG for photographic content, 256-color PNG for UI and diagrams."""
    target = Path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    key = str(target.relative_to(ASSETS).with_suffix("")).removesuffix("_en")
    width = MAX_WIDTH.get(key)
    if target.suffix == ".jpg":
        image = Image.open(png)
        if image.mode in ("RGBA", "LA"):
            flat = Image.new("RGB", image.size, "white")
            flat.paste(image, mask=image.split()[-1])
            image = flat
        image = image.convert("RGB")
        if width and image.width > width:
            image = image.resize((width, round(image.height * width / image.width)), Image.LANCZOS)
        image.save(target, "JPEG", quality=quality, optimize=True, progressive=True, subsampling=0)
    else:
        resize = ["-filter", "Lanczos", "-resize", f"{width}x>"] if width else []
        subprocess.run(["magick", str(png), *resize, "-strip", "-colors", "256", "-define",
                        "png:compression-level=9", str(target)], check=True)
    print(f"{target.relative_to(ASSETS)}  {target.stat().st_size // 1024} KB")


def screen_frames(tmp):
    """First (live view) and last (status panel open) frames of the screen recording."""
    recording = ASSETS / "Screenshots/system-status-swipe.webp"
    subprocess.run(["magick", str(recording), "-coalesce", str(tmp / "screen_%03d.png")], check=True)
    frames = sorted(tmp.glob("screen_*.png"))
    return frames[0], frames[-1]


# ---------------------------------------------------------------- build

WEB_ITEMS = [("#sr", "bottom"), ("#compare", "bottom"), ("#rotate", "bottom"), ("#languageToggle", "bottom"),
             ("#center", (-6, 40)), ("#capture", "top"), ("#record", "top"), ("#fps", (-18, 8.5)),
             ("#raw", (-22, 15)), (".palette-option.active", "top"), ("#settings", (240, 23.5))]
LIVE_POINTS = [(40, 16), (206, 48), (206, 94), (206, 132), (216, 195)]
PANEL_POINTS = [(-3, 22), (-3, 51), (-3, 77), (-3, 103), (62, 168), (131, 168), (200, 168)]
HERO_TILES = {"zh": ["电路板检修", "设备巡检", "插手机当摄像头", "接电脑看画面"],
              "en": ["PCB repair", "Equipment checks", "Phone camera", "On a computer"]}


def build(capture_dir, render):
    from annotate import gestures, phone_annotated, screen_annotated
    from charts import palette_chart, sr_compare
    from compose import gain_ranges, hero, how_it_works, views, web_temp_combo
    from kit import Renderer
    from mock_device import serve, gray_from_capture
    from web_shots import capture_states

    tmp = Path(tempfile.mkdtemp(prefix="t256s-images-"))
    capture_dir = Path(capture_dir)
    if str(render).startswith("http"):
        urllib.request.urlretrieve(render, tmp / "render.png")
        render = tmp / "render.png"
    source_palette = int((capture_dir / "palette.txt").read_text())
    gray_sr = gray_from_capture(capture_dir / "frame-sr.jpg", source_palette)
    gray_native = gray_from_capture(capture_dir / "frame-native.jpg", source_palette)
    live, panel = screen_frames(tmp)

    server, _ = serve(capture_dir, port=8917)
    try:
        web = {lang: capture_states("http://127.0.0.1:8917/", tmp, lang) for lang in ("zh", "en")}
    finally:
        server.shutdown()

    renderer = Renderer()
    try:
        out = {}
        for lang in ("zh", "en"):
            suffix = "" if lang == "zh" else "_en"
            tiles = [(Image.open(ASSETS / f"DCIM/{name}.jpg"), label) for name, label in
                     zip(["scene-pcb", "scene-inspection", "scene-phone", "scene-laptop"], HERO_TILES[lang])]
            out[f"DCIM/t256s-hero{suffix}.jpg"] = hero(renderer, render, tiles, tmp / f"hero-{lang}.png", lang)
            out[f"DCIM/t256s-views{suffix}.jpg"] = views(renderer, render, tmp / f"views-{lang}.png", lang)
            out[f"MISC/how-it-works{suffix}.png"] = how_it_works(renderer, render, tmp / f"flow-{lang}.png", lang)
            out[f"MISC/palettes{suffix}.jpg"] = palette_chart(renderer, gray_sr, tmp / f"palettes-{lang}.png", lang)
            out[f"MISC/sr-compare{suffix}.jpg"] = sr_compare(renderer, gray_native, gray_sr, tmp / f"sr-{lang}.png", lang)
            out[f"MISC/gain-ranges{suffix}.png"] = gain_ranges(renderer, tmp / f"gain-{lang}.png", lang)
            shot, boxes = web[lang]["main"]
            out[f"Screenshots/web-ui{suffix}.png"] = phone_annotated(renderer, shot, boxes, tmp / f"web-{lang}.png",
                                                                     lang, WEB_ITEMS)
            shot, boxes = web[lang]["temp"]
            out[f"Screenshots/web-multipoint{suffix}.png"] = web_temp_combo(renderer, shot, boxes,
                                                                            tmp / f"temp-{lang}.png", lang)
        out["Screenshots/web-compare.jpg"] = web["zh"]["compare"][0]
        out["MISC/screen-gestures.png"] = gestures(renderer, live, tmp / "gestures.png")
        out["Screenshots/screen-live.png"] = screen_annotated(renderer, live, tmp / "live.png", LIVE_POINTS)
        out["Screenshots/screen-status-panel.png"] = screen_annotated(renderer, panel, tmp / "panel.png", PANEL_POINTS)
    finally:
        renderer.close()

    for target, png in out.items():
        encode(png, ASSETS / target, quality=90 if "sr-compare" in target else 84)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    grab = commands.add_parser("capture", help="save the page and real frames from a connected T256S")
    grab.add_argument("--device", default="http://192.168.17.1")
    grab.add_argument("--out", required=True)
    make = commands.add_parser("build", help="render every image into the assets folder")
    make.add_argument("--capture", required=True)
    make.add_argument("--render", default=RENDER_URL, help="official product render (PNG with alpha)")
    args = parser.parse_args()
    if args.command == "capture":
        capture(args.device, args.out)
    else:
        build(args.capture, args.render)


if __name__ == "__main__":
    main()
