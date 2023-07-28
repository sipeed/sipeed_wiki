---
title: Collection of images
keywords: Linux, Lichee, TH1520, SBC, RISCV, image
update:
  - date: 2023-07-19
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

## Supported kernels

Currently T-Heads SDK uses Linux Kernel 5.10: https://gitee.com/thead-yocto
Support is currently added to Linux 6.x, the main contributor of this is `Jisheng Zhang `

## Official Sipeed image

The image for the LicheePi 4A is updated irregularly. The initial image may not be stable, or it may not be able to fully utilize the performance of the TH1520. Please follow the steps below to get the latest image.
The official Sipeed image is based on an adapted Debian.

The default image has two types of account and password configurations, you can try both:
1. User：`root`，`debian`，`sipeed`； the password for all accounts is `licheepi`
2. User: `debian`，password: `debian`； user: `sipeed`，password: `licheepi`

Download Links:

Mega Cloud Storage：[click me](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)
ISCAS mirror: [click me](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/)

### Debian

![debian](./../../../../zh/lichee/th1520/lpi4a/assets/images/debian.png)
![debian_neofetch](./../../../../zh/lichee/th1520/lpi4a/assets/images/debian_neofetch.png)

1. LPI4A_20230721.zip

    - Release date: July 21, 2023
    - Kernel: 5.10
    - Root file system: ext4, 4.3GB
    - Main pre-installed packages:
       - Development
       - Office
    - Fixed issues:
       - HDMI display device and HDMI audio device recognition issues
       - Fix bluetooth issue, now bluetooth devices function normally, and bluetooth headsets can also play audio normally
       - Add auto-login, password-free sudo functionality
       - Fixed the problem that the browser shortcut in the launch bar at the bottom of the desktop is not available, now you can click here to enter chromium
       - Fix the problem that the kernel panic will occur when the USB camera is connected for a long time
       - Fix 16GB memory recognition problem, please update this image if you need to fully recognize 16GB memory
    - Known issues:
       - There is a problem with the sound quality of HDMI audio playing under chromium
    - Instructions for use:
       - This zip file only supports HDMI display, when burning, please note that the suffix in the file name corresponds to the relevant parameters of the device.
         - boot, 8gddr/16gddr in the u-boot file name corresponds to 8g/16g memory respectively.

2. LPI4A_20230721_mipi.zip

    - Release date: July 21, 2023
    - Kernel: 5.10
    - Root file system: ext4, 4.3GB
    - Main pre-installed packages:
       - Development
       - Office
    - Fixed issues:
       - HDMI display device and HDMI audio device recognition issues
       - Fix bluetooth issue, now bluetooth devices function normally, and bluetooth headsets can also play audio normally
       - Add auto-login, password-free sudo functionality
       - Fixed the problem that the browser shortcut in the launch bar at the bottom of the desktop is not available, now you can click here to enter chromium
       - Fixed a problem that may cause a kernel panic when the USB camera is connected for a long time
       - Fix 16GB memory recognition problem, please update this image if you need to fully recognize 16GB memory
    - Known issues:
       - Under dual-screen different display, when the MIPI screen is used as an extended display, the resolution is low, resulting in some blurred fonts
       - When the MIPI screen is not connected, the system will still recognize it as connected, temporarily need to manually turn off the output of the MIPI screen in the settings
          - Switch to root user, execute `echo off > /sys/class/drm/card0-DSI-1/status`
       - For the time being, the brightness of the MIPI screen can only be adjusted by manually writing a value
          - Switch to root user, execute `echo brightness value (integer value from 0-7) > /sys/class/backlight/pwm-backlight@0/brightness`
       - There is a problem with the sound quality of HDMI audio playing under chromium
    - Instructions for use:
      - This zip file is the image of the MIPI screen, please note that the suffix in the file name corresponds to the relevant parameters of the device when burning.
         - 8gddr/16gddr in the boot and u-boot file names correspond to 8g/16g memory respectively.
         - mipi_720p/mipi_1080p in the boot file name corresponds to 800x1280 MIPI screen (with touch)/1200x1920 mipi screen respectively.

<!-- 1. LPi4A_Test_0425
   1. Release date: April 25, 2023
   2. Linux Kernel version: 5.10
   3. rootfs: ext4, 4.3GB
   4. Pre-Installed packages:
      1. Development utilities
      2. Office suite
   5. Fixed issues:
   6. Known problems：
      1. GPU sometimes turns off
      2. After installing the ibus input method, the GPU will be turned on, and the problem of GPU double-buffering (terminal + graphical interface) will be reproduced.
2. LPI4A-tempfix0428
   1. Release date: April 28, 2023
   2. Linux Kernel version: 5.10
   3. rootfs: ext4, 4.3GB
   4. Pre-Installed packages: TODO
   5. Fixed issues:
      1. Temporarily fix the problem of terminal display lag in version 0425, but it will increase CPU usage and halve GPU efficiency
   6. Known issues:
      1. After installing the ibus input method, the GPU will be turned on, and the problem of GPU double-buffering (graphical interface) will be reproduced. -->

### OpenWRT

![openwrt](./../../../../zh/lichee/th1520/lpi4a/assets/images/openwrt.png)

TODO

### Android

![android](./../../../../zh/lichee/th1520/lpi4a/assets/images/android.png)
Readme and image download link: [Click me](https://gitee.com/thead-android/thead-android)

## Third-party images

The images provided by third parties are listed here for informational purposes only. Sipeed does not guarantee the availability and stability of these images.

### openEuler

![openEuler](./../../../../zh/lichee/th1520/lpi4a/assets/images/openEuler.png)
![openeuler_neofetch](./../../../../zh/lichee/th1520/lpi4a/assets/images/openeuler_neofetch.png)
Download: [Click me](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/lpi4a/)   
Twitter: https://twitter.com/openEuler   

### DeepinOS

![deepin](./../../../../zh/lichee/th1520/lpi4a/assets/images/deepin.jpg) 
![deepin_neofetch](./../../../../zh/lichee/th1520/lpi4a/assets/images/deepin_neofetch.png)

Readme and image download address: [Link](https://github.com/aiminickwong/licheepi4a-images)

### openKylin

![openKylin](./../../../../zh/lichee/th1520/lpi4a/assets/images/openkylin.png)
![oepnkylin_neofetch](./../../../../zh/lichee/th1520/lpi4a/assets/images/oepnkylin_neofetch.png) 

Readme link: [Click me](https://github.com/aiminickwong/licheepi4a-images)
[openKylin V1.0 Download address](https://www.openkylin.top/downloads/index-cn.html)

### armbian

![armbian](https://cdn.armbian.com/wp-content/uploads/2018/03/logo2.png)     
Project address: [Click me](https://github.com/chainsx/armbian-riscv-build)  

### Fedora

![fedora](./../../../../zh/lichee/th1520/lpi4a/assets/images/fedora.png)

Project address: [Click me](https://github.com/chainsx/fedora-riscv-builder)  

### Ubuntu

![ubuntu](./../../../../zh/lichee/th1520/lpi4a/assets/images/ubuntu.png)

![ubuntu_neofetch](./../../../../zh/lichee/th1520/lpi4a/assets/images/ubuntu_neofetch.jpg)

### NixOS

![nixos](./../../../../zh/lichee/th1520/lpi4a/assets/images/nixos.png)

### Gentoo

Project address: [Click me](https://wiki.gentoo.org/wiki/Project:RISC-V)

The link below shows how to create a Gentoo Linux system from stage3

Deplay Gentoo Linux [Click me](https://wiki.gentoo.org/wiki/User:Dlan/RISC-V/TH1520)

![gentoo](./../../../../zh/lichee/th1520/lpi4a/assets/images/gentoo.jpg)

### slarm64

![slarm64](./../../../../zh/lichee/th1520/lpi4a/assets/images/slarm64.png)  
Project address: [Click me](https://gitlab.com/sndwvs/images_build_kit)  
Download: [Click me](https://dl.slarm64.org/slackware/images/lichee_pi_4a/)  