---
title: RISC-V Android
keywords: Linux, Lichee, TH1520, SBC, RISCV, Kernel, SDK, Develop
update:
  - date: 2023-07-27
    version: v1.1
    author: ztd
    content:
      - Update English docs
  - date: 2023-05-08
    version: v1.0
    author: wonder
    content:
      - Release docs
---

## Android

[thead-android](https://gitee.com/thead-android/thead-android)

This project is a repository supported by the Android Open Source Project (AOSP), which contains board-level configuration, peripheral HAL layer, kernel, u-boot and pre-compiled component support for the LPi4A board, while the rest of the components can be pulled directly from the upstream AOSP repository.

> Note that the project is still in the early stage, the current AOSP on Licheepi 4A is not stable and the functionality is not yet complete. A stable version with improved functionality will be updated later, so please keep an eye on this document for updates.

### 快速上手

Before downloading the source code of Android open source project , please check your working environment , it is recommended to use a Linux system with at least 250G free disk space , 16GB + RAM (Ubuntu 20.04 or later version is recommended ) of the working environment , compilation time and the number of processor cores of the host computer is related to the host computer , it is recommended to use a host computer with more cores . It is recommended to use a host with more cores. Due to the network, the download time may vary greatly depending on the network conditions, and it is recommended to use a proxy to download the source code.

> The following data is for reference:
> Compiling on a machine with an E5-2699 CPU and 377GB of RAM took about 2 hours (in a docker environment on Ubuntu 22.04). Downloading the source code took about 3 hours.

Download the Android open source project (mainline version) and development board support source code to the working directory, using a fixed version of the upstream code:
```shell
mkdir riscv-android-src && cd riscv-android-src
repo init -u https://gitee.com/thead-android/local_manifests.git -b main_2023_7_7
git clone https://gitee.com/thead-android/local_manifests.git .repo/local_manifests -b thead-android-community
repo sync
```

Using the latest version of the upstream code may cause some compilation issues due to compatibility:
```shell
mkdir riscv-android-src && cd riscv-android-src
repo init -u https://android.googlesource.com/platform/manifest -b master
git clone https://gitee.com/thead-android/local_manifests.git .repo/local_manifests -b thead-android-community
repo sync
```

### Compile Source Code

Once the download is complete, install some of the dependencies that will be used for compilation:
```shell
sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 libncurses5 lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig python3 bc cpio rsync wget
```

The system can then be built with the following commands:
```shell
source build/envsetup.sh
lunch lichee_pi_4a-userdebug
m -j
```

After the compilation is complete, check the generated files:
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

### Burn to LPi4A Development Board

Use fastboot to burn the system image, for adb and fastboot tools use the version downloaded from here:
https://developer.android.com/tools/releases/platform-tools

Copy the files to be burned to the directory where the fastboot utility is located for use by fastboot:
```shell
cp bootpart.ext4 boot.img super.img userdata.img vbmeta.img vbmeta_system.img vendor_boot.img <path_to_fastboot>
```

The development board mainly needs to be connected to the power supply, serial port, USB and display:
The serial port is mainly used for U-boot and kernel command interaction, can be connected through the U0-RX and U0-TX of the GPIO on the board, baud rate is 115200. USB Device interface is mainly used for fastboot and adb tool connection MIPI DSI/HDMI interface can be used to connect the screen to display the UI interface.

To fully burn the system, you need to press and hold the boot button of the development board and press the reset button to enter the boot burning mode. Use the just downloaded fastboot to burn:
```shell
# burn uboot and initialize boot environment variables
fastboot flash ram u-boot-with-spl.bin
fastboot reboot
fastboot flash uboot u-boot-with-spl.bin

#Burn individual partitions
#In non-boot burn mode, you can burn the partitions individually by typing the command fastboot usb 0 at uboot's command line
fastboot flash bootpart bootpart.ext4
fastboot flash boot boot.img
fastboot flash vendor_boot vendor_boot.img
fastboot flash super super.img 
fastboot flash userdata userdata.img
fastboot flash vbmeta vbmeta.img
fastboot flash vbmeta_system vbmeta_system.img

# Initialize metadata and misc partitions
fastboot erase metadata 
fastboot erase misc
```

A typical burn log is shown below:
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

When the completion of the burn-in reset power into the system boot mode, you can access the command line of the system through the serial port / ADB, and can interact with the touch screen or external HDMI display system image interface:

![licheepi4a_aosp](./assets/develop_android/licheepi4a_aosp.png)

### Common Problems

When compiling with the docker environment, you may encounter the following error:
```shell
Build sandboxing disabled due to nsjail error. 
```
This error can be ignored for now, and will not affect later compilation steps. If you want to run nsjail, try upgrading the kernel version to 5.XX or pass in these parameters when you start the docker `--security-opt apparmor=unconfined --security-opt seccomp=unconfined --security-opt systempaths=unconfined` or `--privileged`.