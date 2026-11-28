#!/usr/bin/env python3
"""Read-only MCP server for the Sipeed MS-T160 thermal camera.

Usage:
    T160_BASE=http://192.168.17.1 python3 t160_mcp_server.py

It wraps the camera HTTP API in four read-only tools for MCP clients:
    t160_device_info  model, firmware, capabilities
    t160_thermal      center / maximum / minimum of the current frame
    t160_capture      capture one frame as an Ironbow PNG plus its temperatures
    t160_watch        sample temperatures for N seconds and report the trend

No write operations (subnet changes, OTA, custom web page) are exposed, so an
AI client cannot lock itself out of the camera. Only the Python standard
library is used.
"""

import base64
import json
import os
import struct
import sys
import tempfile
import time
import urllib.error
import urllib.request
import zlib

BASE = os.environ.get("T160_BASE", "http://192.168.17.1").rstrip("/")
TIMEOUT = float(os.environ.get("T160_TIMEOUT", "8"))
PROTOCOL_VERSION = "2024-11-05"
META_BYTES = 120

# Same Ironbow stops as the built-in web page: (position, R, G, B)
IRONBOW = [(0, 0, 0, 8), (.2, 35, 8, 58), (.45, 132, 25, 74), (.68, 232, 78, 35),
           (.86, 255, 190, 74), (1, 255, 255, 238)]


def http_get(path, want_bytes=False):
    with urllib.request.urlopen(BASE + path, timeout=TIMEOUT) as response:
        body = response.read()
        return body if want_bytes else json.loads(body)


def parse_meta(meta):
    """Parse the fields we need from the 120-byte SITHMETA block."""
    if len(meta) < META_BYTES or meta[:8] != b"SITHMETA":
        raise ValueError("bad frame metadata (magic mismatch)")
    if zlib.crc32(meta[:116]) & 0xFFFFFFFF != struct.unpack_from("<I", meta, 116)[0]:
        raise ValueError("bad frame metadata (CRC mismatch)")
    width, height, stride = struct.unpack_from("<HHH", meta, 36)
    quant_max = meta[47]
    scale, offset = struct.unpack_from("<ff", meta, 48)
    center, minimum, maximum = struct.unpack_from("<fff", meta, 56)
    cx, cy, mnx, mny, mxx, mxy = struct.unpack_from("<HHHHHH", meta, 68)
    return {
        "frame_number": struct.unpack_from("<I", meta, 16)[0],
        "timestamp_ms": struct.unpack_from("<I", meta, 24)[0],
        "width": width, "height": height, "stride": stride,
        "quant_max": quant_max, "scale": scale, "offset": offset,
        "center_c": round(center, 2), "min_c": round(minimum, 2), "max_c": round(maximum, 2),
        "center_xy": [cx, cy], "min_xy": [mnx, mny], "max_xy": [mxx, mxy],
    }


def ironbow_lut(levels):
    lut = []
    for i in range(levels + 1):
        t = i / levels if levels else 0
        for (p0, *c0), (p1, *c1) in zip(IRONBOW, IRONBOW[1:]):
            if t <= p1:
                k = (t - p0) / (p1 - p0)
                lut.append(bytes(round(a + (b - a) * k) for a, b in zip(c0, c1)))
                break
    return lut


def png_bytes(width, height, rows):
    """Encode RGB rows (list of bytes) as a PNG using only zlib."""
    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
    raw = b"".join(b"\x00" + row for row in rows)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


def tool_device_info(_args):
    doc = http_get("/api/v1/device")
    summary = {
        "api": doc.get("api"),
        "device": doc.get("device"),
        "sensor": doc.get("sensor"),
        "network": doc.get("network"),
        "streaming": doc.get("streaming"),
        "measurement": doc.get("measurement"),
        "formats": [{"id": f.get("id"), "width": f.get("width"), "height": f.get("height"),
                     "frame": f.get("frame"), "stream": f.get("stream")} for f in doc.get("formats", [])],
        "ota": doc.get("ota"),
    }
    return [{"type": "text", "text": "Device capabilities:\n" + json.dumps(summary, ensure_ascii=False, indent=2)}]


def tool_thermal(_args):
    data = http_get("/api/v1/thermal")
    if not data.get("valid"):
        return [{"type": "text", "text": "No valid frame yet. Wait 1 to 2 seconds and read again."}]
    text = (
        f"Frame {data['frame_number']}: center {data['center']['celsius']} C"
        f" @({data['center']['x']},{data['center']['y']}), "
        f"max {data['maximum']['celsius']} C @({data['maximum']['x']},{data['maximum']['y']}), "
        f"min {data['minimum']['celsius']} C @({data['minimum']['x']},{data['minimum']['y']}). "
        "Coordinates use the 160x120 native landscape frame."
    )
    return [{"type": "text", "text": text}, {"type": "text", "text": json.dumps(data, ensure_ascii=False)}]


def tool_capture(args):
    record = http_get("/frame.temp8", want_bytes=True)
    meta = parse_meta(record[-META_BYTES:])
    w, h, stride, qmax = meta["width"], meta["height"], meta["stride"], meta["quant_max"]
    pixels = record[:stride * h]
    lut = ironbow_lut(qmax)
    black = b"\x00\x00\x00"
    # Rotate 90 degrees counter-clockwise, the same orientation as the web page (360x480 portrait).
    zoom = 3
    rows = []
    for out_y in range(w):
        src_x = w - 1 - out_y
        row = b"".join(lut[v] if v <= qmax else black
                       for v in (pixels[src_y * stride + src_x] for src_y in range(h)))
        row = b"".join(row[i:i + 3] * zoom for i in range(0, len(row), 3))
        rows.extend([row] * zoom)
    png = png_bytes(h * zoom, w * zoom, rows)
    path = args.get("save_path") or os.path.join(tempfile.gettempdir(), f"t160-{int(time.time())}.png")
    with open(path, "wb") as handle:
        handle.write(png)
    text = (
        f"Saved frame {meta['frame_number']} to {path} ({len(png)} bytes, Ironbow, upright like the web page). "
        f"Same frame: center {meta['center_c']} C @{meta['center_xy']}, max {meta['max_c']} C @{meta['max_xy']}, "
        f"min {meta['min_c']} C @{meta['min_xy']}. Coordinates are in the 160x120 native frame. "
        "Pixel colors are not temperatures; use the numbers."
    )
    return [{"type": "text", "text": text},
            {"type": "image", "data": base64.b64encode(png).decode("ascii"), "mimeType": "image/png"}]


def tool_watch(args):
    seconds = max(1.0, min(float(args.get("seconds", 5)), 30.0))
    interval = max(0.1, min(float(args.get("interval", 0.5)), 5.0))
    samples = []
    started = time.time()
    while time.time() - started < seconds:
        data = http_get("/api/v1/thermal")
        if data.get("valid"):
            samples.append({"t": round(time.time() - started, 2), "frame": data["frame_number"],
                            "center": data["center"]["celsius"], "min": data["minimum"]["celsius"],
                            "max": data["maximum"]["celsius"]})
        time.sleep(interval)
    if not samples:
        return [{"type": "text", "text": "No valid frames during the sampling window."}]
    maxima = [s["max"] for s in samples]
    centers = [s["center"] for s in samples]
    text = (
        f"{len(samples)} samples over {seconds:.0f}s: max {min(maxima)} to {max(maxima)} C, "
        f"center {min(centers)} to {max(centers)} C. Frames {samples[0]['frame']} to {samples[-1]['frame']}.\n"
        + json.dumps(samples, ensure_ascii=False)
    )
    return [{"type": "text", "text": text}]


NO_ARGS = {"type": "object", "properties": {}, "additionalProperties": False}
TOOLS = {
    "t160_device_info": {"fn": tool_device_info, "schema": {
        "name": "t160_device_info",
        "description": "Read MS-T160 device information: model, firmware, native resolution, supported formats, stream limit and OTA capability.",
        "inputSchema": NO_ARGS}},
    "t160_thermal": {"fn": tool_thermal, "schema": {
        "name": "t160_thermal",
        "description": "Read center, maximum and minimum temperatures (Celsius) of the current thermal frame, with coordinates in the 160x120 native frame. Fastest way to answer a temperature question; no image needed.",
        "inputSchema": NO_ARGS}},
    "t160_capture": {"fn": tool_capture, "schema": {
        "name": "t160_capture",
        "description": "Capture one thermal frame as an Ironbow PNG (upright, 360x480) and return that frame's center, maximum and minimum temperatures.",
        "inputSchema": {"type": "object", "properties": {
            "save_path": {"type": "string", "description": "Optional PNG output path"}},
            "additionalProperties": False}}},
    "t160_watch": {"fn": tool_watch, "schema": {
        "name": "t160_watch",
        "description": "Sample temperatures over time and return center/min/max and frame number for each sample, to observe heating, cooling or jitter.",
        "inputSchema": {"type": "object", "properties": {
            "seconds": {"type": "number", "minimum": 1, "maximum": 30, "default": 5},
            "interval": {"type": "number", "minimum": 0.1, "maximum": 5, "default": 0.5}},
            "additionalProperties": False}}},
}


def send(message):
    sys.stdout.write(json.dumps(message, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def handle(request):
    method = request.get("method")
    if method == "initialize":
        return {"protocolVersion": PROTOCOL_VERSION, "capabilities": {"tools": {}},
                "serverInfo": {"name": "t160-thermal", "version": "1.0.0"}}
    if method == "tools/list":
        return {"tools": [tool["schema"] for tool in TOOLS.values()]}
    if method == "tools/call":
        params = request.get("params") or {}
        name = params.get("name")
        tool = TOOLS.get(name)
        try:
            if tool is None:
                raise ValueError(f"unknown tool {name}")
            return {"content": tool["fn"](params.get("arguments") or {}), "isError": False}
        except (urllib.error.URLError, OSError) as error:
            return {"content": [{"type": "text", "text": f"Cannot reach {BASE}: {error}. Check that the camera is plugged in and the computer has a 192.168.17.x address on the USB network adapter."}],
                    "isError": True}
        except Exception as error:  # noqa: BLE001 - report tool errors to the model instead of crashing
            return {"content": [{"type": "text", "text": f"{name} failed: {error}"}], "isError": True}
    if method == "ping":
        return {}
    raise KeyError(method)


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
        except json.JSONDecodeError:
            continue
        if "id" not in request:  # notifications need no reply
            continue
        response = {"jsonrpc": "2.0", "id": request["id"]}
        try:
            response["result"] = handle(request)
        except KeyError:
            response["error"] = {"code": -32601, "message": f"Method not found: {request.get('method')}"}
        except Exception as error:  # noqa: BLE001
            response["error"] = {"code": -32603, "message": str(error)}
        send(response)


if __name__ == "__main__":
    main()
