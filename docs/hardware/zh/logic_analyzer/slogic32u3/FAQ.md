---
title: SLogic32U3 常见问题
keywords: SLogic32U3, FAQ, 常见问题, troubleshooting, udev, 驱动, 采样率, DFU
update:
  - date: 2026-10-06
    version: v0.2
    author: Sipeed
    content:
      - 配合文档重构更新内部链接
      - 校正缓存容量与数据流速描述
  - date: 2026-09-30
    version: v0.1
    author: Sipeed
    content:
      - 初始化文档
---

# 常见问题

## 设备与连接

### 为什么找不到 SLogic32U3 设备？

最常见的原因是软件在连接设备之前就已经启动。

解决办法：先连设备再启动上位机；或在软件内打开 **Connect to Device** → 选驱动 → **Scan** → 选中设备。

Linux 上普通用户默认无权限访问 USB 设备，还需要配置 udev 规则，见下文。

### 只亮蓝灯 / 只亮红灯是什么问题？

- **只亮蓝灯**：USB 没有按 USB3 连接。可能是线材不支持 USB3、接了机箱前面板或不兼容的 HUB、供电不足，或线缆过长。
- **只亮红灯**：Flash 加载异常。多为线材质量差导致压降过大，或主机 USB 口故障，也可能是硬件损坏。

正常工作时指示灯应为**青色**（蓝+绿）。完整灯语见[硬件使用指南](./Hardware_Specification.md#act-指示灯)。

## 驱动与权限

### Windows 需要装驱动吗？

**不需要。** SLogic32U3 默认即为 WinUSB 设备，Windows 10/11 即插即用，无需 Zadig 或手动安装驱动。插上设备后直接运行 SLogicView 或 ngscopeclient 即可。

### 如何为 Linux 设置 udev 规则？

SLogic 系列 USB VID 为 `359f`。

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

> Arch 系统请用 `GROUP="uucp"` 替代 `GROUP="plugdev"`。配置完成后拔插一次设备，即可以普通用户身份运行。

### macOS 支持吗？需要额外配置吗？

支持。SLogicView、ngscopeclient 与 sigrok-cli 均提供 macOS 版。若首次运行被系统阻止，在「系统设置 → 隐私与安全性」中放行即可。

## 采集与性能

### 为什么采样率上不去，只能选到某个值？

最大采样率取决于使能的通道数与 USB 带宽。减少通道数即可提高可用采样率，但**只能按固定分组**（4ch=D0–D3、8ch=D0–D7、16ch=D0–D15），**不支持自定义通道**。

对应关系：4ch@1400MHz、8ch@800MHz、16ch@400MHz、32ch@200MHz。详见[软件使用指南 · 采样率与通道数的关系](./Software_User_Guide.md#采样率与通道数的关系)。

### SLogic32U3 用哪种采集模式？

**Stream（流式）模式**：数据实时回传上位机，采集时长理论不限，仅受磁盘容量限制。板载 2 Gbit DDR3 作弹性缓存平滑 USB 传输，实际可持续回传 800 MB/s（6.4 Gbps）。

详见[软件使用指南 · Stream 采集](./Software_User_Guide.md#stream-采集)。

### 出现丢样（dropped samples）怎么办？

- 降低采样率，或减少使能的通道数。
- 使用主板直连的 USB3 口，配高质量短线缆，避免无源 HUB 与机箱前面板接口。
- 关闭其他占用 USB 带宽的大流量设备。

## 解码

### 协议解码结果对不上？

常见原因有三个，按顺序排查：

1. **阈值设置不当**：阈值要匹配被测电路的逻辑电平，3.3 V 逻辑设约 1.6 V。
2. **采样率不足**：采样率至少取信号最高频率的 10 倍。
3. **引脚映射错误**：确认解码器的每个信号对应到正确的通道，例如 SPI 的 MOSI / MISO / SCLK / CS。

解码输出为空只说明当前配置没有产生标注，不能证明波形里没有通信。先回到波形确认电平变化是否正常。

## 固件与模式

### 设备锁定在 DFU 模式，无法切回 SLogic 模式？

通常是 SLogic 固件损坏，多见于 OTA 中断。重新 OTA 刷入正确固件即可恢复。

### 无法进入 DFU 模式，提示 "unknown usb device"？

USB 枚举失败，多因线缆过长或质量差。换一根更短、质量更好的 USB 线即可。

## ADC 示波器模组

### 如何启用示波器（模拟）模式？

在 ngscopeclient 的 UI 中启用。ngscopeclient 现为单二进制程序，全部配置在界面中完成，无需命令行参数。

启用后 32U3 会把 D0–7 / D8–15 / D16–23 / D24–31 合并为 4 路 8-bit 模拟通道 A0–A3，需配合可选 ADC 模组。详见 [ngscopeclient](../ngscopeclient/ngscopeclient.md)。
