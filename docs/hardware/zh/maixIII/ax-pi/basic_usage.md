---
title: Maix-III AXera-Pi 系统基础使用

---

基于上文的烧录系统后，本文介绍使用 Maix-III AXera-Pi 开发板的 Linux debian11 系统基础使用方法。

## 系统登录

### 登录方式

Maix-III AXera-Pi 开发板的 Linux debian11 系统默认使用 root 用户登录，密码为 `root`，目前板子插上电脑通电启动后支持以下登录 Linux 系统方式：

> 由于板子功耗要求低，可以不用外接 2A 电源即可使用 usb3.0 1a 启动 linux 系统。

- 有线 串口 serial 登陆

连接板子上的 usb uart 需要先安装串口驱动，再使用 mobaxterm 即可链接板子。

如下图操作步骤：

> 串口通常只提供给专业的驱动开发工程师调试用，会打印大量的调试信息，如感到不适请使用 ssh 登陆。

- 基于 ip + ssh 登录

系统默认开启了 usb rndis 虚拟以太网，可以透过有线 usb otg 口连接 usb0 网卡的 ip 192.168.233.1 后使用 ssh 登陆到 linux 系统。

rndis 在 Linux 和 Windows 下免驱，而 macos 需要额外安装驱动，Windows 需要勾选驱动，配置一下网络优先级即可。

如下配置图（勾选微软 rndis 驱动，设置网络跃点数调整优先级。）：

想要无线连接 ssh 需要先登陆板子通过 ifconfig 得到板子到 ip 后即可连接。

如下图的 IP 地址都可以用于登陆板子：

> 使用 mobaxterm 进行 ssh 登陆板子可以直接编辑板子内的代码或者执行命令，爷可以很方便的拖拽文件上传或下载到电脑里，类似的工具还有 vscode remote 远程登录 linux 服务器。（附图）

### 登录后

登录后，可以使用 `ls` 命令查看当前目录下的文件，使用 `cd` 命令切换目录，使用 `pwd` 命令查看当前目录。

## 系统配置

### 网络配置

Maix-III AXera-Pi 开发板的 Linux 系统默认使用 DHCP 协议获取 IP 地址，可以使用 `ifconfig` 命令查看当前网络配置。

板子根据下述配置会四种网卡：

```bash
root@AXERA:~# cat /etc/network/interfaces
# interfaces(5) file used by ifup(8) and ifdown(8)
# Include files from /etc/network/interfaces.d:
source /etc/network/interfaces.d/*

auto lo
iface lo inet loopback

# auto eth0
allow-hotplug eth0
iface eth0 inet dhcp

# auto usb0
allow-hotplug usb0
iface usb0 inet static
address 192.168.233.1
netmask 255.255.255.0

# allow-hotplug wlan0
# wpa-ssid "dalaoshu"
# wpa-psk "junhuanchen"
auto wlan0
iface wlan0 inet manual
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
iface wlan0 inet dhcp
```

可以使用 ifconfig 查看所有网卡信息。

```bash
root@AXERA:~# ifconfig 
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.0.77  netmask 255.255.255.0  broadcast 192.168.0.255
        ether 1e:09:dc:e9:1c:29  txqueuelen 1000  (Ethernet)
        RX packets 301  bytes 41433 (40.4 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 31  bytes 2970 (2.9 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 56  

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 16  bytes 1064 (1.0 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 16  bytes 1064 (1.0 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

usb0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.233.1  netmask 255.255.255.0  broadcast 192.168.233.255
        ether 02:da:9b:e4:a8:7f  txqueuelen 1000  (Ethernet)
        RX packets 121  bytes 15220 (14.8 KiB)
        RX errors 0  dropped 15  overruns 0  frame 0
        TX packets 35  bytes 7258 (7.0 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.0.112  netmask 255.255.255.0  broadcast 192.168.0.255
        ether 0c:cf:89:32:c5:c0  txqueuelen 1000  (Ethernet)
        RX packets 950  bytes 154305 (150.6 KiB)
        RX errors 0  dropped 950  overruns 0  frame 0
        TX packets 5  bytes 1398 (1.3 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

- lo: local的简写，一般指本地环回接口。

- eth0：有线网卡，使用 DHCP 协议获取 IP 地址，可以使用 `ifconfig eth0` 命令查看当前网络配置。

支持千兆网络，只需要开机前将网线插上去，启动过程中就会自动配置并联网，可以通过 `apt update` 测试软件源更新。

- wlan0：无线网卡，使用 DHCP 协议获取 IP 地址，可以使用 `ifconfig wlan0` 命令查看当前网络配置。

默认 WIFI 账号密码配置存放在 `wpa_supplicant.conf` 里，测试过支持 Android 手机开放的 WPA-PSK2 热点。

```bash
root@AXERA:~# cat /etc/wpa_supplicant/wpa_supplicant.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="Sipeed_Guest"
    key_mgmt=WPA-PSK
    psk="qwert123"
}
```

账号密码修改后可以重启后生效，手工操作则需要了解 iwconfig 和 iwlist 命令管理 wifi 网卡，例如 WIFI 扫描方法 iwlist wlan0 scanning，手动连接热点 `iwconfig wlan0 essid "xxxxx" iwconfig wlan0 ap auto` 。

```
root@AXERA:~# iwlist wlan0 scanning
wlan0     Scan completed :
          Cell 01 - Address: 58:41:20:05:07:96
                    ESSID:"Sipeed_Guest"
                    Protocol:IEEE 802.11bgn
                    Mode:Master
                    Frequency:2.412 GHz (Channel 1)
                    Encryption key:on
                    Bit Rates:300 Mb/s
                    Extra:wpa_ie =dd160050f20101000050f20401000050f20401000050f202
                    IE: WPA Version 1
                        Group Cipher : CCMP
                        Pairwise Ciphers (1) : CCMP
                        Authentication Suites (1) : PSK
                    Extra:rsn_ie =30140100000fac040100000fac040100000fac020000
                    IE: IEEE 802.11i/WPA2 Version 1
                        Group Cipher : CCMP
                        Pairwise Ciphers (1) : CCMP
                        Authentication Suites (1) : PSK
                    Quality=100/100  Signal level=100/100  
                    Extra:fm =0003
          Cell 02 - Address: 0C:3A:FA:0E:81:7F
                    ESSID:""
                    Protocol:IEEE 802.11bgn
                    Mode:Master
                    Frequency:2.412 GHz (Channel 1)
                    Encryption key:off
                    Bit Rates:144 Mb/s
                    Quality=100/100  Signal level=88/100  
                    Extra:fm =0001
          Cell 03 - Address: 64:64:4A:88:7F:06
                    ESSID:"Reachintelligent"
                    Protocol:IEEE 802.11bgn
                    Mode:Master
                    Frequency:2.412 GHz (Channel 1)
                    Encryption key:on
                    Bit Rates:144 Mb/s
                    Extra:rsn_ie =30140100000fac040100000fac040100000fac020c00
                    IE: IEEE 802.11i/WPA2 Version 1
                        Group Cipher : CCMP
                        Pairwise Ciphers (1) : CCMP
                        Authentication Suites (1) : PSK
                    IE: Unknown: DD7B0050F204104A0001101044000102103B00010310470010876543219ABCDEF0123464644A887F04102100067869616F6D69102300045241373210240004303030321042000531323334351054000800060050F20400011011000C5869616F4D69526F75746572100800020000103C0001031049000600372A000120
                    Quality=100/100  Signal level=100/100  
                    Extra:fm =0003

```

- usb0：USB 虚拟网卡，使用静态 IP 地址（192.168.233.1），这里已经为其配置了 dhcp 服务，从而避免了用户手动设置 IP 地址的操作。

usb0 网卡 rndis 驱动安装参考[这篇 Ghost系列USB网卡（RNDIS) 使用教程](https://www.foream.com/wiki/docs/mindoc/mindoc-1b2er0dm4pos9)，其中在 win10 则如下图。

[图片]

[图片]

连接方法看下图：USB 网卡会自动 DHCP 配置，直接连接 192.168.233.1 即可。
在 Windows 系统下如果遇到多个网卡的时候，会发现 USB 网卡优于局域网导致内网网站访问很慢甚至是失败，此时需要通过Win10如何设置跃点数来调整网络优先级连接顺序修改优先级，数值越大优先级越低（比如设置 1000），从而把 USB 网卡优先级调至最低。

[图片]

目前所有的网络配置都会在重启后自动生效，如果想自己手工控制网卡的开关，请了解一下 ifup 或 ifdown 命令的用法， 类似 `ifup eth0` 启动 eth0 网卡，`ifdown eth0 --force` 强制关闭 eth0 网卡。

## 系统更新

### 系统时间

Maix-III AXera-Pi 开发板的 Linux 系统默认使用 NTP 协议获取系统时间，可以使用 `date` 命令查看当前系统时间。

> 如果联网了会自动使用 `ntp-debian` 同步时间，没有同步则说明没有网络，没有同步 `apt update` 更新软件也会失败。

### 安装软件

Maix-III AXera-Pi 开发板的 Linux 系统可以通过 `apt` 更新软件。

比如 安装 gcc gdb ffmpeg 等常用 linux 软件，只需要使用下述命令即可。

```bash
sudo apt update
sudo apt install gcc gdb ffmpeg
```

其他软件安装亦如此。

由于 linux 系统直接断电可能会导致文件系统损坏，如果有条件建议按下述命令的的方式进行开关机，可以避免一些系统损坏导致的奇怪问题。

### 重启系统

Maix-III AXera-Pi 开发板的 Linux 系统可以通过 `reboot` 命令重启，重启命令如下：

```bash
reboot
```

### 关闭系统

Maix-III AXera-Pi 开发板的 Linux 系统可以通过 `poweroff` 命令关闭，关闭命令如下：

```bash
poweroff
```

### 开机启动脚本

系统已经配置好 `/etc/rc.local` 开机脚本，可以在这里添加开机启动的命令，可以修改 `#!/bin/sh` 到 `exit 0` 之间的命令。

```bash
root@AXERA:~# cat /etc/rc.local 
#!/bin/sh

chmod 755 /opt/scripts/auto_load_all_drv.sh && bash /opt/scripts/auto_load_all_drv.sh > /dev/null 2>&1

# python3 /home/examples/alltest.py > /dev/null 2>&1 &

# export LD_LIBRARY_PATH=/opt/lib:LD_LIBRARY_PATH && /opt/bin/sample_vin_vo -c 2 -e 1 -s 0 -v dsi0@480x854@60

systemctl stop usb-gadget@g0

mkdir -p /mnt/udisk && mount /dev/sda1 /mnt/udisk

python3 /mnt/udisk/alltest.py

export LD_LIBRARY_PATH=/opt/lib:LD_LIBRARY_PATH && /opt/bin/sample_vo -v dsi0@480x854@60 -m 0 &

exit 0

```

注意要在命令后使用 & 将程序挂在后台执行喔！

### 更新内核与驱动

在 SD 卡的第一分区会挂载到系统根目录下的 /boot 系统启动相关的文件，这里直接替换它即可完成更新。

- boot.bin 芯片 spl 初始化程序

- uboot.bin uboot 启动引导程序

- kernel.img linux 内核

- dtb.img linux 设备树

20221001 版本的内核与驱动已经发布，可以挂载镜像从第一分区获取相关文件后替换到 SD 卡的 /boot 目录下，目前 linux 底层还未开源，未来会逐步开源。

## 内置开箱应用

IPCDEMO（商业 ipc 应用）

介绍

提供人脸识别、车牌识别开箱即用的

`/opt/bin/IPCDemo/run.sh /opt/bin/IPCDemo/config/gc4653_config.json`

附图：

效果视频

- https://www.bilibili.com/video/BV1me411T7g8
- https://www.bilibili.com/video/BV1p24y1d7Te

SKEDEMO（暂未开放）

介绍

附图：

效果视频 https://www.bilibili.com/video/BV1B14y1Y7A4

## 系统外设验证

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

附图：

### VIDEO

目前系统的摄b像头驱动不经过 v4l2 驱动框架，所以必须通过代码配置的方式进行启用，相关摄像头驱动都是在应用层上完成的。

- gc4653 （基础版）
- os04a10（夜视版）

目前默认使用的是 gc4653 ，使用 os04a10 需要改一下 -c 2 为 -c 0，如下示意。

```bash
sample_vin_vo -c 0 -e 1 -s 0 -v
```

即可看到效果。

### DISPLAY

目前系统默认使用的是最简单的 framebuffer 显示驱动（/dev/fb0），在系统里内置了 fbon / fboff / fbv xxx.jpg 三个命令负责管理 fb 设备的启用和现实。

```bash

```

附图：

想要使用 libdrm 需要搭配代码使用，请参考 sdk 源码实现，目前系统还未移植好 gpu 驱动，无法使用 modetest 进行测试。

测试屏幕打彩条验证屏幕好坏可以用：`sample_vo -v dsi0@480x854@60 -m 0`，在使用前务必调用 fboff 关闭 fb 设备。

附图：

### NPU



### AUDIO

### USB

### GPIO·

### UART

### I2C

### SPI

### ADC（暂未支持）

### PWM

