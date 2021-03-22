---
title: Grove
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: Grove
---


采用 Grove 标准接口的模块，Grove 为 Seeed 团队使用的统一接口系统，目前以支持大量模块。 

## Grove 接口

Grove 接口的线缆有 4 种颜色，用户可以根据颜色快速区别
![](../../../assets/hardware/module_grove/grove_interface.jpg)

| pin   | 颜色 | 描述                                |
| ----- | ---- | ----------------------------------- |
| pin 1 | 黄色 | (例如，I2C Grove Connectors上的SCL) |
| pin 2 | 白色 | (例如，I2C Grove Connectors上的SDA) |
| pin 3 | 红色 | VCC (所有的Grove接口红色都是VCC)    |
| pin 4 | 黑色 | GND (所有的Grove接口黑色都是GND)    |

Grove模块主要有 4 种接口:

1. Grove Digital 数字接口:<br/>
    Grove 数字接口由 Grove 插头的四条标准线组成.<br/>
    两条信号线通常称为 D0 和 D1 .<br/>
    大多数模块只使用D0，但有些(像LED Bar Grove显示屏)使用两者.通常核心板会将板卡上的第一个Grove连接头称为D0，第二个称为D1.第一个接头会连接到主控芯片的DO/D1管脚，第二个连接头会连接到主控芯片的D1/D2引脚，后面的连接头以此类推.

| pin  | Function             | Note |
| ---- | -------------------- | ---- |
| pin1 | Dn 第一个数字输入    | —    |
| pin2 | Dn+1 第二个数字输入  | —    |
| pin3 | VCC 供电引脚 5V/3.3V | —    |
| pin4 | GND 地               | —    |


2. Grove UART :<br/>
    The Grove UART 是特殊的一种数字输入输出接口.<br/>
    它使用引脚 1 和引脚 2 进行串行输入和发送. <br/>
    引脚1是 RX 线(用于接收数据，因此是输入)，
    其中引脚 2 是 TX 线(用于向 Grove 模块传输数据).

| pin  | Function | Note             |
| ---- | -------- | ---------------- |
| pin1 | RX       | 串行接收         |
| pin2 | TX       | 串行发送         |
| pin3 | VCC      | 供电引脚 5V/3.3V |
| pin4 | GND      | 地               |

3. Grove I2C:<br/>
    有许多类型的I2C Grove 传感器可用.<br/>MaixCube 上的 Grove 只支持 3.3V 传感器

  Grove I2C 连接器具有标准布局.引脚 1 是SCL信号，引脚 2 是SDA信号

| pin  | Function | Note              |
| ---- | -------- | ----------------- |
| pin1 | SCL      | I2C 时钟          |
| pin2 | SDA      | I2C 数据          |
| pin3 | VCC      | 供电引脚，5V/3.3V |
| pin4 | GND      | 地                |

详情请参考：[Grove_System](https://wiki.seeedstudio.com/cn/Grove_System/)

## 外设模块

以下外设均采用 Grove 接口

* [Ultrasonic Ranger 测距](./grove_ultrasonic_ranger.md)
* [Chainable RGB LED 灯](./grove_chainable_rgb_led.md)
* [RGB LED Ring 灯条](./grove_rgb_led_ring.md)