---
title: 主线 Linux
keywords: Linux, Longan, H618, SBC, ARM, Kernel, SDK, Develop
update:
  - date: 2024-05-08
    version: v1.2
    author: 0x754C
    content:
      - Rewrite build script
  - date: 2024-04-07
    version: v1.1
    author: ztd
    content:
      - Add Debian & Ubuntu CLI image build instructions.
  - date: 2023-12-08
    version: v1.0
    author: ztd
    content:
      - Release docs
---

该文档以 Ubuntu 22.04 为例，演示如何搭建 LonganPi 3H 开发环境并进行主线Linux的开发。

在正式合并入主线前，需要拉取 Github 仓库，获取patch开发，预计将于 2024Q1 合并入主线Linux。

## 环境配置
首先用 git 拉取仓库到本地

```shell
git clone https://github.com/sipeed/LonganPi-3H-SDK.git
```

然后根据README设置构建环境

## 构建

进入到仓库所在目录，运行其中的脚本:

```shell
cd LonganPi-3H-SDK
# 文件会输出在 build 目录下
./mkatf.sh     # 编译atf,     输出bin文件,用作uboot构建
./mklinux.sh   # 编译linux，  输出deb文件,用作rootfs构建
./mkuboot.sh   # 编译uboot,   输出bin文件,用作image构建
./mkoverlay.sh # 打包overlay, 输出deb文件,用作rootfs构建
./mkrootfs.sh  # 打包rootfs,  输出tar文件,用作image构建
./mkimage.sh   # 打包启动镜像,输出img文件,最终文件

ls ./build/images/sdcard.img # 用于烧录的文件
```

接下来介绍 SDK 仓库的主要文件构成及其作用：

`linux` 文件夹下，存放的是 kernel 的 patch 文件，在第一次运行 mklinux.sh 时会自动将这些 patch 打入到 kernel 源码中。

`uboot` 文件夹下，存放的是 uboot 的 patch 文件， 在第一次运行 mkuboot.sh 时会自动将这些 patch 打入到 uboot 源码中。

`overlay` 文件夹下有一些用于自定义镜像的文件，在运行 mkoverlay.sh 时会将这些文件打包为overlay.deb

`mkrootfs.sh` 用于构建rootfs的tar归档文件

`mkimage.sh` 用于构建可以启动的SD卡镜像

构建完成后，可以参考[烧录镜像](https://wiki.sipeed.com/hardware/zh/longan/h618/lpi3h/4_burn_image.html)把得到的 img 镜像文件烧录到 TF 卡中。
