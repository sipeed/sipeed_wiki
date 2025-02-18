---
title: MaixCAM-Pro -- Rapid Deployment of AI Vision and Auditory Applications
---

<div style="width:100%; display:flex;justify-content: center;">

![maixcam-pro](/static/image/maixcam_pro.png)

</div>

<div style="padding: 1em 0 0 0; display: flex; justify-content: center">
    <a target="_blank" style="margin: 1em;color: white; font-size: 0.9em; border-radius: 0.3em; padding: 0.5em 2em; background-color: #a80202" href="https://item.taobao.com/item.htm?id=846226367137">Taobao</a>
    <a target="_blank" style="margin: 1em;color: white; font-size: 0.9em; border-radius: 0.3em; padding: 0.5em 2em; background-color: #a80202" href="https://www.aliexpress.com/store/911876460">AliExpress</a>
</div>


## Introduction to MaixCAM-Pro

MaixCAM is a hardware product designed for the rapid implementation of AI vision, auditory, and AIoT applications. It serves as a platform for quickly verifying product prototypes and rapid mass production. MaixCAM-Pro provides a powerful yet cost-effective processor, along with accessories such as a camera, display, WiFi, and a comprehensive, easy-to-use software ecosystem.

<div style="display: flex; justify-content: left">
    <a target="_blank" style="margin: 1em;color: white; font-size: 0.9em; border-radius: 0.3em; padding: 0.5em 2em; background-color: #a80202" href="https://wiki.sipeed.com/maixpy/">For more usage, visit MaixPy</a>
</div>

**Application Scenarios and Target Audience**:
* **AI Algorithm Implementation**: AI algorithm engineers can quickly deploy their AI models onto hardware (MaixCAM) with easy-to-use model conversion tools and SDK.
* **STEM Education**: Offers an easy-to-use MaixPy SDK and development tools, as well as an online model training platform, allowing teachers to focus on teaching without the need for software or hardware development, enabling students to get started quickly.
* **University Research and Education**: Provides rich documentation and tutorials suitable for students at all levels, with RISC-V and AI frontier technologies being helpful for research purposes.
* **A Powerful Tool for Maker and Engineer Prototyping**: Thoughtfully designed hardware, rich peripherals, and extremely easy-to-use software help quickly bring your creative ideas and products to life without getting bogged down in basic software and hardware development.
* **Enterprise Product Upgrades and Deployment**: Quickly deploy products without expensive R&D costs, or use them as an auxiliary tool, for example, in production line QA, or for adding AI vision capabilities to legacy equipment.
* **Competition Assistant**: MaixCAM + MaixPy + MaixCDK can quickly implement various innovations and functions, making it suitable as a designated platform for competitions. Maix products and MaixPy have already been used in various competitions and have won awards.


## Overview of MaixCAM-Pro Hardware

> Compared with [MaixCAM](./README.md), MaixCAM-Pro has redesigned PCB and casing, and upgraded some peripherals. Differences with MaixCAM are in **bold**.

| Component | Description |
| --- | --- |
| CPU Main Core | 1GHz RISC-V C906 processor (plus an optional 1GHz ARM A53 core), running Linux |
| CPU Small Core | 700MHz RISC-V C906, running RTOS |
| CPU Low Power Core | 25~300MHz 8051 processor for low-power applications |
| NPU | 1TOPS@INT8, supports BF16 models, supports operators for common models such as Mobilenetv2, YOLOv5, YOLOv8 |
| Memory | 256MB DDR3 |
| Storage | TF card boot / SD NAND boot |
| Camera | Supports up to 5MP camera, officially supports 4MP GC4653 and OS04A10 cameras (4-lane MIPI CSI input, 22-pin interface, dual CSI split supported) |
| Display | **2.4-inch high-definition IPS capacitive touch screen, resolution 640x480** (2-lane MIPI DSI output, standard 31-pin interface, 6-pin capacitive touch) |
| Audio Output | Built-in PA amplifier + **1W speaker** |
| Audio Input | Built-in analog silicon microphone for direct voice recording |
| Network | Onboard WiFi6 + BLE5.4 module, customizable Ethernet version |
| USB                | Type-C USB2.0, support device and host mode, support USB camera |
| IO Interface | **2.54mm PMOD interface, 12 IO + Vsys/3.3v/GND interface + 1.25mm 6-pin extension interface** |
| Buttons | 1 x RST button + 1 x USER (function) button + **1 x power button** |
| LED | Power indicator + User LED + **illumination LED** |
| Codec | H.264 / H.265 / MJPEG hardware decoding, supports 2k@30fps encoding and decoding |
| Peripherals | I2C/SPI/UART/ADC/PWM/WDT, etc. |
| Power | **Independent power management chip AXP2101, supports lithium battery charging and discharging, available with lithium battery version** |
| Case | **3D-printed acrylic case, standard 1/4 inch threaded hole** |
| IMU | **Onboard six-axis IMU sensor (3-axis accelerometer + 3-axis gyroscope)** |
| RTC | **Onboard BM8653 RTC chip + button cell, keeps time even when powered off** |
| Dimensions | **No-battery version: 67x51x12mm, battery version thickness: 16mm**  |


## MaixCAM Software Ecosystem

We don't just provide hardware; MaixCAM comes with a complete software ecosystem, including:

| Name | Description | Image/Video |
| --- | --- | --- |
| **[MaixPy](https://wiki.sipeed.com/maixpy/)** | Python development package with rich and easy-to-use APIs optimized for MaixCAM, supporting hardware acceleration, with extensive documentation and tutorials | Visit [MaixPy homepage](https://wiki.sipeed.com/maixpy/) |
| [MaixVision](https://wiki.sipeed.com/maixvision) | AI vision IDE for programming, code execution, real-time image preview, even graphical programming, lowering development and usage thresholds | ![MaixVision](../../assets/maixcam/maixvision.jpg)  <video playsinline controls muted preload style="width:100%" src="https://wiki.sipeed.com/maixpy/static/video/maixvision.mp4"></video> |
| [MaixHub](https://maixhub.com) | Online AI model training platform that allows training and deployment of models with a single click, without needing AI knowledge or expensive training equipment | ![MaixVision](../../assets/maixcam/maixhub.jpg) |
| [MaixCDK](https://github.com/sipeed/MaixCDK) | C++ version of MaixPy for developers familiar with C/C++ to get started immediately | Visit [MaixCDK homepage](https://github.com/sipeed/MaixCDK) |
| [App Store](https://maixhub.com/app) | Provides various applications and tools for direct download and use, allowing developers to share their apps | Visit [MaixHub App Store](https://maixhub.com/app) |
| [Community Plaza](https://maixhub.com/share) | Developers share their projects and experiences | Visit [MaixHub Community Plaza](https://maixhub.com/share) |


## Resource Summary

### MaixCAM Exclusive Resources (Provided by Sipeed)

* [MaixCAM-Pro Official Documentation](https://wiki.sipeed.com/maixcam-pro) (This documentation)
* [MaixPy Official Documentation](https://wiki.sipeed.com/maixpy/) (Python SDK) ([MaixPy Source Code](https://github.com/sipeed/MaixPy))
* [MaixCDK](https://github.com/sipeed/MaixCDK) (C/C++ SDK) ([MaixCDK Source Code](https://github.com/sipeed/MaixCDK))
* [System Source Code](https://github.com/sipeed/LicheeRV-Nano-Build)
* [Hardware-related Materials](https://dl.sipeed.com/shareURL/MaixCAM/MaixCAM_Pro)
* Case and Stand: See [Case Documentation](./assemble.md). The casing and bracket 3D model files are also open source. Please visit [makerworld.com](https://makerworld.com/) (recommended) or [makerworld.com.cn](https://makerworld.com.cn) and search for `MaixCAM`.
* Interface Diagram:
![maixcam_pro_io](../../assets/maixcam/maixcam_pro_io.png)


### Chip Resources

MaixCAM-Pro is based on the Sophgo SG2002 chip, so the related documents can also be referenced, along with the documents of Sipeed's LicheeRV-Nano core board.
>! Note: MaixCAM-Pro can use the documents of LicheeRV-Nano and SG2002. **LicheeRV-Nano and other SG2002-based products cannot use MaixPy, MaixCDK, or MaixVision software**, so please make sure you purchase the correct product to avoid wasting time and money.
> If you want to get started developing applications quickly, choose MaixCAM. If you are an experienced Linux developer interested in developing based on original SG2002 resources, you may consider choosing LicheeRV-Nano.

* [Datasheet](https://github.com/sophgo/sophgo-doc/releases) (Register-level data)
* [LicheeRV-Nano Development Board Documentation](https://wiki.sipeed.com/hardware/zh/lichee/RV_Nano/1_intro.html)
* [Toolchain Download](https://sophon-file.sophon.cn/sophon-prod-s3/drive/23/03/07/16/host-tools.tar.gz)
* [Sophgo SDK Development Documentation Summary](https://developer.sophgo.com/thread/471.html)
* [Sophgo HDK Development Documentation Summary](https://developer.sophgo.com/thread/472.html)
* [Sophgo TPU Development Documentation Summary](https://developer.sophgo.com/thread/473.html)
* [Sophgo TDL Development Documentation Summary](https://developer.sophgo.com/thread/556.html) (High-level API encapsulation based on TPU)

### Community Resources

* [MaixHub App Store](https://maixhub.com/app)
* [MaixHub Community Plaza](https://maixhub.com/share)
* [makerworld.com](https://makerworld.com/) (recommended) or [makerworld.com.cn](https://makerworld.com.cn), search for `MaixCAM`
* [Bilibili](https://bilibili.com) - Search for `MaixCAM` or `MaixPy`

## Purchase

* [Sipeed Taobao](https://sipeed.taobao.com/)
* [AliExpress](https://www.aliexpress.com/store/911876460)

