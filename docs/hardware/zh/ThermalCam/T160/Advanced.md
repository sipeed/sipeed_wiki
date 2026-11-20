---
title: MS-T160 进阶使用与开发
keywords: MaixSense, Thermal, MS-T160, T160, 固件更新, OTA, 网段, HTTP API, temp8, SITHMETA, 二次开发
update:
  - date: 2026-11-18
    version: v0.1
    author: Sipeed
    content:
      - 初始化文档：设备设置、固件更新、多设备网段、自定义网页、HTTP 接口与数据格式
      - 自定义网页补充下载源码、资源内嵌要求和 AI 辅助修改
---

# 进阶使用与开发

本页分两部分：

- **设备设置**：在网页上查看固件版本、更新固件、同时接多台设备、替换网页外观。普通用户需要时再看。
- **HTTP 接口**：T160 的所有数据都能通过 HTTP 读取，适合写程序、做测温记录或接入自己的系统。

## 设备设置

竖屏时，在 T160 网页的最下方展开"设备设置与固件更新"面板（英文界面为 **Device settings & firmware**）；横屏时，点左栏的设置按钮。即可看到本节介绍的各项设置。

### 查看固件版本

面板里的"固件更新"一栏会显示当前固件的版本号和构建号，例如 `Version x.y.z · build ...`。反馈问题时请附上这一行。

### 更新固件

固件更新全部在网页上完成，不需要电脑工具。

1. 下载新的 T160 固件文件（`.bin` 格式）。下载地址：待发布。
2. 用浏览器打开 T160 网页，展开"设备设置与固件更新"面板。
3. 在"固件更新"一栏选择下载好的 `.bin` 文件，点**安装更新**，并在弹窗中确认。
4. 等待页面提示"更新完成，设备正在重启"。
5. 几秒后网页会自动重新连上画面。确认面板里的版本号已经变成新版本。

> ⚠️ 写入固件的过程中，不要拔出 T160，不要关闭网页，也不要让手机锁屏。T160 的外壳是密封的，没有可以按到的恢复按键，升级中断可能导致设备无法使用。建议用电量充足的手机或电脑来升级。

更新只替换程序，设备里的测温校准数据会保留，不需要重新校准。

### 同时接多台设备（多设备网段）

每台 T160 默认都使用同一个地址 `192.168.17.1`。只在一台电脑上同时插两台以上 T160 时，才需要给它们分配不同的网段，否则会互相冲突。手机上只插一台时，**不需要修改**。

1. 先只插一台 T160，打开网页并展开"设备设置与固件更新"面板。
2. 在"多设备网段"一栏填一个 1 ~ 254 之间的数字，例如 `18`，点**保存并重启**。
3. 设备重启后，地址变为 `192.168.18.1`。用浏览器打开新地址，确认能看到画面。
4. 换下一台 T160，重复以上步骤，并使用不同的数字。

> ⚠️ 请记住改过的地址。如果忘了，可以在电脑上查看这块 USB 网卡分到的 IP：它是 `192.168.N.x`，那么设备地址就是 `192.168.N.1`。

### 自定义网页外观

如果想换一套自己的界面，可以上传一个 HTML 文件替换 T160 的内置网页：

1. 在"设备设置与固件更新"面板的"自定义网页外观"一栏，选择 `.html` 文件，点**上传并应用**。
2. 刷新页面，即可看到新界面。

> 不熟悉网页开发也可以让 AI 来改：把内置网页交给 AI，说清楚想要的效果，改好后上传即可。步骤和可以直接复制给 AI 的修改规则，见[AI 接入：让 AI 修改网页](./AI_Control.html#让-AI-修改网页)。

使用时请注意：

- 内置网页本身就是一个单独的 HTML 文件，没有构建步骤。用 `curl http://192.168.17.1/builtin -o t160.html` 下载源码，或在浏览器打开 `/builtin` 查看网页源代码，在此基础上修改样式、布局和文字。
- 保留画面相关的元素 `<canvas id="view">`、`#overlay`，以及读取 `/frame.temp8` 或 `/stream.temp8` 的代码。超分继续使用设备内置的 `/assets/sr-fast.wasm`、`/assets/sr-fast-simd.wasm` 和 `/assets/sr-fast.bin`。
- 所有资源都要内嵌：图标用内联 SVG，图片用 data URI，不要引用 CDN、在线字体或外链图片。安卓手机开着飞行模式使用时没有网络，外部资源加载不出来。单个文件最大 124 KiB，内置网页约 98 KB。
- 自定义网页在重启和固件更新后都会保留。更新固件后如果界面不正常，在新的内置网页上重新修改。
- 自定义页面出问题时，用浏览器打开 `http://192.168.17.1/builtin`，内置页面始终可以访问。在面板里点**恢复内置网页**即可删除自定义页面。

## HTTP 接口

T160 在 USB 网卡上运行一个 HTTP 服务，地址就是网页的地址，默认 `http://192.168.17.1`，端口 80。所有接口不需要登录，只有通过 USB 连接的这台手机或电脑能访问。

简单说：要读温度，用 `/api/v1/thermal`；要整幅温度图，用 `/frame.temp8`。

### 接口一览

| 方法与路径 | 用途 |
| :--- | :--- |
| `GET /api/v1/device` | 设备信息：型号、序列号、固件版本、支持的数据格式和能力 |
| `GET /api/v1/thermal` | 当前帧的中心、最低、最高温度及其坐标 |
| `GET /frame.temp8` | 一帧 160 × 120 的 8 位温度图，后跟 120 字节元数据 |
| `GET /stream.temp8` | 连续输出温度图，同一时间只服务一个连接 |
| `GET /frame.adc16` | 一帧未经处理的 14 位原始数据，用于研究和产线测试 |
| `GET /api/v1/measurement` | 测温参数（只读），例如发射率固定为 0.95 |
| `GET /api/v1/network` | 当前网段设置 |
| `PUT /api/v1/network` | 修改网段，修改后设备自动重启 |
| `GET /api/v1/ota/status` | 固件更新状态 |
| `POST /api/v1/ota` | 上传 `.bin` 固件 |
| `GET/POST/DELETE /api/v1/web` | 查询、上传或删除自定义网页 |

### 读取温度

```bash
curl http://192.168.17.1/api/v1/thermal
```

返回示例：

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

其中：

- `celsius` 是摄氏温度；`x`、`y` 是该点在 160 × 120 原始画面中的坐标，见[坐标与画面方向](#坐标与画面方向)。
- `valid` 为 `false` 表示设备刚启动、还没有可用的画面，等 1 ~ 2 秒再读即可。

### 读取设备信息

```bash
curl http://192.168.17.1/api/v1/device
```

返回内容较长，常用的字段有：

- `device.model`：型号，T160 固定为 `T160`；`device.firmware`：固件版本。
- `sensor.native_width`、`sensor.native_height`：原始分辨率 160 × 120。
- `formats`：支持的图像格式及对应的接口路径。写程序时建议先读这里，不要写死分辨率。
- `network.device_ip`：当前设备地址。

### 温度图格式（temp8）

`/frame.temp8` 返回一条固定长度的记录，共 19320 字节：

```text
[像素数据 19200 字节][元数据 120 字节]
```

- **像素数据**：160 × 120 个字节，每个像素 1 字节，按原始画面从左上角开始逐行排列（第 y 行第 x 个像素位于偏移 `y × 160 + x`）。
- **换算成温度**：`温度(℃) = 像素值 × temperature_scale + temperature_offset`。像素值大于 `quant_max` 的点表示无效。
- **精度**：每一帧会把设备自动选定的温度范围线性映射到 0 ~ `quant_max`（当前为 254），一个码值代表的温差就是 `temperature_scale`，画面里冷热差别越大，每个码值越粗。最高温、最低温和中心温度请直接用元数据或 `/api/v1/thermal` 中的数值，它们不受量化影响。
- 如果 `temperature_scale` 是 NaN，说明这一帧没有有效的温度换算（例如画面温度完全均匀），读下一帧即可。

元数据的魔数是 ASCII `SITHMETA`，多字节字段均为小端序，常用字段如下：

| 偏移 | 长度 | 类型 | 字段 | 说明 |
| ---: | ---: | :--- | :--- | :--- |
| 0 | 8 | char[8] | `magic` | 固定为 `SITHMETA` |
| 16 | 4 | u32 | `frame_number` | 帧号 |
| 24 | 4 | u32 | `timestamp_ms` | 设备启动后的毫秒时间戳 |
| 36 | 6 | u16 × 3 | `width`、`height`、`stride_bytes` | 160、120、160 |
| 47 | 1 | u8 | `quant_max` | 最大有效像素值 |
| 48 | 8 | f32 × 2 | `temperature_scale`、`temperature_offset` | 像素值换算温度的系数 |
| 56 | 12 | f32 × 3 | 中心、最低、最高温度 | 单位 ℃ |
| 68 | 12 | u16 × 6 | 中心、最低、最高点的 x、y | 原始画面坐标 |
| 116 | 4 | u32 | `meta_crc32` | 对前 116 字节计算的 CRC-32（与 zlib.crc32 相同） |

响应头里也给出了尺寸，例如 `X-Sipeed-Width: 160`、`X-Sipeed-Record-Bytes: 19320`，可以用来校验。

### 连续流（stream.temp8）

`/stream.temp8` 在一个 HTTP 响应里不断输出上面这样的记录，一条接一条，没有分隔符，也没有 `Content-Length`。按每 19320 字节切一条即可，每条都先校验魔数和 CRC。

> ⚠️ 同一时间只有一个连续流：新的连接会让旧的连接断开。T160 网页本身就在用这个接口，所以用程序读连续流前，请先关掉网页，否则两边会互相抢画面。低频读取用 `/frame.temp8` 或 `/api/v1/thermal`，不受此限制。

### 坐标与画面方向

接口中的所有坐标都基于 160 × 120 的原始横向画面，原点在左上角。T160 网页在手机竖屏时，把画面逆时针旋转 90° 显示成 360 × 480 的竖幅画面；手机转动或手动旋转后，显示方向会跟着变。用接口坐标在网页截图上找位置时，需要按当时的显示方向换算。

### Python 示例

下面的程序只用 Python 标准库：读取一帧温度图，校验后打印中心温度和最热像素。

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

运行前确认电脑已经连上 T160，并且浏览器能打开 `http://192.168.17.1`。

### 写操作

修改网段、更新固件、上传自定义网页这类写操作，必须带上请求头 `X-Sipeed-Request: 1`，并使用正确的 `Content-Type`，否则设备会返回 `400`。这可以防止普通网页在你不知情时修改设备。

修改网段（设备收到后约 1.5 秒自动重启，新地址为 `192.168.18.1`）：

```bash
curl -X PUT http://192.168.17.1/api/v1/network \
  -H 'Content-Type: application/json' \
  -H 'X-Sipeed-Request: 1' \
  -d '{"segment": 18}'
```

上传固件（注意事项同[更新固件](#更新固件)，写入过程中不要拔出设备）：

```bash
curl -X POST http://192.168.17.1/api/v1/ota \
  -H 'Content-Type: application/octet-stream' \
  -H 'X-Sipeed-Request: 1' \
  --data-binary @t160.bin
curl http://192.168.17.1/api/v1/ota/status
```

上传或删除自定义网页（`GET /api/v1/web` 可以查看当前是否在用自定义网页）：

```bash
curl -X POST http://192.168.17.1/api/v1/web \
  -H 'Content-Type: text/html' \
  -H 'X-Sipeed-Request: 1' \
  --data-binary @t160.html
curl -X DELETE http://192.168.17.1/api/v1/web -H 'X-Sipeed-Request: 1'
```

### 常见返回码

| 返回码 | 含义 | 处理方法 |
| :--- | :--- | :--- |
| `200` | 成功 | — |
| `202` | 写操作已接受，例如设备即将重启 | 等几秒后用新地址重新连接 |
| `400` | 请求格式不对，或缺少 `X-Sipeed-Request: 1` | 检查请求头和请求体 |
| `404` | 接口不存在 | 检查路径拼写 |
| `409` | 当前状态不允许该操作 | 稍后重试 |
| `503` | 还没有可用的画面 | 按响应头 `Retry-After` 等待后重试 |

## 下一步

- 想让 AI 工具直接读取 T160 的温度和画面，或者帮你修改网页：见[AI 接入](./AI_Control.md)。
- 遇到问题：见[常见问题](./FAQ.md)。
