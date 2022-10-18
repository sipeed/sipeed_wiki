---
title: Primer 20K Lite blink led
keywords: Primer 20K, Lite, FPGA
desc: Primer 20K start
tags: FPGA, Primer 20K
cover: ./../../
update:
  - date: 2022-10-18
    version: v0.1
    author: wonder
    content:
      - First time edit
---

Let's blink a led after getting the Tang Primer 20K Lite suits.

## Preread

This document is writen for guiding user start preparing GOWIN development enviroment and use the Tang Primer 20K.

The default firmware function in the Core board is as followings:
- All IO port routed to pin 2.54mm pad toggles regularly, including spi_lcd connector ports and sd_card connector ports on Core Board
- DDR test; Test result print_out by serial port connector on Core Board and we can use serial tool in computer to see

Because of the DDR test function, Core Board will be very hot. you can erase the firmware in the Core Board if you mind this. And default firmware project can be found here: [github](https://github.com/sipeed/TangPrimer-20K-example/tree/main/Lite-bottom%20test%20project/test_board)

## Install IDE

Visit [Install IDE](./../../../Tang-Nano-Doc/install-the-ide.md) to prepare the enviroment for this FPGA.

For windows users, we recommend use this