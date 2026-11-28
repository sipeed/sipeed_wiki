"""Frames and numbered callouts for real UI captures (web page and device screen)."""
from PIL import Image

from kit import data_uri

PHONE_CSS = """
.canvas { padding: 26px 34px; background: transparent; }
.phone { position: relative; width: 436px; padding: 12px; border-radius: 46px; background: #11151c;
         box-shadow: 0 0 0 2px #2a313d, 0 24px 60px rgba(17,24,39,.28); }
.screen { position: relative; border-radius: 34px; overflow: hidden; background: #080b10; }
.bar { height: 58px; display: flex; align-items: center; gap: 10px; padding: 0 16px; background: #10151d;
       border-bottom: 1px solid #1d2531; }
.url { flex: 1; height: 38px; border-radius: 19px; background: #1d2430; color: #dfe6ef; display: flex;
       align-items: center; gap: 8px; padding: 0 14px; font: 500 16px FONT; }
.url svg { width: 16px; height: 16px; color: #9aa7b8; }
.dots { width: 4px; height: 18px; background: radial-gradient(circle, #9aa7b8 2px, transparent 2.5px) 0 0/4px 6px; }
.page { position: relative; display: block; width: 412px; }
"""

WARN_ICON = ("<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2'>"
             "<path d='M12 3 2 20h20L12 3Z'/><path d='M12 10v4M12 17h.01'/></svg>")


def marker(number, x, y):
    return f"<span class='marker' style='left:{x:.1f}px;top:{y:.1f}px'>{number}</span>"


def phone_annotated(renderer, shot, boxes, out, lang, items):
    """items: list of (selector, anchor) where anchor is 'center', 'left', 'right', 'top' or (dx, dy)."""
    main = boxes["main"]
    image = Image.open(shot)
    marks = [marker(1, 336, 29)]                         # the address bar
    for number, (selector, anchor) in enumerate(items, start=2):
        x, y, w, h = boxes[selector]
        x -= main[0]
        y -= main[1]
        if anchor == "center":
            px, py = x + w / 2, y + h / 2
        elif anchor == "left":
            px, py = x - 4, y + h / 2
        elif anchor == "right":
            px, py = x + w + 4, y + h / 2
        elif anchor == "top":
            px, py = x + w / 2, y - 2
        elif anchor == "bottom":
            px, py = x + w / 2, y + h + 4
        else:
            px, py = x + anchor[0], y + anchor[1]
        marks.append(marker(number, px, py + 58))        # below the address bar
    body = (f"<div class='canvas'><div class='phone'><div class='screen'>"
            f"<div class='bar'><div class='url'>{WARN_ICON}192.168.17.1</div><span class='dots'></span></div>"
            f"<img class='page' src='{data_uri(image)}'>{''.join(marks)}</div></div></div>")
    return renderer.render(body, out, PHONE_CSS, width=560, lang=lang)


DEVICE_CSS = """
.canvas { padding: 30px 40px; }
.device { position: relative; display: inline-block; padding: 22px; border-radius: 44px;
          background: linear-gradient(145deg, #3b3f46, #15171b 55%, #0c0d10);
          box-shadow: 0 0 0 1.5px #4a4f58, inset 0 1px 0 rgba(255,255,255,.12), 0 22px 50px rgba(17,24,39,.32); }
.glass { position: relative; border-radius: 22px; overflow: hidden; background: #000;
         box-shadow: 0 0 0 5px #050506; }
.glass img { display: block; width: 560px; height: 480px; }
.glass::after { content: ""; position: absolute; inset: 0; border-radius: 22px; pointer-events: none;
                background: linear-gradient(120deg, rgba(255,255,255,.07), transparent 38%); }
"""


def screen_annotated(renderer, screen, out, points, lang="zh"):
    """screen: 560x480 capture (2x of the 280x240 UI). points: [(x, y)] in UI pixels."""
    image = Image.open(screen).convert("RGB")
    marks = "".join(marker(i + 1, 22 + x * 2, 22 + y * 2) for i, (x, y) in enumerate(points))
    body = (f"<div class='canvas'><div class='device'><div class='glass'><img src='{data_uri(image)}'></div>"
            f"{marks}</div></div>")
    return renderer.render(body, out, DEVICE_CSS, width=720, lang=lang)


GESTURE_CSS = DEVICE_CSS + """
.zone { position: absolute; left: 22px; width: 560px; z-index: 4; }
.zone.top { top: 22px; height: 56px; border-radius: 22px 22px 0 0;
            background: linear-gradient(180deg, rgba(114,228,193,.55), rgba(114,228,193,.08)); }
.zone.bottom { bottom: 22px; height: 120px; border-radius: 0 0 22px 22px;
               background: linear-gradient(0deg, rgba(255,200,87,.5), rgba(255,200,87,.06)); }
.arrow { position: absolute; z-index: 6; color: #fff; filter: drop-shadow(0 2px 6px rgba(0,0,0,.65)); }
.arrow svg { display: block; }
.tap { position: absolute; z-index: 6; width: 64px; height: 64px; margin: -32px 0 0 -32px; border-radius: 50%;
       border: 3px solid #fff; box-shadow: 0 0 0 7px rgba(255,255,255,.35), 0 4px 14px rgba(0,0,0,.5); }
.tap.double::after { content: ""; position: absolute; inset: 9px; border-radius: 50%; border: 3px solid #fff; }
"""


def arrow_svg(direction, length=96, color="#ffffff"):
    if direction in ("left-right",):
        return (f"<svg width='{length}' height='34' viewBox='0 0 {length} 34'><path d='M10 17H{length - 10}' "
                f"stroke='{color}' stroke-width='5' stroke-linecap='round'/><path d='M22 5 8 17l14 12M{length - 22} 5 "
                f"{length - 8} 17l-14 12' fill='none' stroke='{color}' stroke-width='5' stroke-linecap='round' "
                f"stroke-linejoin='round'/></svg>")
    if direction == "down":
        return (f"<svg width='34' height='{length}' viewBox='0 0 34 {length}'><path d='M17 6V{length - 10}' "
                f"stroke='{color}' stroke-width='5' stroke-linecap='round'/><path d='M5 {length - 22}l12 14 12-14' "
                f"fill='none' stroke='{color}' stroke-width='5' stroke-linecap='round' stroke-linejoin='round'/></svg>")
    return (f"<svg width='34' height='{length}' viewBox='0 0 34 {length}'><path d='M17 {length - 6}V10' "
            f"stroke='{color}' stroke-width='5' stroke-linecap='round'/><path d='M5 22 17 8l12 14' fill='none' "
            f"stroke='{color}' stroke-width='5' stroke-linecap='round' stroke-linejoin='round'/></svg>")


def gestures(renderer, screen, out):
    """Gesture guide on a real screen capture. No text: the numbers match the gesture table in the docs
    (1 double-tap, 2 swipe sideways, 3 capture, 4 pull down from the top edge, 5 swipe up from the bottom edge)."""
    image = Image.open(screen).convert("RGB")
    # positions are in the device box: screen origin at (22, 22), 2x UI scale
    overlay = (
        "<div class='zone top'></div><div class='zone bottom'></div>"
        f"<div class='tap double' style='left:{22 + 150 * 2}px;top:{22 + 104 * 2}px'></div>"
        f"<div class='arrow' style='left:{22 + 74 * 2}px;top:{22 + 152 * 2}px'>{arrow_svg('left-right', 150)}</div>"
        f"<div class='tap' style='left:{22 + 245 * 2}px;top:{22 + 195 * 2}px'></div>"
        f"<div class='arrow' style='left:{22 + 140 * 2 - 17}px;top:{22 + 2}px'>{arrow_svg('down', 70)}</div>"
        f"<div class='arrow' style='left:{22 + 140 * 2 - 17}px;top:{22 + 240 * 2 - 78}px'>{arrow_svg('up', 70)}</div>"
    )
    badges = "".join(marker(n, x, y) for n, x, y in [
        (1, 22 + 150 * 2 + 40, 22 + 104 * 2 - 36), (2, 22 + 74 * 2 - 18, 22 + 152 * 2 + 17),
        (3, 22 + 245 * 2 - 44, 22 + 195 * 2 - 30), (4, 22 + 140 * 2 + 36, 22 + 30),
        (5, 22 + 140 * 2 + 36, 22 + 240 * 2 - 40)])
    body = (f"<div class='canvas'><div class='device'><div class='glass'><img src='{data_uri(image)}'></div>"
            f"{overlay}{badges}</div></div>")
    return renderer.render(body, out, GESTURE_CSS, width=720)
