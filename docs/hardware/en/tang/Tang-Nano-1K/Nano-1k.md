# Tang Nano 1K

> Edit on 2022.08.18

## Introduction

Tang Nano 1K is a core board designed based on [Gowin](https://www.gowinsemi.com/en/) GW1NZ-LV1 FPGA chip. The board is equipped with RGB LCD interface and onboard USG-JTAG debugger, which make it convenient for users to use. User can use this for small digital logic design and experiment.

![Nano-1](./assets/1k-1.jpg)
![Nano-2](./assets/1k-2.jpg)

## Parameters

|        item        |     Specs      |
| :----------------: | :------------: |
|        chip        | GW1NZ-LV1 FPGA |
| logic units(LUT4)  |      1152      |
|    Register(FF)    |      864       |
|  Block SRAM(bits)  |      72K       |
|  Number of B-SRAM  |       4        |
|  User flash(bits)  |      64K       |
|   Number of Pll    |       1        |
| Number of I/O Bank |       2        |

### Pinmap

![pinmap](./assets/1k-pin.png)

## Informations

- [Datasheet](https://dl.sipeed.com/shareURL/TANG/Nano%201K/1_Specification)
- [Schematic](https://dl.sipeed.com/shareURL/TANG/Nano%201K/2_Schematic)
- [Bit number map](https://dl.sipeed.com/shareURL/TANG/Nano%201K/3_Bit_number_map)
- [Dimensional drawing](https://dl.sipeed.com/shareURL/TANG/Nano%201K/4_Dimensional_drawing)
- [3D File](https://dl.sipeed.com/shareURL/TANG/Nano%201K/5_3D_file)
- [Chip Manual](https://dl.sipeed.com/shareURL/TANG/Nano%201K/6_Chip_Manual)

- [Examples](https://wiki.sipeed.com/hardware/en/tang/common-doc/examples.html)

## Addition

1. If you have trouble with this board, you can join our telegram (t.me/sipeed) or contact us on twitter (https://twitter.com/SipeedIO).

2. For Fpga burning we require using [this](https://dl.sipeed.com/shareURL/TANG/programmer) Programmer application. Because other version Programmer application may fail burning this board.

3. If you meet problems, please visit [problems](./../common-doc/questions.md) first, normally most problems will be solved after using this programmer [Click me](https://dl.sipeed.com/shareURL/TANG/programmer).