# F&Q

## Updating to Solve Issues

NanoKVM Pro will periodically update applications, and some issues may have been resolved in newer versions. Therefore, please try updating the application first.

## System Boot

### Green LED Blinking

The green LED serves as the power indicator for NanoKVM Pro. If a power source with insufficient capacity is connected, the green LED may blink due to voltage instability and fail to start up. Please disconnect all power connections and replace the power adapter.

## Network-related Issue

### WiFi Version NanoKVM-Pro ATX/Desk Missing WiFi Configuration Interface

To resolve this issue, please update to version 1.2.13 or above via Settings -> Check for Updates.

If you are unable to update via the web interface due to network issues, you can try resolving it by re-flashing the firmware: First download the firmware image for version [1.0.13](https://github.com/sipeed/NanoKVM-Pro/releases/tag/v1.0.13) or above, then follow the [operation steps](https://wiki.sipeed.com/hardware/en/kvm/NanoKVM_Pro/faq.html#Image-Burning-Methods) to complete the flashing process.

### NanoKVM-Pro ATX Unable to Configure Network via OLED Screen

In earlier versions \[1\], on the Wi-Fi variant of the ATX, long-pressing the `USR` button may cause the OLED to remain stuck on the `Starting` screen and fail to enter the Wi-Fi configuration page.

**Temporary Workarounds:**

* Connect the device via Ethernet, then log in to the Web interface and complete Wi-Fi configuration under `Settings` → `Device` → `Wi-Fi`.

* Connect the NanoKVM-ATX HID interface to a computer. On Windows, run `ipconfig` in the Command Prompt (use `ifconfig` on Linux), and locate the newly added IPv4 address in the form of `10.aaa.bbb.ccc` (for example, `10.223.155.100`). Access the NanoKVM Web interface via `10.aaa.bbb.1`, then complete Wi-Fi configuration under `Settings` → `Device` → `Wi-Fi`.

After successfully connecting to the network, it is recommended to update the application to version `>= 1.2.9` to permanently resolve this issue.

\[1\]: Affected versions: `1.1.8` ~ `1.2.8`

## Video Related Issues

### NanoKVM-Pro Cannot Display BIOS and Login Screen

When the host has multiple displays, it generally prioritizes the built-in screen or DP interface screen for displaying BIOS and login interface by default. Please refer to your motherboard manual to adjust the display priority, or use the loop-out interface to connect your display.

### DP Adapter Compatibility Issues

DP adapters come in two types: passive and active. Passive DP adapters are low-cost but may pose compatibility risks, manifesting as resolution lists not matching EDID, host wake-up failing to activate the screen, etc. Using the reset HDMI function can wake up the screen.

### Missing Resolution List, Inconsistent with EDID

The resolution list in the host display settings is determined by the host, EDID, (potentially existing) loop-out screen, and video adapter collectively. You can switch between different EDIDs on the web page to achieve the most reasonable compatibility.

### HDMI Icon Lit on NanoKVM Screen but No Video Displayed in Web Interface

NanoKVM-Pro supports video capture and loop-out functions. When only capturing video, it reports a maximum resolution of 4K30FPS to the host by default. When a loop-out display is connected, it reports a common resolution list.
For the default resolution and frame rate list, please refer to [here](https://wiki.sipeed.com/hardware/en/kvm/NanoKVM_Pro/extended.html#How-to-Modify-EDID).

When connected through video adapters or docking stations, the reported capabilities may change (e.g., reporting 4K60FPS capture support, which may cause capture failure). In such cases, adjust the display settings in the host system:

* On Windows: Go to `Settings` → `Display` → `Advanced Display Settings` → Select `NanoKVM-Pro` display → `Display Adapter Properties` → `List All Modes` → Choose the desired mode → Click Apply or OK.

![](./../../../assets/NanoKVM/pro/faq/res.png)

### Blurry Image, Not Matching the Captured Resolution

* In the image above, box ③: If the desktop resolution is lower than the active signal resolution, the captured image may appear blurrier than expected. Follow the steps above to output a clear image.

## Image Burning Methods

### USB Burning

NanoKVM Pro supports restoring or updating the system via USB image burning.

#### Preparation

* Prepare a USB data cable
* Download the latest NanoKVM Pro image file
* Prepare a burning tool (such as balenaEtcher, Rufus, or the dd command)

#### Burning Steps

1. **Download the Image and Burning Tool**
   * Visit the [NanoKVM Pro Release Page](https://github.com/sipeed/NanoKVM-Pro/releases/latest) to download the latest image file.
   * Download and install the burning tool [balenaEtcher](https://etcher.balena.io/).

2. **Enter Burning Mode**
   * Use the USB data cable to connect the NanoKVM Pro's HID interface to your computer.
   * Press and hold the User button on the NanoKVM, then power it on (or press the Reset button while powered on) until the orange LED turns off.
   * The device will then enter burning mode, and the orange LED will start flashing again. Check if your computer recognizes the new disk device.

<div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; align-items: flex-end;">
    <div style="text-align: center; flex: 1; max-width: 400px; min-width: 300px;">
        <img src="./../../../assets/NanoKVM/pro/faq/update_win.jpeg" alt="Windows Recognizing Device" style="width: 100%; height: auto; object-fit: contain; border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        <p style="margin-top: 8px; margin-bottom: 0; font-style: italic; color: #666; font-size: 16px;">Windows Recognizing Device</p>
    </div>
    <div style="text-align: center; flex: 1; max-width: 400px; min-width: 300px;">
        <img src="./../../../assets/NanoKVM/pro/faq/update_linux.jpeg" alt="Linux Recognizing Device" style="width: 100%; height: auto; object-fit: contain; border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        <p style="margin-top: 8px; margin-bottom: 0; font-style: italic; color: #666; font-size: 16px;">Linux Recognizing Device</p>
    </div>
</div>

3. **Burn Using balenaEtcher (Recommended)**
   * Launch balenaEtcher.
   * Click "Flash from file" and select the downloaded image file.
   * Click "Select target" and choose the recognized NanoKVM Pro device.
   * Click "Flash!" to start the burning process.
   * Wait for the burning to complete and verify.

<div align="center">
    <img src="./../../../assets/NanoKVM/pro/faq/flash.jpeg" style="width: 80%; height: auto; border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" alt="Flash">
</div>

* If prompted that the partition table cannot be found, it is normal; click continue.

<div align="center">
    <img src="./../../../assets/NanoKVM/pro/faq/miss_part.jpeg" style="width: 70%; height: auto; border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" alt="Missing Partition">
</div>

4. **Burn Using Command Line**

```bash
# Find the device name
sudo fdisk -l

# Decompress the image file (if it is in .xz format)
xz -dv 20250828_NanoKVMPro_1_0_10.img.xz

# Burn the image (replace /dev/sdX with the actual device name)
sudo dd if=20250828_NanoKVMPro_1_0_10.img of=/dev/sdX bs=4M status=progress

sudo sync
```

5. **Restart the Device**
   * After burning is complete, safely eject the device.
   * Disconnect the USB connection.
   * Reconnect the power, and the device will automatically start the new system.

#### Notes

* Ensure you select the correct device to avoid accidentally operating on other storage devices.
* Do not disconnect the power or remove USB connections during the burning process.
* The first startup may take a long time for initialization and configuration.
* If the orange light does not turn on or the disk device does not appear, please refer to the methods below to use AXDL for burning.

### AXDL Burning

AXDL is an official burning tool provided by Aixin, designed for burning AXP format system images. It currently supports Windows platform only.

#### Preparation

* Prepare a USB data cable.
* Visit the [NanoKVM Pro Release Page](https://github.com/sipeed/NanoKVM-Pro/releases) to download the latest AXP format image file.
* Download and install the AXDL tool and corresponding drivers [Download Link](https://dl.sipeed.com/shareURL/MaixIV/M4N-Dock/10_PC_Software).

#### Burning Steps

1. **Connect the Device**
   * Use the USB data cable to connect the NanoKVM Pro's HID interface to your computer.

2. **Configure the Burning Tool**
   * Open the AXDL tool.
   * Select the downloaded AXP format image file.
   * Click the start burning button.

   <div align="center">
       <img src="./../../../assets/NanoKVM/pro/faq/axdl.jpeg" style="width: 80%; height: auto; border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" alt="AXDL Burning Tool Interface">
   </div>

3. **Enter Burning Mode and Start Burning**
   * Press and hold the User button on the NanoKVM, then power it on (or press the Reset button while powered on).
   * The burning process will start automatically, wait for the progress bar to complete.
   * Wait until the prompt indicates that burning was successful; the entire process is complete.

### SD Card Flashing

The NanoKVM Pro Desk supports writing an image from an SD card to the internal eMMC to restore or update the system. Note: this only supports flashing an image from an SD card to the internal eMMC; the device cannot boot directly from the SD card.

#### Preparation

* Prepare an SD card with at least 8 GB capacity.
* Download the latest NanoKVM Pro SD image from the [NanoKVM Pro Releases](https://github.com/sipeed/NanoKVM-Pro/releases) page (the image is usually provided in a zip archive). Extract the archive and locate the `img` file.
* Prepare a flashing tool such as `balenaEtcher`, `Rufus`, or use the command-line `dd`.
* Prepare a USB card reader to connect the SD card.

#### Flashing Steps

1. Use `balenaEtcher` or `dd` to write the `img` file to the SD card (see the "USB Burning" section above for details on writing images).
2. Insert the flashed SD card into the NanoKVM Pro's SD card slot.
3. Disconnect power from the NanoKVM Pro Desk.
4. Press and hold the NanoKVM Pro Desk `User` button, then connect power.
5. When the orange LED starts flashing steadily, the device is writing the image from the SD card to the internal eMMC.
6. After flashing completes, the orange LED will stay solid, indicating success.
7. Disconnect power, remove the SD card, and reconnect power. The device will boot the new system from internal eMMC.

## Desk Version LCD Not Lighting Up

This may be caused by a loose FPC cable connection of the LCD during transportation.
Click [here](https://wiki.sipeed.com/nanokvmpro-lcd) to view the issue and repair details.

## Appearance Issues

### "Missing" Bottom Screw

In the first batch of NanoKVM-Desk units, the screw in the top-left position (shown below) was found to affect WiFi connection stability due to structural design considerations. This screw hole is intentionally left empty in later assemblies.

![](./../../../assets/NanoKVM/pro/faq/screw.jpg)

