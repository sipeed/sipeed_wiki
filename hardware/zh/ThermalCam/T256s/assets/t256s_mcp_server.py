#!/usr/bin/env python3
"""Read-only MCP server for the Sipeed T256S thermal camera.

Usage:
    T256S_BASE=http://192.168.17.1 python3 t256s_mcp_server.py

It wraps the camera HTTP API in four read-only tools for MCP clients:
    t256s_device_info  model, firmware, capabilities
    t256s_thermal      center / maximum / minimum of the current frame
    t256s_capture      capture a JPEG (sr or native) plus its temperatures
    t256s_watch        sample temperatures for N seconds and report the trend

No write operations (subnet changes, OTA) are exposed, so an AI client cannot
lock itself out of the camera.
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

BASE = os.environ.get("T256S_BASE", "http://192.168.17.1").rstrip("/")
TIMEOUT = float(os.environ.get("T256S_TIMEOUT", "8"))
PROTOCOL_VERSION = "2024-11-05"


def http_get(path, want_bytes=False):
    url = BASE + path
    with urllib.request.urlopen(url, timeout=TIMEOUT) as response:
        body = response.read()
        return body if want_bytes else json.loads(body)


def parse_meta(meta_bytes):
    """Parse the fields we need from the 120-byte metadata block."""
    if len(meta_bytes) < 120 or meta_bytes[:8] != b"SITHMETA":
        return {}
    scale, offset = struct.unpack_from("<ff", meta_bytes, 48)
    center, minimum, maximum = struct.unpack_from("<fff", meta_bytes, 56)
    cx, cy, mnx, mny, mxx, mxy = struct.unpack_from("<HHHHHH", meta_bytes, 68)
    return {
        "scale": scale,
        "offset": offset,
        "center_c": round(center, 2),
        "min_c": round(minimum, 2),
        "max_c": round(maximum, 2),
        "center_xy": [cx, cy],
        "min_xy": [mnx, mny],
        "max_xy": [mxx, mxy],
        "frame_number": struct.unpack_from("<I", meta_bytes, 16)[0],
        "timestamp_ms": struct.unpack_from("<I", meta_bytes, 24)[0],
    }


def tool_device_info(_args):
    doc = http_get("/api/v1/device")
    device = doc.get("device", {})
    summary = {
        "model": device.get("model"),
        "hardware": device.get("hardware"),
        "firmware": device.get("firmware"),
        "serial": device.get("serial"),
        "api": doc.get("api"),
        "sensor": doc.get("sensor"),
        "network": doc.get("network"),
        "streaming": doc.get("streaming"),
        "formats": [
            {"id": f.get("id"), "source": f.get("source"), "width": f.get("width"),
             "height": f.get("height"), "frame": f.get("frame")}
            for f in doc.get("formats", [])
        ],
        "measurement": doc.get("measurement"),
    }
    text = json.dumps(summary, ensure_ascii=False, indent=2)
    return [{"type": "text", "text": "Device capabilities:\n" + text}]


def tool_thermal(_args):
    data = http_get("/api/v1/thermal")
    text = (
        f"Frame {data['frame_number']}: center {data['center']['celsius']} C"
        f" @({data['center']['x']},{data['center']['y']}), "
        f"max {data['maximum']['celsius']} C @({data['maximum']['x']},{data['maximum']['y']}), "
        f"min {data['minimum']['celsius']} C @({data['minimum']['x']},{data['minimum']['y']}). "
        "Coordinates use the 256x192 native landscape frame."
    )
    return [
        {"type": "text", "text": text},
        {"type": "text", "text": json.dumps(data, ensure_ascii=False)},
    ]


def tool_capture(args):
    source = args.get("source", "native")
    if source not in ("sr", "native"):
        raise ValueError("source must be sr or native")
    response = urllib.request.urlopen(f"{BASE}/frame.jpg?source={source}", timeout=TIMEOUT)
    jpeg = response.read()
    meta = parse_meta(base64.b64decode(response.headers.get("X-Sipeed-Meta", "")))
    path = args.get("save_path") or os.path.join(
        tempfile.gettempdir(), f"t256s-{int(time.time())}-{source}.jpg"
    )
    with open(path, "wb") as handle:
        handle.write(jpeg)
    text = (
        f"Saved {source} frame ({len(jpeg)} bytes) to {path}. "
        f"Same frame: center {meta.get('center_c')} C, max {meta.get('max_c')} C "
        f"@({meta.get('max_xy')}), min {meta.get('min_c')} C. "
        "The JPEG is colorized, so pixel colors are not temperatures."
    )
    return [
        {"type": "text", "text": text},
        {"type": "image", "data": base64.b64encode(jpeg).decode("ascii"),
         "mimeType": "image/jpeg"},
    ]


def tool_watch(args):
    seconds = max(1.0, min(float(args.get("seconds", 5)), 30.0))
    interval = max(0.1, min(float(args.get("interval", 0.5)), 5.0))
    samples = []
    started = time.time()
    while time.time() - started < seconds:
        data = http_get("/api/v1/thermal")
        samples.append({
            "t": round(time.time() - started, 2),
            "frame": data["frame_number"],
            "center": data["center"]["celsius"],
            "min": data["minimum"]["celsius"],
            "max": data["maximum"]["celsius"],
        })
        time.sleep(interval)
    maxima = [s["max"] for s in samples]
    centers = [s["center"] for s in samples]
    text = (
        f"{len(samples)} samples over {seconds:.0f}s: max {min(maxima)} to {max(maxima)} C, "
        f"center {min(centers)} to {max(centers)} C. "
        f"Frames {samples[0]['frame']} to {samples[-1]['frame']}.\n"
        + json.dumps(samples, ensure_ascii=False)
    )
    return [{"type": "text", "text": text}]


TOOLS = {
    "t256s_device_info": {
        "fn": tool_device_info,
        "schema": {
            "name": "t256s_device_info",
            "description": "Read T256S device information: model, hardware and firmware versions, native resolution, supported formats, stream limit and OTA capability.",
            "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
        },
    },
    "t256s_thermal": {
        "fn": tool_thermal,
        "schema": {
            "name": "t256s_thermal",
            "description": "Read center, maximum and minimum temperatures (Celsius) of the current thermal frame, with coordinates in the 256x192 native frame. Fastest way to answer a question; no image needed.",
            "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
        },
    },
    "t256s_capture": {
        "fn": tool_capture,
        "schema": {
            "name": "t256s_capture",
            "description": "Capture a colorized thermal frame and return the image bytes plus that frame's temperatures. sr is 480x640 super-resolution, native is 192x256 (less bandwidth).",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "source": {"type": "string", "enum": ["sr", "native"], "default": "native"},
                    "save_path": {"type": "string", "description": "Optional JPEG output path"},
                },
                "additionalProperties": False,
            },
        },
    },
    "t256s_watch": {
        "fn": tool_watch,
        "schema": {
            "name": "t256s_watch",
            "description": "Sample temperatures over time and return center/min/max and frame number for each sample, to observe heating, cooling or jitter.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "seconds": {"type": "number", "minimum": 1, "maximum": 30, "default": 5},
                    "interval": {"type": "number", "minimum": 0.1, "maximum": 5, "default": 0.5},
                },
                "additionalProperties": False,
            },
        },
    },
}


def send(message):
    sys.stdout.write(json.dumps(message, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def handle(request):
    method = request.get("method")
    request_id = request.get("id")

    if method == "initialize":
        return {
            "protocolVersion": PROTOCOL_VERSION,
            "capabilities": {"tools": {}},
            "serverInfo": {"name": "t256s-thermal", "version": "1.0.0"},
        }
    if method == "tools/list":
        return {"tools": [tool["schema"] for tool in TOOLS.values()]}
    if method == "tools/call":
        params = request.get("params") or {}
        name = params.get("name")
        args = params.get("arguments") or {}
        tool = TOOLS.get(name)
        try:
            if tool is None:
                raise ValueError(f"unknown tool {name}")
            return {"content": tool["fn"](args), "isError": False}
        except (urllib.error.URLError, OSError) as error:
            return {
                "content": [{"type": "text", "text": f"Cannot reach {BASE}: {error}. Check that the camera is plugged in and the adapter has a 192.168.17.x address."}],
                "isError": True,
            }
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
        if "id" not in request:  # 通知（notifications/initialized 等）不需要回复
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
