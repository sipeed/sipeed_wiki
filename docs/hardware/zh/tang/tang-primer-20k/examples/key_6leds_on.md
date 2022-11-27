---
title: Tang Primer 20K Dock 按键点六个灯
tags: Tang Primer 20K Dock，上手
keywords: Primer, Tang, Dock， 入门，20K
desc: Tang Primer 20K Dock 基础进阶
update:
  - date: 2022-11-27
    version: v0.1
    author: wonder
    content:
      - 初稿
---

前面已经完成按键亮两个灯操作了，板子上还剩下五个 LED 可自定义操作，这次可以使用位拼接运算符 `{` `}` 来一起控制六个 LED。

## 位拼接运算符

### 例子①

语法：

`assign c[5:0] = {{3{1'b1}},{3{1'b0}}};`

等效于 

`assign c[5:0] = 6'b111000 ;`

### 例子②

语法：

```verilog
wire [2:0] a = 3'b111;
wire [2:0] b = 3'b000;
wire [5:0] c = {a,b} ;
```

等效于 

`assign c[5:0] = 6'b111000 ;`

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

所以直接将按键引脚的逻辑电平输出为 LED 的引脚逻辑电平就可以点亮 LED 灯。

## 操作

### 引脚复用

- READY
- DONE
- SSPI

### 端口和引脚

| Port | Direction | Location |
| --- | --- | --- |
| key | input | T10 |
| led[5] | output | L16 |
| led[4] | output | L14 |
| led[3] | output | N14 |
| led[2] | output | N16 |
| led[1] | output | A13 |
| led[0] | output | C13 |

### 代码

.. tabset::

    ## key_6leds_on.v
    Verilog文件；
    定义了一个按键输入端口，和六个输出端口。六个输出端口的 IO 电平状态由输入端口决定。 
    ```verilog
    module key_6leds_on(
        input key,
        output [5:0] led
    );
        assign led[5:0] = {3{key},3{~key}}; // led[5:0] = {key,key,key,~key,~key,~key};
    endmodule
    ```

    ## key_6leds_on.cst
    物理约束文件；
    将 verilog 代码里的端口绑定到 FPGA 引脚上面
    ```txt
    IO_LOC "led[5]" L16;
    IO_PORT "led[5]" PULL_MODE=UP DRIVE=8;
    IO_LOC "led[4]" L14;
    IO_PORT "led[4]" PULL_MODE=UP DRIVE=8;
    IO_LOC "led[3]" N14;
    IO_PORT "led[3]" PULL_MODE=UP DRIVE=8;
    IO_LOC "led[2]" N16;
    IO_PORT "led[2]" PULL_MODE=UP DRIVE=8;
    IO_LOC "led[1]" A13;
    IO_PORT "led[1]" PULL_MODE=UP DRIVE=8;
    IO_LOC "led[0]" C13;
    IO_PORT "led[0]" PULL_MODE=UP DRIVE=8;
    IO_LOC "key" T10;
    IO_PORT "key" PULL_MODE=UP;
    ```

## 效果

松开 S0 按键，LED0、LED1 和 LED2 亮，LED3、LED4 和 LED5 灭。
按下 S0 按键，LED3、LED4 和 LED5 亮，LED0、LED1 和 LED2 灭。

<!-- |松开 S0 按键|按下 S0 按键|
|---|---|
|<img src="./assets/key_led_on/led_off.png" alt="led_off">|<img src="./assets/key_led_on/led_on.png" alt="led_on">| -->

<p id="back">
    <a href="#" onClick="javascript :history.back(-1);">返回上一页(Back)</a>
</p>