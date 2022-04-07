---
title: Summary
---

> Edit on 2022.04.06

Tang Nano series development boards are designed based on [Gowin](https://www.gowinsemi.com/en/) FPGA chip. Mutiple models of development board meets various requirements. 
- Tang nano 1K with a extremely low price can lead user into FPGA fields
- Tang nano 4K with a Cortex m3 hardcore, almost the cheapest heterogeneous core board
- Tang nano 9K with rich logic units can be used to verify Riscv core 

## Comparation

| Model     | Tang Nano 1K         | Tang Nano 4K   | Tang Nano 9K        |
| --- | -------- | ----------------- | -------- |
| Appreance             | ![Generated](/hardware/zh/tang/Tang-Nano/assets/clip_image002.gif) | ![Generated](/hardware/zh/tang/Tang-Nano/assets/clip_image004.gif) | ![Generated](/hardware/zh/tang/Tang-Nano/assets/clip_image006.gif) |
| Logic units（LUT4） | 1152                                                         | 4608                                                         | 8640                                                         |
| Hard core       |                                                            | Cortex-M3                                                    |                                                            |
| Crystal oscillator frequency         | 27Mhz                                                        | 27Mhz                                                        | 27Mhz                                                        |
| Display interface         | RGB screen interface                                              | HDMI                                                         | HDMI,<br>  RGB screen interface,<br>  SPI screen interface                      |
| Camera           |                                                            | OV2640                                                   |                                                            |
| External SPI FLASH    | Pads are reserved                                                   | Default welding<br>32Mbit SPI FLASH                                     | Default welding<br>32Mbit SPI FLASH                                     |
| TF card slot           |                                                            |                                                            | yes                                                           |
| Programmer           | Onboard USB-JTAG downloader                                            | Onboard USB-JTAG downloader                                            | Onboard USB-JTAG downloader &<br> USB-UART port                                     |

- The blank in the form means none

## Preparation

- [Install IDE](./install-the-ide.md)

## Questions

- [Questions&Answers](./programmer.md)