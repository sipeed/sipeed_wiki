"""Shared helpers: HTML templates rendered to PNG through headless Chromium."""
import base64
import io
import tempfile
from pathlib import Path

from PIL import Image

from cdp import Browser

FONT_STACK = '"Noto Sans", "Noto Sans CJK SC", sans-serif'
FONT_STACK_ZH = '"Noto Sans CJK SC", "Noto Sans", sans-serif'
MONO_STACK = '"Noto Sans Mono", "DejaVu Sans Mono", monospace'

BASE_CSS = """
:root { --ink:#1f2328; --muted:#59636e; --line:#d1d9e0; --soft:#f6f8fa; --red:#dd2629;
        --hot:#ff5a36; --cold:#2f9bff; --accent:#0e9f8a; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: transparent; }
body { font-family: FONT; color: var(--ink); -webkit-font-smoothing: antialiased; }
.canvas { display: inline-block; }
.marker { position: absolute; width: 30px; height: 30px; margin: -15px 0 0 -15px; border-radius: 50%;
          background: #e5383b; color: #fff; font: 700 17px/30px FONT; text-align: center;
          box-shadow: 0 0 0 2.5px #fff, 0 3px 10px rgba(0,0,0,.45); z-index: 10; }
"""


def data_uri(image, fmt="PNG", quality=92):
    """Embed a PIL image (or a path) as a data URI."""
    if not isinstance(image, Image.Image):
        image = Image.open(image)
    buffer = io.BytesIO()
    if fmt == "JPEG":
        image.convert("RGB").save(buffer, "JPEG", quality=quality)
        mime = "image/jpeg"
    else:
        image.save(buffer, "PNG")
        mime = "image/png"
    return f"data:{mime};base64," + base64.b64encode(buffer.getvalue()).decode()


class Renderer:
    """Keeps one Chromium alive and renders HTML snippets to PNG files."""

    def __init__(self):
        self.browser = Browser(lang="en-US", port=9334)
        self.page = self.browser.page()
        self.tmp = Path(tempfile.mkdtemp(prefix="t256s-render-"))

    def render(self, body, out, css="", width=1200, lang="zh", scale=2, selector=".canvas"):
        font = FONT_STACK_ZH if lang == "zh" else FONT_STACK
        html = ("<!doctype html><html lang='%s'><head><meta charset='utf-8'><style>%s%s</style></head>"
                "<body>%s</body></html>") % (lang, BASE_CSS.replace("FONT", font), css.replace("FONT", font)
                                             .replace("MONO", MONO_STACK), body)
        path = self.tmp / (Path(out).stem + ".html")
        path.write_text(html, encoding="utf-8")
        self.page.viewport(width, 800, scale=scale)
        self.page.goto(path.as_uri(), settle=0.2)
        self.page.fonts_ready()
        self.page.wait("Array.from(document.images).every(i => i.complete)")
        return self.page.shot(str(out), selector=selector, scale=1)

    def close(self):
        self.page.close()
        self.browser.close()
