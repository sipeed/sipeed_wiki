---
title: HTTP API
keywords: T256s, ThermalCam, 热成像, HTTP API, 温度, TEMP16, curl, 二次开发
---

## 简介

T256s 用 USB 连接电脑时，除了作为 UVC 摄像头工作，还会向电脑提供一块 USB 网卡。设备在这块网卡上运行 HTTP 服务，可以读取设备信息、当前温度、伪彩画面和每个像素的原始温度。

```text
http://192.168.17.1
```

浏览器打开这个地址，看到的是设备自带的网页；用 `curl` 或任意能发 HTTP 请求的语言访问同一批接口，拿到的是数据。

> HTTP API 需要固件 26.40.0 或更高版本。查看当前版本的方法见[系统更新](System_Update.html)。

HTTP 接口和 UVC 是两条独立的通道：

+ UVC 输出视频画面。MJPEG 画面已经上色，颜色不再对应温度；Y16 是原始数据，使用时需要自己接驱动；
+ HTTP 接口直接返回 JSON 温度、JPEG 画面和 TEMP16 原始温度，不需要驱动。

需要精确温度数值、批量采集，或者接入脚本和 AI 工具时，用 HTTP 接口更方便。

## 工作原理

相机连接电脑后，会同时提供 UVC 摄像头、USB 网卡和一块约 32 MB 的可移动磁盘。HTTP 服务运行在网卡上，电脑拿到地址后即可访问：

```text
你的程序（curl / Python / AI 工具）
        |
        | HTTP
        v
T256s  http://192.168.17.1
        |
        +-- /api/v1/thermal    当前中心、最高、最低温度
        +-- /frame.jpg         伪彩画面
        +-- /frame.temp16      逐像素原始温度
```

其中：

+ 设备固定使用 `192.168.17.1/24`，自己当 DHCP 服务器，给电脑分配 `192.168.17.2` 到 `192.168.17.20`；
+ 读取接口不需要登录，返回的数据不做缓存；
+ 连续视频流最多同时 4 路。

## 使用前准备

开始前，请先确认：

+ 相机已用 Type-C 线连接电脑，并且电脑上能看到 UVC 摄像头；
+ 系统里多出一块 USB 网卡，并已拿到 `192.168.17.x` 地址。Windows 在「网络连接」中查看，Linux 用 `ip addr` 查看；
+ 浏览器打开 `http://192.168.17.1` 能看到设备网页；
+ 电脑上可以使用 `curl`。Windows 10/11 自带 `curl.exe`，在 PowerShell 中可以直接运行。

> 浏览器打不开 `192.168.17.1` 时，先检查网卡有没有拿到地址。拿到 `169.254.x.x` 说明 DHCP 没有成功，可以给网卡设置静态地址 `192.168.17.100`，掩码 `255.255.255.0`。

## 接口一览

| 方法 | 路径 | 用途 |
| --- | --- | --- |
| GET | `/api/v1/device` | 设备型号、固件、分辨率、支持的格式 |
| GET | `/api/v1/network` | 当前网段、设备地址和 DHCP 地址池 |
| PUT | `/api/v1/network` | 修改网段 |
| GET | `/api/v1/thermal` | 当前帧的中心、最高、最低温度 |
| GET | `/api/v1/measurement` | 测温参数（只读） |
| GET | `/frame.temp16` | 单帧逐像素原始温度 |
| GET | `/stream.temp16` | 连续原始温度 |
| GET | `/frame.jpg?source=sr` | 单帧超分伪彩画面 |
| GET | `/frame.jpg?source=native` | 单帧原生伪彩画面 |
| GET | `/stream.jpg?source=sr` | 连续超分伪彩画面 |
| GET | `/stream.jpg?source=native` | 连续原生伪彩画面 |

> 单帧接口 `/frame.temp16`、`/frame.jpg` 也支持 `HEAD`，只返回响应头，适合先探测尺寸和元数据长度。

## 查看设备信息

`GET /api/v1/device` 是接口入口，返回设备型号、固件、分辨率、支持的格式和并发上限。

```bash
curl http://192.168.17.1/api/v1/device
```

返回内容较长，下面只保留常用字段：

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

写程序时，建议先请求一次这个接口，再按返回的 `frame` 和 `stream` 地址取数据，不要写死路径。固件之后增加格式或调整路径时，程序不用跟着改。

## 读取温度

### 当前温度

`GET /api/v1/thermal` 返回当前帧的中心、最高、最低温度，不需要下载图像，适合轮询和报警。

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

其中：

+ `frame_number` 是帧序号，每出一帧加一，可以用来判断有没有新数据；
+ `timestamp_ms` 是设备启动后的毫秒数，不是当前时间；
+ 坐标基于 256×192 的横向画面。伪彩画面是竖屏的，两者方向不同，在图上标注位置时按 `recommended_rotation` 旋转一次。

相邻两帧的温度会有 0.5 ℃ 左右的抖动，判断温度是否在变化时，多采几次看趋势，不要只看一帧。

### 测温参数

`GET /api/v1/measurement` 返回设备当前使用的测温假设：

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

发射率 0.95、距离 1 米、反射温度 25 ℃ 是设备侧测温模型实际使用的参数，接口只读，不能修改。测量光亮金属时，在表面贴一层电工胶带或喷哑光黑漆，比在软件里调参数更有效。

## 抓取画面

`GET /frame.jpg` 返回一张已经上好伪彩的 JPEG 画面，需要带 `source` 参数：

```bash
# 超分画面，480×640，约 180 KB
curl -o sr.jpg "http://192.168.17.1/frame.jpg?source=sr"

# 原生画面，192×256，约 40 KB
curl -o native.jpg "http://192.168.17.1/frame.jpg?source=native"
```

+ `source=sr`：经过设备端 AI 超分的画面，细节更清楚，体积更大；
+ `source=native`：原生分辨率，体积小，适合低带宽预览；
+ 不带 `source` 会返回 `404`，错误码为 `format_not_supported`。

响应头里的 `X-Sipeed-Meta` 是这一帧元数据的 Base64 编码，解码后可以读到中心、最高、最低温度，不用再请求一次温度接口：

```bash
curl -sI "http://192.168.17.1/frame.jpg?source=native" \
  | grep -i x-sipeed
```

> JPEG 画面已经上色，像素颜色不代表温度，不能从画面反推温度。需要逐像素温度时，用下一节的 TEMP16。

## 读取逐像素温度

### 记录格式

`GET /frame.temp16` 返回一条固定长度的记录，共 98424 字节：

| 段 | 长度 | 内容 |
| --- | ---: | --- |
| payload | 98304 字节 | 256×192 个小端 `uint16`，共 49152 个像素 |
| metadata | 120 字节 | 帧号、尺寸、温度系数、极值点等 |

payload 里是线性编码的原始值，按下式换算成摄氏温度：

```text
摄氏温度 = 原始值 × temperature_scale + temperature_offset
```

当前固件的系数是 `1/64` 和 `-273.15`，即 `℃ = raw / 64 - 273.15`，和 UVC Y16 的换算一致。换算时以元数据里的系数为准，不要写死。

下面的 Python 脚本读取一帧并打印最高温和最低温，只用标准库：

```python
import struct, urllib.request, zlib

url = "http://192.168.17.1/frame.temp16"
raw = urllib.request.urlopen(url, timeout=5).read()
payload, meta = raw[:98304], raw[98304:]

crc = struct.unpack_from("<I", meta, 116)[0]
assert meta[:8] == b"SITHMETA"
assert zlib.crc32(meta[:116]) == crc, "元数据校验失败"

scale, offset = struct.unpack_from("<ff", meta, 48)
values = struct.unpack("<49152H", payload)
celsius = [v * scale + offset for v in values]

i = max(range(len(celsius)), key=celsius.__getitem__)
print(f"最高温 {celsius[i]:.2f} ℃ @ ({i % 256}, {i // 256})")
print(f"最低温 {min(celsius):.2f} ℃")
```

运行结果示例：

```text
最高温 42.10 ℃ @ (254, 2)
最低温 39.48 ℃
```

### 元数据字段

元数据固定 120 字节，小端排列。常用字段如下：

| 偏移 | 字段 | 类型 | 说明 |
| ---: | --- | --- | --- |
| 0 | `magic` | `char[8]` | 固定为 `SITHMETA` |
| 8 | `version_major` / `version_minor` | `u8` | 当前为 `1` / `0` |
| 10 | `meta_bytes` | `u16` | 固定为 `120` |
| 12 | `flags` | `u32` | 位掩码。`(flags & 0x1D) == 0x1D` 表示温度字段可用，bit 5 表示 `payload_crc32` 有效 |
| 16 | `frame_number` | `u32` | 帧序号 |
| 24 | `timestamp_ms` | `u32` | 设备启动后的毫秒数 |
| 28 | `payload_bytes` | `u32` | 固定为 `98304` |
| 32 | `payload_crc32` | `u32` | payload 的 CRC32 |
| 36 | `width` / `height` | `u16` | `256` / `192` |
| 40 | `stride_bytes` | `u16` | 固定为 `512` |
| 44 | `display_rotation` | `u8` | 建议旋转量，当前为 `3` |
| 48 | `temperature_scale` | `f32` | 温度斜率，当前为 `0.015625` |
| 52 | `temperature_offset` | `f32` | 温度截距，当前为 `-273.15` |
| 56 | `center_temperature` | `f32` | 中心点温度（℃） |
| 60 | `minimum_temperature` | `f32` | 全帧最低温（℃） |
| 64 | `maximum_temperature` | `f32` | 全帧最高温（℃） |
| 68 | `center_x` / `center_y` | `u16` | 中心点坐标 |
| 72 | `minimum_x` / `minimum_y` | `u16` | 最低温点坐标 |
| 76 | `maximum_x` / `maximum_y` | `u16` | 最高温点坐标 |
| 104 | `measurement_config_id` | `u32` | 测温配置版本，当前为 `0` |
| 116 | `meta_crc32` | `u32` | 前 116 字节的 CRC32 |

`detector_temperature`、`source_low`、`source_high` 当前为 `NaN`，`calibration_id` 和 `nuc_table_index` 未提供，读取时跳过即可。这些数值以元数据为准，不要写死在程序里。

## 连续读取

### 原始温度

`GET /stream.temp16` 会持续输出首尾相接的 98424 字节记录，中间没有分隔符，按固定长度切分即可：

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
        print('帧', int.from_bytes(rec[98304+16:98304+20], 'little'))
"
```

> 读到一半的数据要留在缓冲区里，凑够 98424 字节再解析。按 TCP 分片直接解析会把帧切坏。

### 伪彩画面

`GET /stream.jpg` 是标准的多段 JPEG 流，分隔符为 `--sipeedframe`，每段是一帧 JPEG，段头里同样带 `X-Sipeed-Meta`。

```bash
curl -s "http://192.168.17.1/stream.jpg?source=sr" \
  | ffmpeg -f mpjpeg -i - -r 20 out.mp4
```

也可以把地址直接放进浏览器的 `<img>` 标签，画面会持续刷新。

### 并发上限

设备最多同时提供 4 路连续流。第 5 路会返回 `409`，错误码为 `stream_limit_reached`：

```json
{
  "ok": false,
  "error": {
    "code": "stream_limit_reached",
    "message": "Maximum stream client count reached"
  }
}
```

单帧接口不占这个名额。客户端断开后名额会释放；读取较慢的客户端不会拖慢设备采集，设备会丢掉写不出去的帧。

三路同时读取 15 秒（26.47.0，室内场景）：

| 流 | 帧率 | 带宽 |
| --- | ---: | ---: |
| `/stream.temp16` | 18.6 FPS | 14.7 Mbit/s |
| `/stream.jpg?source=sr` | 18.6 FPS | 28.3 Mbit/s |
| `/stream.jpg?source=native` | 18.7 FPS | 6.1 Mbit/s |

JPEG 的带宽和画面复杂度有关，噪声多、纹理多的场景体积更大。表中的数值来自一次室内测量，不是上限。

## 修改网段

`PUT /api/v1/network` 可以修改设备使用的网段，设备地址会变成 `192.168.<网段>.1`。

```bash
curl -X PUT http://192.168.17.1/api/v1/network \
  -H "X-Sipeed-Request: 1" \
  -H "Content-Type: application/json" \
  -d '{"segment": 19}'
```

> 执行后设备会立即换成 `192.168.19.1`，电脑上的网卡需要重新获取地址。操作前先确认怎么改回来，把 `segment` 改回 17 再执行一次即可。

写接口要求三个条件同时满足：

+ 请求头带 `X-Sipeed-Request: 1`；
+ `Content-Type` 为 `application/json`；
+ 如果带了 `Origin` 请求头，必须是设备自己的地址。

## 错误返回

接口出错时返回统一的 JSON：

```json
{
  "ok": false,
  "error": {
    "code": "not_found",
    "message": "API endpoint not found"
  }
}
```

常见错误：

| 状态码 | 错误码 | 说明 |
| --- | --- | --- |
| 404 | `not_found` | 路径不存在，从 `/api/v1/device` 返回的地址里取 |
| 404 | `format_not_supported` | 格式不支持，检查 `source` 参数 |
| 409 | `stream_limit_reached` | 连续流超过 4 路 |
| 503 | `frame_not_ready` | 设备刚启动，还没有可用画面 |
| 400 / 415 / 403 | `missing_request_guard` / `unsupported_content_type` / `origin_rejected` | 写接口的请求头不符合要求 |

## 常见问题

### 浏览器打不开 192.168.17.1

请检查：

+ 相机是否已经连接到电脑，电脑上是否出现 UVC 摄像头；
+ 是否多出一块 USB 网卡，并且拿到了 `192.168.17.x` 地址；
+ 换一根数据线或换一个 USB 口再试，部分线材只能供电，不能传数据。

### 浏览器能打开，但 curl 连不上

Windows 的 PowerShell 5.1 把 `curl` 当作 `Invoke-WebRequest` 的别名，参数不能直接套用。改用 `curl.exe`：

```powershell
curl.exe http://192.168.17.1/api/v1/thermal
```

### 自己发请求时返回 302

用 socket 或框架直接拼 HTTP 请求时，如果 `Host` 头不是设备地址，设备会把它当成 Captive Portal 探测，返回 302 跳转到 `http://ir.sipeed.com/`。把 `Host` 设成 `192.168.17.1`（或 `t256s.cam`）即可。

### 请求 frame.jpg 返回 404

`/frame.jpg` 必须带 `source` 参数，例如 `/frame.jpg?source=sr` 或 `/frame.jpg?source=native`。不带参数时会返回 `404` 和 `format_not_supported`。

### 同时开多个视频流后请求失败

设备最多支持 4 路连续流，超出后返回 `409`。关掉暂时不用的流即可；只需要温度时，用 `/api/v1/thermal` 轮询，不占流的名额。

### 接口温度和热像仪屏幕显示对不上

常见原因：

+ 两边读的不是同一帧，温度会随时间小幅变化；
+ 设备刚上电，还没有达到热平衡，建议预热 2 分钟；
+ 被测表面发射率低，例如光亮金属，测温本身会偏低或偏高；
+ 屏幕上的数值按伪彩画面显示，接口里的坐标基于横向原始画面，标注位置时要旋转一次。

### 能不能通过接口修改发射率

不能。当前固件里 `GET /api/v1/measurement` 只读，发射率、距离和反射温度都固定在设备侧。

### 录下来的视频里没有温度数据

UVC 的 MJPEG 画面已经上色，颜色不代表温度。需要温度时，用 HTTP 的 TEMP16 或 `/api/v1/thermal`，不要从彩色画面反推。

### 改了网段之后连不上了

设备地址已经变成 `192.168.<网段>.1`，电脑需要重新获取地址。用浏览器打开新地址，再把 `segment` 改回 17 执行一次即可恢复。

## 下一步

+ 想让 AI 读取温度、抓图并给出结论，见[用 AI 控制](AI_Control.html)；
+ 想先了解 UVC 的两种输出格式，见[使用指南](UG.html)。
