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

## ToolChain

[Here](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/Toolchain) is a toolchain for V831, it can be run in linux system.

## MaixPy3

For this device we suggest you use [Maixpy3] to develop , and its English documents will come out soon.

## SDK development

Now we have open V831 source sode here, use this https://github.com/Tina-Linux/tina-V83x if you need. 