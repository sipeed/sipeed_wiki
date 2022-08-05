# Burn image

## System introduction

There are 2 system images for Lichee MaixSense(which will be called R329 below) 

| Image name   | armbian                                        | Tina                                                   |
| :----------- | :--------------------------------------------- | :----------------------------------------------------- |
| Description  | A lightweight Debian for arm development board | Linux system created by Allwinner Based on OpenWRT1404 |
| Feature      | Linux mainline, mutiple contents               | Tiny os                                                |
| Target users | Geeker, or newer                               | Customization requirements developer                   |

- For armbian system image it's required to use sd card over than 4GBi
- For Tina os it needs sd card over than 512MBi
- Low speed sd card will lead a bad experience

## Get image

### armbian system image

Download armbian system image from MEGA ：https://mega.nz/folder/1B4RFKpK#X0tMwHLHFQJvJ9POt_lXtg

The image named with maixpy3 means this image has installed MaixPy3 and its related drivers

This image file is created by [dd](https://en.wikipedia.org/wiki/Dd_(Unix)). It's suggested to use Etcher in Windows OS to burn image, and use Linux Terminal to burn image in Linux OS.


### Tina system image

Tina os need to be compiled by yourself, visit [https://github.com/sipeed/R329-Tina-jishu](https://github.com/sipeed/R329-Tina-jishu) for imformation.

Its burning method is the same as MaixII Dock, visit [Buring MaixII-Dock OS](./../M2/flash.md#Buring-system) for detailed steps.

## Burn system

### Windows burn system

Get software:
- [Etcher](https://www.balena.io/etcher/ "Etcher")
- [SD Card Formatter](https://www.sdcard.org/downloads/formatter/eula_windows/SDCardFormatterv5_WinEN.zip "SDCardFormatter")

Exteact the .img file from your downloaded image file, then use `SD Card Formatter` format your sd card, run Etcher, click `Flash from file`, choose the extracted .img file, click `Select target` and choose your sd card, click `Flash` to burn your sd card, wait it for finishing.

![burn](./../../maixII/M2A/assets/95133.gif)

### Linux burn system

Exteact the .img file from your downloaded image file, format the sd card, and open a terminal, use command `sudo dd if = xxx.img of=/dev/sdx bs=1M status=progress oflag=direct` to burn image into your sd card. The `xxx.img` is your extracted file, and the `of=/dev/sdx` is your sd card registered name.

![](./../M2A/assets/2021-08-05-11-44-49.gif)

We can also use Disks to burn sd card

![](./../M2A/assets/2021080511-46-53.gif)

After finishing burning, insert the sd card burned image file into Lichee MaixSense.

## Use Serial communication

- Plug in Type C cable into the usb port marked Debug, then you can use serial terminal to control this board

### Linux & macOS

For linux OS, use command `ls /dev/ttyUSB*` to see your device COM number, then use serial application to connect the board.

### Windows

Lichee MaixSense equips with CH340 as serial chip, but we need install its driver to use it.

[Click this](https://api.dl.sipeed.com/shareURL/MAIX/tools/ch340_ch341_driver) to download the driver for this serial chip, after installing this driver, you can find your device serial port from `Device manager`