---
title:  作为CKLink使用
keywords: LogicAnalyzer, debugger, link, RISCV, tool
update:
  - date: 2023-07-23
    version: v0.1
    author: lxo
    content:
      - Release docs
---

SLogic Combo8 具备高速CK-Link功能，且速率远超CK-Link Lite，接近CK-Link Pro，是调试RISC-V芯片的好工具。在此模式下还同时具备一路高速串口（20Mbps）功能。

准备开始使用CK-LINK！

## 开启CKLink功能

按下切换按键，将指示灯切换为黄色

![slogic_led_yellow](./assets/use_cklink_function/slogic_led_yellow.png)

> 验证CKLink功能是否开启的方法:
> Linux使用lsusb命令/Windows使用设备管理器，可以找到CKLink HS设备

## 开始使用

### 引脚连接

> CKLink和DAPLink线序相似，所以放到了一张图里，请忽略掉“DAP”

![daplink_cklink_line_order](./assets/use_daplink_function/daplink_cklink_line_order.png)

CKLink模式下可以同时支持一路CKLink和一路UART

- 上图左侧的引脚（TXD、RXD、DTR、RTS）可以作为串口使用
- 上图右侧的引脚（TCK、TDI、TDO、TMS）作为CKLink调试使用

### 使用方法

 在Windows、Linux系统可以直接参考[使用 CDK + Sipeed RV-Debugger Plus 编译调试](https://bouffalolab.gitee.io/bl_mcu_sdk/get_started/cdk_rv_debugger_plus.html#cdk-sipeed-rv-debugger-plus)和[T-HEAD Debug Server 用户手册](https://occ.t-head.cn/document?temp=introduction-2&slug=t-head-debug-server-user-manual)，用法完全一样