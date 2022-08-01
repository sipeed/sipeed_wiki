---
title: Chip introduction
keywords: MaixII, MaixPy3, Python, Python3, M2dock
desc: maixpy doc: 
---

About V831

In the last year or so, we’ve started to see several camera SoCs with a built-in NPU or SIMD instructions to accelerate face detection, objects detection and so on, starting with the low-resolution Kendryte K210 processor to the 2.5K Ingenic T31 MIPS video processor, or even the 4K capable iCatch V37 camera SoC.

Allwinner introduces several camera processors (V3, V316, S3…) in the past, but none of them included an NPU aka AI accelerator. This has now changed with Allwinner V831 Cortex-A7 Full HD camera SoC also including a small 200 GOPS NPU.

> Copied from [allwinner-v831-ai-full-hd-camera-soc-powers-sochip-v831-development-board](https://www.cnx-software.com/2020/04/28/allwinner-v831-ai-full-hd-camera-soc-powers-sochip-v831-development-board/)

## v831 Chip

![V831_struct.png](./../../../zh/maixII/M2/asserts/V831_struct.png)

## Parameters

| Item          | Specs                                                                            | Addition                   |
| ------------- | -------------------------------------------------------------------------------- | -------------------------- |
| CPU           | Up to 800Mhz                                                                     |                            |
| Video encoder | H.264, up to 1080p@30fps</br>H265, up to 1080p@30fps</br>JPEG, up to 1080p@30fps | ---                        |
| NPU           | 0.2T                                                                             | ---                        |
| EISE          | Up to 1080p@30fps                                                                | ---                        |
| SDRAM         | SIP 64MB DDR2                                                                    | SIP(System In a Package)   |
| SMHC          | SMHC x2 (SDC0, SDC1)                                                             | SD-MMC Host controller     |
| SPI           | SPI x2 (SPI0, SPI1)                                                              | ---                        |
| LCD           | Serial RGB, i8080                                                                | ---                        |
| DSPO          | BT656                                                                            | ---                        |
| I2S           | I2S x1 (I2S0)                                                                    | ---                        |
| Parallel CSI  | No support                                                                       | ---                        |
| Ethernet      | 10/100 Mbit/s Ethernet port with RMII                                            |                            |
| TWI           | TWI x4 (TWI0, TWI1, TWI2, TWI3)                                                  | ---                        |
| RSB           | No support                                                                       | ---                        |
| GPADC         | 1-ch                                                                             | ---                        |
| Audio codec   | Output: LINEOUTP</br>Input: MICIN1P/N                                            | ---                        |
| MIPI CSI      | 2-lane, up to 1080p@60fps                                                        | ---                        |
| MIPI DSI      | No support                                                                       | ---                        |
| Package       | QFN88                                                                            | ---                        |

Click to download [V833／V831 Datasheet V1.0.pdf](https://linux-sunxi.org/images/b/b9/V833%EF%BC%8FV831_Datasheet_V1.0.pdf)

## Support

M2dock meets customer's needs in varieties of scenarios, and has been widely used in AIoT. It also has gained a very good reputation in the industry with its quality and performance. Contact support@sipeed.com for more business help.