#!/usr/bin/env python3
"""Generates the SPI2HDMI pinout and wiring diagrams (zh + _en). Run: python3 gen_diagrams.py"""
FONT = 'font-family="Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, PingFang SC, Arial, sans-serif"'
INK, MUTED, BOARD, PADC, LINE = '#1f2933', '#5b6770', '#1f7a4d', '#e6c36a', '#c5ccd3'
WIRE = {'5V': '#d64545', 'GND': '#30363d', 'SCK': '#e08a1e', 'CS': '#7a52c7', 'RST': '#8a8f98',
        'IO0': '#1f77c9', 'IO1': '#16a085', 'IO2': '#c0397b', 'IO3': '#8d6e3f', 'TE': '#5f8f1f'}
LEFT, RIGHT = ['5V', 'GND', 'SCK', 'CS', 'RST'], ['IO0', 'IO1', 'IO2', 'IO3', 'TE']

def T(zh, en): return {'zh': zh, 'en': en}
def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" {FONT}>'
            f'<rect width="{w}" height="{h}" fill="#ffffff"/>{body}</svg>\n')
def text(x, y, s, size=15, anchor='start', fill=INK, weight='normal'):
    s = str(s).replace('&', '&amp;').replace('<', '&lt;')
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{fill}" font-weight="{weight}">{s}</text>'

# Board geometry from the PCB (mil): 900 x 805, the two corners at the HDMI end are chamfered,
# headers at x=10/810 with pins at y=550..150, HDMI socket 590 wide overhanging the top edge by 76.
MIL = 229 / 900.0
def module(x, y, s=1.0, labels=True):
    """Top view of the module (HDMI socket up). Returns (svg, {pin: (px, py)})."""
    k = MIL * s
    X = lambda mil: x + (mil + 40) * k
    Y = lambda mil: y + (805 - mil) * k
    outline = [(-40, 0), (860, 0), (860, 609.3), (705.3, 805), (114.7, 805), (-40, 609.3)]
    o = ['<polygon points="' + ' '.join(f'{X(a):.1f},{Y(b):.1f}' for a, b in outline) + f'" fill="{BOARD}" stroke-linejoin="round" stroke="{BOARD}" stroke-width="{4*s}"/>']
    cx0, cx1, cy0, cy1 = X(115), X(705), Y(881), Y(455)
    o.append(f'<rect x="{cx0:.1f}" y="{cy0:.1f}" width="{cx1 - cx0:.1f}" height="{cy1 - cy0:.1f}" rx="{5*s}" fill="#c9ced4" stroke="#8b939b" stroke-width="{1.5*s}"/>')
    o.append(f'<rect x="{cx0 + 14*s:.1f}" y="{cy0 + 9*s:.1f}" width="{cx1 - cx0 - 28*s:.1f}" height="{28*s}" rx="{3*s}" fill="#3a4047"/>')
    o.append(text((cx0 + cx1) / 2, cy0 + 72 * s, 'HDMI', 15 * s, 'middle', '#4a5158', 'bold'))
    o.append(text((cx0 + cx1) / 2, Y(52), 'SPI2HDMI', 17 * s, 'middle', '#f3d98b', 'bold'))
    pins = {}
    for col, names in ((0, LEFT), (1, RIGHT)):
        px = X(10 if col == 0 else 810)
        for i, n in enumerate(names):
            py = Y(550 - i * 100)
            o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{8.5*s}" fill="{PADC}" stroke="#8a6d1f" stroke-width="{1.2*s}"/><circle cx="{px:.1f}" cy="{py:.1f}" r="{3.6*s}" fill="#ffffff"/>')
            if labels:      # pill background keeps the name readable where the HDMI socket is close
                lw = (len(n) * 7.6 + 8) * s; lx = px + 12 * s if col == 0 else px - 12 * s - lw
                o.append(f'<rect x="{lx:.1f}" y="{py - 8.5 * s:.1f}" width="{lw:.1f}" height="{17 * s}" rx="{4 * s}" fill="{BOARD}"/>')
                o.append(text(lx + lw / 2, py + 4.2 * s, n, 11.5 * s, 'middle', '#ffffff', 'bold'))
            pins[n] = (px, py)
    return ''.join(o), pins

def dimensions(lang):
    """Mechanical outline with the real board shape (no pin names: shared look, two languages)."""
    W, H = 760, 610; k = 0.42; x0, y0 = 190, 140
    X = lambda mil: x0 + (mil + 40) * k
    Y = lambda mil: y0 + (805 - mil) * k
    RED = '#d6453d'
    outline = [(-40, 0), (860, 0), (860, 609.3), (705.3, 805), (114.7, 805), (-40, 609.3)]
    o = [text(W / 2, 34, T('SPI2HDMI 模块尺寸（顶视图）', 'SPI2HDMI dimensions (top view)')[lang], 20, 'middle', INK, 'bold'),
         '<polygon points="' + ' '.join(f'{X(a):.1f},{Y(b):.1f}' for a, b in outline) + f'" fill="#ffffff" stroke="{INK}" stroke-width="2"/>',
         f'<rect x="{X(115):.1f}" y="{Y(881):.1f}" width="{590 * k:.1f}" height="{426 * k:.1f}" rx="4" fill="#f1f3f5" stroke="{INK}" stroke-width="1.5"/>',
         text(X(410), Y(668), 'HDMI', 15, 'middle', MUTED)]
    for px in (10, 810):
        for i in range(5):
            o.append(f'<circle cx="{X(px):.1f}" cy="{Y(550 - i * 100):.1f}" r="7" fill="#ffffff" stroke="{INK}" stroke-width="1.5"/>')
    def dim(x1, y1, x2, y2, label, dx=0, dy=-8, anchor='middle'):
        o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{RED}" stroke-width="1.5"/>')
        for (a, b) in ((x1, y1), (x2, y2)): o.append(f'<circle cx="{a:.1f}" cy="{b:.1f}" r="3" fill="{RED}"/>')
        o.append(text((x1 + x2) / 2 + dx, (y1 + y2) / 2 + dy, label, 14, anchor, RED))
    def ext(x1, y1, x2, y2): o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{RED}" stroke-width="0.8" stroke-dasharray="4 3"/>')
    yb = Y(0) + 44; ext(X(-40), Y(0), X(-40), yb + 6); ext(X(860), Y(0), X(860), yb + 6)
    dim(X(-40), yb, X(860), yb, '22.86 mm', dy=20)
    xl = X(-40) - 44; ext(X(-40), Y(0), xl - 6, Y(0)); ext(X(114.7), Y(805), xl - 6, Y(805))
    dim(xl, Y(805), xl, Y(0), '20.45 mm', dx=-10, dy=5, anchor='end')
    dim(X(10), Y(80), X(810), Y(80), T('20.32 mm (800 mil) 排针间距', '20.32 mm (800 mil) between rows')[lang])
    xr = X(860) + 34; ext(X(810), Y(550), xr + 6, Y(550)); ext(X(810), Y(450), xr + 6, Y(450))
    dim(xr, Y(550), xr, Y(450), '2.54 mm', dx=10, dy=5, anchor='start')
    xr2 = X(860) + 34; ext(X(810), Y(150), xr2 + 6, Y(150)); ext(X(860), Y(0), xr2 + 6, Y(0))
    dim(xr2, Y(150), xr2, Y(0), '3.81 mm', dx=10, dy=5, anchor='start')
    yt = Y(881) - 22; ext(X(115), Y(881), X(115), yt - 6); ext(X(705), Y(881), X(705), yt - 6)
    dim(X(115), yt, X(705), yt, T('15 mm（HDMI 座，伸出板边约 1.9 mm）', '15 mm (HDMI socket, overhangs the edge by about 1.9 mm)')[lang])
    return svg(W, H, ''.join(o))

def pinout(lang):
    W, H = 980, 424
    m, pins = module(376, 96, 1.0)
    o = [text(W / 2, 34, T('SPI2HDMI 引脚定义（顶视图，HDMI 座朝上）', 'SPI2HDMI pinout (top view, HDMI socket up)')[lang], 20, 'middle', INK, 'bold'), m]
    desc = {
        '5V': T('5V 供电输入', '5 V power input'), 'GND': T('地', 'Ground'), 'SCK': T('时钟', 'Clock'),
        'CS': T('片选，低有效', 'Chip select, active low'), 'RST': T('复位，低有效（可悬空）', 'Reset, active low (may be left open)'),
        'IO0': T('SPI：MOSI ｜ QSPI：D0', 'SPI: MOSI | QSPI: D0'), 'IO1': T('SPI：D/C ｜ QSPI：D1', 'SPI: D/C | QSPI: D1'),
        'IO2': T('SPI：不用 ｜ QSPI：D2', 'SPI: unused | QSPI: D2'), 'IO3': T('SPI：悬空 ｜ QSPI：D3（兼模式选择）', 'SPI: open | QSPI: D3 (also mode select)'),
        'TE': T('帧同步输出（可不接）', 'Frame-sync output (optional)')}
    for n in LEFT + RIGHT:
        px, py = pins[n]; left = n in LEFT
        x2 = 350 if left else 630
        o.append(f'<line x1="{px + (-10 if left else 10)}" y1="{py}" x2="{x2}" y2="{py}" stroke="{WIRE[n]}" stroke-width="2.5"/>')
        o.append(f'<rect x="{x2 - 58 if left else x2}" y="{py - 13}" width="58" height="26" rx="5" fill="{WIRE[n]}"/>')
        o.append(text(x2 - 29 if left else x2 + 29, py + 5, n, 14, 'middle', '#ffffff', 'bold'))
        o.append(text(x2 - 68 if left else x2 + 68, py + 5, desc[n][lang], 14, 'end' if left else 'start'))
    o.append(text(W / 2, 372, T('板子 22.86 × 20.45 mm ｜ 两排排针相距 20.32 mm (800 mil) ｜ 针距 2.54 mm', 'Board 22.86 × 20.45 mm | header rows 20.32 mm (800 mil) apart | 2.54 mm pitch')[lang], 14, 'middle', MUTED))
    o.append(text(W / 2, 398, T('供电 5V ｜ 信号电平 3.3V', '5 V supply | 3.3 V signal level')[lang], 14, 'middle', MUTED))
    return svg(W, H, ''.join(o))

def wiring(lang, title, host_name, links, note):
    """links: [(host_label, module_pin)].  The host pins are laid out so that no two wires cross:
    left-header pins sit level with the module, right-header pins are nested underneath."""
    PITCH = 25.4
    left = [l for l in links if l[1] in LEFT]; right = [l for l in links if l[1] in RIGHT]
    left.sort(key=lambda l: LEFT.index(l[1])); right.sort(key=lambda l: -RIGHT.index(l[1]))
    W = 980; mx, my = 560, 96
    m, pins = module(mx, my, 1.0)
    hx, hw = 70, 240
    y_first = pins[LEFT[0]][1]
    # host rows: one per left-header pin of the module (level with it), then the right-header group
    rows = [(n, None) for n in LEFT]
    for h, mp in left: rows[LEFT.index(mp)] = (mp, h)
    gap = 1
    hy = y_first - 56
    hh = 56 + (len(LEFT) + gap + len(right)) * PITCH
    H = int(hy + hh + 30 + len(right) * 11 + 66)
    o = [text(W / 2, 34, title[lang], 20, 'middle', INK, 'bold'),
         f'<rect x="{hx}" y="{hy}" width="{hw}" height="{hh}" rx="10" fill="#f4f6f8" stroke="{LINE}" stroke-width="2"/>',
         text(hx + hw / 2, hy + 28, host_name[lang], 16, 'middle', INK, 'bold'), m]
    def host_pin(py, label):
        return (f'<circle cx="{hx + hw}" cy="{py}" r="5.5" fill="#ffffff" stroke="{INK}" stroke-width="1.5"/>'
                + text(hx + hw - 14, py + 5, label[lang] if isinstance(label, dict) else label, 14, 'end'))
    for i, (mp, h) in enumerate(rows):
        if h is None: continue
        py = y_first + i * PITCH
        o.append(host_pin(py, h))
        o.append(f'<line x1="{hx + hw + 6}" y1="{py}" x2="{pins[mp][0] - 9}" y2="{pins[mp][1]}" stroke="{WIRE[mp]}" stroke-width="3"/>')
    n = len(right)
    for k, (h, mp) in enumerate(right):
        py = y_first + (len(LEFT) + gap + k) * PITCH
        o.append(host_pin(py, h))
        x_drop = hx + hw + 30 + (n - 1 - k) * 12          # upper pins drop further right
        y_low = hy + hh + 18 + k * 11                      # lower pins run deeper
        x_up = mx + 229 + 20 + k * 11                      # deeper wires come up further out
        x2, y2 = pins[mp]
        o.append(f'<path d="M{hx + hw + 6} {py} H{x_drop} V{y_low} H{x_up} V{y2} H{x2 + 9}" fill="none" stroke="{WIRE[mp]}" stroke-width="3" stroke-linejoin="round"/>')
    o.append(text(W / 2, H - 22, note[lang], 14, 'middle', MUTED))
    return svg(W, H, ''.join(o))

def features(lang, cols=3):
    CW, CH, G, M = 300, 210, 18, 22
    rows_n = 6 // cols
    W, H = M * 2 + CW * cols + G * (cols - 1), M * 2 + CH * rows_n + G * (rows_n - 1)
    ACC, SOFT = '#d6453d', '#fdf1ef'
    def monitor(x, y, w, h, fill='#1f2933'):
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}"/>'
                f'<rect x="{x + w / 2 - 14}" y="{y + h}" width="28" height="7" fill="#8b939b"/>'
                f'<rect x="{x + w / 2 - 26}" y="{y + h + 7}" width="52" height="4" rx="2" fill="#8b939b"/>')
    def art(i, x, y):
        cx = x + CW / 2
        if i == 0:   # ILI9341 commands -> monitor
            o = ''.join(f'<rect x="{x + 34}" y="{y + 26 + k * 26}" width="74" height="20" rx="4" fill="{SOFT}" stroke="{ACC}"/>'
                        + text(x + 71, y + 41 + k * 26, c, 13, 'middle', ACC, 'bold') for k, c in enumerate(['0x2A', '0x2B', '0x2C']))
            o += f'<path d="M{x + 120} {y + 62} h36" stroke="{INK}" stroke-width="3"/><path d="M{x + 152} {y + 55} l10 7 l-10 7 z" fill="{INK}"/>'
            o += monitor(x + 172, y + 28, 96, 62)
            cols = ['#ffffff', '#ffe600', '#00d5e6', '#1fc24a', '#d83bd2', '#e23b3b', '#2f63e0']
            o += ''.join(f'<rect x="{x + 178 + k * 12}" y="{y + 34}" width="12" height="50" fill="{c}"/>' for k, c in enumerate(cols))
            return o
        if i == 1:   # SPI / QSPI
            o = f'<rect x="{x + 30}" y="{y + 22}" width="110" height="84" rx="8" fill="{SOFT}" stroke="{ACC}"/>' + text(x + 85, y + 44, 'SPI', 15, 'middle', ACC, 'bold')
            o += f'<path d="M{x + 46} {y + 62} h78" stroke="#1f77c9" stroke-width="4"/>' + text(x + 85, y + 94, '80 MHz', 14, 'middle', INK, 'bold')
            o += f'<rect x="{x + 160}" y="{y + 22}" width="110" height="84" rx="8" fill="{SOFT}" stroke="{ACC}"/>' + text(x + 215, y + 44, 'QSPI', 15, 'middle', ACC, 'bold')
            o += ''.join(f'<path d="M{x + 176} {y + 53 + k * 7} h78" stroke="{c}" stroke-width="4"/>' for k, c in enumerate(['#1f77c9', '#16a085', '#c0397b', '#8d6e3f']))
            o += text(x + 215, y + 99, '40 MHz', 14, 'middle', INK, 'bold')
            return o
        if i == 2:   # two outputs
            o = monitor(x + 34, y + 38, 84, 58) + text(x + 76, y + 64, '640×480', 13, 'middle', '#ffffff', 'bold') + text(x + 76, y + 82, '60 Hz', 12, 'middle', '#c5ccd3')
            o += monitor(x + 142, y + 24, 128, 72) + text(x + 206, y + 56, '1280×720', 14, 'middle', '#ffffff', 'bold') + text(x + 206, y + 76, '30 Hz', 12, 'middle', '#c5ccd3')
            return o
        if i == 3:   # zoom
            px = ['#e23b3b', '#ffe600', '#1fc24a', '#2f63e0']
            o = ''.join(f'<rect x="{x + 40 + (k % 2) * 14}" y="{y + 50 + (k // 2) * 14}" width="14" height="14" fill="{c}"/>' for k, c in enumerate(px))
            o += f'<path d="M{x + 82} {y + 64} h34" stroke="{INK}" stroke-width="3"/><path d="M{x + 112} {y + 57} l10 7 l-10 7 z" fill="{INK}"/>'
            o += ''.join(f'<rect x="{x + 136 + (k % 2) * 42}" y="{y + 22 + (k // 2) * 42}" width="42" height="42" fill="{c}"/>' for k, c in enumerate(px))
            o += text(x + 250, y + 58, '×2 ×4', 14, 'middle', ACC, 'bold') + text(x + 250, y + 80, '×8 ×16', 14, 'middle', ACC, 'bold')
            return o
        if i == 4:   # colour depths
            # Schematic, not literal: smooth = full colour, 16 bands = "fewer colours", 4 greys, 2 levels
            N = 88
            rows = [('RGB565', [_hex(*_hue(i / (N - 1))) for i in range(N)]),
                    (T('256 色', '256 col')[lang], [_hex(*_hue(i / 15)) for i in range(16)]),
                    (T('灰度', 'Grey')[lang], ['#000000', '#555555', '#aaaaaa', '#ffffff']),
                    (T('黑白', 'Mono')[lang], ['#000000', '#ffffff'])]
            o = ''
            for r, (name, cols) in enumerate(rows):
                yy = y + 20 + r * 23; cw = 176 / len(cols)
                o += text(x + 84, yy + 14, name, 12.5, 'end', INK, 'bold')
                o += ''.join(f'<rect x="{x + 94 + k * cw:.2f}" y="{yy}" width="{cw + 0.4:.2f}" height="18" fill="{c}"/>' for k, c in enumerate(cols))
                o += f'<rect x="{x + 94}" y="{yy}" width="176" height="18" fill="none" stroke="#c5ccd3" stroke-width="0.6"/>'
            return o
        # HDMI audio
        o = f'<path d="M{x + 52} {y + 52} h22 l26 -22 v68 l-26 -22 h-22 z" fill="{INK}"/>'
        o += ''.join(f'<path d="M{x + 112 + k * 14} {y + 64 - 14 - k * 9} q{12 + k * 5} {14 + k * 9} 0 {28 + k * 18}" fill="none" stroke="{ACC}" stroke-width="4" stroke-linecap="round"/>' for k in range(3))
        import math
        pts = ' '.join(f'{x + 176 + t * 2:.1f},{y + 64 - 22 * math.sin(t / 5.2) * (0.55 + 0.45 * math.sin(t / 17)):.1f}' for t in range(48))
        o += f'<polyline points="{pts}" fill="none" stroke="#1f77c9" stroke-width="3"/>'
        return o
    cells = [
        (T('兼容 ILI9341 指令', 'ILI9341-compatible'), T('现有 SPI 屏驱动改个分辨率就能用', 'Reuse your SPI display driver')),
        (T('SPI / QSPI 双模式', 'SPI and QSPI'), T('4 线 SPI 接线少，QSPI 刷新快', 'Fewer wires, or faster refresh')),
        (T('两种分辨率输出', 'Two output resolutions'), T('运行时可切换', 'Switchable at run time')),
        (T('像素整数放大', 'Integer pixel zoom'), T('小内存单片机也能铺满屏幕', 'Small MCUs can fill the screen')),
        (T('多种色深', 'Several colour depths'), T('从 65536 色到黑白，按需取舍', 'From 65,536 colours to monochrome')),
        (T('HDMI 音频', 'HDMI audio'), T('48kHz 16 位单声道，随画面输出', '48 kHz 16-bit mono with the picture')),
    ]
    o = []
    for i, (title, sub) in enumerate(cells):
        x = M + (i % cols) * (CW + G); y = M + (i // cols) * (CH + G)
        o.append(f'<rect x="{x}" y="{y}" width="{CW}" height="{CH}" rx="14" fill="#ffffff" stroke="#e3e7eb" stroke-width="1.5"/>')
        o.append(f'<rect x="{x}" y="{y}" width="{CW}" height="128" rx="14" fill="#f6f8fa"/><rect x="{x}" y="{y + 100}" width="{CW}" height="28" fill="#f6f8fa"/>')
        o.append(art(i, x, y))
        o.append(text(x + CW / 2, y + 160, title[lang], 18, 'middle', INK, 'bold'))
        o.append(text(x + CW / 2, y + 186, sub[lang], 13.5, 'middle', MUTED))
    return svg(W, H, ''.join(o))

FIGS = {
 'dimensions': dimensions,
 'features': features,
 'pinout': pinout,
 'wiring-ch32v003': lambda l: wiring(l, T('CH32V003 接线（SPI 模式）', 'CH32V003 wiring (SPI mode)'),
    T('CH32V003（3.3V 供电）', 'CH32V003 (3.3 V supply)'),
    [('5V', '5V'), ('GND', 'GND'), ('PC5 (SCK)', 'SCK'), ('PC4', 'CS'), (T('任意 GPIO（可选）', 'Any GPIO (optional)'), 'RST'), ('PC6 (MOSI)', 'IO0'), ('PC3', 'IO1'), (T('PD0（可选）', 'PD0 (optional)'), 'TE')],
    T('单片机须工作在 3.3V；5V 取自开发板的 USB 5V 引脚；RST 和 TE 可不接，IO2、IO3 悬空', 'Run the MCU at 3.3 V; take 5 V from the board\'s USB 5V pin; RST and TE are optional, leave IO2 and IO3 open')),
 'wiring-esp32s3': lambda l: wiring(l, T('ESP32-S3 接线（SPI / QSPI 通用）', 'ESP32-S3 wiring (works for SPI and QSPI)'),
    T('ESP32-S3 开发板', 'ESP32-S3 dev board'),
    [('5V', '5V'), ('GND', 'GND'), ('GPIO12', 'SCK'), ('GPIO10', 'CS'), ('GPIO8', 'RST'), ('GPIO11', 'IO0'), ('GPIO13', 'IO1'), ('GPIO14', 'IO2'), ('GPIO9', 'IO3'), ('GPIO3', 'TE')],
    T('例程会自己控制 IO3 和 RST 来切换 SPI / QSPI，一套接线两种模式都能用', 'The example drives IO3 and RST itself to switch between SPI and QSPI, so one wiring serves both')),
}
def strip(colors, w=240, h=22):
    """Colour swatch strip without text (shared by both languages)."""
    n = len(colors); cw = w / n
    body = ''.join(f'<rect x="{i * cw:.2f}" y="0" width="{cw + 0.5:.2f}" height="{h}" fill="{c}"/>' for i, c in enumerate(colors))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{body}'
            f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" fill="none" stroke="#c5ccd3"/></svg>\n')

def _hue(t):
    import colorsys
    r, g, b = colorsys.hsv_to_rgb(t * 0.83, 1.0, 1.0)
    return int(r * 255), int(g * 255), int(b * 255)

def _hex(r, g, b): return f'#{r:02x}{g:02x}{b:02x}'
def _q(v, bits):                       # quantise an 8-bit channel to <bits> and expand back
    q = v >> (8 - bits); return q * 255 // ((1 << bits) - 1)

CGA16 = ['#000000', '#0000aa', '#00aa00', '#00aaaa', '#aa0000', '#aa00aa', '#aa5500', '#aaaaaa',
         '#555555', '#5555ff', '#55ff55', '#55ffff', '#ff5555', '#ff55ff', '#ffff55', '#ffffff']
STRIPS = {
    'depth-rgb565': [_hex(_q(r, 5), _q(g, 6), _q(b, 5)) for r, g, b in (_hue(i / 119) for i in range(120))],
    'depth-rgb332': [_hex(_q(r, 3), _q(g, 3), _q(b, 2)) for r, g, b in (_hue(i / 119) for i in range(120))],
    'depth-pal16': CGA16,
    'depth-gray4': [_hex(v * 17, v * 17, v * 17) for v in range(16)],
    'depth-gray2': [_hex(v * 85, v * 85, v * 85) for v in range(4)],
    'depth-mono1': ['#000000', '#ffffff'],
    # grey levels multiplied by a tint colour (command 0x89), here amber and green
    'depth-gray4-tint': [_hex(v * 17, v * 17 * 176 // 255, 0) for v in range(16)],
    'depth-gray2-tint': [_hex(v * 85 * 64 // 255, v * 85, v * 85 * 96 // 255) for v in range(4)],
}

if __name__ == '__main__':
    for name, fn in FIGS.items():
        for lang, suffix in (('zh', ''), ('en', '_en')):
            open(f'{name}{suffix}.svg', 'w', encoding='utf-8').write(fn(lang))
            print('wrote', f'{name}{suffix}.svg')
    for name, colors in STRIPS.items():
        open(f'{name}.svg', 'w', encoding='utf-8').write(strip(colors))
        print('wrote', f'{name}.svg')
