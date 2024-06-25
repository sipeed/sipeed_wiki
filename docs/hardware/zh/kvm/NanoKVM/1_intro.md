---
title: LicheeRV Nano
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2024-6-21
    version: v0.1
    author: BuGu
    content:
      - Release docs
---

## 简介
Lichee NanoKVM 是基于 LicheeRV Nano 的 IP-KVM 产品，继承了 LicheeRV Nano的极致体积 和 强大功能。
Lichee NanoKVM分为两个版本：
NanoKVM Lite 为基础版配置，适合 具有一定DIY能力的个人用户 和 有批量需求的企业用户。
NanoKVM Full 为完整版配置，带精致外壳和完整配件，内置开机即用的系统镜像卡，推荐个人用户购买。

![](./../assets/RV_Nano/intro/RV_Nano_1.jpg)

## 参数

| 产品 | NanoKVM (Lite) | NanoKVM (FULL) | PiKVM V4 |
| --- | --- | --- | --- |
| 计算单元                | LicheeRV Nano(RISCV) | LicheeRV Nano(RISCV) | CM4 (ARM) |
| 分辨率                  | 1080P @ 60fps | 1080P @ 60fps | 1080P @ 60fps |
| 视频编码                | MJPEG, H264(developing) | MJPEG, H264(developing) | MJPEG, H264 |
| 视频延迟                |                |                | 100～140ms |
| UEFI/BIOS               | ✓ | ✓ | ✓ |
| 模拟USB键鼠 <br>Virtual HID | ✓ | ✓ | ✓ |
| 模拟USB存储 <br> Virtual CD-ROM | ✓ | ✓ | ✓ |
| IPMI      | ✓ | ✓ | ✓ |
| Wake-on-LAN | ✓ | ✓ | ✓ |
| ATX电源控制 | 无，用户可自行连接 | USB接口IO控制板 | RJ45接口IO控制板 |
| OLED显示 | 无，用户可自行扩展 | 128x64 0.96" white | 128x32 0.91" white |
| 外接串口 | 2路 | 2路 | 1路 |
| TF卡 | 无，用户自备 | 有，开机即用 | 有 |
| 扩展配件 | 无 | WiFi 或 PoE | WiFi/LTE |
| 功耗 | 0.2A@5V | 0.2A@5V | Peak 2.6A@5V |
| 电源输入 | PC USB即可供电 | PC USB即可供电 <br> 也支持额外辅助供电 | 需要DC 5V 3A供电 |
| 散热 | 静音无风扇 | 静音无风扇 | 需要风扇主动散热 |
| 尺寸 | 23x37x15mm <br> ～1/30 PiKVM V4 体积 | 40x36x36mm <br/> ～1/7 PiKVM V4 体积 | 120x68x44mm |

![](./../assets/RV_Nano/intro/RV_Nano_3.jpg)

![](./../assets/RV_Nano/intro/RV_Nano_4.jpg)


## 硬件资料

NanoKVM 基于 Sipeed 的 [LicheeRV Nano](https://wiki.sipeed.com/hardware/zh/lichee/RV_Nano/1_intro.html) 核心板搭建，这部分硬件的规格书、原理图、尺寸图等均可在这里找到：[点击这里](http://cn.dl.sipeed.com/shareURL/LICHEE/LicheeRV_Nano)

NanoKVM Lite 由 LicheeRV Nano E 和 HDMItoCSI 小板构成，NanoKVM FULL 在 NanoKVM Lite 基础上增加 NanoKVM-A/B 板和外壳。HDMItoCSI板用于转换HDMI信号；NanoKVM-A 包含 OLED、ATX控制输出（TypeC接口形式）、辅助供电（TypeC接口）以及ATX开关机、复位按键；NanoKVM-B 一端连接A板，一端连接电脑ATX针脚，用于电脑的远程开关机

+ [板卡规格书](http://cn.dl.sipeed.com/shareURL/LICHEE/LicheeRV_Nano/01_Specification)

## 软件资料

+ [LicheeRV Nano SDK](https://github.com/sipeed/LicheeRV-Nano-Build)

