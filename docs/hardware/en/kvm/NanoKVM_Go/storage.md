---
title: Image Mounting and File Sharing
keywords: NanoKVM Go, image mount, ISO, IMG, file sharing, virtual U-disk, removable disk
---

## Introduction

In addition to video, audio, keyboard, mouse, and the virtual network adapter, the main USB-C port of NanoKVM Go also presents a USB storage device to the target machine. That storage has two uses, and both start from `Images & File sharing` in the floating toolbar:

+ `Disk mount`: hands an ISO or IMG file to the target machine, which sees an optical drive or a hard disk. Use it to install an operating system, boot a rescue environment, or repair a system.
+ `File sharing`: hands the NanoKVM Go shared volume to the target machine, which sees a removable disk. Use it to move files in either direction.

Click the hard drive icon in the floating toolbar at the top of the web console to open these two options:

![The Images & File sharing entry in the floating toolbar](./../../../assets/NanoKVM/go/storage/nanokvm-go-storage-entry-en.webp)

## How It Works

Both features share the same USB storage device. NanoKVM Go presents an image file or the shared volume on the device to the target machine over USB mass storage, so only one medium is available to the target machine at a time.

```text
Control device (browser)
|
| upload ISO / IMG, manage files on the shared volume
v
NanoKVM Go
|
| Disk mount: image file (ISO / IMG)
| File sharing: shared volume (exFAT)
|
| over USB mass storage, one medium at a time
v
Target machine
```

The two features differ in what they present:

+ `Disk mount` uses the image file in `/data` directly. Nothing is copied and no extra space is used.
+ `File sharing` uses an exFAT shared volume that is normally mounted at `/data`. While the volume is not attached to the target machine, the web file manager can read and write it.
+ While the shared volume is attached to the target machine, local `/data` becomes read-only and the web page can only browse and download.
+ Mounting an image first ejects the shared volume; eject the current medium before switching to the other feature.

The target machine only sees the disk or optical drive that NanoKVM Go provides, not the NanoKVM Go system files.

## Preparation

Before using either feature, confirm that:

+ NanoKVM Go is connected to the target machine over USB-C;
+ `Virtual Disk` under `Settings > Device` has been initialized. On first use, turn the switch on, choose a capacity, and initialize it; see [Initialize the Shared Volume](#Initialize-the-Shared-Volume);
+ HID-Only mode is off. HID-Only makes the USB port emulate a keyboard and mouse only, and disables both features;
+ no upload or download is running.

> The first initialization of `Virtual Disk` erases `/data`, including existing image files and the shared volume, and cannot be undone. Download the images you still need to your computer first.

## Disk Mount

### Add an Image

Open `Disk mount` from `Images & File sharing`, then choose one of the options under `Add media`:

+ `Upload ISO / IMG`: drag an image file into the window, or click to choose a file and upload it from the control device;
+ `Download from URL`: enter the image URL and NanoKVM Go downloads it directly. A download can be paused, resumed, or cancelled;
+ `SCP`: upload the image to the `/data` directory on NanoKVM Go;
+ put the image on the shared volume through `File sharing`; the image then appears under `Images`.

Both upload methods accept an optional SHA-256 checksum. When you provide one, only a file whose checksum matches is added to the list.

Images are listed under `Images` with their size and file system type.

![The Disk mount window](./../../../assets/NanoKVM/go/storage/nanokvm-go-storage-disk-mount-en.webp)

### Choose a Mount Mode

The mount mode decides what kind of device the target machine sees:

| Mount mode | Target machine sees | Access | Supported images |
| --- | --- | --- | --- |
| `Mass storage` | A hard disk | Read-only by default; writable after turning off `Read only` | ISO, IMG |
| `CD-ROM` | An optical drive | Always read-only | ISO, UDF |

The mode applies to the next mount. While an image is attached, eject it before switching modes.

### Mount an Image

1. Click the mount button next to the image.
2. Check the target machine for the new disk or optical drive.

![The mount button on the right of an image](./../../../assets/NanoKVM/go/storage/nanokvm-go-storage-mount-button.webp)

To boot from the medium, reboot the target machine, open the boot menu during POST (`F11`, `F12`, and `ESC` are common), then choose the NanoKVM Go disk or optical drive.

### Eject an Image

1. Eject the disk or optical drive safely from the target machine first.
2. Return to the web page and click the eject button next to the image.

![Once an image is attached, its button becomes eject](./../../../assets/NanoKVM/go/storage/nanokvm-go-storage-eject-button.webp)

If the target machine is still using the medium, the web page offers a forced eject. A forced eject re-enumerates the USB device, can lose data that has not been written back, and briefly disconnects the keyboard, mouse, and virtual network adapter. Avoid it when a safe eject is possible.

### Delete an Image

Images you no longer need can be deleted with the delete button. Deleted files are not moved to a recycle bin.

![The delete button on the right of an image](./../../../assets/NanoKVM/go/storage/nanokvm-go-storage-delete-button.webp)

The delete button is unavailable while the image is attached to the target machine. When sensitive-action protection is enabled, you must verify once more before deleting; see [Two-factor authentication](./two_factor_authentication.html).

## File Sharing

The flow is: put files on the shared volume from the web page, hand the volume to the target machine, then take the files from the removable disk. The local side is read-only while the target machine holds the volume, so turn `Virtual Disk` off before uploading.

### Initialize the Shared Volume

Create the shared volume the first time you use the feature:

1. Open `Settings > Device` and find `Virtual Disk`.
2. Turn on `Virtual Disk`. If the volume has never been initialized, the `Initialize Virtual Disk` window opens.
3. Choose a capacity in GiB and confirm.
4. When initialization finishes, `Images & File sharing > File sharing` becomes available and the removable disk appears on the target machine.

> Initialization erases `/data`, including image files stored there, and cannot be undone. The capacity cannot be changed afterwards; to use a different size you must disable the volume and initialize it again.

At this point the shared volume is already handed to the target machine and the web page is read-only. To put files on it, turn `Virtual Disk` off as described in the next section.

### Upload Files

While the shared volume is attached to the target machine, the web page can only browse and download. Take the volume back before uploading:

1. Turn off `Virtual Disk` under `Settings > Device`.
2. Open the `File sharing` window, click `Upload`, or drag files into the window.
3. When the upload finishes, the files appear in the current directory.

Creating a folder and deleting files also require `Virtual Disk` to be off. The new-folder and delete buttons are greyed out while the volume is attached to the target machine.

![The File sharing window](./../../../assets/NanoKVM/go/storage/nanokvm-go-storage-file-share-en.webp)

### Hand the Volume to the Target Machine

1. Make sure the files have finished uploading.
2. Turn on `Virtual Disk` under `Settings > Device`.
3. The removable disk appears on the target machine; open it and copy the files.
4. Turn `Virtual Disk` off when you are done. The files stay on the shared volume.

If an image is still mounted, eject it under `Disk mount` first. Toggling `Virtual Disk` re-enumerates the USB device, so the keyboard and mouse on the target machine drop for a moment.

### Disable the Shared Volume

After you turn off `Virtual Disk`, the settings page shows a `Disable` button. Disabling deletes the shared volume and frees the space it occupies. All files in it are lost, and the next enable asks for a capacity and initializes again.

## FAQ

### The target machine does not show a new disk

Check that:

+ the USB-C cable is connected to the target machine;
+ `Virtual Disk` under `Settings > Device` is enabled;
+ HID-Only mode is off;
+ when booting from the medium, USB boot is allowed in the BIOS/UEFI.

### The mount button is greyed out

Check that:

+ no image is already attached; eject the current image first;
+ no upload or download is running; wait for the transfer to finish;
+ in CD-ROM mode, whether the selected image is an ISO/UDF file.

### The Add media buttons are greyed out

The shared volume is attached to the target machine, so local storage is read-only. Turn off `Virtual Disk` under `Settings > Device`, then upload the image.

### The File sharing card is greyed out

The shared volume has not been initialized. Turn on `Virtual Disk` under `Settings > Device`, choose a capacity, and initialize it; see [Initialize the Shared Volume](#Initialize-the-Shared-Volume).

### Files cannot be uploaded from the web page

The shared volume is attached to the target machine and the web page can only browse and download. Turn off `Virtual Disk` to upload, create, and delete files again.

### Uploaded files do not appear on the target machine

Check that the upload finished, then check that `Virtual Disk` under `Settings > Device` is on. While the switch is off, the shared volume stays on NanoKVM Go and the target machine cannot see it.

### Files written by the target machine are missing from the web page

Click refresh. The target machine may not have written the data back to the disk yet, so wait a few seconds and refresh again.

### Are files lost when Virtual Disk is turned off?

No. Turning `Virtual Disk` off only takes the shared volume back from the target machine; the files stay on the shared volume. Only `Disable` deletes the shared volume and the files in it.

### Can disk mount and file sharing be used at the same time?

No. Both features share the same USB storage device, so only one medium is available to the target machine at a time.
