<!--
维护者说明（不渲染）：SLogic32U3 常见问题骨架。
待办以 "TODO" 标记。多数条目可迁移自 SLogic16U3 FAQ（已注明 "复用 16U3"），
迁移时请按 32U3 实物核对（设备名、VID、灯语、驱动方式等）。
目标：分类 + "症状→原因→解决" 决策式排障，覆盖使用类问题（竞品 FAQ 多缺）。
-->
---
title: SLogic32U3 常见问题
keywords: SLogic32U3, FAQ, troubleshooting, udev, Zadig, 驱动, 采样率
update:
  - date: 2026-09-30
    version: v0.1
    author: Sipeed
    content:
      - 初始化 FAQ 骨架
---

# SLogic32U3 常见问题

## 设备与连接

### 为什么找不到 SLogic32U3 设备？

> 复用 16U3。

最常见原因是软件在连接设备之前就已启动。解决：先连设备再启动 PulseView；或在软件内打开 "Connect to Device" → 选驱动 → Scan → 选中设备。

Linux 上普通用户默认无权限访问 USB，见下方 udev 规则。

### 只亮蓝灯 / 只亮红灯是什么问题？

> 复用 16U3（待确认 32U3 灯语一致）。

- **只亮蓝灯**：USB 未按 USB3 连接——线材不支持 USB3、接了机箱前面板/不兼容 HUB、供电不足或线缆过长。
- **只亮红灯**：线材质量差压降过大、主机 USB 口故障，或硬件损坏。

## 驱动与权限

### Windows 需要装驱动吗？

**不需要。** SLogic32U3 默认即 WinUSB 设备，Windows 10/11 即插即用，无需 Zadig 或手动装驱动。插上设备后直接运行 PulseView 或 ngscopeclient 即可。

### 如何为 Linux 设置 udev 规则？

> SLogic 系列 USB VID 为 `359f`。

```bash
sudo tee /etc/udev/rules.d/60-sipeed.rules <<EOF
SUBSYSTEM!="usb|usb_device", GOTO="sipeed_rules_end"
ACTION!="add", GOTO="sipeed_rules_end"
ATTRS{idVendor}=="359f", MODE="0666", GROUP="plugdev", TAG+="uaccess", ENV{ID_MM_DEVICE_IGNORE}="1"
LABEL="sipeed_rules_end"
EOF
sudo udevadm control --reload
sudo udevadm trigger
```

> Arch 系统用 `GROUP="uucp"` 替代。之后拔插设备即可以普通用户运行。

### macOS 支持吗？需要额外配置吗？

支持。PulseView、ngscopeclient 与 sigrok-cli 均提供 macOS 版。若首次运行被系统阻止，在「系统设置 → 隐私与安全性」中放行即可。

## 采集与性能

### 为什么采样率上不去 / 只能到某个值？

最大采样率取决于使能通道数与 USB 带宽——**关闭未使用的通道**即可提高可用采样率。详见 [UG · 采样率制约](./UG.md#采样率深度与通道的相互制约)。

### SLogic32U3 用哪种采集模式？

SLogic32U3 为 **Stream（流式）模式**：实时回传、采集时长理论不限（受磁盘限制），板载 2Gbit（256MB）DDR 作弹性缓存，稳定带宽 6.4Gbps（800MB/s）。采样率随使能通道数变化：4ch@1400MHz / 8ch@800MHz / 16ch@400MHz / 32ch@200MHz——只启用需要的通道即可获得更高采样率。详见 [UG · Stream 采集](./UG.md#stream-采集与采样率组合)。

### 出现丢样（dropped samples）怎么办？

- 降低采样率或减少使能通道。
- 用主板直连的 USB3 口 + 高质量短线缆，避免无源 HUB。

## 解码

### 协议解码结果对不上？

常见原因：**阈值设置不当 / 采样率不足 / 引脚映射错误**。逐项核对：阈值匹配 DUT 电平、采样率 ≥ 信号频率 10 倍、引脚映射正确（如 SPI 的 MOSI/MISO/SCLK/CS）。

## 固件与模式

### 装置锁定在 DFU 模式，无法切回 SLogic 模式？

> 复用 16U3。通常是 SLogic 固件损坏（OTA 失败）。解决：重新 OTA 正确固件。

### 无法进入 DFU 模式，提示 "unknown usb device"？

> 复用 16U3。USB 枚举失败，多因线缆过长/质量差。解决：换更短/更好的 USB 线。

## ADC 示波器模组

### 如何启用示波器（模拟）模式？

在 ngscopeclient 的 UI 中启用（ngscopeclient 现为单二进制程序，全部在界面中配置，无需命令行参数）。32U3 会把 D0–7 / D8–15 / D16–23 / D24–31 合并为 4 路 8-bit 模拟通道 A0–A3；需硬件支持外接 ADC 模块。详见 [ngscopeclient](../ngscopeclient/ngscopeclient.md)。

> 🚧 **TODO**：补充在 ngscopeclient UI 中启用/切换模拟模式的具体步骤。

### ADC 模组能和数字采集同时用吗？

> 🚧 **TODO**：确认后补充。

---

> 🚧 **TODO**：随内测反馈持续补充"使用类"高频问题（竞品 FAQ 多只覆盖驱动/售后，这是我们的差异点）。
