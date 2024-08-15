---
title: LicheePi Cluster 3A
keywords: LicheePi, Sodimm, K1, RISCV, SBC, Cluster
update:
  - date: 2023-07-30
    version: v0.1
    author: zepan
    content:
      - Initial doc
---

## Intro

The Lichee Cluster 3A (hereinafter referred to as LC3A) is a high-performance RISC-V cluster computing platform developed by Sipeed. It can be used to build multi-node computing clusters and is an excellent tool for learning Kubernetes, automation, edge AI computing, local mini-servers, hosting applications, and containers. A single Lichee Cluster 3A can accommodate up to 7 LM3A core boards, each featuring an NPU with 2 TOPS@int8 AI computing power, supporting up to 16GB of LPDDR4X memory and 128GB of eMMC storage per core board. The entire cluster offers robust flexibility and scalability.

The Lichee Cluster 3A comes with an onboard eight-port gigabit switch to provide high-speed connections, easily linking multiple nodes to form a powerful computing cluster. It also supports USB 3.0 and SD card storage expansion, allowing for easy addition of extra storage or peripheral devices.

Additionally, the Lichee Cluster 3A is equipped with a BMC (Baseboard Management Controller) for out-of-band management. The BMC independently connects to the system serial port and reset pins of each LM3A. It can reset individual compute nodes from the hardware level and execute commands via the serial port, such as using ser2net or kermit to manage slots.

## Tech Spec

<table>
<colgroup>
<col  class="org-left" />
<col  class="org-left" />
</colgroup>
<tr>
<td class="org-left">SOMs</td>
<td class="org-left"> <a href="https://wiki.sipeed.com/lm3a">LM3A</a> * 7</td>
</tr>
<tr>
<td class="org-left">CPU</td>
<td class="org-left"><strong>RiscV X60@1.6GHz * 8</strong> * 7</td>
</tr>
<tr>
<td class="org-left">GPU</td>
<td class="org-left">IMG™ B  BXE-2-32 * 7</td>
</tr>
<tr>
<td class="org-left">NPU</td>
<td class="org-left">2TOPS@INT8 * 7</td>
</tr>
<tr>
<td class="org-left">RAM</td>
<td class="org-left">最大 16GB * 7</td>
</tr>
<tr>
<td class="org-left">EMMC</td>
<td class="org-left">Maximum 128GB * 7</td>
</tr>
<tr>
<td class="org-left">BMC</td>
<td class="org-left"><a href="https://wiki.sipeed.com/Lichee-RV">SIPEED Lichee RV</a></td>
</tr>
<tr>
<td class="org-left">Ethernet</td>
<td class="org-left">GbE 1(Slot#1)<br>GbE 2(交换机)<br>100M Ethernet(BMC)</td>
</tr>
<tr>
<td class="org-left">USB</td>
<td class="org-left">USB3.0 * 7 (LM3A)<br>USB2.0 * 1 (BMC)</td>
</tr>
<tr>
<td class="org-left">HDMI</td>
<td class="org-left">HDMI * 1 (Slot 1)</td>
</tr>
<tr>
<td class="org-left">SDCARD</td>
<td class="org-left">TF * 7</td>
</tr>
<tr>
<td class="org-left">Power</td>
<td class="org-left">support DC powerin<br>support ATX 24PIN power</td>
</tr>
<tr>
<td class="org-left">RTC </td>
<td class="org-left">CR2032 Button cell</td>
</tr>
<tr>
<td class="org-left">heat radiation</td>
<td class="org-left">5V PWM FAN * 7<br>12V 4PIN PWM FAN * 1</td>
</tr>
<tr>
<td class="org-left">Size</td>
<td class="org-left">Mini ITX, 17 * 17 cm (6.7 * 6.7 inch)<br>optional MINI ITX case, 20 * 12 * 22 cm</td>
</tr>
</table>


## Hardware system

### Motherboard introduction

![lc3a_top](./assets/lc3a/lc3a_top.png)

### Motherboard frame diagram

![lc3a_architecture](./assets/lc3a/lc3a_architecture.png)

LicheeRV SOM (D1 C906@1GHz) has 5 native serial ports and two USB serial ports, which are independently connected to 7 SOMs.

Each LM3A's RST/BOOT can be controlled via an analog switch.

LM3A No. 1 has the second Gigabit port and HDMI port by default, which facilitates the SOM to perform task distribution operations for the entire cluster.

The motherboard can be powered by a 12V DC charging head (12V9A or above recommended), or by a standard ATX power supply.

### Chassis introduction

It is recommended to choose the MINI-ITX chassis. This chassis has good appearance and heat dissipation performance, and is convenient for the deployment and display of computing clusters.

The chassis is adapted to the MINI-ITX motherboard, equipped with a 250W high-power power supply, and installed with a 12cm silent fan for heat dissipation, which can ensure that the CPU temperature is below 70 degrees when running at full load.

![lc3a_box](./assets/lc3a/lc3a_box.png)

### Hardware Installation Guide

By default, all SOMs have been installed on the LC3A during transportation. If you need to remove or upgrade the SOM, please refer to the following instructions.

#### Install core board

Pull the white lock buckle to both sides. Please confirm the gap before inserting to avoid damage caused by incorrect direction.

![lc3a_install_goldfinger](./assets/lc3a/lc3a_install_goldfinger.png)

After placing the core board, apply downward pressure evenly

![lc3a_install_install_lm3a](./assets/lc3a/lc3a_install_install_lm3a.png)

After hearing a click, confirm that the white lock is properly engaged and the installation is complete. If you need to take out the core board, just pull the white locks to both sides.

![lc3a_install_slot](./assets/lc3a/lc3a_install_slot.jpeg)

#### Install BMC

Install the burned image SD card to LicheeRV, then install the LicheeRV module to the seat next to the switch chip, and then tighten the screws.

#### Plug in power

Optional ATX power supply or DC movie power supply.

Make sure the buckle of the ATX power socket is fastened to avoid poor contact causing the connector to heat up.

![lc3a_power_atx20_cable](./assets/lc3a/lc3a_power_atx20_cable.png)

Plug in the jumper cap

![lc3a_power_jumpwire](./assets/lc3a/lc3a_power_jumpwire.png)

#### Internet connection

The cluster system mainly connects to two external network ports: 1. Onboard Gigabit switch network port 2. BMC network port
It is recommended that the onboard Gigabit switch network port be connected to the user's intranet or main network for the cluster to obtain required network data.
It is recommended that the BMC network port be connected to an independent network for cluster control, which is more secure.
The clusters are connected internally through Gigabit switches.

How to get the cluster’s IP address:

The pre-installed firmware installation has the mdns service enabled
Enable avahi service on your PC (Linux)
Use mdns to scan the entire network to obtain the mdns domain name information of lc3a:
```
avahi-browse-art | grep lc3a
```
Then use:
```
ssh debin@lc3aXXXX.local
```
XXXX is the last four digits of the mac address, used to distinguish each slot

## Software system

### LM3A Mirror

The LM3A SOM in the cluster can directly use the LicheePi3A image.

If you need to enable USB, you can apply the following PATCH in the Linux device tree: [Click here to download](https://dl.sipeed.com/fileList/LICHEE/LicheeCluster3A/04_Firmware/lpi3a/src/linux/0001-arch- riscv-boot-dts-lpi3a-disable-i2c-io-expander-fo.patch)

Or use the precompiled image directly: [Click here to download](https://dl.sipeed.com/shareURL/LICHEE/LicheeCluster3A/04_Firmware/lpi3a/bin)

Image burning method:

1. Press the BOOT button and press the RST button at the same time, then use the A to A male USB cable to connect to the computer

2. Burn using fastboot tool

### OpenBMC Image

The LicheeRV SOM on the motherboard runs OpenBMC to manage the SOM on the motherboard.

Mirror download address: [Click here to jump](https://dl.sipeed.com/shareURL/LICHEE/LicheeCluster3A/04_Firmware/bmc/bin)

Image burning method:

```
bmaptool copy obmc-phosphor-image-lichepi-rv.wic.gz /dev/YOUR_SDCARD
```

Default username: `root`

Default password: `0penBmc`

0 is zero, not O

If you need to develop customization, please download PATCH:

https://dl.sipeed.com/shareURL/LICHEE/LicheeCluster3A/04_Firmware/bmc/src

And applied to OpenBMC source code:

```
git clone https://github.com/openbmc/openbmc/
git checkout commit-id
git amxxx.patch
```

### OpenBMC Management

Access Slot's serial port from SSH:

```
ssh -p 2301 root@bmcip # access first slot's serial port
```

* Port 22: OpenBMC shell

* Port 2301: SOL (Serial Over LAN) of slot1
* Port 2302: SOL for slot2
* Port 2303: SOL for slot3
* Port 2304: SOL for slot4
* Port 2305: SOL for slot5
* Port 2306: SOL for slot6
* Port 2307: SOL for slot7

The serial port of each Slot is output to the log:

```
cat /var/log/obmc-cons*.log
```

