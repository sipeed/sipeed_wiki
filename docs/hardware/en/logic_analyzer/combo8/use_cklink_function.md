---
title:  Using as CKLink
keywords: LogicAnalyzer, debugger, link, RISCV, tool
---

SLogic Combo8 features high-speed CK-Link functionality, with a speed that surpasses CK-Link Lite and comes close to CK-Link Pro, making it a great tool for debugging RISC-V chips. In this mode, it also has a high-speed serial port (20Mbps).

> Note: SLogic directly transmits data to the PC's USB port, so to achieve the maximum speed mentioned above, it is recommended to avoid using SLogic on a USB HUB with multiple devices connected.

Let's get started with using CK-LINK!

## Enable SLogic Functionality

Press the toggle button to switch the indicator light to yellow.

![](../../../zh/logic_analyzer/assets/slogic_led_yellow.png)

> To verify if SLogic functionality is enabled:
>
> On Linux, use the lsusb command / On Windows, check in Device Manager to find the CKLink HS device.

## Getting Started

On both Windows and Linux systems, you can directly refer to [Using CDK + Sipeed RV-Debugger Plus for Compilation and Debugging](https://bouffalolab.gitee.io/bl_mcu_sdk/get_started/cdk_rv_debugger_plus.html#cdk-sipeed-rv-debugger-plus) and [T-HEAD Debug Server User Manual](https://occ.t-head.cn/document?temp=introduction-2&slug=t-head-debug-server-user-manual), the usage is exactly the same.

