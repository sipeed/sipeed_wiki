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

SLogic Combo 8 features high-speed DAP-Link functionality, suitable for various common chips, especially for debugging STM32 chips using IDE on Windows.

## Enable DAPLink Functionality

Press the toggle button to switch the indicator light to green.

![slogic_led_green](./../../../zh/logic_analyzer/combo8/assets/use_daplink_function/slogic_led_green.png)

> To verify if DAPLink functionality is enabled:
> Open the device manager in Windows environment, and use the lsusb command in Linux environment to find the "RV CMSIS-DAP" device

## Getting Started

Here's a step-by-step guide on using the STM32F103C8T6 chip with Windows MDK IDE as an example:

### Pin sequence

> CKLink and DAPLink have similar pin connections, so they are shown together in one diagram. Please ignore the 'CK' label.

![daplink_cklink_line_order](./../../../zh/logic_analyzer/combo8/assets/use_daplink_function/daplink_cklink_line_order.png)

In DAPLink mode, it can simultaneously support one DAPLink interface and one UART interface.

The pins on the left side of the diagram (TXD, RXD, DTR, RTS) can be used as a UART interface.

The pins on the right side of the diagram (TCK, TDI, TDO, TMS) are used for DAPLink debugging.

### Connecting DAPLink using MDK
- Set the Reset Options to SYSRESETREQ.
- In CMSIS-DAP, locate and select the RV CMSIS-DAP device.

![cfg_dap_debugger_of_mdk](./../../../zh/logic_analyzer/combo8/assets/use_daplink_function/cfg_dap_debugger_of_mdk.png)

### Download the firmware using MDK:

![download_fw_in_mdk](./../../../zh/logic_analyzer/combo8/assets/use_daplink_function/download_fw_in_mdk.png)

### Debug the firmware using MDK:

![start_debugger_in_mdk](./../../../zh/logic_analyzer/combo8/assets/use_daplink_function/start_debugger_in_mdk.png)

Thank you for the document contribution from 'dragonforward'.

