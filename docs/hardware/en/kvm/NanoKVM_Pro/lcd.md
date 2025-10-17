---
title: Customize Auxiliary Screen
keywords: NanoKVM, Auxiliary Screen
update:
  - date: 2025-10-10
    version: v0.1
    author: zepan
    content:
      - initial docs
  - date: 2025-10-18
    version: v0.2
    author: bugu
    content:
      - improve docs
---

## Introduction
The NanoKVM-Pro Desk is equipped with a 1.47-inch 320x172 mini display. In addition to serving as a basic configuration interface, it can also display user-customized content in various ways, functioning as a secondary screen.

## HDMI Secondary Screen
When NanoKVM-Pro is operating, it virtually emulates a monitor, allowing it to capture HDMI images and display them on its own screen, enabling HDMI secondary screen functionality.

In the UI, select the HDMI output video source to display the captured video image on the small screen.

When used as a desktop accessory, this feature can serve as a desktop mini secondary screen for performance monitoring, video thumbnail player, and other functions.

![](./../../../assets/NanoKVM/pro/lcd/hdmi.jpg)

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
  <video playsinline controls muted preload src="../../../assets/NanoKVM/pro/lcd/cat.mp4"></video>
  <video playsinline controls muted preload src="../../../assets/NanoKVM/pro/lcd/video.mp4"></video>
</div>

## USB Secondary Screen

Currently, the USB secondary screen feature only supports Windows systems.

1. Download and extract the USB secondary screen driver: https://github.com/sipeed/NanoKVM-Pro/releases/download/v1.0.5/nanokvmpro_usb_graphic_win.zip

2. On the Desk: From the screen, tap `Settings` → `USB` to enter the USB configuration page, then enable `Panel`.

3. On the controlled machine:

   - Open `Device Manager` → `Other devices`
   - Find `NanoKVMPro` → Right-click `Properties` → `Driver` → `Update Driver`
   - Select `Browse my computer for drivers` → `Let me pick from a list of available drivers on my computer`
   - Double-click `Show all devices`
   - Find `USB Composite Device` under `Standard USB Host Controller` / `标准 USB 主机控制器` / `Standard system devices` / `标准系统设备` → Double-click to install

   > **Note**: Driver locations may vary across different Windows versions. Please search patiently.

4. After completion, a new `loop input to output` device will appear under `Other devices` in `Device Manager`.

5. Right-click the device → `Update Driver` → `Browse my computer for drivers` → `Browse` → Select the USB secondary screen driver folder → `Next` → Follow the prompts to complete installation.

6. After driver installation is complete, a new NanoKVM graphics device will appear in the `Display adapters` section.

7. On the Desk, navigate to the secondary screen page from the screen and select USB to use the Desk as a USB secondary screen.

8. To disable, refer to step 2 and turn off `Panel`.

9. When re-enabling, some systems may require reinstalling the USB driver.

## Custom Display

> Note: This feature requires the NanoKVM-Desk application to be updated to version `1.1.5` or higher.

NanoKVM Desk introduces a user-defined APP function in version `1.1.5`. By long-pressing the screen/knob and switching to the fourth page, you can view all APPs. Three demo apps are pre-installed by default: `coin`, `conway`, and `hello`.

[hello.py](../../../assets/NanoKVM/pro/lcd/hello.py)
[conway.py](../../../assets/NanoKVM/pro/lcd/conway.py)
[coin.py](../../../assets/NanoKVM/pro/lcd/coin.py)

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
  <video playsinline controls muted preload src="../../../assets/NanoKVM/pro/lcd/doom.mp4"></video>
  <video playsinline controls muted preload src="../../../assets/NanoKVM/pro/lcd/conway.mp4"></video>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
  <video playsinline controls muted preload src="../../../assets/NanoKVM/pro/lcd/pao.mp4"></video>
  <video playsinline controls muted preload src="../../../assets/NanoKVM/pro/lcd/coin.mp4"></video>
</div>

### How to Build Your Own Application

NanoKVM Desk will search for all folders in the system's `/userapp` directory and use the folder names as APP names. It is recommended to keep folder names under 8 characters.

In the `User APP` interface, when you click on a user-defined application, the system will attempt to launch a Python application named `main.py` inside the corresponding folder.

At this point, the small screen uses the standard FB driver, allowing users to utilize `/dev/fb0` to implement custom screen display operations.

Clicking the screen or pressing the knob will exit the application.