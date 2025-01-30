---
title: "Install TD driver on Windows"
date: 2019-02-15T19:21:19+05:30
draft: false
---

## Check for default windows driver

Insert Tang Primer into your computer and open Device Manager to see the information. It may be named `WinUsb Device` or `USB-JTAG-Cable` depending on the Windows version. Make sure USB VID:PID is `0547:1002`.

![device manager](./windows/no_driver.png "Check for default windows driver.")

![device manager win10](./windows/no_driver_win10.png "Check for default windows 10 driver.")

## Install drivers (Windows 7)

Double click on `WinUsb Device` to select update driver

![update driver 1](./windows/update_driver1.png "Update driver step 1")

![update driver 2](./windows/update_driver2.png "Update driver step 2")

Browse the folder and select the driver directory under the `TD installation directory`. Click OK to start the installation.

![Choose driver folder](./windows/choosefolder.png "Choose driver folder")

The installation is successful and can be seen in the device manager.

![Install success](./windows/installsuccess.png "Install success")

## Install drivers (Windows 10)

> Before installing the driver itself, make sure you [disable driver signature enforcement](https://social.technet.microsoft.com/wiki/contents/articles/51875.windows-10-how-to-install-drivers-which-are-not-digitally-signed.aspx) first, otherwise Windows 10 won't allow you to install the unsigned driver from Anlogic.

Double click on `USB-JTAG-Cable` to select update driver.

![update driver 1](./windows/update_driver1_win10.png "Update driver step 1")

![update driver 2](./windows/update_driver2_win10.png "Update driver step 2")

Browse the folder and select the `driver\win8_10_64` directory under the `TD installation directory`. Click OK. Then click on `Let me pick from a list of available drivers on my computer`.

![Choose driver folder](./windows/choosefolder_win10.png "Choose driver folder")

Click on `Have Disk...`, then select the directory you selected in the last step, then click OK.

![Install from disk](./windows/install_from_disk_win10.png "Install from disk")

Now select the `Anlogic usb cable v0.1` in the driver list and click Next to start the installation.

![Select driver](./windows/select_driver_win10.png "Select driver")

The installation is successful and can be seen in the device manager.

![Install success](./windows/installsuccess.png "Install success")

## Check if device detected by Tang Dynasty IDE

Click on Download button as shown in following image.

![TD GUI Mode](./linux/87078310026779781.jpg "Tang Dynasty SDK in GUI Mode.")

Plugin Tang Primer into your computer and hit Refresh buttion on Download Dialog box.

![TD Download Dialog](./linux/1823555291194601.jpg "Bitstream Download Dialog")

Congratulations, you have setup the TD driver on Windows.
