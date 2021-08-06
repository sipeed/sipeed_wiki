---
title: 芯片平台介绍
keywords: MaixII, MaixPy3, Python, Python3, M2dock
desc: maixpy doc: 芯片平台介绍
---

V831 芯片介绍

从 2019 年至今的时间，可以开始看到几个相机 SoC 与一个内置的转专业或 SIMD 指令加快人脸检测、物体检测等等，从低分辨率 Kendryte K210 处理器 2.5 k Ingenic T31 MIPS 视频处理器，甚至 4k 能力 iCatch V37 相机 SoC 。 Allwinner 过去推出了几个摄像头处理器(V3， V316， S3…)，但没有一个包含 NPU (又名 AI 加速器)。现在这已经改变了，Allwinner V831 Cortex-A7 全高清摄像头 SoC 还包括一个小的 200 GOPS NPU 。

> 取自 [allwinner-v831-ai-full-hd-camera-soc-powers-sochip-v831-development-board](https://www.cnx-software.com/2020/04/28/allwinner-v831-ai-full-hd-camera-soc-powers-sochip-v831-development-board/)

## v831 Chip

![V831_struct.png](./asserts/V831_struct.png)

## 参数表

| 项目            | 参数                                                                               | 备注                                  |
| ------------- | -------------------------------------------------------------------------------- | ----------------------------------- |
| CPU           | 最高 800Mhz                                                                        |                                     |
| Video encoder | H.264, up to 1080p@30fps</br>H265, up to 1080p@30fps</br>JPEG, up to 1080p@30fps | ---                                 |
| NPU           | 0.2T                                                                             | ---                                 |
| EISE          | Up to 1080p@30fps                                                                | ---                                 |
| SDRAM         | SIP 64MB DDR2                                                                    | SIP封装（System In a Package系统级封装）     |
| SMHC          | SMHC x2 (SDC0, SDC1)                                                             | 主机控制器（SMHC）接口；物理层规范V2.0，SDIO卡规范V2.0 |
| SPI           | SPI x2 (SPI0, SPI1)                                                              | ---                                 |
| LCD           | Serial RGB, i8080                                                                | ---                                 |
| DSPO          | BT656                                                                            | ---                                 |
| I2S           | I2S x1 (I2S0)                                                                    | ---                                 |
| Parallel CSI  | No support                                                                       | ---                                 |
| Ethernet      | 10/100 Mbit/s Ethernet port with RMII                                            |                                     |
| interface     | ---                                                                              |                                     |
| TWI           | TWI x4 (TWI0, TWI1, TWI2, TWI3)                                                  | ---                                 |
| RSB           | No support                                                                       | ---                                 |
| GPADC         | 1-ch                                                                             | ---                                 |
| Audio codec   | Output: LINEOUTP</br>Input: MICIN1P/N                                            | ---                                 |
| MIPI CSI      | 2-lane, up to 1080p@60fps                                                        | ---                                 |
| MIPI DSI      | No support                                                                       | ---                                 |
| Package       | QFN88                                                                            | ---                                 |
| ---           | ---                                                                              | ---                                 |

[V833／V831 Datasheet V1.0.pdf](https://linux-sunxi.org/images/b/b9/V833%EF%BC%8FV831_Datasheet_V1.0.pdf)

