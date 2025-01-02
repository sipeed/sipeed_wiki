---
title: Quick Start
keywords: NanoKVM, Remote desktop, tool, USB
update:
  - date: 2024-12-25
    version: v0.1
    author: xwj
    content:
      - Release docs
---

## Interface

![](./../../../assets/NanoKVM/usb/interface.jpg)

## Wiring

Use a USB3.0 or Type-C cable to connect NanoKVM-USB and the Host device.

![](./../../../assets/NanoKVM/usb/quick_start/wiring1.png)

Use an HDMI cable to connect NanoKVM-USB and Target device.

![](./../../../assets/NanoKVM/usb/quick_start/wiring2.png)

Use a USB3.0 cable to connect NanoKVM-USB and Target device.

![](./../../../assets/NanoKVM/usb/quick_start/wiring3.png)

## Use in Web

### Open the webpage

Use Chrome browser to visit `https://usbkvm.sipeed.com`.

> Please use the desktop Chrome browser, and the version number must be greater than 89.
>
> Mobile Chrome or other browsers that do not support [Web Serial API](https://developer.mozilla.org/en-US/docs/Web/API/Serial) cannot use keyboard and mouse.

### Authorization

NanoKVM-USB will simulate a USB camera to transmit video and audio data. Therefore, the web page must obtain permission to use the camera.

![](./../../../assets/NanoKVM/usb/quick_start/auth_camera.png)

> If you rejected the authorization or want to turn off the authorization, you can choose to reset all permissions.
>
> ![](./../../../assets/NanoKVM/usb/quick_start/reset.png)

### Select USB devices

After obtaining authorization, We need to select two USB devices:

1. USB camera: for video and audio input;
2. Serial device: for sending keyboard and mouse data.

#### USB Camera

Click the drop-down button and select the camera device named in the format of `USB Video`.

Once the device is selected, the web page will start to display the video image.

![](./../../../assets/NanoKVM/usb/quick_start/usb_video.png)

#### Serial Port Device

Click button and a list of available serial port devices will pop up. Select the device named in the format of `USB Serial`.

> If the browser does not support Web Serial API, the button will not be displayed and the keyboard and mouse is not available.

![](./../../../assets/NanoKVM/usb/quick_start/usb_serial.png)

Setup complete!

Enjoy it!

### Audio

If the webpage does not play sound automatically, some manual setups are required.

Here is an example of Mac controlling Windows:

#### Target side

On the Target side(Windows), select NanoKVM as the **audio output** device.

The name of the audio device depends on whether a loopback device is connected:

- If the loopback device is not connected, the audio device name is `HDMI TO USB`;
- If the loopback device is connected, the name of the audio device is the same as the loopback device.

![](./../../../assets/NanoKVM/usb/quick_start/audio_output.jpg)

#### Host side

On the Host side(Mac), select NanoKVM as the **audio input** device.

The name format of the audio device is generally `USB Digital Audio`.

![](./../../../assets/NanoKVM/usb/quick_start/audio_input.png)

### Mouse

The mouse uses the `absolute mode` by default.

In the BIOS or some systems, this mode may not work properly. Please switch to the `relative mode` if the mouse is not available.

![](./../../../assets/NanoKVM/usb/quick_start/mouse_mode.png)
