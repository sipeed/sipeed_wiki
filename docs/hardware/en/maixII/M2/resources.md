---
title: M2dock introduction
keywords: MaixII, MaixPy3, Python, Python3, M2dock
desc: maixpy doc: Onboard resources
---

Maix-II-Dock is positioned as a cost-effective AIOT development board. While supporting conventional Linux development, it also has a unique AI hardware acceleration feature. With the complete software ecosystem provided by Sipeed, you can quickly realize your edge AI application.

* **Hardware**, based on the Allwinner V831 chip, the development board is formed in the form of [core board] + [backplane]. You can use the development board directly, or you can use only the core board to design the backplane according to your needs, which is convenient and fast to complete. development.
* **Software**, in addition to directly using the data provided by Quanzhi for development (some may need to be obtained from Quanzhi), Sipeed provides a very convenient Python SDK ([MaixPy3](/maixpy3)) and C SDK ([libmaix](https://github.com/sipeed/libmaix));
It also provides an online model training service ([MaixHub](https://maixhub.com)), which is convenient for beginners to quickly train usable AI models.
* **Purchase**: [sipeed.aliexpress.com](https://www.aliexpress.com/item/1005002538932487.html)


<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=298543445&bvid=BV1sF411u7xb&cid=586467021&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
</p>


## M2 core board

<img style="max-height: 260px" src="./../../../zh/maixII/M2/asserts/maix_v831.jpg" alt="core_board"/>


> Download hardware reference data from [Sipeed_Maix_II_3101](https://api.dl.sipeed.com/shareURL/MaixII/MaixII-Dock/HDK/Sipeed_MaixII_V831/Sipeed_Maix_II_3101)

### V831 chip brief

Allwinner V831, single-core Cortex-A7 800MHz, 64MiB on-chip DDR2 memory, cost-effective SOC that can run Linux, and supports hardware AI acceleration (0.2Tops computing power), can be used as a normal Linux SOC, and can also be used for edge AI application, see the manual and below for more detailed parameters.

Dataset: [V833／V831 Datasheet V1.0.pdf](https://linux-sunxi.org/images/b/b9/V833%EF%BC%8FV831_Datasheet_V1.0.pdf)

Chip structure:

<img style="max-height: 400px" src="./../../../zh/maixII/M2/asserts/V831_struct.png" alt="V831 structure"/>


### M2 core board details

Compared with Maix-I generation

| Item                    | Maix-I (K210)                        | Maix-II (V831)                                                                 |
| ----------------------- | ------------------------------------ | ------------------------------------------------------------------------------ |
| Main frequency          | 400~600Mhz                           | 800~1000Mhz                                                                    |
| Video encoder           | None                                 | H.264, up to 1080p@30fps<br>H265, up to 1080p@30fps<br>JPEG, up to 1080p@30fps |
| NPU                     | 0.23TOPS<br>support Conv+BN+ACT+POOL | 0.2TOPS<br>support Conv,Inner_Product,Pool,Eltwise,ACT,BN,Split,Concat         |
| Memory                  | 8MB SRAM                             | SIP 64MB DDR2                                                                  |
| Storage                 | 16MB SPI Nor Flash                   | Choosable 16M flash(Blank default)                                             |
| Camera                  | DVP, support 30W pixels max          | 2lane MIPI, Up to 1080P@60fps                                                  |
| Display                 | 8bit MCU LCD                         | 8bit MCU LCD, can use other screen by convert board                            |
| SDIO                    | None                                 | SMHC x2 (SDC0, SDC1)                                                           |
| SPI                     | SPIx3                                | SPI x2 (SPI0, SPI1)                                                            |
| I2C                     | I2C x3                               | I2C x4 (TWI0, TWI1, TWI2, TWI3)                                                |
| I2S                     | 8bit I2S                             | I2S x1 (I2S0)                                                                  |
| Ethernet                | None                                 | 10/100 Mbit/s Ethernet port with RMII interface                                |
| ADC                     | None                                 | 1-ch 6bit LRADC for key                                                        |
| Audio                   | None                                 | LINEOUTP + MICIN1P/N                                                           |
| Development environment | Maixpy/C                             | MaixPy3/linux                                                                  |

## Bottom board

Normally we think the screen panel is the front and camera is back.

![m2dock](./../../../zh/maixII/M2/asserts/m2dock.jpg)

> Download dock board hardware data [Click me](https://api.dl.sipeed.com/shareURL/MaixII/MaixII-Dock/HDK/Sipeed_MaixII_Dock_V831)
> Thanks for net users sharing the [NGFF M.2 B-key footprint for Maix-II module](https://bbs.elecfans.com/jishu_2036119_1_1.html)

### Dock board Specs

![Dock board](./../../../zh/maixII/M2/asserts/M2Dock_pin.jpg)

| Number | Maix II Part                       | Function                                              | Note                                                             |
| ------ | ---------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------- |
| 1      | M.2 B-KEY female slot*1            | Used for connect V831 core board                      | Have connectted with core board when sold                        |
| 2      | Core board M2 copper column nuts*1 | Fix core board with bottom board                      | Have been fixed when sold                                        |
| 3      | Power LED*1                        | Show power state                                      | ---                                                              |
| 4      | State LED*1                        | User programmable led                                 | ---                                                              |
| 5      | CPU Reset button*1                 | Reset V831 chip                                       | ---                                                              |
| 6      | User button*2                      | Change IO voltage value，custome usage                | ---                                                              |
| 7      | Wi-Fi module*1                     | RTL8189FTV，adds Wi-Fi function for this board        | SDIO Interface                                                   |
| 8      | BTB camera interface*1             | Connect BTB camera module                             | Have connectted with bottom board when sold                      |
| 9      | Camera M2 copper column nuts*2     | Fix BTB camera with bottom board                      | Have been fixed when sold                                        |
| 10     | FHD camera*1                       | Default SP2305 Sensor BTB style, 1080P                | Default 6mm focal length M12 lens，can use other Suitable camera |
| 11     | USB to UART chip*1                 | Provide serial port communication                     | ---                                                              |
| 12     | Type-C interface(USB OTG) *1       | Used for V831 otg function                            | Can be used for power supply                                     |
| 13     | Type-C interface(UART) *1          | Used for V831 uart debugging                          | Can be used for power supply                                     |
| 14     | Three-axis accelerometer*1         | I2C interface，can read 3 axes acceleration data      | ---                                                              |
| 15     | MicroSD card slot*1                | Connect microSD card                                  | Default boot from SD card                                        |
| 16     | LCD interface*1                    | FPC0.5mm 24Pin，MCU interface                         |                                                                  |
| 17     | IPS HD screen\*1                   | 1.3 inch IPS screen，resolution 240\*240              | Have connectted with core board when sold                        |
| 18     | IPEX Wi-Fi antenna connector       | IPEX(first generation) Wi-Fi antenna                  | ---                                                              |
| 19     | Extension female header            | Route V831 general IO，used for connecting peripheral | ---                                                              |
| 20     | Speaker connector*1                | MX1.25 2P interface（1.25mm pitch）                   | ---                                                              |
| 21     | Loudspeaker*1                      | 8Ω1W 1609 composite aluminum membrane speakers        | Have connectted with core board when sold                        |
| 22     | Microphone*1                       | Analog electret microphone                            | ---                                                              |

## Resource summary

Hardware: [MaixII Hardware Library](https://api.dl.sipeed.com/shareURL/MaixII/MaixII-Dock/HDK)

software:
* Python SDK: [MaixPy3 software documentation](/maixpy3)
* C SDK: [libmiax](https://github.com/sipeed/libmaix)
* MaixHub model platform (AI model download, online training, project sharing): [MaixHub](https://maixhub.com)
* Allwinner tina-V83x SDK: [Tina-Linux/tina-V83x](https://github.com/Tina-Linux/tina-V83x)
* Toolchain: [dl.sipeed.com](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/Toolchain) or [github](https://github.com/sipeed/libmaix /releases/download/v0.1.0/toolchain-sunxi-musl-pack-2021-01-09.tar.xz)

## Maix-II-Dock Getting Started Development Route Guide

* Because you need a linux system (tina-linx), you need to learn to burn the system image first, just like learning how to reinstall the computer system, so you can start over if you encounter problems, find the "Burn image" article in the left directory to view
<!-- There is no link to the burning system, let users learn to view the left directory -->
* Learn basic Linux operations, such as how to open a terminal, basic terminal commands, and how to transfer files to the development board, such as serial port usage, adb usage, and other basic operations
* Select development language:
  * If you are familiar with C and have some development experience, you can choose to use [libmaix](https://github.com/sipeed/libmaix)
  * If you want to get started quickly and develop in Python, please use [MaixPy3](/maixpy3) and read its documentation carefully
* If you need to use AI functions, you can use it with the [MaixHub](https://maixhub.com) online training platform, and you can share AI models or projects to the platform