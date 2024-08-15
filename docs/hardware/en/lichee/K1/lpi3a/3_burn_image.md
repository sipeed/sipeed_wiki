---
title: Burn Image
keywords: Linux, Lichee, K1, SBC, RISCV, image
update:
  - date: 2024-07-30
    version: v1.0
    author: zepan
    content:
      - Release docs
---

## Get Images
### Bianbu 
![bianbu](./assets/image/bianbu.png) 
LicheePi3A has been supported by the official bianbu image of Spacemit
You can go to the official mirror site of Spacemit https://archive.spacemit.com/image/k1/version/bianbu/ ）Download, please note to download images v1.0.11 or higher



### Fedora 
![fedora](./assets/images/fedora.png)
https://images.fedoravforce.com/LicheePi%203A

### openKylin 
![openKylin](./assets/images/openkylin.png)
https://www.openkylin.top/downloads/

### Deepin 
![deepin](./assets/images/deepin.jpg)   
https://ci.deepin.com/repo/deepin/deepin-ports/cdimage/20240815/riscv64/


## Get burning tools
LicheePi3A can be burned using fastboot or titan burning tools.
[Windows]( https://cloud.spacemit.com/prod-api/release/download/tools?token=titantools_for_windows_X86_X64 )
[Linux]( https://cloud.spacemit.com/prod-api/release/download/tools?token=titantools_for_linux_64BIT_APPIMAGE )
Download the latest tools from the official website of Spacemit:
https://developer.spacemit.com/#/Documentation
Burning Guide:
https://bianbu.spacemit.com/installation_and_upgrade

## Burn eMMC
### Use Titan Flasher to flash the device
When the board detects that the BOOT key is pressed during startup, it can enter the burning mode. That is to say, first press and hold the BOOT key, then plug it in or short press the RESET key to enter the burning mode.
![flash1](./assets/image/flash1.png) 
![flash2](./assets/image/flash2.png) 
![flash3](./assets/image/flash3.png) 

### Use Fastboot to flash the device
The zip firmware ending in. zip can be used to flash the device with fastboot after decompression.
**Prerequisite**
1. The device has been plugged in with a USB data cable and connected to a PC;
2. Install the fastboot command on the computer.
**Flashing steps**
1. Unzip firmware
2. Download the flashing script [flash all. zip](https://archive.spacemit.com/image/k1/flash-all.zip) , and extract it to the firmware directory;
3. Enter fastboot mode
```reboot fastboot```
Wait for the device to restart and enter fastboot mode:
1. Run the flash all script and wait for the flashing to complete;
2. When running flash all. sh on a Linux PC, be sure to grant executable permissions first; Run flash all. bat on Windows PC;
3. After flashing the device, simply power it on again to enter the system.
##Burn TF card
The firmware ending in img.zip is the sdcard firmware. After decompression, it can be written to the sdcard using the dd command or balenaEtcher. Please note that this firmware is not compatible with eMMC.
**Steps**
1. Write the firmware to the sdcard;
2. Insert the sdcard into the device;
3. The device can be started by powering it on.
   
## LPi4A compatibility settings
Note that if you are using the LPi4A motherboard, the differences in the motherboard may cause the USB A port under the default image to be unusable. For the first use, you need to connect to the serial port or network, enter the device terminal, and replace the dtb
Under/boot/spacemit/6.1.15/, overwrite k1-x_lpi3a_4a.dtb with k1-x_lpi3a.dtb and restart to use USB

## LCD support
The default image only has HDMI output enabled. If LCD support is required, dtb needs to be replaced
Under/boot/spacemit/6.1.15/, overwrite k1-x_lpi3a_lcd.dtb with k1-x_lpi3a.dtb and restart to use the LCD
Please note that this dtb must be connected to an LCD in order to use it




