---
title: Grove
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: Grove
---


Modules using Grove standard interfaces, Grove is a unified interface system used by the Seeed team, and currently supports a large number of modules.

## Grove interface

The cables of the Grove interface have 4 colors, and users can quickly distinguish them according to the colors
![](../../../assets/hardware/module_grove/grove_interface.jpg)

| pin | color | description |
| --- | --- | --- |
| pin 1 | yellow | (for example, SCL on I2C Grove Connectors) |
| pin 2 | white | (for example, SDA on I2C Grove Connectors) |
| pin 3 | Red | VCC (All Grove ports are VCC in red) |
| pin 4 | black | GND (all Grove ports are GND in black) |

Grove module mainly has 4 kinds of interfaces:

1. Grove Digital digital interface:<br/>
    The Grove digital interface consists of four standard wires of Grove plugs.<br/>
    The two signal lines are usually called D0 and D1.<br/>
    Most modules only use D0, but some (like LED Bar Grove displays) use both. Usually the core board will call the first Grove connector on the board as D0, and the second as D1. The first The connector will be connected to the DO/D1 pin of the main control chip, the second connector will be connected to the D1/D2 pin of the main control chip, and the following connectors will be deduced by analogy.

| pin | Function | Note |
| --- | --- | --- |
| pin1 | Dn First digital input | — |
| pin2 | Dn+1 The second digital input | — |
| pin3 | VCC power supply pin 5V/3.3V | — |
| pin4 | GND ground | — |


2. Grove UART :<br/>
    The Grove UART is a special digital input and output interface.<br/>
    It uses pins 1 and 2 for serial input and transmission. <br/>
    Pin 1 is the RX line (used to receive data, so it is input),
    Among them, pin 2 is the TX line (used to transmit data to the Grove module).

| pin | Function | Note |
| --- | --- | --- |
| pin1 | RX | Serial Receive |
| pin2 | TX | Serial transmission |
| pin3 | VCC | Power supply pin 5V/3.3V |
| pin4 | GND | Ground |

3. Grove I2C:<br/>
    There are many types of I2C Grove sensors available.<br/>The Grove on MaixCube only supports 3.3V sensors

  The Grove I2C connector has a standard layout. Pin 1 is the SCL signal, and pin 2 is the SDA signal

| pin | Function | Note |
| --- | --- | --- |
| pin1 | SCL | I2C clock |
| pin2 | SDA | I2C data |
| pin3 | VCC | Power supply pin, 5V/3.3V |
| pin4 | GND | Ground |

For details, please refer to: [Grove_System](https://wiki.seeedstudio.com/cn/Grove_System/)

## Peripheral Module

The following peripherals all use Grove interface

* [Ultrasonic Ranger](./grove_ultrasonic_ranger.md)
* [Chainable RGB LED light](./grove_chainable_rgb_led.md)
* [RGB LED Ring strip](./grove_rgb_led_ring.md)
