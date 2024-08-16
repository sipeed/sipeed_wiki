---
title: System Overview
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2024-8-14
    version: v0.1
    author: BuGu
    content:
      - Release docs
---

## Firmware (Image) and Applications (APP)

The NanoKVM application runs on a modified LicheeRV Nano [firmware](https://github.com/sipeed/NanoKVM/releases). You can check the version numbers of both the image and the application on the webpage -> `Settings` -> `About`.

+ Application updates include new features and bug fixes for the KVM, which can be updated directly through the webpage and are pushed frequently.
+ Firmware updates include major system features and hardware adaptations. These need to be downloaded from GitHub and re-flashed onto the SD card, and are pushed less frequently.

> The NanoKVM image is built on the LicheeRV Nano SDK and MaixCDK. It can use LicheeRV Nano resources, but LicheeRV Nano or other SG2002 products cannot use the KVM software. If you want to build HDMI input-related applications on NanoKVM, please contact us for technical support.

## Open Source Repository

+ NanoKVM frontend is now open source, and the backend will be open-sourced soon (after the GitHub repository reaches 2K stars).
+ [NanoKVM Open Source Repository](https://github.com/sipeed/NanoKVM)

## Firmware Version Information

The Full version of NanoKVM includes KVM-A/B boards. There are hardware differences between early beta versions and official versions.

+ Firmware version 1.2.0 and above supports both beta and official versions.
+ Firmware versions 1.1.0 and 1.0.0 only support the beta version hardware.

The latest firmware includes more system features and ensures support for different hardware. To ensure all functions are available, please use the latest firmware.

## Image Compilation

The NanoKVM image is based on the [LicheeRV Nano SDK](https://github.com/sipeed/LicheeRV-Nano-Build) and is built using Buildroot.

Image modification Todo

## PiKVM Support Coming Soon