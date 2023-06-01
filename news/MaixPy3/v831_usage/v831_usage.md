---
title: M2DOCK 上手视觉指南
tags: M2DOCK, V831, 避坑指南, 上手指南
keywords: V831, 视觉指南，避坑, 上手
update:
  - date: 2023-05-15
    version: v0.1
    author: lyx
    content:
      - 编写文档
---

## 产品介绍

> 铛 ~ 新的 2023 年当然要有新的上手指南辣（虽然已经过去5个月）总有事情要被鸽但能填上就是好坑。
> 新的上手指南还是旧的目的，希望大家可以借助这篇文章在使用 M2DOCK 时更加顺利一点吧！

![m2dock](./../../../docs/hardware/assets/maixII/m2dock.jpg)

本篇文章以 `视觉` 为主题阐述如何在 M2DOCK（V831）从基础的开箱上手再到视觉的衍生（深度开发）的使用全过程，因篇幅的有限这里不再对产品进行详细介绍，想要了解相关产品介绍可点击资料进行查看。

- **相关资料及硬件参数：[点击查看](https://wiki.sipeed.com/hardware/zh/maixII/M2/resources.html) 购买链接：[点击前往](https://item.taobao.com/item.htm?id=635874427363)**

<iframe src="//player.bilibili.com/player.html?aid=298543445&bvid=BV1sF411u7xb&cid=586467021&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

## 前情提要

**【有基础可跳过】**促使我们做上手指南的原因永远都是以降低用户使用难度为目的，但一些基础知识（Python 语法）我们还是需掌握熟悉的，而大部分的小伙伴是从 `K210（MaixPy)` 换代升级到 `M2DOCK（MaixPy3)` 的，但我们区分这两者之间的不同吗？显然（萌新）小伙伴们是不清楚的。

>**我们可以这么来理解**：本质上它们都是专门为 AloT 提供的 Python 开发环境，提供了各类各样的模块。MaixPy 基于 MicroPython 的环境制作和 MCU 无系统的，而后者 MaixPy3 则是基于 Linux Python3 的环境以及 Linux 系统，可点击：[[关于 MaixPy 与 MaixPy3 的区别]](https://wiki.sipeed.com/news/MaixPy3/difference.html) 查看更多。

根据下文的链接自行学习相关的 Python 基础语法及知识：

- [什么是 Python ?](https://wiki.sipeed.com/soft/maixpy3/zh/origin/python.html?highlight=python)
- [国内 Python 基础教程](https://wiki.sipeed.com/soft/maixpy3/zh/origin/video.html)
- [【适合有一定基础】大佬鼠の嵌入式 Python 入门教程[1]](https://wiki.sipeed.com/soft/maixpy3/zh/origin/hello_world.html)
- [【适合有一定基础】大佬鼠の嵌入式 Python 入门教程[2]](https://wiki.sipeed.com/soft/maixpy3/zh/origin/loop_python.html)

## 准备工作（必看）

充足的准备能让后续的上手旅程更事半功倍（为了不掉坑里~）文档以 `M2DOCK` 的全功能套餐来演示，我们收到后会有一套 M2DOCK 板卡、Type-C 线 以及 SD 镜像卡，但还需准备一个 USB 3.0 读卡器以作备用。

![maixii](./assest/maixii.jpg)

### 上手流程图

上手指南搭配流程图一起食用更佳~

![steps](./assest/steps.png)

### 烧录镜像系统

准备完相关的硬件工具后就是开启软件类的的相关准备操作，我们先进行烧录 M2DOCK 相关的适配系统。

> 文档示例环境：**Windows10**    
> 镜像版本：**v831-m2dock-maixpy3-0.5.4-20230505**
> 1. 在官方淘宝店购买过（预烧录好）镜像 SD 卡的小伙伴可跳过进入下一步。
> 2. 如果没有购入官方相关镜像卡，建议用户购买正规正版（防止出现烧录失败现象）的镜像卡。
> 3. 非必要的情况下不建议多次且随意进行镜像烧录。

- **镜像文件命名说明**

对于 V831 的镜像文件名字是有对应的规则，以后大家可以根据自己的需求来进行下载。
就以 `v831-m2dock-maixhub-0.5.1-20220701.zip`和 ` v831-m2dock-maixpy3-0.5.1-20220701.zip` 来对比说明

| 名称          | 含义                                                                                                              |
| ------------- | ----------------------------------------------------------------------------------------------------------------- |
| maixpy3-0.5.1 | 此镜像是给 [MaixPy3](https://wiki.sipeed.com/maixpy3) 专用，并内置了`0.5.1`的版本，但其中 **无** 内置 maixhub app |
| maixhub-0.5.1 | 此镜像是给 [MaixPy3](https://wiki.sipeed.com/maixpy3) 专用，并内置了`0.5.1`的版本，但其中 内置 maixhub app        |
| m2dock        | 可使用 MaixII-Dock 开发板平台                                                                                     |
| 20220701      | 镜像更新日期                                                                                                      |

> 上述镜像均为开源版，只适用于 TF 卡烧录启动

- **获取相关的镜像包及工具**

1. V831 系统镜像下载站 [SDK_MaixII/release](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/release) 
2. V831 系统镜像百度云 [点我 提取码：v831](https://pan.baidu.com/e/verify?surl=Yrqpk26BL3sOCm4P1cMpBQ)
3. 烧录工具 [PhoenixCard](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/tools)
4. 内存卡格式化工具 [SD Card Formatter](https://www.sdcard.org/downloads/formatter/eula_windows/SDCardFormatterv5_WinEN.zip)

- **开始进行烧录工作**

**第一步**：先使用读卡器将镜像卡接入 USB 端，使用格式化工具 `SD Card Formatter` 进行格式化操作。
**第二步**：格式化完成后，再使用 `PhoenixCard` 烧录工具进行烧录。
**烧录流程示例**：可前往 [Windows/Linux M2dock 系统烧录](https://wiki.sipeed.com/hardware/zh/maixII/M2/flash.html) 查看相关示例，下图显示绿色代表烧录成功。

![img](./assest/img.png)

### 安装 MaixPy3 IDE 

`MaixPy3 IDE` 是基于 `Jupyter` 实现的 `Python3` 集成开发环境，运行界面可视化的操作降低使用难度，支持电脑端（支持跨平台）编辑或运行 Python 代码并实时显示效果，故而对无相关基础的用户们较友好。

![hello](./assest/hello.jpg)

> `注意事项（超重要！）`：**下载时确保我们安装的软件包版本（大于 0.5.0）且在安装过程中会弹出安装驱动程序的提示，请根据提示安装驱动并确保安装完成才能进行下一步操作。**

![usb](/news/MaixPy3/v831_usage/assest/usb.jpg)

接下来根据 `注意事项` 来自行下载安装包并安装好驱动及软件，根据示例文档熟悉界面的基础用法。

- **软件包下载链接：**

MaixPy3 IDE 下载站：[点击](https://dl.sipeed.com/shareURL/MaixII/MaixPy3-IDE) 
MaixPy3 IDE 百度云：[点击](https://eyun.baidu.com/s/3htTXfaG#sharelink/path=%2F%E4%B8%8B%E8%BD%BD%E7%AB%99%E6%96%87%E4%BB%B6%2FMaixII%2FMaixPy3-IDE&parent_path=%2F%E6%B7%B1%E5%9C%B3%E7%9F%BD%E9%80%9F%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8)
  
- **示例文档：**

多平台安装 MaixPy3 IDE 方法：[Windows/Macos/Linux MaixPy3 IDE](https://wiki.sipeed.com/soft/maixpy3/zh/tools/MaixPy3_IDE.html)
软件使用文档：[MaixPy3 IDE 界面介绍](https://wiki.sipeed.com/soft/maixpy3/zh/tools/MaixPy3_IDE.html#MaixPy3-IDE-%E7%95%8C%E9%9D%A2%E4%BB%8B%E7%BB%8D)

> 一起搭配我们的【M2DOCK 开箱大放送】视频食用更佳噢~
<iframe src="//player.bilibili.com/player.html?aid=384617683&bvid=BV14Z4y147Lg&cid=734640023&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

### 上电接线方式

准备好相关的软件以及基础工作我们开始学习如何正确接线并上电。

**第一步**：USB Type-C 数据线【需自行准备的话】请准备质量可靠或者是手机附赠的数据线，质量差的数据线会因电压问题造成开发板处于非正常工作状态导致后续影响使用，有些 Type-C 线只能供电。

![type-c](./k210_usage/../../../MaixPy/mixly_application/accets/k210_usage/type_c.jpg)

**第二步**：把我们准备的镜像卡插入 M2DOCK 的卡槽内，并确定烧录的版本（大于 0.5.1）即可。

![sd](./assest/sd.jpg)

**第三步**：将 `M2DOCK` 与电脑通过 OTG 标识的 USB 口连接，确认设备通电亮起（power）电源**红灯**，请看下图红圈别接错 USB 口的位置，OTG 标识的丝印在板子背面。

![otg](./assest/otg.jpg)

**第四步**：确认屏幕出现 logo 或二维码（wiki）表示系统启动开始工作，同时电脑会弹出 U 盘标识（意味着板卡系统已准备就绪）即可进行下一环开始使用！

![u_logo](./assest/u_logo.jpg)

> **如果出现异常情况**：通电后无法弹出 U 盘标识（常见于 Windows 平台）根据第五步卸载相关驱动即可。

**衍生第五步**：打开设备管理器后，根据示例图找到相关的 `Android ADB Interface` 手机驱动（常见于 XX 手机助手）右键进行卸载设备。

![adb](./assest/adb.jpg)

然后勾选卸载驱动（重要！！一定要勾选）进行卸载即可，U 盘自动弹出也代表底层硬件正常可用。

![delete](./assest/delete.jpg)

> 如果 U 盘还是没有如上述步骤出现，可以重烧系统或重启设备或考虑换台电脑操作，有可能是个别系统驱动不兼容导致的，实在是解决不了请找官方的淘宝客服。

## 上手运行程序

> 这里后不再重复任何基础操作知识，默认大家会操作 [Jupyter](https://wiki.sipeed.com/soft/maixpy3/zh/tools/0.MaixII-Dock.html#%E9%80%89%E6%8B%A9-RPyc-Python-%E6%A0%B8%E5%BF%83%E8%A1%A8%E7%A4%BA%E5%9C%A8%E6%9D%BF%E5%AD%90%E4%B8%8A%E8%BF%90%E8%A1%8C-Python-%E7%A8%8B%E5%BA%8F) 相关运行界面及方法。

开始体验运行代码前，我们先了解 M2DOCK 支持多种编程方式，分别是 Linux shell（adb）命令行、Jupyter notebook（Python）开发、U 盘编辑运行（Python）等。Linux shell 更多的是专业开发者或是熟悉 Linux 终端的同学进行使用，而如果是无基础的萌新更推荐其余两种方式。

>下文全以适配软件 MaixPy3 IDE 的使用来示例。

- **先熟悉相关的运行环境**

IDE 软件启动时会附带一个 `keep_adb.exe` 命令行终端的程序提供给熟悉 linux 终端操作开发板的同学，软件版本 0.4.2 后 keep_adb 服务会自动调用 adb 配置映射（forward）端口（22，18811，18812）与板子连接的 ide 服务是否工作。

**如何进行判断**：可以在交互终端输入 ps | grep mjpg 查看是否存在下图红框所指示的服务。

![keep_adb](./assest/keep_adb.jpg)

> 如果发现不存在 ide 服务（`python -c 'from maix import mjpg;mjpg.start();`）我们可以手动运行相关服务，并把现象汇报到社群，目前发现该现象主要出现在 Windows 11 系统之间的差异上。

最后确认系统防火墙是否阻止了软件底层所需要 `TCP 18811 18812` 的端口号（主用于运行程序和图像传输）
**了解更多**：可以点此查看关于 [MaixPy3](https://wiki.sipeed.com/soft/maixpy3/zh/tools/MaixPy3_IDE.html) IDE 的更加详细的介绍，此处不再赘述。

> **启动 MaixPy3 IDE 时会弹出 Jupyter 的编辑网页，我们先来测试板卡的连接以及外设是否正常可用。**

### 测试板卡连接

复制下列代码块，再点击上方菜单栏中的运行，测试板子连接是否正常。

```python3
import platform
print(platform.platform())

import time
print(time.asctime())
```

![test](./assest/test.jpg)

**由运行后打印出的结果我们可知以下信息：**

1. 运行这段代码的时间是 [ rpyc-kernel ]( running at Wed Jul 13 15:20:20 2022 )
2. 运行这段代码的平台是 Linux-4.9.118-armv7l-with-libc
3. 运行这段代码时：板子系统时间是 Thu Jan 1 04:04:55 1970。

当代码运行的时间为当前时间，并打印出以上代码，说明开发板已经连接上并可以正常的使用。

> 关于更详细或报错的话请查看 [如何运行代码](https://wiki.sipeed.com/soft/maixpy3/zh/tools/0.MaixII-Dock.html#%E5%A6%82%E4%BD%95%E8%BF%90%E8%A1%8C%E4%BB%A3%E7%A0%81) 进行排查或了解。

### 测试屏幕及摄像头

> 当确定板卡的连接状态正常后，我们来测试屏幕以及摄像头的功能是否正常。

运行以下程序后可在代码下方看见摄像头实时获取的图像。

```python3
from maix import camera, display, image #引入python模块包

while True:
    img = camera.capture()    #从摄像头中获取一张图像
    display.show(img)         #将图像显示出来
```

![sensor](./assest/sensor.png)

图中我们看见运行程序后可实时看到摄像头捕捉的画面，正面我们的屏幕以及摄像头都是正常可用的。

>更多的图像处理基础用法：[查看](https://wiki.sipeed.com/soft/maixpy3/zh/usage/vision/maixpy3-example.html#%E4%BB%8E%E6%91%84%E5%83%8F%E5%A4%B4%E8%8E%B7%E5%8F%96%E5%9B%BE%E5%83%8F%E5%B9%B6%E6%98%BE%E7%A4%BA)

### 测试拍照功能

```python
from maix import camera, display, image 
display.show(camera.capture())
```

<center><img src="./../../../out/hardware/zh/maixII/M2/asserts/hello_world.jpg" width="500"></center>

> 如果屏幕没有显示内容。那么首先确认一下镜像镜像版本，并且确认一下外设和驱动对的上

## 基础使用

上文我们使用了基本的（搭载 Python）Jupyter 并运行代码测试了相关外设走出了使用的第一步，接下来我们来使用命令行运行代码并联网。

>命令行也就是所谓的 Linux Shell，它是用户使用 Linux 的桥梁，Shell 是指一种应用程序，这个应用程序提供了一个界面，用户通过这个界面访问操作系统内核的服务，使用 shell 需要使用者具备一定的 Linux 基础知识 [Shell 教程](https://www.runoob.com/linux/linux-shell.html)/[部分常用 Linux 命令](https://wiki.sipeed.com/hardware/zh/maixII/M2/usage.html#%E9%83%A8%E5%88%86%E5%B8%B8%E7%94%A8-Linux-%E5%91%BD%E4%BB%A4)可根据需求进行学习。

### 使用命令行联网

M2Dock 带有 2.4G 无线模组，可以用来连接 2.4G 频段的无线网络，因镜像的更新（WiFi）链接方式有两种可供大家选择，但是文档示例以最新镜像方法为示例标准，更多可查询下文给出的参考链接。

- **使用以下命令行进行联网 确保镜像系统：0.5.4（20230207）**

使用下面的命令来连接名称为 Sipeed_Guest， 且密码为 qwert123 的无线网络。

```
wifi_connect_ap_test Sipeed_Guest qwert123
```

![wlan](./assest/wlan.jpg)

连接成功后可使用 `ifconfig` 命令查询 `wlan0` 的 IP 地址，关于命令行联网的详情请看[ V0.5.4 联网.](https://wiki.sipeed.com/hardware/zh/maixII/M2/usage.html#V0.5.4)

- **修改 wpa_supplicant.conf 进行联网：（V0.5.4）前镜像**

这个办法适用于 V0.5.4 前的镜像系统，通过修改 U 盘里的 `wpa_supplicant.conf` 文件修改名称及密码来联网，更加具体的操作请看[ V0.5.4 前镜像联网。](https://wiki.sipeed.com/hardware/zh/maixII/M2/usage.html#V0.5.4-%E4%B9%8B%E5%89%8D%E7%9A%84%E9%95%9C%E5%83%8F)

### 使用 U 盘配置开机脚本

>上文我们尝试了怎么使用 Linux shell 来进行联网操作，这里我们来尝试使用 U 盘配置开机脚本。

**对于 M2DOCK 如何使用 U 盘设置开机脚本呢？其实很简单只需要一下几个步骤：**

**第一步**：把（待存）脚本存成名为 `main.py` 的文件，然后根据第二步判断存放位置。
**第二步**：判断 U 盘目录下是否有 app 的文件夹，如果有就把 `main.py` 存进 `app` 文件夹后进行下一步，如果没有直接把 `main.py` 存放在 U 盘即可进行下一步。
**第三步**：存放好后使用电脑操作系统自带的移除 U 盘方式来保证文件在没有损坏的情况下保存进板卡，否则会因为不当操作而导致 `main.py` 没有正常保存到 U 盘（板卡系统）里面。

>**注意事项：**MaixPy3 IDE 运行时会停止 M2Dock 的开机脚本程序，所以我们应该在电脑托盘找到并退出 MaixPy3 IDE 或者选择仅使用板子上的 TypeC 串口来进行供电以查看开机运行脚本效果。

以下为 root 目录下 main.py 文件里的默认内容：

```python
#!/usr/bin/env python
from maix import camera, display, image, nn
image.load_freetype("/home/res/sans.ttf")
qrcode = image.open('/home/res/qrcode.png')
canvas = image.new((display.width(), display.height()), (0xFF, 0xFF, 0xFF), "RGB")
canvas.draw_image(qrcode, (canvas.width - qrcode.width) // 2, (canvas.height - qrcode.height) // 2)
info = "wiki.sipeed.com/maixpy3"
w, h = image.get_string_size(info, 1.2)
canvas.draw_string((canvas.width - w) // 2 + 5, canvas.height - h - 5, info, 1.2, color=(0x00, 0x00, 0x00))
for i in range(120):
    img = camera.capture().draw_image(canvas, alpha=0.7)
    display.show(img)
```

![logo](./assest/logo.jpg)

> 关于更多的 [配置开机脚本](https://wiki.sipeed.com/soft/maixpy3/zh/tools/0.MaixII-Dock.html#%E9%85%8D%E7%BD%AE%E5%BC%80%E6%9C%BA%E5%90%AF%E5%8A%A8%E8%84%9A%E6%9C%AC) 的详情资料可前往查看。

### 使用 U 盘传输文件

在使用 U 盘进行传输文件之前我们需要先了解电脑端 U 盘的目录与 M2DOCK 文件系统目录的对应规则。

>规则：电脑上的 U 盘对应着 M2DOCK 文件系统的 /root 目录。

传输文件操作如下：（前提 M2DOCK 通过 OTG 口连接电脑端）

**第一步**：将文件拖拽进 U 盘后相当于完成存储到 M2DOCK 系统上的操作。
**第二步**：存储后务必使用电脑系统自带的 U 盘移除相关的功能来断开电脑与 U 盘的通信。
**第三步**：最后进行重启（按下 RST 键或者重新插拔 USB）来使 m2dock 再次重新加载文件系统，否则会因为板卡与电脑非正常断开通信而导致文件系统损坏，保存失败。

## 学会使用文档（资源）

无论是在 K210 还是 M2DOCK（V831）上一定要学会使用我们公开的文档资料，去借助资料的力量帮助自己在学习的道路上往前走，学会借助资源完善自身的不足，可以让你少走很多的坑以及弯路。

1. 学会搜索并利用官方的 `文档社区` 以及 `github issue` 资源，会让新手小白少走很多弯路雷坑。
2. 文档资源在 `常见问题 FAQ` 中基本涵盖了所有的坑，使用途中报错可以先查看排错。
3. 想要实现更多的功能示例或需要更多的脚本源码，可前往 MaixPy3 的源码例程仓库查找。

**文档搜索例程**：[点击查看](https://wiki.sipeed.com/soft/maixpy/zh/how_to_read.html)
**BBS 社区教程贴**：[点击前往](https://bbs.sipeed.com/thread/492)
**MaixPy3 源码仓库**：[点击前往](https://github.com/sipeed/maixpy3)
**MaixPy3 issue**：[点击前往](https://github.com/sipeed/MaixPy3/issues)
**MaixPy3 常见问题指南**：[点击前往](https://wiki.sipeed.com/soft/maixpy3/zh/tools/0.MaixII-Dock.html#%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E6%8C%87%E5%8D%97)
**V831 源码**：[点击前往](https://github.com/Tina-Linux/tina-V83x)
**V83 工具链**：[点击前往](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/Toolchain)
**V831 常见问题与解决方法**：[点击前往](https://wiki.sipeed.com/soft/maixpy3/zh/question/maixpy3_faq.html)
**BBS 社区常见问题汇总贴**：[点击查看](https://bbs.sipeed.com/thread/489)

## 进阶使用

> 到达进阶使用这里后，这里则需要小伙伴们具备一些 Linux 基础了才能继续往下走学习。

### 认识 openwrt 系统

全志 V831 使用 Tina Linux 系统移植自 OpenWrt。

OpenWrt 可以被描述为一个嵌入式的 Linux 发行版，详情可看 [官方网址](https://openwrt.org) 和 [官方开源仓库](https://github.com/openwrt/openwrt)。

更多相关的详情点击:[详情资料](https://wiki.sipeed.com/hardware/zh/maixII/M2/usage.html#%E8%AE%A4%E8%AF%86-openwrt-%E7%B3%BB%E7%BB%9F)

### Opkg 包管理器

Opkg 是一个轻量快速的套件管理系统，目前已成为 Opensource 界嵌入式系统标准。常用于 路由、交换机等 嵌入式设备中，用来管理软件包的安装升级与下载。

相关的常用命令：[点击查看](https://wiki.sipeed.com/hardware/zh/maixII/M2/usage.html#Opkg-%E5%8C%85%E7%AE%A1%E7%90%86%E5%99%A8)

### pip 包管理器

[pip](https://pypi.org/project/pip/) 是 Python 包管理工具，该工具提供了对 Python 包的查找、下载、安装、卸载的功能。

如何使用示例：[点击查看](https://wiki.sipeed.com/hardware/zh/maixII/M2/usage.html#pip-%E5%8C%85%E7%AE%A1%E7%90%86%E5%99%A8)

### 如何更新 MaixPy3 包

有时镜像包更新但我们确不想再次进行烧录板子以作更新，这时可以手工更新 MaixPy3 达到更新目的。

**MaixPy3 最新安装包**：[点击前往下载](https://pypi.org/project/maixpy3/#history)
**Maixpy3 更新操作**：[操作示例](https://wiki.sipeed.com/soft/maixpy3/zh/tools/0.MaixII-Dock.html#%E6%9B%B4%E6%96%B0-MaixPy3-%E5%8C%85)

![maixpy3_cp38](./assest/maixpy3_cp38.jpg)

### 如何使用 USB 摄像头（主机模式）

>M2DOCK 是双 Type-c 接口的（分别是 UART/OTG）而 OTG 接口是默认作为 USB 从机来使用的。

如果想使用 USB 摄像头则需手动更改端口为主机模式，从板子上的串口 USB（UART）来操作板子，并执行以下命令修改 OTG 口为主机模式使用。

```shell
echo "usb_host" > /sys/devices/platform/soc/usbc0/otg_role
```

### 如何将 USB OTG 口作为从机

M2Dock 默认的 OTG 口就是 USB 从机设备，如有其他原因需重新设置成从机设备的话，只需在 M2DOCK 上执行以下命令即可。

```shell
echo "usb_device" > /sys/devices/platform/soc/usbc0/otg_role
```

### 更换屏幕

目前开发板支持的屏幕有 1.3寸、2.4寸、2.8寸 的 IPS 屏，且只是支持在我们淘宝上售卖的显示屏；对于别的屏幕有需求的，可以走商务通道进行定制。

**如何进行屏幕的切换及更新设备树**：[点击查看](https://wiki.sipeed.com/hardware/zh/maixII/M2/other.html#%E5%88%87%E6%8D%A2%E5%B1%8F%E5%B9%95)

### 更换摄像头

目前 MaixII-Dock 开发板目前支持的摄像头有 sp2305、vs3205、ov2685（只支持在官方店上再售卖的摄像头，有别的摄像头需求可以进行商务定制），摄像头之间的切换同样时需要更换设备树文件，更换方式上面的更换屏幕一样的。

**如何进行摄像头以及设备树的切换**：[点击查看](https://wiki.sipeed.com/hardware/zh/maixII/M2/other.html#%E6%9B%B4%E6%8D%A2%E6%91%84%E5%83%8F%E5%A4%B4)

### 编译链

有需求的可以自行尝试，但是对于 V831 还是推荐使用 MaixPy3 和 MaixHub。

**Linux 系统下 V831 使用编译链**：[toolchain-sunxi-musl-pack-2021-01-09.tar.xz](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/Toolchain)

## 如何编译与开发

### 系统环境搭建

- 安装 vscode 和换源：[点击前往](https://fishros.org.cn/forum/topic/20/%E5%B0%8F%E9%B1%BC%E7%9A%84%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%E7%B3%BB%E5%88%97)
- 安装输入法：[点击前往](https://shurufa.sogou.com/linux/guide)
- 安装截图工具：[点击前往](https://zhuanlan.zhihu.com/p/88325211)，并设置快捷键为 `ctrl + alt + a`.
- 安装魔法上网工具：自行安装

### MaixPY3 架构介绍

篇幅过多这里不详细介绍，小伙伴可根据指路前往：[MaixPy3 架构介绍](https://wiki.sipeed.com/soft/maixpy3/zh/others/framework.html)

### 为什么采用 libmax 开发

```C++
+----------------------------------------+
|                                        |
|    User develop sipeed all product.    |
|                                        |
+----------------------------------------+

+-----------------+     +----------------+
|                 |     |                |
| Run Python Code |     | Run C/C++ Code |
|                 |     |                |
+--------^--------+     +-------^--------+
         |                      |
   +-----+-----+                |
   |           |                |
   |  maixpy3  |                |
   |           |                |
   +-----^-----+                |
         |                      |
    +----+----+                 |
    |         |                 |
    | libmaix +-----------------+
    |         |
    +----^----+
         |
+----------------------------------------+
|  +-------------+                       |
|  |             |   openwrt   debian    |
|  |    Linux    |                       |
|  |             |   armbian   ubuntu    |
|  +-------------+                       |
+-------------------------+------------+-+
      ^        ^          ^            ^
      |        |          |            |
+-----++ +-----++ +-------++ +---------+-+
|      | |      | | x86/64 | |  AX620A   |
| V83X | | R329 | | debian | |   V85X    |
|      | |      | | ubuntu | |  more...  |
+------+ +------+ +--------+ +-----------+

```

可以清楚的看到我们平时用的 Python 的接口底层实现也是通过了 libmaix 的开发成果，我们平时需要 Python 语言调参验证原型功能，是为了快速验证我们的开发板可用于不同的场景和功能，方便我们快速验证功能外设是否正常，同时我们也需要 C / C++ 优化性能和减少内存占用用于开发商业项目，那么，直接使用 libmaix 进行开发就显得尤为重要了。
一开始采用的 python 需要一定时间过渡到 c++ ，特别是成熟的项目，更需要脱离 python 了，为了更成熟精简的项目结构和更好的性能，这就不得不看看 libmaix 了喵。

#### 首先要配置好开发环境

参考下面连接完成你的开发环境配置

1. [V831 如何使用 libmaix SDK C++ 开发](https://wiki.sipeed.com/news/MaixPy3/run_lvgl/run_lvgl.html)
2. [Linux 连接不上 adb 设备](https://wiki.sipeed.com/news/others/linux_adb/linux_adb.html)

完成了上面的环境配置后，这里提供了一个Demo，内容就是如何使用 V831 LINUX C++ 进行图像视觉处理和开发，在此我提供了一个 串口 + mv cv ai 的示例项目，供开发者评估使用，此处不涉及到 ISP 调试，需要进一步 ISP 图像调试则需要联系大佬鼠。

>相关资料：[libmaix](https://github.com/sipeed/libmaix/blob/6ad1102a0527bd3d394c0b1de82cbf64d6eac40d/components/maix_dls831/src/dls831_uvai.cpp#L435-L663)

**操作步骤**：连接上板子的 OTG 接口后，在 `/libmaix/libmaix/examples/app_dls831` 目录下使用 `make` 下进行编译（编写好的脚本会自动把编译好的文件上传并运行）。

![libmaix](./assest/libmaix.jpg)

我们可以看到程序是稳定三十帧的运行速率。

<html>
  <img src="./assest/h26x_831.jpg" width=45%>
  <img src="./assest/fps.jpg" width=45%>
</html>



