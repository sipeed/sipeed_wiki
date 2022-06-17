---
title: MaixII 通过 USB OTG 口连接U盘
keywords: MaixII, U盘
date: 2022-06-14
tags: MaixII, U盘
---

MaixII的USB口是用来做device连接电脑跑adb的。
但是有没有方法可以在不跑adb的时候（总不能天天跑adb吧，再说adb也可以网络跑啊）连接一些USB设备玩玩呢。

<!-- more -->

原文链接：https://bbs.sipeed.com/thread/844 有改动

## 摸索过程

MaixII dock 有两个接口，我们要更改 otg 口因此我们使用 UART口 连接电脑来更改板子设置

### 看看在那里定义了 

在 /etc/init.d/ 文件夹里面可以看到有如下的文件

```bash
root@sipeed:# ls /etc/init.d
S00mpp       S10udev      S40network   S52ntpd      log          rc.preboot
S01audio     S11dev       S41netparam  adbd         network      rcK
S01logging   S12usb       S50telnet    cron         rc.final     rcS
S02app       S20urandom   S51dropbear  fontconfig   rc.modules   sysntpd
```

注意到里面有一个 `S12usb`

使用 `cat /etc/init.d/S12usb` 查看里面内容后发现有一句 

```bash
otg_role=`cat /sys/devices/platform/soc/usbc0/otg_role`
```

抱着好奇的心态在设备上跑了这句脚本，结果如下所示：

```bash
root@sipeed:~# cat /sys/devices/platform/soc/usbc0/otg_role
usb_device
```

### 切换为 USB host

再好奇下看这个 /sys/devices/platform/soc/usbc0 目录中都有啥，结果如下：

```bash
root@sipeed:~# ls /sys/devices/platform/soc/usbc0
driver           hw_scan_debug    of_node          subsystem        usb_device       usb_null
driver_override  modalias         otg_role         uevent           usb_host
```

重点是里面的：`usb_device` `usb_host` `usb_null`

那直接把 `usb_host` echo 到 `/sys/devices/platform/soc/usbc0/otg_role` 中看看啥效果：

```bash
echo "usb_host" > /sys/devices/platform/soc/usbc0/otg_role
```

然后我们使用 `lsusb` 看看都有啥

```bash
root@sipeed:~# lsusb
Bus 001 Device 001: ID 1d6b:0002
Bus 002 Device 001: ID 1d6b:0001
```

哈，USB控制器出来了。

### 连接USB设备

想着设备内识别SD卡，那U盘应该也差不多。插个U盘试下。

```bash
root@sipeed:~# lsusb
Bus 001 Device 001: ID 1d6b:0002
Bus 001 Device 002: ID aaaa:8816
Bus 002 Device 001: ID 1d6b:0001
```

多出来一个设备，在 /dev 目录下看了下果然多出来一个sda：

```bash
root@sipeed:/# ls /dev/sda
sda   sda1  sda2
```

挂载 U盘 试试：

出现 `Read-only file system` 的话，重烧是最快的解决方法。

```bash
root@sipeed:~# mkdir -p /home/usbdisk
root@sipeed:~# mount /dev/sda2 /home/usbdisk/
root@sipeed:~# df
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/root               256512     88352    162920  35% /
tmpfs                    29864        12     29852   0% /tmp
none                     29796         0     29796   0% /dev
/dev/mmcblk0p3            2013         1      2013   0% /mnt/cfg
/dev/mmcblk0p6         2939292     59664   2863244   2% /mnt/UDISK
/dev/sda4              7926272    405644   7520628   5% /home/usbdisk
```

挂载成功。

然后，试了下无线网卡、USB串口啥的，基本都没识别出来，估计是驱动没有编译进去吧。