---
title: AXera-Pi 烧录系统
tags: AXera-Pi, 烧录系统
keywords: AXera-Pi，烧录, 上手
desc: AXera-Pi 烧录系统
update:
  - date: 2022-09-13
    version: v0.1
    author: lyx
    content:
      - 初稿
  - date: 2022-09-29
    version: v0.2
    author: wonder
    content:
      - 丰富内容
---

---

## 系统简介

AXera-Pi 默认板卡没有存储介质，因此需要准备一张系统卡来启动设备。

目前 AXera-Pi 提供的是 Debian11 Bullseye 镜像，[Ubuntu 源自 Debian。 这意味着 Ubuntu 使用与 Debian 相同的 apt 打包系统，并共享来自 Debian 存储库的大量软件包和库，利用 Debian 基础设施作为基础。 大多数“派生” Linux 发行版，它们使用相同的包管理系统并与基于的发行版共享软件包。 ](https://zhuanlan.zhihu.com/p/426219868)。

> [选择 Debian 的理由](https://www.debian.org/intro/why_debian)

官方店铺可以购买到预烧录了系统镜像的 SD 卡，不然的话就需要进行下面的操作来自己准备 SD 镜像卡了。

## 获取镜像

因为镜像文件比较大，因此这里仅提供百度云下载链接：

前往百度云

## 烧录镜像

### 准备工作

硬件：
- 一张容量大于 4G 的 SD 卡；建议购买官方提供的卡，不然可能因为其他的 SD 卡质量差而带来糟糕的体验
- 一个读卡器；建议使用 USB3.0 接口得读卡器，不然读卡器得 USB 速度过低会导致烧录时间过长

软件：
- <a href="https://www.balena.io/etcher/" alt="Etcher" target="_blank"> Etcher </a>；根据自身电脑下载对应版本的软件即可

### 镜像系统烧录方法

首先解压所下载的镜像压缩包，得到 `.img` 镜像文件，打开 [Etcher](https://www.balena.io/etcher/ "Etcher") 软件，点击 `Flash from file` ,选中解压出来的 `.img ` 文件镜像，然后点击 `Select target` 选中sd卡，最后点击 `Flash` 进行烧录，等待完成即可。 

最终下载结束后的效果会和下图一样，显示 `Flash Complete!`：

![下载结束](./../../maixII/M2A/assets/finish_flash.png)

如果烧录失败了，请手动格式化一下 sd 卡。Windows 和 MacOS 可以使用 [SD Card Formatter](https://www.sdcard.org/downloads/formatter/eula_windows/SDCardFormatterv5_WinEN.zip)来格式化 sd 卡，Linux 系统可以使用 [Gparted](https://gparted.org/)来格式化。

<!-- 烧录方法如下图示意
![etcher](../../../assets/maixIII/ax-pi/etcher.jpg)
点击“flash!”开始烧录，可看到进度条的跳动。
![etcher_two](../../../assets/maixIII/ax-pi/etcher_t.jpg)
最终下载结束后的效果会和下图一样，显示 `Flash Complete!`：
![etcher_three](../../../assets/maixIII/ax-pi/etcher_h.jpg)
如果烧录失败的话 方法： -->
