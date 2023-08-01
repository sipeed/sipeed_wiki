---
title: Using as DAPLink
keywords: LogicAnalyzer, debugger, link, RISCV, tool
update:
  - date: 2023-07-26
    version: v0.1
    author: ctx
    content:
      - Release docs
---

SLogic Combo8 features high-speed DAP-Link functionality, suitable for various common chips, especially for debugging STM32 chips using IDE on Windows.

## Enable DAPLink Functionality

Press the toggle button to switch the indicator light to green.

![slogic_led_green](./../../../zh/logic_analyzer/combo8/assets/use_daplink_function/slogic_led_green.png)

> To verify if DAPLink functionality is enabled:
> Linux: Use the lsusb command to check if the CMSIS-DAP HS USB device appears.

## Getting Started

Here's a step-by-step guide on using the STM32F103C8T6 chip with Windows MDK IDE as an example:

### Pin sequence

> CKLink and DAPLink have similar pin connections, so they are shown together in one diagram. Please ignore the 'CK' label.

![1690857341367](./../../../zh/logic_analyzer/combo8/assets/use_daplink_function/daplink_cklink_line_order.png)

In DAPLink mode, it can simultaneously support one DAPLink interface and one UART interface.

The pins on the left side of the diagram (TXD, RXD, DTR, RTS) can be used as a UART interface.

The pins on the right side of the diagram (TCK, TDI, TDO, TMS) are used for DAPLink debugging.

### Connecting DAPLink using MDK
- Set the Reset Options to SYSRESETREQ.
- In CMSIS-DAP, locate and select the CMSIS-DAP HS device.

![cfg_dap_debugger_of_mdk](./../../../zh/logic_analyzer/combo8/assets/use_daplink_function/cfg_dap_debugger_of_mdk.png)

### Download the firmware using MDK:

![download_fw_in_mdk](./../../../zh/logic_analyzer/combo8/assets/use_daplink_function/download_fw_in_mdk.png)

### Debug the firmware using MDK:

![start_debugger_in_mdk](./../../../zh/logic_analyzer/combo8/assets/use_daplink_function/start_debugger_in_mdk.png)

## Issues

1. Can't find DAPLink device

- Check if the MDK version is too low, as older versions of MDK may not recognize DAPLink. The MDK version used in this document for testing is V5.38.
- If the low MDK version is causing DAPLink recognition issues and you prefer not to upgrade, you can refer to the methods provided [here](https://developer.arm.com/documentation/ka003663/latest/) to update the debug driver for CMSIS-DAP.

Thank you for the document contribution from 'dragonforward'.

