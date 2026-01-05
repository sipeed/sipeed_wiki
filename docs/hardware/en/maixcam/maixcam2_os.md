---
title: MaixCAM2 System Flashing
---



## Downloading the System

At present, only images in the `.img` format are provided, and may be compressed to `.img.xz` or multi-volume compression to `.img.7z.00x`.

[Download image (Baidu Netdisk)](https://pan.baidu.com/s/1r4ECNlaTVxhWIafNBZOztg) Extraction code: `vjex`.
[Download image (MEGA)](https://mega.nz/folder/01IEDZQb#3ktByGkFMn_x6jDxMLbK4w)

Image file directory description:
1. `boot_parts_maixcam2-xxx-maixpy-xxx.axp`:This file is a minimal boot image. Normally, it does not need to be flashed. Only when the board cannot be flashed via TF card or USB, refer to the method described below for flashing .axp files. After flashing this file, the TF card and USB flashing functions can be restored.
2. `maixcam2-xxx-maixpy-xxx.img.7z.00x`:The image is split into multiple files using multi-volume compression. You may see files such as `maixcam2-2025-12-22-maixpy-v4.12.4.img.7z.001` and `maixcam2-2025-12-22-maixpy-v4.12.4.img.7z.002`. All volume files must be downloaded before extraction.
    > Extraction instructions:
    > - `On Linux`: use `7z` to extract. Place all volume files in the same directory, then run: '`7z x maixcam2-2025-12-22-maixpy-v4.12.4.img.7z.001`'
    > - `On Windows`: place all volume files in the same folder, then right-click the first file (`.7z.001` or `.7z`) and select 7-Zip -> Extract Files or Extract Here.The software will automatically merge and extract the files. Make sure all volumes are complete and correctly named.

For MaixCAM2, there are two types of systems and flashing methods:

* **Method 1**: The original chip manufacturer’s flashing format (`.axp`). Requires [AXDL](https://dl.sipeed.com/shareURL/MaixCAM/MaixCAM2/Software/Tools) to flash.
  * Pros: Works regardless of whether the EMMC has a boot partition or system.
  * Cons: Only supported on Windows, flashing speed is slow.
* **Method 2**: USB flashing (`.img` format), which contains a complete system. You can flash it with general tools such as `etcher / rufus / win32diskimager / imageUSB`.
  * Pros: Simple, OS/software independent, faster (TF > USB2.0 > AXDL).
  * Cons: Only works if the EMMC already has a **boot partition**. If the boot partition is missing or corrupted, you must first flash a `*.axp` system using Method 1 before Method 2 can be used.
* **Method 3**: TF card flashing (`.img` format), which contains a complete system.
  * Pros: Simple, OS/software independent, no extra 3rd-parth PC software needed, faster (TF > USB2.0 > AXDL).
  * Cons: Need a TF card. Only works if the EMMC already has a **boot partition**. If the boot partition is missing or corrupted, you must first flash a `*.axp` system using Method 1 before Method 2 can be used.

**Recommended**: Normally, devices are shipped with a boot partition already flashed, so Method 2 is sufficient. Only use Method 1 if the boot partition is damaged.

Follow the [MaixPy system flashing guide](https://wiki.sipeed.com/maixpy/doc/zh/basic/upgrade.html) to download the appropriate system image for your model, and remember to back up your data.

## System Boot Process (Overview)

To help you understand, here’s a simplified version of the boot process:

1. On power-up, the chip’s internal bootrom checks if the `boot/Func` pin is pulled low (the MaixCAM2 `Func` button pressed). If yes, it enters `AXDL` USB download mode and waits for AXDL software to communicate via USB for at least **5 seconds**.
   If not pressed, it proceeds to normal boot.

2. It then loads the **boot partition** firmware from internal EMMC storage (where the system and data are stored). This firmware also checks if `boot/Func` is pressed—if yes, it enters USB/TF upgrade mode; if not, it continues loading the system from EMMC.


## Method 1: Flashing `.axp` System via USB to EMMC

As mentioned earlier, there are three flashing methods. Here we’ll cover the first in detail.

### Launch AXDL Software

Download [AXDL](https://dl.sipeed.com/fileList/MaixCAM/MaixCAM2/Software/Tools/AXDL_V1.24.22.1.7z).(Only have Windows version)
Download [AXDL Driver](https://dl.sipeed.com/fileList/MaixCAM/MaixCAM2/Software/Tools/Driver_V1.20.46.1.7z), Run `DriverSetup.exe` after decompression to install the driver. If the driver can not be recognized, please try to restart the computer.

Open the AXDL software interface.

### Preparing the System

You should already have downloaded the `.axp` format system. Usually, two types are provided, e.g.:

* `maixcam2-2025-09-01-maixpy-v4.11.9.axp`: A **full** `.axp` system (\~8GB).
* `boot_parts_maixcam2-2025-09-01-maixpy-v4.11.9.axp`: A **boot partition only** file (<50MB).

This means you can:

* Use AXDL once to flash the complete system, then boot and run directly.
* Or, if you prefer USB/TF flashing but your boot partition is damaged (“bricked”), quickly restore just the **boot partition** with `boot_parts_xxx.axp`, then use Method 2 to flash the full system.

### Load and Flash the System File

* Click the “Load System File” button and select your `.axp` system file.
* After loading, click “Start” to begin USB detection.
* Hold the `boot/Func` button, connect the board to the PC via USB, and AXDL will start flashing. Release the button and wait.
* Alternatively, connect USB first, then hold `boot/Func` and power on. Once detected by AXDL, release the button.
* Do not touch the USB cable or board during flashing.
* After completion, the board reboots into the system. The **first boot** may take longer—wait until it reaches the main interface before powering off.

## Method 2 (Recommended): Flashing `.img` System via USB to EMMC

This method is faster and easier than flashing `.axp` files. It works on any OS and achieves higher speeds (\~40MiB/s).

### Choosing the Right Flashing Software


We’ll use [Etcher](https://etcher.balena.io/)  as an example. Other software works similarly.

On Windows, you can also use [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/), [Rufus](https://rufus.ie/), or [imageUSB](https://www.osforensics.com/tools/write-usb-images.html). If Etcher fails, try one of these alternatives.


If you encounter errors like `Error spawning the child process`, it’s likely a permissions issue. Run as administrator.
If problems persist, or the system won’t boot after flashing, try `rufus` or `win32diskimager`.

### Load and Flash the System File

> `Etcher`may occurs `Missing partition table` `not a bootable image ...` warning, it's normall for `MaixCAM2`, just click `Continue` to continue.

* Load the system image you downloaded and extract it. Make sure you’re loading the right one. It’s usually named `maixcam2-2025-09-01-maixpy-v4.11.9.img`.
* Enter USB/TF upgrade mode:

  * Method 1: Plug one end of USB into the PC, then within `1 second` of connecting to the board, press and hold `boot/Func`. Release after `3 seconds`.
  * Method 2: Power off, connect USB, power on, then within `1 second` press and hold `boot/Func`. Release after `3 seconds`.

  > Don’t hold the button before power-on—this enters AXDL mode, which takes at least 10 seconds. Too slow.
* After a few seconds, you’ll see a virtual U-disk appear. The blue LED flashes in a `off-on-on` pattern.
* Click the software’s “Flash” button to begin. The blue LED flashes `0.5s on / 0.5s off`.
* If Windows prompts to format the new drive—**do not format it**! Just close the window.
* When done, the blue LED becomes solid on. Software may still be verifying data—wait for it.
* Safely eject the drive.
* Reboot to enter the new system. Again, wait for the first boot to reach the main interface before powering off.

## Method 3: Flashing `.img` System via TF Card to EMMC

This is similar to USB flashing but often faster (depending on TF card speed, e.g. \~90MiB/s).

### Preparing a TF Upgrade Card

* Insert the TF card into your PC using a card reader.
* Format the TF card as `exFAT` or `ext4` (not `FAT32`). Make sure to partition the TF card.
* Copy the xxx.img file to the first partition of the TF card. If you have previously copied other `.img` files, you need to delete the old image files.
* Safely eject the card to ensure data is fully written.
* Power off the MaixCAM2, then insert the TF card into the MaixCAM2.
* Power on the MaixCAM2, and within `1 second`, press and hold the `boot/Func` button.
* The board will auto-detect and flash the system. Blue LED flashes `0.5s on / 0.5s off`.
  > If it doesn’t, check previous steps.
* When complete, the LED stays solid on. Fast flashing (`0.3s on / 0.3s off`) indicates failure. Do not power off—use Method 2 (USB) to recover. If powered off and still failing, use AXDL to restore the boot partition.
* Reboot to enter the new system. As before, wait for the first boot to finish before shutting down.

## Power Supply Notes

### Shutdown and Power-Off

Aside from the above flashing situations, do **not** power off by cutting power (including using the power switch, which is also a hard cut). If the system is writing to the TF card, forced power-off can corrupt data. The same risk applies when pressing `reset`. Always **shutdown via software first**.

Ways to safely shutdown/reboot:

* Method 1: From the main interface, long-press `Func` to select shutdown, or go to `Settings -> Power`.
* Method 2: In terminal, run `poweroff` or `reboot`.
* Method 3: From code, e.g. in Python: `import os; os.system("poweroff")`.

### File Writing and Data Loss

The system uses caching. When writing files, data may remain in memory before being flushed to disk. If power is cut in this period, data is lost.

Solutions:

* Avoid forced shutdowns/resets; use software shutdown.
* To ensure data is written, manually flush caches. For example, in Python:

  ```python
  import os
  os.sync()
  ```

  This tells the system to immediately write cached data to disk. Other languages/contexts have equivalent APIs (search for “Linux flush cache to disk”).

