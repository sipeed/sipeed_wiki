---
title: Others
keywords: MaixII, MaixPy3, Python, Python3, M2dock
desc: maixpy doc: Others
---

- Here tells some other usages and related ways to deal with.

## Replace screen

Up to now this development board supports 1.3 inch, 2.4 inch and 2.8 inch spi screen, they can be bought from aliexpress in our [shop](https://sipeed.aliexpress.com/store/1101739727?spm=a2g0o.detail.100005.2.54df59cebhGZrI), consult the sale support for more information. And if you need to use other size of screen, you can email to support@sipeed.com for Commercial customization.

### Prepare

- The replace screen and its convert board (Consult sale support for more information)
- M2-Dock
- Latest system image

### Connect board

This board can connect 1.3 inch screen directly, but it can't connect with 2.4 inch or 2.8 inch screen directly because of different line sequence, so it's required to use convert board.

There is a mark 1 on convert board, which notes the direction to connect lcd screen and development board.

The mark 1 on screen is as below:

<html>
<style>
.imbox{
     display:flex;
     flex-direction: row;
     }
</style>
<div class="imbox">
    <img src="./../../../zh/maixII/M2/asserts/other/1.3.png" width=350>
    <img src="./../../../zh/maixII/M2/asserts/other/2.4.jpg" width=350>
</div>
</html>

The mark 1 on convert board is shown as below:

<img src="./../../../zh/maixII/M2/asserts/other/change.jpg" width=600>

The mark 1 on development board is shown as below:

<img src="./../../../zh/maixII/M2/asserts/other/V831.jpg" width=600>

Connect them as what is shown below

<html>
    <img src="./../../../zh/maixII/M2/asserts/other/not-connected.jpg" width=350>
    <img src="./../../../zh/maixII/M2/asserts/other/connected.jpg" width=350>
</html>

### Change device tree

- update_dtb application is for Allwinner tina linux
- The compiled dtb file can be download from [Download station](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/Toolchain)

This dtb file is compiled from kernel, and it's not suggested to be compiled by users because it's a bit difficult.

The rule of dtb file name is shown as following:

| File name | Fit screen | Fit camera |
| :----: | :----: | :---: |
| sipeed_240x240_vs3205.dtb | 1.3 inch | vs3205 |
| sipeed_240x240_sp2305.dtb | 1.3 inch | sp2305 |
| sipeed_240x320_vs3205.dtb | 2.4 inch |vs3205 |
| sipeed_240x320_sp2305.dtb | 2.4 inch |sp2305 |

Copy the compiled dtb file into the virtual U-disk, then run following commmand in adb shell.

```bash
sync  #Refresh contents
update_dtb /dev/mmcblk0 /root/sipeed_240x240_vs3205.dtb
reboot #Restart to apply
```

Then we succeed changing device tree. 

- If your screen displays incorrectly, this means you choose wrond dtb file, just reupdate it to fix this.

Here is a correct display picture. 

![correct display](./../../../zh/maixII/M2/asserts/show.jpg)

## Replace camera

Up to now MaixII-Dock development board support sp2305 and vs3205 these two cameras, and they are being sold in our online [store](https://sipeed.aliexpress.com/store/1101739727?spm=a2g0o.detail.100005.2.54df59cebhGZrI), consult our salers for help. If you want to use other camera, we can do commercial customization for you, or you can adapt the drivers by yourself.

Same as replacing screen, we need to update device tree to change driver.

### Prepare

- The replace camera
- MaixII-Dock
- Latest system mirror

### Connect camera

> Be careful of your camera direction, if you connect if in a wrong direction, your camera may burn out.

Just make sure the white point in the same place

<html>
<div class="imbox">
    <img src="./../../../zh/maixII/M2/asserts/other/camera_outlook_1.jpg" width=350 alt="camera top">
    <img src="./../../../zh/maixII/M2/asserts/other/camera_outlook_2.jpg" width=350 alt="camera bottom">
</div>
</html>

### Update device tree

> update_dtb is a tiny tool for Allwinner tina linux

Put your downloaded dtb file into the virtual disk created bu development board. Then run following commands in adb shell

```bash
sync  #Refresh content
update_dtb /dev/mmcblk0 /root/sipeed_240x240_vs3205.dtb
reboot #Reboot to apply
```

Then we succeed changing camera.

This dtb file is compiled from kernel, and it's not suggested to be compiled by users because it's a bit difficult.

| File name | Fit screen | Fit camera |
| :----: | :----: | :---: |
| sipeed_240x240_vs3205.dtb | 1.3 inch | vs3205 |
| sipeed_240x240_sp2305.dtb | 1.3 inch | sp2305 |
| sipeed_240x320_vs3205.dtb | 2.4 inch |vs3205 |
| sipeed_240x320_sp2305.dtb | 2.4 inch |sp2305 |