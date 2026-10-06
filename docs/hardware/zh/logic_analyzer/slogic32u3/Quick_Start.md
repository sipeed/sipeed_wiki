---
title: SLogic32U3 快速上手
keywords: SLogic32U3, 快速上手, 开箱, 安装, SLogicView, SLogicWeb, udev
update:
  - date: 2026-10-06
    version: v0.1
    author: Sipeed
    content:
      - 从简介中拆出独立的快速上手页
---

# 快速上手

本页用最短路径带你完成第一次采集。硬件细节见[硬件使用指南](./Hardware_Specification.md)，各上位机的完整功能见[软件使用指南](./Software_User_Guide.md)，遇到问题见[常见问题](./FAQ.md)。

---

## 1. 开箱

![包装内含物](./assets/DCIM/whats-in-the-box.jpg)

包装内含：

| 配件 | 数量 | 说明 |
| - | - | - |
| SLogic32U3 主机 | × 1 | CNC 铝合金外壳 |
| Mini-HDMI 同轴探头线 | × 4 | 15 cm 同轴屏蔽线，每条 8 通道，4 条共 32 通道 |
| 逻辑分析仪测试夹 | × 32 | 对应 32 个通道 |
| USB-C 数据线 | × 1 | 含 C 转 A 转接头 |
| 收纳包 | × 1 | 便于携带与归置配件 |
| 标号热缩管 | × 32 | 带通道编号，由用户自行套到对应线上标识通道 |

选配件见[硬件使用指南 · 配件](./Hardware_Specification.md#配件)。

---

## 2. 安装软件

SLogic32U3 有多套上位机可选。**默认用 SLogicView**，它是 Sipeed 自研维护的图形界面，也是本文档的基准。

从 [GitHub Release](https://github.com/sipeed/SLogic/releases/latest) 下载对应平台的包：

| 平台 | 文件后缀 | 说明 |
| - | - | - |
| Windows 10/11 x64 | `SLogicView-SLogic-x.y.z-windows-x86_64.exe` | 运行安装程序 |
| Linux x86_64 | `SLogicView-SLogic-x.y.z-linux-x86_64.AppImage` | `chmod +x` 后直接运行 |
| macOS (Apple Silicon) | `SLogicView-SLogic-x.y.z-macos-arm64.dmg` | 打开 dmg 后把程序拖到「应用程序」 |

> **完全不想装软件？** 直接用浏览器打开 **[slogic.sipeed.com](https://slogic.sipeed.com)**，免安装、免驱动，连安卓手机都能采集。详见[软件使用指南 · SLogicWeb 网页版](./Software_User_Guide.md#slogicweb网页版)。

---

## 3. 配置驱动与权限

| 平台 | 需要做什么 |
| - | - |
| Windows | **不需要**。设备即为 WinUSB 设备，即插即用，无需 Zadig |
| Linux | **必须**配置一次 udev 规则，否则普通用户看不到设备，见[硬件使用指南](./Hardware_Specification.md#linuxudev-规则) |
| macOS | 一般无需配置；若首次运行被阻止，在「系统设置 → 隐私与安全性」中放行 |

---

## 4. 连接设备

> [!WARNING]
> **务必接到 10 Gbps 的 USB 口。** 接口规格直接决定采集速率：
>
> - 接 **USB3.2 Gen2（10 Gbps）** 口才能跑满 800 MB/s，达到标称的采样率组合。
> - 接 USB3.0 / 3.1 Gen1（5 Gbps）口，速率会明显低于预期。
> - **不支持 USB2.0 采集。** 接到 USB2.0 口将无法正常工作。
>
> 电脑上的 10 Gbps 口通常标有 `SS10` 或 `10` 字样。只看蓝色并不可靠，蓝色口很多只是 5 Gbps。请查阅主板或笔记本的接口规格确认。

> [!TIP]
> **优先使用 USB-C 口直连。** 随附线材虽然配了 C 转 A 转接头以兼容 A 口，但转接头本身会带来额外插损，降低信号质量。在性能较弱的电脑上，这可能导致速率跑不满。条件允许时请直接插 USB-C 口。

连接步骤：

1. 用随附 USB-C 线把 SLogic32U3 **直连**电脑的 10 Gbps USB-C 口，避免无源 HUB 与机箱前面板接口。
2. 指示灯亮**青色**（蓝+绿）表示已上电且 USB3 链路正常。
   - 只亮蓝灯说明 USB3 链路没建立，多半是线材或接口不是 USB3，见[常见问题](./FAQ.md)。
3. 把 Mini-HDMI 探头线插到需要的通道组上，接口标号 0~3 依次对应 CH0–7 / CH8–15 / CH16–23 / CH24–31。Mini-HDMI 为防呆接口，只能单向插入。

---

## 5. 接线与接地

![实际使用场景](./assets/DCIM/SLogic32U3-with-laptop.jpg)

- 探头远端每组 8 路用 8 种颜色区分，排列顺序与通道顺序一致，从第一根依次数过去即可。详见[通道配色](./Hardware_Specification.md#通道配色)。
- 把测试夹夹到待测信号上，**每根信号线就近配一根地线**。
- **地线绝不可接到信号线上**，可能损坏设备。
- 频率越高、通道越多，接地越关键。详见[探测与信号完整性](./Hardware_Specification.md#探测与信号完整性)。

---

## 6. 第一次采集

以抓一路 UART 为例：

1. 启动上位机，在左上角选择 **Sipeed SLogic Analyzer** 设备。
2. 设置**采样率**：建议为被测信号频率的 10~100 倍。例如 115200 波特率的 UART，选 10 MHz 足够。
3. 设置**采样深度**（Samples）：先用 1 M 试手。
4. 设置**电压阈值**：按被测逻辑电平，3.3 V 逻辑设约 1.6 V。
5. 只勾选实际接线的通道，通道越少可用采样率越高。
6. 点 **Run** 开始采集。

---

## 7. 查看与解码

![协议解码](./assets/Screenshots/pulseview-multi-decode.jpg)

> 本页配图暂用同源的 PulseView 界面截图，SLogicView 操作一致，后续版本将更新为 SLogicView 实机界面。

1. 采集完成后，用鼠标滚轮缩放、左键拖动浏览波形。
2. 点工具栏的 **Add protocol decoder**，选择 `UART`。
3. 在解码器设置里把 `RX` 映射到实际接线的通道，填入波特率 115200、8 数据位、无校验、1 停止位。
4. 解码结果会以标注形式叠加在波形下方。

---

## 8. 下一步

- 硬件接口、配件、指示灯、固件更新、信号完整性 → [硬件使用指南](./Hardware_Specification.md)
- 各上位机与网页版的区别、触发、解码、命令行 → [软件使用指南](./Software_User_Guide.md)
- GPU 加速与混合信号分析 → [ngscopeclient](../ngscopeclient/ngscopeclient.md)
- 让 AI 代跑采集与解码 → [SLogic 接入 AI Agent](../slogic_agent/readme.md)
- 排障 → [常见问题](./FAQ.md)
