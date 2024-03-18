---
title: 多媒体框架（MMF）开发指南
keywords: riscv, licheerv, nano, mmf
update:
  - date: 2024-02-04
    version: v0.1
    author: lxowalle
---

## 简述

本文用来介绍使用算能SDK开发MMF的方法，为想要上手开发MMF却无从下手的开发者提供一个开发思路。
MMF全称是多媒体软件架构（Multimedia Framework），这个架构将视频输入输出、音频输入输出、图像信号处理、硬件编解码等功能提供了统一格式的API，用户可以通过调用封装好的API来快速实现多媒体相关的功能。

## 搭建MMF的开发环境

请参考`LicheeRV Nano->系统开发->cvi_mmf_sdk`中介绍的方法来搭建MMF的开发环境

或者参考下面的指令

```shell
# 下载依赖
sudo apt install pkg-config build-essential ninja-build automake autoconf libtool wget curl git gcc libssl-dev bc slib squashfs-tools android-sdk-libsparse-utils android-sdk-ext4-utils jq cmake python3-distutils tclsh scons parallel ssh-client tree python3-dev python3-pip device-tree-compiler libssl-dev ssh cpio squashfs-tools fakeroot libncurses5 flex bison

# 下载sdk和工具链
git clone https://github.com/sipeed/LicheeRV-Nano-Build.git
wget https://sophon-file.sophon.cn/sophon-prod-s3/drive/23/03/07/16/host-tools.tar.gz
tar xvf host-tools.tar.gz

# 用build_middleware命令编译所有示例
cd LicheeRV-Nano-Build
ln -s ../host-tools ./
source build/cvisetup.sh
defconfig sg2002_licheervnano_sd
build_middleware
```

上述指令介绍了如何安装MMF相关的编译环境，以及如何编译SDK提供的MMF示例。

- 注意：你可能在编译sample_cvg时会失败，如果不需要使用这个示例，则删掉`LicheeRV-Nano-Build/middleware/v2/sample/cvg`文件夹后再重试。如果你需要这个demo，则使用build_all编译后再尝试，build_all需要编译整个sdk，因此编译时间较长

## 开发资料

请参考`LicheeRV Nano->板卡介绍`中来找到大部分资料

对于MMF应用可以着重看下面的资料

- [MMF媒体软件开发指南](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/MPI/Media_Processing_Software_Development_Reference/build/html/index.html)或者[Media Processing Software Development Reference](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/en/01.software/MPI/Media_Processing_Software_Development_Reference/build/html/index.html)
- [SDK LicheeRV-Nano-Build](https://github.com/sipeed/LicheeRV-Nano-Build)

## 通过网络连接开发板

通过网络连接开发板的目的是为了让我们编译的固件可以被上传到板子中。

请参考`LicheeRV Nano->外设使用`中的方法来获取开发板的IP地址，三种方法任意实现其中一种即可：`网线连接`、`WIFI连接`、`USB RNDIS连接`

## 编译和运行一个示例

MMF内部封装了直接操作硬件的方法，因此稍有疏忽就有导致系统崩溃的可能，开发MMF一定要注意保持耐心和注重细节。建议是通过示例来修改出自己的程序。

以sample_vio为例

```shell
# 确保已经搭建好了MMF的基本编译环境，并且已经使用build_middleware编译过一次
# 编译sample_vio
cd middleware/v2/sample/vio
make

# 上传到开发板(账户root，密码cvitek)
scp sample_vio root@xxx.xxx.xxx.xxx:/root	# xxx.xxx.xxx.xxx是板子的IP地址

# 登入开发板
ssh root@xxx.xxx.xxx.xxx

# 如果需要使用显示屏，则需要运行fb_load.sh以确保加载了驱动（只需要执行一次）
# 新版镜像不用执行这个，已经内置到uboot
/opt/fb_load.sh

# 运行示例
cd ~
./sample_vio
```

上述指令介绍了如何编译某一个MMF示例，以及上传示例到开发板和运行这个示例。开发者可以根据自己的应用来修改示例，最后开发出自己想要实现的功能。

## 出现无法解决的问题怎么办

1. 请保持耐心、并仔细的参阅开发资料，尝试找到是否存在遗漏的地方。比如输入参数是否正确、资源是否真正的释放等。
2. 在[maixhub](https://maixhub.com/discussion)或github上发布你的问题。请整理好你想要实现的功能、遇到的问题、尝试过的解决方案以及复现方法，顺便一提，很多时候在整理思路的过程中就能找到解决的方法了。

