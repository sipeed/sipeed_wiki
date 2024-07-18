---
title: MaixCAM System Flashing
---

## Download the System

Find the latest system image file on the [MaixPy Release Page](https://github.com/sipeed/MaixPy/releases), such as `maixcam_os_20240401_maixpy_v4.1.0.xz`.

Alternative download link:
* [Sourceforge](https://sourceforge.net/projects/maixpy/files/)

## Prepare the Flashing Tool

Download [Etcher](https://etcher.balena.io/)(highly recommended), install and open it.

Windows users can also use [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/) or [Rufus](https://rufus.ie/).

## Flashing the TF Card

There are two ways to flash the TF card:
* If you bought the official TF card package, it already contains a system, but the version might be outdated. It is recommended to use the USB update method so you don't have to disassemble the casing, which makes it difficult to reassemble.
* If you are using your own card and have never flashed a system onto it before, you must first flash it using a card reader and then install the TF card by disassembling the device. After that, you can flash the image directly via USB without disassembling.

### Method One: Flashing the TF Card Using a Card Reader

* Remove the TF card and insert it into a card reader, then plug it into the computer.
* Open Etcher, select the image file, choose the TF card, and click `Flash`.
* Wait for the burning process to complete. If your computer prompts `You need to format the disk in drive G: before you can use it`, **do not** click on format disk! Otherwise, the newly burned system will be formatted again! Close the window, right-click the disk, and select eject TF card.
* Insert it into the MaixCAM, power it up, and wait for the system to boot. The first boot may be slow, just wait for a while.

### Method Two: Update the TF Card Image via USB

**Note: USB can only be used for updates, not for the first-time flashing.**
Ensure that the system has already been flashed using a card reader and is **running properly** before using this method.

* Power off the MaixCAM, keeping the TF card inserted.
* Hold down the `user` button, plug in the USB cable to the computer, (or plug in the USB cable first, then hold down the `user` button, press the `reset` button briefly and release it), wait for the disk drive to appear on the computer, and then release the `user` button.
* Open `Etcher`, select the image file, choose the disk drive, and click `Flash`.
* Wait for the burning process to complete. If your computer prompts `You need to format the disk in drive G: before you can use it`, **do not** click on format disk! Otherwise, the newly burned system will be formatted again! Close the window, right-click the disk, and select eject TF card.
* Then press the `reset` button or power it back on, wait for the system to boot. The first boot might be slow, wait until the screen displays content (to be safe, wait about 1 minute), and do not power off during boot-up to prevent file corruption during system initialization (if this happens, reflash the image).

> If you cannot enter USB upgrade mode, the system files may be corrupted, and you should reflash the TF card using a card reader.

## Points to Note When Using the System

### Forced Shutdown

Other than the above situations where using the `reset` button, it is **not recommended to press the `reset` button** during normal use. This button forcefully cuts off power. If your system is writing content to the TF card, it could cause system and data damage.
Similarly, forcibly unplugging the power supply while the system is still running poses the same risk. Try to **shut down the software before unplugging the power supply**.

For normal use, please **shut down or reboot via software**. Methods:
* Method One: From the interface, select `Settings` -> `Power` to perform a software shutdown or reboot.
* Method Two: In the terminal, use the `poweroff` or `reboot` commands to shut down or restart via software.
* Method Three: Other software calls, such as using `Python` to invoke `import os;os.system("poweroff")` for shutdown or reboot.

### Issues with File Writing and Data Loss

The system uses a caching mechanism. When your code writes a file, it might only write to memory initially, and the system automatically writes to the disk after some time. If the power is cut during this period, the content will not be written to the disk (TF card), and the next time the system boots, the previously written content will be missing.

Solutions:
* Try not to directly cut off power or press the `reset` button; use the software shutdown methods mentioned above.
* To save critical content, you can manually call an API to force the content to be written to disk. For example, in `Python`, you can use `os.sync()` to tell the system to immediately write all cached files to the disk. For other methods such as writing to a specific file, and other languages, please search for terms

