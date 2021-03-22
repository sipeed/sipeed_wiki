---
title: MaixDuino
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: MaixDuino
---


## 概述

  SIPEED MaixDuino 是基于我们 M1 模块(主控:Kendryte K210)开发的一款外形兼容 Arduino 的开发板
  <br/>MaixDuino 集成摄像头、TF卡槽、用户按键、TFT显示屏、MaixDuino 扩展接口等, 用户可使用 MaixDuino 轻松搭建一款人脸识别门禁系统, 同时还预留开发调试接口, 也能将其作为一款功能强大的 AI 学习开发板.

## 外观及功能介绍

### 外观一览

![MaixDuino](../../assets/hardware/maix_duino/maixduino_4.png)

### 板载功能

| 项目             | 说明                                              |
| ---------------- | ------------------------------------------------- |
| CPU：            | 双核 64bit RISC-V / 400MHz* (双精度FPU集成)       |
| 内存：           | 8MiB 64bit 片上 SRAM                              |
| 存储：           | 16MiB Flash, 支持 micro SDXC 拓展存储 (最大128GB) |
| 屏幕（套餐）：   | 2.4 寸 TFT, 屏幕分辨率：320\*240          |
| 摄像头（套餐）： | 30W 像素 GC0328 摄像头                            |
| DVP：            | 标准 Camera DVP 24PIN 接口                        |
| 电源+USB：       | USB Type-C 接口                                   |
| ESP32：          | ESP32 SPI 连接(ESP32 支持 WIFI 与 蓝牙)，PAM8403A |
| DAC：            | I2C DAC                                           |
| TF 卡槽：        | 多媒体资源扩展，支持大容量储存                    |

### 引脚资源

![MaixDuino](../../assets/hardware/maix_duino/sipeed_maixduin_pins.png)

## 资料下载

Sipeed-Maix-Duino 资料下载：[Sipeed-Maix-Duino](https://dl.sipeed.com/shareURL/MAIX/HDK/Sipeed-Maixduino/)

Sipeed-Maix-Duino 规格书下载：[Sipeed-Maix-Duino](https://dl.sipeed.com/shareURL/MAIX/HDK/Sipeed-Maixduino/Specifications)

Sipeed-Maix-Duino 原理图下载：[Sipeed-Maix-Duino][Sipeed-Maix-Duino]

[Sipeed-Maix-Duino]: https://dl.sipeed.com/fileList/MAIX/HDK/Sipeed-Maixduino/Maixduino_2832/Maixduino_2832(Schematic).pdf