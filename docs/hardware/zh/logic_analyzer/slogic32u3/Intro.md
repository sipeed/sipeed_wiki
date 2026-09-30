<!--
维护者说明（不会渲染到站点）：
本页为 SLogic32U3 文档骨架草稿。所有待补内容均以字面量 "TODO" 标记，
可用 `grep -rn TODO docs/hardware/zh/logic_analyzer/slogic32u3` 跟踪待办。
配图占位以 "> 🚧 **TODO(配图)**" 形式给出，并附建议的资源文件名（放在 ./assets/ 下）。
标注 "(待确认)" 的规格需硬件/研发最终核实后去掉标注。
-->
---
title: SLogic32U3 简介
keywords: LogicAnalyzer, SLogic, SLogic32U3, USB3.2, 10Gbps, sigrok, PulseView, ngscopeclient
update:
  - date: 2026-09-30
    version: v0.1
    author: Sipeed
    content:
      - 初始化文档骨架（含已知规格与占位/TODO 待补）
---

# SLogic32U3 简介：全球首款 10Gbps USB3.2 逻辑分析仪

SLogic32U3 是 Sipeed SLogic 系列的旗舰逻辑分析仪。它在铝合金外壳中通过 USB3.2 Gen2（10Gbps 线速）接口实现 32 通道高速 Stream 采集，稳定带宽 6.4Gbps（800MB/s）：1400M@4CH、800M@8CH、400M@16CH、200M@32CH。数字输入支持 0~10V 范围、0~6V 可调阈值，并可选配 4 通道 ADC 模组，让同一台设备兼具采样示波器能力。软件侧同时兼容 sigrok/PulseView、ngscopeclient 与 sigrok-cli，并可接入 AI Agent 自动完成采集与解码。

<div style="text-align:center;">
  <img src="./assets/SLogic32U3-photo.jpg" alt="SLogic32U3" style="max-width:100%;">
</div>

> 🚧 **TODO(配图)**：主视觉产品图（正面 4×Mini-HDMI + USB-C 一侧的清晰照）。建议文件：`assets/DCIM/SLogic32U3-hero.jpg`（当前先复用 `SLogic32U3-photo.jpg`）。

---

## 核心特性

1. **10Gbps USB3.2 Gen2**：全球首款 USB3.2 Gen2 逻辑分析仪，**Stream 模式稳定带宽 6.4Gbps（800MB/s）**，配板载 2Gbit DDR 弹性缓存，在高通道数下仍维持高采样率（各档位见下方规格表）。
2. **32 通道 / 最高 1400MSa/s**：1400M@4CH、800M@8CH、400M@16CH、200M@32CH，覆盖从单总线调试到多路并行总线分析。
3. **可调阈值 + 宽输入范围**：数字输入 0~10V，逻辑阈值 0~6V 可调，适配 1.2V/1.8V/3.3V/5V 等多种逻辑电平。
4. **Mini-HDMI 屏蔽探头**：32 通道分为 4 组、每组 8 通道合并到 1 个 Mini-HDMI 接口，每组按 红/橙/黄/绿/棕/蓝/白/灰 八色循环标识，兼顾高速信号完整性与接线便利。
5. **可选 ADC → 示波器**：选配 4 通道 ADC 模组（8-bit，10MHz 模拟带宽，±15V/±7.5V 量程，AC/DC 耦合可切换 <!-- TODO 采样率 100 还是 200 MSa/s 待确认 -->），同一台设备兼作采样示波器，实现混合信号观测。在 ngscopeclient 的 UI 中启用。
6. **多前端 + 绿色免安装**：PulseView（sigrok）、ngscopeclient、sigrok-cli 任选，无系统级安装、随插随用。
7. **接入 AI Agent**：配合 `sigrok-cli-slogic-plugin`，把通道与协议目标告诉 Agent，即可自动扫描、采集 `.sr` 波形并解码。详见 [SLogic 接入 AI Agent](../slogic_agent/readme.md)。

---

## 技术规格

> 🚧 **TODO**：下表标 **(待确认)** 的条目请研发/硬件最终核实后移除标注；缺失项补齐。

| 项目 | 规格 |
| :--- | :--- |
| 数字通道数 | 32 |
| 最大采样率 | 1400 MSa/s（4CH） |
| 采样率–通道梯度 | 1400M@4CH · 800M@8CH · 400M@16CH · 200M@32CH |
| USB 接口 | USB3.2 Gen2（10Gbps 线速，稳定 6.4Gbps / 800MB/s） |
| 采集模式 | Stream（流式，实时回传）；板载 2Gbit（256MB）DDR 弹性缓存 |
| 输入电压范围 | 0 ~ 10V |
| 可调阈值 (Vth) | 0 ~ 6V，步进 0.1V（低于 Vth 判为 0，高于判为 1） |
| 输入阻抗 | **(待确认)** |
| 最小可捕获脉宽 | ≈0.71 ns（= 1/1400MHz 单采样间隔）**(捕获判定定义待确认)** |
| 触发能力 | 多通道 / 多边沿组合（PulseView、sigrok-cli）；ngscopeclient 集成当前仅单通道单边沿 |
| 采样深度 | Stream 理论无限（受磁盘限制），板载 2Gbit（256MB）DDR 弹性缓存 |
| 可选 ADC 模组 | 4 通道，8-bit，10MHz 模拟带宽，±15V/±7.5V，AC/DC 耦合，采样率 **(待确认)** |
| 接口/连接器 | 4 × Mini-HDMI（每组 8 通道，屏蔽） + USB-C |
| 供电 | USB 供电 **(待确认：功耗与 VCC 输出能力)** |
| 外壳 / 尺寸 | 铝合金，50 × 50 × 10 mm |
| 兼容软件 | sigrok/PulseView、ngscopeclient、sigrok-cli |
| 支持系统 | Windows 10/11 x64、Linux x86_64、macOS |
| 参考价格 | ~¥999 / ~$149 **(待确认：最终定价与众筹档位)** |

---

## SLogic 系列对比

| 属性 | SLogic Combo8 | SLogic16U3 | SLogic32U3 |
| - | - | - | - |
| USB 类型 | USB2.0 | USB3.0 | USB3.2 Gen2 |
| 最大采样率 | 80M | 800M | 1400M |
| 最大通道数 | 8 | 16 | 32 |
| 最大带宽 | 0.3Gbps | 3.2Gbps | 6.4Gbps |
| 典型组合（stream） | 80M@4CH, 40M@8CH | 800M@4CH, 400M@8CH, 200M@16CH | 1400M@4CH, 800M@8CH, 400M@16CH, 200M@32CH |
| 兼容 Sigrok | Y | Y | Y |
| 可调阈值 | N | Y | Y |
| 外壳材质 | 塑料 | 铝合金 | 铝合金 |
| 额外特性 | DAP-Link, CK-Link, 4-UART | | 可选 ADC → 示波器 |
| 尺寸 | 20x40x10mm | 40x40x10mm | 50x50x10mm |
| 价格 | ￥69 | ￥369 | ~￥999 (待确认) |

---

## 生态兼容一览

SLogic32U3 提供 4 种使用方式，按需选择：

| 前端 | 定位 | 适合 |
| - | - | - |
| **PulseView (sigrok)** | 最常用的图形界面 | 日常采集、协议解码、上手最快 |
| **ngscopeclient** | GPU 加速、Filter Graph、混合信号 | 高级分析、配合 ADC 示波器模式 |
| **sigrok-cli** | 命令行 | 自动化 / CI / 无头采集 |
| **AI Agent** | 自然语言驱动 | 让 Agent 代跑扫描/采集/解码 |

> 详细用法见 [用户指南](./UG.md)、[ngscopeclient](../ngscopeclient/ngscopeclient.md) 与 [SLogic 接入 AI Agent](../slogic_agent/readme.md)。

---

## 软件下载

多平台上位机（PulseView / ngscopeclient / sigrok-cli）从 **GitHub Release** 获取最新版；下载站为备份镜像。

- **GitHub Release（推荐，最新）**：https://github.com/sipeed/SLogic/releases/latest
- 下载站（备份镜像）：https://dl.sipeed.com/shareURL/SLogic
- SLogic 版 sigrok-cli（命令行）：`sigrok-cli-SLogic-xxxx.{AppImage,exe,dmg}`
- AI Agent Plugin：`https://dl.sipeed.com/fileList/SLogic/sigrok-cli-slogic-plugin.zip`
- 源代码（libsigrok，slogic-dev 分支）：https://github.com/sipeed/libsigrok/tree/slogic-dev
- libsigrok 驱动名：`sipeed-slogic-analyzer`
- 固件更新工具：**(待确认)** <!-- TODO 类比 slogic16u3-tools，补 32U3 仓库/固件地址 -->

---

## 相关链接

> 🚧 **TODO**：发售后补齐购买与固件下载链接。

- 购买（众筹）：**(待确认)** <!-- Kickstarter -->
- 购买（官方 / 淘宝 / AliExpress）：**(待确认)**
- MaixHub 讨论区：[maixhub.com](https://maixhub.com/discussion/slogic)
- 支持邮箱：support@sipeed.com
- Sipeed GitHub：https://github.com/sipeed
- 社区（Discord）：[discord.gg/V4sAZ9XWpN](https://discord.gg/V4sAZ9XWpN)
