---
title: 给 M2Dock 安装 Opencv
keywords: M2Dock, Opencv, Python, V831
date: 2022-07-23
tags: Opencv, M2Dock, V831
---

M2Dock 既然能够运行 Python, 那么我们也可以给它安装 Opencv。

<!-- more -->

## 前言

由于 V831 性能有限，且交叉编译什么的对于大多数人来说太烦琐了，因此这里提供一个 github 上的一位的大神 [irfan798](https://github.com/irfan798) 所 release 的一个适用于 M2Dock 的 Opencv 库。

仓库地址: [v83x_opencv-4.5.5.62_numpy-1.19.2](https://github.com/irfan798/maix3_opencv_python/releases/tag/cv-4.5.5.62_numpy-1.19.2)

相关的使用方法在 release 页面已经写了，但是不会操作话可以继续往下面看。

## 下载、安装、运行

![download_open](./assets/download_opencv.png)

点击上图中红框处的文件即可下载由 [irfan798](https://github.com/irfan798) 所发布的适用于 M2Dock 的 Opencv Python 安装包。

把下载下来的名为 `opencv_python_headless-4.5.5.62-cp38-cp38-linux_armv7l.whl` 文件复制到由 M2Dock 在电脑上所显示的 U 盘中。

在 adb 命令行终端中依次执行下面的命令来在 M2Dock 上安装刚刚所下载的 Opencv Python 安装包：

```shell
sync  #刷新所有文件
pip install /root/opencv_python_headless-4.5.5.62-cp38-cp38-linux_armv7l.whl --upgrade #安装刚刚下载的 Opencv Python 安装包
```

要注意的是上面的操作是需要在 M2Dock 的命令终端执行。

成功安装完之后我们可以在 M2Dock 上运行 Opencv 了。如下所示:

```shell
root@sipeed:~# python
>>> cv2.version
'4.5.5'
```

## 其他

如果你想使用其他的 numpy 版本，可以根据 [irfan798](https://github.com/irfan798) 所创建 [https://github.com/irfan798/maix3_opencv_python](https://github.com/irfan798/maix3_opencv_python) 仓库里面的 README.md 内的相关操作来自行编译自己想要的 numpy 版本。