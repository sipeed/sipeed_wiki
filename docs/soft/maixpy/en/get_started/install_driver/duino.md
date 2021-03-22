---
title: Maix Duino USB Driver Installation
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: Maix Duino USB driver installation
---


## Linux

Linux does not need to install the driver, the system comes with it, use `ls /dev/ttyUSB*` to see the device number

## Windows

The development board uses the `CH552` chip to realize the `USB` to serial port function. There is no `JTAG` simulation function. `Windows` needs to install the `FT2232` driver.

- USB driver: **FT2232** ->[[download link here](https://dl.sipeed.com/MAIX/tools/ftdi_vcp_driver)](https://dl.sipeed.com/MAIX/tools/ftdi_vcp_driver)

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
