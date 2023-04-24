---
title: 其他事项
keywords: MaixII, MaixPy3, Python, Python3, M2dock
desc: maixpy  其他事项
---

> 编辑于 2022年8月23日

这里讲述 V831 开发板的一些额外使用事项和相关解决方法

以下替换设备相关操作完成后，名称为 `maixhub` 的镜像里的 app 应用不再可用

## 切换屏幕

目前开发板支持的屏幕有 1.3寸、2.4寸、2.8寸 的 IPS 屏，且只是支持在[我们淘宝](https://sipeed.taobao.com/)上售卖的显示屏；对于别的屏幕有需求的，可以走商务通道进行定制。

### 准备

- 需要切换的屏幕与对应的转接板
- 开发板
- 最新[系统镜像](./flash.md)

### 屏幕连接

开发板可以直接与 1.3寸 屏幕连接，但是与 2.4寸 或 2.8寸 屏幕连接的话需要使用转接板

转接板上的接口一个 1 的标识符，是来确保不被反插的。屏幕排线上的 1 要和转接板、开发板的上 1 相位置对应。

屏幕标识的 1 如下所示

<html>
    <img src="./asserts/other/1.3.png" width=45%>
    <img src="./asserts/other/2.4.jpg" width=45%>
</html>

转接板上面的 1 如下所示

<img src="./asserts/other/change.jpg" width=600>

板子上的 1 如下所示

<img src="./asserts/other/V831.jpg" width=600>

具体接线参考下面两张图

<html>
    <img src="./asserts/other/not-connected.jpg" width=45%>
    <img src="./asserts/other/connected.jpg" width=45%>
</html>

### 切换设备树

- update_dtb 程序是给 Allwinner tina linux 专门写的应用。
- 编译好的设备树文件，可以在[下载站](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/Toolchain)中进行下载

该设备树文件是通过内核编译出来的，不推荐个人用户自行编译。设备树文件命名规则如下：

| 文件名字 | 可用屏幕 | 可用摄像头 |
| :----: | :----: | :---: |
| sipeed_2.8_240x320_vs3205.dtb | 2.8寸 | vs3205 |
| sipeed_2.8_240x320_sp2305.dtb | 2.8寸 | sp2305 |
| sipeed_2.4_240x320_vs3205.dtb | 2.4寸 | vs3205 |
| sipeed_2.4_240x320_sp2305.dtb | 2.4寸 | sp2305 |
| sipeed_1.3_240x240_vs3205.dtb | 1.3寸 | vs3205 |
| sipeed_1.3_240x240_sp2305.dtb | 1.3寸 | sp2305 |
| sipeed_1.3_240x240_ov2685.dtb | 1.3寸 | ov2685 |

将设备树文件存放到开发板中在电脑中显示的虚拟U盘中。
接着在 adb 终端里面执行下面命令

```bash
sync  #刷新一下文件
update_dtb /dev/mmcblk0 /root/sipeed_240x240_vs3205.dtb
reboot #重启设备来更新配置
```

即可切换设备树。

- 如果发现屏幕显示效果不对 说明选错了对应的设备树文件。重新换成正确的设备树即可

这里贴一张正常显示的图样

![show](./asserts/show.jpg)

## 更换摄像头

目前 MaixII-Dock 开发板目前支持的摄像头有 sp2305、vs3205、ov2685（只支持在官方店上再售卖的摄像头，有别的摄像头需求可以进行商务定制），摄像头之间的切换同样时需要更换设备树文件，更换方式上面的更换屏幕一样的。

### 准备

- 需要切换的摄像头模块
- 开发板
- 最新的[系统镜像](./flash.md)
- 编译好的设备树文件，可以在[下载站](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/Toolchain)中进行下载

### 连接摄像头

> **注意的是要摄像头的接法，不要把摄像头给接反了，摄像头的底板上有一个白点，开发板卡上也有一个白点，这两个白点要在同一边。如果接反了，摄像头烧毁了请自行再买一个吧**

<html>
<div class="imbox">
    <img src="./asserts/other/camera_outlook_1.jpg" width=350 alt="camera top">
    <img src="./asserts/other/camera_outlook_2.jpg" width=350 alt="camera bottom">
</div>
</html>

### 切换设备树

> update_dtb 程序是给 Allwinner tina linux 专门写的小工具。

将设备树文件存放到开发板中在电脑中显示的虚拟U盘中。
接着在 adb 终端里面执行下面命令

```bash
sync  #刷新一下文件
update_dtb /dev/mmcblk0 /root/sipeed_240x240_vs3205.dtb
reboot #重启设备来更新配置
```

即可切换设备树，该设备树文件是通过内核编译出来的，不推荐个人用户自行编译

| 文件名字 | 可用屏幕 | 可用摄像头 |
| :----: | :----: | :---: |
| sipeed_2.8_240x320_vs3205.dtb | 2.8寸 | vs3205 |
| sipeed_2.8_240x320_sp2305.dtb | 2.8寸 | sp2305 |
| sipeed_2.4_240x320_vs3205.dtb | 2.4寸 | vs3205 |
| sipeed_2.4_240x320_sp2305.dtb | 2.4寸 | sp2305 |
| sipeed_1.3_240x240_vs3205.dtb | 1.3寸 | vs3205 |
| sipeed_1.3_240x240_sp2305.dtb | 1.3寸 | sp2305 |
| sipeed_1.3_240x240_ov2685.dtb | 1.3寸 | ov2685 |

## 编译链

在[下载站](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/Toolchain)里有一个名为 `toolchain-sunxi-musl-pack-2021-01-09.tar.xz` 的文件，这是在 Linux 系统下为 V831 所使用的编译链。

有需求的可以自行尝试，但是对于 V831 还是推荐使用 MaixPy3 和 MaixHub。
