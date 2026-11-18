---
title: MS-T160 Advanced Use and Development
keywords: MaixSense, Thermal, MS-T160, T160, firmware update, OTA, subnet, HTTP API, temp8, SITHMETA, development
update:
  - date: 2026-11-18
    version: v0.1
    author: Sipeed
    content:
      - Initial release covering device settings, firmware update, multi-device subnet, custom web page, HTTP API and data format
      - Custom web page: how to get the source, embed all resources, and edit with AI help
---

# Advanced Use and Development

This page has two parts:

- **Device settings**: check the firmware version, update firmware, use several devices on one computer and replace the web page. Read these when you need them.
- **HTTP API**: every piece of T160 data is available over HTTP, for your own programs, temperature logging or system integration.

## Device Settings

In portrait, expand the **Device settings & firmware** panel at the bottom of the T160 web page. In landscape, tap the settings button in the left bar.

### Check the Firmware Version

The Firmware update section of the panel shows the current version and build, for example `Version x.y.z · build ...`. Include this line when you report a problem.

### Update the Firmware

Firmware updates happen entirely in the web page. No computer tools are needed.

1. Download the new T160 firmware file (`.bin`). Download link: coming soon.
2. Open the T160 web page and expand the **Device settings & firmware** panel.
3. In the Firmware update section, choose the `.bin` file, tap **Install update** and confirm.
4. Wait for "Update complete. Device is restarting…".
5. A few seconds later the page reconnects to the image. Check that the panel shows the new version.

> ⚠️ While the firmware is being written, do not unplug the T160, close the page or let the phone lock. The enclosure is sealed and has no reachable recovery button, so an interrupted update can leave the device unusable. Use a phone or computer with enough battery.

An update replaces only the program. The temperature calibration data on the device is kept, so no recalibration is needed.

### Use Several Devices on One Computer (Subnet)

Every T160 uses the same address, `192.168.17.1`, by default. Only when you plug two or more into one computer do they need different subnets to avoid conflicts. With a single T160 on a phone, **change nothing**.

1. Plug in one T160 only, open its page and expand the **Device settings & firmware** panel.
2. Under **Multi-device subnet**, enter a number from 1 to 254, for example `18`, and tap **Save & restart**.
3. After the restart the address becomes `192.168.18.1`. Open it in the browser and check that the image appears.
4. Repeat with the next T160, using a different number.

> ⚠️ Remember the new address. If you forget it, look up the IP of this USB network adapter on the computer. If it is `192.168.N.x`, the device is at `192.168.N.1`.

### Customize the Web Page

You can replace the built-in page with your own HTML file:

1. In the **Custom web appearance** section of the panel, choose an `.html` file and tap **Upload & apply**.
2. Reload the page to see your design.

> No web experience? Let an AI do the editing: give it the built-in page, describe what you want, and upload the result. For the steps and rules you can paste straight into the AI, see [AI Integration: Let AI Edit the Web Page](./AI_Control.html#Let-AI-Edit-the-Web-Page).

Keep these points in mind:

- The built-in page is a single HTML file with no build step. Download its source with `curl http://192.168.17.1/builtin -o t160.html`, or open `/builtin` in a browser and view the page source, then edit the style, layout and text.
- Keep the image elements `<canvas id="view">` and `#overlay`, plus the code that reads `/frame.temp8` or `/stream.temp8`. Super resolution keeps using the built-in `/assets/sr-fast.wasm`, `/assets/sr-fast-simd.wasm` and `/assets/sr-fast.bin`.
- Embed every resource: inline SVG for icons and data URIs for images, with no CDN scripts, web fonts or remote images. An Android phone in airplane mode has no internet, so external resources would not load. A single file can be up to 124 KiB; the built-in page is about 84 KB.
- A custom page stays through restarts and firmware updates. If it misbehaves after an update, redo your changes on the new built-in page.
- If the custom page breaks, open `http://192.168.17.1/builtin`; the built-in page always works there. Tap **Restore built-in page** in the panel to delete the custom page.

## HTTP API

The T160 runs an HTTP server on its USB network adapter, at the same address as the web page: `http://192.168.17.1` by default, port 80. No login is needed, and only the phone or computer connected over USB can reach it.

In short: use `/api/v1/thermal` for temperatures and `/frame.temp8` for a full temperature image.

### Endpoints

| Method and path | Purpose |
| :--- | :--- |
| `GET /api/v1/device` | Device info: model, serial, firmware, supported formats and capabilities |
| `GET /api/v1/thermal` | Center, minimum and maximum temperatures of the current frame, with coordinates |
| `GET /frame.temp8` | One 160 × 120 8-bit temperature image followed by 120 bytes of metadata |
| `GET /stream.temp8` | Continuous temperature images; serves one connection at a time |
| `GET /frame.adc16` | One frame of unprocessed 14-bit raw data, for research and production tests |
| `GET /api/v1/measurement` | Measurement parameters (read only); emissivity is fixed at 0.95 |
| `GET /api/v1/network` | Current subnet setting |
| `PUT /api/v1/network` | Change the subnet; the device restarts afterwards |
| `GET /api/v1/ota/status` | Firmware update status |
| `POST /api/v1/ota` | Upload a `.bin` firmware |
| `GET/POST/DELETE /api/v1/web` | Read, upload or delete the custom web page |

### Read Temperatures

```bash
curl http://192.168.17.1/api/v1/thermal
```

Example response:

```json
{
  "frame_number": 18342,
  "timestamp_ms": 733600,
  "valid": true,
  "center":  {"celsius": 29.50, "x": 80,  "y": 60},
  "minimum": {"celsius": 8.20,  "x": 41,  "y": 97},
  "maximum": {"celsius": 33.70, "x": 132, "y": 21},
  "measurement_config_id": 0
}
```

- `celsius` is in degrees Celsius. `x` and `y` are coordinates in the 160 × 120 native image; see [Coordinates and image orientation](#Coordinates-and-Image-Orientation).
- `valid` is `false` right after start-up, before the first frame. Read again after 1 to 2 seconds.

### Read Device Info

```bash
curl http://192.168.17.1/api/v1/device
```

The response is long. The most useful fields are:

- `device.model`: always `T160` for this product; `device.firmware`: the firmware version.
- `sensor.native_width` and `sensor.native_height`: the native 160 × 120 resolution.
- `formats`: the supported image formats and their paths. Read this first in your code instead of hard-coding the resolution.
- `network.device_ip`: the current device address.

### Temperature Image Format (temp8)

`/frame.temp8` returns one fixed-length record of 19320 bytes:

```text
[19200 bytes of pixels][120 bytes of metadata]
```

- **Pixels**: 160 × 120 bytes, one byte per pixel, in native orientation, row by row from the top-left corner. Pixel (x, y) is at offset `y × 160 + x`.
- **Temperature**: `°C = pixel × temperature_scale + temperature_offset`. Pixels above `quant_max` are invalid.
- **Precision**: each frame maps a range picked automatically by the device onto 0 to `quant_max` (currently 254). One step equals `temperature_scale`, so a scene with a wider temperature spread gets coarser steps. For the maximum, minimum and center, use the values in the metadata or `/api/v1/thermal`; they are not quantized.
- If `temperature_scale` is NaN, the frame has no valid temperature mapping (for example a perfectly uniform scene). Read the next frame.

The metadata starts with the ASCII magic `SITHMETA`. All multi-byte fields are little-endian. The most useful fields:

| Offset | Size | Type | Field | Meaning |
| ---: | ---: | :--- | :--- | :--- |
| 0 | 8 | char[8] | `magic` | Always `SITHMETA` |
| 16 | 4 | u32 | `frame_number` | Frame number |
| 24 | 4 | u32 | `timestamp_ms` | Milliseconds since start-up |
| 36 | 6 | u16 × 3 | `width`, `height`, `stride_bytes` | 160, 120, 160 |
| 47 | 1 | u8 | `quant_max` | Largest valid pixel value |
| 48 | 8 | f32 × 2 | `temperature_scale`, `temperature_offset` | Pixel-to-temperature coefficients |
| 56 | 12 | f32 × 3 | Center, minimum, maximum temperature | In °C |
| 68 | 12 | u16 × 6 | x and y of the center, minimum and maximum | Native coordinates |
| 116 | 4 | u32 | `meta_crc32` | CRC-32 of the first 116 bytes (same as zlib.crc32) |

The response headers also carry the sizes, for example `X-Sipeed-Width: 160` and `X-Sipeed-Record-Bytes: 19320`, which you can use for checks.

### Continuous Stream (stream.temp8)

`/stream.temp8` keeps sending records like the one above, back to back, with no separator and no `Content-Length`. Cut every 19320 bytes and check the magic and CRC of each record.

> ⚠️ Only one stream runs at a time: a new connection drops the old one. The T160 web page itself uses this stream, so close the page before reading the stream from a program, or the two will keep taking the image from each other. For occasional reads, use `/frame.temp8` or `/api/v1/thermal`, which have no such limit.

### Coordinates and Image Orientation

All API coordinates use the 160 × 120 native landscape image with the origin at the top-left. For a phone held upright, the T160 web page rotates the image 90° counterclockwise into a 360 × 480 portrait view. Turning the phone or rotating by hand changes the displayed orientation. Convert by the orientation in use when you match API coordinates to a screenshot of the page.

### Python Example

This program uses only the Python standard library. It reads one temperature image, checks it, and prints the center temperature and the hottest pixel.

```python
import struct
import urllib.request
import zlib

BASE = "http://192.168.17.1"

record = urllib.request.urlopen(BASE + "/frame.temp8", timeout=5).read()
pixels, meta = record[:-120], record[-120:]

assert meta[:8] == b"SITHMETA", "not a T160 frame"
assert zlib.crc32(meta[:116]) == struct.unpack_from("<I", meta, 116)[0], "CRC mismatch"

width, height, stride = struct.unpack_from("<HHH", meta, 36)
quant_max = meta[47]
scale, offset = struct.unpack_from("<ff", meta, 48)


def temperature(x, y):
    value = pixels[y * stride + x]
    return None if value > quant_max else value * scale + offset


print("Center: %.1f C" % temperature(width // 2, height // 2))
value, x, y = max((pixels[y * stride + x], x, y)
                  for y in range(height) for x in range(width)
                  if pixels[y * stride + x] <= quant_max)
print("Hottest pixel: (%d, %d) %.1f C" % (x, y, value * scale + offset))
```

Before running it, make sure the computer is connected to the T160 and the browser can open `http://192.168.17.1`.

### Write Operations

Writes such as changing the subnet, updating firmware or uploading a custom page must send the header `X-Sipeed-Request: 1` and the correct `Content-Type`; otherwise the device returns `400`. This stops ordinary web pages from changing the device without your knowledge.

Change the subnet (the device restarts about 1.5 seconds later at `192.168.18.1`):

```bash
curl -X PUT http://192.168.17.1/api/v1/network \
  -H 'Content-Type: application/json' \
  -H 'X-Sipeed-Request: 1' \
  -d '{"segment": 18}'
```

Upload firmware (the same cautions as in [Update the Firmware](#Update-the-Firmware) apply; do not unplug during the write):

```bash
curl -X POST http://192.168.17.1/api/v1/ota \
  -H 'Content-Type: application/octet-stream' \
  -H 'X-Sipeed-Request: 1' \
  --data-binary @t160.bin
curl http://192.168.17.1/api/v1/ota/status
```

Upload or delete a custom page (`GET /api/v1/web` shows whether one is in use):

```bash
curl -X POST http://192.168.17.1/api/v1/web \
  -H 'Content-Type: text/html' \
  -H 'X-Sipeed-Request: 1' \
  --data-binary @t160.html
curl -X DELETE http://192.168.17.1/api/v1/web -H 'X-Sipeed-Request: 1'
```

### Common Status Codes

| Code | Meaning | What to do |
| :--- | :--- | :--- |
| `200` | Success | — |
| `202` | Write accepted, for example the device is about to restart | Reconnect to the new address after a few seconds |
| `400` | Malformed request, or `X-Sipeed-Request: 1` is missing | Check the headers and body |
| `404` | No such endpoint | Check the path |
| `409` | The operation is not allowed in the current state | Try again later |
| `503` | No image available yet | Wait for the `Retry-After` header and retry |

## Next Steps

- To let AI tools read temperatures and images directly, or edit the web page for you, see [AI Integration](./AI_Control.md).
- If something goes wrong, see the [FAQ](./FAQ.md).
