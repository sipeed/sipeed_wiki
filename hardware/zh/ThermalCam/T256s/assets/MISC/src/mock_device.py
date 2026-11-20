"""Replay real T256S captures behind the device's own web page, for documentation screenshots.

The page (protocol-v1.html / protocol-v1.js) is served unmodified. Device JPEG frames are
recolored with the firmware palette the page selects, exactly as the device does: the SR and
native captures are mapped back to their 8-bit gray levels and run through the chosen LUT.
"""
import argparse
import base64
import io
import json
import re
import struct
import threading
import time
import zlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import numpy as np
from PIL import Image
from scipy.spatial import cKDTree

from palettes import NAMES, load_luts

LUTS = load_luts()


def gray_from_capture(jpeg_path, palette):
    """Map a device-colored JPEG back to the 8-bit levels the device colored it from."""
    rgb = np.asarray(Image.open(jpeg_path).convert("RGB"), np.float32)
    _, index = cKDTree(LUTS[palette].astype(np.float32)).query(rgb.reshape(-1, 3))
    return index.reshape(rgb.shape[:2]).astype(np.uint8)


def seal(meta, frame, payload=None):
    """Renumber a SITHMETA block and refresh its CRCs."""
    struct.pack_into("<II", meta, 16, frame, frame)
    struct.pack_into("<I", meta, 24, frame * 40)
    if payload is not None:
        struct.pack_into("<II", meta, 28, len(payload), zlib.crc32(payload))
    struct.pack_into("<I", meta, 116, zlib.crc32(bytes(meta[:116])))
    return bytes(meta)


class Device:
    """Serves one capture directory (see `build_images.py capture`)."""

    def __init__(self, capture, firmware, palette):
        capture = Path(capture)
        source_palette = int((capture / "palette.txt").read_text())
        self.firmware = firmware
        self.palette = palette
        self.frame = 26470
        self.lock = threading.Lock()
        self.gray = {source: [gray_from_capture(capture / f"frame-{source}.jpg", source_palette)]
                     for source in ("sr", "native")}
        self.meta = {source: bytearray((capture / f"frame-{source}.meta").read_bytes()) for source in ("sr", "native")}
        self.records = [bytearray(path.read_bytes()) for path in sorted(capture.glob("frame-temp16-*.bin"))]
        self.cache = {}

    def next_frame(self):
        with self.lock:
            self.frame += 1
            return self.frame

    def jpeg(self, source, index):
        key = (source, index % len(self.gray[source]), self.palette)
        if key not in self.cache:
            image = Image.fromarray(LUTS[self.palette][self.gray[source][key[1]]])
            buffer = io.BytesIO()
            image.save(buffer, "JPEG", quality=95)
            self.cache[key] = buffer.getvalue()
        jpeg = self.cache[key]
        meta = seal(bytearray(self.meta[source]), self.next_frame(), jpeg)
        return jpeg, base64.b64encode(meta).decode()

    def temp16(self, index):
        record = bytearray(self.records[index % len(self.records)])
        record[98304:] = seal(record[98304:], self.next_frame())
        return bytes(record)

    def info(self):
        return {
            "api": {"name": "sipeed-thermal-http", "major": 1, "minor": 0},
            "device": {"model": "T256S", "serial": "0000000000000000", "hardware": "1.0",
                       "firmware": self.firmware},
            "sensor": {"native_width": 256, "native_height": 192, "recommended_rotation": 3},
            "network": {"segment": 17, "device_ip": "192.168.17.1", "configurable": True,
                        "config_url": "/api/v1/network"},
            "streaming": {"max_stream_clients": 4, "simultaneous_formats": True},
            "measurement": {"supported": True, "center_roi": {"width": 1, "height": 1}},
            "palette": {"processing": "device", "api": "/api/cmap", "count": 20},
            "super_resolution": {"device": True, "client_recommended": True,
                                 "client_max_native_width": 256, "client_max_native_height": 192},
            "formats": [
                {"id": "temp16", "width": 256, "height": 192, "stride_bytes": 512, "bits_per_pixel": 16,
                 "temperature_encoding": "linear", "metadata": "sipeed-thermal-meta-v1",
                 "frame": "/frame.temp16", "stream": "/stream.temp16"},
                {"id": "jpg", "source": "device_sr", "source_width": 256, "source_height": 192,
                 "width": 480, "height": 640, "temperature_encoding": "none",
                 "colorization": "device_palette", "metadata": "sipeed-thermal-meta-v1-base64",
                 "frame": "/frame.jpg?source=sr", "stream": "/stream.jpg?source=sr"},
                {"id": "jpg", "source": "device_native", "source_width": 256, "source_height": 192,
                 "width": 192, "height": 256, "temperature_encoding": "none",
                 "colorization": "device_palette", "metadata": "sipeed-thermal-meta-v1-base64",
                 "frame": "/frame.jpg?source=native", "stream": "/stream.jpg?source=native"},
            ],
            "ota": {"supported": True, "format": "sipeed-t256s-sysupgrade-v2", "max_bytes": 50331648,
                    "rollback": True, "transport": "web-and-cli", "migration_required": False,
                    "upload": "/api/v1/ota", "status": "/api/v1/ota/status", "slots": "/api/v1/slots"},
        }


TEMP16_HEADERS = {
    "Content-Type": "application/vnd.sipeed.thermal-frame; version=1; format=temp16",
    "X-Sipeed-Protocol": "1.0", "X-Sipeed-Format": "temp16", "X-Sipeed-Width": "256",
    "X-Sipeed-Height": "192", "X-Sipeed-Stride-Bytes": "512", "X-Sipeed-Payload-Bytes": "98304",
    "X-Sipeed-Meta-Bytes": "120", "X-Sipeed-Record-Bytes": "98424",
}


def make_handler(device, web):
    web = Path(web)
    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def log_message(self, *args):
            pass

        def reply(self, body, content_type="application/json", status=200, extra=None):
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            for key, value in (extra or {}).items():
                self.send_header(key, value)
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            path, _, query = self.path.partition("?")
            source = "native" if "source=native" in query else "sr"
            if path in ("/", "/index.html"):
                return self.reply((web / "protocol-v1.html").read_bytes(), "text/html; charset=utf-8")
            if path == "/protocol-v1.js":
                return self.reply((web / "protocol-v1.js").read_bytes(), "text/javascript")
            if path == "/api/v1/device":
                return self.reply(json.dumps(device.info()).encode())
            if path == "/api/v1/network":
                return self.reply(json.dumps({"mode": "fixed_private_subnet", "segment": 17,
                                              "device_ip": "192.168.17.1", "default_segment": 17}).encode())
            if path == "/api/cmap":
                return self.reply(json.dumps({"index": device.palette}).encode())
            if path == "/frame.jpg":
                jpeg, meta = device.jpeg(source, 0)
                return self.reply(jpeg, "image/jpeg", extra={"X-Sipeed-Meta": meta})
            if path == "/frame.temp16":
                return self.reply(device.temp16(0), extra=TEMP16_HEADERS)
            if path == "/stream.jpg":
                return self.stream_jpeg(source)
            if path == "/stream.temp16":
                return self.stream_temp16()
            self.reply(b'{"ok":false}', status=404)

        def do_POST(self):
            match = re.fullmatch(r"/api/cmap/(\d+)", self.path)
            if match:
                device.palette = int(match.group(1)) % 20
                return self.reply(json.dumps({"index": device.palette}).encode())
            self.reply(b'{"ok":false}', status=404)

        def stream_jpeg(self, source):
            self.send_response(200)
            self.send_header("Content-Type", "multipart/x-mixed-replace; boundary=sipeedframe")
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            index = 0
            try:
                while True:
                    jpeg, meta = device.jpeg(source, index)
                    head = (f"--sipeedframe\r\nContent-Type: image/jpeg\r\nContent-Length: {len(jpeg)}\r\n"
                            f"X-Sipeed-Meta: {meta}\r\n\r\n").encode()
                    self.wfile.write(head + jpeg + b"\r\n")
                    self.wfile.flush()
                    index += 1
                    time.sleep(0.05)
            except (BrokenPipeError, ConnectionResetError):
                pass

        def stream_temp16(self):
            self.send_response(200)
            self.send_header("Content-Type", TEMP16_HEADERS["Content-Type"])
            for key, value in TEMP16_HEADERS.items():
                if key != "Content-Type":
                    self.send_header(key, value)
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            index = 0
            try:
                while True:
                    self.wfile.write(device.temp16(index))
                    self.wfile.flush()
                    index += 1
                    time.sleep(0.05)
            except (BrokenPipeError, ConnectionResetError):
                pass

    return Handler


def serve(capture, port=8917, firmware="26.47.0", palette=2):
    device = Device(capture, firmware, palette)
    server = ThreadingHTTPServer(("127.0.0.1", port), make_handler(device, Path(capture) / "page"))
    server.daemon_threads = True
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, device


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture", required=True, help="directory written by `build_images.py capture`")
    parser.add_argument("--port", type=int, default=8917)
    args = parser.parse_args()
    server, _ = serve(args.capture, args.port)
    print(f"mock T256S on http://127.0.0.1:{args.port}/")
    threading.Event().wait()
