---
title: MaixCAM — Fast Deployment for AI Vision and Audio Projects
---

<div style="width:100%; display:flex;justify-content: center;">

![MaixCAM](https://wiki.sipeed.com/maixpy/static/image/maixcam.png)

</div>

<div style="padding: 1em 0 0 0; display: flex; justify-content: center">
    <a target="_blank" style="margin: 1em;color: white; font-size: 0.9em; border-radius: 0.3em; padding: 0.5em 2em; background-color: #a80202" href="https://item.taobao.com/item.htm?id=784724795837">Taobao</a>
    <a target="_blank" style="margin: 1em;color: white; font-size: 0.9em; border-radius: 0.3em; padding: 0.5em 2em; background-color: #a80202" href="https://www.aliexpress.com/store/911876460">AliExpress</a>
</div>

## Introduction to MaixCAM

MaixCAM is a hardware product designed for the rapid deployment of AI vision, audio, and AIOT applications. It serves as a platform for quickly verifying product prototypes and moving to mass production, featuring a powerful yet cost-effective processor with integrated cameras, screens, WiFi, and a complete, easy-to-use software ecosystem.

<div style="padding: 1em 0 0 0; display: flex; justify-content: left">
    <a target="_blank" style="margin: 1em;color: white; font-size: 0.9em; border-radius: 0.3em; padding: 0.5em 2em; background-color: #a80202" href="https://wiki.sipeed.com/maixpy/">More Features on the MaixPy Homepage</a>
</div>

**Target Use Cases and Audience**:
* **AI Algorithm Deployment**: AI engineers can quickly deploy their AI models on real hardware (MaixCAM) using easy-to-use model conversion tools and SDKs.
* **STEM Education**: With the MaixPy SDK and development tools, teachers can focus on teaching while students quickly get hands-on experience without needing to develop hardware or software.
* **University Research and Education**: Comprehensive documentation and tutorials provide learning paths for students at all levels, while RISC-V and AI technologies offer tools for research.
* **Prototyping for Makers and Engineers**: Well-designed hardware, extensive peripherals, and easy-to-use software let you quickly turn ideas into reality without getting bogged down by basic development tasks.
* **Enterprise Product Upgrades and Deployment**: Quickly deploy products without high R&D costs, or add AI vision to existing equipment for smart enhancements.
* **Competitions**: MaixCAM + MaixPy + MaixCDK provide rapid innovation for competitions. The platform has already been used to win various awards.

## MaixCAM Hardware Overview

MaixCAM hardware info, more info please refer to CPU's datasheet.
And there is another model called [MaixCAM-Pro](./maixcam_pro.md).

| Component          | Description |
|--------------------|-------------|
| CPU Big Core       | 1GHz RISC-V C906 (plus an optional 1GHz ARM A53 for Linux) |
| CPU Small Core     | 700MHz RISC-V C906 running RTOS |
| Low-Power Core     | 25~300MHz 8051 for low-power applications |
| NPU                | 1TOPS@INT8, BF16 model support, operators for popular models like Mobilenetv2, YOLOv5, YOLOv8 |
| Memory             | 256MB DDR3 |
| Storage            | TF card or SD NAND boot |
| Camera             | Up to 5MP, officially supports 4MP GC4653 and OS04A10 (4-lane MIPI CSI, 22-pin interface, supports dual CSI split) |
| Screen             | 2.3" HD IPS touch screen, 552x368 resolution (2-lane MIPI DSI output, 31-pin standard interface, 6-pin capacitive touch) |
| Audio Output       | Onboard PA amplifier for 1W or less speakers |
| Audio Input        | Built-in analog silicon mic for audio input |
| Network            | Onboard WiFi6 + BLE5.4 module, Ethernet versions available |
| USB                | Type-C USB2.0, support device and host mode, support USB camera |
| IO Ports           | 2 x 14-pin 2.54mm headers, 800mil spacing, breadboard-compatible |
| Buttons            | 1 x RST button + 1 x USER (function) button |
| LEDs               | Power LED + User LED |
| Codec              | H.264/H.265/MJPEG hardware decode, supports 2K@30fps encoding/decoding |
| Peripherals        | I2C/SPI/UART/ADC/PWM/WDT |
| Case               | 3D printed with two screw mounts for attaching to stands |

## MaixCAM Software Ecosystem

MaixCAM offers more than just hardware. It comes with a complete software ecosystem, including:

| Name        | Description | Image/Video |
|-------------|-------------|-------------|
| [MaixPy](https://wiki.sipeed.com/maixpy/) | Python SDK optimized for MaixCAM with simple APIs and hardware acceleration | Refer to[MaixPy](https://wiki.sipeed.com/maixpy/) |
| [MaixVision](https://wiki.sipeed.com/maixvision) | AI vision IDE for programming, running code, live image preview, and graphical programming | ![MaixVision](../../assets/maixcam/maixvision.jpg) <video playsinline controls muted preload style="width:100%" src="https://wiki.sipeed.com/maixpy/static/video/maixvision.mp4"></video>|
| [MaixHub](https://maixhub.com) | Online AI model training platform that requires no AI expertise or expensive hardware | ![MaixHub](../../assets/maixcam/maixhub.jpg) |
| [MaixCDK](https://github.com/sipeed/MaixCDK) | C++ version of MaixPy for C/C++ developers | Refer to [MaixCDK](https://github.com/sipeed/MaixCDK) |
| [App Store](https://maixhub.com/app) | Download tools and applications, or upload your own | Refer to [App Store](https://maixhub.com/app) |
| [Share Center](https://maixhub.com/share) | A space for developers to share projects and experiences | Refer to [Share center](https://maixhub.com/share) |

## MaixCAM Documentation

### Official Resources (by Sipeed)
* [MaixCAM Documentation](https://wiki.sipeed.com/maixcam)(This documentation)
* [MaixPy Documentation](https://wiki.sipeed.com/maixpy/) (Python SDK) ([Source Code](https://github.com/sipeed/MaixPy))
* [MaixCDK Documentation](https://github.com/sipeed/MaixCDK) (C/C++ SDK) ([Source Code](https://github.com/sipeed/MaixCDK))
* [System Source Code](https://github.com/sipeed/LicheeRV-Nano-Build)
* [Schematic](https://dl.sipeed.com/shareURL/LICHEE/LicheeRV_Nano/02_Schematic)
* [Camera and Lens Documentation](https://dl.sipeed.com/shareURL/MaixCAM/MaixCAM/Camera)
* [Core Board Hardware Documentation](https://dl.sipeed.com/shareURL/LICHEE/LicheeRV_Nano)
* [MaixCAM Case Model](https://makerworld.com.cn/zh/models/467141)
* [MaixCAM Stand Model](https://makerworld.com.cn/zh/models/467152)

### Chip Documentation

MaixCAM is based on Sipeed's LiecheeRV-Nano core board, which uses the SG2002 chip. The following resources may also be useful:
> Note: While MaixCAM can use documentation from LicheeRV-Nano and SG2002, **LicheeRV-Nano and other SG2002 products cannot use MaixPy, MaixCDK, or MaixVision software.** Please ensure you choose the right product for your development needs.

* [Datasheet](https://github.com/sophgo/sophgo-doc/releases)
* [LicheeRV-Nano Development Board Documentation](https://wiki.sipeed.com/hardware/zh/lichee/RV_Nano/1_intro.html)
* [Toolchain Download](https://sophon-file.sophon.cn/sophon-prod-s3/drive/23/03/07/16/host-tools.tar.gz)
* [Sophon SDK Documentation](https://developer.sophgo.com/thread/471.html)
* [Sophon HDK Documentation](https://developer.sophgo.com/thread/472.html)
* [Sophon TPU Documentation](https://developer.sophgo.com/thread/473.html)
* [Sophon TDL Documentation](https://developer.sophgo.com/thread/556.html)

### Community Resources

* [MaixHub App Store](https://maixhub.com/app)
* [MaixHub Share Plaza](https://maixhub.com/share)
* [makerworld.com](https://makerworld.com/) (recommended) or [makerworld.com.cn](https://makerworld.com.cn) — search for `MaixCAM`
* [Bilibili](https://bilibili.com) — search for `MaixCAM` or `MaixPy`

## Purchase

MaixCAM comes in two versions. For details, please visit [Sipeed Taobao](https://sipeed.taobao.com/) or [AliExpress](https://www.aliexpress.com/store/911876460).

