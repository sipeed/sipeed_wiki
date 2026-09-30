<!--
维护者说明（不渲染）：SLogic32U3 用户指南骨架（功能全参考）。
待办以 "TODO" 标记；配图占位以 "> 🚧 **TODO(配图)**" 给出，附建议资源名。
可迁移自 SLogic16U3 的内容已在对应小节用 "复用 16U3" 注明——迁移时请按 32U3 实物核对（通道数、接口、灯语等）。
若本页过长，可拆为 UG_Hardware.md + UG_Software.md，届时同步更新 sidebar.yaml。
-->
---
title: SLogic32U3 用户指南
keywords: SLogic32U3, User Guide, PulseView, sigrok-cli, ngscopeclient, trigger, decoder, 信号完整性
update:
  - date: 2026-09-30
    version: v0.1
    author: Sipeed
    content:
      - 初始化用户指南骨架（章节 + 已知硬件事实 + 占位/TODO）
---

# SLogic32U3 用户指南

本指南是 SLogic32U3 的功能全参考，涵盖硬件、三套上位机、触发、协议解码与信号完整性。想快速上手请先看[快速上手](./QS.md)。

---

## 一、硬件详解

### 接口总览

> 🚧 **TODO(配图)**：正面 / 背面接口标注图。建议：`assets/MISC/front.jpg`、`assets/MISC/rear.jpg`

- **4 × Mini-HDMI 通道组**：32 通道分为 4 组，每组 8 通道（CH0–7 / CH8–15 / CH16–23 / CH24–31），经屏蔽线引出。**(待确认：每组是否含独立 GND / VCC / CK 引脚)**
- **USB-C**：USB3.2 Gen2，需使用具备 USB3 能力的线缆与主机端口。
- **MODE 按键**：**(待确认：是否沿用 16U3 的隐藏式卡针按键，用于切换 DFU 模式)**
- **ACT 指示灯**：见 [指示灯](#指示灯) 小节。
- **CK / 触发输出 (TO)**：**(待确认：是否提供外部采样时钟输入 / 触发信号输出)**

### 通道与探头线

> 🚧 **TODO(配图)**：Mini-HDMI 探头线与测试夹接线细节。建议：`assets/MISC/probe.jpg`

- 32 通道分 4 组，每组 8 通道合并到 **1 个 Mini-HDMI** 接口输入。
- **通道配色**：每组 8 通道按 **红 / 橙 / 黄 / 绿 / 棕 / 蓝 / 白 / 灰** 八色循环标识。
- **(待确认)** 探头线的方向标记、信号/GND 排布。
- **(待确认)** VCC 输出能力（电压 / 电流上限）。

### 可选 ADC 示波器模组

SLogic32U3 可选配 4 通道 ADC 模组，把对应管脚采样**作为 8-bit 模拟信号上传**，让同一台设备兼作采样示波器。

- 通道数：4
- 分辨率：8-bit
- 模拟带宽：10MHz
- 输入量程：±15V / ±7.5V 可选
- 耦合：AC / DC 可切换
- 采样率：**(待确认：100 或 200 MSa/s)**
- 启用方式：在 ngscopeclient 的 `sigrok-bridge` 启动时加 `--adc-mode analog`；32U3 会把 D0–7 / D8–15 / D16–23 / D24–31 合并为 4 路 8-bit 模拟通道 A0–A3。**该模式只能在 bridge 启动时指定，连接后不能动态切换**（改模式需重启 bridge）。详见 [ngscopeclient](../ngscopeclient/ngscopeclient.md)。

> 🚧 **TODO(配图)**：ADC 模组照片 + 示波器模式波形。建议：`assets/DCIM/adc-module.jpg`、`assets/Screenshots/scope-mode.png`

### 指示灯

> 复用 16U3（需按 32U3 实物核对灯语）。<!-- TODO 核对 32U3 的 RGB 灯语是否与 16U3 一致 -->

> 🚧 **TODO(配图)**：ACT 指示灯位置与状态。建议：`assets/MISC/act-led.jpg`

| 状态 | 颜色 | 备注 |
| - | - | - |
| 正常连接 | 青色（蓝+绿） | **(待确认)** |
| 数据传输 | 青+红快闪 | **(待确认)** |
| DFU 模式 | 青+红慢闪 | **(待确认)** |
| USB 连接失败 | 只亮蓝 | 常见于非 USB3 线材/口 |
| Flash 加载异常 | 只亮红 | 线材压降过大 / 硬件问题 |

### MODE 按键与 DFU 模式

**MODE 按键用于在 APP（SLogic 逻辑分析仪）模式与 DFU（固件升级）模式之间切换。** 上电默认进入 APP 模式；按 MODE 切到 DFU 模式后即可刷写固件（见 [固件更新](#固件更新)）。

> 🚧 **TODO**：确认按键形态（是否沿用 16U3 的隐藏式卡针按键）与切换时的指示灯变化。

### 固件更新

> 🚧 **TODO**：补齐 32U3 固件更新工具链与固件下载地址（类比 [slogic16u3-tools](https://github.com/sipeed/slogic16u3-tools)）。

1. 进入 DFU 模式（按 MODE，等红灯慢闪）。
2. 确认出现 "SLogic DFU" 设备。
3. 使用命令行工具刷入固件：`spi_flash_xxx <固件路径>` **(待确认工具名)**。

### 探测与信号完整性

> 本节是高速逻辑分析仪的重点，建议充实为教学内容（参考 Saleae 的探针/接地教学）。

- **接地是关键**：低频、少通道可共用一根地；随频率/通道数升高，地线自感会在地线上产生压降、劣化测量——**高速时每根信号线就近配一根地线**。
- **地线绝不可接到信号线上**（可能损坏设备）。
- **阈值电压**：按 DUT 逻辑电平设置（如 3.3V 逻辑设 ~1.6V）。不确定时先用万用表/示波器测量。
- **输入范围 0~10V**，超范围前请确认硬件限制。
- Mini-HDMI 屏蔽线相比杜邦线更适合高速信号。

> 🚧 **TODO(配图)**：接地对比示意（好/坏接地下的波形）。建议：`assets/MISC/grounding-good-bad.png`

### 安全与注意事项

> 复用 16U3。

- VCC 为电源输出，**切勿与 GND 短接**。
- 与市电供电电脑配合时，探头地会与电脑地相连，请仅连接等电位接地点，**切勿接热地**。
- **(待确认：32U3 的 VCC 供电能力与过流保护参数)**

### 驱动与安装

#### Windows：免驱（WinUSB）

SLogic32U3 默认即为 WinUSB 设备，Windows 10/11 即插即用，**无需 Zadig、无需手动安装驱动**——这是相比部分 sigrok 生态竞品的体验优势。插上设备后直接运行 PulseView 或 `sigrok-bridge` 即可。

> 🚧 **TODO**：确认 PulseView 原生 Windows 版是否有带宽/采样率上限（16U3 上原生 exe 曾无法跑满目标带宽）。

#### Linux udev 规则

普通用户默认无权限访问 USB，需安装一次 udev 规则（设备 VID 为 `359f`）：

```bash
sudo tee /etc/udev/rules.d/60-sipeed.rules <<'EOF'
SUBSYSTEM!="usb|usb_device", GOTO="sipeed_rules_end"
ACTION!="add", GOTO="sipeed_rules_end"
ATTRS{idVendor}=="359f", MODE="0666", GROUP="plugdev", TAG+="uaccess"
ENV{ID_MM_DEVICE_IGNORE}="1"
LABEL="sipeed_rules_end"
EOF
sudo udevadm control --reload && sudo udevadm trigger
```

> Arch 系统将 `GROUP="plugdev"` 改为 `GROUP="uucp"`。装完后拔插一次设备使规则生效。

#### macOS

支持 macOS。PulseView 与 sigrok-cli 提供 macOS 版；若首次运行被系统阻止，在「系统设置 → 隐私与安全性」中放行即可。ngscopeclient 的 macOS 版即将推出。

---

## 二、软件使用 — PulseView (sigrok)

### 连接与设备检测

> 复用 16U3 软件指南（把设备名改为 SLogic32U3）。

最佳做法：先把设备连到 USB3 口，再启动 PulseView，让软件启动时自动检测。若已在运行，用 "Connect to Device" → 选驱动 → Scan → 选中设备。

> 🚧 **TODO(配图)**：连接对话框截图。建议：`assets/Screenshots/pv-connect.png`

### Stream 采集与采样率组合

SLogic32U3 采用 **Stream（流式）模式**：数据实时回传上位机，采集时长理论不限（受磁盘容量限制），并由板载 **2Gbit（256MB）DDR** 作弹性缓存平滑 USB 传输。稳定带宽达 **6.4Gbps（800MB/s）**。

各通道数下的最高采样率（受带宽或最高采样时钟约束）：

| 使能通道数 | 最高采样率 | 数据率 |
|---|---|---|
| 4ch | 1400 MHz | 5.6 Gbps |
| 8ch | 800 MHz | 6.4 Gbps |
| 16ch | 400 MHz | 6.4 Gbps |
| 32ch | 200 MHz | 6.4 Gbps |

> 8 / 16 / 32ch 均跑满 6.4Gbps（800MB/s）带宽上限；4ch 受最高采样时钟 1400MHz 约束（5.6Gbps）。**使能通道越少 → 可用采样率越高**，因此只启用本次采集需要的通道。

> **vs USB3.0 竞品**：DreamSourceLab DSLogic U3Pro32（USB3.0）Stream 模式 16ch 约 125MHz、32ch 约 50MHz（据其公开 Datasheet）；SLogic32U3 对应为 16ch@400MHz、32ch@200MHz，Stream 采样率约 3~4×。

### 采样率、深度与通道的相互制约

- 使能通道越多，可用采样率越低（受 USB 吞吐限制）。
- **采样率怎么选**（决策式）：经验上取信号最高频率的 **≥10 倍**；采样率过低会错过边沿，过高则可能采到毛刺。
- 采样率 × 深度 决定内存/磁盘占用，长采集前先确认磁盘空间。

> 🚧 **TODO(配图)**：采样率/通道预设面板；采样率过高/过低的波形对比。建议：`assets/Screenshots/samplerate-presets.png`、`assets/Screenshots/samplerate-compare.png`

### 触发

SLogic32U3 支持**多通道、多边沿组合触发**（在 PulseView / sigrok-cli 中配置）：可对多个通道分别设定上升沿 / 下降沿 / 任意边沿 / 电平条件并组合使用。

> ⚠️ **ngscopeclient 集成当前仅支持单通道、单边沿触发**——需要多通道 / 多边沿组合时请改用 PulseView 或 sigrok-cli。

- **触发位置**：SLogic32U3 为 Stream 模式，触发位置**(待确认——流式设备通常固定在采集起点附近，是否可调需研发确认)**。

> 🚧 **TODO**：为常见总线各配 1~2 个触发实例（如 UART 起始位、I²C 起始条件）。

> 🚧 **TODO(配图)**：触发设置面板。建议：`assets/Screenshots/trigger.png`

### 浏览与光标测量

- 缩放：滚轮；平移：拖动或 Shift+滚动；垂直平移：Ctrl+滚动。
- 用光标测量时间差，换算波特率 / 脉宽 / 事件间隔（Shift+拖动创建测量光标）。

> 🚧 **TODO(配图)**：光标测量示例。建议：`assets/Screenshots/cursors.png`

### 协议解码

1. 打开 Decoder 面板，选择协议（I2C/SPI/UART/CAN/SDIO…）。
2. 配置引脚映射、字节序、时钟极性/相位、波特率/时钟速率。
3. 解码帧标注在波形上，可点击查看详情；支持 decoder 堆叠（stack）。

**常见解码失败原因**：阈值设置不当、采样率不足、引脚映射错误。

> 🚧 **TODO**：为常用协议各补一个 32U3 实测示例（接线 + 触发 + 解码结果截图）。
> 建议每协议一小节：`UART` / `I2C` / `SPI` / `CAN` / `SDIO`。

### 文件操作

- 保存会话：保存样本、通道配置、触发与 decoder 状态。
- 导出：CSV / VCD 等；导入已有 `.sr` 波形。

---

## 三、软件使用 — ngscopeclient

SLogic32U3 是 ngscopeclient 分发版的重点支持型号。完整安装与连接见 [ngscopeclient 上手指南](../ngscopeclient/ngscopeclient.md)。

本节仅补 32U3 特有（完整安装/连接见共享页）：

- **先启动 `sigrok-bridge` 再连**：bridge 是绿色单文件，`./sigrok-bridge` 启动后保持运行、不要关闭。
- **连接参数**：菜单 File → Add → Oscilloscope，填 Driver=`sigrok`、Transport=`twinlan`、Path=`localhost:10101`（硬件在远程机器则填 `<IP>:10101`）。防火墙需放通 **10101**（命令）与 **10102**（数据）。连上后通道面板出现 **32** 路通道。
- **Filter Graph**：ngscopeclient 把协议解码/数学/测量统一为 Filter 节点，串成处理链。
- **ADC 模拟模式**：`./sigrok-bridge --adc-mode analog` 启动，把数字管脚合并为 4 路 8-bit 模拟通道 A0–A3，像采样示波器一样观测（量程/坐标轴/FFT 等自动可用）。

> 🚧 **TODO(配图)**：ngscopeclient 里 32U3 的波形/解码。建议：`assets/Screenshots/ngscope-32u3.png`

---

## 四、命令行 — sigrok-cli

用于自动化、CI、无头采集。

Sipeed 按平台预分发 SLogic 版 `sigrok-cli`：`sigrok-cli-SLogic-xxxx.{AppImage,exe,dmg}`（[下载站](https://dl.sipeed.com/shareURL/SLogic)）。libsigrok 驱动名为 `sipeed-slogic-analyzer`。

```bash
sigrok-cli --scan                                   # 扫描设备
sigrok-cli -d sipeed-slogic-analyzer --show         # 查看设备能力
sigrok-cli -d sipeed-slogic-analyzer \              # 采集：只启用 D0，10MHz 采 500k 样本
  --config samplerate=10m -C D0 \
  --samples 500k -o capture.sr
sigrok-cli -i capture.sr -P uart:rx=D0:baudrate=115200 -A uart   # 解码
```

> 采样时间(秒) = 样本数 ÷ 采样率。想让 AI Agent 代跑扫描/采集/解码，见 [SLogic 接入 AI Agent](../slogic_agent/readme.md)。
> 🚧 **TODO**：补一个完整的端到端脚本示例（扫描→采集→解码→导出 CSV），并核对驱动名在发布版 `sigrok-cli` 中的确切拼写。

---

## 五、接入 AI Agent

配合 `sigrok-cli-slogic-plugin`，无需学 PulseView，把通道与协议目标告诉 Agent 即可自动扫描/采集/解码。完整教程见 [SLogic 接入 AI Agent](../slogic_agent/readme.md)。

---

## 六、真实约束与已知问题

> 学习 sigrok 的 "Known Issues" 文化——如实标注限制，建立可信度。

> 🚧 **TODO**：随测试完善本节。候选条目：

- 采样率 × 通道数 × 深度 的组合限制（哪些组合不可用）。
- PulseView 原生 Windows 版是否有带宽/采样率上限（16U3 上原生 exe 曾无法跑满目标带宽；32U3 待验证。注：设备本身在 Windows 免驱、为 WinUSB）。
- 触发在 Stream 模式下的限制。
- ADC 模组与数字采集是否可同时使用。
