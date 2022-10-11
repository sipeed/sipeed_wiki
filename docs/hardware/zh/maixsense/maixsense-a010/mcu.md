
# MS-A010 接入 MCU（Maix Bit）

此文详细说明一下 MaixSense-a010 接入 K210 Bit 例程，用户可基于此篇快速进行二次开发。

[Maix Bit 购买链接指路](https://item.taobao.com/item.htm?spm=a230r.1.14.11.681570a1yq4sJD&id=586580351110&ns=1&abbucket=10&mt=)
[]()
![ms_mscu](./assets/ms_mcu.jpg)

## 概述

MS-A010 拥有强大的兼容性，可基于串口协议外接 Maix-I-Bit 这样的单片机开发板或树莓派之类的 linux 开发板来进行二次开发。
MAIX-I-BIT 开发板是 Sipeed Maix 中产品线的一员，基于嘉楠堪智科技的边缘智能计算芯片 K210 (RISC-V 架构 64位双核) 设计的一款 AIOT 开发板。

## 准备工作

首先，我们肯定要各自拥有一个 MS-A010 模组和 Bit 开发板 如果没有的话，接入例程就此停步。
接下来 准备 4pin 端子线以及 USB type-c 线一条。

### 接线教程

接线需要了解 A010 的接口的引脚信息，
