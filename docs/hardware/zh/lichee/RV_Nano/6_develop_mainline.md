---
title: LicheeRV Nano Develop
keywords: riscv, licheerv,nano
update:
  - date: 2024-1-26
    version: v0.1
    author: 0x754C
---

## 芯片手册

datasheet: https://github.com/sophgo/sophgo-doc/releases

## 芯片启动流程

1. bootrom 判断sd卡第一个FAT32分区内是否拥有 fip.bin，如果有，则执行2，如果没有，则进入usb烧录模式(提供一个ACM串口从机设备)

2. 加载fip.bin，跳转到fsbl,初始化clock,DRAM,执行3

3. 加载opensbi，执行，然后跳转到uboot,执行4

4. uboot加载第一个分区内的boot.sd文件到DRAM，如果文件没有问题,跳转到5

5. 跳转到boot.sd内提供的代码(通常是Linux内核)

## cvi_mmf_sdk

基于算能官方SDK修改，如果要使用mmf框架，则必须使用这个SDK

源码:

https://github.com/sipeed/LicheeRV-Nano-Build/tree/v4.1.0

构建环境搭建可以参考repo内的github cicd文件:

https://github.com/sipeed/LicheeRV-Nano-Build/blob/main/.github/workflows/licheervnano-host-linux-amd64.yml

文档:

- 编译工具链下载地址：https://sophon-file.sophon.cn/sophon-prod-s3/drive/23/03/07/16/host-tools.tar.gz
- 软件SDK下载地址： https://github.com/sophgo/cvi_mmf_sdk
- SDK开发文档汇总：https://developer.sophgo.com/thread/471.html
- HDK 开发文档汇总： https://developer.sophgo.com/thread/472.html
- TPU SDK 开发资料汇总：https://developer.sophgo.com/thread/473.html
- TDL SDK开发指南：（提供的常用 AI 模型算法，基于 TPU SDK 的应用封装）
 - https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/zh/01.software/TPU/TDL_SDK_Software_Development_Guide/build/TDLSDKSoftwareDevelopmentGuide_zh.pdf
 - https://developer.sophgo.com/thread/556.html
- 如何交叉编译HelloWorld: https://github.com/sipeed/LicheeRV-Nano-Build/blob/v4.1.0/build/boards/cv181x/cv1812cp_licheerv_nano_sd/readme.md#compile-program-use-vendors-toolchain

## buildroot

基于crosstool-ng生成专用的交叉工具链，用在基于主线buildroot的SDK上，在cvi_mmf_sdk上验证好的功能可以移植到这里使用。

源码:

https://github.com/0x754C/sipeed-toolchain

构建环境搭建可以参考repo内的github cicd文件:

https://github.com/0x754C/sipeed-toolchain/blob/master/.github/workflows/licheervnano-host-linux-amd64.yml

## openwrt

TODO

基于主线openwrt，面向将板子当作便携无线AP的用户。

## alpine linux

TODO

基于主线alpine linux,面向在板子上跑distro的用户。

## 引脚复用

这些寄存器的描述可以在芯片手册中找到

提供两种方法修改引脚复用

1. 进入系统后读写/dev/mem修改pinumux:

```
devmem REG_ADDDRESS 32 VALUE
```

2. 在uboot里面修改pinmux:

例如，wifi的pinmux:

https://github.com/sipeed/LicheeRV-Nano-Build/blob/926bbe94f4f00059ce0ff3857cc72a708aa85122/build/boards/cv181x/cv1812cp_licheerv_nano_sd/u-boot/cvi_board_init.c#L52

## 初始化MIPI TX

算能SDK提供两种方式:

1. 在middleware中的用户空间demo中添加屏幕初始化序列.

2. 在uboot中添加屏幕的初始化序列.

## 初始化MIPI RX

算能SDK的MIPI RX只能在用户空间初始化，需要修改middleware中的代码
