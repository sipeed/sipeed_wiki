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

## 接口

![](./../../../assets/NanoKVM/usb/interface.jpg)

## 参数

| 产品 | NanoKVM USB | NanoKVM Cube | USB 采集卡 |
| --- | --- | --- | --- |
| HDMI 画面 | 4K@30fps | 1080P@60fps | 4K@30fps |
| USB 采集 | 1080P@60fps | - | 1080P@60fps |
| 环出 | 4K@30fps | - | 需环出采集卡 |
| 支持键鼠 | 是 | 是 | 否 |
| 无需软件 | 是 | 是 | 否 |
| 延迟 | 50-100ms| 90-230ms | 50-100ms |
| USB 切换器 | 有 | 无 | 无 |
| 功耗 | 5V/0.24A@1.2W | 5V/0.2A@1W | 5V/0.2A@1W |

## 购买入口

[淘宝官方购买地址]() (待上架)
[速卖通购买地址]()(待上架)
[预售页面](https://sipeed.com/nanokvm/usb)

## 产品反馈

如果您在使用过程中有任何问题或建议，请通过以下渠道和我们反馈：

+ [Github issues](https://github.com/sipeed/NanoKVM)
+ [MaixHub 论坛](https://maixhub.com/discussion/nanokvm)
+ QQ 交流群: 703230713
