<!--
维护者说明（不渲染）：SLogic32U3 快速上手骨架。
待办以 "TODO" 标记；配图占位以 "> 🚧 **TODO(配图)**" 给出。
本页目标：动词式 5 分钟闭环——开箱→装软件→装驱动→接线→第一次采集→看结果。
深入内容一律链到 UG.md，不在本页展开。
-->
---
title: SLogic32U3 快速上手
keywords: SLogic32U3, Quick Start, PulseView, sigrok, 上手
update:
  - date: 2026-09-30
    version: v0.1
    author: Sipeed
    content:
      - 初始化快速上手骨架
---

# SLogic32U3 快速上手

本页用最短路径带你完成第一次采集。深入配置、原理与全部功能见[用户指南](./UG.md)；遇到问题见[常见问题](./FAQ.md)。

## 开箱

> [!NOTE]
> **📷 配图待补（TODO）**：开箱全家福（配件清单定稿后拍摄）。
> 文件：`assets/DCIM/unboxing.jpg`｜要求：俯拍平铺、所有配件入镜。

一套完整硬件包含 **SLogic32U3 主机** 与以下附件：

> 🚧 **TODO**：确认最终配件清单与数量（下表为占位，请按实物修正）。

- SLogic32U3 主机 × 1
- Mini-HDMI 屏蔽探头线 × **(待确认)**（对应 4 组通道）
- 逻辑分析仪测试夹 × **(待确认)**
- USB-C 数据线（USB3 规格）× 1
- 可选：ADC 示波器模组 × **(待确认)**
- **(待确认：卡针 / 说明卡 / 收纳包等)**

## 安装软件（PulseView）

SLogic32U3 为绿色便携软件，无系统级安装。从 [GitHub Release](https://github.com/sipeed/SLogic/releases/latest) 下载对应平台的最新版（下载站为备份镜像，见 [Intro · 软件下载](./Intro.md#软件下载)）。

| 平台 | 操作 |
| - | - |
| Windows 10/11 | 解压便携包，双击 `pulseview.exe` |
| Linux x86_64 | `chmod +x Pulseview.appimage && ./Pulseview.appimage` |
| macOS | 打开 `Pulseview.dmg` 直接运行 |

> 🚧 **TODO(配图)**：三平台各一张软件启动截图。建议：`assets/Screenshots/pv-win.png` / `pv-linux.png` / `pv-macos.png`

## 安装驱动 / 配置权限

不同平台首次使用需要一次性配置，否则软件可能扫描不到设备。

- **Windows**：**免驱**——SLogic 默认即 WinUSB 设备，Windows 10/11 即插即用，无需 Zadig。详见 [UG · 驱动与安装](./UG.md#驱动与安装)。
- **Linux**：需安装 udev 规则（设备 VID `359f`），否则普通用户无权限访问 USB。见 [UG · Linux udev 规则](./UG.md#linux-udev-规则)。
- **macOS**：支持；若首次运行被系统阻止，在「系统设置 → 隐私与安全性」放行。

## 接线与接地

> 🚧 **TODO(配图)**：接线示意图（Mini-HDMI 探头方向 + 信号/GND 对应）。建议：`assets/MISC/wiring.jpg`

1. 用 USB-C 线把 SLogic32U3 直连电脑的 **USB3** 口（避免无源 HUB / 机箱前面板）。
2. 将 Mini-HDMI 屏蔽探头线插入对应通道组（Mini-HDMI 为防呆接口，只能单向插入）；探头远端每组 8 路信号按 红/橙/黄/绿/棕/蓝/白/灰 八色循环区分。
3. 把待测信号接到任一空闲 **CH**，并**务必将被测设备 GND 与 SLogic GND 相连**。
4. 高速信号建议**每根信号线就近配一根地线**——详见 [UG · 探测与信号完整性](./UG.md#探测与信号完整性)。

## 第一次采集（以 UART 为例）

以采集一路 115200 8N1 的 UART 为例：

1. 连接设备后启动 PulseView，确认设备被自动识别（未识别见 [FAQ](./FAQ.md#为什么找不到-slogic32u3-设备)）。
2. 只使能用到的通道（如 D0），其余关闭以留出带宽余量。
3. 设置**电压阈值**匹配 DUT 电平（如 3.3V 逻辑设 ~1.6V）。
4. 选择合适的**采样率**（经验：≥ 信号最高频率的 10 倍；本例 115200 UART 选 10M 即可）。
5. 点击采集。

> 🚧 **TODO(配图)**：采集参数设置面板 + 采到的波形各一张。建议：`assets/Screenshots/qs-capture-cfg.png` / `qs-uart-wave.png`

## 看结果并解码

1. 打开 Decoder 面板，添加 **UART** 解码器。
2. 配置引脚映射（RX/TX）、波特率 115200、8N1。
3. 波形上会标注解码出的字符。

> 🚧 **TODO(配图)**：UART 解码标注结果。建议：`assets/Screenshots/qs-uart-decode.png`

---

## 下一步

- 想深入采集模式 / 触发 / 更多协议：[用户指南](./UG.md)
- 想用 GPU 加速界面或 ADC 示波器模式：[ngscopeclient](../ngscopeclient/ngscopeclient.md)
- 想让 AI 代跑采集与解码：[SLogic 接入 AI Agent](../slogic_agent/readme.md)
- 遇到问题：[常见问题](./FAQ.md)
