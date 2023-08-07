---
title: 镜像集合
keywords: Linux, Lichee, TH1520, SBC, RISCV, image
update:
  - date: 2023-07-14
    version: v1.1
    author: ztd
    content: 
      - Update docs
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
![debian_neofetch](./assets/images/debian_neofetch.png)  

1. LPI4A_20230721.zip

   - 发布日期：2023年7月21日
   - 内核：5.10
   - 根文件系统：ext4, 4.3GB
   - 主要预装软件包：
      - 开发类
      - 办公类
   - 修复问题：
      - HDMI 显示设备和 HDMI 音频设备识别问题
      - 修复蓝牙问题，现在蓝牙设备功能正常，蓝牙耳机也能正常播放音频
      - 添加自动登录，免密码 sudo 功能
      - 修复桌面底部启动栏浏览器快捷方式不可用的问题，现在能点击这里进入 chromium
      - 修复在长时间连接 USB 摄像头情况下，会导致 kernel panic 的问题
      - 修复16GB内存识别问题，需完全识别16GB内存请更新此镜像
   - 已知问题：
      - HDMI 音频在 chromium 下播放音质有问题
   - 使用说明：
      - 该压缩包为仅支持 HDMI 显示，烧录时请注意文件名中的后缀和设备相关参数对应
         - boot，u-boot 文件名中的 8gddr/16gddr 分别对应 8g/16g 内存

2. LPI4A_20230721_mipi.zip

   - 发布日期：2023年7月21日
   - 内核：5.10
   - 根文件系统：ext4, 4.3GB
   - 主要预装软件包：
      - 开发类
      - 办公类
   - 修复问题：
      - HDMI 显示设备和 HDMI 音频设备识别问题
      - 修复蓝牙问题，现在蓝牙设备功能正常，蓝牙耳机也能正常播放音频
      - 添加自动登录，免密码 sudo 功能
      - 修复桌面底部启动栏浏览器快捷方式不可用的问题，现在能点击这里进入 chromium
      - 修复在长时间连接 USB 摄像头情况下，可能会导致 kernel panic 的问题
      - 修复16GB内存识别问题，需完全识别16GB内存请更新此镜像
   - 已知问题：
      - 双屏异显下，MIPI 屏幕作扩展显示器时分辨率较低，导致字体有些模糊
      - 在没连接 MIPI 屏幕时，系统仍会识别为连接，暂时需要在设置中手动关闭 MIPI 屏幕的输出
         - 切换为 root 用户，执行`echo off > /sys/class/drm/card0-DSI-1/status`
      - MIPI 屏幕暂时只能通过手动写值调节亮度
         - 切换为 root 用户，执行`echo 亮度值(0-7的整数值) > /sys/class/backlight/pwm-backlight@0/brightness`
      - HDMI 音频在 chromium 下播放音质有问题
   - 使用说明：
      - 该压缩包为支持 MIPI 屏幕的镜像，烧录时请注意文件名中的后缀和设备相关参数对应
         - boot，u-boot 文件名中的 8gddr/16gddr 分别对应 8g/16g 内存
         - boot 文件名中的 mipi_720p/mipi_1080p 分别对应800x1280的 MIPI 屏幕（带触摸）/1200x1920的mipi屏幕

### OpenWRT

![openwrt](./assets/images/openwrt.png)

TODO

### Android

![android](./assets/images/android.png)

Readme and image download link: [Click me](https://gitee.com/thead-android/thead-android)

> 安卓13 SDK 仍处于初期状态，会逐步修复其中的问题

Sipeed 官方镜像的网盘下载链接中提供了 Android 13的预编译镜像文件，下载后烧录方式如下，fastboot工具请使用从这里下载的版本：
https://developer.android.com/tools/releases/platform-tools

网盘中也有提供 fastboot 的文件

```shell
#烧录uboot并初始化boot环境变量
fastboot flash ram u-boot-with-spl.bin
fastboot reboot
fastboot flash uboot u-boot-with-spl.bin

#烧录各个分区
#在非boot烧写模式，可以在uboot的命令行中输入命令fastboot usb 0，单独烧录分区
fastboot flash bootpart bootpart.ext4
fastboot flash boot boot.img
fastboot flash vendor_boot vendor_boot.img
fastboot flash super super.img 
fastboot flash userdata userdata.img
fastboot flash vbmeta vbmeta.img
fastboot flash vbmeta_system vbmeta_system.img

#初始化metadata和misc分区
fastboot erase metadata 
fastboot erase misc
```

## 第三方镜像

这里整理了第三方提供的镜像，仅供用户体验，sipeed 不保证此类镜像的可用性，稳定性。

### openEuler

![openEuler](./assets/images/openEuler.png)   
![openeuler_neofetch](./assets/images/openeuler_neofetch.png)  

Download: [Click me](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/lpi4a/)   
Twitter: https://twitter.com/openEuler

### DeepinOS 深度

![deepin](./assets/images/deepin.jpg)   
![deepin_neofetch](./assets/images/deepin_neofetch.png)  

Readme and image download link: [Click me](https://github.com/aiminickwong/licheepi4a-images)

### openKylin

![openKylin](./assets/images/openkylin.png)
![oepnkylin_neofetch](./assets/images/oepnkylin_neofetch.png)

Readme link: [Click me](https://github.com/aiminickwong/licheepi4a-images)
[openKylin V1.0 Download address](https://www.openkylin.top/downloads/index-cn.html)

### armbian (unofficial)

![armbian](https://cdn.armbian.com/wp-content/uploads/2018/03/logo2.png)
![armbian_neofetch](./assets/images/armbian_neofetch.png)

Project address: [Click me](https://github.com/chainsx/armbian-riscv-build)

### Fedora (unofficial)

![fedora](./assets/images/fedora.png)
![fedora_neofetch](./assets/images/fedora_neofetch.png)

Project address: [Click me](https://github.com/chainsx/fedora-riscv-builder)

### OpenWrt (unofficial)

![openwrt](./assets/images/openwrt.png)
![openwrt_unofficial](./assets/images/openwrt_unofficial.png)

Project address: [Click me](https://github.com/chainsx/openwrt-th1520)

### Ubuntu

![ubuntu](./assets/images/ubuntu.png)

![ubuntu_neofetch](./assets/images/ubuntu_neofetch.jpg)

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
