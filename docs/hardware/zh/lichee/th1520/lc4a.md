---
title: LicheePi Cluster 4A
keywords: LicheePi, Sodimm, TH1520, RISCV, SBC, Cluster
update:
  - date: 2023-09-07
    version: v0.1
    author: 0x754C
    content:
      - 初次编写文档
---

# 简介

Lichee Cluster 4A （以下简称LC4A）是矽速科技研发的高性能RISC-V集群计算平台，可以用于构建多节点计算集群，而且还是学习 Kubernetes、自动化、边缘人工智能计算、本地迷你服务器，托管应用程序、容器等的优秀工具。Lichee Cluster 4A能够安装最多7个LM4A核心板，每个LM4A核心板支持4TOPS@int8 AI 算力的 NPU，单卡最大支持 16GB LPDDR4X 内存和 128G eMMC 存储，有强大的灵活性和可扩展性。

Lichee Cluster 4A 板载 1 Gbps 以太网和集成管理交换机提供高速连接，可轻松将多个节点连接在一起，并创建强大的计算集群，还包括 USB3.0 和SD卡存储扩展，可以轻松地将额外的存储和外围设备添加到集群中。


Lichee Cluster 4A 板的另一个特性是其内置的 BMC（带外管理）。该BMC独立连接了每个LM4A的系统串口，复位引脚，通过BMC可以:

1. 从硬件引脚复位节点。
2. 连接到每个Slot的串口，可以使用串口执行命令，也可以在串口上运行ser2net或kermit来管理Slot.

# 技术规格

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">支持的核心板</td>
<td class="org-left">SIPEED LM4A * 7</td>
</tr>
</tbody>
<tbody>
<tr>
<td class="org-left">CPU</td>
<td class="org-left">1.85Ghz C910 * 4 * 7</td>
</tr>
</tbody>
<tbody>
<tr>
<td class="org-left">GPU</td>
<td class="org-left">IMG™ B 系列 BXM-4-64 * 7</td>
</tr>
</tbody>
<tbody>
<tr>
<td class="org-left">NPU</td>
<td class="org-left">4TOPS@INT8 * 7</td>
</tr>
</tbody>
<tbody>
<tr>
<td class="org-left">RAM</td>
<td class="org-left">最大 16GB * 7</td>
</tr>
</tbody>
<tbody>
<tr>
<td class="org-left">EMMC</td>
<td class="org-left">最大 128GB * 7</td>
</tr>
</tbody>
<tbody>
<tr>
<td class="org-left">BMC</td>
<td class="org-left">SIPEED Lichee RV （D1  C906@1GHz，512MB DDR3）</td>
</tr>
</tbody>
<tbody>
<tr>
<td class="org-left">电源管理</td>
<td class="org-left">Sipeed M0 Sense（增加风扇调速、机箱开机键、等功能）</td>
</tr>
</tbody>
<tbody>
<tr>
<td class="org-left">ETHERNET</td>
<td class="org-left">千兆以太网1(Slot#1)</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">千兆以太网2(交换机)</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">百兆以太网(BMC)</td>
</tr>
</tbody>
<tbody>
<tr>
<td class="org-left">USB</td>
<td class="org-left">USB3.0 * 7 (LM4A)</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">USB2.0 * 1 (BMC)</td>
</tr>
</tbody>
<tbody>
<tr>
<td class="org-left">HDMI</td>
<td class="org-left">HDMI * 1 (Slot 1)</td>
</tr>
</tbody>
<tbody>
<tr>
<td class="org-left">SDCARD</td>
<td class="org-left">TF * 7</td>
</tr>
</tbody>
<tbody>
<tr>
<td class="org-left">电源支持</td>
<td class="org-left">支持DC口直流电源供电</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">支持ATX 24PIN电源</td>
</tr>
</tbody>
<tbody>
<tr>
<td class="org-left">RTC 供电</td>
<td class="org-left">CR2032 纽扣电池</td>
</tr>
</tbody>
<tbody>
<tr>
<td class="org-left">风扇</td>
<td class="org-left">5V PWM风扇接口 * 7</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">12V 4PIN PWM风扇接口 * 1</td>
</tr>
</tbody>
<tbody>
<tr>
<td class="org-left">尺寸</td>
<td class="org-left">Mini ITX, 17 * 17 cm (6.7 * 6.7 inch)</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">可选配MINI ITX机箱, 20 * 12 * 22 cm</td>
</tr>
</tbody>
</table>

# 硬件系统

## 主板介绍

![LC4A_BOARD](./assets/LC4A_BOARD.png)

## 主板框架图

![LC4A_BOARD_TOP](./assets/LC4A_BOARD_TOP.png)

LicheeRV SOM（D1 C906@1GHz）有5个原生串口，以及两个USB串口，分别独立连接到了7个SOM上。

每个LM4A的RST/BOOT均可通过模拟开关进行控制。

1号LM4A默认引出了第二千兆口和HDMI口，方便该SOM进行整个集群的任务分发操作。

主板可通过12V DC充电头供电（推荐12V9A以上），或者使用标准ATX电源供电。

## 机箱介绍

推荐选配MINI-ITX机箱，该机箱具备良好的外观和散热性能，方便计算集群的部署展示。

机箱适配MINI-ITX主板，配备250W大功率电源，并安装了12cm静音风扇散热，可以保证CPU在满载运行时的温度低于70度。

![LC4A_BOX](./assets/LC4A_BOX.png)

## 硬件安装指南

默认运输途中LC4A已经安装了所有SOM，如果你需要拆卸或者升级SOM，可以参考以下说明。

### 安装核心板

向两侧拉开白色锁扣，插入前请确认缺口为止，避免方向错误导致损坏

![LC4A_SLOT_INSTALL1](./assets/LC4A_SLOT_INSTALL1.png)

放入核心板后均匀的向下施加压力

![LC4A_SLOT_INSTALL2](./assets/LC4A_SLOT_INSTALL2.png)

听到喀哒声后，确认白色锁扣正确扣上，安装完成。如果需要取出核心板，向两侧拉开白色锁扣即可。

![LC4A_SLOT_INSTALL3](./assets/LC4A_SLOT_INSTALL3.jpeg)

### 安装BMC

安装烧录好镜像的SD卡到LicheeRV, 然后将LicheeRV的模块安装至交换机芯片旁边的座子,然后拧上螺丝.

### 插入电源

可选ATX电源供电或者DC电影供电。

确认ATX电源插座的卡扣已经扣紧，避免接触不良导致连接器升温

![LC4A_ATX_PWR_INSTALL1](./assets/LC4A_ATX_PWR_INSTALL1.png)

插上跳线帽

![LC4A_ATX_PWR_INSTALL2](./assets/LC4A_ATX_PWR_INSTALL2.png)

### 网络连接

集群系统对外主要连接两个网口：1. 板载千兆交换机网口 2. BMC网口
板载千兆交换机网口建议连接入用户所在内网或者主网络，用于集群获取所需网络数据。
BMC网口建议连入独立网络进行集群控制，更具安全性。
集群内部通过千兆交换机连接。

如何获得集群的IP地址:

预装的固件安装启用了mdns服务
在你的PC上启用avahi服务(Linux)
使用mdns扫描整个网络获得lc4a的mdns域名信息:
```
avahi-browse -art | grep lc4a
```
然后使用:
```
ssh debin@lc4aXXXX.local
```
XXXX为mac地址后四位，用于区分每个slot

# 软件系统

## LM4A镜像

集群中的LM4A SOM可以直接使用LicheePi4A的镜像.

如果需要使能USB，可以在Linux设备树中应用以下PATCH: 
https://dl.sipeed.com/fileList/LICHEE/LicheeCluster4A/lpi4a/src/linux/0001-arch-riscv-boot-dts-lpi4a-disable-i2c-io-expander-fo.patch

或者直接使用预编译镜像：https://dl.sipeed.com/shareURL/LICHEE/LicheeCluster4A/lpi4a/bin

镜像烧录方法：

1. 按下BOOT按键的同时按一下RST按键，然后使用A TO A公头的USB线缆连接到电脑

2. 使用fastboot工具烧录

## OpenBMC镜像

主板上的LicheeRV SOM运行OpenBMC来管理主板上的SOM。

镜像下载地址: https://dl.sipeed.com/shareURL/LICHEE/LicheeCluster4A/bmc/bin

镜像烧录方法:

```
bmaptool copy obmc-phosphor-image-licheepi-rv.wic.gz /dev/YOUR_SDCARD
```

默认用户名: root

默认密码:   0penBmc

0是零，不是O

如果需要开发定制，请下载PATCH:

https://dl.sipeed.com/shareURL/LICHEE/LicheeCluster4A/bmc/src

并应用到OpenBMC源码:

```
git clone https://github.com/openbmc/openbmc/
git checkout commit-id
git am xxx.patch
```

## OpenBMC管理

从SSH访问Slot的串口:

```
ssh -p 2301 root@bmcip # access first slot's serial port
```

* 端口 22: OpenBMC的shell

* 端口 2301: slot1 的 SOL (Serial Over LAN)
* 端口 2302: slot2 的 SOL
* 端口 2303: slot3 的 SOL
* 端口 2304: slot4 的 SOL
* 端口 2305: slot5 的 SOL
* 端口 2306: slot6 的 SOL
* 端口 2307: slot7 的 SOL

每个Slot的串口输出到日志:

```
cat /var/log/obmc-cons*.log
```
