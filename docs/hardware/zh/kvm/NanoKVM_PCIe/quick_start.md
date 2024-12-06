---
title: 快速上手
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2024-12-5
    version: v0.1
    author: BuGu
    content:
      - Release docs
---

## 开箱

![](./../../../assets/NanoKVM/unbox/PCIe_unbox.jpg)

NanoKVM-PCIe 包装内包含主机, 半高 PCIe 挡板, 两条 USBA-C线缆, 一条 HDMI 线缆, 一根天线, 16P 公对母排线, 4P 母对母排线和一把小螺丝刀
主机上包含杜邦跳线(2+4P), SMA 天线座

注: 上图是 NanoKVM-PCIe 带WiFi 带PoE 版本,不带 WiFi 版本会少一根天线, 挡板上少 SMA 天线座

## 接口介绍

俯视图:

![](./../../../assets/NanoKVM/unbox/PCIe-Interface1.png)

侧视图:

![](./../../../assets/NanoKVM/unbox/PCIe-Interface2.png)

机箱内部接口:

![](./../../../assets/NanoKVM/unbox/PCIe-Pin.jpg)


## 供电

+ NanoKVM-PCIe 有多种供电选择: USB HID直接供电, USB PWR IN辅助供电, PCIe 插槽取电, PoE 供电(选配) 请任选一种即可, 同时存在多路供电不会干扰 NanoKVM-PCIe 的运行

+ 如果需要USB HID直接供电,则需要在BIOS中设置主板关机 USB 常供电，否则会影响远程开机功能

+ NanoKVM-PCIe USB-PWR-IN CC 接口下拉5.1K电阻，可使用正规 PD 充电头供电。部分劣质PD电源存在烧坏 NanoKVM-PCIe 的风险。

## 接线

+ NanoKVM-PCIe 在接线上与 Cube 类似, 请在主机关机且断电的情况下安装 NanoKVM-PCIe

+ 使用一条 USB C to A 数据线连接远程主机和 NanoKVM 的 PC USB 接口（位于 HDMI 接口下方）

+ 使用附赠的 HDMI 线缆连接远程主机和 NanoKVM 的 HDMI 接口

  ![](./../../../assets/NanoKVM/unbox/hdmi.png)

+ 使用网线连接 路由器/交换机 与 NanoKVM

## 更新

### 更新镜像

> **Lite 版本需要准备 TF 卡并且烧录镜像后才能开始使用！**

Full 版本出厂时已经烧录了镜像，可以跳过此步骤。

镜像会不定期更新。建议更新到最新版本镜像，以获取更好的使用体验。

具体操作方式请参考 [烧录镜像](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/flashing.html)。

### 更新应用

新的应用往往带来更多功能或修复某些重要漏洞，建议您将 NanoKVM 应用更新到最新版本，具体操作方式请参考 [更新应用](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/updating.html)。

## 基础操作

### 如何获取IP地址

Full版NanoKVM自带OLED显示屏，联网之后会在显示屏第一行显示IP地址；

![](./../../../assets/NanoKVM/unbox/oled.jpg)

Lite版用户请参考[获取IP](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/updating.html#%E8%8E%B7%E5%8F%96-IP)

### 查看远程桌面

浏览器直接输入获取的IP，进入登录页面，默认账号密码为admin、admin，登录后建议**先检查更新**（设置 -> 检查更新），详细步骤可参考 [更新应用](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/updating.html)。

Lite版用户，或Full用户重新烧卡登录后页面上无远程画面，请先升级应用后刷新网页，即可开始使用

注: 建议使用Chrome浏览器，其他浏览器可能出现无法显示画面或无法操作键鼠等兼容性问题

![](./../../../assets/NanoKVM/unbox/frist_update.png)

### 修改账号密码

**为保障您的信息安全，请在测试功能正常后修改账号密码**

![](./../../../assets/NanoKVM/unbox/unbox_9.png)

### ATX电源控制

Full 版套餐内包含了 NanoKVM-A/B 板，用于控制和查看主机开关机状态。

+ 顶板上的 5V LED（蓝色）指示 NanoKVM 的供电情况；
+ PWR LED（绿色）为主机的电源指示；
+ POWER按键作用同主机的电源按键，可以控制主机的开关机；
+ RESET按键用主机的重启按键，开机状态下按下RESET将强制重启主机
+ 网页端也可以查看并控制，参考[用户指南](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/user_guide.html)

