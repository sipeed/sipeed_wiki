---
title: RISC-V Android
keywords: Linux, Lichee, TH1520, SBC, RISCV, Kernel, SDK, Develop
update:
  - date: 2023-07-27
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

## Android

[项目地址](https://gitee.com/thead-android/thead-android)

本项目为安卓开源项目(AOSP)支持的仓库，其中包含了 LPi4A 发板的板级配置、外设HAL 层、内核、u-boot 和预编译组件支持，其余组件则可直接从上游 AOSP 仓库拉取。

> 注意，该项目尚处于初期阶段，目前的 AOSP 在 Licheepi 4A 上运行并不稳定，且功能还未完善。后续会更新功能完善的稳定版，请关注该文档的更新。

### 快速上手

在下载安卓开源项目源代码之前，请检查您的工作环境，建议使用具有至少 250G 空闲磁盘空间、16GB+ 内存的 Linux 系统(推荐使用 Ubuntu 20.04 以上版本)的工作环境， 编译时间和主机的处理器核心数有关，建议使用有较多核心的主机。且由于网络原因，下载时间根据网络情况会有很大差别，推荐使用代理下载源码。

> 以下数据供参考：
> 使用 E5-2699 CPU，内存 377GB 的机器编译，编译时间约为2小时（在Ubuntu22.04的docker环境下）。下载源码的时间约为3小时。

将安卓开源项目(主线版本)和开发板支持源代码下载到工作目录,使用固定版本上游代码:
```shell
mkdir riscv-android-src && cd riscv-android-src
repo init -u https://gitee.com/thead-android/local_manifests.git -b main_2023_7_7
git clone https://gitee.com/thead-android/local_manifests.git .repo/local_manifests -b thead-android-community
repo sync
```

使用最新版本上游代码，可能会由于兼容性导致一些编译问题:
```shell
mkdir riscv-android-src && cd riscv-android-src
repo init -u https://android.googlesource.com/platform/manifest -b master
git clone https://gitee.com/thead-android/local_manifests.git .repo/local_manifests -b thead-android-community
repo sync
```

### 编译源码

下载完成后，先安装一些编译会用到的依赖：
```shell
sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 libncurses5 lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig python3 bc cpio rsync wget
```

然后可以通过以下命令对系统进行构建：
```shell
source build/envsetup.sh
lunch lichee_pi_4a-userdebug
m -j
```

编译完成后，检查生成的文件：
```shell
$ ls out/target/product/lichee_pi_4a/*img
out/target/product/lichee_pi_4a/boot.img           
out/target/product/lichee_pi_4a/super_empty.img        
out/target/product/lichee_pi_4a/vendor_boot-debug.img
out/target/product/lichee_pi_4a/cache.img          
out/target/product/lichee_pi_4a/system.img             
out/target/product/lichee_pi_4a/vendor_boot-test-harness.img
out/target/product/lichee_pi_4a/dtb.img            
out/target/product/lichee_pi_4a/system_ext.img         
out/target/product/lichee_pi_4a/vendor_boot.img
out/target/product/lichee_pi_4a/dtbo-unsigned.img  
out/target/product/lichee_pi_4a/userdata.img           
out/target/product/lichee_pi_4a/vendor_ramdisk-debug.img
out/target/product/lichee_pi_4a/dtbo.img           
out/target/product/lichee_pi_4a/vbmeta.img             
out/target/product/lichee_pi_4a/vendor_ramdisk-test-harness.img
out/target/product/lichee_pi_4a/product.img        
out/target/product/lichee_pi_4a/vbmeta_system.img      
out/target/product/lichee_pi_4a/vendor_ramdisk.img
out/target/product/lichee_pi_4a/ramdisk.img        
out/target/product/lichee_pi_4a/vendor-bootconfig.img
out/target/product/lichee_pi_4a/super.img          
out/target/product/lichee_pi_4a/vendor.img
```

### 烧录至 LPi4A 开发板

使用fastboot对系统镜像进行烧写，adb和fastboot工具请使用从这里下载的版本：
https://developer.android.com/tools/releases/platform-tools

将需要烧录的文件拷贝到 fastboot 工具所在目录下，供fastboot使用：
```shell
cp bootpart.ext4 boot.img super.img userdata.img vbmeta.img vbmeta_system.img vendor_boot.img <path_to_fastboot>
```

开发板使用主要需要连接电源、串口、USB 和显示：
串口主要用于 U-boot 和内核中的命令交互，可通过底板上 GPIO 的 U0-RX 和 U0-TX 连接，波特率为115200。USB Device 接口主要用于fastboot和adb工具的连接 MIPI DSI/HDMI 接口可以使用于连接屏幕显示 UI 界面。

对系统进行完整烧写需要按住开发板的boot按键同时按复位键进入boot烧写模式。使用刚刚下载下来的 fastboot 烧写：
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

典型烧录 log 如下：
```shell
< waiting for any device >
Sending 'ram' (982 KB)                             OKAY [  0.261s]
Writing 'ram'                                      OKAY [  0.002s]
Finished. Total time: 0.268s
Rebooting                                          OKAY [  0.001s]
Finished. Total time: 0.402s
< waiting for any device >
Sending 'uboot' (982 KB)                           OKAY [  0.044s]
Writing 'uboot'                                    OKAY [  0.077s]
Finished. Total time: 0.158s
Sending 'bootpart' (8192 KB)                       OKAY [  0.217s]
Writing 'bootpart'                                 OKAY [  0.071s]
Finished. Total time: 0.316s
Warning: skip copying boot_a image avb footer (boot_a partition size: 65536, boot_a image size: 33554432).
Sending 'boot_a' (32768 KB)                        OKAY [  0.825s]
Writing 'boot_a'                                   OKAY [  0.255s]
Finished. Total time: 1.116s
Sending 'vendor_boot_a' (32768 KB)                 OKAY [  0.824s]
Writing 'vendor_boot_a'                            OKAY [  0.254s]
Finished. Total time: 1.107s
Sending sparse 'super' 1/9 (114684 KB)             OKAY [  2.872s]
Writing 'super'                                    OKAY [  0.855s]
Sending sparse 'super' 2/9 (114336 KB)             OKAY [  2.849s]
Writing 'super'                                    OKAY [  0.880s]
Sending sparse 'super' 3/9 (114684 KB)             OKAY [  2.947s]
Writing 'super'                                    OKAY [  0.857s]
Sending sparse 'super' 4/9 (114684 KB)             OKAY [  2.921s]
Writing 'super'                                    OKAY [  0.862s]
Sending sparse 'super' 5/9 (114684 KB)             OKAY [  2.875s]
Writing 'super'                                    OKAY [  0.904s]
Sending sparse 'super' 6/9 (110208 KB)             OKAY [  2.794s]
Writing 'super'                                    OKAY [  0.859s]
Sending sparse 'super' 7/9 (106652 KB)             OKAY [  2.679s]
Writing 'super'                                    OKAY [  0.853s]
Sending sparse 'super' 8/9 (109509 KB)             OKAY [  2.754s]
Writing 'super'                                    OKAY [  2.400s]
Sending sparse 'super' 9/9 (88872 KB)              OKAY [  2.251s]
Writing 'super'                                    OKAY [  0.707s]
Finished. Total time: 34.231s
Sending 'userdata' (2652 KB)                       OKAY [  0.085s]
Writing 'userdata'                                 OKAY [  0.581s]
Finished. Total time: 0.706s
Sending 'vbmeta_a' (8 KB)                          OKAY [  0.019s]
Writing 'vbmeta_a'                                 OKAY [  0.021s]
Finished. Total time: 0.078s
Sending 'vbmeta_system_a' (4 KB)                   OKAY [  0.019s]
Writing 'vbmeta_system_a'                          OKAY [  0.023s]
Finished. Total time: 0.079s
Erasing 'metadata'                                 OKAY [  0.087s]
Finished. Total time: 0.132s
Erasing 'misc'                                     OKAY [  0.029s]
Finished. Total time: 0.071s
```

当完成烧写后重新复位上电进入系统启动模式,可以通过串口/ADB访问系统的命令行，并可通过触屏或外接HDMI显示系统图像界面进行交互：

![licheepi4a_aosp](./assets/develop_android/licheepi4a_aosp.png)

### 常见问题

下载源码时，若运行 `repo init -u https://gitee.com/thead-android/local_manifests.git -b main_2023_7_7` 命令始终不成功，可以尝试运行以下命令后，再进行 repo init ：
```shell
export REPO_URL='https://mirrors.tuna.tsinghua.edu.cn/git/git-repo/'
```

使用 docker 环境编译时，可能会遇到如下报错：
```shell
Build sandboxing disabled due to nsjail error. 
```
这个报错可以暂时忽略，不影响后面的编译步骤。若想运行 nsjail，可以尝试升级内核版本至5.XX或者启动 docker 时传入这些参数 `--security-opt apparmor=unconfined --security-opt seccomp=unconfined --security-opt systempaths=unconfined` 或 `--privileged`。