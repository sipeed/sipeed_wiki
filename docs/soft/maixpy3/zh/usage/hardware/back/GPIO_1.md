---
title: GPIO
keywords: maixpy3, GPIO
desc: maixpy3 doc: GPIO
---

## 如何使用 GPIO 输出高低电平

GPIO 是可以复用成别的通信接口，对于 MaixPy3 来说并不需要那么麻烦，GPIO 就用来输出高低电平，别的用法后面再说。

下面以 MaixII-Dock 开发板为例子讲述如果使用 MaixPy3 输出高低电平。

通过查看 MaixII-Dock 的引出管脚图可以知道，那些管脚可以直接用来当 GPIO 口使用

![](./../asserts/M2Dock_pin.png)

> 以下代码由于 MaixPy3 还在优化中，可能不能运行，具体的代码到 [github](https://github.com/sipeed/MaixPy3) 上查看

```python
from maix import GPIO
import time
led =GPIO.pin("PH", 14)             # 设置使用 PH 14 管脚
while led:
    led.set_value(0)                # 设置低电平
    time.sleep(0.5)
    print("0", led.get_value())     # 获取管脚当前状态
    led.set_value(1)                # 设置高电平
    time.sleep(0.5)
    print("1", led.get_value())     # 获取管脚当前状态

```

## 什么是 GPIO 
GPIO（英语：General-purpose input/output），通用型之输入输出的简称，功能类似8051的P0—P3，其接脚可以供使用者由程控自由使用，PIN脚依现实考量可作为通用输入（GPI）或通用输出（GPO）或通用输入与输出（GPIO），如当clk generator, chip select等。

既然一个引脚可以用于输入、输出或其他特殊功能，那么一定有寄存器用来选择这些功能。对于输入，一定可以通过读取某个寄存器来确定引脚电位的高低；对于输出，一定可以通过写入某个寄存器来让这个引脚输出高电位或者低电位；对于其他特殊功能，则有另外的寄存器来控制它们。
> 源自[百度百科](https://baike.baidu.com/item/gpio/4723219?fr=aladdin)

## GPIO 的用途

不同系统间的GPIO的确切作用不同。通用常有下面几种：

1. 输出值可写（高=1，低=0）。一些芯片也可以选择驱动这些值的方式，以便支持“线-或”或类似方案（开漏信号线）。
2. 输入值可读（1，0）。一些芯片支持输出管脚回读，这在线或的情况下非常有用（以支持双向信号线）。GPIO控制器可能具有一个输入防故障/防反跳逻辑，有时还会有软件控制。
3. 输入经常被用作中断信号，通常是边沿触发，但也有可能是电平触发。这些中断可以配置为系统唤醒事件，从而将系统从低功耗模式唤醒。
4. 一个GPIO经常被配置为输入/输出双向，根据不同的产品单板需求，但也存在单向的情况。
5. 大多是GPIO可以在获取到spinlock自旋锁时访问，但那些通过串行总线访问的通常不能如此操作（休眠的原因）。一些系统中会同时存在这两种形式的GPIO。
6. 在一个给定单板上，每个GPIO用于一个特定的目的，如监控MMC/SD卡的插入/移除，检查卡写保护状态，驱动LED，配置发送器，串行总线位拆，触发一个硬件看门狗，触发一个开关之类的。

> 原则[电子发烧友论坛](http://www.elecfans.com/emb/jiekou/20171206595752.html)



只需要修改对应的管脚口即可进行高低电平输出，对于图中别的通信使用方式会在后面讲述

对于 GPIO 更多的使用方式，通过查看开发板的规格书得知