---
title: Maix Dock USB driver installation
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy doc: Maix Dock USB driver installation
---

## Linux

Linux does not need to install the driver, the system comes with it, use `ls /dev/ttyUSB*` to see the device number

## Windows

`Maix Dock` uses `CH340` as the driver chip.`Windows` users need to install the driver of `CH340`.

Windows download [ch340 ch341 driver](https://api.dl.sipeed.com/shareURL/MAIX/tools/ch340_ch341_driver) and install it, and then you can see the serial device in the `Device Manager`
