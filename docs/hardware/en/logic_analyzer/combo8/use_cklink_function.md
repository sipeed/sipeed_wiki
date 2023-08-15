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

### Debugging with CDK

- Click the `Start/Stop Debugger` button on the toolbar to enter the debug interface, as shown in the image below:

   ![Debug CDK](../../../zh/logic_analyzer/assets/cklink_cdk_debug.png)
   _Debug HelloWorld!_

- Under the `debug` interface, you can view the internal register data of the CPU in the `Register` window on the left side. At the same time, in the `Peripherals` peripheral panel on the right side, you can browse the corresponding peripheral register data. You can select the desired peripherals by using the `Peripherals->System Viewer` option in the top menu bar. Additionally, in the toolbar above the interface, you will find relevant debugging buttons that can be used for setting breakpoints, single-stepping, executing instructions one by one, and running at full speed. Of course, all these operations have corresponding shortcuts and quick setup methods. For detailed information, please refer to the CDK documentation, which will provide a comprehensive guide.

- Click the single-step run button to execute the code. You will see the cursor move to the next line of code, and at the same time, the serial panel will display the output "Hello World!"

### Debugging with T-HEAD Debug Server

> Please refer to the **Section Ten: Debugging with JTAG** in the [Getting Started with M1s DOCK](../../maix/m1s/other/start.md) guide for details.
