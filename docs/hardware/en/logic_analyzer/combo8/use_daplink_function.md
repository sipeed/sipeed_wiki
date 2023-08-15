---
title: Using as DAPLink
keywords: LogicAnalyzer, debugger, link, RISCV, tool
---

SLogic Combo8 features high-speed DAP-Link functionality, suitable for various common chips, especially for debugging STM32 chips using IDE on Windows.

## Enable DAPLink Functionality

Press the toggle button to switch the indicator light to green.

![](../../../zh/logic_analyzer/assets/slogic_led_green.png)

> To verify if DAPLink functionality is enabled:
>
> Linux: Use the lsusb command to check if the CMSIS-DAP HS USB device appears.

### Getting Started

Here's a step-by-step guide on using the STM32F103C8T6 chip with Windows MDK IDE as an example:

1. Quickly generate the project using STM32CUBEMX, paying attention to the minimum version number of the generated project.

2. Connect to DAPLink using MDK:

![](../../../zh/logic_analyzer/assets/cfg_dap_debugger_of_mdk.png)

3. Download the firmware using MDK:

![](../../../zh/logic_analyzer/assets/download_fw_in_mdk.png)

4. Debug the firmware using MDK:

![](../../../zh/logic_analyzer/assets/start_debugger_in_mdk.png)
