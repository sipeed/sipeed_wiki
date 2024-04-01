---
---
title: MaixCAM System Flashing
---

## Download the System

Find the latest system image file, such as `maixcam_os_20240401_maixpy_v4.1.0.xz`, on the [MaixPy release page](https://github.com/sipeed/MaixPy/releases).

Alternative address:
* [Sourceforge](https://sourceforge.net/projects/maixpy/files/)

## Prepare Flashing Tools

Download [Etcher](https://etcher.balena.io/), install and open it.

Windows can also use [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/) or [Rufus](https://rufus.ie/).

## Flash TF Card

There are two ways to flash the TF card:

## Flash TF Card with Card Reader

* Directly remove the TF card, insert it into the card reader, and then insert it into the computer.
* Open Etcher, select the image file, select the TF card, and click `Flash`.
* Wait for the flashing to complete, eject the TF card, insert it into MaixCAM, then power on, wait for the system to start, the first boot will be slower, just wait a while.

## Flash TF Card via USB

* Power off MaixCAM, keep the TF card inserted.
* Hold down the `user` button on the device without releasing it, insert the USB cable connected to the computer, and wait for the USB device to appear on the computer.
* Open Etcher, select the image file, select the USB device, and click `Flash`.
* Wait for the flashing to complete, then press the `reset` button or re-power on, wait for the system to start, the first boot will be slower, just wait a while.





