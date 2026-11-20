"""Data-driven charts built from real T256S captures: palette chart and SR comparison."""
import numpy as np
from PIL import Image

from kit import data_uri
from palettes import NAMES, NAMES_ZH, load_luts

LUTS = load_luts()

DARK_CSS = """
.canvas { background: #0b0f16; padding: 22px; color: #e8edf4; }
"""

PALETTE_CSS = DARK_CSS + """
.grid { display: grid; grid-template-columns: repeat(5, 128px); gap: 14px; }
.tile { background: #141b26; border: 1px solid #263244; border-radius: 14px; padding: 7px 7px 9px; }
.tile img { display: block; width: 112px; height: 149px; border-radius: 9px; margin: 0 auto; }
.name { margin-top: 7px; text-align: center; font-size: 14.5px; font-weight: 700; color: #f2f5f9; }
.alt { text-align: center; font-size: 11.5px; color: #8c9bb0; margin-top: 1px; }
.no { position: absolute; margin: 5px 0 0 5px; min-width: 21px; height: 21px; padding: 0 5px; border-radius: 11px;
      background: rgba(8,11,16,.78); color: #dce3ec; font: 700 11.5px/21px MONO; text-align: center; }
"""


def palette_chart(renderer, gray_sr, out, lang):
    tiles = []
    for index, lut in enumerate(LUTS):
        image = Image.fromarray(lut[gray_sr]).resize((224, 298), Image.LANCZOS)
        if lang == "zh":
            label = f"<div class='name'>{NAMES_ZH[index]}</div><div class='alt'>{NAMES[index]}</div>"
        else:
            label = f"<div class='name'>{NAMES[index]}</div>"
        tiles.append(f"<div class='tile'><span class='no'>{index + 1}</span>"
                     f"<img src='{data_uri(image)}'>{label}</div>")
    body = f"<div class='canvas'><div class='grid'>{''.join(tiles)}</div></div>"
    return renderer.render(body, out, PALETTE_CSS, width=760, lang=lang)


COMPARE_CSS = DARK_CSS + """
.row { display: flex; gap: 18px; }
.panel { position: relative; width: 324px; }
.frame { position: relative; width: 324px; height: 432px; border-radius: 14px; overflow: hidden; }
.frame img.full { display: block; width: 324px; height: 432px; }
.pixelated { image-rendering: pixelated; }
.pill { position: absolute; left: 12px; top: 12px; padding: 6px 12px; border-radius: 99px; z-index: 3;
        background: rgba(8,11,16,.8); font-size: 15px; font-weight: 700; letter-spacing: .1px; }
.pill b { color: #72e4c1; font-family: MONO; font-weight: 700; margin-left: 6px; }
.lens { position: absolute; width: 168px; height: 168px; border-radius: 50%; overflow: hidden; z-index: 2;
        border: 3px solid #fff; box-shadow: 0 8px 28px rgba(0,0,0,.6); }
.lens img { position: absolute; }
.spot { position: absolute; border: 2px dashed rgba(255,255,255,.9); border-radius: 50%; z-index: 2; }
.caption { margin-top: 12px; font-size: 13.5px; color: #a9b6c7; line-height: 1.5; }
"""


def sr_compare(renderer, gray_native, gray_sr, out, lang, palette="Ironbow", focus=(146, 132), zoom=3.2):
    lut = LUTS[NAMES.index(palette)]
    native = Image.fromarray(lut[gray_native])                    # 192 x 256
    sr = Image.fromarray(lut[gray_sr])                            # 480 x 640
    shown = 324 / 480                                             # CSS px per SR px
    fx, fy = focus                                                # in SR pixel coordinates
    lens = 168
    src_box = lens / zoom / shown                                 # SR px covered by the lens

    def panel(image, pixelated, title, size, caption):
        cls = "full pixelated" if pixelated else "full"
        big_w = 324 * zoom
        left = -(fx * shown * zoom - lens / 2)
        top = -(fy * shown * zoom - lens / 2)
        lx, ly = 324 - lens - 14, 432 - lens - 14
        spot_d = src_box * shown
        return (f"<div class='panel'><div class='frame'>"
                f"<img class='{cls}' src='{data_uri(image)}'>"
                f"<span class='pill'>{title}<b>{size}</b></span>"
                f"<span class='spot' style='left:{fx * shown - spot_d / 2:.1f}px;top:{fy * shown - spot_d / 2:.1f}px;"
                f"width:{spot_d:.1f}px;height:{spot_d:.1f}px'></span>"
                f"<div class='lens' style='left:{lx}px;top:{ly}px'><img class='{cls.replace('full', '')}' "
                f"src='{data_uri(image)}' style='width:{big_w:.1f}px;left:{left:.1f}px;top:{top:.1f}px'></div>"
                f"</div><div class='caption'>{caption}</div></div>")

    if lang == "zh":
        left = panel(native, True, "原生画面", "256 × 192", "传感器原始分辨率，放大显示时能看到明显的像素块。")
        right = panel(sr, False, "AI 超分", "640 × 480", "同一时刻的设备端超分输出，边缘和细节更清楚。")
    else:
        left = panel(native, True, "Native", "256 × 192", "Sensor resolution. Enlarged, the pixels show.")
        right = panel(sr, False, "AI super resolution", "640 × 480", "On-device output of the same moment, with cleaner edges.")
    body = f"<div class='canvas'><div class='row'>{left}{right}</div></div>"
    return renderer.render(body, out, COMPARE_CSS, width=760, lang=lang)
