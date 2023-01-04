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

![mobaxterm-serial-4](./../../../../soft/maixpy3/zh/tools/assets/mobaxterm-serial-4.png)

Then click the created serial session to open the serial port to build communication.

![mobaxterm-serial-5](./../../../../soft/maixpy3/zh/tools/assets/mobaxterm-serial-5.png)

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

1. Run command `ifconfig wlan0` to see whether there is the wireless device first, if there is no wireless device, visit [AXera-Pi Q&A](./faq_axpi.md#qno-wlan0-shown-in-result-after-running-command-ifconfig) to solve this problem. And only 2.4GHz wireless network is feasible.

2. Run command `nmtui-connect` to open a wireless internet graphical interface.
![nmtui](./../../../../hardware/zh/maixIII/assets/nmtui.jpg)

3. Run command `ifconfig wlan0` to see whether there is the ip address.
![nmtui_wlan0_ifconfig](./assets/flash_system/nmtui_wlan0_ifconfig.png)

Besides, Run command `nmcli device wifi connect Sipeed_Guest password qwert123` can also connect to wireless network, change the `Sipeed_Guest` into your wireless network name and change `qwert123` into your wireless network password.

## Config System

### System time

Maix-III AXera-Pi uses the NTP protocol to update the system time. You can run the `date` command to get the current system time.

> After connecting to Internet, system will automatically run `ntpdate-debian` to update system time.

#### Change timezone

Maix-III AXera-Pi default timezone is GMT+8, you can change it with command `dpkg-reconfigure tzdata` if necessary.

![system_time_timezone](./assets/flash_system/system_time_timezone.jpg)

#### Update time

Run `ntpdate-debian` command after connectting Maix-III AXera-Pi to network to update time.

### Install software

Based in debian, we can use `apt` to install the software on Maix-III AXera-Pi. Change the software resource if you think it's slow to download the software.

Here we install `gcc`, `gparted`.

```bash
sudo apt update
sudo apt install gcc gparted
```

![install_software_gcc_gparted](./assets/flash_system/install_software_gcc_gparted.jpg)

### Reboot/Shutdown device

For Linux we suggest rebooting or shutdown device by command line instaed of by disconnecting the USB cable or click the reset key, which may destory the file system.

Run command `reboot` to restar device.

```bash
reboot
```

Run command `shutdown` to power off device.

```bash
poweroff
```

### Enlarge system memory

Run command `lsblk` to see the partition information, then resize the memory partition by command `cfdisk /dev/mmcblk2`.

![enlarge_memory_lsblk](./assets/flash_system/enlarge_memory_lsblk.jpg)

Then the following similar interface shown, and we choose `/dev/mmcblk2p2` by arrow keyboard `↑` `↓`, select the `Resize` below by arrow keyboard `←` `→`. 

![rizese-mmcblk2](./../../../zh/maixIII/assets/rizese-mmcblk2.png)

The whole free space is resized by default, and you can enter your desired memory storge.

![new-resize](./../../../zh/maixIII/assets/new-resize.png)

Enter your desired memory storge, and press Enter keyboard to save your temp change. Use arrow keyboard `←` `→` and choose `Write` to apply your change, and enter `yes` to confirm the change.

![write-disk](./../../../zh/maixIII/assets/write-disk.png)

Use arrow keyboard `←` `→` and select `Quit` to quit the storge partition.

![quit](./../../../zh/maixIII/assets/quit.jpg)

Finishing these, we run command `df -h` to see the disk space usage, and we can see that the resized memory storge is not applied, we use command `resize2fs /dev/mmcblk2p2` to change the size of `mmcblk2`, and run command `df -h` again to see the applied change.

![df-mmcblk2](./../../../zh/maixIII/assets/df-mmcblk2.jpg)

> `reboot` first if there is some trouble resizing the storge memory.

### Boot script

The boot script is in `/boot` and named `rc.local`, you can edit it if you need.

The boot script uses the root directory `/` by default, for example, if you want to run `/home/run.sh` at startup:

1. Use the absolute path to run the script background `/home/run.sh & `, if it's not running background we may bot be able to control the board by command line anymore.
2. Use the relative path to run the script background `cd /home && ./run.sh &`, note that the path is different from the absolute path.

Here is the default boot script.

```bash
root@AXERA:~# cat /boot/rc.local
```

```txt
#!/bin/sh

# this file is called by /etc/rc.local at boot.

# systemctl stop usb-gadget@g0
# mkdir -p /mnt/udisk && mount /dev/sda1 /mnt/udisk
# python3 /mnt/udisk/alltest.py

# this control lcd backlight(50 ~ 1000)
echo 0 > /sys/class/pwm/pwmchip0/export
echo 1000 > /sys/class/pwm/pwmchip0/pwm0/period
echo 500 > /sys/class/pwm/pwmchip0/pwm0/duty_cycle
echo 1 > /sys/class/pwm/pwmchip0/pwm0/enable

# wifi connect ssid Sipeed_Guest pasw qwert123
nmcli device wifi connect Sipeed_Guest password qwert123

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
  sleep 0.8 && /home/fbv-1.0b/fbv /home/res/2_480x854.jpeg && killall sample_vo_fb &
  python3 -c "import os, binascii; os.system('sed -i \'/iface eth0 inet dhcp/ahwaddress ether {}\' /etc/network/interfaces'.format(binascii.hexlify(bytes.fromhex(open('/proc/ax_proc/uid').read().split('0x')[1][:-5]),':').decode('iso8859-1'))) if os.system('grep \'hwaddress ether\' /etc/network/interfaces -q') != 0 else exit();" &
fi

exit 0
```

![start](./../../../zh/maixIII/assets/start.jpg)

From the boot script `rc.local`, we can see that `/home/res/2_480x854.jpeg` is what displayed on the screen, and you can change it if you need.

### Update kernel and driver

The first partition of system image card is mounted at `/boot` after booting, and replace the file we can update the firmware.


- `boot.bin` spl initialize file

- `uboot.bin` uboot boot file 

- `kernel.img` linux kernel

- `dtb.img` linux device tree

## Transfer file

> If you need to transfer file to AXera-Pi, here are some ways to do this.

### SD card reader

Because of the `ext4` format file system, those who use Windows/Mac can't open the file without other application, so it's only suggested to open the tf image card in Linux. And it's also a good idea to transfer by u-disk connected to the USB-OTG port on AXera-Pi.

### Connect to computer

#### Network SSH

We have told the way to login AXera-Pi by [SSH](#login-by-ssh), and with [mobaxterm](https://mobaxterm.mobatek.net/) it's really convenient to transfer files on Windows. Besides, login by ssh on [vscode](https://code.visualstudio.com/), we can transfer file by the Vscode Explorer.

![transfer_file_vscode](./assets/flash_system/transfer_file_vscode.jpg)

Besides, we can not only use mobaxterm for file transfer, but also run X11 on this software if you login by ssh. This is an example running gparted on Axera-Pi with X11 on mobaxterm.

![transfer_file_mobaxterm](./assets/flash_system/transfer_file_mobaxterm.jpg)

#### Serial communication

If you connect the board with computer by [serial port](#serial-communication), after installing the `lrzsz` application by command `apt-get install lrzsz` after AXera-Pi is connected with network, we can transfer by `minicom` on Linux or [mobaxterm](https://mobaxterm.mobatek.net/) on Windows.

## Check the peripheral

### Built in application

Maix-III AXera-Pi contains some Built-in Linux applications, and they are in `ls /opt` directory.

```bash
root@AXERA:~# ls /opt
```

```bash
bin  include  lib  scripts  share
```

And some resources are in the `/home` directory

```bash
root@AXERA:~# tree -L 1 /home
```

```bash
├── ax-samples          # npu ai sdk
|-- bin                 # Ax example applications
├── examples            # Ax example applications
├── fbv-1.0b            # fbv picture viewer
├── images              # Test pictures
├── libmaix             # simple pipeline sdk
├── models              # Built in AI models
├── res                 # Pictures and fonts
├── systemd-usb-gadget  # Config usb service
├── usb-uvc-gadget      # Config uvc service
└── ustreamer           # mjpeg application
```

We have put `gcc g++ gdb libopencv ffmpeg` into the Linux system image, with which we can compile the application on AXera-Pi.


Here is an example using libmaix：

```bash
cd /home/libmaix/examples/axpi/
python3 project.py build
fbon
./dist/start_app.sh
```

Screen displays the content of camera, if you failed running this application, visit [AXear-Pi Q&A](./faq_axpi.md) to see how to switch camera.

![libmaix](./../../../zh/maixIII/assets/libmaix.jpg)

The axsample has been compiled, and its joint models are in `/home/models/` for people to use.

```bash
/home/ax-samples/build/install/bin/ax_yolov5s -m /home/models/yolov5s.joint -i /home/images/cat.jpg -r 10
fbon
fbv yolov5s_out.jpg
```

Screen shows the yolovs_out.jpg picture file, `reboot` system if there is something occupied the system resources

![cat](./../../../zh/maixIII/assets/cat.jpg)

Run `git pull` to get the latest libmaix code.

### Pin maps

![layout_axpi](./../../../zh/maixIII/assets/layout_axpi_1.png)

### RTC

There is a RTC(Real Time Clock) on the ext-board under the Core module, which provides the read time for Maix-III AXera-Pi when not access to wireless. Use command `hwclock -w -f /dev/rtc0` to write current system time into RTC to adjust its time date.

Run command `ls /sys/class/rtc`, we can see two rtc device: `rtc0` and `rtc1`, `rtc0` is the Real Time Clock on the ext-board and `rtc1` is the AXera-Pi internal Real Time Clock.

![rtc0_data_time](./assets/flash_system/rtc0_data_time.jpg)

### CPU & RAM

Default runs at 800MHz, and can be changed into 1GHZ.

By command `ax_lookat`, we can get the values of memory.

![ax_look_at](./assets/flash_system/ax_look_at.jpg)

Set cpu at 800MHz:

```bash
root@AXERA:~# ax_lookat 0x01900000 -s 33
```

View cpu frequency:

```
root@AXERA:~# ax_clk
AX620A:
DDR:            3733 MHz
CPU:            800 MHz
BUS of VPU:     624 MHz
BUS of NPU:     624 MHz
BUS of ISP:     624 MHz
BUS of CPU:     624 MHz
NPU OTHER:      800 MHz
NPU GLB:        24 MHz
NPU FAB:        800 MHz
NPU CORE1:      800 MHz
NPU CORE0:      800 MHz
ISP:            533 MHz
MM:             594 MHz
VPU:            624 MHz
```

Set cpu at 1GHz:

```
root@AXERA:~# ax_lookat 0x01900000 -s 35
```

View cpu frequency:

```
root@AXERA:~# ax_clk
AX620A:
DDR:            3733 MHz
CPU:            1000 MHz
BUS of VPU:     624 MHz
BUS of NPU:     624 MHz
BUS of ISP:     624 MHz
BUS of CPU:     624 MHz
NPU OTHER:      800 MHz
NPU GLB:        24 MHz
NPU FAB:        800 MHz
NPU CORE1:      800 MHz
NPU CORE0:      800 MHz
ISP:            533 MHz
MM:             594 MHz
VPU:            624 MHz
```

### VIDEO

This is a demo for testing camera, visit [built in application](#built-in-applications) for more usages.

- gc4653 （Defaule camera）
- os04a10（Night enhanced camera）

```bash
sample_vin_vo -c 2 -e 1 -s 0 -v dsi0@480x854@60
```

![video](./../../../zh/maixIII/assets/video.jpg)

> Those using os04a10 visit [AXera Pi](./faq_axpi.md#qhow-to-switch-to-os04a10-camera) to see how to switch camera.

### DISPLAY

Now we use framebuffer (/dev/fb0) to control the camera content, run command `fbon` to enable the framebuffer, and `fboff` to disable the framebuffer. When `/dev/fb0` is enabled, we can display picture on the screen by command `fbv xxx.jpg`, and some pictures have been stored in `/home/res/` directory, display them by youeself.

![_home_res](./assets/flash_system/_home_res.jpg)

```
fbon                        # enable framebuffer
fbv /home/res/logo.png      # display picture
```

![fbv_logo](./../../../zh/maixIII/assets/fbv_logo.jpg)

Run command `sample_vo -v dsi0@480x854@60 -m 0` we can see there is colorbar on the screen to test the screen display, make sure you have disable the framebuffer with command `fboff`, otherwise this `sample_vo -v dsi0@480x854@60 -m 0` will not work, and use command hotkey `Ctrl` + `c` to cancel the command is you want to stop running application.

### NPU

The NPU examples is in the `/home/ax-samples/build/install` directory, just run them to see their results.

```bash
fbon
/home/ax-samples/build/install/bin/ax_yolov5s -m /home/models/yolov5s.joint -i /home/images/cat.jpg -r 10
fbv yolov5s_out.jpg
```

### AUDIO

There is a 3.5mm audio connector on AXera-Pi, we can use is to play or record audio, here are examples to test this peripheral, it's a bit loud, change the volume by `alsamixer`.

![alsamixer](./../../../zh/maixIII/assets/alsamixer.jpg)

And these are examples:

- **Test command**：`speaker-test -t sine -f 440 -c1`
- **Play audio**：`aplay /home/res/boot.wav`
- **Record audio**: `arecord test.wav -c 2 -d 2`

And this is a python example to record and play the audio.

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

### USB

There is a USB-OTG port on AXera-Pi, we can change its function to be a OTG device or HOST device.

#### USB OTG RNDIS

We set this function as the default function of USB-OTG port, with this we can see there is a usb RNDIS divice in the device manager and we can login to AXera-Pi by SSH with ip `192.168.233.1` if connecting computer with AXera-Pi via its USB-OTG port. [Click me](#rndis) to know how to login with RNDIS.

![ssh-usb](./../../../zh/maixIII/assets/ssh-usb.jpg)

The system enable amd start this service by command `systemctl enable usb-gadget@g0` and `systemctl start usb-gadget@g0`, run command `systemctl disable usb-gadget@g0` to disable this service or command `systemctl stop usb-gadget@g0` to stop this service, by stopping this we can use this USB-OTG port for other function, we'll tell these in the following content.

#### USB HOST Device

Stop the RNDIS service with command `systemctl stop usb-gadget@g0`, then run command `systemctl start usb-gadget@g1` to set the USB-OTG port as the HOST function, connect a USB device with the USB-OTG port, run command `lsusb` to check the usb device.

Here are the example logs(To read a usb storge device and mount it on AXera-Pi).

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

#### USB OTG CAM

**usb-uvc-gadget**：[usb-uvc-gadget](https://github.com/junhuanchen/usb-uvc-gadget)

Visit [uvc_vo](#uvc_vo) to know more.

#### USB HOST CAM

By this example we can connect a USB camera to AXera-Pi USB-OTG port, and display the usb camera content in the browser, so we need to make sure AXera-Pi have connected to the network first, and we ned to get the ip address of AXera-Pi, with which we can view the usb camera content in the browser.

**Ustreamer**：[Github](https://github.com/pikvm/ustreamer)

Run following code, and open the ip address of AXera-Pi in a web browser.

```bash
/home/ustreamer/ustreamer --device=/dev/video0 --host=0.0.0.0 --port=80
```

![ustreamer_adb](./../../../zh/maixIII/assets/ustreamer_adb.png)

We have these choices: 

![ustreamer](./../../../zh/maixIII/assets/ustreamer.png)

Streamer example:

![ustreamer_snapshot](./../../../zh/maixIII/assets/ustreamer_snapshot.jpg)

- **Read USB Camera by OPENCV**

Run following python code to display the USB camera content on the screen of AXera-Pi by OPENCV

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

![opencv](./../../../zh/maixIII/assets/opencv.jpg)
![opencv_cream](./../../../zh/maixIII/assets/opencv_cream.jpg)

> Visit [AXera-Pi FAQ](./faq_axpi.md) if you have some trouble.

### GPIO

#### Read KEY input：GPIO2 21

This is the USER key on AXera-Pi.

Config the USER key first.

```bash
echo 85 > /sys/class/gpio/export            # export the USER key
echo in > /sys/class/gpio/gpio85/direction  # set the exported USER key direction
```

Get the USER key value

```bash
cat /sys/class/gpio/gpio85/value            # Get the value of USER key, 1 is unpressed and 0 is pressed
```

#### Blink a LED GPIO2 A4-68 A5-69

Export the LED IO and set its direction.

```bash
echo 68  > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio68/direction
```

Set led IO voltage value to control the LED.

```bash
echo 1 > /sys/class/gpio/gpio68/value
sleep 1
echo 0 > /sys/class/gpio/gpio68/value
sleep 1
echo 1 > /sys/class/gpio/gpio68/value
```

> Calculating Rule: GPIO2 A4 == 32 *  2 + 4 = 68

For Axera chip, GPIO0 means A IO port and GPIO2 means C IO port, and example like A4 is just a siginal.

GPIO2 A4 in AXera-Pi is GPIO C(2) 4(A4) in standard definition , and standard definition GPIOA0 means IO GPIO0A4 in AXera-Pi.

Example [gpio.h/gpio.c](https://www.cnblogs.com/juwan/p/16917802.html#gpio--pwm)

### UART

The dafault uart port of USB-UART is **ttyS0**, and the UART on the pin header is **ttyS1**, the virtual USRT is **ttyGS0**.

![uart_tty](./../../../zh/maixIII/assets/uart_tty.jpg)

Here is a `python3 pyserial` example code to test the UART on the pin header, make sure you have connect the GND on your UART-TTL with the GND on the AXera-Pi.

```python
import serial
ser = serial.Serial('/dev/ttyS1', 115200, timeout=1)
ser.write(b'hello world\n')
ser.close()
```

Example [ uart.h/uart.c ](https://www.cnblogs.com/juwan/p/16917802.html#linux-uart-ttysx)

### PWM

Here we change the brightness of the screen of AXera-Pi to test the pwm example
**Example**：Run command `echo 204 > /sys/class/pwm/pwmchip0/pwm0/duty_cycle` and the screen is only one-tenth of the original brightness.

```bash
echo 0 > /sys/class/pwm/pwmchip0/export
echo 4167 > /sys/class/pwm/pwmchip0/pwm0/period
echo 204 > /sys/class/pwm/pwmchip0/pwm0/duty_cycle
echo 2084 > /sys/class/pwm/pwmchip0/pwm0/duty_cycle
echo 0 > /sys/class/pwm/pwmchip0/pwm0/enable
```

PWM Example：[Click me](https://wiki.sipeed.com/soft/maixpy3/zh/usage/hardware/PWM.html#%E5%BC%80%E5%A7%8B).

### I2C

> The I2C on the pin header is `/dev/i2c-7` in AXera-Pi, we use command `i2cdetect` to check the i2c device.

![i2c_detect](./assets/flash_system/i2c_detect.jpg)

The `i2c-0`, `i2c-1`, `i2c-2` are the camera interface, and `i2c-7` is the connector on pin header, `i2c-8` is the RTC clock, and `i2c-9` is reserved.

![i2c_dev](./assets/flash_system/i2c_dev.jpg)

For example wo use command `i2cdetect -y 0` to see the device on i2c bus.

If you can't detect your i2c device, make sure you have pull up the data line.

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
```

The **0x21** 和 **0x36** in the log means there is a i2c device connecting to the `/dev/i2c-0` connector, and we can use command `i2cget` to read the data of the i2c device or command `i2cset` to write the i2c device.

### SPI

### CHIP ID

Get the unique chip id of the main chip.

```bash
cat /proc/ax_proc/uid
```

### ADC

### Factory test script

.. details::This is the factory test python script
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


## Built in applications

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
输入启动命令后，终端会打印大量调试信息。
![ipc](./../../../zh/maixIII/assets/ipc.jpg)

访问页面后会弹出登录页面，点击登录后页面会弹出下图画面。

![ipc-admin](./../../../zh/maixIII/assets/ipc-admin.jpg)

#### 如何抓拍？如何录制？

浏览器抓拍录制（web）

- **抓拍图像**
  
软件经过上文的启动后显示画面，右下角有抓拍和录制的功能图标。
用户可点击摄像头图标进行抓拍喜欢的场景，抓拍的照片浏览器会自动弹出进行下载方便用户查看存储。

![ipc-web](./../../../zh/maixIII/assets/ipc-web.jpg)

- **录制视频**

点击右下角的录制图标，即可进入本地录制视频（mp4）模式，再次点击图标即录制完成结束。

![ipc-mp4](./../../../zh/maixIII/assets/ipc-mp4.jpg)

用户可在配置页面的`录像回放`选项预览视频进行下载到本地或删除的操作。

![ipc-config](./../../../zh/maixIII/assets/ipc-config.jpg)

>**注意**：
>**20221017** 后的镜像默认打开了录制保存到`/opt/mp4`的目录下。
>视频录制要储存到文件系统后才能打开，某种意义上用户也可以挂载网络路径来当监控录像使用。

#### 人脸检测
>基于上文的基础功能，IPCDemo 自身还附带其他一些功能应用.例如**：人脸检测、车牌识别**。

使用前请参考上文使用命令行登录 IPC 网页，登录后先进行相机结构化配置，具体配置流程看下文。

.. details::点击查看配置流程
    接入页面后选择**配置**在**智能配置**里再进行**结构化配置**，用户可根据自己的需要进行勾选即可。

    ![ipc-video](./../../../zh/maixIII/assets/ipc-video.jpg)

设置完成后回到预览页面即可进行人脸及人形识别，IPC 会自动框出识别人脸并且截取人脸的图片，可在预览页面下方点击截取图样放大查看附带信息。
- 左侧：人脸检测 右侧：人形检测
  
<html>
  <img src="./../../../zh/maixIII/assets/ipc-model.jpg" width=45%>
  <img src="./../../../zh/maixIII/assets/ipc-person.jpg" width=45%>
</html>

#### 车牌识别

使用前请参考上文基础功能使用命令行登录网页，再进行**结构化配置**勾选车牌所需的检测画框即可。

.. details::点击查看 IPC 配置流程
    接入页面后选择**配置**在**智能配置**里再进行**结构化配置**，用户可根据自己的需要进行勾选即可。

    ![ipc-video](./../../../zh/maixIII/assets/ipc-video.jpg)

设置完成即可回到预览页面进行车牌识别，IPC 会自动框出识别到得车牌及读取车牌数字信息，用户可在预览下方点击图片放大查看截取到车牌图片及信息。

![ipc-car](./../../../zh/maixIII/assets/ipc-car.jpg)

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

    ![vl-yolov5s](./../../../zh/maixIII/assets/vlc-yolov5s.jpg)

运行命令后终端会弹出调试信息，打开 `VLC Media Player` 进行配置网络串流后即可看到画面效果。

```bash
/home/examples/vin_ivps_joint_venc_rtsp_vo_onvif_mp4v2/run.sh
```
 
.. details::点击查看终端运行图
    ![vlr-run](./../../../zh/maixIII/assets/vlc-run.jpg)

.. details::点我查看 VLC Media Player 配置步骤
    打开后在上方选择**媒体**后选择**打开网络串流**进到配置画面。
    ![vlc](./../../../zh/maixIII/assets/vlc.jpg)
    在网络页面输入**网络 URL ：`rtsp://192.168.233.1:8554/axstream0`**，
    勾选下方更多选项进行调整缓存后点击下方播放即可。
    ![vlc-urt](./../../../zh/maixIII/assets/vlc-urt.jpg)

- 双屏效果如下图示例：
  
<html>
  <img src="./../../../zh/maixIII/assets/rtsp-display.jpg" width=48%>
  <img src="./../../../zh/maixIII/assets/rtsp-axpi.jpg" width=48%>
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
    
   ![odm](./../../../zh/maixIII/assets/odm.jpg)

在终端运行下方命令，设备屏幕会跳出 yolov5s 模型运行画面，接着我们来配置 `ODM` 实现 PC 端显示。

>**注意**：ODM 受网络影响较大，如果有卡顿现象把网络更换成以太网即可。
>默认摄像头为 os04a10 如型号不同请移步[Maix-III 系列 AXera-Pi 常见问题(FAQ)](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/faq_axpi.html)更换参数。

.. details::点击设备运行效果图
    ![odm-mipi](./../../../zh/maixIII/assets/odm-mipi.jpg)

```bash
/home/examples/vin_ivps_joint_venc_rtsp_vo_onvif_mp4v2/run.sh
```

打开我们下载好的 `ODM` 软件点击左侧白框的 `Refresh` 按键扫描设备，扫描成功会显示 `IP-Camera` 方框点击后选择下方的 `Live video` 即可在 PC 端看到画面。

![odm-config](./../../../zh/maixIII/assets/odm-config.jpg)

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
    ![model-save](./../../../zh/maixIII/assets/model-save.jpg)
    根据提示按下 **Y** 键保存，界面会显示修改内容写入的文件名按**回车**键确定，
    再次运行 `run.sh` 脚本即可看到模型更换成功。
    ![model-file](./../../../zh/maixIII/assets/model-file.jpg)
    除了上方通过命令修改 `run.sh` 更换还可以通过 `MdbaXterm` 工具查看 `/home/examples/vin_ivps_joint_venc_rtsp_vo_onvif_mp4v2/` 目录下的`run.sh`脚本文件直接修改保存。

- **按键录制 MP4**
运行 `run.sh` 期间可按下板载的按键 `user` 进行录制视频，按下后 **LED0** 会亮起代表开始录制 MP4，

.. details::点击查看按键示意图
    ![odm-mp4](./../../../zh/maixIII/assets/odm-mp4.jpg)

终端界面会显示下图 `delete file`，当录制完成后再次按下按键停止录制而 LED0 会灭掉，

![odm-adb](./../../../zh/maixIII/assets/odm-adb.png)

录制完成的 MP4 文件可在 **`home/examples/`** 目录下查看。

![mp4-file](./../../../zh/maixIII/assets/mp4-file.png)

### PP_human

>**20221116** 后更新的系统镜像已内置了 `pp_human` 人体分割应用。
>还内置了不同摄像头的参数命令在 `run.sh`，只需要调用注释相应源码即可使用。

运行下方的命令后终端会输出调试信息，设备屏幕会显示运行画面。

```bash
/home/examples/vin_ivps_joint_vo_pp_human_seg/run.sh
```
![pp_human](./../../../zh/maixIII/assets/pp_human.jpg)
可使用下方命令进入图形化页面，对 `run.sh` 里不同摄像头参数的源码进行调用或注释。

```bash
nano /home/examples/vin_ivps_joint_vo_pp_human_seg/run.sh
```

.. details::点击查看图形化页面
    修改后按 **ctrl+x** 键会进入保存页面，后续按终端提示操作即可。
    ![pp_human_adb](./../../../zh/maixIII/assets/pp_humana_adb.png)

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
    ![uvc_adb](./../../../zh/maixIII/assets/uvc_adb.png)

打开 `PC` 端自带相机应用即可在设备屏幕以及 `PC` 端观察到模型检测画面。

![uvc_vo](./../../../zh/maixIII/assets/uvc_vo.jpg)

可以使用以下的命令行更换尾缀 `start` 开启、`stop` 停止、`restore` 重启来对 `uvc` 程序进行操作。

```bash
/home/usb-uvc-gadget/uvc-gadget.sh #start/stop/restore
```

- **手机端虚拟摄像头**

UVC 也能在安卓手机端的 `app` 上当虚拟摄像头使用，使用前在软件商店下载好 **USB 摄像头专业版** 软件。

.. details::USB 摄像头专业版软件介绍
    USB 摄像头是一款支持 USB 摄像头、适配采集卡等设备通过 OTG 连接手机并驱动设备展示画面。

    ![uvc_usb](./../../../zh/maixIII/assets/uvc_usb.jpg)

把双头 `type-c` 线的分别接上手机端以及设备的 OTG 口，运行上方命令后会自动连接。

![uvc_phone](./../../../zh/maixIII/assets/uvc_phone.jpg)

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
    ![lvgi_adb](./../../../zh/maixIII/assets/lvgl_adb.png)

<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=690497396&bvid=BV1n24y1C7DN&cid=901748014&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
</p>