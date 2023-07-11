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

1. LPI4A_20230706.zip
   - 发布日期：2023年7月6日
   - 内核：5.10
   - 根文件系统：ext4, 4.3GB
   - 主要预装软件包：
      - 开发类
      - 办公类
   - 修复问题：
      - HDMI显示设备和HDMI音频设备识别问题
      - 修复蓝牙问题，现在蓝牙设备功能正常
   - 已知问题：
   - 使用说明：
      - 该压缩包为仅支持HDMI显示，烧录时请注意boot的后缀和设备对应
         - 8gddr/16gddr分别对应8g/16g内存

2. LPI4A_20230706_mipi.zip
   - 发布日期：2023年7月6日
   - 内核：5.10
   - 根文件系统：ext4, 4.3GB
   - 主要预装软件包：
      - 开发类
      - 办公类
   - 修复问题：
      - HDMI显示设备和HDMI音频设备识别问题
      - 修复蓝牙问题，现在蓝牙设备功能正常
   - 已知问题：
      - 双屏异显下，mipi屏幕作扩展显示器时分辨率较低，导致字体有些模糊
      - 触摸屏横屏显示时坐标不准
   - 使用说明：
      - 该压缩包为支持mipi屏幕的镜像，烧录时请注意boot的后缀和设备对应
         - 8gddr/16gddr分别对应8g/16g内存
         - mipi_720p/mipi_1080p分别对应800x1280的mipi屏幕（带触摸）/1200x1920的mipi屏幕

### OpenWRT

![openwrt](./assets/images/openwrt.png)

TODO

### Android

![android](./assets/images/android.png)

TODO


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
