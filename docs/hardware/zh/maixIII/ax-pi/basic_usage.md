---
title: Maix-III AXera-Pi 系统基础使用

---

基于上文的烧录系统后，本文介绍使用 Maix-III AXera-Pi 开发板的 Linux debian11 系统基础使用方法。

## 准备工作

开始进行系统的调试使用之前，请先准备好所需的硬件设备，然后参考下方的接线示例正确接好后上电。

1. Maix-III AXera-Pi 开发板
2. 能出 1A 的 USB3.0 口（或是带供电的 usb hub 拓展）
3. 一张大于 8G 烧录 debian11 的镜像系统卡
4. GC4653 Sensor（自行按需求购入）
5. 5 寸 MIPI屏（自行按需求购入）

图待补充

**供电要求**：由于板子的功耗要求低，使用 usb3.0 1A 即可启动 linux 系统。

### 接线示例

注意：摄像头接线一定要十分注意！！！接反可能会烧坏板子或者是摄像头！！

**接线**：将屏幕（排线反面朝上）接入底板背面接口，组装好后翻正板子在右侧卡槽处插入镜像卡，再接入（排线反面朝上）摄像头并揭开保护盖，可参考示意图进行接线。

<html>
  <img src="./../assets/mipi.jpg" width=48%>
  <img src="./../assets/sensor.jpg" width=48%>
</html>

## 系统登录

### 登录工具

.. details::点我查看 MobaXterm 介绍

    MobaXterm 是在 Windows 下使用的全能终端管理软件，而 Linux 系统可以使用 ssh 远程被操作，使用 MobaXterm 进行 ssh 登陆板子直接编辑板内的代码或执行命令，也能方便的拖拽文件上传或下载到电脑里，类似的工具还有 vscode remote 远程登录 linux 服务器。

    ![mobaxterm_ssh](./../assets/ssh.jpg)

下载链接：[点击跳转](mobaxterm.mobatek.net/download) 分别付费与免费双版本，下载免费版本即可。
使用教程：[如何使用 MobaXterm](https://wiki.sipeed.com/hardware/zh/maixII/M2/tools/mobaxterm.html?highlight=ssh)

.. details::点我查看 vscode remote 介绍

    vscode remote 是 vscode 的一个插件，可以直接连接到远程的 linux 服务器，然后在本地编辑代码，同步到远程服务器上编译运行，这里以一台 Windows 10 的桌面计算机系统为例，只要能安装 vscode 编辑器软件计算机都行。

    ![vscode](./../assets/vscode.jpg)

下载连接：[点击跳转](https://code.visualstudio.com/)
连接教程：[如何使用 vscode remote 连接板子](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/dev_prepare.html?highlight=ssh#vscode-remote)

### 登录方式

Maix-III AXera-Pi 开发板的 Linux debian11 系统默认使用 root 用户登录。
用户名为 `root`，密码为 `root`，目前板子接入电脑端上电启动后支持以下登录 Linux 系统方式。

- **有线 串口 serial 登陆**

> 使用串口 serial 登陆前需安装 tty 转 USB 串口驱动

**Linux**：系统本身自带无需再装驱动，使用 `ls /dev/ttyUSB*` 即可看到设备号。

**Windows**：直接[点击下载 CH340 驱动](https://api.dl.sipeed.com/fileList/MAIX/tools/ch340_ch341_driver/CH341SER.EXE)安装，安装后可在`设备管理器`查看串口设备。

.. details::点我查看 CH340 驱动安装
    先打开设备管理器查看是否有 **CH340** 驱动，如无驱动的话请点击上方链接进行下载。
    ![usb-serial](./../assets/usb-serial.jpg)
    下载完成后，右键点击文件，选择**以管理员身份运行(A)**即会自动安装。
    ![install-serial](../assets/install-serial.jpg)
    安装完成，可在设备管理器端口处查看设备。
    
>[有些同学会遇到 Ubuntu22.04 CH340系列串口驱动（没有ttyUSB）问题，点此查看解决方案。](https://blog.csdn.net/qq_27865227/article/details/125538516)

.. details::点我查看 usb uart 接口示意图

    ![uart](./../assets/uart.jpg)

使用 usb 3.0 线连接板子上的 usb uart 接入电脑端，使用前请安装上文的驱动，再使用 MobaXterm 即可连接，默认串口配置为 115200、8N1（波特率115200，8位数据，无奇偶校验，1位停止位）。

**serial 登陆教程**：[点击查看](https://wiki.sipeed.com/hardware/zh/maixII/M2/tools/mobaxterm.html?highlight=ssh#%E8%BF%9E%E6%8E%A5-%E4%B8%B2%E5%8F%A3%28Serial%29)
成功连接后会打印大量调试信息，会弹出登陆账号信息，输入用户名及密码即可登陆。

![serial](./../assets/serial.jpg)

> 串口通常只提供给专业的驱动开发工程师调试用，会打印大量的调试信息，如感到不适请使用 **ssh** 登陆。

- **基于 ip + ssh 登录**

> 登录前需安装 **rndis usb** 网卡驱动

一般情况下 rndis usb 网卡驱动在 Linux 下可不用安装，在 Windows 下需要按下图手动安装系统自带驱动，而 macos 需要编译安装驱动（horndis），Windows 还需要配置一下网络优先级，勾选微软 rndis 驱动后设置网络跃点数调整优先级。

**驱动安装**：[这篇 Ghost 系列 USB 网卡（RNDIS) 使用教程](https://www.foream.com/wiki/docs/mindoc/mindoc-1b2er0dm4pos9)

**Windows 配置网络优先级**：[设置网络跃点数调整优先级](https://jingyan.baidu.com/article/358570f6bc5cfdce4724fca2.html)


.. details::点我查看 Win10 驱动安装过程

    打开设备管理器找到其他设备，选中 rndis 选择更新驱动程序，在如何搜索设备软件窗口中，选择**浏览计算机查找驱动程序软件（R）**。

    ![rndis_1](./../assets/rndis_1.jpg)
    再选择**从计算机的设备驱动程序列表中选择（L）**在硬件设备列表中往下拉，找到**网络适配器**，选中**下一步**。

    ![rndis_2](./../assets/rndis_2.jpg)
    在厂商列表中选择 **Microsoft Corporation**，右侧列表中选择 **USB RNDIS Adapter**。

    ![rndis_3](./../assets/rndis_3.jpg)

.. details::点我查看 usb otg 接口示意图

    ![otg](./../assets/otg.jpg)

系统默认开启了 usb rndis 虚拟以太网，可以透过有线 usb otg 口连接 usb0 网卡的 ip 192.168.233.1 后使用 ssh 登陆到 linux 系统。
想要无线连接 ssh 需要先登陆板子通过 `ifconfig` 得到板子 IP 后即可连接，下图的 IP 地址都能登陆板子。

![ifconfig](./../assets/ifconfig.jpg)

**ssh 连接教程**：[点击跳转](https://wiki.sipeed.com/hardware/zh/maixII/M2/tools/mobaxterm.html?highlight=ssh#%E8%BF%9E%E6%8E%A5-SSH)
按教程示例新建 ssh 会话，双击会话后会有提醒输入账号及密码，输入后按回车即可连接。

![ssh](./../assets/ssh.jpg)

### 登录后

登录后，可以使用 `ls` 命令查看当前目录下的文件，使用 `cd` 命令切换目录，使用 `pwd` 命令查看当前目录。

## 系统配置

### 网络操作基础

- **使用 ping baidu.com 测试网络**

![baidu](./../assets/baidu.jpg)

- **使用 ifconfig 查看所有网卡情况**

Maix-III AXera-Pi 开发板的 Linux 系统默认使用 DHCP 协议获取 IP 地址，可以使用命令行 `ifconfig` 查看当前网络配置，板子根据下述会配置四种网卡类型。


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
wpa-conf /boot/wpa_supplicant.conf
iface wlan0 inet dhcp
```

可以使用命令行 `ifconfig` 查看所有网卡信息。

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

- **使用 dhclient 触发 DHCP 获取 ip**

>这里以有线网卡（eth0）为例，decliient 还支持无线 WIFI（wlan0）.
使用上方 `ifconfig` 命令后，如果 eth0 的地址获取失败，可使用 `dhclient eth0` 命令触发 DHCP 获取 IP。
 
```bash
root@AXERA:~# dhclient eth0 &
[1]+  Done                    dhclient eth0
root@AXERA:~# ifconfig eth0
wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.0.136  netmask 255.255.255.0  broadcast 192.168.0.255
        ether 0c:cf:89:32:c5:dc  txqueuelen 1000  (Ethernet)
        RX packets 1284  bytes 157505 (153.8 KiB)
        RX errors 0  dropped 1274  overruns 0  frame 0
        TX packets 205  bytes 20798 (20.3 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

### USB RNDIS（usb0）配置方法

可使用静态 IP 地址 `192.168.233.1` 这里已配置好 dhcp 服务了，从而避免用户需手动设置 IP 地址的操作。

> 使用 usb0 前需要安装 rndis 驱动，可参考上文的驱动安装过程。

在 Windows 系统下如果遇到多个网卡时，发现 USB 网卡优于局域网导致内网网站访问很慢甚至失败，此时就需要通过 Win10 设置跃点数来调整网络优先级的连接顺序，去修改优先级改善访问慢的状态，数值越大优先级越低（比如设置 1000），从而把 USB 网卡优先级调至最低**可参考上文的调整网络优先级的教程**。

- **查看 usb0 网卡是否存在**

可通过 `ifconfig usb0` 命令查看 usb0 网卡或尝试 `ping 192.168.233.1` 是否能通。

```bash
root@AXERA:~# ifconfig usb0
usb0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 192.168.233.1  netmask 255.255.255.0  broadcast 192.168.233.255
        ether 16:37:cd:c6:f2:ae  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

- **在 ping 通后 192.168.233.1 即可通过 usb 线登陆到板子**

USB 网卡会自动 DHCP 配置，直接连接 192.168.233.1 即可，连接方式可参考示意图。

![ssh-usb](./../assets/ssh-usb.jpg)

### 有线以太网（eth0）配置方法

- **查看 eth0 网卡是否存在**
  
可使用 `dhclient eth0 &` 手动启动 DHCP 客户端获取 IP 地址，得到 ip 后使用 `ifconfig eth0` 命令查看当前网络配置。默认支持千兆网络，只需要开机前将网线插上去，在启动过程中就会自动配置并联网，可以通过 `apt update` 测试软件源更新。

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
```

- **一些问题排除方法，如没有 ip 如何配置**

登录后无法获取以太网地址的话，可用上文命令启动 DHCP 客户端获取 IP 地址。
或者是使用 `ifdown eth0` 关闭网卡后再使用 `ifup eth0 --force` 启动手动配置 IP。

.. details::点我查看配置示例
    ![eth0-config](./../assets/eth0-config.jpg)


### 无线 WIFI （wlan0）配置方法

- **查看 WIFI 网卡是否存在**

**wlan0**：无线网卡，使用 DHCP 协议获取 IP 地址，可使用命令 `ifconfig wlan0` 查看当前网络配置。 

- **如何修改连接的 WIFI 账号密码（会开机自动联网）**

默认 WIFI 账号密码配置存放在 `/boot/wpa_supplicant.conf` 里，测试过并支持 Android 手机开放的 WPA-PSK2 热点，配置修改后会在重启后生效。

```bash
root@AXERA:~# cat /boot/wpa_supplicant.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="Sipeed_Guest"
    key_mgmt=WPA-PSK
    psk="qwert123"
}
```

- **如何改用 mntui-connect 可视化配置** 

想要更好的命令行网络管理工具请使用 `apt-get install network-manager` 在 20221008 后的镜像已预置。

启用需要 `systemctl enable ModemManager.service` 并在 `nano /etc/NetworkManager/NetworkManager.conf` 里修改成 `：managed=true` 和注释掉 `/etc/network/interfaces` 里的 wlan0 相关配置后重启即可使用 `nmtui-connect` 进行联网，但原来的 `wpa_supplicant.conf` 里的配置会失效，禁用需要 `systemctl disable ModemManager.service` 。

> [配置 NetworkManager 参考](https://support.huaweicloud.com/bestpractice-ims/ims_bp_0026.html#section1) & [linux系统中使用nmtui命令配置网络参数（图形用户界面）](https://www.cnblogs.com/liujiaxin2018/p/13910144.html)

- **（附录）如何扫描 WIFI 热点**
  
手工操作则需要了解 iwconfig 和 iwlist 命令去管理 WIFI 网卡，例如 WIFI 扫描方法 `iwlist wlan0 scanning`，由于 iwconfig 只支持无密码和 WEP 认证的热点，所以现已不使用这个命令，仅供简单的查询热点或测试 WIFI 的好与坏。

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
>目前所有的网络配置都会在重启后自动生效，如果想要自己手工控制网卡的开关，请了解一下 ifup 或 ifdown 命令的用法，类似 ifup eth0 启动 eth0 网卡，ifdown eth0 --force 强制关闭 eth0 网卡等。


## 系统更新

### 系统时间

Maix-III AXera-Pi 开发板的 Linux 系统默认使用 NTP 协议获取系统时间，可以使用 `date` 命令查看当前系统时间。

> 如果联网了会自动使用 `ntp-debian` 同步时间，没有同步则说明没有网络，没有同步 `apt update` 更新软件也会失败。

### 安装软件

Maix-III AXera-Pi 开发板的 Linux 系统可以通过 `apt` 更新软件。
比如安装 gcc gdb ffmpeg 等常用 Linux 软件，只需要使用下述命令即可，其他软件安装也同理。

```bash
sudo apt update
sudo apt install gcc gdb ffmpeg
```

.. details::点我查看示例图

    ![apt](./../assets/apt.jpg)

> 由于 Linux 系统直接断电可能会导致文件系统损坏，如果可以的话建议按下述命令去进行开关机，可以避免一些由于直接断电系统损坏导致的奇怪问题出现。

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

>**20221013** 后更新的镜像已预置正式版本开机自启脚本

系统已经配置好 `/etc/rc.local & /boot/rc.local` 开机脚本，
Maix-III AXera-Pi 开发板上电后会自启点亮 5 寸屏幕以及耳机播放开机音乐。

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

    ```

.. details::点我查看示例图
    ![start](./../assets/start.jpg)

这里可以添加开机启动的命令，还可以修改 `#!/bin/sh` 到 `exit 0` 之间的命令。

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

**注意**：开机时的执行对象由于没有环境变量，所以不同于登录后运行的 `sample_vo -v dsi0@480x854@60 -m 0 &` 需要修改成 `export LD_LIBRARY_PATH=/opt/lib:LD_LIBRARY_PATH && /opt/bin/sample_vo -v dsi0@480x854@60 -m 0 & ` 才能开机启动，注意要在命令后使用 & 将程序挂在后台执行喔！

### 更新内核与驱动

在 SD 卡的第一分区会挂载到系统根目录下的 /boot 系统启动相关的文件，这里直接替换它即可完成更新。

- boot.bin 芯片 spl 初始化程序

- uboot.bin uboot 启动引导程序

- kernel.img linux 内核

- dtb.img linux 设备树

## 系统外设验证

### 系统预置的资源

Maix-III AXera-Pi 开发板的 Linux 系统预置了一些资源，可以通过 `ls /opt` 命令来查看。

```bash
root@AXERA:~# ls /opt
bin  include  lib  scripts  share
```

还有一些在 `home` 目录下：

```bash
root@AXERA:~# tree -L 1 /home

├── ax-samples # npu ai sdk

├── examples # 一些示例程序

├── fbv-1.0b # 图片查看器

├── images # 一些测试图片

├── libmaix # pipeline sdk

├── models # 一些 AI 模型

├── res # 一些资源

└── systemd-usb-gadget

8 directories, 0 files
```

板子已经预置了 `gcc g++ gdb libopencv ffmpeg` 等工具，可直接在板上编译运行程序。

> **注意**：使用 xxxx menuconfig 报错请移步[Maix-III 系列 AXera-Pi 常见问题（FAQ）](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/faq_axpi.html)

在 **20221001** 推出的镜像里内置了 libmaix 和 ax-sample 仓库，可以直接在 `home` 目录下找到它。
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

目前系统的摄像头驱动不经过 v4l2 驱动框架，所以必须通过代码配置的方式进行启用，相关摄像头驱动都是在应用层上完成的。

- gc4653 （基础版）
- os04a10（夜视版）

目前默认使用的是 gc4653 ，使用 os04a10 需要改一下 -c 2 为 -c 0，如下示意。

```bash
sample_vin_vo -c 2 -e 1 -s 0 -v dsi0@480x854@60
```

.. details::运行上方命令后可看到画面（示例效果）
    ![video](./../assets/video.jpg)

>使用摄像头时如有报错或者是不显示，请移步[Maix-III 系列 AXera-Pi 常见问题(FAQ)](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/faq_axpi.html)查询。

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

### RTSP

**RTSP**：也称实时流传输协议，可通过 RTSP 实现推流，该协议定义了一对多应用程序如何有效地通过 IP 网络传送多媒体数据。

>**20221019** 后更新的镜像内置了 **`/home/vin_ivps_joint_venc_rtsp_v2`** 可用于评估从摄像头运行 yolov5s 模型识别结果推流的演示效果。

运行 `yolov5s` 模型实现推流前，我们需要先认识工具 `VLC Media Player`。

**点击跳转下载**：[VLC Media Player](https://www.videolan.org/vlc/)

.. details::点我查看 VLC Media Player 介绍
    VLC Media Player（VLC 多媒体播放器），是一款可播放大多数格式，而无需安装编解码器包的媒体播放器，以及支持多平台使用、支持 DVD 影音光盘，VCD 影音光盘及各类流式协议。

    ![vl-yolov5s](./../assets/vlc-yolov5s.jpg)

>不同型号的摄像头记得修改 `-c` 后的值，具体可参考[Maix-III 系列 AXera-Pi 常见问题（FAQ）.](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/faq_axpi.html)

- **PC 端推流**

1. 可使用下文命令运行 yolov5s 模型终端会弹跳出信息。
2. 着打开我们已经下载好的 `VLC Media Player` 软件，进行配置网络串流连接获取画面进行物体检测。

```bash
cd /home/vin_ivps_joint_venc_rtsp_v2/ && ./sample_vin_ivps_joint_venc_rtsp -c 0 -m yolov5s_sub_nv12_11.joint
```
 
.. details::点击查看终端运行图
    ![vlr-run](./../assets/vlc-run.jpg)

.. details::点我查看 VLC Media Player 配置步骤
    打开后在上方选择**媒体**后选择**打开网络串流**进到配置画面。
    ![vlc](./../assets/vlc.jpg)
    在网络页面输入**网络 URL ：`rtsp://192.168.233.1:8554/axstream0`**，
    勾选下方更多选项进行调整缓存后点击下方播放即可。
    ![vlc-urt](./../assets/vlc-urt.jpg)

![vlc-yolov5s](./../assets/vlc-yolov5s.jpg)

- **双屏推流**
  
双屏推流顾名思义是基于上文的升级版，适配到 PC 端与设备屏幕双屏同时显示推流画面。

1. 可使用下文命令运行 yolov5s 模型进行 PC 端与设备屏幕双屏推流，运行后终端会弹跳出信息。
2. 接着打开我们已经下载好的 `VLC Media Player` 软件，进行配置网络串流连接获取画面进行物体检测。

```bash
cd /home/vin_ivps_joint_venc_rtsp_v2/ && ./sample_vin_ivps_joint_venc_rtsp_vo -c 0 -m ./yolov5s_sub_nv12_11.joint
```

效果图如下：
<html>
  <img src="./../assets/rtsp-display.jpg" width=48%>
  <img src="./../assets/rtsp-axpi.jpg" width=48%>
</html>



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

我们在 debian 系统上配置了 usb-gadget@g1 和 usb-gadget@g0 两个服务。

- **配置虚拟网卡 RNDIS usb0 有线 ssh 登录**

默认就会启动配置 `systemctl enable usb-gadget@g0`，停止开机启动用 `systemctl disable usb-gadget@g0`，停止服务用`systemctl stop usb-gadget@g0`。

此时使用命令 `sshpass -p root ssh root@192.168.233.1` 即可连接，账号及密码都是 root 。

![ssh-usb](./../assets/ssh-usb.jpg)

- **配置虚拟串口 /dev/ttyGS0 并转发登录接口**

停止 usb-gadget@g0 后使用 `systemctl start usb-gadget@g1` 即可看到，然后使用 `systemctl start getty@ttyGS0` 即可转发串口终端到 usb 的虚拟串口上。

![usb_tty](./../assets/usb_tty.jpg)

- **如何使用 USB HOST 读取一个 256M 的 SD 卡**
先关了 otg 的 rndis 后再 lsusb 就可以看到了。

> 系统同一个时刻只有一种 usb 设备方向，要么上 otg 模式变成串口、网卡接电脑，要么是 host 模式接鼠标键盘U盘，不能同时使用。

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

### PWM

> pwm0 被锁在屏幕背光了，目前在系统上还没有开 debugfs 或 sysfs 接口去控制。

以 pwm1 示意

```bash
echo 1 > /sys/class/pwm/pwmchip0/export
echo 4167 > /sys/class/pwm/pwmchip0/pwm1/period
echo 2084 > /sys/class/pwm/pwmchip0/pwm1/duty_cycle
echo 1 > /sys/class/pwm/pwmchip0/pwm1/enable
```

### I2C

使用 i2c-tools 工具包，可使用 i2cdetect -y 0 来查看 i2c 总线上的设备。

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

在终端运行下面的命令即可启动软件，服务默认绑定到 0.0.0.0 地址，直接在浏览器输入 usb0 的 IP 即可访问，使用板子上其他 IP 也可以访问页面。

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

>**20222017** 后的镜像默认打开了录制保存到 `/opt/mp4` 的目录下。
>**注意**：视频录制完后储存到文件系统后才能打开。某种意义上讲；用户也可以挂载一个网络路径来当监控录像使用。

#### 人脸识别
>基于上文的基础功能，IPCDemo 自身还附带其他一些功能应用.例如**：人脸识别、车牌识别**。

使用前请参考上文使用命令行登录 IPC 网页，登录后先进行相机结构化配置，具体配置流程看下文。

.. details::点击查看配置流程
    接入页面后选择**配置**在**智能配置**里再进行**结构化配置**，用户可根据自己的需要进行勾选即可。

    ![ipc-video](./../assets/ipc-video.jpg)

设置完成后回到预览页面即可进行人脸及人形识别，IPC 会自动框出识别人脸并且截取人脸的图片，可在预览页面下方点击截取图样放大查看附带信息。
- 左侧：人脸识别 右侧：人形识别
  
<html>
  <img src="./../assets/ipc-model.jpg" width=48%>
  <img src="./../assets/ipc-person.jpg" width=48%>
</html>


#### 车牌识别

使用前请参考上文基础功能使用命令行登录网页，再进行**结构化配置**勾选车牌所需的检测画框即可。

.. details::点击查看 IPC 配置流程
    接入页面后选择**配置**在**智能配置**里再进行**结构化配置**，用户可根据自己的需要进行勾选即可。

    ![ipc-video](./../assets/ipc-video.jpg)

设置完成即可回到预览页面进行车牌识别，IPC 会自动框出识别到得车牌及读取车牌数字信息，用户可在预览下方点击图片放大查看截取到车牌图片及信息。

![ipc-car](./../assets/ipc-car.jpg)


### RTSP 推流

推流：把采集阶段封包好的内容传输到服务器的过程。

进行 RTSP 推流前先需要下载工具 `VLC Media Player` 软件。

**VLC Media Player**：[点击下载](https://www.videolan.org/vlc/)
**VLC Media Player 介绍及配置流程**：[点击查看](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/basic_usage.html#RTSP)

运行下文命令后终端无报错，打开 VLC 软件参考上文配置流程进行配置，点击播放即可查看 RTSP 推流效果。

```bash
cd /home/vin_ivps_joint_venc_rtsp_v2/ && ./sample_vin_ivps_joint_venc_rtsp -c 0 -m yolov5s_sub_nv12_11.joint
```

.. details::点击查看终端运行图
    ![vlr-run](./../assets/vlc-run.jpg)

![vlc-rtsp](./../assets/vlc-rtsp.jpg)

### SKEDEMO

> 这是一个基于 IPCDemo 的人体关键点开箱示例（暂未开放）

<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=773227207&bvid=BV1B14y1Y7A4&cid=837154353&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="max-width:640px; max-height:480px;"> </iframe>
</p>

### 出厂测试脚本

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
