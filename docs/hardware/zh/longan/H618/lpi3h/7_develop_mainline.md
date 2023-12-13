---
title: 主线 Linux
keywords: Linux, Longan, H618, SBC, ARM, Kernel, SDK, Develop
update:
  - date: 2023-12-08
    version: v1.0
    author: ztd
    content:
      - Release docs
---

该文档以 Ubuntu 22.04 为例，演示如何搭建 LonganPi 3H 并进行主线Linux的开发。

在正式合并入主线前，需要拉取 Github 仓库，获取patch开发，预计将于 2024Q1 合并入主线Linux。

首先用 git 拉取仓库到本地，并安装工具链：
```shell
git clone https://github.com/sipeed/LonganPi-3H-SDK.git
sudo apt install gcc-aarch64-linux-gnu
```

然后进入到仓库所在目录，运行其中的脚本即可得到构建出的 uboot, kernel, dtb 和 rootfs。
```shell
cd LonganPi-3H-SDK
./mkatf.sh
./mklinux.sh
./mkuboot.sh
./mkrootfs.sh
```

生成的 Image文件，设备树文件，会复制到该仓库目录下的 overlay/boot/ 文件夹中，生成的内核模块会复制到该仓库目录下的 overlay/usr/ 文件夹中。

