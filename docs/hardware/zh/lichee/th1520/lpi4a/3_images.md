---
title: 镜像集合
keywords: Linux, Lichee, TH1520, SBC, RISCV, image
update:
  - date: 2023-05-08
    version: v1.0
    author: wonder
    content:
      - Release docs
---

## 内核支持

目前平头哥官方 SDK 使用 Linux5.10 内核： https://gitee.com/thead-yocto
主线 linux6.x 内核正在移植中，主要社区贡献者：`Jisheng Zhang `

## Sipeed官方镜像

LicheePi 4A 的镜像不定期更新中，初期的镜像可能不太稳定，或者无法发挥 TH1520 的完全性能，请关注本页面，获取最新镜像。
Sipeed 官方镜像基于 Debian 系统修改适配。 

默认镜像有两类帐号密码配置，可以都尝试下：
1. 帐号：`root`，`debian`，`sipeed`；密码均为 `licheepi`
2. 帐号`debian`，密码`debian`；帐号`sipeed`，密码`licheepi`

下载地址：
百度网盘：[点我](https://pan.baidu.com/s/1xH56ZlewB6UOMlke5BrKWQ)
Mega 云盘：[点我](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)
ISCAS 镜像站：[点我](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/)

### Debian

![debian](./assets/images/debian.png)

1. LPi4A_Test_0425
   1. 发布日期：2023年4月25日
   2. 内核：5.10
   3. 根文件系统：ext4, 4.3GB
   4. 主要预装软件包：
      1. 开发类
      2. 办公类
   5. 修复问题：
   6. 已知问题：
      1. 关闭GPU
      2. 安装ibus输入法后会导致GPU开启，复现GPU双缓冲卡顿（终端+图形界面）问题
2. LPI4A-tempfix0428
   1. 发布日期：2023年4月28日
   2. 内核：5.10
   3. 根文件系统：ext4, 4.3GB
   4. 主要预装软件包：TODO
   5. 修复问题：
      1. 临时修复0425版本中终端显示滞后的问题，但是会导致CPU占用率提升，GPU效率减半
   6. 已知问题：
      1. 安装ibus输入法后会导致GPU开启，复现GPU双缓冲卡顿（图形界面）问题

### OpenWRT

![openwrt](./assets/images/openwrt.png)

TODO

### Android

![android](./assets/images/android.png)

TODO

系统安装：提示默认已安装到 eMMC。升级系统的方式（镜像下载，烧录工具，步骤）

## 第三方镜像

这里整理了第三方提供的镜像，仅供用户体验，sipeed 不保证此类镜像的可用性，稳定性。

### openEuler

![openEuler](./assets/images/openEuler.png)   
Download: [Click me](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/lpi4a/)   
Twitter: https://twitter.com/openEuler

### DeepinOS 深度

![deepin](./assets/images/deepin.jpg) 

Readme and image download link: [Click me](https://github.com/aiminickwong/licheepi4a-images)

### openKylin

![openKylin](./assets/images/openkylin.png) 

Readme and image download link: [Click me](https://github.com/aiminickwong/licheepi4a-images)

### armbian

![armbian](https://cdn.armbian.com/wp-content/uploads/2018/03/logo2.png) 

Project address: [Click me](https://github.com/chainsx/armbian-riscv-build)  

### Fedora

![fedora](./assets/images/fedora.png)

Project address: [Click me](https://github.com/chainsx/fedora-riscv-builder)  

### Ubuntu

![ubuntu](./assets/images/ubuntu.png)

### NixOS

![nixos](./assets/images/nixos.png)

### Gentoo

Project address: [Click me](https://wiki.gentoo.org/wiki/Project:RISC-V)

下面链接说明如何从stage3制作一个Gentoo Linux系统

Deplay Gentoo Linux [Click me](https://wiki.gentoo.org/wiki/User:Dlan/RISC-V/TH1520)

![gentoo](./assets/images/gentoo.jpg)

### slarm64

![slarm64](./assets/images/slarm64.png)  
Project address: [Click me](https://gitlab.com/sndwvs/images_build_kit)  
Download: [Click me](https://dl.slarm64.org/slackware/images/lichee_pi_4a/)  