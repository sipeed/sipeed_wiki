# Install on Windows

> Edit on 2022.05.17

## Install TD

We can download TD install-package and get its license from [Download station](https://dl.sipeed.com/shareURL/TANG).
This may take a really long time to download.
But we need it to development tang primer

Install-package ：`TD_5.0.4_27252_Win7_64bit_NL.msi`
License file：`Anlogic_20220703.lic`

Double click the Install-package to install this software, and rename the license file Anlogic_20220703.lic as Anlogic.lic, then move the license file to the TD5.0.27252\license folder in the installed path.

**Note：license is valid before 2022.07.03 after when we don't support anymore**

Then we can use TD

## Install the USB serial port

Connect Tang Primer with computer and open device manager to see device information.
It may be named WinUsb Device or USB-JTAG-Cable duo to different Windows verison.
Make sure USB VID:PID is 0547:1002

- Windows7 without installing driver

![no_driver](./../../../../zh/tang/assets/get_started/no_driver.png)

- Windows10 without installing driver

![no_driver_win10](./../../../../zh/tang/assets/get_started/no_driver_win10.png)

### Install driver on windows7

Double WinUsb Device and choose 更新驱动程序(P) 
![update_drive1](./../../../../zh/tang/assets/get_started/update_driver1.png)
![update_drive2](./../../../../zh/tang/assets/get_started/update_driver2.png)

Select the driver directory where the TD installed. Click 确定 to install the driver.

![choosefolder](./../../../../zh/tang/assets/get_started/choosefolder.png)

After succeed installing,we can see this in device manager
![installsuccess](./../../../../zh/tang/assets/get_started/installsuccess.png)

### Install driver on windows10

> Before installing the driver itself, make sure you disable driver signature enforcement first, otherwise Windows 10 won’t allow you to install the unsigned driver from Anlogic.

Double click on USB-JTAG-Cable to select update driver 
![update_drive1](./../../../../zh/tang/assets/get_started/update_driver1_win10.png)
![update_drive2](./../../../../zh/tang/assets/get_started/update_driver2_win10.png)

Browse the folder and select the driver\win8_10_64 directory under the TD installation directory. Click OK. Then click on Let me pick from a list of available drivers on my computer.
![choosefolder](./../../../../zh/tang/assets/get_started/choosefolder_win10.png)

Click on Have Disk..., then select the directory you selected in the last step, then click OK. 
![install_from_disk_win10](./../../../../zh/tang/assets/get_started/install_from_disk_win10.png)

The installation is successful and can be seen in the device manager.
![installsuccess](./../../../../zh/tang/assets/get_started/installsuccess.png)

## Check if device detected by Tang Dynasty IDE

Click on Download button as shown in following image.
![](./../../../../zh/tang/assets/get_started/87078310026779781.jpg)

Plugin Tang Primer into your computer and click Refresh buttion on Download Dialog box.
![](./../../../../zh/tang/assets/get_started/1823555291194601.jpg)

Congratulations, you have setup the TD driver on Windows.