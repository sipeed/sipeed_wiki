---
title: MaixCAM 系统烧录
---


## 下载系统

在 [MaixPy 发布页面](https://github.com/sipeed/MaixPy/releases) 找到最新的系统镜像文件，比如`maixcam_os_20240401_maixpy_v4.1.0.xz`。

备用地址：
* [Sourceforge](https://sourceforge.net/projects/maixpy/files/)


## 准备烧录工具

下载 [Etcher](https://etcher.balena.io/)，安装并打开。

Windows 也可以用 [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/) 或 [Rufus](https://rufus.ie/)。


## 烧录 TF 卡

有两种方式烧录 TF 卡：

## 读卡器烧录 TF 卡

* 直接取出 TF 卡，插入读卡器，然后插入电脑。
* 打开 Etcher，选择镜像文件，选择 TF 卡，点击`Flash`。
* 等待烧录完成，弹出 TF 卡，插入 MaixCAM，然后上电，等待系统启动，第一次启动会慢一点，等待一会即可。

## USB 烧录 TF 卡

* MaixCAM 断电，保持 TF 卡插入。
* 按住设备的 `user` 按键不松开，插入 USB 线连接到电脑，等待 U 盘设备出现在电脑上。
* 打开 Etcher，选择镜像文件，选择 U 盘设备，点击`Flash`。
* 等待烧录完成，然后按一下 `reset` 按键或者重新上电，等待系统启动，第一次启动会慢一点，等待一会即可。







