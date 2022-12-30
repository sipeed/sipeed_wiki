---
title: AXera-Pi Guide
tags: AXera-Pi, Burn image
keywords: AXera-Pi，Burn, image
desc: AXera-Pi Burn image
update:
  - date: 2022-12-22
    version: v0.2
    author: wonder
    content:
      - Finish editing
  - date: 2022-12-09
    version: v0.1
    author: wonder
    content:
      - Create this File
---

---

> This page is on building, please use translation application to see https://wiki.sipeed.com/m3axpi instead.

## Product guideline

To make it easiler to use this board, we prepare this guide.

## OS introduction

**The default AXera-Pi kit has no onboard memory storage, so it's necessary to prepare a TF card to boot this device.**

For Axera-Pi, we provide Debian11 Bullseye image file.

> ![debian_logo](./../../../zh/maixIII/assets/debian_logo.jpg)
> [Reasons to use Debian](https://www.debian.org/intro/why_debian.en.html).

TF card which has been burnned system image can be bought from [Sipeed aliexpress](https://sipeed.aliexpress.com/store/1101739727), otherwise you need to perpare your own system image TF card by following steps.

## Choose TF card

People who has bought the the TF card which has been burnned system image can skip this chapter and read [start Linux]() to use this board

We have tested the read and write speed of some TF cards on Axera-pi, for users to make the choice of TF card.

![sd](./../../../zh/maixIII/assets/flash_system/sd.jpg)

> Some TF cards are added to test after this photo, so they are not in this photo but they can be recognized by their number.

| Number | Model                                    | <p style="white-space:nowrap">Write speed（Write 160MB）</p> | <p style="white-space:nowrap">Read speed（Read 160MB） </p> |
| ------ | ---------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| 1.     | Netac A2  P500-HS-64GB                   | 2.04697 s, 80.0 MB/s                                         | 1.8759 s, 87.3 MB/s                                         |
| 2.     | Samsung microSDXC UHS-I 128G (Bule card) | 2.53387 s, 64.7 MB/s                                         | 1.99882 s, 82.0 MB/s                                        |
| 3.     | EAGET T1 series 64G                      | 6.56955 s, 24.9 MB/s                                         | 7.13792 s, 23.0 MB/s                                        |
| 4.     | Keychron microSDXC UHS-I 128G            | 2.28133 s, 71.8 MB/s                                         | 1.92001 s, 85.3 MB/s                                        |
| 5.     | KIOXIA microSDXC UHS-I 32G               | 6.71284 s, 24.4 MB/s                                         | 2.36794 s, 69.2 MB/s                                        |
| 6.     | Netac  A1 32GB                           | 4.31411 s, 38.0 MB/s                                         | 2.00759 s, 81.6 MB/s                                        |
| 7.     | BanQ JOY card platinum 64G               | 9.08105 s, 18.0 MB/s                                         | 9.02843 s, 18.1 MB/s                                        |
| 8.     | Hiksemi HS -TF- P2 64G                   | 2.28079 s, 71.8 MB/s                                         | 1.87698 s, 87.3 MB/s                                        |

Tht following TF cards are not in this photo but we also tested them.

| Number | Model                                 | <p style="white-space:nowrap">Write Speed (Write 160MB) </p> | <p style="white-space:nowrap">Read Speed (Read 160MB) </p> |
| ------ | ------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- |
| 1.     | Lexar 64GB TF（MicroSD）C10 U3 V30 A2 | 2.59644 s, 63.1 MB/s                                         | 1.9106 s, 85.8 MB/s                                        |
| 2.     | Lexar 128GB TF（MicroSD）C10 U3 V30   | 6.73793 s, 24.3 MB/s                                         | 6.94079 s, 23.6 MB/s                                       |

## Burn system image

![flash](./../../../zh/maixIII/assets/axpi-flash.png)

We only reserved EMMC pad on board, so we need to a TF card which have been burned system image to boot linux on this boad.

### Get image

Because the system image is about 2G, so we only provide mega link to download.

Visit mega [Click me](https://mega.nz/folder/9EhyBbJZ#lcNhhm9aWXOyo2T0DDaSqA) to download the image file.

![debian](./assets/flash_system/debian.jpg)

The file name end with `img.xz` is the compressed system image file, and the other file name end with `img.xz.md5sum` is the check file, which we use to check the compressed system image file.

The name rule of compressed system image file is `Image provider` _ `Target chip` _ `Linux distribution` _ `Created time` + `img.xz`

The check file should be used in the Linux, and users using windows10 or windows 11 can use the wsl to prepare a Linux environment

Run command `md5sum -c *.md5sum*` in the path where compressed system image file and check file are to check the compressed system image file.

| Check succeeded                                                       | Check failed                                                     |
| -------------------------------------------------------------- | ------------------------------------------------------------ |
| ![md5sum_success](./../../../zh/maixIII/assets/flash_system/md5sum_success.jpg) | ![md5sum_failed](./../../../zh/maixIII/assets/flash_system/md5sum_failed.jpg) |

If there is some thing with the compressed system image file, it will shows FAILED. Normally we don't need to check the compressed system image file, this is only for those who need.

### Burn image

**Before burning image, we need do following preparation:**

- A TF card with a storge capacity card over 8GB; It is recommended to buy an official image card, otherwise it may lead to a bad experience due to the bad performace of the TF card
- A card reader: It is recommended to use the card reader that supports USB3.0, this will save our time on burning the system image card.
- [Etcher](https://www.balena.io/etcher/) application: Download the edition of this application suitable for your computer system.

**Burning system image steps**

Run [Etcher](https://www.balena.io/etcher/ "Etcher") application, click `Flash from file`, choose the compressed system image `img.xz` file， then click `Select target` to choose the TF card，click `FLASH` to burn your TF card.

**Burn the TF card**

![burn_image_by_etcher](./../../../assets/maixIII/ax-pi/burn_image_by_etcher.gif)


| Burning                                                                          | Finish burning                                                    |
| ------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| ![axera_burning_image](./../../../assets/maixIII/ax-pi/axera_burning_image.png) | ![finish_flash](./../../../zh/maixII/M2A/assets/finish_flash.png) |

Note that after finish burning the application shows `Flash Complete!` and `Successful`.

Finishing above steps, the computer will ask us to format the udisk, we just ignore this information and remove the TF card (Because we have make `Successful` in Etcher), prepare for the following operations.

### Burning Questions

#### 1. After selecting sustem image, Etcher shows error.

Rerun Etcher application to solve this error due to software cache or other issues

#### 2. After finishing burning software the application shows FAILED not Successful

Reburn the TF card.

#### 3. The storage capacity of tf card is too small

In this case, those who use Windows and MaxOS can use [SD Card Formatter](https://www.sdcard.org/downloads/formatter/eula_windows/SDCardFormatterv5_WinEN.zip) to format tf card, and those use Linux can format the tf card by [Gparted](https://gparted.org/).

## Boot System

Finishing burning system image into tf card, we can assemble this board and boot this device.

![axpi-connect](./../../../zh/maixIII/assets/axpi-connect.png)

### Assemble this board

> Those have bought the `Full board package` can skip these steps and visit [boot Axera-pi] to start.

**Preparation**

- An AXera-Pi development board
- At least one USB3.0 connector to connect device(This board may fail to boot because the insufficient of power supply from USB2.0)
- A tf card which has been burned system image
- GC4653 camera or OS04a10 camera
- The 5 inchs MIPI screen suitable for Axera-pi

![axpi-config](./../../../zh/maixIII/assets/axpi-config.jpg)

**Follow these steps to make sure you assemble them correctly**

1. Set the screen and the board as shown in the image below, and connect them.
2. Insert tf card which has been burned system image into the card slot on Axera-pi.
3. Connect the camera with Axera-pi as shown in the image below, make sure you have removed the cover on the camera after finishing connectting.

<html>
  <img src="./../../../zh/maixIII/assets/mipi.jpg" width=48%>
  <img src="./../../../zh/maixIII/assets/sensor.jpg" width=48%>
</html>

### Boot AXera-Pi

Connect both `USB-UART` and `USB-OTG` port with computer by USB type-c cable to boot AXera-Pi, make sure you have insert the tf card which has been burned system image.

![start](./../../../zh/maixIII/assets/start.jpg)

> In **20221013** we update the power-on phenomenon:

- The 3.5mm connector play the music if connected with device.
- 5 inches screen displays picture.
- The logs are printed to USB-UART port, run serial port application to see it if you need.

Here are the drivers for CH340 which is the USB-UART chip on Axera-Pi, install it if you can't see the serial device in your computer.

[CH34x Windows driver](https://dl.sipeed.com/shareURL/MAIX/tools/ch340_ch341_driver)
[CH34x Linux driver](http://www.wch-ic.com/downloads/CH341SER_LINUX_ZIP.html)

And those who use Ubuntu22.04 may not be able to open serial port (ttyUSB), read [this](https://www.chippiko.com/ch340-dev-ttyusb-not-showing) to see the solvement.

.. details:: Click to see the system boot log of debian11

    ```bash
    Vddr init success!
    The system boot form EMMC
    enter boot normal mode

    U-Boot 2020.04 (Jun 16 2022 - 00:16:34 +0800)

    Model: AXERA AX620_demo Board
    DRAM:  1 GiB
    NAND:  unknown raw ID 77ee0178
    uclass_get_device: Invalid bus 0 (err=-524)
    0 MiB
    initr_pinmux: delay pinmux_init for env board id
    MMC:   enter sdhci_cdns_get_cd call mmc_getcd
    enter sdhci_cdns_get_cd call mmc_getcd
    mmc@10000000: 0, mmc@4950000: 1
    Loading Environment from MMC... OK
    In:    serial
    Out:   serial
    Err:   serial
    MMC: no card present
    sd card is not present
    enter normal boot mode
    Net:
    reset EMAC0: ethernet@0x4970000 ...
    Warning: ethernet@0x4970000 (eth0) using random MAC address - 6a:e4:fd:58:97:ea
    eth0: ethernet@0x4970000
    Hit any key to stop autoboot:  0
    reading DTB and BOOT image ...
    reading bootimg header...
    MAGIC:       AXERA!
    img size:    4841536
    kernel_size: 4841472
    kernel_addr: 64
    id:bc 19 bb a7 2d 27 74 de 7c 91 4b 70 ea c9 ab 96 50 61 bd e0 2b 02 8b e5 c8 ee 22 ce df b1 cf ea
    load kernel image addr = 0x40008000,load dtb image addr = 0x48008000
    boot cmd is :bootm 0x40008000 - 0x48008000
    ## Booting kernel from Legacy Image at 40008000 ...
      Image Name:   Linux-4.19.125
      Image Type:   ARM Linux Kernel Image (uncompressed)
      Data Size:    4839952 Bytes = 4.6 MiB
      Load Address: 40008000
      Entry Point:  40008000
      Verifying Checksum ... OK
    ## Flattened Device Tree blob at 48008000
      Booting using the fdt blob at 0x48008000
      Loading Kernel Image
      Using Device Tree in place at 48008000, end 480103d6

    Starting kernel ...


    Welcome to Debian GNU/Linux 11 (bullseye)!

    [  OK  ] Created slice system-getty.slice.
    [  OK  ] Created slice system-modprobe.slice.
    [  OK  ] Created slice system-serial\x2dgetty.slice.
    [  OK  ] Created slice User and Session Slice.
    [  OK  ] Started Dispatch Password …ts to Console Directory Watch.
    [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
    [  OK  ] Reached target Local Encrypted Volumes.
    [  OK  ] Reached target Network is Online.
    ......
    ```

## Login AXera-Pi

![start](./../../../zh/maixIII/assets/start.jpg)

> When the logo above is displayed on the screen of AXera-Pi, the system has finished booting, and we can login to AXera-Pi.

![axpi-login](./../../../zh/maixIII/assets/axpi-login.png)

The First time to login to device, we need to use serial port application to open serial port to communicate with device to login, and use SSH login is also ok if you know the ip address of your board.

[MobaXterm](https://mobaxterm.mobatek.net/) is a ultimate toolbox for remote computing, we use this software to run our command on the board for example.

![ssh](https://wiki.sipeed.com/hardware/zh/maixIII/assets/ssh.jpg)

### Login by serial port

We take MobaXterm as the example serial port software, you can use your favorite one.

In MobaXterm, we create a serial session. Set baudrate 115200, then click ok to create it.

![mobaxterm-serial-4](https://wiki.sipeed.com/soft/maixpy3/zh/tools/assets/mobaxterm-serial-4.png)

Then click the created serial session to open the serial port to build communication.

![mobaxterm-serial-5](https://wiki.sipeed.com/soft/maixpy3/zh/tools/assets/mobaxterm-serial-5.png)

Run the serial port application, use username `root` and password `root` to login.

The password is not displayed when you enter it, so just retry if you fail login.

![axera_pi_serial_root_login](./assets/flash_system/axera_pi_serial_root_login.jpg)

### Login by SSH

To login by ssh, we need to know the ip address of Axera-Pi.

#### Traditional ip address

We make Axera-Pi and the computer in a same network environment, then run command `ifconfig` on Axera-Pi to get the ip address of Axera-Pi in this network environment.

But you need to make sure you have connected Axera-Pi to network, visit [Connect to network](#connect-to-network) to know how to connect to network.

#### RNDIS

Connect the computer with USB-OTG port on Axera-Pi.

![otg](https://wiki.sipeed.com/hardware/zh/maixIII/assets/otg.jpg)

Normally RNDIS is driver free in Linux, and in Windows we need to update driver [Click me](./rndis.md), for macos it's need to build and install `horndis` to use RNDIS.

Deflaut RNDIS driver error in Windows:

![rndis_error_device](./assets/flash_system/rndis_error_device.jpg)

Run command `ifconfig`, we can see there is a usb device with IP `192.168.1.233`, we'll use this ip address many time in the following content.

![ifconfig_usb_ip_address](./assets/flash_system/ifconfig_usb_ip_address.jpg)

#### Login to board

Up to now you have get one of your ip address, run command `ssh {username}@{ip address}` to connect to your board.

Here we take the RNDIS ip address for example to connect Axera-Pi by SSH, and the username is root, you can use other ip address or username you like if you have created the new user.

```bash
ssh root@192.168.233.1
```

![ssh_rndis_connect](./assets/flash_system/ssh_rndis_connect.jpg)

## Connect to network

Axera-Pi connects to network through network cable or wireless.

### Connect by Ethernet

Connect the board ethernet port with a network gateway by network cable.

Run command `ifconfig eth0` to see whether there is the ip address.

![nmtui_eth0_ifconfig](./assets/flash_system/nmtui_eth0_ifconfig.jpg)

If there is no ip address of eth0 after connected with network gateway, run command `dhclient eth0 &
` to get the ip address manually.
![nmtui_eth0_dhclient](./assets/flash_system/nmtui_eth0_dhclient.jpg)

### Wireless network

1. Run command `ifconfig wlan0` to see whether there is the wireless device first, if there is no wireless device, visit [AXera-Pi Q&A](./faq_axpi.md#qno-wlan0-shown-in-result-after-running-command-ifconfig) to solve this problem.

2. Run command `nmtui-connect` to open a wireless internet graphical interface.
![nmtui](./../../../../hardware/zh/maixIII/assets/nmtui.jpg)

3. Run command `ifconfig wlan0` to see whether there is the ip address.
![nmtui_wlan0_ifconfig](./assets/flash_system/nmtui_wlan0_ifconfig.png)

## Config System

### System time

Maix-III AXera-Pi uses the NTP protocol to update the system time. You can run the `date` command to get the current system time.

> After connecting to Internet, system will automatically run `ntpdate-debian` to update system time.

#### Change timezone

Maix-III AXera-Pi default timezone is GMT+8, you can change it with command `dpkg-reconfigure tzdata` if necessary.

![system_time_timezone](./assets/flash_system/system_time_timezone.jpg)

#### Update time

Run `ntpdate-debian` command after connectting Maix-III AXera-Pi to network to update time.

#### Write into device

There is a RTC(Real Time Clock) on the ext-board under the Core module, which provides the read time for Maix-III AXera-Pi when not access to wireless. Use command `hwclock -w -f /dev/rtc0` to write current system time into RTC to adjust its time date.

### Install software

Based in debian, we can use `apt` to install the software on Maix-III AXera-Pi. Change the software resource if you think it's slow to download the software.

Here we install `gcc`, `gparted`.

```bash
sudo apt update
sudo apt install gcc gparted
```

![install_software_gcc_gparted](./assets/flash_system/install_software_gcc_gparted.jpg)

### Reboot device

> 由于 Linux 系统直接断电可能会导致文件系统损坏，如果可以的话建议按下述命令去进行开关机，可以避免一些由于直接断电系统损坏导致的奇怪问题出现。

Maix-III AXera-Pi 开发板的 Linux 系统可以通过 `reboot` 命令重启，重启命令如下：

```bash
reboot
```

### Shutdown device

Maix-III AXera-Pi 开发板的 Linux 系统可以通过 `poweroff` 命令关闭，关闭命令如下：

```bash
poweroff
```

### 磁盘扩容

基于一些用户可能有扩容分区的需求，因此在这里添加在 AXera-Pi 上给板子扩容或者是建立新分区的内容。

- 操作方法

首先需要烧录完上方的 debian11 的镜像系统后，再使用 AXera-Pi 登陆上 Linux 系统来进行磁盘扩容分区。

>[点击查看 AXera-Pi 登陆方式](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/basic_usage.html#%E7%B3%BB%E7%BB%9F%E7%99%BB%E5%BD%95)

成功登陆到 AXera-Pi 上后，用户可以先使用 `lsblk` 命令来查看设备当前的存储情况。接着使用 `cfdisk /dev/mmcblk2` 来进行磁盘分区扩容的操作。（`mmcblk2` 是我们进行操作的区域名称也称设备名）

.. details::点击查看配置示意图
    ![cfdisk](./../assets/cfdisk-mmcblk2.jpg)

运行命令后终端会弹出下图操作界面，由 `Free space` 可见存储空间还余 `4.3G`，用户可使用键盘上的方向键移动选择我们要扩容的分区 `/dev/mmcblk2p2` 。

.. details::点击查看配置示意图
    ![rizese-mmcblk2](./../assets/rizese-mmcblk2.png)

选择上图的 `Resize` 按下**回车键**对当前分区进行缩容或扩容，界面会跳出提示用户修改新的分区大小。

.. details::点击查看配置示意图
    ![new-resize](./../assets/new-resize.png)

修改后敲**回车键**确定，终端界面会回到原页面。这时我们已经完成对分区扩容的修改了，还需要把改动的部分写入磁盘。在页面选择 `Write` 并敲**回车键**后输入 `yes` 确定将改动分区表写入磁盘中，再敲**回车键**即可。

.. details::点击查看配置示意图
    ![write-disk](./../assets/write-disk.png)

操作后会返回原界面，选择 `Quit` 退出即可。

.. details::点击查看配置示意图
    ![quit](./../assets/quit.jpg)

接下来使用命令行 `df -h` 查询磁盘使用空间的情况，终端会显示用户没改动之前的使用情况，需要我们使用命令 `resize2fs /dev/mmcblk2p2` 来调整文件系统的大小实现对 `mmcblk2` 分区的扩容，再使用 `df -h` 查询就可以看到磁盘改动后的情况。

.. details::点击查看配置示意图
    ![df-mmcblk2](./../assets/df-mmcblk2.jpg)

> **注意**：如果调整完文件系统的大小后使用 `df -h` 查询磁盘信息依旧是改动前的信息，可使用 `reboot` 重启设备后在查询。

### 开机启动脚本

系统已经内置好 `/boot/rc.local` 的开机启动脚本，用户可参照以下示例进行修改。

开机启动脚本是在 / 根目录下运行的，举例来说，如果想要开机启动 `/home/run.sh` 脚本。

1. 用绝对路径挂后台运行程序 `/home/run.sh & ` 才可以确保开机后进入 shell 命令终端。
2. 【推荐】用相对路径挂后台运行程序 `cd /home && ./run.sh &` 注意此时 pwd 和绝对路径是不一样。

请先验证好可以在 / 根目录下启动后再放入以下的开机脚本中，不会就抄以下脚本的例子。

```bash
root@AXERA:~# cat /boot/rc.local
#!/bin/sh

# this file is called by /etc/rc.local at boot.

# systemctl stop usb-gadget@g0
# mkdir -p /mnt/udisk && mount /dev/sda1 /mnt/udisk
# python3 /mnt/udisk/alltest.py

if [ -f "/root/boot" ]; then
  cd /root/ && chmod 777 * && ./boot &  
elif [ -d "/root/app" ]; then
  cd /root/app && chmod 777 *
  if [ -f "./main" ]; then
    ./main &
  elif [ -f "./main.bin" ]; then
    ./main.bin &
  elif [ -f "./main.py" ]; then
    python3 ./main.py &
  fi
else
  aplay /home/res/boot.wav >/dev/null 2>&1 &
  /opt/bin/sample_vo_fb -v dsi0@480x854@60 -m 0 >/dev/null 2>&1 &
  sleep 0.5 && /home/fbv-1.0b/fbv /home/res/2_480x854.jpeg && killall sample_vo_fb
fi

exit 0
```

.. details::点我查看示例图
    ![start](./../assets/start.jpg)

.. details::点击查看连接后串口输出的 debian11 系统启动日志。

    ```bash
    Vddr init success!
    The system boot form EMMC
    enter boot normal mode

    U-Boot 2020.04 (Jun 16 2022 - 00:16:34 +0800)

    Model: AXERA AX620_demo Board
    DRAM:  1 GiB
    NAND:  unknown raw ID 77ee0178
    uclass_get_device: Invalid bus 0 (err=-524)
    0 MiB
    initr_pinmux: delay pinmux_init for env board id
    MMC:   enter sdhci_cdns_get_cd call mmc_getcd
    enter sdhci_cdns_get_cd call mmc_getcd
    mmc@10000000: 0, mmc@4950000: 1
    Loading Environment from MMC... OK
    In:    serial
    Out:   serial
    Err:   serial
    MMC: no card present
    sd card is not present
    enter normal boot mode
    Net:
    reset EMAC0: ethernet@0x4970000 ...
    Warning: ethernet@0x4970000 (eth0) using random MAC address - 6a:e4:fd:58:97:ea
    eth0: ethernet@0x4970000
    Hit any key to stop autoboot:  0
    reading DTB and BOOT image ...
    reading bootimg header...
    MAGIC:       AXERA!
    img size:    4841536
    kernel_size: 4841472
    kernel_addr: 64
    id:bc 19 bb a7 2d 27 74 de 7c 91 4b 70 ea c9 ab 96 50 61 bd e0 2b 02 8b e5 c8 ee 22 ce df b1 cf ea
    load kernel image addr = 0x40008000,load dtb image addr = 0x48008000
    boot cmd is :bootm 0x40008000 - 0x48008000
    ## Booting kernel from Legacy Image at 40008000 ...
    Image Name:   Linux-4.19.125
    Image Type:   ARM Linux Kernel Image (uncompressed)
    Data Size:    4839952 Bytes = 4.6 MiB
    Load Address: 40008000
    Entry Point:  40008000
    Verifying Checksum ... OK
    ## Flattened Device Tree blob at 48008000
    Booting using the fdt blob at 0x48008000
    Loading Kernel Image
    Using Device Tree in place at 48008000, end 480103d6

    Starting kernel ...


    Welcome to Debian GNU/Linux 11 (bullseye)!

    [  OK  ] Created slice system-getty.slice.
    [  OK  ] Created slice system-modprobe.slice.
    [  OK  ] Created slice system-serial\x2dgetty.slice.
    [  OK  ] Created slice User and Session Slice.
    [  OK  ] Started Dispatch Password …ts to Console Directory Watch.
    [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
    [  OK  ] Reached target Local Encrypted Volumes.
    [  OK  ] Reached target Network is Online.
    ......

### 更新内核与驱动

在 SD 卡的第一分区会挂载到系统根目录下的 /boot 系统启动相关的文件，替换它即可完成更新。

- boot.bin 芯片 spl 初始化程序

- uboot.bin uboot 启动引导程序

- kernel.img linux 内核

- dtb.img linux 设备树

## 如何传输文件 

> 如果在使用 AXera-Pi 途中出现从设备到电脑端文件互传的需求，可根据以下的方式进行传输：
###  使用读卡器物理拷贝文件

**物理传输**：由于 Linux 系统采用 `ext4` 分区在 Windows / Mac 默认系统下无法进行查看，用户需额外安装增强工具才能读取到具体的分区。而 Linux 系统可直接看到卡里的分区和内容，也可以选择把读卡器接到安卓设备通过 **OTG** 转接头实现文件拷贝。

- [如何在 Windows 下访问 ext4 格式的硬盘？](https://zhuanlan.zhihu.com/p/448535639)

- [[macOS] 在 macOS 上挂载 Linux 的 ext/ext3/ext4 文件系统](https://blog.twofei.com/773/)

### 板子与电脑的文件互传

>基于让用户的使用更加快速便捷，还可以选择直接在板子上与电脑端通过工具实现文件互传。

**使用 SSH 远程管理工具进行文件传输：**

使用前需要使用 `ifconfig` 查询板子的 IP 地址做登录备用，可点击前往[系统登录](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/basic_usage.html#%E5%9F%BA%E4%BA%8E-ip-%2B-ssh-%E7%99%BB%E5%BD%95)查看。在 Windows 上有众多远程管理 Linux 服务器的工具都提供了文件传输的功能，这里推荐免费绿色的 **Mobaxterm** 工具。

- [如何使用 MobaXterm](https://wiki.sipeed.com/hardware/zh/maixII/M2/tools/mobaxterm.html)

- [利用 MobaXterm 实现 Linux 和 Windows 之间传输文件](https://jingyan.baidu.com/article/9f63fb91e2bc6688400f0e93.html)

- [用 MobaXterm 在 Linux 和 Windows 之间上传/下载文件](https://blog.csdn.net/unforgettable2010/article/details/123930796)

> 如果想了解更多的工具可点击[【推荐7款超级好用的终端工具 —— SSH+FTP】](https://zhuanlan.zhihu.com/p/301653835)查看，而其他系统都提供了好用的命令行终端，支持 SSH 、scp 等命令直接执行。

**使用 scp 命令复制文件：**

和 cp 复制文件等命令一样，它就是 `ssh + cp = scp` 这个意思。

- [Linux 操作系统 scp 命令使用方法](https://cloud.tencent.com/developer/article/1876623)

**使用有线串口互传文件：**

使用前根据串口 serial 登录接线配置参数连上板子，安装 `apt-get install lrzsz` 工具后可参考以下文章。

- [有线串口 serial 登录](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/basic_usage.html#%E6%9C%89%E7%BA%BF-%E4%B8%B2%E5%8F%A3-serial-%E7%99%BB%E9%99%86)

- 使用命令行工具 `minicom -D /dev/ttyUSB0 -b 115200` 可以查看[ Ubuntu 中使用 minicom 玩转文件的上传与下载](https://blog.csdn.net/wanyeye/article/details/42002377)。

- 使用 MobaXterm 可以点击 [MobaXterm 使用 rz/sz 传送文件](https://blog.csdn.net/qq_28837389/article/details/120073720)查看。

## 验证系统外设

### 系统预置的资源

Maix-III AXera-Pi 开发板的 Linux 系统预置了一些资源，可以通过 `ls /opt` 命令来查看。

```bash
root@AXERA:~# ls /opt
bin  include  lib  scripts  share
```

还有一些在 `home` 目录下：

```bash
root@AXERA:~# tree -L 1 /home
├── ax-samples          # npu ai sdk
├── examples            # 一些开箱示例
├── fbv-1.0b            # fbv 图片查看器
├── images              # 一些测试图片
├── libmaix             # simple pipeline sdk
├── models              # 内置的 AI 模型
├── res                 # 一些图像字体资源
├── systemd-usb-gadget  # 配置 usb 服务
├── usb-uvc-gadget      # 配置 uvc 服务
└── ustreamer           # mjpeg 图传
```

板子已经预置了 `gcc g++ gdb libopencv ffmpeg` 等工具，可直接在板上编译运行程序。

> **注意**：使用 xxxx menuconfig 报错请移步[Maix-III 系列 AXera-Pi 常见问题（FAQ）](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/faq_axpi.html)

可参考下方使用方法：

```bash
cd /home/libmaix/examples/axpi/
python3 project.py build
fbon
./dist/start_app.sh
```

.. details::点击查看示例效果
    使用命令行后会打印大量数据信息并启动摄像头及屏幕。

    ![libmaix](./../assets/libmaix.jpg)

而 axsample 已经预编译好了，相关 joint 模型已内置在 `/home/models/` 下便于用户查询。

```bash
/home/ax-samples/build/install/bin/ax_yolov5s -m /home/models/yolov5s.joint -i /home/images/cat.jpg -r 10
fbon
fbv yolov5s_out.jpg
```

.. details::点击查看效果
    输入上方命令后屏幕会显示 yolovs_out.jpg 图像

    ![cat](./../assets/cat.jpg)

可以在联网后直接 `git pull` 更新仓库的提交记录，如果不能访问 github 的话就设置一下 `git remote` 从 gitee 拉取代码吧。

### 排针引脚图

![layout_axpi](./../assets/layout_axpi_1.png)

### CPU & RAM

默认 800MHz 可以调到 1ghz.

```bash
root@AXERA:~# ax_lookat 0x01900000 -s 33
0x1900000:00000033
root@AXERA:~# ax_clk
AX620A:
DDR:                 3733 MHz
CPU:                 800 MHz
BUS of VPU:         624 MHz
BUS of NPU:         624 MHz
BUS of ISP:         624 MHz
BUS of CPU:         624 MHz
NPU OTHER:         800 MHz
NPU GLB:         24 MHz
NPU FAB:         800 MHz
NPU CORE1:         800 MHz
NPU CORE0:         800 MHz
ISP:                 533 MHz
MM:                 594 MHz
VPU:                 624 MHz
root@AXERA:~# ax_lookat 0x01900000 -s 35
0x1900000:00000035
root@AXERA:~# ax_clk
AX620A:
DDR:                 3733 MHz
CPU:                 1000 MHz
BUS of VPU:         624 MHz
BUS of NPU:         624 MHz
BUS of ISP:         624 MHz
BUS of CPU:         624 MHz
NPU OTHER:         800 MHz
NPU GLB:         24 MHz
NPU FAB:         800 MHz
NPU CORE1:         800 MHz
NPU CORE0:         800 MHz
ISP:                 533 MHz
MM:                 594 MHz
VPU:                 624 MHz
root@AXERA:~#
```

目前硬件内存虽然是 2g 但在系统上只能看到 745M ，不用担心，这是目前的分配内存过于保守导致的，后续更新内核调整一下 NPU 和 CMM 的内存分配的。

### VIDEO

>**注意**：以下例程是原始测试时检查硬件好坏的程序，请用下面内置应用看正常的效果！
>内置开箱应用传送门：[点击前往](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/basic_usage.html#%E5%86%85%E7%BD%AE%E5%BC%80%E7%AE%B1%E5%BA%94%E7%94%A8)
目前系统的摄像头驱动不经过 v4l2 驱动框架，所以必须通过代码配置的方式进行启用，相关摄像头驱动都是在应用层上完成的，

- gc4653 （基础版）
- os04a10（夜视版）

```bash
sample_vin_vo -c 2 -e 1 -s 0 -v dsi0@480x854@60
```

.. details::运行上方命令后可看到画面（示例效果）
    ![video](./../assets/video.jpg)

>目前默认使用的是 gc4653 ，使用 os04a10 请移步[Maix-III 系列 AXera-Pi 常见问题(FAQ)](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/faq_axpi.html)查询。

### DISPLAY

目前系统默认使用的是最简单的 framebuffer 显示驱动（/dev/fb0），在系统里内置了 `fbon / fboff / fbv xxx.jpg` 三个命令负责管理 fb 设备的启用和现实。

```bash
fbon
fbv /home/res/logo.png
fboff
```

![fbv_logo](./../assets/fbv_logo.jpg)

目前想要使用 libdrm 需要搭配代码使用，请参考 sdk 的源码实现，因为目前系统还未移植好 gpu 驱动所以无法使用 modetest 进行测试，但可以参考下面进行测试。

测试屏幕是否能用运行右侧 `sample_vo -v dsi0@480x854@60 -m 0` 命令屏幕会显示彩条，但使用前务必调用 `fboff` 关闭 fb 设备。

### NPU

测试 NPU 的示例程序在 `/home/ax-samples/build/install` 目录下，已经预编译好了，直接就可以调用并显示运行结果。

```fbon
/home/ax-samples/build/install/bin/ax_yolov5s -m /home/models/yolov5s.joint -i /home/images/cat.jpg -r 10
fbv yolov5s_out.jpg
```

### AUDIO

和桌面系统保持一致，直接可用 alsa-utils 进行测试。

- **测试脚本**：`speaker-test -t sine -f 440 -c1`
- **播放音频**：`aplay test.wav`
- **录制音频**；`arecord test.wav -c 2 -d 2`

录音回放的 `python3` 代码如下：

```python
import pyaudio
try:
    chunk = 1024      # Each chunk will consist of 1024 samples
    sample_format = pyaudio.paInt16      # 16 bits per sample
    channels = 2      # Number of audio channels
    fs = 44100        # Record at 44100 samples per second
    time_in_seconds = 30
    p = pyaudio.PyAudio()
    stream = p.open(format=sample_format,
                    channels = channels,
                    rate = fs,
                    frames_per_buffer = chunk,
                    input = True, output = True)
    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * time_in_seconds)):
        data = stream.read(chunk)
        stream.write(data)
finally:
    # Stop and close the Stream and PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()
```

可以在 alsamixer 配置你的设备，如果不了解的话建议不要修改。

![alsamixer](./../assets/alsamixer.jpg)

### USB

>**注意**：由于芯片只有一个完整功能的 usb2.0，同一时刻下只有一个使用方向如 OTG 从机或 HOST 主机。

#### 如何配置 USB OTG 虚拟网卡 RNDIS usb0 有线 ssh 登录

默认就会启动配置 `systemctl enable usb-gadget@g0`，启动用 `systemctl start usb-gadget@g0`，停止开机启动用 `systemctl disable usb-gadget@g0`，停止服务用`systemctl stop usb-gadget@g0`。

此时使用命令 `sshpass -p root ssh root@192.168.233.1` 即可连接，账号及密码都是 root 。

![ssh-usb](./../assets/ssh-usb.jpg)

#### 如何配置 USB OTG 虚拟串口 /dev/ttyGS0 并转发登录接口

停止 usb-gadget@g0 后使用 `systemctl start usb-gadget@g1` 即可看到，然后使用 `systemctl start getty@ttyGS0` 即可转发串口终端到 usb 的虚拟串口上。

![usb_tty](./../assets/usb_tty.jpg)

#### 如何使用 USB HOST 读取一个 256M 的 SD 卡

先关了 otg 的 rndis 后再 lsusb 就可以看到了。

>我们在 debian 系统上配置了 usb-gadget@g1 和 usb-gadget@g0 两个服务。

```bash
root@AXERA:~# systemctl stop usb-gadget@g0
root@AXERA:~# lsusb
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 002: ID 067b:2731 Prolific Technology, Inc. USB SD Card Reader
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
root@AXERA:~# fdisk -l
Disk /dev/mmcblk2: 58.94 GiB, 63281561600 bytes, 123596800 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x32eb5429

Device         Boot  Start       End   Sectors  Size Id Type
/dev/mmcblk2p1 *      2048    264191    262144  128M  c W95 FAT32 (LBA)
/dev/mmcblk2p2      264192 123596799 123332608 58.8G 83 Linux


Disk /dev/sda: 240 MiB, 251658240 bytes, 491520 sectors
Disk model: SD Card Reader
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x0607cfd2

Device     Boot Start    End Sectors   Size Id Type
/dev/sda1  *      240 490239  490000 239.3M  e W95 FAT16 (LBA)
root@AXERA:~# mkdir /mnt/sdcard && mount /dev/sda1 /mnt/sdcard
```

一步到位挂载 U 盘第一分区的命令 `systemctl stop usb-gadget@g0 && lsusb && mkdir -p /mnt/udisk && mount /dev/sda1 /mnt/udisk`

#### 如何配置 USB OTG 虚拟一个 USB 摄像头

**usb-uvc-gadget**：[usb-uvc-gadget](https://github.com/junhuanchen/usb-uvc-gadget)

**更多详情请移步内置应用查看**：[应用传送门](http://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/basic_usage.html#uvc_vo)

#### 如何配置 USB HOST 读取一个 USB 摄像头

>适配 usb 摄像头前我们需要给板子接上以太网 `eth0`，使用 `ifconfig` 查询以太网的 `IP` 方便我们使用。
>如果获取不到以太网的 `IP` 地址，请移步右侧进行重新启动/配置[点击前往相关](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/basic_usage.html#%E6%9C%89%E7%BA%BF%E4%BB%A5%E5%A4%AA%E7%BD%91%EF%BC%88eth0%EF%BC%89%E9%85%8D%E7%BD%AE%E6%96%B9%E6%B3%95)。

**Ustreamer**：[点击查看相关仓库](https://github.com/pikvm/ustreamer)
运行下方的命令行，终端会弹出调试信息无明显报错后，打开任意浏览器输入我们刚获取的以太网 `IP` 地址，进入 `ustreamer` 使用体验拍照及录像功能。

```bash
/home/ustreamer/ustreamer --device=/dev/video0 --host=0.0.0.0 --port=80
```

![ustreamer_adb](./../assets/ustreamer_adb.png)

`snapshot` 为拍照功能，`stream` 为视频功能。

![ustreamer](./../assets/ustreamer.png)

.. details::点击查看效果图

    ![ustreamer_snapshot](./../assets/ustreamer_snapshot.jpg)

- **使用 Opencv 读取 USB 摄像头**

可在终端进入 `python3` 模式运行以下代码即可使用 USB 摄像头进行拍照。

```python
import os
import cv2
video = cv2.VideoCapture(0)
for i in range(30):
    ret, frame = video.read()
    if ret:
        cv2.imwrite("/tmp/capture.jpg", frame)
        os.system("fbon && fbv /tmp/capture.jpg")
```

.. details::点击查看终端运行图以及效果图

    ![opencv](./../assets/opencv.jpg)
    ![opencv_cream](./../assets/opencv_cream.jpg)

>运行出现报错请移步[Maix-III 系列 AXera-Pi 常见问题(FAQ)](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/faq_axpi.html)进行查询。

### GPIO

#### 读取 KEY 按键输入：GPIO2 21

```bash
echo 85  > /sys/class/gpio/export
echo in > /sys/class/gpio/gpio85/direction
cat /sys/class/gpio/gpio85/value
```

#### 点亮 LED 灯 GPIO2 A4-A5 68-69

```bash
echo 68  > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio68/direction
echo 1 > /sys/class/gpio/gpio68/value
sleep 1
echo 0 > /sys/class/gpio/gpio68/value
sleep 1
echo 1 > /sys/class/gpio/gpio68/value
```

> 计算规则 GPIO2 A4 == 32 *  2 + 4 = 68
对于爱芯的芯片，GPIO0 和 GPIO2 对应 A 和 C ，此处 A4 并不代表 GPIO2 只是序号。
也就是 GPIO2 A4 在标准设备中的定义为 GPIO C(2) 4(A4) 同理 GPIOA0 对应 GPIO0A4。

以后主流会统一到 PA0 或 PC4 这类定义，方便不同芯片共同定义。

[可参考的 gpio.h/gpio.c 代码](https://www.cnblogs.com/juwan/p/16917802.html#linux-spiv)

### UART

系统输出默认是 **ttyS0** ，排针上的是 **ttyS1** ，而虚拟串口是 **ttyGS0**。

![uart_tty](./../assets/uart_tty.jpg)

可用 `python3 pyserial` 库来测试功能的好与坏，但是需要注意排针丝印可能不准确。
如果出现串口的 tx 和 rx 没有数据的话可以反接一下，以及确保是共地的。

```python
import serial
ser = serial.Serial('/dev/ttyS1', 115200, timeout=1)
ser.write(b'hello world\n')
ser.close()
```

[可参考的 uart.h/uart.c 代码](https://www.cnblogs.com/juwan/p/16917802.html#linux-uart-ttysx)

### PWM

以配置一个 pwm0 修改屏幕背光为例，需更新到 **20221201** 后的镜像。
**例**：`echo 204 > /sys/class/pwm/pwmchip0/pwm0/duty_cycle` 运行后屏幕亮度只有十分之一.

```bash
echo 0 > /sys/class/pwm/pwmchip0/export
echo 4167 > /sys/class/pwm/pwmchip0/pwm0/period
echo 204 > /sys/class/pwm/pwmchip0/pwm0/duty_cycle
echo 2084 > /sys/class/pwm/pwmchip0/pwm0/duty_cycle
echo 0 > /sys/class/pwm/pwmchip0/pwm0/enable
```

PWM 使用参考：[点击查看](https://wiki.sipeed.com/soft/maixpy3/zh/usage/hardware/PWM.html#%E5%BC%80%E5%A7%8B).

### I2C

> m3axpi 的排针上的 I2C 是 /dev/i2c-7 对应 `i2cdetect -y -r 7` 喔， 0 1 2 是摄像头的， 8 是系统的 usb rtc 的， 9 做预留。
使用 i2c-tools 工具包，可使用 i2cdetect -y 0 来查看 i2c 总线上的设备。
如果出现 i2c 设备扫不到的情况需要接一下上拉电阻。

```bash
root@AXERA:~# i2cdetect -y -r 0
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- 21 -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- 36 -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
root@AXERA:~#
```

这里 **0x21** 和 **0x36** 就代表的板子在 cam0 这个排线上的 /dev/i2c-0 设备存在某个摄像头的 i2c 设备，而读写可用 i2cget 和 i2cset 命令，与其他芯片皆为同理。

### SPI

可参考右边同理事例：[为 AW V831 配置 spidev 模块，使用 py-spidev 进行用户层的 SPI 通信。](https://www.cnblogs.com/juwan/p/14341406.html)

```
root@AXERA:~# ./spidev_test -D /dev/spidev1.0 -v
spi mode: 0x0
bits per word: 8
max speed: 500000 Hz (500 KHz)
TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@....�..................�.
RX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@....�..................�.
root@AXERA:~# ./spidev_test -D /dev/spidev1.0 -v
spi mode: 0x0
bits per word: 8
max speed: 500000 Hz (500 KHz)
TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@....�..................�.
RX | FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF  | ................................
root@AXERA:~# ./spidev_test -D /dev/spidev1.0 -v
spi mode: 0x0
bits per word: 8
max speed: 500000 Hz (500 KHz)
TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@....�..................�.
RX | FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF  | ................................
```

### CHIP ID

获取芯片唯一的 id 码。

```
cat /proc/ax_proc/uid
```

### ADC（暂未支持）

.. details::点击查看

    硬件上支持，但软件上目前还没写调试工具配合。
    可参考外围开发手册，这需要专用的代码控制，目前还没有全部补充完。

    1. 设置 THM 寄存器
    2. 中间需要 delay 一段时间，否则读取出来的值，可能不对.
    3. 0x2000028 寄存器读取出来的值 DATA
    4. DAT 和 voltage 的对应关系，voltage = DATA / 1024 * VREF(1.8V)
    5. 如果读取 chan1/2/3/4，需要读取 0x200002c，0x2000030，0x2000034，0x2000038

    使能 ADC 通道
    devmem 0x2000020 32 0x1000 //chan0
    devmem 0x2000020 32 0x800 //chan1
    devmem 0x2000020 32 0x400 //chan2
    devmem 0x2000020 32 0x200 //chan3
    devmem 0x2000020 32 0x100 //chan4

    devmem 0x200002c
    devmem 0x2000030
    devmem 0x2000034
    devmem 0x2000038

### 出厂测试脚本

.. details::点击可查看产品出厂测试时用的 Python 测试脚本
    ```python
    test_flag = False

    try:
        from gpiod import chip, line, line_request
        config = None # rpi is default value A 0
        def gpio(gpio_line=0, gpio_bank="a", gpio_chip=0, line_mode = line_request.DIRECTION_OUTPUT):
            global config
            if config != None and gpio_line in config:
                gpio_bank, gpio_chip = config[gpio_line]
            l, c = [32 * (ord(gpio_bank.lower()[0]) - ord('a')) + gpio_line, chip("gpiochip%d" % gpio_chip)]
            tmp = c.get_line(l)
            cfg = line_request() # led.active_state == line.ACTIVE_LOW
            cfg.request_type = line_mode # line.DIRECTION_INPUT
            tmp.request(cfg)
            tmp.source = "GPIO chip %s bank %s line %d" % (gpio_chip, gpio_bank, gpio_line)
            return tmp
        def load(cfg=None):
            global config
            config = cfg
    except ModuleNotFoundError as e:
        pass

    key = gpio(21, gpio_chip=2, line_mode = line_request.DIRECTION_INPUT)
    led0 = gpio(4, gpio_chip=2, line_mode = line_request.DIRECTION_OUTPUT)
    led1 = gpio(5, gpio_chip=2, line_mode = line_request.DIRECTION_OUTPUT)

    import time
    import ifcfg
    import os

    def check_ifconfig():
        result = []
        for name, interface in ifcfg.interfaces().items():
            if name in ['eth0', 'wlan0'] and interface['inet']:
                result.append(name)
        return result

    try:
        if (0 == key.get_value()):
            os.system("export LD_LIBRARY_PATH=/opt/lib:LD_LIBRARY_PATH && /opt/bin/sample_vin_vo -c 2 -e 1 -s 0 -v dsi0@480x854@60 &")
            led1.set_value(1)
            while True:
                led0.set_value(1)
                time.sleep(0.2)
                led0.set_value(0)
                time.sleep(0.2)
                tmp = check_ifconfig()
                if len(tmp) > 1:
                    led0.set_value(0)
                    led1.set_value(0)
                    test_flag = True
                    break
            while (0 == key.get_value()):
                time.sleep(0.2)
            os.system("aplay /home/res/boot.wav")
            led0.set_value(1)
            led1.set_value(1)
            import pyaudio
            chunk = 1024      # Each chunk will consist of 1024 samples
            sample_format = pyaudio.paInt16      # 16 bits per sample
            channels = 2      # Number of audio channels
            fs = 44100        # Record at 44100 samples per second
            p = pyaudio.PyAudio()
            stream = p.open(format=sample_format,
                            channels = channels,
                            rate = fs,
                            frames_per_buffer = chunk,
                            input = True, output = True)
            while (1 == key.get_value()):
                data = stream.read(chunk, exception_on_overflow = False)
                stream.write(data)
            while (0 == key.get_value()):
                time.sleep(0.2)
            os.system('killall sample_vin_vo')
            os.system('killall sample_vin_vo')
            # Stop and close the Stream and PyAudio
            stream.stop_stream()
            stream.close()
            p.terminate()
    except Exception as e:
        print(e)
    finally:
        if test_flag:
            led0.set_value(0)
            led1.set_value(0)

    '''

    import pyaudio
    try:
        chunk = 1024      # Each chunk will consist of 1024 samples
        sample_format = pyaudio.paInt16      # 16 bits per sample
        channels = 2      # Number of audio channels
        fs = 44100        # Record at 44100 samples per second
        time_in_seconds = 300
        p = pyaudio.PyAudio()
        stream = p.open(format=sample_format,
                        channels = channels,
                        rate = fs,
                        frames_per_buffer = chunk,
                        input = True, output = True)
        for i in range(0, int(fs / chunk * time_in_seconds)):
            data = stream.read(chunk)
            stream.write(data)
    finally:
        # Stop and close the Stream and PyAudio
        stream.stop_stream()
        stream.close()
        p.terminate()

    '''
    ```


## 内置开箱应用

### IPCDemo

这是一个典型的 IPC 演示程序，对应的功能模块有：

- ISP：负责从 Sensor 获取图像 RAW 数据并转为 YUV，最终分 3 路通道输出以上信息。
- IVPS：图像视频处理模块。实现对视频图形进行一分多、Resize、Crop、旋转等功能。
- VENC / JENC：视频/JPEG 编码输出。
- Detect：支持人脸或结构化检测。
- Web 显示：实现 H264 流的 Web 传输和提供 Web 方式查看实时视频。
- RTSP 推流：实现 H264 流的 RTSP 封装以及传输。
- 录像 TF 卡存储：封装 H264 流为 MP4 格式文件并保存至 TF 卡或者 FLASH 空间。

<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=260625114&bvid=BV1me411T7g8&cid=837160730&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="max-width:640px; max-height:480px;"> </iframe>
</p>

<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=688159412&bvid=BV1p24y1d7Te&cid=837167669&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="max-width:640px; max-height:480px;"> </iframe>
</p>

#### 使用方法

>**注意**：启动命令默认的镜头型号为 **gc4653** ，因不同的摄像头配置文件不一致，使用别的型号时需点击右侧[更换摄像头](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/faq_axpi.html#Q%EF%BC%9A%E5%A6%82%E4%BD%95%E6%9B%B4%E6%8D%A2-os04a10-%E6%91%84%E5%83%8F%E5%A4%B4%EF%BC%9F)进行修改。

在终端运行下面的命令即可启动软件，服务默认绑定到 0.0.0.0 地址，直接在浏览器输入 usb0 的 IP 即可访问，使用板子上其他 IP 也可以访问页面（例如：`192.168.233.1:8080`）.

```bash
/opt/bin/IPCDemo/run.sh /opt/bin/IPCDemo/config/gc4653_config.json
```
.. details::点击查看
    输入启动命令后，终端会打印大量调试信息。
    ![ipc](./../assets/ipc.jpg)

访问页面后会弹出登录页面，点击登录后页面会弹出下图画面。

![ipc-admin](./../assets/ipc-admin.jpg)

#### 如何抓拍？如何录制？

浏览器抓拍录制（web）

- **抓拍图像**
  
软件经过上文的启动后显示画面，右下角有抓拍和录制的功能图标。
用户可点击摄像头图标进行抓拍喜欢的场景，抓拍的照片浏览器会自动弹出进行下载方便用户查看存储。

![ipc-web](./../assets/ipc-web.jpg)

- **录制视频**

点击右下角的录制图标，即可进入本地录制视频（mp4）模式，再次点击图标即录制完成结束。

![ipc-mp4](./../assets/ipc-mp4.jpg)

用户可在配置页面的`录像回放`选项预览视频进行下载到本地或删除的操作。

![ipc-config](./../assets/ipc-config.jpg)

>**注意**：
>**20221017** 后的镜像默认打开了录制保存到`/opt/mp4`的目录下。
>视频录制要储存到文件系统后才能打开，某种意义上用户也可以挂载网络路径来当监控录像使用。

#### 人脸检测
>基于上文的基础功能，IPCDemo 自身还附带其他一些功能应用.例如**：人脸检测、车牌识别**。

使用前请参考上文使用命令行登录 IPC 网页，登录后先进行相机结构化配置，具体配置流程看下文。

.. details::点击查看配置流程
    接入页面后选择**配置**在**智能配置**里再进行**结构化配置**，用户可根据自己的需要进行勾选即可。

    ![ipc-video](./../assets/ipc-video.jpg)

设置完成后回到预览页面即可进行人脸及人形识别，IPC 会自动框出识别人脸并且截取人脸的图片，可在预览页面下方点击截取图样放大查看附带信息。
- 左侧：人脸检测 右侧：人形检测
  
<html>
  <img src="./../assets/ipc-model.jpg" width=45%>
  <img src="./../assets/ipc-person.jpg" width=45%>
</html>

#### 车牌识别

使用前请参考上文基础功能使用命令行登录网页，再进行**结构化配置**勾选车牌所需的检测画框即可。

.. details::点击查看 IPC 配置流程
    接入页面后选择**配置**在**智能配置**里再进行**结构化配置**，用户可根据自己的需要进行勾选即可。

    ![ipc-video](./../assets/ipc-video.jpg)

设置完成即可回到预览页面进行车牌识别，IPC 会自动框出识别到得车牌及读取车牌数字信息，用户可在预览下方点击图片放大查看截取到车牌图片及信息。

![ipc-car](./../assets/ipc-car.jpg)

#### 人体关键点

> 这是一个基于 IPCDemo 的人体关键点开箱示例（暂未开放）

<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=773227207&bvid=BV1B14y1Y7A4&cid=837154353&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="max-width:640px; max-height:480px;"> </iframe>
</p>

### rtsp

>**rtsp**：也称实时流传输协议，该协议定义了一对多应用程序如何有效地通过 IP 网络传送多媒体数据。

**VLC Media Player**：[点击下载](https://www.videolan.org/vlc/)

使用 RTSP 传送数据前，我们需要先认识工具 `VLC Media Player`。

.. details::点我查看 VLC Media Player 介绍
    VLC Media Player（VLC 多媒体播放器），是一款可播放大多数格式，而无需安装编解码器包的媒体播放器，以及支持多平台使用、支持 DVD 影音光盘，VCD 影音光盘及各类流式协议。

    ![vl-yolov5s](./../assets/vlc-yolov5s.jpg)

运行命令后终端会弹出调试信息，打开 `VLC Media Player` 进行配置网络串流后即可看到画面效果。

```bash
/home/examples/vin_ivps_joint_venc_rtsp_vo_onvif_mp4v2/run.sh
```
 
.. details::点击查看终端运行图
    ![vlr-run](./../assets/vlc-run.jpg)

.. details::点我查看 VLC Media Player 配置步骤
    打开后在上方选择**媒体**后选择**打开网络串流**进到配置画面。
    ![vlc](./../assets/vlc.jpg)
    在网络页面输入**网络 URL ：`rtsp://192.168.233.1:8554/axstream0`**，
    勾选下方更多选项进行调整缓存后点击下方播放即可。
    ![vlc-urt](./../assets/vlc-urt.jpg)

- 双屏效果如下图示例：
  
<html>
  <img src="./../assets/rtsp-display.jpg" width=48%>
  <img src="./../assets/rtsp-axpi.jpg" width=48%>
</html>

>**注意**：默认摄像头为 os04a10 型号不同请移步[Maix-III 系列 AXera-Pi 常见问题(FAQ)](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/faq_axpi.html)更换参数。
#### ffplay

工具除了 `VCL` 还可以直接使用 `ffplay`。
**ffplay** :[点击下载](https://dl.sipeed.com/shareURL/MaixIII/AXera/09_Software_tool)

```bash
sudo apt install ffmpeg
ffplay rtsp://192.168.233.1:8554/axstream0 -fflags nobuffer
```

### ONVIF ODM

>在 **20221111** 后的更新的镜像系统，内置了按键录像 mp4 和支持更换 yolov5s 人脸/物体检测模型以及对 ODM（ONVIF）进行支持。

**ONVIF Device Manager**：[点击下载](https://sourceforge.net/projects/onvifdm/)

.. details::点击查看 ODM 软件介绍

    ONVIF 协议作为全球性的网络视频监控开放接口标准，推进了网络视频在安防市场的应用，特别是促进了高清网络摄像头的普及和运用。 越来越多的前端 IPC 厂家和后端 NVR 及存储提供商加入进来。而 ONVIF Device Manager 是 ONVIF 官方基于协议提供的免费第三方的 ONVIF 协议测试工具，与上文的 VLC 相比性能不同，但 ODM 的内容形式更加多样丰富。
    
   ![odm](./../assets/odm.jpg)

在终端运行下方命令，设备屏幕会跳出 yolov5s 模型运行画面，接着我们来配置 `ODM` 实现 PC 端显示。

>**注意**：ODM 受网络影响较大，如果有卡顿现象把网络更换成以太网即可。
>默认摄像头为 os04a10 如型号不同请移步[Maix-III 系列 AXera-Pi 常见问题(FAQ)](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/faq_axpi.html)更换参数。

.. details::点击设备运行效果图
    ![odm-mipi](./../assets/odm-mipi.jpg)

```bash
/home/examples/vin_ivps_joint_venc_rtsp_vo_onvif_mp4v2/run.sh
```

打开我们下载好的 `ODM` 软件点击左侧白框的 `Refresh` 按键扫描设备，扫描成功会显示 `IP-Camera` 方框点击后选择下方的 `Live video` 即可在 PC 端看到画面。

![odm-config](./../assets/odm-config.jpg)

还可通过下方命令去查看文件配置：

```bash
 cd /home/examples/vin_ivps_joint_venc_rtsp_vo_onvif_mp4v2/
 ls -l
```

- **更换模型**
>20221116 后更新的镜像已在 `run.sh` 内置了不同摄像头参数的源码。
>20221111 镜像内置 yolov5s 的人脸/物体检测模型，可使用以下命令更改运行脚本内容更换模型。

``` bash
nano /home/examples/vin_ivps_joint_venc_rtsp_vo_onvif_mp4v2/run.sh
```

.. details::点击查看修改操作示例
    运行后会显示 `run.sh` 的编辑页面，对当前启动的模型进行注释或调用其他模型即可，
    按 **ctrl+X** 键后会提示是否保存修改内容。
    ![model-save](./../assets/model-save.jpg)
    根据提示按下 **Y** 键保存，界面会显示修改内容写入的文件名按**回车**键确定，
    再次运行 `run.sh` 脚本即可看到模型更换成功。
    ![model-file](./../assets/model-file.jpg)
    除了上方通过命令修改 `run.sh` 更换还可以通过 `MdbaXterm` 工具查看 `/home/examples/vin_ivps_joint_venc_rtsp_vo_onvif_mp4v2/` 目录下的`run.sh`脚本文件直接修改保存。

- **按键录制 MP4**
运行 `run.sh` 期间可按下板载的按键 `user` 进行录制视频，按下后 **LED0** 会亮起代表开始录制 MP4，

.. details::点击查看按键示意图
    ![odm-mp4](./../assets/odm-mp4.jpg)

终端界面会显示下图 `delete file`，当录制完成后再次按下按键停止录制而 LED0 会灭掉，

![odm-adb](./../assets/odm-adb.png)

录制完成的 MP4 文件可在 **`home/examples/`** 目录下查看。

![mp4-file](./../assets/mp4-file.png)

### PP_human

>**20221116** 后更新的系统镜像已内置了 `pp_human` 人体分割应用。
>还内置了不同摄像头的参数命令在 `run.sh`，只需要调用注释相应源码即可使用。

运行下方的命令后终端会输出调试信息，设备屏幕会显示运行画面。

```bash
/home/examples/vin_ivps_joint_vo_pp_human_seg/run.sh
```
![pp_human](./../assets/pp_human.jpg)
可使用下方命令进入图形化页面，对 `run.sh` 里不同摄像头参数的源码进行调用或注释。

```bash
nano /home/examples/vin_ivps_joint_vo_pp_human_seg/run.sh
```

.. details::点击查看图形化页面
    修改后按 **ctrl+x** 键会进入保存页面，后续按终端提示操作即可。
    ![pp_human_adb](./../assets/pp_humana_adb.png)

### uvc_vo

**usb-uvc-gadget**：[点击查看相关仓库](https://github.com/junhuanchen/usb-uvc-gadget)

>**20221123** 镜像内置了 uvc vo 应用，并且还可以在手机端软件使用。
>目前应用还处于不稳定的状态，第一次启动程序会改变 usb otg rndis 转成 usb otg uvc 模式导致设备重启，重启再运行即可，画面绿屏是启动脚本里摄像头配置不对。

使用前需要准备两条 USB type_c  的数据线以及一条双 type_c 口的数据线。
把设备的 **UART** 及 **OTG** 口用`USB type-c` 线全部接入 `PC` 端，再运行下方命令终端会弹出无报错调试信息。

```bash
/home/examples/vin_ivps_joint_venc_uvc_vo/run.sh
```

.. details::点击查看终端示例图
    ![uvc_adb](./../assets/uvc_adb.png)

打开 `PC` 端自带相机应用即可在设备屏幕以及 `PC` 端观察到模型检测画面。

![uvc_vo](./../assets/uvc_vo.jpg)

可以使用以下的命令行更换尾缀 `start` 开启、`stop` 停止、`restore` 重启来对 `uvc` 程序进行操作。

```bash
/home/usb-uvc-gadget/uvc-gadget.sh #start/stop/restore
```

- **手机端虚拟摄像头**

UVC 也能在安卓手机端的 `app` 上当虚拟摄像头使用，使用前在软件商店下载好 **USB 摄像头专业版** 软件。

.. details::USB 摄像头专业版软件介绍
    USB 摄像头是一款支持 USB 摄像头、适配采集卡等设备通过 OTG 连接手机并驱动设备展示画面。

    ![uvc_usb](./../assets/uvc_usb.jpg)

把双头 `type-c` 线的分别接上手机端以及设备的 OTG 口，运行上方命令后会自动连接。

![uvc_phone](./../assets/uvc_phone.jpg)

>**注意**：如果需要完全脱离电脑端用手机端供电的话，需要把 uvc 程序写入开机脚本即可。

### lvgl7 UI

> 在 **20221125** 后更新的镜像系统里，我们内置了 lvgl7 UI 应用。

**运行前先准备材料**：USB type-c 线/USB type-c 转换头/无线鼠标。
使用 USB type-c 线接入设备的 **UART** 口与 **PC** 端，使用转换头将鼠标的 USB 接收器接入设备 **OTG** 口。
运行下方命令后终端会弹出无报错的启动信息后，屏幕会显示画面用户即可体验 lvgl 应用了。

```
cd /home
./bin/sample_vin_ivps_joint_vo_lvgl -c 0
```

.. details::点击查看终端示例图
    ![lvgi_adb](./../assets/lvgl_adb.png)

<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=690497396&bvid=BV1n24y1C7DN&cid=901748014&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
</p>