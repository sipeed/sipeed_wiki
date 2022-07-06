---
title: Others
keywords: MaixII, MaixPy3, Python, Python3, M2dock
desc: maixpy doc: Others
---

- Here tells some other usages and related ways to deal with.

## Switch screen

Up to now this development board supports 1.3 inch, 2.4 inch and 2.8 inch spi screen, they can be bought from aliexpress in our [shop](https://sipeed.aliexpress.com/store/1101739727?spm=a2g0o.detail.100005.2.54df59cebhGZrI), consult the sale support for more information. And if you need to use other size of screen, you can email to support@sipeed.com for Commercial customization.

### Prepare

- The switch screen and its convert board (Consult sale support for more information)
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

The rule of dtb file name is shown as follows:

| File name | Fit screen | Fit camera |
| :----: | :----: | :---: |
| sipeed_240x240_vs3205.dtb | 1.3 inch | vs3205 |
| sipeed_240x240_sp2305.dtb | 1.3 inch | sp2305 |
| sipeed_240x320_vs3205.dtb | 2.4 inch and 2.8 inch |vs3205 |
| sipeed_240x320_sp2305.dtb | 2.4 inch and 2.8 inch |sp2305 |

Copy the compiled dtb file into the virtual U-disk, then run following commmand in adb shell.

```bash
sync  #Refresh contents
update_dtb /dev/mmcblk0 /root/sipeed_240x240_vs3205.dtb
reboot #Restart to apply
```

Then we succeed changing device tree. 
- 如果发现屏幕显示效果不对 说明选错了对应的设备树文件。重新弄一下即可

这里贴一张正常显示的图样

![](./asserts/show.jpg)