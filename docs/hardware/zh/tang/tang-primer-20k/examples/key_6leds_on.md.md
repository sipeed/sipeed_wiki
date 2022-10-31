---
title: Tang Primer 20K Dock 按键点六个灯
tags: Tang Primer 20K Dock，上手
keywords: Primer, Tang, Dock， 入门，20K
desc: Tang Primer 20K Dock 基础进阶
update:
  - date: 2022-10-27
    version: v0.1
    author: wonder
    content:
      - 初稿
---

前面已经完成按键亮一个灯操作了，板子上还剩下五个 LED 可自定义操作，这次可以使用位拼接运算符 `{` `}` 来一起控制六个 LED。

## 位拼接运算符

### 例子①

语法：

`assign c[5:0] = {{3{1'b1}},{3{1'b0}}};`

等效于 

`assign c[5:0] = 6'b111000 ;`

### 例子②

语法：

```verilog
wire [2:0] a = 3'b000;
wire [2:0] b = 3'b000;
wire [5:0] c = {a,b} ;
```

## 硬件电路说明

从 [原理图](https://dl.sipeed.com/shareURL/TANG/Primer_20K/02_Schematic) 中，可以知道以下信息：

### 按键电路：

根据 DOCK 底板原理图，可以看出当板载按键按下时，对应的 FPGA 引脚会为低电平输入。

| 板载按键电路原理图 | 板载按键与 FPGA 连接引脚图 |
|---|---|
| ![key_schematic](./assets/key_led_on/key_schematic.png)| ![key_pin](./assets/key_led_on/key_pin.png) |

### LED 电路:

根据 LED 电路，可以知道当 FPGA 引脚为低电平的时候对应连接的 LED 会亮起来。

| 板载自定义 LED 电路原理图 | 板载自定义 LED 与 FPGA 连接引脚图 |
|---|---|
| ![key_schematic](./assets/key_led_on/led_schematic.png)| ![key_pin](./assets/key_led_on/led_pin.png) |

所以直接将按键引脚的逻辑电平输出为 LED 的引脚裸机电平就可以点亮 LED 灯。