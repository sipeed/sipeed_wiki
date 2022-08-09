# 系统烧录

## 系统简介

Lichee MaixSense（以下简称R329）提供了以下两种系统镜像

|   名称   |               armbian               |       Tina      |
| :------ | :------------------------ | :---------------------- |
|   简介   | 专门用于ARM开发板的轻量级 Debian |    全志魔改OpenWRT1404的系统     |
|   特点   |        主线化Linux，功能丰富      |        厂商魔改，比较精简        |
| 适用人群 |       极客，嵌入式入门玩家等      | 深度开发，需要自行定制等开发人员 |

> ！！！一定要严格按照步骤操作！！！armbian系统请使用大于 4G 的 TF/SD 卡进行烧录，Tina系统请使用大于 1G 的 TF/SD 卡进行烧录, 质量较差的启动卡会有糟糕的实际使用体验

对于 R329 芯片， 在 Windows 使用 Etcher ，Linux 上使用 Livesuit 烧录镜像文件。

## 获取镜像

### armbian 系统镜像

armbian 镜像获取：

> 链接：[点我](https://eyun.baidu.com/s/3htTXfaG#sharelink/path=%2F%E4%B8%8B%E8%BD%BD%E7%AB%99%E6%96%87%E4%BB%B6%2FMaixII%2FMaixII-A%2FSDK&parent_path=%2F%E6%B7%B1%E5%9C%B3%E7%9F%BD%E9%80%9F%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8)

其中带有 MaixPy3 名称的是已经装载了 MaixPy3 库和相关驱动的镜像包。

armbian 镜像所打包的方法为 [dd](https://baike.baidu.com/item/DD/2654972); 可以选用适合当前系统的 [Etcher](https://www.balena.io/etcher/ "Etcher") 软件来烧录。

### Tina 系统镜像

Tina 系统需要自己进行编译，具体编译方式参考 [https://github.com/sipeed/R329-Tina-jishu](https://github.com/sipeed/R329-Tina-jishu)

Tina 系统的烧录方式和 MaixII Dock 通用，可参考[MaixII M2dock 烧录系统 - Sipeed Wiki](./../M2/flash.md)，这里不多做介绍

## 烧录镜像

### 资源获取

- 下载[Etcher](https://www.balena.io/etcher/ "Etcher")

### 烧录步骤

首先解压所下载的镜像压缩包，得到 `.img` 镜像文件，打开 [Etcher](https://www.balena.io/etcher/ "Etcher") 软件，点击 `Flash from file` ,选中解压出来的 `.img ` 文件镜像，然后点击 `Select target` 选中sd卡，最后点击 `Flash` 进行烧录，等待完成即可。 

下面只是用原始的 armbian 作为展示，有需求的话可也已选择下载带有 MaixPy3 的镜像文件。

![burn](./assets/95133.gif)

如果烧录失败了，请手动格式化一下 sd 卡。Windows 和 MacOS 可以使用 [SD Card Formatter](https://www.sdcard.org/downloads/formatter/eula_windows/SDCardFormatterv5_WinEN.zip)，Linux 系统可以使用 [Gparted](https://gparted.org/)。

## 连接串口

- 直接将开发板有 Debug 标志的 Type C 接口与电脑连接即可

### Linux & macOS

Linux 不需要装驱动，系统自带了，使用 `ls /dev/ttyUSB*` 命令即可看到设备号

### Windows

Lichee MaixSense 使用了 CH340 作为串口芯片。Windows 用户需要安装 CH340 的驱动。

Windows 下载 [ch340 ch341 driver](https://api.dl.sipeed.com/shareURL/MAIX/tools/ch340_ch341_driver) 安装即可，然后可以在 设备管理器 中看到串口设备和端口号。