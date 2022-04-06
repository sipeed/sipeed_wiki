# Tang Nano 9K

>  Edit on 2022.04.06

## Introduction

Tang Nano 9K is a core board designed based on [Gowin](https://www.gowinsemi.com/en/) GW1NR-9 FPGA chip. The board is equipped with HDMI interface, RGB screen interface, SPI screen interface, SPI FLASH and 6 LEDs to help user verifiy fpga design and RISC-V soft core conveniently and quickly. Its rich 8640 logic units can not only be used to design various complex logic circuits, but also enough to test PicoRV softcore, which meets user's demand like studying FPGA, verifying softcore, further studying and so on.

## Parameters

| Item                   | value                                                                                                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Logic units(LUT4)      | 8640                                                                                                                                                                     |
| Registers(FF)          | 6480                                                                                                                                                                     |
| ShadowSRAM SSRAM(bits) | 17280                                                                                                                                                                    |
| Block SRAM BSRAM(bits) | 468K                                                                                                                                                                     |
| Number of B-SRAM       | 26                                                                                                                                                                       |
| User flash(bits)       | 608K                                                                                                                                                                     |
| SDR SDRAM(bits)        | 64M                                                                                                                                                                      |
| 18 x 18 Multiplier     | 20                                                                                                                                                                       |
| SPI FLASH              | 32M-bit                                                                                                                                                                  |
| Number of Pll          | 2                                                                                                                                                                        |
| Display interface      | HDMI interface, SPI screen interface and RGB screen interface                                                                                                            |
| Debugger               | Onboard BL702 chip provides USB-JTAG and USB-UART functions for GW1NR-9                                                                                                  |
| IO                     | • support 4mA、8mA、16mA、24mA other driving capabilities <br>• Provides independent Bus Keeper, pull-up/pull-down resistors, and Open Drain output options for each I/O |
| Connector              | TF card slot, 2x24P 2.54mm Header pads                                                                                                                                   |
| Button                 | 2 programmable buttons for users                                                                                                                                         |
| LED                    | Onboard 6 programmable LEDs                                                                                                                                              |


![Generated](.\assets\clip_image008.jpg)

![Generated](.\assets\clip_image010.gif)

| Usage           | FPGA                     | MCU                                                                               | FPGA+MCU                                                              |
| :-------------- | :----------------------- | :-------------------------------------------------------------------------------- | :-------------------------------------------------------------------- |
| Language        | Verilog HDL/Verilog      | C/C++                                                                             | Verilog HDL/Verilog ，  C/C++                                         |
| summary         | verify HDL design        | After flashing the softcore bitstream, <br>this board can bu used as a normal mcu | After flashing the softcore bitstream,<br>it can be used as two chips |
| suitable people | beginner，FPGA developer | RISC-V developers，Cortex-M developers                                            | Senior hardware and software engineer                                 |

## Others

- [Schematic](https://dl.sipeed.com/shareURL/TANG/Nano%209K/2_Schematic)
- [Download center](https://dl.sipeed.com/shareURL/TANG/Nano%209K)
- [Examples](./Tang-nano-9k.md)

## Support

Email to support@sipeed.com for technical support and Business cooperation.

