---
title: 开箱体验
keywords: Linux, Lichee, TH1520, SBC, RISCV, unbox
update:
  - date: 2023-05-08
    version: v1.0
    author: wonder
    content:
      - Release docs
---

## Unboxing / Box contents

There are two versions of the LicheePi 4A board, the closed beta version and the official version.
The closed beta version was released in May 2023. There is only one version of the board with 8+8 (DDR+eMMC).
The official version is expected to release in June 2023. There will be a 8+32, 16+128 version, with some minor adjustments and fixes based on the feedback from the closed beta version users. The functionality and images will
stay the same as the closed beta version.

### Closed Beta Version

If you received the board as part of the closed beta program, you will receive the following package:
![package_alpha](./../../../../zh/lichee/th1520/lpi4a/assets/unbox/package_alpha.png)

The opened box will look like this：
![unbox_alpha](./../../../../zh/lichee/th1520/lpi4a/assets/unbox/unbox_alpha.png) 
the main body of LicheePi 4A is wrapped in black foam, and the other labeled parts are:
1. 30x30mm thermal grease pad, used to attach the heatsink to the CPU.
2. 30mm 5V cooling fan. The connector should be plugged into the 5V fan header on the board. Note: The red wire is the positive wire and should be connected to the + pole. The fan will not work if you reverse the polarity.
3. 2.4G WiFi Antenna, already connected to the IPEX socket. If it comes loose please re-attach it yourself.
4. USB-C cable, used for power supply and image flashing.

If you miss any part during unpacking, please contact customer service for help.


### Offical Version

(Scheduled to be released in June 2023)

### Optional Accessories

If you have purchased the optional accessories, these parts may also be included in the package:
![option_alpha](./../../../../zh/lichee/th1520/lpi4a/assets/unbox/option_alpha.png)
In the upper part of the picture is the optional RVDebugger Plus, which has JTAG+UART function. If you need to do low-level debugging, you can purchase it as an option.

The lower part of the picture is the optional 12V2A power adapter, if you need to connect a lot of power-consuming peripherals (such as USB, MIPI screen) to the board, you can buy it as an option.

A 5V 2A USB power supply can run the board with full-load at 1.85GHz

There will be an POE Power Add-on Module/Board in the future as well.

## Assembling the board

### SOM installation

By default, the LM4A SOM has been installed on the motherboard. If you need to upgrade/replace the SOM, you can follow the instructions below to remove and install the SOM

1. Removing the SOM:
   <table>
    <tr>
      <td colspan=2>Unlock the board by pushing the retainer tabs outwards and lift up the SOM</td>
    </tr>
    <tr>
      <td><img src="./../../../../zh/lichee/th1520/lpi4a/assets/unbox/unlock_som.png" alt="unlock_som"></td>
      <td><img src="./../../../../zh/lichee/th1520/lpi4a/assets/unbox/remove_som.png" alt="remove_som"></td>
    </tr>
   </table>

2. Installing the SOM:
   <table>
    <tr>
      <td colspan=2>First insert the SOM into the connector, ensure that it´s pushed all the way in and push down on both sides till the retainer clips automatically hold the board.</td>
    </tr>
    <tr>
      <td><img src="./../../../../zh/lichee/th1520/lpi4a/assets/unbox/insert_som.png" alt="insert_som"></td>
      <td><img src="./../../../../zh/lichee/th1520/lpi4a/assets/unbox/lock_som.png" alt="lock_som"></td>
    </tr>
   </table>

### Cooler Installation 

LicheePi 4A is a high performance SBC，you need to install an active cooler to dissipate the heat. Otherwise it might automatically throttle the frequency due to overheating and is unable to deliver the full performance.
1. Installing the thermal pad,
    take the thermal pad and remove the protective film from both sides, then place the thermal pad in the location shown below, the thermal pad can be re-arragnet if needed. Please ensure that you cover the main CPU as well as both memory chips fully.
    ![silicone_pad](./../../../../zh/lichee/th1520/lpi4a/assets/unbox/silicone_pad.png)

2. Installing the fan / heatsink
    Allign the 30x30mm heatsink and fan with the thermal pad and press down lightly.
    ![insert_fan](./../../../../zh/lichee/th1520/lpi4a/assets/unbox/insert_fan.png)

3. Connecting the cooling fan
    By default the cooling fan should already be plugged in when you received the board. If the fan power cables was unplugged, please re-plug it as shown in the image below.
    Pay attention to the polarity of the fan, in case the fan is plugged-in backwards it will not work.
    Note: The fan is controlled by a linux kernel driver which needs to be configured correctly to work. (fan does not spin per default)
    If you are unsure if the fan works, you can test it by plugging it into a +5V and GND pin on the 20-pin GPIO header.
    ![insert_fan_cable](./../../../../zh/lichee/th1520/lpi4a/assets/unbox/insert_fan_cable.png)

### WiFi Antenna Installation 

The WiFi antenna is already connected when you receive the board. If it got unplugged, here is how to install it:
![insert_ant](./../../../../zh/lichee/th1520/lpi4a/assets/unbox/insert_ant.png)

### POE module installation

The POE module can be purchased seperatly. It´s a 5V POE power module with a length of 35.6mm, which can be soldered to the POE POWER holes on the development board.

The PoE module should be installed like this：

   <table>
    <tr>
      <td><img src="./../../../../zh/lichee/th1520/lpi4a/assets/unbox/unbox_poe_0.jpg" alt="poe_back"></td>
      <td><img src="./../../../../zh/lichee/th1520/lpi4a/assets/unbox/unbox_poe_1.jpg" alt="poe_front"></td>
    </tr>
   </table>

### Assembly completed

This is how the fully assembled board looks like:
![assemble_ok](./../../../../zh/lichee/th1520/lpi4a/assets/unbox/assemble_ok.png)

## Booting the board

LicheePi 4A is pre-loaded with a basic system image, so you can try it out directly!

Note: The pre-loaded system image might be very old. After you booted the system for the first time, please have a look at the next section on how to flash / update the image.

Use an HDMI cable (not included) to connect a display (not included) to the HDMI port of LicheePi 4A. Use the supplied USB-C cable to connect the board to a USB power supply (not included) with at least 5V and 2A output.
The LicheePi 4A will automatically boot into the default image and the login screen should appear within 30 seconds.
![boot_login](./../../../../zh/lichee/th1520/lpi4a/assets/unbox/boot_login.png)

The default image has two types of account password configurations, you can try both:
1. User：`root`，`debian`，`sipeed`； the password for all accounts is `licheepi`
2. User: `debian`，password: `debian`； user: `sipeed`，password: `licheepi`

If you followed the above procedure, but your display fails to show any image, please check the following:
1. Check whether the USB-Power supply is connected correctly, works and whether the power LED is lit on the board.
2. Check that the heatsink is installed correctly and that the fan is spinning.
3. Check that the HDMI connection is correct and that the display is turned on and the correct input is selected.
4. It might be the case that there is no pre-loaded image from the factory, in this case check the next section on how to flash an image.
5. If none of the above works, please contact us for support.

## Board hardware overview

After booting up the board for the first time, let´s take a look at the hardware of LicheePi 4A, so you can get familiar with it and maybe do some maintenance work in the future.
![pi_view](./../../../../zh/lichee/th1520/lpi4a/assets/unbox/pi_view.png) 

### Overclocking

The nominal operating frequency of the TH1520 is 1.85GHz, and we only guarantee that the board you receive can work stably at 1.85GHz.
If you are an enthusiast you can try to overclock the board to 2GHz, but we don´t guarantee that the board will work stable at this frequency.
After some testing, about 80% of the boards can boot into the system when overclocked to 2GHz and about 50% of the boards sucessfully pass the stress test at 2GHz.

### USB Power Limitation

The maximum input power of the board is 12V at 2A which is 24W. After it is converted to 5V on the board, there is about 20W of effective power available.

In order to provide maximum power to the SOM (the SOM can pull up to 12W when overclocked), the output of the USB-Hub is limited to 1.5A. This is for the pre-production version of the board, the final version will have a higher current limit based on feedback from the community.
When you connect a large number of USB-Devices, you might exceed this current limit, in this case we recommend to use an external power supply for the USB devices.
If you need to disable the current limit, please do the following: TODO

### Known issues and limitations of closed beta version board

1. Booting is only supported from built-in eMMC flash. Booting from SD / SPI Flash is not supported. The official board version will have DIP-Switches to select the boot device.
2. HDMI level shifting may be incompatible with some monitors that prevent the setting of the resolution. You can try to use another monitor.
3. The cut-off frequency of the on-board audio high-pass filter circuit is too high (500Hz), which results in the loss of bass. The RC-Filter component values will be changed in the official version.

### Board info download links

[Datasheet](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/01_Specification)
[Schematic](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/02_Schematic)
[BOM](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/03_Bit_number_map)
[Dimensional Drawing](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/04_Dimensional_drawing)
[3D Model](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/05_3D_model)

## Other links

Online store: [Aliexpress](https://www.aliexpress.com/item/1005005532736080.html)

[Github](https://github.com/sipeed/LicheePi4A)
[Sipeed Site](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a)

Telegram: https://t.me/linux4rv

Contact email: support@sipeed.com