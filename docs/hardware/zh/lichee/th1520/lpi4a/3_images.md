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

默认镜像的帐号密码配置如下：
账户：`debian`，密码： `debian`；
账户： `sipeed`，密码：`licheepi`；
root 账户默认没有设置密码。

### 内存问题修复说明
重要提示：2023.8.1 之前发出的 16GB 内存板存在错误图像，无法正确识别 16GB 内存（运行大型应用程序可能导致系统崩溃），请按照以下说明修复此错误。

请使用下面的命令烧录新的 u-boot 到板子中，16G 内存使用的 u-boot 在[网盘链接](https://pan.baidu.com/s/1xH56ZlewB6UOMlke5BrKWQ)中，也能在[这个链接](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/07_Tools)中下载
相关文件在 `20230803_tempfix.zip` 压缩包中。
（0721及以后版本的镜像内存能正常使用，无需替换为此处的文件）

```shell
sudo ./fastboot flash ram ./images/u-boot-with-spl-lpi4a-16g.bin
sudo ./fastboot reboot
sleep 1
sudo ./fastboot flash uboot ./images/u-boot-with-spl-lpi4a-16g.bin
# 若自己使用的 boot.ext4 中没有 16G ddr 对应的设备树，则需要再烧录 16G ddr 对应的 boot.ext4
sudo ./fastboot flash boot ./images/boot.ext4
```

### Debian

![debian](./assets/images/debian.png)  
![debian_neofetch](./assets/images/debian_neofetch.png)  

下载地址：
百度网盘：[点我](https://pan.baidu.com/s/1xH56ZlewB6UOMlke5BrKWQ)
Mega 云盘：[点我](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)
ISCAS 镜像站：[点我](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/)

1. LPI4A_20230912.zip

   - 发布日期：2023年9月12日
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
         - u-boot 带 16g 后缀的为支持 16g 内存的u-boot，不带后缀的为支持 8g 内存的 u-boot

2. LPI4A_20230912_MIPI.zip

   - 发布日期：2023年9月12日
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
         - u-boot 带 16g 后缀的为支持 16g 内存的u-boot，不带后缀的为支持 8g 内存的 u-boot

### OpenWRT

![openwrt](./assets/images/openwrt.png)

[Click me](https://github.com/ruyisdk/openwrt)

### Android

![android](./assets/images/android.png)

Readme and image download link: [Click me](https://gitee.com/thead-android/thead-android)

预构建镜像下载地址：
百度网盘：[点我](https://pan.baidu.com/s/1xH56ZlewB6UOMlke5BrKWQ)
Mega 云盘：[点我](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)

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

### armbian (official, use RV64GC toolchain)

![armbian](https://cdn.armbian.com/wp-content/uploads/2018/03/logo2.png)

Project address: [Click me](https://github.com/armbian/build)

### armbian (unofficial, use T-Head optimized toolchain)

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

### NixOS (unofficial)

![nixos](./assets/images/nixos.png)

![nixos_neofetch](./assets/images/nixos-licheepi-neofetch.jpg)

Project address: [Click me](https://github.com/ryan4yin/nixos-licheepi4a)

### Gentoo

Project address: [Click me](https://wiki.gentoo.org/wiki/Project:RISC-V)

下面链接说明如何从stage3制作一个Gentoo Linux系统

Deplay Gentoo Linux [Click me](https://wiki.gentoo.org/wiki/User:Dlan/RISC-V/TH1520)

![gentoo](./assets/images/gentoo.jpg)

### slarm64

![slarm64](./assets/images/slarm64.png)  
Project address: [Click me](https://gitlab.com/sndwvs/images_build_kit)  
Download: [Click me](https://dl.slarm64.org/slackware/images/lichee_pi_4a/)  
