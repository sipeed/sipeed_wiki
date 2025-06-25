---
title: Introduction
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool, PCIe
update:
  - date: 2024/12/11
    version: v0.1
    author: BuGu
    content:
      - Release docs
---

## Introduction

![](./../../../assets/NanoKVM/introduce/NanoKVM-PCIe.png)

NanoKVM-PCIe is a new form of NanoKVM, featuring a built-in PCIe bracket that can be securely installed inside a chassis, providing a better experience for desktop users.

Based on the NanoKVM-Cube, the NanoKVM-PCIe adds optional WiFi and PoE functionality; it comes with a PCIe slot that can draw power from the motherboard's PCIe slot. In addition, the wired connection (ETH) is more stable and meets more professional requirements.

The NanoKVM series products include an HDMI input interface, which can be recognized by computers as a display to capture computer graphics. It features a USB 2.0 interface that connects to the computer host and can be recognized as HID devices such as keyboards, mice, and touchpads. It also utilizes extra storage space on the TF card, which is mounted as a USB drive. All models are equipped with a 100 Mbps Ethernet port for network transmission of video and control signals. The PCIe version of NanoKVM comes standard with a 0.49-inch OLED display to show various status information in real-time, including WiFi network configuration and other information.

> Note: The PCIe version of NanoKVM draws power only from the PCIe interface and cannot directly obtain images from the PCIe as a graphics/display device.

To meet diverse user needs, the NanoKVM-PCIe offers two optional modules for WiFi and PoE, allowing for flexible combinations during purchase.

## Use Cases

![](./../../../assets/NanoKVM/introduce/web_ui.gif)

+ **Server Management**: Used for real-time monitoring of servers, obtaining the operating status of servers, and controlling them.
+ **Remote Power&Desktop**: NanoKVM frees itself from the limitations of having the host connected to the network and dependent on system software. As an external hardware solution, it directly provides remote control functionality.
+ **Remote Installation**: NanoKVM simulates a USB drive, allowing users to mount installation images and install operating systems, as well as access BIOS settings for the computer.
+ **Remote Serial Port**: NanoKVM exposes two sets of serial ports that can work in conjunction with IPMI or connect to other development boards for web-based serial terminal interaction. Additionally, users can expand with more accessories as needed.
+ **Dual Computer Collaborative Operation**.

## Parameters

| Product              | NanoKVM (PCIe)       | NanoKVM (Full)         | PiKVM V4              |
|----------------------|----------------------|-------------------------|-----------------------|
| Computing Unit       | SG2002 (RISCV)      | LicheeRV Nano (RISCV)  | CM4 (ARM)             |
| Resolution           | 1080P @ 60fps       | 1080P @ 60fps          | 1080P @ 60fps         |
| Video Encoding       | MJPEG, H264         | MJPEG, H264            | MJPEG, H264           |
| Video Latency        | 90–230ms            | 90–230ms               | 100–230ms             |
| UEFI/BIOS            | ✓                    | ✓                       | ✓                     |
| Emulated USB Keyboard & Mouse | ✓          | ✓                       | ✓                     |
| Emulated USB Storage  | ✓                   | ✓                       | ✓                     |
| IPMI                 | ✓                    | ✓                       | ✓                     |
| Wake-on-LAN          | ✓                    | ✓                       | ✓                     |
| Tailscale            | ✓                    | ✓                       | ✓                     |
| WebSSH               | ✓                    | ✓                       | ✓                     |
| Custom Scripts       | ✓                    | ✓                       | -                     |
| ETH                  | 100M/10M            | 100M/10M               | 1000M/100M/10M        |
| PoE                  | Optional             | Only external connection | 1000M/100M/10M        |
| WiFi                 | Optional             | -                       | ✓                     |
| ATX Power Control    | Directly connects to 9Pin power header | USB interface IO control board | RJ45 interface IO control board |
| OLED Display         | 64*32 0.49" white   | 128x64 0.96" white     | 128x32 0.91" white    |
| Serial Terminal      | 2 channels           | 2 channels              | -                     |
| Micro SD Card        | Yes, ready to use on boot | Yes, ready to use on boot | Yes                  |
| Power Consumption     | 0.2A@5V            | 0.2A@5V                | Peak 2.6A@5V         |
| Power Input          | Multiple power modes | Powered by PC USB <br> Also supports additional auxiliary power | Requires DC 5V 3A power |
| Cooling              | Silent, fanless      | Silent, fanless        | Requires active cooling fan |
| Dimensions           | 66x57x18mm (without panel) | 40x36x36mm              | 120x68x44mm          |


## NanoKVM-PCIe Information

NanoKVM uses the same SOC as Sipeed [LicheeRV Nano](https://wiki.sipeed.com/hardware/zh/lichee/RV_Nano/1_intro.html). For those interested in secondary development, you can find more information [here](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/development.html).

The NanoKVM Cube/PCIe software is now fully open source: [KVM Application Open Source Location](https://github.com/sipeed/NanoKVM), [Image Open Source Location](https://github.com/sipeed/LicheeRV-Nano-Build/tree/NanoKVM).

> The NanoKVM image is built on the LicheeRV Nano SDK and MaixCDK, allowing compatibility with LicheeRV Nano resources. Conversely, the LicheeRV Nano or other SG2002 products cannot utilize KVM software. If you wish to develop HDMI input-related applications on NanoKVM, please contact us for technical support.

NanoKVM-Cube and NanoKVM-PCIe share the same image and applications, automatically adapting to different hardware versions.

+ [Download NanoKVM Image](https://github.com/sipeed/NanoKVM/releases)

## Purchase Links

[Official Taobao Store]()(To be updated)
[AliExpress Store]()(To be updated)
[Pre-sale Page](https://sipeed.com/nanokvm/pcie)

## Product Feedback

If you encounter any issues or have suggestions, please contact us through the following channels:

+ [Github Issues](https://github.com/sipeed/NanoKVM)
+ [MaixHub Forum](https://maixhub.com/discussion/nanokvm)
+ QQ Group: 703230713

