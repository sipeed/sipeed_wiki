---
title: MaixPy Development Board Power
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: MaixPy development board power
---

When we get the MaixPy development board

## Check the hardware

Check whether the hardware is damaged, and whether the camera and the screen are connected properly. Do not connect the cable reversely.


## Connect the hardware

Connect the Type C cable, one end of the computer and the other end of the development board

Check whether the device has been correctly identified:

In Windows, you can open the Device Manager to view

Under Linux, you can use `ls /dev/ttyUSB*` or `ls /dev/ttyACM*` to view, if not, you can search for `ls /dev`. The specific device name is related to the serial port chip and driver


If the device is not found, you need to confirm whether the driver is installed and the contact is good

After power on, if it is a new factory development board, it may display a red background. The foreground is a simple MaixPy introduction, including the official website address. The screen is still, and it needs to be changed by the following programming.

## Check the firmware version

Use **Serial Terminal** to open the serial port, and then reset, see the output version information, and [github](https://github.com/sipeed/MaixPy/releases) or [master branch](http://dl. sipeed.com/MAIX/MaixPy/release/master/) firmware version comparison, consider upgrading to the latest version according to the current version

such as:

```python
[MaixPy] init end

 __ __ _____ __ __ _____ __ __
| \/ | /\ |_ _| \ \ / / | __ \ \ \ / /
| \ / | / \ | | \ V / | |__) | \ \_/ /
| |\/| | / /\ \ | |> <| ___/ \ /
| | | | / ____ \ _| |_ /. \ | | | |
|_| |_| /_/ \_\ |_____| /_/ \_\ |_| |_|

Official Site: https://www.sipeed.com
Wiki: https://maixpy.sipeed.com

MicroPython v0.5.0-12-g284ce83 on 2019-12-31; Sipeed_M1 with kendryte-k210
Type "help()" for more information.
```

**View version number:**

  The version here is `v0.5.0-12-g284ce83`, you can also use the following code to view the version

> **Note:** The firmware can be obtained from the download site [dl.sipeed.com](http://dl.sipeed.com/MAIX/MaixPy/release/master/)

```python
import sys
print(sys.implementation.version)
```

If you encounter problems during the development process, you can also try to update the firmware to the latest version first

## Execute code

* After opening the serial port terminal, press the reset button of the development board to see the printed boot information and output

```shell
>>>
```

That is, we are waiting for us to enter the code. If there is no such symbol, there may be a program running automatically when booting up. You can press `Ctrl+C` to cancel the running program

* Then enter the program to execute

```python
>>> print("hello world")
hello world
>>>
```

## Paste and execute multiple lines of code

When we have multiple lines of code copied from other places, such as

```python
import os
f = os.listdir()
print(f)
```

* Copy the code first
* Press `Ctrl+E` on the serial terminal
* Paste the code
* Press `Ctrl+D` (note that if you did not press `Ctrl+E` before, it is a software reset command, MaixPy will soft reset), and then you can see all the codes are executed

```python
>>>
['boot.py','main.py','freq.conf']
>>>

```

> If the amount of data is relatively large, the serial port may lose data, which will result in a syntax error. You can try several times
