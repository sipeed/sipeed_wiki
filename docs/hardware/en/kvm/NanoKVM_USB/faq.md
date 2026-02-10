---
title: F&Q
keywords: NanoKVM-USB, Lichee, PiKVM, RISCV, tool
---

## Exception Fixes

### No ttyUSBx Serial Device After Opening Web Page on Linux

+ This may be due to a missing serial driver. Please reinstall the CH34x driver using the following steps:

1. Download the driver from the WCH official website ([download link](https://www.wch.cn/downloads/CH341SER_LINUX_ZIP.html)), extract it, and navigate to the `driver` directory.
2. Run `uname -r` to check your operating system's release version. Find the corresponding version in ([this link](https://elixir.bootlin.com/linux/v6.2/source/drivers/usb/serial/ch341.c)) and copy the content into `ch341.c`.
3. Execute the `make` command to compile the driver.
4. Run `sudo make load` to install the driver.
5. Replace the old driver: `cp ch341.ko /lib/modules/$(uname -r)/kernel/drivers/usb/serial/ch341.ko`.

+ Some Linux distributions come with `brltty`, a Braille display tool that occupies the `/dev/ttyUSB0` serial port, causing the webpage to be unable to detect it. If you are not using `brltty`, it is recommended to uninstall it with `sudo apt remove brltty`.

### No USB Serial (COMx) Device After Opening Web Page on Windows

+ This may be caused by a missing serial driver. Please reinstall the CH34x driver as follows:

  + Download the driver from the WCH official website ([download link](https://www.wch.cn/downloads/CH341SER_EXE.html)), then double-click the installer to run it.

### NanoKVM-USB Device Driver Not Installed on Windows Controlled End

+ This may be caused by the USB composite device not being recognized correctly. Please reinstall the driver as follows:
  + Open `Device Manager` → `Other devices`
  + Find `NanoKVM-USB` → Right-click `Properties` → `Driver` → `Update Driver`
    ![](./../../../assets/NanoKVM/usb/windows_usb_1.jpeg)
  + Select `Browse my computer for drivers` → `Let me pick from a list of available drivers on my computer`
    ![](./../../../assets/NanoKVM/usb/windows_usb_2.jpeg)
  + Double-click `Show all devices`
    ![](./../../../assets/NanoKVM/usb/windows_usb_3.jpeg)
  + In `Standard USB Host Controller` / `Standard system devices`, find `USB Composite Device` and double-click to install
    ![](./../../../assets/NanoKVM/usb/windows_usb_4.jpeg)

    ![](./../../../assets/NanoKVM/usb/windows_usb_5.jpeg)

    > **Note**: The driver location may vary depending on the Windows version. Please search patiently.

### Unable to Open NanoKVM-USB Corresponding Serial Device After Opening Web Page

+ This may be due to other programs occupying the serial port. Please ensure it is not in use before trying again.
+ Linux may lack permissions to open the serial port. Execute `sudo chmod 777 /dev/ttyUSB*` in the terminal.
+ The Chrome browser may not have detected the serial port. Please refresh the webpage or restart Chrome.
+ Chrome may lack sufficient permissions. Please grant the necessary permissions.

### The serial port device cannot be found after connecting the device on the Mac Mini (Apple Silicon)

This is typically because the rear Thunderbolt ports and the front USB ports on newer Mac Minis use different controllers, resulting in varying compatibility with certain USB devices. The rear Thunderbolt ports may be more selective when handling legacy USB serial devices (CDC ACM), while the native USB-C ports on the front generally offer better compatibility.

Recommended Solutions:

+ Use the front ports: Connect the device to the front USB-C port on the Mac Mini.
+ Use a USB Hub: If you must use the rear ports, try connecting through a USB Hub, which usually resolves the detection issue.

## Video Issues

### Some Hosts Experience Abnormal Colors or Visual Artifacts in BIOS Display Output/Capture  

+ Early firmware of NanoKVM-USB may cause issues on certain BIOS systems, such as reddish display output, greenish capture colors, or visual artifacts. These problems can be resolved by flashing the new firmware. Please download the flashing software and firmware first:  
**Standard Edition:** [Firmware Download Link](https://dl.sipeed.com/fileList/KVM/NanoKVM_USB/MS2131_LIB_V2_0_27_Demo_GPIO0_PlugDetect_20251205_replaced_E158EDID.bin)、[Flashing Software Download Link](https://dl.sipeed.com/fileList/KVM/NanoKVM_USB/MS_USB3_0_UpgradeTool_V1_3_2.exe)  
**4K Edition:** [Firmware Download Link](https://dl.sipeed.com/fileList/KVM/NanoKVM_USB/MS2131S_XSKJ001_20260205_1019.bin)、[Flashing Software Download Link](https://dl.sipeed.com/shareURL/KVM/NanoKVM_USB) USBVideoDownloadTool_V1.9.15.77.exe  

+ Flashing Steps:  
    1. Open the software and select the downloaded firmware.  
    2. Connect the USB-C port on the NanoKVM-USB Host end to your computer.  
    3. Wait for the software to establish a connection, then click "Start Flashing" and wait for the process to complete.  

> **Do not disconnect NanoKVM-USB during the flashing process, as it may brick the device.**  
> Be sure to distinguish between the Standard Edition and the 4K Edition. The flashing software and firmware are different for each version.  
> The flashing software is only compatible with Windows.

### Poor Video Quality

+ First, check if you're using a USB 2.0 cable/HOST interface. When the resolution is high, USB 2.0 may not provide sufficient bandwidth, which can lower the video quality. It is recommended to use a USB 3.0 cable.
+ At 2K resolution, the video quality may decrease due to the chip's encoding capability. Please switch to 1080P.
+ If the target device is connected to a Windows host, go to System Settings > Display Settings > Advanced Display Settings, and change to 1080P60 in the "List all modes" section. Also, check if the "Desktop Resolution" and "Active Signal Resolution" are consistent.

### DP-HDMI Adapter

+ Some passive DP to HDMI converters only perform level conversion in their internal circuitry, resulting in poor compatibility with NanoKVM-USB. This manifests as the video signal not appearing when waking from sleep; the NanoKVM-USB still shows a black screen, requiring manual unplugging and replugging of the HDMI cable.

### No HDMI Loop Out

+ The beta version hardware only supports USB power from the HOST side. Please ensure proper power supply from the HOST side during use.

### Loop Out Display

+ The NanoKVM-USB uses its own EDID (Extended Display Identification Data) before connecting to the loop-out display. After connecting to the loop-out display, it switches to the EDID of the loop-out display.
+ Since the EDID contains information about the display manufacturer and color settings, the resolution list in the Target system settings may appear different before and after connecting the loop-out display. Additionally, the color of the video captured via USB may vary before and after the connection.

## Other

+ If the above methods do not resolve the issue, please describe your purchased model and the encountered problem on the forum, GitHub, or QQ group, and we will respond patiently.

## Known Issues

### Latency

+ The ARM version of macOS experiences increased latency when connected to a Raspberry Pi via NanoKVM-USB; other combinations are not affected.

## Feedback Methods

+ [GitHub Issues](https://github.com/sipeed/NanoKVM)
+ [MaixHub Forum](https://maixhub.com/discussion/nanokvm)
+ QQ Group: 703230713
