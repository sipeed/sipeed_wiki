---
title: Maix Dock USB 驱动安装
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: Maix Dock USB 驱动安装
---


## Linux

Linux 不需要装驱动，系统自带了，使用 `ls /dev/ttyUSB*` 即可看到设备号

## Windows

`Maix Dock` 使用了 `CH340` 作为驱动芯片。`Windows` 用户需要安装 `CH340` 的驱动。

Windows 下载 [ch340 ch341 driver](https://api.dl.sipeed.com/fileList/MAIX/tools/ch340_ch341_driver/CH341SER.EXE) 安装即可，然后可以在 `设备管理器` 中看到串口设备

