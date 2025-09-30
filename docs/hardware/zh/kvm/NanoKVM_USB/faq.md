---
title: F&Q
keywords: NanoKVM-USB, Lichee, PiKVM, RISCV, tool
---

## 串口/键鼠问题

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

## 视频问题

### 视频画质差

+ 首先检查是否使用了 USB2.0 的线缆/HOST接口，当分辨率较大时 USB2.0 不足以提供充足的传输带宽，会被动降低画质，建议选用 USB3.0的线缆
+ 2K分辨率下首先于芯片编码能力，画质会下降，请切换为1080P使用
+ 如果 Target 连接的是 Windws主机，请前往系统设置-显示设置-高级显示设置-列出所有模式中更改为 1080P60，并检查`桌面分辨率`和`活动信号分辨率是否一致`

### DP-HDMI转接器

+ 部分无源DP转HDMI转换器内部电路仅做电平转换，对NanoKVM-USB兼容性较差，表现为视频信号从无到有（比如从睡眠唤醒时）NanoKVM-USB仍显示然黑屏，需要手动拔插HDMI。

### 无HDMI环出

+ 内测版硬件仅支持HOST侧USB供电，请在使用时保持HOST测供电正常

### 环出显示屏

+ NanoKVM-USB在未连接环出显示屏前使用自身的EDID（显示器识别数据），连接环出显示器后切换为环出显示器的EDID。
+ 由于EDID中包含显示器厂家以及颜色信息，插入环出显示器前后Target系统设置中可能显示为不同的分辨率列表，USB采集的画面颜色可能在插入前后有所差异

## 音频问题

### 音频不连续

+ NanoKVM-USB 在USB2.0模式下可能会因带宽不够的原因出现音频传输不连续的问题，请尽量使用USB3.0连接NanoKVM-USB和Host

## 已知问题

### 延迟：

+ ARM 版的 macOS 通过 NanoKVM-USB 连接树莓派时延迟会增大，其他组合则不受影响

## 反馈方式

+ 若上述方法不能解决异常，请在论坛,GitHub或QQ群说明您购买的型号和遇到的问题，我们会耐心解答

- [Github issues](https://github.com/sipeed/NanoKVM)
- [MaixHub 论坛](https://maixhub.com/discussion/nanokvm)
- QQ 交流群: 703230713