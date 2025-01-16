---
title: F&Q
keywords: NanoKVM-USB, Lichee, PiKVM, RISCV, tool
---

## 异常修复

### Linux打开网页后无 ttyUSBx 串口设备

+ 可能缺少串口驱动导致,请按照以下方法重新安装CH34x驱动:

1. 在WCH官网下载驱动(下载地址)[https://www.wch.cn/download/CH341SER_LINUX_ZIP.html]，解压后进入driver目录
2. 执行`uname -r`查看操作系统发行版本，在(此处)[https://elixir.bootlin.com/linux/v6.2/source/drivers/usb/serial/ch341.c]找到对应的版本，将内容复制到`ch341.c`中
3. 执行`make`命令编译驱动
4. 执行`sudo make load`命令安装驱动
5. 替换旧驱动:`cp ch341.ko /lib/modlues/$(uname -r)/kernel/drivers/usb/serial/ch341.ko`

+ 部分linux发行版内置了`brltty`,这是一款盲文阅读工具，但会占用/dev/ttyUSB0串口，导致网页检测不到，在确认不使用`brltty`后建议将其卸载`sudo apt remove brltty`

### 打开网页后 NanoKVM-USB 对应串口设备无法打开

+ 可能是部分程序占用该串口，请确认无占用后再试
+ Linux可能缺少权限，导致串口无法打开，在终端中执行`sudo chmod 777 /dev/ttyUSB*`
+ Chrome浏览器可能没有检测到该串口，请刷新网页或重启 Chrome
+ Chrome权限可能不足，请打开相应权限

### 无HDMI环出

+ 内测版硬件仅支持HOST侧USB供电，请在使用时保持HOST测供电正常

### 若上述方法不能解决异常，请在论坛,GitHub或QQ群说明您购买的型号和遇到的问题，我们会耐心解答

## 反馈方式

- [Github issues](https://github.com/sipeed/NanoKVM)
- [MaixHub 论坛](https://maixhub.com/discussion/nanokvm)
- QQ 交流群: 703230713