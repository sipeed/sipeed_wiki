"""Capture the device web page (served by mock_device) in several states, with element boxes."""
import json
import time

from cdp import Browser

PREPARE = """
Object.defineProperty(navigator, 'language', {get: () => '%(lang)s'});
Object.defineProperty(navigator, 'languages', {get: () => ['%(lang)s']});
document.addEventListener('DOMContentLoaded', () => {
  const style = document.createElement('style');
  style.textContent = `* { font-family: "Noto Sans", "Noto Sans CJK SC", sans-serif; }
    .temp, .temp *, #fps, .mark-coord, .mark-temp, .segment-box, .segment-box input { font-family: "Noto Sans Mono", monospace; }`;
  document.head.append(style);
});
try { localStorage.palette = '%(palette)s'; } catch (_) {}
"""

BOXES = ["main", "#model", "#subtitle", ".logo", "#sr", "#compare", "#rotate", "#languageToggle", "#viewer",
         "#high", "#center", "#low", "#capture", "#record", "#status", "#fps", "#raw", "#palette",
         ".palette-option.active", "#settings", "#rawTools", "#markList", ".viewer-foot", "aside.panel"]


def boxes(page):
    return page.js("""(() => { const out = {};
      for (const s of %s) { const e = document.querySelector(s); if (!e) continue;
        const r = e.getBoundingClientRect(); out[s] = [r.left + scrollX, r.top + scrollY, r.width, r.height]; }
      return out; })()""" % json.dumps(BOXES))


def open_page(browser, url, lang, palette, width=412, height=1600):
    page = browser.page()
    page.send("Page.addScriptToEvaluateOnNewDocument",
              source=PREPARE % {"lang": "zh-CN" if lang == "zh" else "en-US", "palette": palette})
    page.viewport(width, height, scale=2, mobile=True)
    page.goto(url)
    page.wait("/\\d/.test(document.getElementById('fps').textContent)", timeout=30)
    time.sleep(2.0)                                   # let the FPS meter settle
    page.fonts_ready()
    return page


def capture_states(url, outdir, lang, palette=2):
    """Return {state: (png_path, boxes)} for the states used in the docs."""
    results = {}
    browser = Browser(lang="zh-CN" if lang == "zh" else "en-US", port=9335)
    try:
        page = open_page(browser, url, lang, palette)
        # 1. default view, rotated 180 degrees so no temperature label is clipped by the frame edge
        page.js("document.getElementById('rotate').click()")
        time.sleep(1.2)
        results["main"] = (page.shot(f"{outdir}/web-main-{lang}.png", selector="main"), boxes(page))

        # 2. comparison mode with the splitter in the middle
        page.js("document.getElementById('compare').click()")
        page.wait("document.getElementById('viewer').classList.contains('compare')")
        time.sleep(2.0)
        results["compare"] = (page.shot(f"{outdir}/web-compare-{lang}.png", selector="#viewer"), boxes(page))
        page.js("document.getElementById('compare').click()")
        time.sleep(1.0)

        # 3. multi-point temperature with a few marks
        page.js("document.getElementById('raw').click()")
        page.wait("!document.getElementById('rawTools').hidden")
        time.sleep(1.5)
        for fx, fy in [(0.23, 0.30), (0.62, 0.42), (0.36, 0.70), (0.80, 0.84)]:
            page.js("""(() => { const c = document.getElementById('view'); const r = c.getBoundingClientRect();
                c.dispatchEvent(new MouseEvent('click', {bubbles: true, clientX: r.left + r.width * %f,
                clientY: r.top + r.height * %f})); })()""" % (fx, fy))
            time.sleep(0.25)
        time.sleep(1.2)
        results["temp"] = (page.shot(f"{outdir}/web-temp-{lang}.png", selector="main"), boxes(page))
        page.close()
    finally:
        browser.close()
    return results
