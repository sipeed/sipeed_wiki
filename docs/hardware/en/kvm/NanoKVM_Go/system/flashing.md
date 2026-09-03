---
title: Flash Image
keywords: NanoKVM Go, Remote desktop, KVM, flashing
---

*NanoKVM Go is usually shipped with an image already flashed. If the device boots normally, you can skip this step at first.*

## Preparation

Before flashing, prepare the following items:

- NanoKVM Go;
- a SIM eject pin or another tool that can press and hold the Reset button;
- a USB data cable;
- a Windows computer;
- the NanoKVM Go image file;
- the ImageUSB flashing tool.

## Download the Image

Download the latest NanoKVM Go image from GitHub.

Image download link: TODO

## Download the Flashing Tool

Download and install [ImageUSB](https://www.osforensics.com/tools/write-usb-images.html).

![ImageUSB download page](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_imageusb_download.webp)

## Enter Flashing Mode

1. Disconnect the USB cable from NanoKVM Go.

2. Use the SIM eject pin to press and hold the Reset button on NanoKVM Go.

![Press and hold the NanoKVM Go Reset button with a SIM eject pin](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_press_reset.webp)

3. Keep holding the Reset button, connect the USB data cable to the NanoKVM Go data port, and connect the other end to the computer.

![Hold Reset and connect the NanoKVM Go data port](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_connect_data_port.webp)

4. Open ImageUSB and wait until it detects the USB device for NanoKVM Go.

![NanoKVM Go device detected in ImageUSB](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_device_detected.webp)

5. Release the Reset button after the device is detected.

## Flash the Image with ImageUSB

1. In ImageUSB, select the USB device corresponding to NanoKVM Go.

![Select NanoKVM Go in ImageUSB](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_select_device.webp)

2. Select the mode for writing an image.

![Select write image mode in ImageUSB](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_write_mode.webp)

3. Select the downloaded NanoKVM Go image file.

![Select the NanoKVM Go image in ImageUSB](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_select_image.webp)

4. Click the write button to start flashing.

![Click the ImageUSB write button](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_start_write.webp)

5. Confirm the write operation when prompted.

![Confirm the ImageUSB write operation](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_confirm_write.webp)

6. Wait for flashing to complete.

![ImageUSB writing the image](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_write_progress.webp)

7. Flashing succeeded.

![ImageUSB flashing complete](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_complete.webp)

After flashing is complete, safely eject the USB device, disconnect the USB cable, reconnect NanoKVM Go, and wait for the system to boot.

> Do not disconnect USB or close ImageUSB during flashing. Otherwise, the image may fail to write correctly.
