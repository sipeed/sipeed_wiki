# 烧录系统

## 系统简介

Lichee MaixSense（以下简称R329）提供了以下两种系统镜像

|   名称   |               armbian               |               Tina               |
| ------ | --------------------------------- | ------------------------------ |
|   简介   | 专门用于`ARM`开发板的`Debian` |    全志深度修改OpenWRT1404的系统     |
|   特点   |        主线化Linux，功能丰富        |        厂商深度修改，软硬件契合度高        |
| 适用人群 |       极客，嵌入式入门玩家等        | 深度开发，需要自行定制等开发人员 |

> ！！！一定要严格按照步骤操作！！！armbian系统请使用大于 4G 的 TF/SD 卡进行烧录，tina系统请使用大于 1G 的 TF/SD 卡进行烧录

R329为全志的SOC，所以Windows使用PhoenixCard，Linux 上使用Livesuit烧录镜像文件。

- 从下载站获取最新的R329系统镜像 [SDK_MaixII/release](https://dl.sipeed.com/shareURL/MaixII/SDK/release) ，找不到就搜索R329 获取最新的镜像。
- 下载站中有多个同版本不同大小的镜像系统，文件较大的镜像是需要使用dd命令进行系统的烧录。
- 解压 R329镜像压缩包，得到一个 xxxx.img 文件。
- 从网上获取 PhoenixCard(Windows) 烧录工具。


## Tina系统烧录

镜像下载站连接：

Tina系统的烧录方式和Maix Ⅱ dock通用，可参考[MaixII M2dock 烧录系统 - Sipeed Wiki](https://wiki.sipeed.com/soft/maixpy3/zh/install/maixii_m2dock/flash.html#windows-phoenixcard)，这里不多做介绍

## armbian系统烧录

armbian镜像获取：

> 链接：[https://pan.baidu.com/s/1RM8yjut_Mnzy6XJF4y-wRg](https://pan.baidu.com/s/1RM8yjut_Mnzy6XJF4y-wRg)
> 提取码：kh5n
> 阿里网盘：<https://www.aliyundrive.com/s/vcL7X57ZRox>

armbian使用的烧录方式为dd，windows下推荐使用Etcher，linux下推荐使用Terminal。

### windows下系统烧录

资源获取：

​	下载[Etcher](https://www.balena.io/etcher/ "Etcher")

​	下载[SD Card Formatter](https://www.sdcard.org/downloads/formatter/eula_windows/SDCardFormatterv5_WinEN.zip "SDCardFormatter")

首先解压镜像，得到 .img镜像文件，然后使用SD Card Formatter格式化sd卡，打开Etcher，点击`Flash from file`,选中dd镜像包，然后点击`Select target`选中sd卡，最后点击`Flash`烧录。 

### linux下系统烧录

首先解压镜像，得到 .img镜像文件，然后格式化sd卡，打开Terminal，输入  `sudo dd if = xxx.img of=/dev/sdx bs=1M status=progress`烧录。注意xxx.img为文件名，  `/dev/sdx`为sd卡实挂载位置。

烧录完毕后，即可放入Lichee MaixSense中运行。

## 访问串口

> 请将 USB口插入到 USB UART 口(下面的口）从而获得串口。

### Linux & macOS

Linux 不需要装驱动，系统自带了，使用 `ls /dev/ttyUSB*` 即可看到设备号

### Windows

`Lichee MaixSense` 使用了 `CH340` 作为驱动芯片。`Windows` 用户需要安装 `CH340` 的驱动。

Windows 下载 [ch340 ch341 driver](https://api.dl.sipeed.com/shareURL/MAIX/tools/ch340_ch341_driver) 安装即可，然后可以在 `设备管理器` 中看到串口设备

## 配置系统

