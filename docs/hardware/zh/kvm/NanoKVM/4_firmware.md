---
title: Firmware
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2024-6-21
    version: v0.1
    author: BuGu
    content:
      - Release docs
---

## 镜像烧录与升级

NanoKVM 有两种升级模式，一种是常规的应用升级，在浏览器操作即可；若功能涉及到底层镜像修改则需重新烧卡。

### 应用升级

在浏览器页面内点击设置->检查更新->立即更新
等待约10s后，OLED重新刷出KVM状态信息，刷新网页，即可完成更新

### 镜像烧录

Lite版NanoKVM默认不带TF卡出货，需要自行准备一张8G以上的TF卡（Full版默认带一张32G TF卡，超出8G的部分将自动创建exFAT分区，用于虚拟U盘的挂载）

Full版NanoKVM自带TF卡，可上电即用，如后续涉及到镜像升级，同样可以参考以下描述

使用烧卡软件烧录TF卡，这里建议使用[Etcher](https://etcher.balena.io/)进行烧录

镜像下载地址:https://github.com/sipeed/NanoKVM/releases/tag/NanoKVM