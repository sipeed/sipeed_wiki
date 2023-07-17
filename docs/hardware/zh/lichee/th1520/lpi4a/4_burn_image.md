---
title: 烧录镜像
keywords: Linux, Lichee, TH1520, SBC, RISCV, image
update:
  - date: 2023-05-08
    version: v1.0
    author: wonder
    content:
      - Release docs
---

## 准备工作

### 获取镜像

参见上一章“镜像集合”，选取需要的镜像下载。
以下的烧录方式以 Debian 镜像 `LPi4A_Test_0425.7z` 为例。

### 获取烧录工具

在镜像集合的网盘内可以获得 `burn_tool.zip`, 解压可得 win/linux/mac 三个系统下的 fastboot 烧录工具。

## 进入烧录模式

注意不同版本硬件进入烧录模式的方式略有不同，参见以下章节。

### 内测版硬件

按住板上的BOOT按键不放，然后插入 USB-C 线缆上电（线缆另一头接 PC ），即可进入 USB 烧录模式。
![press_boot](./assets/burn_image/press_boot.png)

在 Windows 下使用设备管理器查看，会出现 “USB download gadget” 设备。

在 Linux 下，使用 `lsusb` 查看设备，会显示以下设备： `ID 2345:7654 T-HEAD USB download gadget`

### 正式版硬件

TODO

### Windows 下驱动安装

Windows 下烧录时，需要先进入高级启动模式，禁用数字签名。才能正常安装下面的驱动。

![before_install_driver](./assets/burn_image/before_install_driver.png)
![install_driver](./assets/burn_image/install_driver.png)

## 烧录镜像

进入烧录模式后，可使用 burn_tool.zip 内的 fastboot 进行烧录操作，注意可能需要先赋予 fastboot 可执行权限。

### Windows 系统步骤

编辑 burn_tool.zip 文件夹里面的 `burn_lpi4a.bat` 文件，将对应的镜像路径更改成自己实际使用的镜像及名称。然后双击运行 `burn_lpi4a.bat` 就能够正常进行烧录了。

需要注意的是 `fastboot.exe` 的路径也需要匹配上，不然会被提示找不到文件。

![target_burn_image_path](./assets/burn_image/target_burn_image_path.png)

### Linux 系统步骤

在按住BOOT按键的条件下，系统在reset启动后，会默认进入fastboot模式，
这时侯我们可以通过fastboot下载并启动u-boot镜像的命令，来进入到u-boot的fastboot烧录模式（相比Brom阶段，会有更大下载buffer，速度会更快）
下面的指令会检查并格式化分区，请务必执行，否则后面烧录 rootfs 会很慢。

```bash
sudo ./fastboot flash ram ./images/u-boot-with-spl.bin
sudo ./fastboot reboot
sleep 1
```

分别烧录下面三个镜像：启动引导镜像-uboot，启动分区-boot，操作系统根分区-root
```bash
sudo ./fastboot flash uboot ./images/u-boot-with-spl.bin
sudo ./fastboot flash boot ./images/boot.ext4
sudo ./fastboot flash root ./images/rootfs.ext4
```

`boot.ext4` 为 boot 分区，包含以下内容： 

```bash
fw_dynamic.bin        #opensbi
Image                 #kernel image
kernel-release        #commit id of kernel
light_aon_fpga.bin    #fw for E902 aon
light_c906_audio.bin  #fw for C906 audio
light-lpi4a.dtb       #1.85GHz dtb
light-lpi4a_2Ghz.dtb  #2GHz overclock dtb
light-lpi4a-ddr2G.dtb #history dtb
```

`rootfs.ext4` 为根文件系统，默认为 Debian 系统。

烧录镜像的典型 log 输出如下：

![](./assets/burn_image/burn_image_progress_result.png)

<!--  
```bash
(base) pc@n5105:~/work/$ sudo ./fastboot flash ram u-boot-with-spl.bin
Sending 'ram' (935 KB)                             OKAY [  0.248s]
Writing 'ram'                                      OKAY [  0.002s]
Finished. Total time: 0.255s
(base) pc@n5105:~/work/$ sudo ./fastboot reboot
Rebooting                                          OKAY [  0.001s]
Finished. Total time: 0.202s
(base) pc@n5105:~/work/$ sudo ./fastboot flash uboot u-boot-with-spl.bin
Sending 'uboot' (935 KB)                           OKAY [  0.054s]
Writing 'uboot'                                    OKAY [  0.030s]
Finished. Total time: 0.107s
(base) pc@n5105:~/work/$ sudo ./fastboot flash boot boot_20230420.ext4 
Sending 'boot' (40000 KB)                          OKAY [  1.705s]
Writing 'boot'                                     OKAY [  0.877s]
Finished. Total time: 2.770s
(base) pc@n5105:~/work/$ sudo ./fastboot flash root rootfs-20230425-001635-nogpu.ext4 
Invalid sparse file format at header magic
Sending sparse 'root' 1/37 (114572 KB)             OKAY [  4.793s]
Writing 'root'                                     OKAY [  3.087s]
Sending sparse 'root' 2/37 (105264 KB)             OKAY [  4.465s]
Writing 'root'                                     OKAY [  2.330s]
Sending sparse 'root' 3/37 (111970 KB)             OKAY [  4.814s]
Writing 'root'                                     OKAY [  2.861s]
Sending sparse 'root' 4/37 (114684 KB)             OKAY [  4.902s]
Writing 'root'                                     OKAY [  2.658s]
Sending sparse 'root' 5/37 (101490 KB)             OKAY [  4.305s]
Writing 'root'                                     OKAY [  2.652s]
Sending sparse 'root' 6/37 (114684 KB)             OKAY [  4.648s]
Writing 'root'                                     OKAY [  2.657s]
Sending sparse 'root' 7/37 (113862 KB)             OKAY [  4.755s]
Writing 'root'                                     OKAY [  2.826s]
Sending sparse 'root' 8/37 (111189 KB)             OKAY [  4.741s]
Writing 'root'                                     OKAY [  2.695s]
Sending sparse 'root' 9/37 (114625 KB)             OKAY [  4.865s]
Writing 'root'                                     OKAY [  2.660s]
Sending sparse 'root' 10/37 (104030 KB)            OKAY [  4.506s]
Writing 'root'                                     OKAY [  4.108s]
Sending sparse 'root' 11/37 (111701 KB)            OKAY [  4.744s]
Writing 'root'                                     OKAY [  2.717s]
Sending sparse 'root' 12/37 (107317 KB)            OKAY [  4.568s]
Writing 'root'                                     OKAY [  2.583s]
Sending sparse 'root' 13/37 (114629 KB)            OKAY [  4.830s]
Writing 'root'                                     OKAY [  2.753s]
Sending sparse 'root' 14/37 (109798 KB)            OKAY [  4.711s]
Writing 'root'                                     OKAY [  2.778s]
Sending sparse 'root' 15/37 (112203 KB)            OKAY [  4.795s]
Writing 'root'                                     OKAY [  2.982s]
Sending sparse 'root' 16/37 (112502 KB)            OKAY [  4.827s]
Writing 'root'                                     OKAY [  2.991s]
Sending sparse 'root' 17/37 (114110 KB)            OKAY [  4.849s]
Writing 'root'                                     OKAY [  2.853s]
Sending sparse 'root' 18/37 (114681 KB)            OKAY [  4.888s]
Writing 'root'                                     OKAY [  2.802s]
Sending sparse 'root' 19/37 (112042 KB)            OKAY [  4.799s]
Writing 'root'                                     OKAY [  3.674s]
Sending sparse 'root' 20/37 (109101 KB)            OKAY [  4.631s]
Writing 'root'                                     OKAY [  2.582s]
Sending sparse 'root' 21/37 (114225 KB)            OKAY [  4.623s]
Writing 'root'                                     OKAY [  2.782s]
Sending sparse 'root' 22/37 (114365 KB)            OKAY [  4.703s]
Writing 'root'                                     OKAY [  2.667s]
Sending sparse 'root' 23/37 (103529 KB)            OKAY [  4.133s]
Writing 'root'                                     OKAY [  2.442s]
Sending sparse 'root' 24/37 (114664 KB)            OKAY [  4.631s]
Writing 'root'                                     OKAY [  2.581s]
Sending sparse 'root' 25/37 (114550 KB)            OKAY [  4.749s]
Writing 'root'                                     OKAY [  2.878s]
Sending sparse 'root' 26/37 (114686 KB)            OKAY [  4.796s]
Writing 'root'                                     OKAY [  2.853s]
Sending sparse 'root' 27/37 (114466 KB)            OKAY [  4.800s]
Writing 'root'                                     OKAY [  2.894s]
Sending sparse 'root' 28/37 (110689 KB)            OKAY [  4.711s]
Writing 'root'                                     OKAY [  2.616s]
Sending sparse 'root' 29/37 (114687 KB)            OKAY [  4.880s]
Writing 'root'                                     OKAY [  2.992s]
Sending sparse 'root' 30/37 (110984 KB)            OKAY [  4.710s]
Writing 'root'                                     OKAY [  2.451s]
Sending sparse 'root' 31/37 (114685 KB)            OKAY [  4.920s]
Writing 'root'                                     OKAY [  2.749s]
Sending sparse 'root' 32/37 (114684 KB)            OKAY [  4.825s]
Writing 'root'                                     OKAY [  2.503s]
Sending sparse 'root' 33/37 (114684 KB)            OKAY [  4.816s]
Writing 'root'                                     OKAY [  3.262s]
Sending sparse 'root' 34/37 (114686 KB)            OKAY [  4.745s]
Writing 'root'                                     OKAY [  2.825s]
Sending sparse 'root' 35/37 (114684 KB)            OKAY [  4.913s]
Writing 'root'                                     OKAY [  2.630s]
Sending sparse 'root' 36/37 (114684 KB)            OKAY [  4.838s]
Writing 'root'                                     OKAY [  2.593s]
Sending sparse 'root' 37/37 (21324 KB)             OKAY [  0.926s]
Writing 'root'                                     OKAY [  0.487s]
Finished. Total time: 281.671s
```
-->

## 启动机制

brom -> uboot spl -> uboot -> opensbi -> kernel

TODO

## 批量烧录

如果你有商业需求，需要批量烧录固件，可以使用 sipeed 提供的 ARM/RV 版 fastboot 制作离线批量烧录器。
如果你需要烧录的数量很大，也可以直接联系 support@sipeed.com，我们提供预烧录镜像服务。