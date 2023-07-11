---
title: Tang Nano 系列例程
tags: Tang Nano, example, guide
keywords: Tang Nano，example
update:
  - date: 2023-01-09
    author: wonder
    content:
      - 添加 Tang Nano 9K Lushay Labs 跳转链接
---

## 前言

基本上手使用和相关的历程

## Tang Nano

> 板载下载器为CH552

Github: https://github.com/sipeed/Tang-Nano-examples

- [点灯例程](./../Tang-Nano/examples/1_led.md)
- [驱屏教程](./../Tang-Nano/examples/2_lcd.md)

## Tang Nano 1K

Github: https://github.com/sipeed/TangNano-1K-examples

- [点灯例程](./../Tang-Nano-1K/examples/LED.md)
- [驱屏教程](./../Tang-Nano-1K/examples/LCD.md)

## Tang Nano 4K

Github: https://github.com/sipeed/TangNano-4K-example

- [点灯例程](./../Tang-Nano-4K/examples/LED.md) （快速上手）
- [按键标志点灯](https://github.com/sipeed/TangNano-4K-example/tree/main/key_blink)(github)
- [HDMI显示工程](https://github.com/sipeed/TangNano-4K-example/tree/main/hdmi_720p)(github)
- [HDMI 显示摄像头内容](https://github.com/sipeed/TangNano-4K-example/tree/main/camera_hdmi)(github)
- 在Nano 4K上运行GBA的工程：https://github.com/Martoni/GbHdmi
- litex 在 4K 支持：https://github.com/litex-hub/litex-boards

其他： 

- 使用 Cortex-M3 点灯例程：[Github](https://github.com/verilog-indeed/gowin_fpga_tutorials) (英文)

## Tang Nano 9K

Github: https://github.com/sipeed/TangNano-9K-example

- [点灯例程](./../Tang-Nano-9K/examples/LED.md)
- [驱RGB屏教程](./../Tang-Nano-9K/examples/LCD.md)
- [PicoRV 在9K上运行的示例](./../Tang-Nano-9K/examples/picorv.md)
- [FPGA驱动1.14 SPI屏幕工程](./../Tang-Nano-9K/examples/spi_lcd.md)
- HDMI 示例：参考 [PicoRV 在9K上运行的示例](./../Tang-Nano-9K/examples/picorv.md)
- litex 在 9K 支持：https://github.com/litex-hub/litex-boards

[Lushay Labs](https://lushaylabs.com/) 有意做以太网、图形卡或者双核处理器的 FPGA 开发教程计划，有意者可以阅读本文末尾处他们提供的 [部分教程](#lushay-labs) 来了解他们。有兴趣参与项目的话可以发邮件到 `contact@lushaylabs.com` 

## Tang Nano 20K

Github: https://github.com/sipeed/TangNano-20K-example

- [开箱使用](https://wiki.sipeed.com/hardware/zh/tang/tang-nano-20k/example/unbox.html)
- [点灯例程](https://wiki.sipeed.com/hardware/zh/tang/tang-nano-20k/example/led.html)

## 哔哩哔哩视频

> 感谢 [ZQ坐看云起时](https://space.bilibili.com/375786914) 友情制作

<table>
<tr><td><a href="https://www.bilibili.com/video/BV1Jv4y1Q7u6/" target="_blank_">TANG NANO 9K 开发板应用《1: 云源IDE安装》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1MK411z7it/" target="_blank_">TANG NANO 9K 开发板应用《2: 云源软件基本使用》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1HW4y1K7mT/" target="_blank_">TANG NANO 9K 开发板应用《3: 新建FPGA工程》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV19d4y1h7CQ/" target="_blank_">TANG NANO 9K 开发板应用《4：时钟分频器使用之IP调用法》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1YA411X7Tt/" target="_blank_">TANG NANO 9K 开发板应用《5：时钟分频器使用之直接例化法》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1z24y1S7MX/" target="_blank_">TANG NANO 9K 开发板应用《6：38译码器设计与测试》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV19Y411m7XN/" target="_blank_">TANG NANO 9K 开发板应用《7：高云逻辑分析仪之配置篇》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1m24y1S7f2/" target="_blank_">TANG NANO 9K 开发板应用《8：高云逻辑分析仪之使用篇》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1dR4y1U7pJ/" target="_blank_">TANG NANO 9K 开发板应用《9：存储器BSRAM使用方法介绍》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1bv4y1i7Ez/" target="_blank_">TANG NANO 9K 开发板应用《10：高云逻辑分析仪调试BSRAM》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1L24y1i7k8/" target="_blank_">TANG NANO 9K 开发板应用《11：BSRAM设置初始化数据》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1y8411K7ey/" target="_blank_">TANG NANO 9K 开发板应用《12：基于BSRAM的pROM使用》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1hK411y7a4/" target="_blank_">TANG NANO 9K 开发板应用《13：输入时钟CLK信号捕获技巧》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1V8411w7rw/" target="_blank_">TANG NANO 9K 开发板应用《14：基于ST7789芯片1.14寸LCD屏幕驱动》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1534y1f75w/" target="_blank_">TANG NANO 9K 开发板应用《15：基于ST7789芯片LCD寄存器配置和显示》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1Ld4y1n7R4/" target="_blank_">TANG NANO 9K 开发板应用《16: 1.14寸LCD图片显示实验》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1C84y1n7mb/" target="_blank_">TANG NANO 9K 开发板应用《17: 1.14寸LCD图片滚动实验》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV11N411F7i1/" target="_blank_">TANG NANO 9K 开发板应用《18：手搓简易标准SPI驱动及仿真》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1qs4y1V7D4/" target="_blank_">TANG NANO 9K 开发板应用《19：SPI读flash P25Q32HS/W25Q32 芯片ID实验》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1ck4y1h7KZ/" target="_blank_">TANG NANO 9K 开发板应用《20：SPI读写/擦除P25Q32HS/W25Q32实验》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1Nx4y1A7E7/" target="_blank_">TANG NANO 9K 开发板应用《21：串口发送模块的实现》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1yL411S7T5/" target="_blank_">TANG NANO 9K 开发板应用《22：串口接收模块的实现》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1xM411T7kv/" target="_blank_">TANG NANO 9K 开发板应用《23：环形队列(FIFO)的实现》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1Xh4y1p7x7/" target="_blank_">TANG NANO 9K 开发板应用《24：串口转SPI操作flash》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1rc411J7vP/" target="_blank_">TANG NANO 9K 开发板应用《25：串口转SPI文件传输上位机》</a></td></tr>
<tr><td><a href="https://www.bilibili.com/video/BV1BM4y1t7xu/" target="_blank_">TANG NANO 9K 开发板应用《26：PWM》</a></td></tr>
</table>
<table>
<tr><td><a href="https://www.bilibili.com/video/BV1iA411R7Zi/" target="_blank_">iverilog + gtkwave 开源仿真工具《1：软件安装篇》</a></tr></td>
<tr><td><a href="https://www.bilibili.com/video/BV18y4y1R7eu/" target="_blank_">iverilog + gtkwave 开源仿真工具《2：计数器仿真实验》</a></tr></td>
</table>

## 其他上手说明

Tang Nano 9K 合作代理教程(英文)：

### Lushay Labs

<a href="https://learn.lushaylabs.com/tang-nano-series/"><img src="./assets/lushaylab_logo.png" alt="lushaylab_logo" width="35%"></a>

1. [Installation & Getting Started](https://learn.lushaylabs.com/getting-setup-with-the-tang-nano-9k/)
2. [Debugging & UART](https://learn.lushaylabs.com/tang-nano-9k-debugging/)
3. [OLED 101](https://learn.lushaylabs.com/tang-nano-9k-graphics/)
4. [Creating a Text Engine](https://learn.lushaylabs.com/tang-nano-9k-creating-a-text-engine/)
5. [Data Conversion & Visualization](https://learn.lushaylabs.com/tang-nano-9k-data-visualization/)
6. [Reading from the External Flash](https://learn.lushaylabs.com/tang-nano-9k-reading-the-external-flash/)
7. [Generating Random Numbers](https://learn.lushaylabs.com/tang-nano-9k-generating-random/)
8. [Sharing Resources](https://learn.lushaylabs.com/tang-nano-9k-sharing-resources/)
9. [I2C, ADC and Micro Procedures](https://learn.lushaylabs.com/i2c-adc-micro-procedures/)
10. [Our First CPU](https://learn.lushaylabs.com/tang-nano-9k-first-processor/)

## 结语

有问题可以在相关页面下面留言，或者加入 QQ 群讨论，常见问题已被收录。

QQ 群：834585530
常见问题: [点我](https://wiki.sipeed.com/hardware/zh/tang/Tang-Nano-Doc/questions.html)