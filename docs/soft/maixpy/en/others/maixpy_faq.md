---
title: MaixPy FAQ
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: MaixPy FAQ
---




## What are the similarities and differences between MaixPy and C development, and how should I choose

MaixPy is a scripting language based on Micropython. It does not need to be compiled and parsed at runtime. It is simpler and more convenient to write, but it is not as real as C language at runtime.
So if you are a quick verification, novice, only python, less hair, etc., you can use MaixPy; those who are pursuing extreme performance efficiency or are familiar with C, and those who are not confident about the long-term stability of MaixPy can use C language development

## MaixPy IDE cannot successfully connect to the development board

**phenomenon:**

​ After getting the development board, I have been unable to connect to MaixPy IDE

* Check whether the firmware supports IDE, early firmware and firmware with `minimum` in the name are not supported
* Check whether the serial port is occupied (other software also opened the serial port)
* After clicking the connection, do not use it with the terminal tool at the same time, otherwise the serial port will be occupied and cannot be opened
* If you have been unable to successfully connect successfully, check:
  * Please check whether the development board model selection is wrong;

  * Observe whether there is any change on the development board screen, if there is no response, it may be the serial port selection error;

  * Try to upgrade to the latest [master branch firmware](http://cn.dl.sipeed.com/MAIX/MaixPy/release/master), and the latest MaixPy IDE software

> MaixPy version number is lower than 0.5.0_v0 does not support connection to MaixPy IDE


## The document webpage cannot be opened and the speed is slow

If you encounter some pages that cannot be accessed, please check whether the URL (path) is correct, and you can return to the home page (`maixpy.sipeed.com`) and re-enter.

For example, this URL is caused by clicking too quickly:

```shell
http://localhost:4000/zh/zh/get_started/how_to_read.html
```

The correct URL should be:

```shell
http://localhost:4000/zh/get_started/how_to_read.html
```

In addition, you can try another network line, such as connecting to a proxy, or changing mobile phone data. You can also use `cn.maixpy.sipeed.com` in China.

## The download speed of the download station is slow, and the file cannot be downloaded

If you encounter slow download speed at the dl.sipeed.com download station, you can use the domestic synchronization server cn.dl.sipeed.com to download, the path is the same, and it is synchronized once a day;
Some files provide CDN download links, which will be faster, for example, IDE has instructions in readme.txt

## Micro SD card cannot be read


Micro SD cannot be read phenomenon and solutions:

* Confirm whether the SD can be used normally on the computer, if not, the SD is damaged,

* The computer can be used normally, read SD, but MaixPy development board cannot be used:

  SD card is not formatted as MBR partition FAT32 format

* The computer can use the SD card normally. It is also confirmed that the disk format of the SD card is FAT32, but the MaixPy development board still cannot be used:

  Possible reasons: When some SDs leave the factory, there is no disk partition table in the sd, or the disk partition table type is not MBR

  Solution: Use a third-party disk management software to convert the sd partition table type to MBR, and format the sd format to FAT32

> Here **Diskgenius** is used to convert the disk partition table format

![Diskgenius](../../assets/other/diskgenius.png)


![GPT type to MBR](../../assets/other/diskgenius_sd_gpt_to_mbr.png)

![MBR Type](../../assets/other/diskgenius_sd.png)

* SD card does not support SPI protocol

At present, the hardware can only support SPI protocol reading, try to buy a regular card

For example: the two cards on the left side of the picture below are not supported by MaixPy drivers, the middle and right ones are supported, but the class 10 card in the middle has the fastest speed (up to 128GB tested and available)
> I have also tested several SanDisk, Kingston, and Samsung cards purchased online, and found that one of the Samsung cards cannot be used

![](../../assets/hardware/other/tf_sdcard.png)


## How much capacity does the SD card support?

Maximum tested 128GiB can be used

## Use SD to load file, model is unsuccessful

Phenomenon: We may encounter errors when loading the model during use.

Possible cause of the problem: sd is not compatible and the mount is unsuccessful

Verify whether the SD card is mounted:

```python
import os
print(os.listdir("/"))
>>['flash'] # SD card is not mounted

>>['flash','sd'] # Successfully mount the SD card
```

## Why is the frame rate reduced a lot when the IDE is connected

K210 has no USB peripherals, so it can only use the serial port to communicate with the IDE. The speed is not as fast as the USB device, so it will affect the frame rate. You can turn off the IDE camera preview


## Why the camera image previewed on the IDE is blurry

K210 has no USB peripherals, so it can only use the serial port to communicate with the IDE. The speed is not as fast as the USB device. Therefore, the picture is compressed. If you need to see a clear picture, please watch it on the screen of the development board, or save it as a picture and upload it to the computer View

Therefore, the image preview function of the IDE is mainly for teaching and demonstration. It is usually recommended to use the screen.
You can use the following code to set the preview quality
```python
sensor.set_jb_quality(95)
```
This sets the quality of the preview image to 95%, but the frame rate will be significantly reduced


## How to increase the camera frame rate

* Change to a better camera. For example, the frame rate of `ov7740` will be higher than that of `ov2640`. But the premise is that the camera circuit must be compatible with the circuit of the development board
* Increase the camera clock frequency (`sensor.reset(freq=)`), but be careful not to be too high, too high will make the picture worse
* You can compile the source code yourself, turn on the camera double buffering option (by default), and `sensor.reset(dual_buff=True)`, the frame rate will increase, but the memory consumption will increase accordingly (approximately 384KiB)


## IDE frame buffer imaging direction is incorrect, LCD display direction is incorrect

Since MaixPy supports many hardware models, the display direction will be incorrect when using MaixPy IDE or LCD display, then we need to rotate the image at this time;
Before correcting the display direction, we need to confirm whether the sensor direction is rotated (the image in the upper right corner of MaixPy IDE is the image directly output by the Sensor) or the LCD direction is rotated
Correction method:

- Sensor direction correction:

```python
# Set camera horizontal mirroring
# `enable`: 1 means to turn on horizontal mirroring 0 means to turn off horizontal mirroring
sensor.set_hmirror(enable)

# Set the camera to mirror vertically
# `enable`: 1 means turn on vertical mirroring 0 means turn off vertical mirroring
sensor.set_vflip(enable)
```

- lcd direction correction:

```python
# Set `LCD` screen orientation
# Parameters: `dir`: value range [0,3], rotate clockwise from `0` to `3`
# Return value: current direction, value [0,3]
lcd.rotation(dir)

# Set whether `LCD` is mirrored
# Parameters: `invert`: Whether to display in a mirror, `True` or `False`
# Return value: The current setting, whether it is mirrored or not, returns `True` or `False`
lcd.mirror(invert)
```

## After burning MaixPy, MaixPy fails to start

Phenomenon: We may encounter MaixPy cannot be started after burning MaixPy (it appears that the screen cannot be turned on, the screen is white, etc.).
The cause of the problem: A large part of this phenomenon is that the configuration file in the internal file system is read incorrectly, or the system configuration value we set (such as the gc heap value is too large) is incorrect and the system cannot be started.

Solution: Erase the file system (erase all flash)

Use kflash_gui to select the `erase` function in the upper right corner, then load the `MaixPy file system` template, the address becomes `0xD00000`, and the length becomes `3MiB`

Or download the erase firmware: erase.fpkg/flash_erase_16MB.bin/[erase_spiffs.kfpkg](https://cn.dl.sipeed.com/MAIX/MaixPy/release)


## Using JTAG debugger has been unable to connect to K210

Phenomenon: Using bare metal to develop K210, JTAG debugger has been unable to connect to K210

possible reason:
  1. There is a problem with the OpenOCD debugging environment (the details are not explained here)
  2. After burning ken_gen.bin, the JTAG debugging function of K210 will be permanently disabled

## After downloading and saving the script to MaixPy internal flash, the board cannot update the firmware and cannot start the script

-Possible phenomenon: After downloading and saving the script to MaixPy internal flash, the board cannot update the firmware, and the board cannot start


> The problem can be located from the hardware and software:

Possible hardware reasons:

​ TODO: To be updated

Possible software reasons:

  1. GPIO16 is pulled up in the program, which causes the automatic download point circuit to fail to pull down GPIO16, making K210 enter ISP mode

## kflash cannot burn/update MaixPy firmware

kflash_gui configuration options

- Development board model
  - The wrong development board model is selected
- Burning space (SRAM/Flash)
  - Wrong selection of burning space
- Baud rate & download speed mode
  - Download baud rate is too high
