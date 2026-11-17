---
title: HTTP API
keywords: T256s, ThermalCam, thermal camera, HTTP API, temperature, TEMP16, curl
---

## Introduction

When a T256s is connected to a computer over USB, it works as a UVC camera and also provides a USB network adapter. The camera runs an HTTP service on that adapter, so you can read device information, current temperatures, colorized images and per-pixel raw temperatures.

```text
http://192.168.17.1
```

Open this address in a browser and you get the camera's built-in web page. Use `curl` or any language that can send HTTP requests and you get the data.

> The HTTP API requires firmware 26.40.0 or later. See [System Update](System_Update.html) for checking the version.

The HTTP API and UVC are separate channels:

+ UVC outputs video. MJPEG frames are already colorized, so the colors no longer represent temperature; Y16 carries raw values but needs a driver on the host;
+ The HTTP API returns JSON temperatures, JPEG frames and TEMP16 raw temperatures directly, with no driver involved.

The HTTP API is the easier choice when you need accurate temperature values, batch collection, or a connection to scripts and AI tools.

## How It Works

After the camera is connected, it provides a UVC camera, a USB network adapter and a removable disk of about 32 MB. The HTTP service runs on the network adapter, and the host can reach it once it has an address:

```text
Your program (curl / Python / AI tool)
        |
        | HTTP
        v
T256s  http://192.168.17.1
        |
        +-- /api/v1/thermal    center, maximum, minimum
        +-- /frame.jpg         colorized frame
        +-- /frame.temp16      raw per-pixel temperature
```

In this setup:

+ The camera always uses `192.168.17.1/24` and acts as its own DHCP server, handing out `192.168.17.2` to `192.168.17.20`;
+ Read endpoints require no login and are served without caching;
+ At most 4 continuous streams can be open at the same time.

## Preparation

Before you start, check the following:

+ The camera is connected to the computer with a Type-C cable and the UVC camera is visible;
+ A USB network adapter has appeared and has an address in `192.168.17.x`. On Windows, check Network Connections; on Linux, use `ip addr`;
+ Opening `http://192.168.17.1` in a browser shows the camera web page;
+ `curl` is available. Windows 10 and 11 include `curl.exe`, which runs directly in PowerShell.

> If the browser cannot open `192.168.17.1`, check the address of the network adapter first. An address in `169.254.x.x` means DHCP failed; set a static address such as `192.168.17.100` with mask `255.255.255.0`.

## Endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/api/v1/device` | Model, firmware, resolution and supported formats |
| GET | `/api/v1/network` | Current subnet, device address and DHCP pool |
| PUT | `/api/v1/network` | Change the subnet |
| GET | `/api/v1/thermal` | Center, maximum and minimum of the current frame |
| GET | `/api/v1/measurement` | Measurement settings (read-only) |
| GET | `/frame.temp16` | One raw per-pixel temperature frame |
| GET | `/stream.temp16` | Continuous raw temperatures |
| GET | `/frame.jpg?source=sr` | One super-resolution colorized frame |
| GET | `/frame.jpg?source=native` | One native colorized frame |
| GET | `/stream.jpg?source=sr` | Continuous super-resolution video |
| GET | `/stream.jpg?source=native` | Continuous native video |

> The single-frame endpoints `/frame.temp16` and `/frame.jpg` also support `HEAD`, which returns only the headers and is useful for checking sizes before downloading.

## Device Information

`GET /api/v1/device` is the entry point. It returns the model, firmware, resolution, supported formats and stream limit.

```bash
curl http://192.168.17.1/api/v1/device
```

The full response is long. The commonly used fields are:

```json
{
  "device": { "model": "T256S", "firmware": "26.47.0" },
  "sensor": { "native_width": 256, "native_height": 192 },
  "network": { "segment": 17, "device_ip": "192.168.17.1" },
  "streaming": { "max_stream_clients": 4 },
  "formats": [
    { "id": "temp16", "frame": "/frame.temp16" },
    { "id": "jpg", "source": "device_sr",
      "frame": "/frame.jpg?source=sr" },
    { "id": "jpg", "source": "device_native",
      "frame": "/frame.jpg?source=native" }
  ]
}
```

In your program, request this endpoint first and then use the `frame` and `stream` URLs it returns. Do not hard-code paths. If a later firmware adds a format or changes a path, your program keeps working.

## Reading Temperatures

### Current Temperature

`GET /api/v1/thermal` returns the center, maximum and minimum temperature of the current frame. It does not download an image, so it is a good fit for polling and alarms.

```bash
curl http://192.168.17.1/api/v1/thermal
```

```json
{
  "frame_number": 2070,
  "timestamp_ms": 68681,
  "valid": true,
  "center": { "celsius": 40.79, "x": 128, "y": 96 },
  "minimum": { "celsius": 39.48, "x": 7, "y": 169 },
  "maximum": { "celsius": 41.91, "x": 254, "y": 2 }
}
```

In this response:

+ `frame_number` increments with every frame and can be used to tell whether new data arrived;
+ `timestamp_ms` counts milliseconds since the camera booted, not wall-clock time;
+ Coordinates use the 256×192 landscape frame. The colorized image is portrait, so rotate coordinates by `recommended_rotation` before drawing markers.

Adjacent frames vary by about 0.5 °C. When checking whether a temperature is changing, sample several frames and look at the trend rather than a single frame.

### Measurement Settings

`GET /api/v1/measurement` returns the assumptions the camera uses for temperature measurement:

```bash
curl http://192.168.17.1/api/v1/measurement
```

```json
{
  "processing": "device",
  "revision": 0,
  "defaults": {
    "emissivity": 0.95,
    "distance_m": 1.0,
    "reflected_temperature_c": 25.0
  },
  "limits": {
    "emissivity": [0.01, 1.0],
    "distance_m": [0.1, 100.0],
    "reflected_temperature_c": [-40.0, 550.0]
  }
}
```

The defaults (emissivity 0.95, distance 1 m, reflected temperature 25 °C) are the values the on-device model actually uses. The endpoint is read-only and cannot change them. For shiny metal, tape or matte black paint on the surface works better than changing settings in software.

## Capturing Images

`GET /frame.jpg` returns one colorized JPEG frame and requires a `source` parameter:

```bash
# Super-resolution frame, 480×640, about 180 KB
curl -o sr.jpg "http://192.168.17.1/frame.jpg?source=sr"

# Native frame, 192×256, about 40 KB
curl -o native.jpg "http://192.168.17.1/frame.jpg?source=native"
```

+ `source=sr`: processed by the on-device AI super-resolution, sharper and larger;
+ `source=native`: native resolution, smaller, suitable for low-bandwidth preview;
+ Without `source` the camera returns `404` with error code `format_not_supported`.

The `X-Sipeed-Meta` response header holds this frame's metadata as Base64. Decode it to read the center, maximum and minimum temperatures without another request:

```bash
curl -sI "http://192.168.17.1/frame.jpg?source=native" \
  | grep -i x-sipeed
```

> JPEG frames are already colorized, so colors do not represent temperature and cannot be converted back. For per-pixel temperatures, use TEMP16 in the next section.

## Reading Per-Pixel Temperatures

### Record Layout

`GET /frame.temp16` returns one fixed-length record of 98424 bytes:

| Segment | Size | Content |
| --- | ---: | --- |
| payload | 98304 bytes | 256×192 little-endian `uint16` values, 49152 pixels |
| metadata | 120 bytes | Frame number, size, temperature coefficients, extremes |

The payload holds linearly encoded raw values. Convert them with:

```text
celsius = raw × temperature_scale + temperature_offset
```

On the current firmware the coefficients are `1/64` and `-273.15`, so `°C = raw / 64 - 273.15`, the same conversion as UVC Y16. Always use the coefficients from the metadata instead of hard-coding them.

The following Python script reads one frame and prints the maximum and minimum temperatures. It uses the standard library only:

```python
import struct, urllib.request, zlib

url = "http://192.168.17.1/frame.temp16"
raw = urllib.request.urlopen(url, timeout=5).read()
payload, meta = raw[:98304], raw[98304:]

crc = struct.unpack_from("<I", meta, 116)[0]
assert meta[:8] == b"SITHMETA"
assert zlib.crc32(meta[:116]) == crc, "metadata CRC mismatch"

scale, offset = struct.unpack_from("<ff", meta, 48)
values = struct.unpack("<49152H", payload)
celsius = [v * scale + offset for v in values]

i = max(range(len(celsius)), key=celsius.__getitem__)
print(f"max {celsius[i]:.2f} °C @ ({i % 256}, {i // 256})")
print(f"min {min(celsius):.2f} °C")
```

Example output:

```text
max 42.10 °C @ (254, 2)
min 39.48 °C
```

### Metadata Fields

The metadata is 120 bytes, little-endian. The commonly used fields are:

| Offset | Field | Type | Description |
| ---: | --- | --- | --- |
| 0 | `magic` | `char[8]` | Always `SITHMETA` |
| 8 | `version_major` / `version_minor` | `u8` | Currently `1` / `0` |
| 10 | `meta_bytes` | `u16` | Always `120` |
| 12 | `flags` | `u32` | Bit mask. `(flags & 0x1D) == 0x1D` means temperature fields are usable; bit 5 means `payload_crc32` is valid |
| 16 | `frame_number` | `u32` | Frame counter |
| 24 | `timestamp_ms` | `u32` | Milliseconds since boot |
| 28 | `payload_bytes` | `u32` | Always `98304` |
| 32 | `payload_crc32` | `u32` | CRC32 of the payload |
| 36 | `width` / `height` | `u16` | `256` / `192` |
| 40 | `stride_bytes` | `u16` | Always `512` |
| 44 | `display_rotation` | `u8` | Suggested rotation, currently `3` |
| 48 | `temperature_scale` | `f32` | Slope, currently `0.015625` |
| 52 | `temperature_offset` | `f32` | Intercept, currently `-273.15` |
| 56 | `center_temperature` | `f32` | Center temperature (°C) |
| 60 | `minimum_temperature` | `f32` | Minimum temperature (°C) |
| 64 | `maximum_temperature` | `f32` | Maximum temperature (°C) |
| 68 | `center_x` / `center_y` | `u16` | Center coordinates |
| 72 | `minimum_x` / `minimum_y` | `u16` | Coldest pixel coordinates |
| 76 | `maximum_x` / `maximum_y` | `u16` | Hottest pixel coordinates |
| 104 | `measurement_config_id` | `u32` | Measurement configuration revision, currently `0` |
| 116 | `meta_crc32` | `u32` | CRC32 of the first 116 bytes |

`detector_temperature`, `source_low` and `source_high` are currently `NaN`, and `calibration_id` and `nuc_table_index` are not provided; skip them when parsing. Always read values from the metadata instead of hard-coding them.

## Continuous Streams

### Raw Temperature

`GET /stream.temp16` writes back-to-back 98424-byte records with no delimiter. Split the stream on the fixed length:

```bash
curl -s http://192.168.17.1/stream.temp16 | python3 -c "
import sys
buf = b''
while True:
    chunk = sys.stdin.buffer.read(65536)
    if not chunk: break
    buf += chunk
    while len(buf) >= 98424:
        rec, buf = buf[:98424], buf[98424:]
        print('frame', int.from_bytes(rec[98304+16:98304+20], 'little'))
"
```

> Keep partial data in your buffer and parse only when you have 98424 bytes. Parsing raw TCP chunks splits frames.

### Colorized Video

`GET /stream.jpg` is a standard multipart JPEG stream with the boundary `--sipeedframe`. Each part is one JPEG and carries `X-Sipeed-Meta` in its headers.

```bash
curl -s "http://192.168.17.1/stream.jpg?source=sr" \
  | ffmpeg -f mpjpeg -i - -r 20 out.mp4
```

You can also put the URL in an `<img>` tag in a browser and the picture keeps refreshing.

### Client Limit

The camera serves at most 4 continuous streams at once. The fifth returns `409` with error code `stream_limit_reached`:

```json
{
  "ok": false,
  "error": {
    "code": "stream_limit_reached",
    "message": "Maximum stream client count reached"
  }
}
```

Single-frame endpoints do not count against this limit. The slot is released when a client disconnects. A slow client does not slow down acquisition; the camera drops frames it cannot write.

Three streams read together for 15 seconds (26.47.0, indoor scene):

| Stream | Frame rate | Bandwidth |
| --- | ---: | ---: |
| `/stream.temp16` | 18.6 FPS | 14.7 Mbit/s |
| `/stream.jpg?source=sr` | 18.6 FPS | 28.3 Mbit/s |
| `/stream.jpg?source=native` | 18.7 FPS | 6.1 Mbit/s |

JPEG bandwidth depends on scene complexity; noisy or highly textured scenes produce larger frames. These numbers come from one indoor measurement and are not a ceiling.

## Changing the Subnet

`PUT /api/v1/network` changes the subnet the camera uses. The camera address becomes `192.168.<segment>.1`.

```bash
curl -X PUT http://192.168.17.1/api/v1/network \
  -H "X-Sipeed-Request: 1" \
  -H "Content-Type: application/json" \
  -d '{"segment": 19}'
```

> The camera switches to `192.168.19.1` immediately and the host adapter has to obtain a new address. Decide how to switch back before running the command; sending `segment` 17 again restores the default.

Write endpoints require three conditions:

+ The `X-Sipeed-Request: 1` header;
+ The correct `Content-Type`: `application/json`;
+ If an `Origin` header is present, it must be the camera's own address.

## Errors

Errors use one JSON shape:

```json
{
  "ok": false,
  "error": {
    "code": "not_found",
    "message": "API endpoint not found"
  }
}
```

Common errors:

| Status | Code | Description |
| --- | --- | --- |
| 404 | `not_found` | Unknown path; use the URLs returned by `/api/v1/device` |
| 404 | `format_not_supported` | Unsupported format; check the `source` parameter |
| 409 | `stream_limit_reached` | More than 4 continuous streams |
| 503 | `frame_not_ready` | The camera just booted and has no frame yet |
| 400 / 415 / 403 | `missing_request_guard` / `unsupported_content_type` / `origin_rejected` | Write request headers are not acceptable |

## FAQ

### The browser cannot open 192.168.17.1

Check the following:

+ The camera is connected and the UVC camera is visible on the computer;
+ A USB network adapter has appeared with an address in `192.168.17.x`;
+ Try another cable or USB port. Some cables provide power only and cannot carry data.

### The browser works but curl cannot connect

PowerShell 5.1 on Windows aliases `curl` to `Invoke-WebRequest`, so curl arguments do not apply. Use `curl.exe` instead:

```powershell
curl.exe http://192.168.17.1/api/v1/thermal
```

### A hand-built request returns 302

When you write HTTP requests by hand or through a framework, a `Host` header that is not the camera address is treated as a captive-portal probe and answered with a 302 to `http://ir.sipeed.com/`. Set `Host` to `192.168.17.1` (or `t256s.cam`).

### frame.jpg returns 404

`/frame.jpg` requires a `source` parameter, for example `/frame.jpg?source=sr` or `/frame.jpg?source=native`. Without it the camera returns `404` with `format_not_supported`.

### Requests fail after opening several video streams

The camera supports at most 4 continuous streams and returns `409` beyond that. Close the streams you do not need, or poll `/api/v1/thermal` when you only need temperatures; single requests do not use a stream slot.

### API temperatures differ from the camera screen

Common causes:

+ The two readings come from different frames, and temperatures drift slightly over time;
+ The camera has just powered on and has not reached thermal equilibrium; allow about 2 minutes;
+ The target surface has low emissivity, such as shiny metal, so the reading is biased;
+ The screen follows the colorized picture, while API coordinates use the landscape raw frame; rotate before placing markers.

### Can the API change emissivity

No. On the current firmware, `GET /api/v1/measurement` is read-only and emissivity, distance and reflected temperature are fixed on the device.

### Recorded video has no temperature data

The UVC MJPEG stream is already colorized, so colors do not represent temperature. Use TEMP16 or `/api/v1/thermal` over HTTP instead of inferring values from the picture.

### The camera is unreachable after changing the subnet

The camera now lives at `192.168.<segment>.1` and the host has to obtain a new address. Open the new address in a browser and send `segment` 17 again to restore the default.

## Next Steps

+ To let an AI read temperatures, capture frames and draw conclusions, see [Controlling the Camera with AI](AI_Control.html);
+ To learn about the two UVC output formats first, see the [User Guide](UG.html).
