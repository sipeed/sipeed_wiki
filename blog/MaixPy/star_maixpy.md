---
title: MaixPy 上手指南（避坑）之上手篇
keywords: MaixPy, K210, Python, MicroPython
desc: MaixPy 上手指南（避坑） 之上手篇
date: 2022-04-01
tags: MaixPy, K210

---

> 作者：Ray（Rui）

拿到热乎的 K210 开发板，如何上手使用。我接触了许许多多的小白开发者后，整理出来的资料和路线，希望可以减少你们遇到的问题，可以更加愉快的使用 K210 进行自己的项目开发。

<!-- more -->

## K210 开发板

市面上有很多中关于 K210 的开发板，但是并不是所有的开发板都是可以使用 MaixPy 进行开发的。毕竟不同厂商使用的摄像头、屏幕、引脚上使用，都是由差异性的。目前支持的使用 MaixPy 开发的板子有 Sipeed 家的 [Maix 系列](/hardware/zh/maix/readme.md)。

如果是试用别家的开发板，并不能很好的兼容 MaixPy，存在差异性。

## 开箱

拿到开发板，首先需要根据屏幕和摄像头排线上的丝印提示来安装好，即排线上的数字 “1” 和板子卡座边上引脚丝印 “1” 方位对应接上。上电之后，屏幕上会显示出一个红色的界面这是开发板已经正常启动了。（也可能存在部分丝印印反）

### 首先要安装开发环境：

1. [【安装驱动】](/soft/maixpy/zh/get_started/env_install_driver.md) 根据自己使用的开发进行选择需要按安装驱动
2. [【更新固件】](/soft/maixpy/zh/get_started/upgrade_maixpy_firmware.md) 确保使用的是最新版本的固件，并学习一下每个固件之间的[差异](/soft/maixpy/zh/get_started/upgrade_maixpy_firmware.html#固件命名说明)
3. [【安装 MaixPy IDE】](/soft/maixpy/zh/get_started/env_maixpyide.html) 

如果安装驱动的时候出现安装失败，或者是安装驱动之后，电脑上没有显示 COM 口的，就需要更新一下系统或者是检查一下自己的系统是不是正版的了。因为有部分的盗版系统安装不上驱动，或者是安装驱动之后并显示。或者通过换 USB 口进行连接，也许就可以检测到开发板

### 运行代码检测摄像头

将开发板接到电脑上，打开 MaixPy IDE，运行打开的例程代码，检查自己的屏幕和摄像头是否正确连接上了。如果运行例程代码之后，并没有图像出现来屏幕和 IDE 上时，可能摄像头接反了。

## 开始学习使用

开始使用 K210 之前，一定要学习 Python，如果你连 Python 都不会的，就不要继续往下走，可以快速的过一遍 [Python](/soft/maixpy3/zh/origin/python.md) 的语法和使用，一定要会 Python !一定要会 Python !一定要会 Python !

现在就当你懂 Python 了，这是就可以开始看 MaixPy 文档中的[【入门指南】——【上手】](/soft/maixpy/zh/get_started/get_started_power_on.md)，进行对于 MaixPy 的使用和 K210 的基本了解。

[【进阶教程】](/soft/maixpy/zh/course/readme.md) 中将有 MaixPy 更多的使用案例和使用方式，一定要确保自己已经对应入门教程中内容已经了解和掌握了再去看，否则你在学习的时候还是会一脸懵逼，不知所云。

## 获取 AI 模型文件

在【进阶教程】中是有讲述如何运行神经网络模型，也知道怎么去获取示例中的模型文件，但是少了如何获取机器码这个操作，这里详细的讲述一下何如获取机器码。

1. 将 [key_gen.bin](https://dl.sipeed.com/fileList/MaixHub_Tools/key_gen_v1.2.bin) 这个固件通过 Kflash 烧录到开发板上。烧录这个机器码固件之后，开发板是处于一个不能使用的状态，上电屏幕只会变成一个白屏。
2. 这时将开发板通过 USB 连接到电脑上，利用[【串口连接】](/soft/maixpy/zh/get_started/env_serial_tools.html)中的方式来连接开发板。注：IDE 中的串口终端和 IDE 的连接方式相对独立的，而且串口不能通过多种方式进行连接
3. 利用串口软件连接上开发板，这时按下开发板上的 reset 的按键，就会出现一串字符在终端窗口上，这就机器码。如果机器码

> 推荐使用 IDE 中的 串口终端进行查看，这个相对别的软件更加适合 K210

机器码是一机一码的一种加密方式，用于模型文件的加密。如果使用别的机器码去加密或者下载以 smodel 为文件后缀的模型文件，开发板是无法使用该模型文件的。
