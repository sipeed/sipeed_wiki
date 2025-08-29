---
title: Introduction
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, ARM, tool, PCIe
update:
  - date: 2025-8-25
    version: v0.1
    author: BuGu
    content:
      - Release docs
---

## Introduction

NanoKVM Pro is the continuation of NanoKVM, inheriting the extreme compactness and powerful expandability of the NanoKVM series as an IP-KVM product. It has made a significant leap in performance, making it more suitable for remote working scenarios.

To meet different user needs, NanoKVM Pro offers two forms: NanoKVM-Desk and NanoKVM-ATX:

![](./../../../assets/NanoKVM/pro/introduce/combine.png)

NanoKVM-Desk is the desktop version of NanoKVM Pro, featuring an anodized matte metal shell. The front panel has a 1.47-inch touchscreen that displays core KVM information and allows for easy hardware function settings or can be used as a mini secondary screen, providing a more tactile user experience with the left-side infinite knob.

NanoKVM-ATX is the internal version of NanoKVM Pro, equipped with half-height/full-height brackets for installation inside a case. It allows for easier installation for host users with built-in USB cables and power control interfaces. Remote control can be achieved via external HDMI, network, and USB connections.

NanoKVM Pro uses the AX630 as its main control core, featuring an ARM 1.2G dual-core A53 CPU. The external 1GB LPDDR4 memory provides strong computing support for remote desktop connections. It has built-in HDMI loop-out and capture chips, offering up to 4K60FPS HDMI loop-out and 4K45FPS video capture. Thanks to AX630's efficient and powerful image processing architecture, NanoKVM-Pro can transmit high-resolution images with very low latency, with typical delays as low as 60ms at 2K resolution.

The IP-KVM series products are hardware add-ons for remote desktops, capturing images via HDMI, synchronizing images and keyboard/mouse operations in real time over the network, and simulating keyboard/mouse control of the computer. Since this entire process does not require host software and is completely implemented by external hardware, NanoKVM can achieve BIOS-level control of the host, making it widely applicable in scenarios such as remote power on/off, multi-system switching, BIOS configuration, and remote installation.

Due to its upgraded powerful performance, NanoKVM Pro not only provides reliable support for temporary maintenance but also excels in the remote working field due to its low-latency and high-resolution characteristics. We will continue to upgrade the software of NanoKVM Pro, offering more convenient automation/MCP features and broader compatibility.

To meet different user needs, NanoKVM Pro offers optional features such as WiFi, PoE, and screen-edge synchronized LED strips. Please refer to the purchase page for related configurations and pricing.

## Specifications

| Product       | NanoKVM-Pro    | NanoKVM      | GxxKVM      | JxxKVM      |
|---------------|----------------|--------------|-------------|-------------|
| Main Control  | AX630C         | SG2002       | RV1126      | RV1106      |
| Core          | 2xA53@1.2G     | 1xC906@1.0G  | 4xA7@1.5G   | 1xA7@1.2G    |
| Memory        | 1G LPDDR4X     | 256M DDR3    | 1G DDR3     | 256M DDR3   |
| Storage       | 32G eMMC       | 32G microSD  | 8G eMMC     | 16G eMMC    |
| System        | NanoKVM+PIKVM  | NanoKVM      | GxxKVM      | JxxKVM      |
| Resolution    | 4K@45fps, 2K@95fps[4] | 1080P@60fps | 4K@30fps, 2K@60fps | 1080P@60fps |
| HDMI Loop-Out | 4K Loop-Out    | ×            | ×           | ×           |
| Video Encoding | MJPG/H264/H265[5] | MJPG/H264    | MJPG/H264   | MJPG/H264   |
| Audio Transmission | √         | ×            | √           | ×           |
| UEFI/BIOS Support | √         | √            | √           | √           |
| Simulated USB Keyboard/Mouse | √ | √          | √           | √           |
| Simulated USB ISO | √          | √            | √           | √           |
| IPMI          | √              | √            | √           | ×           |
| Wake-on-LAN (WOL) | √          | √            | √           | √           |
| WebSSH        | √              | √            | √           | √           |
| Custom Scripts | √             | √            | ×           | ×           |
| Serial Terminal | 2 Channels   | 2 Channels   | None        | 1 Channel   |
| Storage Performance | 32G eMMC 300MB/s | 32G MicroSD 12MB/s | 8G eMMC 120MB/s | 8G eMMC 60MB/s |
| Ethernet      | 1000M          | 100M         | 1000M       | 100M        |
| Internal Form Factor | Optional ATX version | Optional PCIe version | ×           | ×           |
| WiFi          | Optional WiFi6  | Optional WiFi6 | ×           | ×           |
| ATX Power Control | √          | √            | +15$        | +10$        |
| Display       | 1.47-inch 320x172 LCD<br>0.96-inch 128x64 OLED | 0.96-inch 128x64 OLED | None | 1.66-inch 280x240 |
| Additional Features | Synchronized LED effects, Smart Assistant | –        | –           | –           |
| Power Consumption | 0.6A@5V   | 0.2A@5V      | 0.4A@5V     | 0.2A@5V     |
| Power Input   | USB-C/PoE      | USB-C/PoE/PCIe | USB-C       | USB-C       |
| Dimensions     | 65x65x28mm    | 40x36x36mm   | 80x60x7.5mm | 60x6x24-30mm |

## NanoKVM-PCIe Information

+ [NanoKVM Pro Image Download (To be updated)](https://github.com/sipeed/NanoKVM-Pro/releases/latest)
+ [ATX Getting Started Guide](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM_Pro/atx_start.html)
+ [Advanced Applications](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM_Pro/extended.html)
+ [FAQ](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM_Pro/faq.html)

## Purchase Links

[Pre-sale Page](https://sipeed.com/nanokvm/pro)  
[Official Taobao Purchase Link (To be updated)]()  
[AliExpress Purchase Link (To be updated)]()  

## Product Feedback

If you encounter any issues or have suggestions during use, please provide feedback through the following channels:

+ [Github Issues](https://github.com/sipeed/NanoKVM-Pro/issues)
+ [MaixHub Forum](https://maixhub.com/discussion/nanokvm)
+ QQ Group: 703230713

> [1] In scenarios with only loop-out, the capture function can be turned off to directly loop out 4K60 images; when loop-out and capture are running simultaneously, it can achieve 4K30FPS.  
> [2] Latency may vary due to network bandwidth and nodes; the measured data comes from Sipeed Labs.  
> [3] The USB-HID interface can be wired internally in the case or connected externally; choose one.  
> [4] Due to 4K45FPS being a non-standard mode, the factory default uses 4K30+2K60; methods to unlock 4K45FPS/2K95FPS/1080P144FPS will be provided in future updates.  
> [5] Currently, the factory supports H264/MJPEG modes; future updates will provide H265 support.
