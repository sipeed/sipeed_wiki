---
title: SLogic32U3 硬件使用指南
keywords: SLogic32U3, 硬件, Mini-HDMI, 探头, ACT 指示灯, MODE, DFU, 固件更新, 信号完整性, udev
update:
  - date: 2026-10-06
    version: v0.3
    author: Sipeed
    content:
      - 新增配件章节（选配精细探头夹、ADC 模组、同轴探头线）
      - 新增 Mini-HDMI 线序与 AFE 电路说明，附探头子板原理图
      - 通道配色表加上色块，修正探头线与 ADC 模组参数
  - date: 2026-10-06
    version: v0.2
    author: Sipeed
    content:
      - 按 SLogic16U3 页面结构重构，拆分出独立的硬件使用指南
      - 补充接口标注、配件一览与实物配图
  - date: 2026-09-30
    version: v0.1
    author: Sipeed
    content:
      - 初始化文档
---

# 硬件使用指南

本页介绍 SLogic32U3 的硬件接口、配件、指示灯、固件更新与探测要点。软件操作见[软件使用指南](./Software_User_Guide.md)，快速上手见[快速上手](./Quick_Start.md)。

---

## 硬件概览

![SLogic32U3](./assets/DCIM/SLogic32U3-perspective.jpg)

SLogic32U3 为 CNC 铝合金一体外壳，尺寸 59 × 51 × 13 mm，表面散热齿兼顾散热与握持。所有接口分布在机身前后两端：

- **正面**：4 × Mini-HDMI 通道组接口，标号 0 ~ 3
- **背面**：USB-C 接口、ACT 指示灯、MODE 小孔按键

### 接口总览

**正面：4 组 Mini-HDMI 通道口**

![正面接口](./assets/MISC/view-front-mini-hdmi.jpg)

32 通道分为 4 组，每组 8 通道，经同轴屏蔽探头线引出。接口标号与通道对应关系：

| 接口标号 | 对应通道 |
| - | - |
| 0 | CH0 – CH7 |
| 1 | CH8 – CH15 |
| 2 | CH16 – CH23 |
| 3 | CH24 – CH31 |

每个 Mini-HDMI（HDMI Type-C 1.4）口含 8 路数据 + GND + VCC(+5V) + CK。**4 组的 GND / VCC / CK 为同源共用**，并非各组独立。

**背面：USB-C、指示灯与 MODE 按键**

![背面接口](./assets/MISC/view-rear-usb-c.jpg)

- **USB-C**：USB3.2 Gen2。必须接 10 Gbps 的 USB3 口才能跑满标称速率，**不支持 USB2.0 采集**。优先用 USB-C 直连，随附的 C 转 A 转接头会带来额外插损。
- **ACT 指示灯**：见下文[ACT 指示灯](#act-指示灯)。
- **MODE 按键**：隐藏式小孔按键，见下文 [MODE 按键](#mode-按键)。
- **CK**：100 MHz LVCMOS33 **固定时钟输出**，不可调、仅输出。

### 连接方式

1. 用随附 USB-C 线把设备**直连**电脑的 **10 Gbps USB-C 口**（通常标 `SS10` 或 `10`）。接口规格直接决定采集速率，详见[快速上手 · 连接设备](./Quick_Start.md#4-连接设备)。
2. 指示灯亮**青色**表示已上电且 USB3 链路正常。
3. 按需把 Mini-HDMI 探头线插到对应通道组。
4. 把测试夹接到待测信号与地。

![实际连接](./assets/DCIM/SLogic32U3-desk-scene.jpg)

### 开始使用

连接完成后，启动 SLogicView / ngscopeclient / sigrok-cli 任一上位机即可采集。首次使用请先完成[驱动与权限配置](#驱动与权限)。

---

## 通道与探头线

- 32 通道分 4 组，每组 8 通道合并到 **1 个 Mini-HDMI** 接口。
- **探头线结构**：前端为同轴电缆子板（每板 8 通道对应 1 个 Mini-HDMI）。每路信号走 15 cm 同轴线，芯线为信号（数字输入阻抗约 100 kΩ），屏蔽层为信号地；末端为特氟龙杜邦线。
- 同轴屏蔽线相比普通杜邦线能显著降低串扰、改善高速信号完整性，这也是 SLogic32U3 能跑到 350 MHz 数字信号带宽的前提之一。
- **Mini-HDMI 为防呆接口**，只能单向插入，不会插反。
- **VCC**：Mini-HDMI 提供 +5 V 输出（4 组同源），可为小型被测电路供电，**切勿与 GND 短接**。

### 通道配色

探头远端每组 8 路信号用 8 种不同颜色区分，排列顺序与通道顺序一致，**肉眼从第一根依次数过去即可确定通道号**。典型线序为：

<table>
  <tr><th>组内序号</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th></tr>
  <tr>
    <th>典型线色</th>
    <td style="background:#e03131;color:#fff;text-align:center">红</td>
    <td style="background:#f76707;color:#fff;text-align:center">橙</td>
    <td style="background:#f2d024;color:#333;text-align:center">黄</td>
    <td style="background:#2f9e44;color:#fff;text-align:center">绿</td>
    <td style="background:#8a5a2b;color:#fff;text-align:center">棕</td>
    <td style="background:#1c7ed6;color:#fff;text-align:center">蓝</td>
    <td style="background:#ffffff;color:#333;text-align:center;border:1px solid #ccc">白</td>
    <td style="background:#adb5bd;color:#fff;text-align:center">灰</td>
  </tr>
</table>

> 每组一定是 8 种颜色，但具体用哪几种颜色、按什么顺序排列，可能因生产批次而略有不同。上表为典型线序，以手上实物的排列为准。

4 组的线色方案相同，跨组分辨靠 Mini-HDMI 接口标号，也可以用随附的标号热缩管做长期标记。

---

## Mini-HDMI 线序与 AFE 电路

每组 8 通道通过一块同轴电缆子板汇总到 1 个 Mini-HDMI（HDMI Type-C 1.4）接口。

### 引脚规律

线序规律非常简单：**奇数脚全是 GND，偶数脚全是信号。**

这对应 Mini-HDMI 公头的物理结构：**梯形长边那一面全是奇数脚，短边那一面全是偶数脚**。所以只要认准梯形的朝向，就知道哪一面是地、哪一面是信号。

偶数脚 2 ~ 18 共 9 个，按顺序就是 8 个通道加 1 路时钟输出：

| 引脚 | 功能 | | 引脚 | 功能 |
| :-: | - | - | :-: | - |
| **2** | CH0 | | **12** | CH5 |
| **4** | CH1 | | **14** | CH6 |
| **6** | CH2 | | **16** | CH7 |
| **8** | CH3 | | **18** | CLK 输出（100 MHz LVCMOS33，固定不可调、仅输出）|
| **10** | CH4 | | 奇数脚 | GND |

> 通道号为组内编号。接口标号 0~3 依次对应 CH0–7 / CH8–15 / CH16–23 / CH24–31，例如 2 号口的 pin 2 实际是整机的 CH16。
>
> **4 组的 GND / VCC(+5V) / CK 为同源共用**，并非各组独立。

### 子板原理图

![HDMI 8CH 探头子板原理图](./assets/MISC/hdmi-probe-schematic.jpg)

子板上每路信号的前端网络：同轴芯线经 **100 kΩ** 串入，并有 **100 Ω + 15 pF** 对地；主板侧再经 **33 Ω** 串入 FPGA，并有 **100 kΩ** 下拉。

### 想在自己板上放 Mini-HDMI 对插？

> [!WARNING]
> **务必补上 AFE 部分电路。**
>
> Mini-HDMI 接口本身只是连接器，SLogic32U3 的输入特性（100 kΩ 输入阻抗、带宽与过冲抑制）由探头子板上的 AFE 网络决定。如果你的板子只把信号直接焊到 Mini-HDMI 引脚上、省掉 AFE，会出现：
>
> - 输入阻抗与标称不符，加重对被测电路的负载；
> - 高速边沿产生过冲和振铃，波形失真、解码出错；
> - 极端情况下可能损伤设备输入端。
>
> 请按上方原理图中 `AFE For SLogic (Each Data Channel)` 虚线框内的网络，在**每一条数据通道**上照搬实现。

---

## 配件

### 随机标配

| 配件 | 数量 | 说明 |
| - | - | - |
| Mini-HDMI 同轴探头线 | × 4 | 15 cm 同轴屏蔽线 + 特氟龙杜邦线，每条 8 通道 |
| 逻辑分析仪测试夹 | × 32 | 通用测试夹，适配常规排针与元件引脚 |
| USB-C 数据线 | × 1 | 含 C 转 A 转接头 |
| 标号热缩管 | × 32 | 带通道编号，由用户自行套到对应线上 |

![同轴屏蔽探头线](./assets/DCIM/accessory-coax-probe-cable.jpg)

### 选配：精细探头夹

![精细探头夹](./assets/DCIM/accessory-fine-hook-clips.jpg)

标配测试夹适合常规排针和较大引脚。遇到细间距封装时，可选配**精细探头夹（Fine-Pitch Micro Hook Clips）**：

- 可夹 **0.65 mm 间距的 TSSOP 引脚**，也适用于 SOP、SSOP 等细间距封装。
- 钩爪更细、弹性更好，直接勾住引脚即可，不易滑脱或连带相邻引脚。
- 多色可选，便于与通道编号对应。

> 做高密度芯片调试（细间距 SOP/TSSOP、QFP 边缘引脚）建议备一套，比用标配夹子去够引脚可靠得多。

---

### 选配：ADC 示波器模组

SLogic32U3 可选配 4 通道 ADC 模组，把对应管脚采样**作为 8-bit 模拟信号上传**，让同一台设备兼作采样示波器。

| 项目 | 规格 |
| - | - |
| 通道数 | 4 |
| 分辨率 | 8-bit |
| 采样率 | 100 MSa/s |
| 模拟带宽 | 10 MHz |
| 安全输入电压 | ±15 V |
| 输入阻抗 | 由探头决定 |

![可选 ADC 示波器模组](./assets/DCIM/adc-module-photo.jpg)

启用方式：在 ngscopeclient 的 UI 中配置。启用后 32U3 会把 D0–7 / D8–15 / D16–23 / D24–31 合并为 4 路 8-bit 模拟通道 A0–A3。详见 [ngscopeclient](../ngscopeclient/ngscopeclient.md)。

---

## ACT 指示灯

指示灯为 3 色 RGB：**蓝 = 电源，绿 = USB LINK，红 = 运行状态**，叠加后呈现不同颜色。

### 颜色与功能

| 状态 | 颜色 | 说明 |
| - | - | - |
| 正常连接 | 青色（蓝+绿） | 已上电且 USB3 链路已建立 |
| 数据传输 | 青 + 红快闪 | 采集中 |
| DFU 模式 | 青 + 红慢闪 | 固件升级模式 |

### 异常状态

| 现象 | 可能原因 | 处理 |
| - | - | - |
| 只亮蓝灯 | USB3 链路未建立 | 换 USB3 线材 / 换 USB3 接口，避免劣质延长线与 USB2 HUB |
| 只亮红灯 | Flash 加载异常 | 线材压降过大或硬件问题，换线后仍异常请联系售后 |
| 完全不亮 | 未上电 | 检查线材与接口是否供电正常 |

---

## MODE 按键

**MODE 为隐藏式小孔按键**，位于机身背面，需用卡针或 SIM 卡针捅入按下。用于在 APP（逻辑分析仪）与 DFU（固件升级）模式之间切换。

- 上电默认进入 **APP 模式**，即正常的逻辑分析仪工作模式。
- 按下 MODE 切到 **DFU 模式**，指示灯变为慢闪，此时可刷写固件。

---

## 更新固件

SLogic32U3 支持 Easy OTA，固件可在线升级。

### 更新步骤

1. 按 MODE 键进入 DFU 模式，等待指示灯慢闪。
2. 确认电脑上出现 "SLogic DFU" 设备。
3. 运行固件刷写工具，按提示选择固件文件并刷入。
4. 刷写完成后重新插拔设备，设备会回到 APP 模式。

> **SLogic32U3 固件尚未发布**，正式发布后将于[下载站](https://dl.sipeed.com/shareURL/SLogic)提供。
>
> 刷写工具与 SLogic16U3 共用同一套工具链：[slogic16u3-tools](https://github.com/sipeed/slogic16u3-tools/releases/latest)。

---

## 探测与信号完整性

高速逻辑分析仪的测量质量，一大半取决于怎么接线。

### 接地是关键

- 低频、少通道时可以共用一根地线。
- 随着频率和通道数升高，地线自感会在地线上产生压降、劣化测量结果。
- **高速测量时，每根信号线就近配一根地线**，这是改善波形质量最有效的手段。
- **地线绝不可接到信号线上**，可能损坏设备。

### 阈值电压

按被测电路的逻辑电平设置阈值。常见取值：

| 逻辑电平 | 建议阈值 |
| - | - |
| 1.2 V | 0.6 V |
| 1.8 V | 0.9 V |
| 2.5 V | 1.25 V |
| 3.3 V | 1.6 V |
| 5 V | 2.5 V |

不确定被测电平时，先用万用表或示波器量一下再设。

### 其他要点

- **输入范围 0 ~ 10 V**，超出范围前务必确认硬件限制。
- Mini-HDMI 同轴屏蔽线比杜邦线更适合高速信号，高速测量优先用同轴线。
- 探头线尽量短、尽量不要盘绕。

---

## 安全与注意事项

- **VCC**：Mini-HDMI 提供 +5 V 输出（4 组同源），**切勿与 GND 短接**。
- 与市电供电的电脑配合使用时，探头地会与电脑地相连。请仅连接等电位接地点，**切勿接热地**，否则可能损坏设备甚至造成危险。
- 不要在带电状态下反复插拔探头线。
- 由于 10 Gbps 数据量较大，设备持续工作时外壳会较烫，可能接近 50 ℃，属正常现象。

---

## 驱动与权限

### Windows：免驱（WinUSB）

SLogic32U3 默认即为 WinUSB 设备，Windows 10/11 即插即用，**无需 Zadig、无需手动安装驱动**。插上设备后直接运行 SLogicView 或 ngscopeclient 即可。

> 原生 Windows 版上位机**没有软件层面的带宽或采样率上限**，实际可达速率仅取决于物理机性能。这一点与 SLogic16U3 早期 Windows 原生 exe 的降速限制不同，32U3 在 Windows 下不需要靠 Linux 虚拟机来跑满带宽。

### Linux：udev 规则

普通用户默认无权限访问 USB 设备，需安装一次 udev 规则（设备 VID 为 `359f`）：

```bash
sudo tee /etc/udev/rules.d/60-sipeed.rules <<'EOF'
SUBSYSTEM!="usb|usb_device", GOTO="sipeed_rules_end"
ACTION!="add", GOTO="sipeed_rules_end"
ATTRS{idVendor}=="359f", MODE="0666", GROUP="plugdev", TAG+="uaccess", ENV{ID_MM_DEVICE_IGNORE}="1"
LABEL="sipeed_rules_end"
EOF
sudo udevadm control --reload && sudo udevadm trigger
```

> Arch 系统请把 `GROUP="plugdev"` 改为 `GROUP="uucp"`。配置完成后拔插一次设备使规则生效。

### macOS

SLogicView、ngscopeclient 与 sigrok-cli 均提供 macOS 版。若首次运行被系统阻止，在「系统设置 → 隐私与安全性」中放行即可。
