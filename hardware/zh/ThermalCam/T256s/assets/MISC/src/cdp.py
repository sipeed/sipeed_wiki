"""Tiny Chrome DevTools Protocol driver for headless screenshots.

Only depends on `websocket-client` and a local Chromium/Chrome binary.
"""
import base64
import json
import shutil
import subprocess
import tempfile
import time
import urllib.request

import websocket


class Browser:
    def __init__(self, lang="zh-CN", port=9333, binary=None):
        self.port = port
        self.profile = tempfile.mkdtemp(prefix="cdp-")
        binary = binary or shutil.which("chromium") or shutil.which("google-chrome")
        self.proc = subprocess.Popen(
            [binary, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
             "--no-first-run", "--no-default-browser-check", "--mute-audio",
             f"--lang={lang}", f"--remote-debugging-port={port}", f"--user-data-dir={self.profile}",
             "about:blank"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for _ in range(100):
            try:
                urllib.request.urlopen(f"http://127.0.0.1:{port}/json/version", timeout=1)
                break
            except OSError:
                time.sleep(0.1)
        else:
            raise RuntimeError("Chromium did not start")

    def page(self):
        req = urllib.request.Request(f"http://127.0.0.1:{self.port}/json/new?about:blank", method="PUT")
        info = json.load(urllib.request.urlopen(req))
        return Page(info["webSocketDebuggerUrl"])

    def close(self):
        self.proc.terminate()
        try:
            self.proc.wait(5)
        except subprocess.TimeoutExpired:
            self.proc.kill()
        shutil.rmtree(self.profile, ignore_errors=True)


class Page:
    def __init__(self, ws_url):
        self.ws = websocket.create_connection(ws_url, timeout=60, suppress_origin=True)
        self.next_id = 0
        self.send("Page.enable")
        self.send("Runtime.enable")

    def send(self, method, **params):
        self.next_id += 1
        my_id = self.next_id
        self.ws.send(json.dumps({"id": my_id, "method": method, "params": params}))
        while True:
            message = json.loads(self.ws.recv())
            if message.get("id") == my_id:
                if "error" in message:
                    raise RuntimeError(f"{method}: {message['error']}")
                return message.get("result", {})

    def viewport(self, width, height, scale=2, mobile=False):
        self.send("Emulation.setDeviceMetricsOverride", width=width, height=height,
                  deviceScaleFactor=scale, mobile=mobile)
        if mobile:
            self.send("Emulation.setTouchEmulationEnabled", enabled=True, maxTouchPoints=5)

    def goto(self, url, settle=0.3):
        self.send("Page.navigate", url=url)
        self.wait("document.readyState === 'complete'")
        time.sleep(settle)

    def js(self, expression):
        result = self.send("Runtime.evaluate", expression=expression, awaitPromise=True,
                           returnByValue=True)
        if "exceptionDetails" in result:
            raise RuntimeError(result["exceptionDetails"])
        return result.get("result", {}).get("value")

    def wait(self, expression, timeout=20):
        end = time.time() + timeout
        while time.time() < end:
            try:
                if self.js(f"Boolean({expression})"):
                    return
            except RuntimeError:
                pass
            time.sleep(0.1)
        raise TimeoutError(expression)

    def fonts_ready(self):
        self.js("document.fonts.ready.then(() => true)")

    def rect(self, selector):
        return self.js(
            "(() => { const r = document.querySelector(%s).getBoundingClientRect();"
            " return {x: r.left + scrollX, y: r.top + scrollY, width: r.width, height: r.height}; })()"
            % json.dumps(selector))

    def shot(self, path, selector=None, clip=None, scale=1):
        if selector:
            clip = self.rect(selector)
        params = {"format": "png", "captureBeyondViewport": True}
        if clip:
            params["clip"] = {**clip, "scale": scale}
        data = self.send("Page.captureScreenshot", **params)["data"]
        with open(path, "wb") as handle:
            handle.write(base64.b64decode(data))
        return path

    def close(self):
        self.ws.close()
