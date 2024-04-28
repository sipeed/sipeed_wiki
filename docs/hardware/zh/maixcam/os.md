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

### 读卡器烧录 TF 卡

* 直接取出 TF 卡，插入读卡器，然后插入电脑。
* 打开 Etcher，选择镜像文件，选择 TF 卡，点击`Flash`。
* 等待烧录完成，弹出 TF 卡，插入 MaixCAM，然后上电，等待系统启动，第一次启动会慢一点，等待一会即可。

### USB 更新 TF 卡镜像

**注意使用 USB 只能更新系统不能用作第一次烧录。**
请保证 TF 里面已经用 读卡器烧录过系统，并且**系统能正常运行**之后才能用这种方式。

* MaixCAM 断电，保持 TF 卡插入。
* 按住设备的 `user` 按键不松开，插入 USB 线连接到电脑，（或者先插入 USB 线，然后按住 `usr`按键不放，再按一下`reset`按钮立即松开）等待 U 盘设备出现在电脑上。
* 打开 `Etcher`，选择镜像文件，选择 U 盘设备，点击`Flash`。
* 等待烧录完成，然后按一下 `reset` 按键或者重新上电，等待系统启动，第一次启动会慢一点，等待一会即可。


## 使用系统注意点

### 强制关机

除了上诉情况使用`reset`按钮，平时正常使用系统时**不建议按`reset`按钮**，这个按钮是强制断电，如果你的系统正在写入内容到 TF 卡，可能会造成系统和数据损坏。
另外系统仍在运行，强制拔掉电源和按`reset`按钮的是同样的问题，尽量**先软件关机再拔电源**。

正常使用请**软件关机或者重启**，方法：
* 方法一： 界面选择`设置`->`电源` 进行软件关机或者重启。
* 方法二： 终端使用`poweroff` 或者`reboot`命令进行软件关机或者重启。
* 方法三：其它软件调用，比如 `Python` 调用 `import os;os.system("poweroff")` 进行关机或者重启。





