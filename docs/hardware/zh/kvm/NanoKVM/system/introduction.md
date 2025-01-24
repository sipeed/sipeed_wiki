---
title: 系统介绍
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2024-8-14
    version: v0.1
    author: BuGu
    content:
      - Release docs
---

## 固件（镜像）与应用（APP）

NanoKVM 应用运行在修改后的 LicheeRV Nano [固件](https://github.com/sipeed/NanoKVM/releases)上，在网页端->`设置`->`关于`中可以分别看到镜像和应用的版本号。

+ 应用更新包含了KVM的新功能和问题修复，可以在网页直接更新，推送频次较高;
+ 固件更新则包含较大的系统功能的添加和硬件的适配，需要在github下载镜像并重新烧卡，推送频次较低。

> NanoKVM 镜像在LicheeRV Nano SDK 和 MaixCDK 基础上构建，可以兼容使用 LicheeRV Nano 的资料，反之LicheeRV Nano 或其他 SG2002 产品无法使用KVM软件。如果您想在 NanoKVM 上构建 HDMI 输入相关应用，请与我们联系，以获得技术支持。

## 开源仓库

+ NanoKVM 现已开源前端，后端即将开源（github仓库满2K star）
+ [NanoKVM 开源仓库](https://github.com/sipeed/NanoKVM)

## 固件版本说明

Full 版 NanoKVM 上包含 KVM-A/B 板，早期内测版和正式版存在硬件上的区别

+ 1.2.0 及以上的固件同时支持内测版和正式版
+ 1.1.0 和 1.0.0 版本固件仅支持内测版的硬件

最新的固件有更多的系统功能，同时保证了对不同硬件的支持，为确保所有功能可用，请尽量烧录最新的固件。

## 镜像编译

NanoKVM 镜像基于 [LicheeRV Nano SDK](https://github.com/sipeed/LicheeRV-Nano-Build) ，使用 Buildroot 构建

## 镜像修改 

Todo
