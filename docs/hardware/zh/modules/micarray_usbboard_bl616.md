# 麦克风阵列 UAC 驱动板 MA-USB8（使用指南）

## 产品概览

![](../../assets/modules/micarray_usbboard_bl616/product-front.png)

MA-USB8 是一块为麦克风阵列提供 USB 音频与串口数据接口的驱动板，主要用于把麦克风阵列采集到的音频（通过 UAC2.0 8 通道）和声场成像/声源定位热力图（通过 CDC ACM / UART 帧）输出到上位机或 MCU。常见应用场景有语音采集、降噪、波束指向与声场可视化等。

- UAC2.0（USB Audio Class）：8 通道，PCM S16_LE，48 kHz
- CDC ACM（USB 虚拟串口）: 16×16 原始格式声场热力图（Hotmap Frame）串行输出
- UART: 通过 UART (2,000,000 bps) 输出 16×16 原始/HEX+彩色格式声场热力图（适合 MCU 场景）

UAC 通道定义如下：

| 通道 | 数据 |
| --- | --- |
| CH0～CH5 | PEC 采集的原始有符号 16-bit PCM |
| CH6 | CH0～CH5 延时对齐后的平均值，用作波束合成输出 |
| CH7 | PEC 采集的原始有符号 16-bit PCM |

所有通道的采样率均为 48 kHz。UAC 传输期间，CH6 对应的 PEC 原始数据会被波束合成结果覆盖。

### 波束方向与物理麦克风顺序

观察麦克风阵列正面并将连接器、平边朝下：外圈顶部为 MIC0（CH0），MIC1～MIC5（CH1～CH5）沿顺时针排列。串口命令 `0,1,..9,A,B` 从 MIC0 方向开始，以 30° 为步进沿顺时针选择波束方向：

| 命令 | 角度 | 对应物理方向 |
| --- | --- | --- |
| `0` | 0° | MIC0 / CH0 |
| `1` | 30° | MIC0 与 MIC1 之间 |
| `2` | 60° | MIC1 / CH1 |
| `3` | 90° | MIC1 与 MIC2 之间 |
| `4` | 120° | MIC2 / CH2 |
| `5` | 150° | MIC2 与 MIC3 之间 |
| `6` | 180° | MIC3 / CH3 |
| `7` | 210° | MIC3 与 MIC4 之间 |
| `8` | 240° | MIC4 / CH4 |
| `9` | 270° | MIC4 与 MIC5 之间 |
| `A` | 300° | MIC5 / CH5 |
| `B` | 330° | MIC5 与 MIC0 之间 |

物理编号和板上位置可参见[麦克风阵列模块](./micarray.md)的点位图。CH6 是波束合成输出，不代表第 7 个物理方向。

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
在设备管理器中可看到音频接口 MicArray（UAC2.0）和虚拟串口 USB 串行设备（CDC ACM）。如需录制 8 通道音频，请在录音软件中选择 MicArray，并将格式设置为 8 通道、PCM 16-bit、48 kHz。

如果录音软件只能选择 1 或 2 通道，请参见[Windows 只能选择 1 或 2 通道](#Windows-只能选择-1-或-2-通道)。

![](../../assets/modules/micarray_usbboard_bl616/devmgmt.png)

### 录音：录制 8 通道音频（UAC2.0）
下面给出 Linux CLI 与 Audacity 的常见步骤。

#### Linux（命令行，arecord 示例）
1. 确认设备 `arecord -l`。记下 card:id，例如 hw:1,0。
2. 使用 arecord 录制：
```bash
arecord -D hw:1,0 -f S16_LE -c 8 -r 48000 -t wav -d 10 test_8ch.wav
```
这条命令录制 10 秒的 8 通道 WAV（PCM S16_LE，48 kHz）。

3. （可选）使用 sox 提取指定通道（如 CH6）进行回放或分析：
```bash
sudo apt install sox
sox test_8ch.wav ch6.wav remix 7  # sox 的通道编号从 1 开始，7 表示第 7 个通道 (0-based->1-based 转换)
aplay ch6.wav
```

> 注意：硬件编号与通道索引关系与系统环境有关，录制或回放时请根据 `arecord -l`/`aplay -l` 输出确认硬件编号。如果无法访问串口设备，请参见[Linux 无法访问串口设备](#Linux-无法访问串口设备)。

#### Audacity（GUI）
1. 打开 Audacity -> 编辑 -> 首选项 -> 设备，选择 MA-USB8 采集设备。
2. 在录音通道处选择 8 通道。
3. 开始录制，你会看到多通道波形，停止后可以选择某一路音轨听/导出。

![](../../assets/modules/micarray_usbboard_bl616/audacity-linux-sine1k.png)

**Windows 下请选择 WASAPI；如果仍然只有 1 或 2 通道，请参见[Windows 只能选择 1 或 2 通道](#Windows-只能选择-1-或-2-通道)。**
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

驱动板通过 CDC ACM（`/dev/ttyACM0`）或 UART（2,000,000 bps）输出声场热力图，两个接口的默认显示方式不同：

- CDC ACM 连续输出原始二进制数据。每帧包含 16 字节帧头和 256 字节数据，详见 [Hotmap Frame 格式](#Hotmap-Frame-格式（开发者视角）)。
- UART 默认输出原始二进制数据。在串口中输入大写 `F` 后，开启 16×16 文本热力图；再输入大写 `C`，开启伪彩显示。输入小写 `f`、`c` 可分别关闭对应功能，详见[完整指令表](#完整指令表（开发者）)。

### 通过 minicom / picocom 观察（快速）

CDC ACM 使用 minicom 观察原始帧：

```bash
minicom -D /dev/ttyACM0 -H
```

UART 使用 picocom，波特率固定为 2,000,000 bps：

```bash
picocom -b 2000000 /dev/ttyUSB0
```

打开 picocom 后输入大写 `F`，将原始二进制流切换为 16×16 文本热力图；需要伪彩显示时，再输入大写 `C`。

如果串口没有数据或输出乱码，请分别参见[CDC ACM 不输出热力图](#CDC-ACM-不输出热力图)和[UART 输出乱码或无法显示](#UART-输出乱码或无法显示)。

<figure>
  <img src="../../assets/modules/micarray_usbboard_bl616/minicom_acm&picocom_uart-combine.png" style="width: 100%;">
  <figcaption>左：CDC ACM 原始二进制帧的十六进制预览。右：UART 开启 16×16 打印后，从普通文本热力图切换到伪彩热力图的过程。</figcaption>
</figure>

<div style="display: flex; gap: 2%; flex-wrap: wrap;">
  <figure style="flex: 1 1 260px; margin: 0;">
    <img src="../../assets/modules/micarray_usbboard_bl616/picocom_uart-hex.png" style="width: 100%;">
    <figcaption>UART 16×16 文本热力图：输入 <code>F</code> 开启。</figcaption>
  </figure>
  <figure style="flex: 1 1 260px; margin: 0;">
    <img src="../../assets/modules/micarray_usbboard_bl616/picocom_uart-hex-cmap.png" style="width: 100%;">
    <figcaption>UART 伪彩热力图：开启 16×16 打印后输入 <code>C</code>。</figcaption>
  </figure>
</div>

### MCU 解析串口数据帧

如果要在 MCU 端解析这个帧，原则相同：丢弃 16 字节头并把后 256 字节按行/列解析。

## 常用串口命令 (用户速查)
下面摘录最常用且对普通用户最有用的串口命令，便于现场调试：

- 设置波束方向（0..9, A, B）：向串口直接输入字符（例如 `0`、`3`、`A`）来设置波束方向。
- 打开/关闭 LED 指示灯：输入 `e` / `E` （小写关，大写开）。
- 切换 UART 热力图打印：输入 `f` 关闭、`F` 开启 16×16 ASCII 打印。

更多详细指令及行为参见本文末的“开发者参考”中的完整指令表。

### 示例：设置并验证波束方向
1. 在串口中输入 `3`（示例）设置方向为 90°（3×30=90）。
2. 在 Audacity 中监听 CH6：你应该在 CH6 听到来自目标方向的声音被增强，或在系统中录制 CH6 再回放分析。

## 常见问题与故障排查

### Windows 只能选择 1 或 2 通道

先选择 `WASAPI`，再进入“设置 → 系统 → 声音 → 输入 → MicArray”，将“音频增强（Audio Enhancements）”设为“关闭”，然后重新打开录音软件。Windows 的 Voice Clarity 等音频增强可能限制应用可用的录音通道数。

### Linux 无法访问串口设备

无法访问 `/dev/ttyACM0` 或 `/dev/ttyUSB0` 时，可将当前用户加入 `plugdev` 组，然后重新登录：

```bash
sudo usermod -a -G plugdev $USER
```

也可以创建 udev 规则（示例，替换 vendor/product id）：

```bash
# /etc/udev/rules.d/99-ma-usb8.rules
SUBSYSTEM=="tty", ATTRS{idVendor}=="359F", MODE="0666", GROUP="plugdev"
```

### CDC ACM 不输出热力图

确认设备同时处于 CDC ACM/UAC 模式，而不是仅用作 UAC 音频。关闭其他占用该串口的软件，然后重新打开串口。

### UART 输出乱码或无法显示

确认波特率为 `2000000 bps`，并使用 `picocom -b 2000000`、`minicom -b 2000000` 等工具。Windows 下需要安装正确的 USB 串口驱动（CH340/CH341/CH552 等）。

## 固件升级

本页提供的固件仅适用于 MA-USB8：

### 20260803

- 文件：[MA-USB8-260803.bin](../../assets/modules/micarray_usbboard_bl616/firmware/MA-USB8-260803.bin)
- 文件大小：87456 字节
- SHA-256：`40a03a916f0cd95113109e9ba2e259e37b20db5cb19b8d1664280446cbb2ee07`

### 20251201

- 文件：[MA-USB8-251201.bin](../../assets/modules/micarray_usbboard_bl616/firmware/MA-USB8-251201.bin)
- 文件大小：87552 字节
- SHA-256：`f2381d1f5a50b0fc7a15e6723f61c4204dfae9dc394bfa349a18404ecd0c2905`

升级步骤：

1. 下载固件并核对文件大小或 SHA-256。
2. 按照[固件刷写教程](../logic_analyzer/combo8/update_firmware.html#Burn-firmware)连接设备、进入烧录模式并写入固件。
3. 烧录完成后重新插拔设备。
4. 在 Linux 下使用 `lsusb -v` 和 `arecord -l`，或在 Windows 声音设置中确认 MicArray 已提供 8 通道、PCM 16-bit、48 kHz 格式。
5. 如果 Windows 录音软件仍然只能选择 1 或 2 通道，请参见[Windows 只能选择 1 或 2 通道](#Windows-只能选择-1-或-2-通道)。

升级前请记录当前固件版本和设备描述符，便于升级失败时核对设备状态。固件升级过程中不要断开 USB 连接或关闭烧录工具。

---
## 开发者参考（协议、代码示例、完整指令表）

以下内容针对需要二次开发或深入调试的用户；普通用户可以忽略其中的协议细节。

### Hotmap Frame 格式（开发者视角）
| frame | bytes     | value |
| ----- | --------- | ----- |
| head  | 16        | 16 × 0xFF |
| data  | 16 × 16   | 每点 1 字节 (0-255)，按行优先 (HxW) | 

说明：总长度为 16 + 256 = 272 字节；head 用于对齐与帧头检测，payload 为 256 字节，每个字节表示该网格点的强度（0 最小，255 最大）。

### 完整指令表（开发者）
| 指令 | 输入(小/大写: 关/开) | 默认值 | 作用 | 输入源 |
| - | - | - | - | - |
| 设置 UAC CH6 波束成型方向角度 | 0,1,..9,A,B | 0 | 从 MIC0 / CH0 开始顺时针选择方向，每步 30°；映射见[波束方向与物理麦克风顺序](#波束方向与物理麦克风顺序)，CH6 输出合成音频 | 任意（串口/CDC） |
| 修改声源定位激活阈值(t,T) | t, T | 650 | t: -50, T: +50, 阈值可调范围: 0~2000 | 任意（串口/CDC） |
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
