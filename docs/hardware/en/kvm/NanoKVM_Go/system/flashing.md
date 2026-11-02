---
title: Flash Image
keywords: NanoKVM Go, Remote desktop, KVM, flashing
---

*NanoKVM Go is usually shipped with an image already flashed. If the device boots normally, you can skip this step at first.*

## Preparation

Before flashing, prepare the following items:

- NanoKVM Go;
- a SIM eject pin or another tool that can press and hold the flashing-mode button;
- a USB data cable;
- a computer running Windows, macOS, or Linux;
- the NanoKVM Go image file;
- the flashing tool for your operating system:
  - Windows: balenaEtcher 2.1.6 or ImageUSB;
  - macOS: balenaEtcher 2.1.6;
  - Linux: balenaEtcher 2.1.6.

## Download the Image

Download the latest NanoKVM Go image from GitHub.

Image download link: [NanoKVM-Go Releases](https://github.com/sipeed/NanoKVM-Go/releases)

> NanoKVM Go and NanoKVM Go+ use the same image. There is no separate image for Go+, so download the same file for either model.

## Download the Flashing Tool

balenaEtcher runs on Windows, macOS, and Linux, so prefer it; ImageUSB runs on Windows only and is the fallback there.

### balenaEtcher 2.1.6 (Windows / macOS / Linux)

Stay on balenaEtcher 2.1.6:

Download link: [balenaEtcher v2.1.6](https://github.com/balena-io/etcher/releases/tag/v2.1.6)

In the `Assets` section of that release, pick the installer for your operating system:

- Windows: `balenaEtcher-2.1.6.Setup.exe`;
- macOS: `balenaEtcher-2.1.6-arm64.dmg` (Apple silicon) or `balenaEtcher-2.1.6-x64.dmg` (Intel);
- Linux: `balena-etcher_2.1.6_amd64.deb` (Debian / Ubuntu) or `balena-etcher-2.1.6-1.x86_64.rpm` (Fedora / RHEL).

The official download page lists installers by operating system and architecture but does not let you choose a version, so use the release link above to get 2.1.6.

![balenaEtcher download options by operating system and architecture](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_etcher_download.webp)

### ImageUSB (Windows)

ImageUSB runs on Windows only. Download the zip from the official site, unzip it, and run `imageUSB.exe`; no installation is required.

Download link: [ImageUSB](https://www.osforensics.com/tools/write-usb-images.html)

![ImageUSB download page](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_imageusb_download.webp)

## Enter Flashing Mode

1. Disconnect the USB cable from NanoKVM Go to power off the device.

2. Insert the SIM eject pin through the opening and press and hold the flashing-mode button on NanoKVM Go.

![Press and hold the NanoKVM Go flashing-mode button with a SIM eject pin](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_press_reset.webp)

3. Keep holding the flashing-mode button, insert the USB data cable connected to the computer into the NanoKVM Go data port (Data Port).

![Hold the flashing-mode button and connect the NanoKVM Go data port](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_connect_data_port.webp)

## Flash the Image with balenaEtcher (Windows / macOS / Linux)

1. In balenaEtcher, click `Flash from file` and select the downloaded NanoKVM Go image.

![Click Flash from file in balenaEtcher](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_etcher_flash_from_file_en.webp)

2. When the `Missing partition table` warning appears, click `Continue`.

![Missing partition table warning in balenaEtcher](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_etcher_no_partition_table_en.webp)

3. Click `Select target`.

![Click Select target in balenaEtcher](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_etcher_select_target_en.webp)

4. Select the drive that corresponds to NanoKVM Go (listed as `Compute Module`) and click `Select 1`.

![Select the NanoKVM Go drive in balenaEtcher](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_etcher_choose_disk_en.webp)

5. Click `Flash!` and wait for the flashing to finish.

![balenaEtcher starting the flash](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_etcher_write_progress_en.webp)

6. balenaEtcher reports `Flash Completed!` once the image has been written.

![balenaEtcher reports Flash Completed](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_etcher_complete_en.webp)

## Flash the Image with ImageUSB (Windows)

1. Open ImageUSB and click `Refresh Drives`. The NanoKVM Go device (`Linux File-Stor Gadget`) should appear in the list.

![Click Refresh Drives in ImageUSB](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_refresh_drives.webp)

2. In `Step 1`, select the USB drive that corresponds to NanoKVM Go.

![Select NanoKVM Go in ImageUSB](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_select_device.webp)

3. In `Step 2`, select `Write image to USB drive`.

![Select write image mode in ImageUSB](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_write_mode.webp)

4. In `Step 3`, click `Browse` and select the downloaded NanoKVM Go image file.

![Select the NanoKVM Go image in ImageUSB](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_select_image.webp)

5. In `Step 4`, click `Write` to start flashing.

![Click the ImageUSB write button](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_start_write.webp)

6. Click `Yes` in the confirmation dialog to confirm the write.

![Confirm the ImageUSB write operation](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_confirm_write.webp)

7. Wait for flashing to complete.

![ImageUSB writing the image](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_write_progress.webp)

8. `Imaging Completed!` appears once the image has been written.

![ImageUSB flashing complete](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_complete.webp)

After flashing is complete, safely eject the USB device, disconnect the USB cable, reconnect NanoKVM Go, and wait for the system to boot.

> Do not disconnect USB or close the flashing tool during flashing. Otherwise, the image may fail to write correctly.

## Flash the Recovery Image

### Download the Recovery Image

Download the recovery image from MEGA:

- [MEGA](https://mega.nz/folder/N5ZTGaAB#vWbMjiaVzgcOP8d0QP8pUg)

Open the MEGA link and go into the `NanoKVM-Go` folder:

![NanoKVM-Go folder in the MEGA share](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_recovery_mega_folder.webp)

That folder holds the recovery images along with a readme:

![Recovery images and readme inside the NanoKVM-Go folder](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_recovery_mega_files.webp)

Pick the image that matches your device:

- NanoKVM Go: `NanoKVM-Go_Recovery_*.img.xz`
- NanoKVM Go+: `NanoKVM-Go_GoPlus_Recovery_*.img`

### Flash Method

Flash it exactly as you would a normal image, following **Flash the Image with balenaEtcher** or **Flash the Image with ImageUSB** above.

> The recovery image overwrites the system partitions and settings. Back up important data before you start.

### Complete the Recovery on the Device

When flashing is done, release the flashing-mode button instead of holding it, cut power to the device, then power it back on. NanoKVM Go boots straight into the recovery flow and shows the following screens in order:

> Recovery takes a few minutes. Keep the device powered the whole time: do not cut power and do not unplug the USB cable.

1. `WARNING` appears, noting that the system and settings will be overwritten. With power connected, tap `START REPAIR` to begin.

![Warning screen shown before the recovery image is written](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_repair_confirm.webp)

2. `Writing recovery` appears while the recovery partition is written, taking about 10 seconds.

![Writing the recovery partition](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_repair_writing_recovery.webp)

3. `Verifying recovery` appears while the recovery partition is verified, taking about 10 seconds.

![Verifying the recovery partition](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_repair_verifying_recovery.webp)

4. `Writing system` appears while the system partition is written, taking about 100 seconds.

![Writing the system partition](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_repair_writing_system.webp)

5. `Verifying system` appears while the system partition is verified, taking about 110 seconds.

![Verifying the system partition](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_repair_verifying_system.webp)

6. `REPAIR COMPLETE` and `100%` appear, and the device restarts on its own after 5 seconds. That ends the recovery flow.

![Recovery complete at 100 percent](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_repair_complete.webp)

If power is lost or the write fails partway through, the screen shows `REPAIR STOPPED` and asks you to re-enter USB flashing mode and flash the image again. Repeat the flashing steps above.

![REPAIR STOPPED shown after an interrupted recovery](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_repair_stopped.webp)
