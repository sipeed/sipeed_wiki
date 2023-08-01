---
title:  Using as CKLink
keywords: LogicAnalyzer, debugger, link, RISCV, tool
update:
  - date: 2023-07-26
    version: v0.1
    author: ctx
    content:
      - Release docs
---

SLogic Combo8 features high-speed CK-Link functionality, with a speed that surpasses CK-Link Lite and comes close to CK-Link Pro, making it a great tool for debugging RISC-V chips. In this mode, it also has a high-speed serial port (20Mbps).

Let's get started with using CK-LINK!

## Enable CKLink Functionality

Press the toggle button to switch the indicator light to yellow.

![slogic_led_yellow](./../../../zh/logic_analyzer/combo8/assets/use_cklink_function/slogic_led_yellow.png)

> To verify if SLogic functionality is enabled:
> On Linux, use the lsusb command / On Windows, check in Device Manager to find the CKLink HS device.

## Getting Started

### Pin sequence

> CKLink and DAPLink have similar pin connections, so they are shown together in one diagram. Please ignore the 'DAP' label.

![daplink_cklink_line_order](./../../../zh/logic_analyzer/combo8/assets/use_daplink_function/daplink_cklink_line_order.png)

In CKLink mode, it can simultaneously support one CKLink interface and one UART interface.

The pins on the left side of the diagram (TXD, RXD, DTR, RTS) can be used as a UART interface.

The pins on the right side of the diagram (TCK, TDI, TDO, TMS) are used for CKLink debugging.

### Instructions

On both Windows and Linux systems, you can directly refer to [Using CDK + Sipeed RV-Debugger Plus for Compilation and Debugging](https://bouffalolab.gitee.io/bl_mcu_sdk/get_started/cdk_rv_debugger_plus.html#cdk-sipeed-rv-debugger-plus) and [T-HEAD Debug Server User Manual](https://occ.t-head.cn/document?temp=introduction-2&slug=t-head-debug-server-user-manual), the usage is exactly the same.

