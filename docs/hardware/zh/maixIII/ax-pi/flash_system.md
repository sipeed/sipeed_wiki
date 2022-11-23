---
title: AXera-Pi 烧录系统
tags: AXera-Pi, 烧录系统
keywords: AXera-Pi，烧录, 上手
desc: AXera-Pi 烧录系统
update:
  - date: 2022-11-10
    version: v0.3
    author: wonder
    content:
      - 优化排版
  - date: 2022-09-29
    version: v0.2
    author: wonder
    content:
      - 丰富内容
  - date: 2022-09-13
    version: v0.1
    author: lyx
    content:
      - 初稿
---

---

## 系统简介

AXera-Pi 默认板卡没有存储介质，因此需要准备一张系统卡来启动设备。

目前 AXera-Pi 提供的是 Debian11 Bullseye 镜像，[Ubuntu 源自 Debian。 这意味着 Ubuntu 使用与 Debian 相同的 apt 打包系统，并共享来自 Debian 存储库的大量软件包和库，利用 Debian 基础设施作为基础。 大多数“派生” Linux 发行版，它们使用相同的包管理系统并与基于的发行版共享软件包。 ](https://zhuanlan.zhihu.com/p/426219868)。

> [选择 Debian 的理由](https://www.debian.org/intro/why_debian)

官方店铺可以购买预烧录系统镜像的 SD 卡，否则就需要自己进行以下的操作来准备 SD 镜像卡了。

## 如何选择 SD 卡？

除了在官方店铺购买以及预烧录 debian11 的 SD 卡还可以在参考以下表格选择适合需求的 SD 卡。
为了方便用户选择，我们对部分 SD 卡在 AXera-Pi 板子上进行了读写测速。

![sd](./../assets/sd.jpg)

> 因为部分 SD 卡是后面陆续才进行测试，没有一一单独拍照但可以根据型号辨认。 

| 序号 | 型号                                     | <p style="white-space:nowrap">写入速度（写入量 160MB）</p> | <p style="white-space:nowrap">读取速度（读取量 160MB） </p> |
| ---- | ---------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| 1.   | Netac 朗科 A2  P500-超高速-64GB 存储卡   | 2.04697 s, 80.0 MB/s                                       | 1.8759 s, 87.3 MB/s                                         |
| 2.   | 三星 microSDXC UHS-I 128G 存储卡（蓝卡） | 2.53387 s, 64.7 MB/s                                       | 1.99882 s, 82.0 MB/s                                        |
| 3.   | EAGET TF卡（T1系列）64G 存储卡           | 6.56955 s, 24.9 MB/s                                       | 7.13792 s, 23.0 MB/s                                        |
| 4.   | 京东 高性能 microSDXC UHS-I 128G 存储卡  | 2.28133 s, 71.8 MB/s                                       | 1.92001 s, 85.3 MB/s                                        |
| 5.   | KIOXIA microSDXC UHS-I 32G 存储卡        | 6.71284 s, 24.4 MB/s                                       | 2.36794 s, 69.2 MB/s                                        |
| 6.   | Netac 朗科 A1 32GB 存储卡                | 4.31411 s, 38.0 MB/s                                       | 2.00759 s, 81.6 MB/s                                        |
| 7.   | BanQ JOY card 白金 64G 存储卡            | 9.08105 s, 18.0 MB/s                                       | 9.02843 s, 18.1 MB/s                                        |
| 8.   | 海康威视 HS -TF- P2 64G 存储卡           | 2.28079 s, 71.8 MB/s                                       | 1.87698 s, 87.3 MB/s                                        |

下面为没有拍照但是测速过的卡：

| 序号 | 型号                                                  | <p style="white-space:nowrap">写入速度（写入量 160MB）</p> | <p style="white-space:nowrap">读取速度（读取量 160MB） </p> |
| ---- | ----------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| 1.   | 雷克沙（Lexar）64GB TF（MicroSD）存储卡 C10 U3 V30 A2 | 2.59644 s, 63.1 MB/s                                       | 1.9106 s, 85.8 MB/s                                         |
| 2.   | 雷克沙（Lexar）128GB TF（MicroSD）存储卡 C10 U3 V30   | 6.73793 s, 24.3 MB/s                                       | 6.94079 s, 23.6 MB/s                                        |

## 获取镜像

因为镜像文件比较大，因此这里仅提供百度云下载链接。

前往百度云 [点我](https://pan.baidu.com/s/1-UtDoAVP6spwqjHP2wneJA) ，提取码 `sdls` ,下载文件，镜像包与校验文件都已经放在里面了。

![debian](./../assets/debian.jpg)

用两个文件名来举例，其中文件命名规则如下（拖动滚动条来查看全部）：

| 文件名                                 | 提供方 | 文件类型                                          | 适用芯片 | 镜像发行版 | 发布日期 |
| -------------------------------------- | ------ | ------------------------------------------------- | -------- | ---------- | -------- |
| sipeed_ax620a_debian11_20221013.zip    | sipeed | 镜像压缩包                                        | ax620a   | debian11   | 20221009 |
| sipeed_ax620a_debian11_20221013.md5sum |        | <p style="white-space:nowrap">md5sum 校验文件</p> |          |            |          |

如果里面有多个镜像文件，那么建议下载最新的镜像文件。

校验文件需要在 Linux 环境中使用，windows10 及以上的用户可以使用 wsl 当作 Linux 环境。

使用方法为 `md5sum -c md5sum校验文件`。

.. details::点我查看校验 log

    ```bash    
    root@desktop:$ md5sum -c sipeed_ax620a_debian11_20221009.md5sum
    sipeed_ax620a_debian11_20221009.zip: OK
    ```

## 烧录镜像

### 准备工作

**硬件**：
- 一张容量大于 8G 的 SD 卡：建议购买官方提供的卡，不然可能因为其他的 SD 卡质量差而带来糟糕的体验
- 一个读卡器：建议使用 USB3.0 接口的读卡器，不然读卡器的 USB 速度过低会导致烧录时间过长

**软件**：
- <a href="https://www.balena.io/etcher/" alt="Etcher" target="_blank"> Etcher </a>：根据自身电脑下载对应版本的软件即可

### 镜像系统烧录方法

> **20221012** 现已确认 Etcher 软件可直接支持烧录 zip 压缩包里面的 img 镜像，用户不需要解压的步骤直接选择 zip 文件按下面步骤操作即可。

首先打开 [Etcher](https://www.balena.io/etcher/ "Etcher") 软件，点击 `Flash from file` ,选中已经下载好的 `zip` 文件镜像，然后点击 `Select target` 选中sd卡，最后点击 `Flash` 进行烧录，等待完成即可。 

**解压出镜像文件：**
![extract_image_file](./../../../assets/maixIII/ax-pi/extract_image_file.gif)

**烧录镜像文件到 SD 卡：**
![burn_image_by_etcher](./../../assets/../../assets/maixIII/ax-pi/burn_image_by_etcher.gif)

下图是烧录过程中的一张截图（可参照）：
![axera_burning_image](./../../../assets/maixIII/ax-pi/axera_burning_image.png)

最终下载结束后的效果会和下图一样，显示 `Flash Complete!`：

![下载结束](./../../maixII/M2A/assets/finish_flash.png)

> **注意**：如果出现烧录失败的情况，请手动格式化一下 SD 卡。
> Windows 和 MacOS 可以使用 [SD Card Formatter](https://www.sdcard.org/downloads/formatter/eula_windows/SDCardFormatterv5_WinEN.zip)来格式化 SD 卡，Linux 系统可以使用系统的 disk 工具或 [Gparted](https://gparted.org/)来格式化。

## 上手指引系列

1. 根据上文自行烧录镜像系统到 TF/SD 卡里。
   
   ![axpi-flash](./../assets/axpi-flash.png)

2. 当烧录系统完成后，我们需要给 AXera-Pi 进行正确的接线并且上电。
   **如何正确接入屏幕及摄像头**：[点击查看](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/basic_usage.html#%E6%8E%A5%E7%BA%BF%E7%A4%BA%E4%BE%8B).

   ![axpi-connect](./../assets/axpi-connect.png)
 
3. 以上的准备工作完成后，可以开始对 AXera-Pi 登陆系统进行使用配置。
   **如何登陆 Linux debian11 系统**：[点击查看](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/basic_usage.html#%E6%8E%A5%E7%BA%BF%E7%A4%BA%E4%BE%8B).

   ![axpi-login](./../assets/axpi-login.png)

4. 登陆上 Debian 系统后即可体验我们内置的众多 AI 开箱应用。
   **如何体验内置 AI 应用**：[点击查看](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/basic_usage.html#%E5%86%85%E7%BD%AE%E5%BC%80%E7%AE%B1%E5%BA%94%E7%94%A8).

   ![axpi-ai](./../assets/axpi-ai.png)

  

