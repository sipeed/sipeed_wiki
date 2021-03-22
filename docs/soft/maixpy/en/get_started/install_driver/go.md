---
title: Maix Go USB Driver Installation
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: Maix Go USB driver installation
---


The firmware of this `STM32` chip is shipped with [open-ec](https://github.com/sipeed/open-ec) firmware by default. If there is no problem, one or two serial ports will appear, such as `Linux There are two serial ports `/dev/ttyUSB0` and `/dev/ttyUSB1` under `. Please use `/dev/ttyUSB1` when downloading and accessing the serial port. Windows is similar.

If you need to re-burn this firmware, you can download it from [github](https://github.com/sipeed/open-ec/releases) or [download open-ec firmware from the official website](http://dl.sipeed.com/ MAIX/tools/flash-zero.bin), and then use `ST-LINK` to connect the `SW` pins (`GND`, `SWDIO`, `SWCLK`) of `STM32` on the board to burn. (The `STM32` on the current version of the `Go` board does not support serial port programming. You can only use `ST-LINK` for programming. If necessary, please purchase it yourself, or use a board to simulate it with `IO` ( Such as Raspberry Pi))

In addition to `open-ec`, there is also `CMSIS-DAP` firmware. Compared with `open-ec`, it can simulate `JTAG` to debug the board. Currently, `open-ec` does not support simulation of `JTAG`. Download the firmware from the official website](http://dl.sipeed.com/MAIX/tools/cmsis-dap/), use `ST-LINK` to burn it, there will be `/dev/ttyACM0` under `Linux` equipment

> ST-LINK has complete information on the programming method of `STM32`, please search by yourself

**Please note that updating the firmware of STM32 is not the same as updating the firmware of MaixPy. Generally, there is no need to update the firmware of STM32. The default is enough. STM32 is just a USB-to-serial tool! ! ! Don't be confused. . . **

## Linux

Linux does not need to install the driver, the system comes with it, use `ls /dev/ttyUSB*` to see the device number

## Windows

The development board uses a `STM32` to realize the analog serial port and the `JTAG` function. `Windows` needs to install the driver of `FT2232`.

-USB driver: **FT2232** ->[[download link here](https://dl.sipeed.com/MAIX/tools/ftdi_vcp_driver)](https://dl.sipeed.com/MAIX/tools/ftdi_vcp_driver)

When we get the MaixPy development board and connect it to the computer, we can open the device manager to check whether the serial port driver has been installed. The methods to open the device manager are:

- This computer (right click) -> Properties -> Device Manager
- Start menu (right click) -> Device Manager
- Control Panel -> (Search) Device Manager

<img src="../../../assets/get_started/win_device_1.png" height="400">

1. When our system is a Windows 10 system, the system will automatically install the driver for us, and if it is an old version of Win7, win8, we need to install the USB driver manually:
    ![](../../../assets/get_started/win_device_2.png)

2. Open the link in the previous section to download the driver
    ![](../../../assets/get_started/win_device_3.png)

3. Click Install
    ![](../../../assets/get_started/drives.gif)

4. After the installation is complete, you can see in the device manager that two serial devices have been identified (only one serial port is available)
    ![](../../../assets/get_started/win_device_4.png)
