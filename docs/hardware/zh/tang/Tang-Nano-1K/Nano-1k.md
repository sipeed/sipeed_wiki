# Tang Nano 1K

## 概述

Tang Nano 1K 是基于高云半导体的小蜜蜂系列 GW1NZ-LV1 FPGA设计的简约型开发板。开发板设计小巧精致，将芯片的所有资源都引出，板载Type-C、USB-JTAG、有源晶振、RGB(可接LCD屏、VGA等外设)等，并把所有IO资源引出，方便开发者拓展使用，非常适用于小型数字逻辑的设计和实验。

![Nano-1](./../Tang-Nano/assets/1k-1.jpg)
![Nano-2](./../Tang-Nano/assets/1k-2.jpg)

## 参数

Tang Nano 1K 开发板板载的 GW1NZ-LV1 FPGA芯片功能非常强大，具有较丰富的逻辑资源，支持多种 I/O 电平标准，内嵌块状静态随机存储器、锁相环、Flash 等资源，是一款具有非易失性的 FPGA 产品;另外，板载 27MHz 有源晶振，为 FPGA 各种时序操作提供了更精准的频率。

|       项目       |      参数      |
| :--------------: | :------------: |
|       核心       | GW1NZ-LV1 FPGA |
|  逻辑单元(LUT4)  |      1152      |
|    寄存器(FF)    |      864       |
| Block SRAM(bits) |      72K       |
|   B-SRAM块个数   |       4        |
|  用户闪存(bits)  |      64K       |
|    锁相环PLL     |       1        |
|   I/O Bank总数   |       2        |
|  最多用户I/O数   |       48       |
|      核电压      |      1.2V      |

### 引脚图

![pin_map](./../Tang-Nano/assets/1k-pin.png)

## 资料

- [相关例程](./../Tang-Nano-Doc/examples.md)
- [资料下载](https://dl.sipeed.com/shareURL/TANG/Nano%201K)
- [原理图](https://dl.sipeed.com/shareURL/TANG/Nano%201K/2_Schematic)

## 补充

1. 如果有什么疑问，欢迎加群 `834585530`, 或者去[论坛](bbs.sipeed.com)发帖。
2. 下载 FPGA 是要求使用 [这里](https://dl.sipeed.com/shareURL/TANG/programmer) 的 Programmer 软件。不然有极大概率不能下载固件到板子。
3. 有问题的话先去 [常见问题](./../Tang-Nano-Doc/questions.md) 自查，通常来说使用 [这里](https://dl.sipeed.com/shareURL/TANG/programmer) 的 Programmer 软件能解决 99% 问题。
