---
title: Usage
keywords: MaixII, MaixPy3, Python, Python3, M2dock, Tina, Openwrt
desc: maixpy  MaixII M2dock start to use
---

## Introduct openwrt

> Allwinnner V831 use Tina Linux, which is created from [OpenWrt](https://openwrt.org).

The OpenWrt is a Linux operating system targeting embedded devices. Visit [official-website](https://openwrt.org) and [official open repository](https://github.com/openwrt/openwrt) for more details.

For V831 we use adb shell to control it. Connect otg interface marked on board with computer.

---
- Fow Windows users, download the latest adb, add its path into system path and save it then use command `adb shell` to connect V831.
- For linux we need to install adb first, then run command `adb shell` to connect V831.
---

## Wireless connection

There is a 2.4G wireless module on M2Dock, with which we can connect to wireless network.

Because of the change of different system image, the ways to connect to wireless network on V0.5.4 system version and system version before V0.5.4 are different.

### V0.5.4

In this system version, we remove the way to connect wireless network by editting `wpa_supplicant.conf` file of the u-disk, and we use commands to connect wireless network.

We can see there are many linux commands about wifi in this system.

![wifi_test_command_list](./../../../zh/maixII/M2/asserts/usage/wifi_test_command_list.jpg)

Here we use `wifi_connect_ap_test` to connect wireless network, and we can use `wifi_scan_results_test` to scan the wireless network to see whether M2Dock detects your target network.

We use following command connect wireless network named `Sipeed_Guest` and its password is `qwert123`.

```bash
wifi_connect_ap_test Sipeed_Guest qwert123
```

Change `Sipeed_Guest` into your target wireless network name and change `qwert123` into your target wireless network password.

![wifi_test_connect_wireless](./../../../zh/maixII/M2/asserts/usage/wifi_test_connect_wireless.jpg)

From the connection message, we can see `192.168.3.158`, this is the IP address of M2Dock in this network enviroment.

We can run `ifconfig` on M2Dock to see the ip address, from which we see that the ip address is the same as the wireless network connection message.

![wifi_test_ifconfig](./../../../zh/maixII/M2/asserts/usage/wifi_test_ifconfig.jpg)

### V0.5.4 and previous image

Connect M2Dock USB-OTG port to computer, there is a u-disk in your computer.

Edit the `wpa_supplicant.conf` file which is in the u-disk,

![wap_conf_png](./../../../zh/maixII/M2/asserts/usage/wap_conf.png)

Change `yourWIFIname` and `yourWIFIpassword` into your target wireless network name and password. Then remove the u-disk from your system, use your operating system command to remove the u-disk, otherwise this file will be damaged. After removing the u-disk, reboot M2Dock by press RST KEY.

![wap_conf_gif](./../../../zh/maixII/M2/asserts/usage/wap_conf.gif)

### Update MaixPy3

Download MaixPy3 manually: https://pypi.org/project/maixpy3/#history

![maixpy3_download](./../../../zh/maixII/M2/asserts/usage/maixpy3_download.png)

Download the file whose name incorporates `cp38`, then rename it into `maixpy3-9.9.9-cp38-cp38-linux_armv7l.whl`, save it into the u-disk of M2Dock, reboot your board and maixpy3 will update automatically at boot up.

![maixpy3_install](./../../../zh/maixII/M2/asserts/usage/maixpy3_install.png)

Do Not Do Any Operation When Updating.

### Okpg package management

The opkg utility is the lightweight package manager used for upgrading the functionality of the system rather significantly by downloading and installing pre-made packages from package repositories.

#### Related commom commands

- opkg update # Update the updatable utility
- opkg upgrade # Upgrade the upgradable utility
- opkg list # list all utility
- opkg install # install target utility
- opkg remove # remove target utility
  
For example：

```bash
root@sipeed:/# opkg list 
MaixPy3 - 0.2.5-1
alsa-lib - 1.1.4.1-1
busybox - 1.27.2-3
busybox-init-base-files - 167-1612350358
ca-certificates - 20160104
curl - 7.54.1-1
dropbear - 2015.71-2
e2fsprogs - 1.42.12-1
eyesee-mpp-external - 1.0-1
eyesee-mpp-middleware - 1.0-1
eyesee-mpp-system - 1.0-1
```

## Test screen

- There is a flushing on screen after power on. this means the board is well working, and the flushing is caused by the system reset.

We can use command `cat /dev/urandom > /dev/fb0` to test the screen.

<center><img src="./../../../zh/maixII/M2/asserts/lcd_test.jpg" width="400"></center>

## Run python3

We can type `python3` in adb shell to run python3 in interative mode on V831. 

```python
import platform
print(platform.uname())
```

Actual operation on 2022.07.06

```bash
   __   _
  / /  (_)__  __ ____ __ ------------------------
 / /__/ / _ \/ // /\ \ /  sipeed.com (Neptune)
/____/_/_//_/\_,_//_\_\  ------------------------

root@sipeed:/# python3
Python 3.8.5 (default, Jun 14 2022, 09:51:56)
[GCC 6.4.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import platform
>>> print(platform.uname())
uname_result(system='Linux', node='sipeed', release='4.9.118', version='#3242 PREEMPT Tue Jun 28 04:03:38 UTC 2022', 
machine='armv7l', processor='')
```

## Test camera

We use MaixPy3 to test camera, let's run python3 first.

```python
from maix import camera, display, image 
display.show(camera.capture())
```

<center><img src="./asserts/hello_world.jpg" width="500"></center>

> If your screen doesn't display anything, make sure your mirror is the latest one and your drivers are correct.

## How to use USB camera

There are 2 USB Type-C ports on M2Dock. One masked UART is for the serial communication between this board and computer, another port masked with OTG is used for user-defined functions. We set it `usb_device` default, so we can use `adb` to control this board by default. And by `adb forware`, we can run jupyter code on M2Dock without network but only one usb cable.

To connect USB camera, we need to set the OTG port to be the usb_host. 

Run the following command on M2Dock to change its function, but remember this command will stop the communication between computer and M2Dock via ADB USB OTG port.

```bash
echo "usb_host" > /sys/devices/platform/soc/usbc0/otg_role
```

Then we can control the USB camera device which is in the /dev directory.

## How to set USB OTG port usb_device mode

The OTG port is usb device mode by default, by which we can control this board via `adb`. And maybe we changed its function to be a USB host for some reason and now we want to change it back to being a USB device. Just run the following command on M2Dock(You can run the following command on M2Dock via UART with 115200 baudrate).

```bash
echo "usb_device" > /sys/devices/platform/soc/usbc0/otg_role
```

## ToolChain

[Here](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/Toolchain) is a toolchain for V831, it can be run in linux system.

## MaixPy3

We suggest you use [Maixpy3](/maixpy3) to develop , and its English documents will come out soon.

## SDK development

Now we have open V831 source sode here, use this https://github.com/Tina-Linux/tina-V83x if you need. 