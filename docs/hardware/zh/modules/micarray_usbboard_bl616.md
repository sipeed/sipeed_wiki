# 麦克风阵列 UAC 驱动板 MA-USB8（使用指南）

## 产品概览

![](../../assets/modules/micarray_usbboard_bl616/product-front.png)

MA-USB8 是一块为麦克风阵列提供 USB 音频与串口数据接口的驱动板，主要用于把麦克风阵列采集到的音频（通过 UAC2.0 8通道）和声场成像/声源定位热力图（通过 CDC ACM / UART 帧）输出到上位机或 MCU。常见应用场景有语音采集/降噪/波束指向与声场可视化等。

- UAC2.0（USB Audio Class）: 8 通道，PCM s16_le，48 kHz
- CDC ACM（USB 虚拟串口）: 16×16 原始格式声场热力图（Hotmap Frame）串行输出
- UART: 通过 UART (2,000,000 bps) 输出 16×16 原始/HEX+彩色格式声场热力图（适合 MCU 场景）

> 本文是 MA-USB8 的使用指南，覆盖从接线、验证设备、音频录制、波束成形到如何读取/解析声场热力图与常见故障排查。

## 快速上手

### 硬件接线与基础准备

1. 准备 5V/USB2.0 数据线。
2. 将 MA-USB8 通过 USB 连接 PC（或杜邦线连接到 MCU 主板）。
3. 选择一种模式：
   - 首选：USB（UAC2.0 音频 + CDC ACM 串口）—— 在 PC 上同时获取多通道音频与声场帧。
   - 备用：UART / USB2TTL（2,000,000-bit baudrate）—— 在 MCU/嵌入式场景下只获取（HEX/伪彩）声场帧。

建议在 PC 主机上安装 [Audacity](https://www.audacityteam.org/download/) 常用音频处理软件。

继续前请检查：
- 确认 USB 数据线连接牢靠、设备上电（LED 是否闪烁），并使用 PC 的设备管理/终端确认出现 `/dev/ttyACM0` 或 Windows 下出现 `MA-USB8` 设备。
- 如果在 Windows 下使用 [Audacity](https://www.audacityteam.org/download/) 录音，请先打开设备管理或 [Audacity](https://www.audacityteam.org/download/) 的设置确认 MA-USB8 可见。

### 验证设备（Linux）
- 插入设备后运行：
  - 查 USB 复合设备：
    - dmesg | tail  # 看到 /dev/ttyACM0 和 `SipeedUSB MicArray`。
    - lsusb           # 查看设备 id，便于 udev 规则或故障排查
  - 音频设备：
    - arecord -l      # 列出可用录音设备（应该看到 8 通道 UAC 设备）
    - pactl list short sources  # Pulseaudio 环境下查看来源

![](../../assets/modules/micarray_usbboard_bl616/dmesg.png)
![](../../assets/modules/micarray_usbboard_bl616/lsusb.png)

### 验证设备（Windows）
在设备管理器中可看到：音频接口 MicArray (UAC2.0) 和虚拟串口 USB串行设备 (CDC ACM)；如需 8 通道录制，请在录音软件（如 Audacity）中选择正确设备并设置为 8 通道采样。详细可见下节介绍。

![](../../assets/modules/micarray_usbboard_bl616/devmgmt.png)

### 录音：录制 8 通道音频（UAC2.0）
下面给出 Linux CLI 与 Audacity 的常见步骤。

#### Linux（命令行，arecord 示例）
1. 确认设备 `arecord -l`。记下 card:id，例如 hw:1,0。
2. 使用 arecord 录制：
```bash
arecord -D hw:1,0 -f S16_LE -c 8 -r 48000 -t wav -d 10 test_8ch.wav
```
这条命令录制 10s 的 8 通道 WAV（PCM S16_LE，48kHz）。

3. （可选）使用 sox 提取指定通道（如 CH6）进行回放或分析：
```bash
sudo apt install sox
sox test_8ch.wav ch6.wav remix 7  # sox 的通道编号从 1 开始，7 表示第 7 个通道 (0-based->1-based 转换)
aplay ch6.wav
```

> 注意：硬件编号与频道索引关系与系统环境有关，录制或回放时请根据 `arecord -l`/`aplay -l` 输出确认硬件编号。

#### Audacity（GUI）
1. 打开 Audacity -> 编辑 -> 首选项 -> 设备，选择 MA-USB8 采集设备。
2. 在录音通道处选择 8×通道。
3. 开始录制，你会看到多通道波形，停止后可以选择某一路音轨听/导出。

![](../../assets/modules/micarray_usbboard_bl616/audacity-linux-sine1k.png)

**Windows 需要使用 WASAPI 才会出现 8 声道的选择**
<div style="display: flex; justify-content: space-between;">
  <img src="../../assets/modules/micarray_usbboard_bl616/audacity-windows-wasapi-step-1.png" style="width: 48%;">
  <img src="../../assets/modules/micarray_usbboard_bl616/audacity-windows-wasapi-step-2.png" style="width: 48%;">
</div>

## 波束成形（Beamforming）示例
MA-USB8 支持 12 方向的波束成形（0..B），每步为 30°。

示例：要把波束指向 CH0（0°）并在输出通道 CH6 获取波束合成后的音频：
1. 打开串口（ttyACM0）：
```bash
minicom -D /dev/ttyACM0 -H
```
2. 在 minicom 中直接输入 `0`（字符）设置波束为方向 0°。
3. 在音频软件（[Audacity](https://www.audacityteam.org/download/) / arecord）监听或录制 CH6：CH6 会包含指向 CH0 的波束合成音频（例如输入 0 对应角度 0°）。

备注：输入 0..9, A, B 分别对应 0°,30°,…,330° 的 12 个方向；默认值 0。

![](../../assets/modules/micarray_usbboard_bl616/sine500hz@ch0_and_sine1000hz@ch3_with_beamforming@ch0.png)

## 读取并解析声场热力图（CDC ACM / UART）

驱动板通过 CDC ACM（/dev/ttyACM0）或 UART（2,000,000 bps）发送热力图帧。帧格式上方已给出。下面给出串口读取/解析的示例：

### 通过 minicom / picocom 观察（快速）
- CDC ACM Raw（minicom）: `minicom -D /dev/ttyACM0 -H`（`-H` 使显示十六进制/无回显，视 minicom 版本而定）
- UART（picocom）: `picocom -b 2000000 /dev/ttyUSB0` （仅物理串口 UART 支持 十六进制/颜色映射视图）
  - 按 `F` 切换为十六进制视图 (HEX)，然后按下 `C` （大写）切换为十六进制+颜色映射视图 (HEX-CMAP)。


![](../../assets/modules/micarray_usbboard_bl616/minicom_acm&picocom_uart-combine.png)

<div style="display: flex; justify-content: space-between;">
  <img src="../../assets/modules/micarray_usbboard_bl616/picocom_uart-hex.png" style="width: 45%;">
  <img src="../../assets/modules/micarray_usbboard_bl616/picocom_uart-hex-cmap.png" style="width: 45%;">
</div>

（开发者参考：hexdump 检查方法与数据格式说明请参见本文末的 “开发者参考” 部分。）

### MCU 解析串口数据帧

如果要在 MCU 端解析这个帧，原则相同：丢弃 16 字节头并把后 256 字节按行/列解析。

## 常用串口命令 (用户速查)
下面摘录最常用且对普通用户最有用的串口命令，便于现场调试：

- 设置波束方向（0..9, A, B）：向串口直接输入字符（例如 `0`、`3`、`A`）来设置波束方向。
- 打开/关闭 LED 指示灯：输入 `e` / `E` （小写关，大写开）。
- 切换 UART 热力图打印：输入 `f` / `F`（切换 16×16 ASCII 打印）。

更多详细指令及行为参见本文末的“开发者参考”中的完整指令表。

### 示例：设置并验证波束方向
1. 在串口中输入 `3`（示例）设置方向为 90°（3×30=90）。
2. 在 Audacity 中监听 CH6：你应该在 CH6 听到来自目标方向的声音被增强，或在系统中录制 CH6 再回放分析。

## 常见问题与故障排查
- Windows 上如果仅能看到 2 通道，可能是 Windows USB 音频驱动/软件对 USB 多通道的限制；需要使用 `WASAPI`。
- Linux 权限问题：无法访问 `/dev/ttyACM0` 或 `/dev/ttyUSB0` 可通过添加 udev 规则或将当前用户加入 `plugdev` 组来解决：
  - `sudo usermod -a -G plugdev $USER` 然后重新登录。
  - 创建 udev 规则（示例，替换 vendor/product id）：
```bash
# /etc/udev/rules.d/99-ma-usb8.rules
SUBSYSTEM=="tty", ATTRS{idVendor}=="359F", MODE="0666", GROUP="plugdev"
```

- CDC ACM/ttyACM0 不输出热力图：请确认设备同时处于 CDC ACM/UAC 模式（并不是只用作 UAC 音频），尝试断开其他使用该串口的软件后再打开。
- UART 串口乱码或无法显示：请确认波特率为 `2000000 bps`，且使用 `picocom -b 2000000`、`minicom -b 2000000` 等工具；在 Windows 下需要安装正确的 USB 串口驱动（CH340/CH341/CH552 等）。

## 固件升级
下载 [固件](../../assets/modules/micarray_usbboard_bl616/firmware/MA-USB8-250822.bin) 并参考 [固件刷写教程](../logic_analyzer/combo8/update_firmware.html#Burn-firmware) 进行升级。

---
## 开发者参考（协议、代码示例、完整指令表）

以下内容针对需要二次开发或深入调试的用户；普通用户可以忽略其中的协议细节。

![](../../assets/modules/micarray_usbboard_bl616/picocom_uart-raw-errcode.png)

### Hotmap Frame 格式（开发者视角）
| frame | bytes     | value |
| ----- | --------- | ----- |
| head  | 16        | 16 × 0xFF |
| data  | 16 × 16   | 每点 1 字节 (0-255)，按行优先 (HxW) | 

说明：总长度为 16 + 256 = 272 字节；head 用于对齐与帧头检测，payload 为 256 字节，每个字节表示该网格点的强度（0 最小，255 最大）。

![](../../assets/modules/micarray_usbboard_bl616/minicom_acm-raw.png)
![](../../assets/modules/micarray_usbboard_bl616/minicom_uart-raw.png)

### 完整指令表（开发者）
| 指令 | 输入(小/大写: 关/开) | 默认值 | 作用 | 输入源 |
| - | - | - | - | - |
| 设置 UAC CH6 波束成型方向角度 | 0,1,..9,A,B | 0 | 将波束指向以 30° 步进的方向（实际角度 = 输入 × 30）；CH6 会输出合成后的音频 | 任意（串口/CDC） |
| UART 声源定位图伪彩映射开关 (c/C) | c, C | c | 打开/关闭热力图伪彩（color map），需要先开启 16×16 打印 | 仅 UART |
| UART 打印内部调试信息 (d/D) | d, D | d | 启用/禁用调试信息输出 | 仅 UART |
| LED 指示灯开关 (e/E) | e, E | E | 启用/禁用 LED 实时指示显示 | 任意 |
| UART 16×16 打印开关 (f/F) | f, F | f | 切换 UART 打印 16×16 声场矩阵 (ASCII) | 仅 UART |
| 恢复默认设置 (R) | R | - | 恢复驱动板所有默认设置 | 任意 |

### udev 与权限建议
若运行 Linux 且经常使用串口，建议为设备创建 udev 规则来简化权限管理：

```bash
# /etc/udev/rules.d/99-ma-usb8.rules
SUBSYSTEM=="tty", ATTRS{idVendor}=="XXXX", ATTRS{idProduct}=="YYYY", MODE="0666", GROUP="plugdev"
```
替换 `XXXX` / `YYYY` 为 `lsusb` 显示的设备 Vendor/Product id。

### 串口/USB 注意事项
- CDC ACM（/dev/ttyACM0）在 Linux 下通常为内核 cdc_acm 驱动映射；若发现与 UAC 音频冲突，请先确认没有其他程序占用端口。
- UART/TTY（/dev/ttyUSB0）一般由 USB转串口芯片（CH34x、CH340、CH552）驱动映射。
