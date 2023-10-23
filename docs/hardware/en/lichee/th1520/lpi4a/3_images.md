---
title: Collection of images
keywords: Linux, Lichee, TH1520, SBC, RISCV, image
update:
  - date: 2023-10-23
    version: v1.2
    author: ztd
    content: 
      - Update image info and upload new images
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

There may be problems with the memory identification of some 16G memory core boards, which may cause the system to crash when the memory usage is high.

The default image's account and password configurations is:
User: `debian`，password: `debian`;
User: `sipeed`，password: `licheepi`;
root has no password by default.

### Memory Problem Repair Instructions
IMPORTANT：16GB memory board sendout before 2023.8.1 have a buggy images that can't correctly recognize 16GB memory (occupy errors running big applications), please follow the next instructions to fix this error.

Please use the following command to burn a new u-boot to the board. The u-boot used by 16G memory is in the [Mega Cloud Storage link]( https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA), and can also be downloaded from [this link](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/07_Tools)
The relevant files are in the `20230803_tempfix.zip` compressed package.
(images of 0721 and later versions can be used normally, no need to replace it with the file here)

```shell
sudo ./fastboot flash ram ./images/u-boot-with-spl-lpi4a-16g.bin
sudo ./fastboot reboot
sleep 1
sudo ./fastboot flash ram ./images/u-boot-with-spl-lpi4a-16g.bin
# If there is no device tree corresponding to 16G ddr in the boot.ext4 you use, you need to burn the boot.ext4 corresponding to 16G ddr
sudo ./fastboot flash boot ./images/boot.ext4
```

### Debian

![debian](./../../../../zh/lichee/th1520/lpi4a/assets/images/debian.png)
![debian_neofetch](./../../../../zh/lichee/th1520/lpi4a/assets/images/debian_neofetch.png)

Download Links:

Mega Cloud Storage：[click me](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)
ISCAS mirror(including test mirror, ordinary users please use the mirror in the previous network disk): [click me](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/)

1. LPI4A_20231023_BASIC.zip

- Release Date: October 23, 2023
- Kernel: 5.10
- Root Filesystem: ext4, 4.3GB  
- Preinstalled Software Packages:
  - Development: python3.11
  - Office: libreoffice suite 
  - Browser: chromium
  - Media: 4K video players like Parole, VLC, GIMP
- Bug Fixes:
  - HDMI display and audio device recognition issue (20230706) 
  - Bluetooth issues fixed, Bluetooth devices working normally now, Bluetooth headphones can play audio now (20230706)
  - Fixed browser shortcut issue in bottom launch bar, can launch chromium now (20230706)
  - Fixed kernel panic issue when using USB camera for long time (20230706) 
  - Fixed 16GB memory recognition issue, please update to identify full 16GB memory (20230721)
  - Fixed HDMI audio quality issue in chromium (20230912)
  - Fixed font pixel missing issue in dual screen mode (20230912)
  - Fixed inaccurate mouse cursor issue (20231023)
  - Fixed NPU driver kernel and user version mismatch (20231023)
  - Fixed issue burning rootfs over 4GB (20231023)
- Usage Instructions:
  - Auto login enabled, default login user is sipeed
  - Sudo without password enabled
  - NPU drivers loaded automatically, no manual initialization needed
  - Supports both HDMI and MIPI display, switch in boot menu
    - Boot menu config at /boot/extlinux/extlinux.conf in boot.ext4. 3 options, distinguished by suffix:
       - Suffix (HDMI only) - HDMI only
       - Suffix (HDMI and MIPI) - Dual display
       - Suffix (rescue target) - Recovery
    - Default is HDMI only. Two ways to switch to MIPI:  
       1. Connect serial tool, press 2 to choose MIPI display when boot menu appears, one time only
       2. Edit extlinux.conf, change default l0 to default l1 to change default to MIPI
  - The zip contains two u-boot, note the suffix and device parameters when burning
     - u-boot with 16g suffix is for 16GB memory, no suffix is for 8GB memory
- Known Issues:
  - MIPI screen brightness can only be adjusted manually now
     - Switch to root, run `echo brightness_value(0-7) > /sys/class/backlight/pwm-backlight@0/brightness`

2. LPI4A_20231023_FULL.zip

- Release Date: October 23, 2023  
- Kernel: 5.10
- Root Filesystem: ext4, 9.7GB
- Preinstalled Software Packages:
  - Development: python3.11, GCC, VScode, Kicad (with demo projects), AI env (with precompiled yolov5n/yolov5s executables)
  - Office: libreoffice suite
  - Browser: chromium 
  - Media: 4K video players like Parole (with demo 4K videos), VLC, GIMP, video editor Kdenlive (with demo video clips), kodi
  - Game: SuperTuxKart
  - Other: btop, neofetch
- Bug Fixes:
  - HDMI display and audio device recognition issue (20230706)
  - Bluetooth issues fixed, Bluetooth devices working normally now, Bluetooth headphones can play audio now (20230706) 
  - Fixed browser shortcut issue in bottom launch bar, can launch chromium now (20230706)
  - Fixed kernel panic issue when using USB camera for long time (20230706)
  - Fixed 16GB memory recognition issue, please update to identify full 16GB memory (20230721) 
  - Fixed HDMI audio quality issue in chromium (20230912)
  - Fixed font pixel missing issue in dual screen mode (20230912)
  - Fixed inaccurate mouse cursor issue (20231023) 
  - Fixed NPU driver kernel and user version mismatch (20231023)
  - Fixed issue burning rootfs over 4G (20231023)
- Usage Instructions: 
  - Auto login enabled, default login user is sipeed
  - Sudo without password enabled
  - NPU drivers loaded automatically, no manual initialization needed
  - Supports both HDMI and MIPI display, switch in boot menu
     - Boot menu config at /boot/extlinux/extlinux.conf in boot.ext4. 3 options, distinguished by suffix:
        - Suffix (HDMI only) - HDMI only  
        - Suffix (HDMI and MIPI) - Dual display
        - Suffix (rescue target) - Recovery 
     - Default is HDMI only. Two ways to switch to MIPI:
        1. Connect serial tool, press 2 to choose MIPI display when boot menu appears, one time only
        2. Edit extlinux.conf, change default l0 to default l1 to change default to MIPI
  - The zip contains two u-boot, note the suffix and device parameters when burning
     - u-boot with 16g suffix is for 16GB memory, no suffix is for 8GB memory
- Known Issues:
  - MIPI screen brightness can only be adjusted manually now
     - Switch to root, run `echo brightness_value(0-7) > /sys/class/backlight/pwm-backlight@0/brightness`

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

[Click me](https://github.com/ruyisdk/openwrt)

### Android

![android](./../../../../zh/lichee/th1520/lpi4a/assets/images/android.png)
Readme and image download link: [Click me](https://gitee.com/thead-android/thead-android)

Prebuild Image Download Links:

Mega Cloud Storage：[click me](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)

> The Android 13 SDK is still in its infancy, and the problems will be gradually fixed

The precompiled image file of Android 13 is provided in the network disk download link of Sipeed official image, and the burning method after downloading is as follows. Please use the version downloaded from here for the fastboot tool:
https://developer.android.com/tools/releases/platform-tools

There are also fastboot files in the network disk.

```shell
#Burn uboot and initialize boot environment variables
fastboot flash ram u-boot-with-spl.bin
fastboot reboot
fastboot flash uboot u-boot-with-spl.bin

#Burn all partitions
#In the non-boot burning mode, you can enter the command fastboot usb 0 in the uboot command line to burn the partition separately
fastboot flash bootpart bootpart.ext4
fastboot flash boot boot.img
fastboot flash vendor_boot vendor_boot.img
fastboot flash super super.img
fastboot flash userdata userdata.img
fastboot flash vbmeta vbmeta.img
fastboot flash vbmeta_system vbmeta_system.img

#Initialize metadata and misc partition
fastboot erase metadata
fastboot erase misc
```

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

### NixOS (unofficial)


![nixos](./../../../../zh/lichee/th1520/lpi4a/assets/images/nixos.png)

![nixos_neofetch](./../../../../zh/lichee/th1520/lpi4a/assets/images/nixos-licheepi-neofetch.jpg)

Project address: [Click me](https://github.com/ryan4yin/nixos-licheepi4a)

### Gentoo

Project address: [Click me](https://wiki.gentoo.org/wiki/Project:RISC-V)

The link below shows how to create a Gentoo Linux system from stage3

Deplay Gentoo Linux [Click me](https://wiki.gentoo.org/wiki/User:Dlan/RISC-V/TH1520)

![gentoo](./../../../../zh/lichee/th1520/lpi4a/assets/images/gentoo.jpg)

### slarm64

![slarm64](./../../../../zh/lichee/th1520/lpi4a/assets/images/slarm64.png)  
Project address: [Click me](https://gitlab.com/sndwvs/images_build_kit)  
Download: [Click me](https://dl.slarm64.org/slackware/images/lichee_pi_4a/)  
