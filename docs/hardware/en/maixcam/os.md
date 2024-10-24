---
title: MaixCAM System Flashing
---

## Download the System

Find the **latest** system image file on the [MaixPy Releases page](https://github.com/sipeed/MaixPy/releases), for example, `maixcam-2024-10-22-maixpy-v4.7.6.img.xz`.
Make sure to download the correct version based on your device model:
* For `MaixCAM`, download `maixcam-xxxx.xz`.
* For `MaixCAM-Pro`, download `maixcam-pro-xxxxx.xz`.

Backup download link: [Sourceforge](https://sourceforge.net/projects/maixpy/files/)

## Prepare Flashing Tools

Download [Etcher](https://etcher.balena.io/) (highly recommended), install and open it.

For Windows, you can also use [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/) or [Rufus](https://rufus.ie/) if Etcher doesn't work.

## Launch the Flashing Tool

Normally, double-click the application icon to launch it. If you encounter the error `Something went wrong. If the source image was previously compressed, please check if it's corrupted. Error spawning the child process`, it might be due to insufficient permissions. Right-click the application icon and run it as an administrator.

## Flash the TF Card

There are two ways to flash the TF card:
* If the TF card already has a system installed (for example, if you purchased the official TF card package or previously flashed the card yourself), using the USB update method is quicker (and for MaixCAM, it avoids opening the case).
* If you're using your own card and it has never had a system flashed, you must first use a card reader to flash it at least once. After that, you can use the USB to update the system.

### Method 1: Flash TF Card with a Card Reader

1. Remove the TF card, insert it into the card reader, and connect it to your computer.
2. Open Etcher, select the image file, choose the TF card, and click `Flash`.
3. After flashing, if the computer prompts with `You need to format the disk in drive G: before you can use it`, **do not** format the disk! This would erase the newly flashed system. Close the window, right-click the disk, and select "Eject" to safely remove the TF card.
4. Insert the TF card into MaixCAM, power it on, and wait for the system to boot. The first boot may take a little longer, so be patient.

### Method 2: USB Update for TF Card Image

**Note: USB can only update the system, not be used for the initial flash.** Ensure the TF card has already been flashed using a card reader and the **system is running properly** before using this method.

* For **MaixCAM-Pro**:
  1. Power off MaixCAM-Pro (for battery versions, long press the power button to shut down), keep the TF card inserted.
  2. Press and hold the `user` button without releasing, then power on (connect the USB cable to the computer or press the power button on battery versions). Wait for the USB device to appear on the computer, then release the `user` button.
  3. Open `Etcher`, select the image file, select the USB device, and click `Flash`.
  4. After flashing, if the computer prompts with `You need to format the disk in drive G: before you can use it`, **do not** format the disk! Close the window, right-click the disk, and select "Eject" to safely remove the TF card.
  5. Restart the device and wait for the system to boot. The first boot may take a bit longer, so wait about 1 minute. During booting, do not disconnect the power to avoid corrupting any files (if this happens, you can reflash the image).

* For **MaixCAM**:
  1. Power off MaixCAM and keep the TF card inserted.
  2. Press and hold the `user` button, connect the USB cable to the computer (or first connect the USB cable, then press and hold the `user` button, quickly press the `reset` button and immediately release `reset`). Wait for the USB device to appear on the computer, then release the `user` button.
  3. Open `Etcher`, select the image file, select the USB device, and click `Flash`.
  4. After flashing, if the computer prompts with `You need to format the disk in drive G: before you can use it`, **do not** format the disk! Close the window, right-click the disk, and select "Eject" to safely remove the TF card.
  5. Press the `reset` button or power the device back on and wait for the system to boot. The first boot may take a bit longer, so wait about 1 minute. During booting, do not disconnect the power to avoid corrupting any files (if this happens, reflash the image).

> If you're unable to enter USB upgrade mode, the system files might be corrupted. Use a card reader to reflash the TF card.

## Important System Usage Notes

### Force Shutdown

Other than using the `reset` button in special cases mentioned above, **do not press the `reset` button** during normal use, as this button forces a power cut. If the system is writing to the TF card at the time, it may cause system and data corruption. Similarly, forcefully unplugging the power or pressing `reset` is equally harmful. Always try to **shut down the system via software** before disconnecting the power.

For normal use, you can perform a **software shutdown or restart** using the following methods:
* Method 1: From the interface, go to `Settings` -> `Power` for software shutdown or restart.
* Method 2: Use the terminal command `poweroff` or `reboot` for software shutdown or restart.
* Method 3: Other software methods, such as using `Python` with the command `import os;os.system("poweroff")` for shutdown or restart.
* Method 4: For MaixCAM-Pro, long-pressing the power button for 4 seconds will trigger a software shutdown via the `maix` module. Continuing to hold for 8 seconds will trigger a forced power-off shutdown (firmware version >= 4.8.0 supports this).

### File Writing and Data Loss

The system uses a caching mechanism, so when your code writes to a file, it might be writing to memory first. The system will automatically write the data to disk after some time. If the power is cut during this time, the data may not be saved to the disk (TF card), and the next time you boot, the data may be missing.

Solutions:
* Avoid forcefully cutting power or pressing the `reset` button. Use software shutdown as explained above.
* For important data, manually force the system to write the cached data to the disk. In `Python`, you can use `os.sync()` to tell the system to immediately write all cached files to disk. For other methods or languages, search for keywords like "Linux flush data to disk".


