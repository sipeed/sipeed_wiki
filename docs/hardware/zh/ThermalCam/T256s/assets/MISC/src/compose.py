"""Composed explainer graphics: hero, how it works, product views, gain ranges, web multi-point combo."""
from PIL import Image

from kit import data_uri

ICONS = {
    "power": "<path d='M13 2 4 14h7l-1 8 9-12h-7l1-8Z'/>",
    "camera": "<path d='M4 7.5h3l1.4-2h7.2l1.4 2h3a2 2 0 0 1 2 2V18a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V9.5a2 2 0 0 1 2-2Z'/>"
              "<circle cx='12' cy='13.5' r='4'/>",
    "globe": "<circle cx='12' cy='12' r='9.5'/><path d='M2.5 12h19M12 2.5c3 3.2 3 15.8 0 19M12 2.5c-3 3.2-3 15.8 0 19'/>",
    "folder": "<path d='M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V7Z'/>",
    "usb": "<path d='M12 2v14M8 6l4-4 4 4M7 12v2a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2v-3M12 16v3'/><circle cx='12' cy='21' r='1.6'/>"
           "<rect x='15' y='9' width='4' height='3' rx='.5'/><circle cx='7' cy='11' r='1.5'/>",
    "screen": "<rect x='3' y='4' width='18' height='14' rx='3'/><path d='M8 21h8'/>",
}


def icon(name, size=22, color="currentColor"):
    return (f"<svg width='{size}' height='{size}' viewBox='0 0 24 24' fill='none' stroke='{color}' "
            f"stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'>{ICONS[name]}</svg>")


def render_halves(render_png):
    image = Image.open(render_png).convert("RGBA")
    left = image.crop((0, 0, 360, image.height)).crop(image.crop((0, 0, 360, image.height)).getbbox())
    right_full = image.crop((359, 0, image.width, image.height))
    right = right_full.crop(right_full.getbbox())
    return left, right


HERO_CSS = """
.canvas { width: 720px; height: 376px; background: #fff; position: relative; overflow: hidden; }
.glow { position: absolute; left: -60px; top: 40px; width: 420px; height: 340px; border-radius: 50%;
        background: radial-gradient(closest-side, rgba(255,120,60,.13), rgba(255,120,60,0)); }
.product { position: absolute; left: 22px; top: 34px; width: 330px; }
.product img { display: block; width: 330px; }
.title { position: absolute; left: 30px; top: 206px; }
.title h1 { margin: 0; font-size: 28px; letter-spacing: .3px; font-weight: 800; color: #111418; }
.title p { margin: 5px 0 12px; font-size: 14px; color: #59636e; }
.chips { display: grid; grid-template-columns: repeat(3, max-content); gap: 7px; }
.chip { padding: 5px 10px; border-radius: 99px; background: #f3f5f8; border: 1px solid #e3e8ee;
        font-size: 12.5px; color: #2b3138; white-space: nowrap; }
.chip b { color: #d8452b; font-weight: 700; }
.canvas.en .title { top: 190px; }
.canvas.en .title h1 { font-size: 22px; }
.canvas.en .chips { grid-template-columns: repeat(2, max-content); }
.tiles { position: absolute; right: 22px; top: 22px; display: grid; grid-template-columns: repeat(2, 166px);
         gap: 10px; }
.tile { position: relative; width: 166px; height: 161px; border-radius: 14px; overflow: hidden;
        box-shadow: 0 6px 18px rgba(17,24,39,.14); }
.tile img { width: 100%; height: 100%; object-fit: cover; display: block; }
.tile span { position: absolute; left: 8px; bottom: 8px; padding: 4px 9px; border-radius: 99px;
             background: rgba(15,18,24,.72); color: #fff; font-size: 12.5px; font-weight: 600; }
"""


def hero(renderer, render_png, tiles, out, lang):
    left, right = render_halves(render_png)
    pair = Image.new("RGBA", (left.width + right.width + 24, max(left.height, right.height)), (0, 0, 0, 0))
    pair.paste(left, (0, pair.height - left.height), left)
    pair.paste(right, (left.width + 24, pair.height - right.height), right)
    text = {
        "zh": ("MS-T256S 热成像相机", "机内 AI 超分，带触摸屏，插上手机电脑即用",
               ["<b>256×192</b> 热成像", "<b>2.5×</b> AI 超分", "<b>1.69″</b> 触摸屏",
                "<b>20</b> 种伪彩", "<b>UVC</b> 免驱", "<b>HTTP</b> 接口"]),
        "en": ("MS-T256S Thermal Camera", "On-device AI upscaling and a touchscreen",
               ["<b>256×192</b> thermal", "<b>2.5×</b> AI SR", "<b>1.69″</b> touch",
                "<b>20</b> palettes", "<b>UVC</b> driver-free", "<b>HTTP</b> API"]),
    }[lang]
    chips = "".join(f"<span class='chip'>{c}</span>" for c in text[2])
    tile_html = "".join(f"<div class='tile'><img src='{data_uri(img, 'JPEG', 90)}'><span>{label}</span></div>"
                        for img, label in tiles)
    body = (f"<div class='canvas {lang}'><div class='glow'></div><div class='product'><img src='{data_uri(pair)}'></div>"
            f"<div class='title'><h1>{text[0]}</h1><p>{text[1]}</p><div class='chips'>{chips}</div></div>"
            f"<div class='tiles'>{tile_html}</div></div>")
    return renderer.render(body, out, HERO_CSS, width=760, lang=lang)


FLOW_CSS = """
.canvas { width: 720px; padding: 26px 26px 24px; background: #fff; }
.grid { display: grid; grid-template-columns: 196px 1fr; column-gap: 22px; align-items: center; }
.dev { text-align: center; }
.dev img { width: 176px; display: block; margin: 0 auto 8px; }
.dev b { display: block; font-size: 16px; }
.dev span { font-size: 12.5px; color: #59636e; }
.lanes { display: flex; flex-direction: column; gap: 16px; }
.lane { position: relative; border: 1.5px solid #dfe5ec; border-radius: 16px; padding: 13px 14px 14px;
        background: #fbfcfd; }
.lane::before { content: ""; position: absolute; left: -24px; top: 50%; width: 22px; border-top: 2px dashed #b9c3cf; }
.lane-head { display: flex; align-items: center; gap: 8px; font-size: 13px; color: #59636e; margin-bottom: 9px; }
.lane-head svg { color: #8592a3; }
.cards { display: grid; gap: 8px; }
.card { background: #fff; border: 1px solid #e3e8ee; border-radius: 12px; padding: 10px 12px;
        box-shadow: 0 2px 8px rgba(17,24,39,.05); display: flex; gap: 12px; align-items: center; }
.card .ic { flex: 0 0 auto; width: 36px; height: 36px; border-radius: 10px; display: grid; place-items: center; }
.card b { display: block; font-size: 15px; margin-bottom: 2px; }
.card p { margin: 0; font-size: 12.5px; color: #59636e; line-height: 1.5; }
.card code { font-family: MONO; font-size: 11.5px; color: #1f2328; background: #f1f4f7; padding: 1px 5px;
             border-radius: 5px; }
.c-solo .ic { background: #fff1ea; color: #e2552c; }
.c-uvc .ic { background: #eaf3ff; color: #2f7be0; }
.c-web .ic { background: #e8f8f2; color: #0e9f73; }
.c-msd .ic { background: #f3eefe; color: #7a52d6; }
.solo { display: flex; gap: 12px; align-items: center; }
.solo .ic { margin: 0; flex: 0 0 auto; }
"""


def how_it_works(renderer, render_png, out, lang):
    _, right = render_halves(render_png)
    t = {
        "zh": dict(name="MS-T256S", sub="单机能用，插上手机电脑也能用",
                   solo_head="只接电源：充电宝、充电器", solo_t="单机使用",
                   solo_p="屏幕上直接看温度、切换伪彩、拍照，不需要手机或电脑。",
                   usb_head="插到手机或电脑上，下面三项同时可用",
                   uvc_t="UVC 摄像头", uvc_p="相机应用、OBS、VLC 直接预览，<code>Y16</code> 输出原始温度。",
                   web_t="网页与 HTTP 接口", web_p="浏览器打开 <code>192.168.17.1</code>；程序和 AI 也从这里取数据。",
                   msd_t="U 盘", msd_p="屏幕上拍的照片在 <code>Gallery</code> 文件夹，直接拷走。"),
        "en": dict(name="MS-T256S", sub="Standalone, or plugged into a phone or computer",
                   solo_head="Power only: a power bank or charger", solo_t="Standalone",
                   solo_p="Read temperatures, switch palettes and take photos on the screen, with no phone or "
                          "computer needed.",
                   usb_head="Plugged into a phone or computer, all three work at once",
                   uvc_t="UVC camera", uvc_p="Preview in camera apps, OBS or VLC without a driver; the <code>Y16</code> "
                                            "format carries raw temperatures.",
                   web_t="Web page & HTTP API", web_p="Open <code>192.168.17.1</code> in a browser to view and measure; "
                                                     "programs and AI tools read data here too.",
                   msd_t="USB drive", msd_p="Photos taken on the screen are in the <code>Gallery</code> folder."),
    }[lang]
    body = (
        "<div class='canvas'><div class='grid'>"
        f"<div class='dev'><img src='{data_uri(right)}'><b>{t['name']}</b><span>{t['sub']}</span></div>"
        "<div class='lanes'>"
        f"<div class='lane'><div class='lane-head'>{icon('power', 16)}{t['solo_head']}</div>"
        f"<div class='card c-solo solo'><div class='ic'>{icon('screen')}</div><div><b>{t['solo_t']}</b>"
        f"<p>{t['solo_p']}</p></div></div></div>"
        f"<div class='lane'><div class='lane-head'>{icon('usb', 16)}{t['usb_head']}</div><div class='cards'>"
        f"<div class='card c-uvc'><div class='ic'>{icon('camera')}</div><div><b>{t['uvc_t']}</b><p>{t['uvc_p']}</p></div></div>"
        f"<div class='card c-web'><div class='ic'>{icon('globe')}</div><div><b>{t['web_t']}</b><p>{t['web_p']}</p></div></div>"
        f"<div class='card c-msd'><div class='ic'>{icon('folder')}</div><div><b>{t['msd_t']}</b><p>{t['msd_p']}</p></div></div>"
        "</div></div></div></div></div>")
    return renderer.render(body, out, FLOW_CSS, width=760, lang=lang)


VIEWS_CSS = """
.canvas { width: 720px; height: 404px; position: relative; background: #fff; }
.canvas img { position: absolute; left: 24px; top: 66px; width: 672px; }
.label { position: absolute; font-size: 14px; font-weight: 600; color: #1f2328; white-space: nowrap; }
.label small { display: block; font-size: 12px; font-weight: 400; color: #59636e; margin-top: 1px; }
svg.lines { position: absolute; inset: 0; }
"""


def views(renderer, render_png, out, lang):
    image = Image.open(render_png).convert("RGBA")
    scale = 672 / image.width                       # rendered image is 672 CSS px wide
    ox, oy = 24, 66

    def at(px, py):
        return ox + px * scale, oy + py * scale

    # anchor points measured on the official render (source pixels)
    anchors = {"lens": (207, 141), "plug": (72, 212), "port": (272, 200), "screen": (560, 92)}
    names = {
        "zh": {"lens": ("热成像镜头", "镜头面"), "plug": ("USB-C 公头", "直接插手机或电脑"),
               "port": ("USB-C 母口", "接线到电脑，或接电源"), "screen": ("1.69 英寸触摸屏", "屏幕面")},
        "en": {"lens": ("Thermal lens", "lens side"), "plug": ("USB-C plug", "into a phone or computer"),
               "port": ("USB-C port", "cable to a computer, or power"), "screen": ("1.69″ touchscreen", "screen side")},
    }[lang]
    layout = [("lens", (150, 14), "lens"), ("screen", (500, 14), "screen"), ("plug", (24, 356), "plug"),
              ("port", (292, 356), "port")]
    lines, labels = [], []
    for key, (lx, ly), anchor in layout:
        ax, ay = at(*anchors[anchor])
        tx, ty = lx + 6, ly + (40 if ly < 100 else -6)
        lines.append(f"<path d='M{tx:.0f} {ty:.0f} L{ax:.0f} {ay:.0f}' stroke='#e5383b' stroke-width='1.6' fill='none'/>"
                     f"<circle cx='{ax:.0f}' cy='{ay:.0f}' r='4.5' fill='#e5383b' stroke='#fff' stroke-width='2'/>")
        title, sub = names[key]
        labels.append(f"<div class='label' style='left:{lx}px;top:{ly}px'>{title}<small>{sub}</small></div>")
    body = (f"<div class='canvas'><img src='{data_uri(image)}'><svg class='lines' width='720' height='404'>"
            f"{''.join(lines)}</svg>{''.join(labels)}</div>")
    return renderer.render(body, out, VIEWS_CSS, width=760, lang=lang)


GAIN_CSS = """
.canvas { width: 600px; padding: 16px 20px 10px; background: #fff; }
.axis { position: relative; height: 172px; }
.bar { position: absolute; z-index: 2; height: 40px; border-radius: 10px; display: flex; align-items: center;
       gap: 8px; padding: 0 12px; color: #fff; font-size: 15px; font-weight: 600; white-space: nowrap; }
.bar b { font-weight: 800; letter-spacing: .5px; }
.bar small { font-size: 14px; font-weight: 500; opacity: .92; margin-left: 4px; }
.hi { top: 30px; background: linear-gradient(90deg, #1f9e8c, #36c2a6); }
.lo { top: 84px; background: linear-gradient(90deg, #e2552c, #f39a3a); }
.side { position: absolute; top: 30px; height: 40px; display: flex; align-items: center; font-size: 14px;
        color: #39424d; white-space: nowrap; }
.base { position: absolute; top: 142px; left: 0; right: 0; height: 1px; background: #c5ced8; }
.tick { position: absolute; top: 142px; width: 1px; height: 7px; background: #8592a3; }
.tn { position: absolute; top: 151px; transform: translateX(-50%); font: 600 13px MONO; color: #59636e; }
.unit { position: absolute; top: 151px; right: 0; font: 600 13px MONO; color: #59636e; }
.thr { position: absolute; z-index: 1; top: 8px; height: 134px; border-left: 2px dashed #39424d; }
.thr span { position: absolute; top: -6px; left: 6px; font: 700 13px MONO; color: #39424d; background: #fff;
            padding: 0 3px; white-space: nowrap; }
"""


def gain_ranges(renderer, out, lang):
    """The two measurement ranges; the page text explains the switching rule next to it."""
    lo_t, hi_t = -40, 540
    span = 548

    def x(t):
        return (t - lo_t) / (hi_t - lo_t) * span

    t = {
        "zh": dict(hi="-15 ~ 150&nbsp;℃", lo="50 ~ 500&nbsp;℃", hi_note="高增益：默认档位，精度更高",
                   lo_note="低增益：量程更大", thr="130&nbsp;℃", unit="℃"),
        "en": dict(hi="-15 to 150 °C", lo="50 to 500 °C", hi_note="High gain: the default, more accurate",
                   lo_note="Low gain: wider range", thr="130 °C", unit="°C"),
    }[lang]
    ticks = "".join(f"<i class='tick' style='left:{x(v):.1f}px'></i><span class='tn' style='left:{x(v):.1f}px'>{v}</span>"
                    for v in (-15, 50, 150, 300, 500))
    body = (
        "<div class='canvas'><div class='axis'><i class='base'></i>"
        f"<div class='bar hi' style='left:{x(-15):.1f}px;width:{x(150) - x(-15):.1f}px'><b>HI</b>{t['hi']}</div>"
        f"<div class='side' style='left:{x(150) + 14:.1f}px'>{t['hi_note']}</div>"
        f"<div class='bar lo' style='left:{x(50):.1f}px;width:{x(500) - x(50):.1f}px'><b>LO</b>{t['lo']}"
        f"<small>{t['lo_note']}</small></div>"
        f"<div class='thr' style='left:{x(130):.1f}px'><span>{t['thr']}</span></div>"
        f"{ticks}<span class='unit'>{t['unit']}</span></div></div>")
    return renderer.render(body, out, GAIN_CSS, width=640, lang=lang)


COMBO_CSS = """
.canvas { width: 720px; padding: 18px; background: #080b10; border-radius: 0; display: flex; gap: 16px;
          align-items: flex-start; }
.canvas img { display: block; border-radius: 14px; }
"""


def web_temp_combo(renderer, shot, boxes, out, lang):
    image = Image.open(shot)
    main = boxes["main"]
    viewer = boxes["#viewer"]
    tools = boxes["#rawTools"]
    head = boxes["aside.panel"]

    def crop(box, pad=0):
        x, y, w, h = box
        return image.crop((int((x - main[0] - pad) * 2), int((y - main[1] - pad) * 2),
                           int((x - main[0] + w + pad) * 2), int((y - main[1] + h + pad) * 2)))

    left = crop(viewer)
    right_top = image.crop((int((head[0] - main[0]) * 2), int((head[1] - main[1]) * 2),
                            int((head[0] - main[0] + head[2]) * 2), int((tools[1] - main[1]) * 2)))
    right = crop(tools)
    lw = 330
    rw = 338
    body = (f"<div class='canvas'><img src='{data_uri(left)}' style='width:{lw}px'>"
            f"<div><img src='{data_uri(right_top)}' style='width:{rw}px;margin-bottom:10px'>"
            f"<img src='{data_uri(right)}' style='width:{rw}px'></div></div>")
    return renderer.render(body, out, COMBO_CSS, width=760, lang=lang)
