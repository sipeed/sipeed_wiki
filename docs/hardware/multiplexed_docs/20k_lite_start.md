---
title: Primer 20K Lite 初见
keywords: Primer 20K, Lite, FPGA
desc: Primer 20K 上手
date: 2022-08-12
tags: FPGA, Primer 20K
cover: ./assets/cover.png
---

拿到 Primer 20K Lite 后上手点个灯

<!-- more -->

先把目录放这里吧，需要的话自己直接点击跳转就行。

## 前言

本篇内容是给用户拿来做流水灯实验所用，目的是引导新用户快速完成点灯神技。

## 安装 IDE

参考 [安装IDE](https://wiki.sipeed.com/hardware/zh/tang/Tang-Nano-Doc/get_started/install-the-ide.html) 来完成我们需要准备的软件环境。

过段时间教育版的 IDE 会支持 GW2A-18 器件，不想申请 license 的话可以使用这个版本。

当然对于 Windows 用户我们来额外下载一下 [Programmer](https://dl.sipeed.com/shareURL/TANG/programmer) 烧录专用软件可以降低我们在烧录的时候出现问题的可能性。

对于 Linux 用户的话建议使用 [openfpgaLoader](https://wiki.sipeed.com/hardware/zh/tang/Tang-Nano-Doc/get_started/flash_in_linux.html) 这软件（作者会很快修复 GW2A-18 不能烧录的问题）。

## 新建工程

文件 -> 新建 -> FPGA Design -> Project

<div>
    <img src="./assets/new_project.png" width=55%>
    <img src="./assets/fpga_project.png" width=35%>
</div>

设置工程名称，要求只用英文的下划线命名，存放路径中不要有中文字符或者空格等。

然后在下面的芯片型号中选择 GW2A-LV18PG256C8/I7，这上面的筛选其中选择正确的类型容易更快的选到型号。
![device_choose](./assets/device_choose.png)

