# Tang Nano

## 概述

Lichee Tang Nano是基于高云半导体的小蜜蜂系列GW1NZ-LV1 FPGA设计的简约型开发板。开发板设计小巧精致，将芯片的所有资源都引出，板载Type-C、USB-JTAG、有源晶振、RGB(可接LCD屏、VGA等外设)等，并把所有IO资源引出，方便开发者拓展使用，非常适用于小型数字逻辑的设计和实验。

![](./assets/1k-1.jpg)
![Nano](./assets/1k-2.jpg)

## 参数

Lichee Tang Nano开发板板载的GW1NZ-LV1 FPGA芯片功能非常强大，具有较丰富的逻辑资源，支持多种I/O电平标准，内嵌块状静态随机存储器、锁相环、Flash等资源，是一款具有非易失性的FPGA产品;另外，板载24MHz有源晶振，为FPGA各种时序操作提供了更精准的频率。

| 项目 | 参数 |
| :---: | :---: |
| 核心 | GW1NZ-LV1 FPGA |
| 逻辑单元(LUT4) | 1152 |
| 寄存器(FF) | 864 |
| Block SRAM(bits) | 72K
| B-SRAM块个数| 4 |
| 用户闪存(bits) | 64K |
| 锁相环PLL | 1 |
| I/O Bank总数 | 2 |
| 最多用户I/O数 | 48 |
| 核电压 | 1.2V |


![](./assets/1k-pin.png)


## 资料
[烧录相关使用](/soft/Tang/zh/Tang-Nano-Doc/readme.md)
[资料下载](https://dl.sipeed.com/shareURL/TANG/Nano)