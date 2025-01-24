---
title: 简介
keywords: NanoKVM, Remote desktop, tool, USB 
update:
  - date: 2024-12-25
    version: v0.1
    author: xwj
    content:
      - Release docs
---

## 简介

![](./../../../assets/NanoKVM/usb/NanoKVM-USB.png)

NanoKVM-USB是一款便捷的运维/多设备协同工具，它可以无需键鼠设备和显示器，仅使用手边的一台电脑无需下载软件，通过Chrome浏览器即可图形化开始运维工作。

NanoKVM-USB 捕捉HDMI图像信号，通过USB3.0传输给HOST主机，与普通USB采集卡不同的是，NanoKVM-USB同时捕捉HOST端的键鼠操作，同步给目标主机，无需传统连接屏幕键鼠的方式，就可以完成所有操作。同时支持一路HDMI环出，最高支持4K@30HZ，方便外连大屏。
值得一提的是，NanoKVM-USB自带一个USB-A端口，支持HOST/TARGET两侧切换，当外接U盘时候可以方便的在两台电脑之间转移数据，此外更多功能请自由探索。

![](./../../../assets/NanoKVM/usb/wiring.png)

## 使用场景

![](./../../../assets/NanoKVM/usb/use-cases.jpg)

## 接口

![](./../../../assets/NanoKVM/usb/interface.jpg)

## 参数对比

|  | NanoKVM-USB | Mini-KVM | KIWI-KVM |
| --- | --- | --- | --- |
| HDMI 输入 | 4K@30fps | 1080P@60fps | 4K@30fps |
| HDMI 环出 | 4K@30fps | None | None |
| USB 采集 | 2K@30fps | 1080P@60fps | 1080P@60fps |
| USB 接口 | USB3.0 | USB2.0 | USB3.0 |
| USB 切换器 | 有 | 有 | 无 |
| 模拟键鼠 | 支持 | 支持 | 支持 |
| 剪贴板 | 支持 | 支持 | 支持 |
| 软件 | 无需安装，在 Chrome 中运行 | 需要安装 | 需要安装 |
| 延迟 | 50-100ms | 50-100ms | 50-100ms |
| 体积 | 57x25x23mm | 61x13.5x53mm | 80x80x10mm |
| 外壳 | 铝合金 | 铝合金 | 塑料 |
| 颜色 | 黑/蓝/红 | 黑 | 黑 |
| 价格| `$39.9 / $49.9` | `$89 / $109` | `$69 / $99` |

<div style="display: flex; padding: 30px 0 20px 0">
  <img src="./../../../assets/NanoKVM/usb/black.png" width="200" height="150" alt="Image 1" style="margin-right: 10px;">
  <img src="./../../../assets/NanoKVM/usb/blue.png" width="200" height="150" alt="Image 1" style="margin-right: 10px;">
  <img src="./../../../assets/NanoKVM/usb/red.png" width="200" height="150" alt="Image 1" style="margin-right: 10px;">
</div>

## 购买入口

- [淘宝官方购买地址]() (待上架)
- [速卖通购买地址]()(待上架)
- [预售页面](https://sipeed.com/nanokvm/usb)

## 产品反馈

如果您在使用过程中有任何问题或建议，请通过以下渠道和我们反馈：

- [Github issues](https://github.com/sipeed/NanoKVM)
- [MaixHub 论坛](https://maixhub.com/discussion/nanokvm)
- QQ 交流群: 703230713
