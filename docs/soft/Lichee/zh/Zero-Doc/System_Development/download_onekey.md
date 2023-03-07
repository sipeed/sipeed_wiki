---
title: Windows 下烧录指南
---

> 最方便的镜像烧录方法，类似于ghost一键装机

## 准备：

- 先去下载站获取镜像 dl.sipeed.com [点我跳转](https://dl.sipeed.com/shareURL/LICHEE/Zero/Images)。
  余下内容以 Zero_pub_V0.3.gz [点我跳转](https://dl.sipeed.com/shareURL/LICHEE/Zero/SDK) 压缩包里面的镜像为例

- 下载[Etcher](https://www.balena.io/etcher/ "Etcher")

- 下载[SD Card Formatter](https://www.sdcard.org/downloads/formatter/eula_windows/SDCardFormatterv5_WinEN.zip "SDCardFormatter")

## 烧录步骤：

> 格式化内存卡是为了能够成功烧录~

-  打开SD卡格式化工具

    - 点击`Refresh`来刷新盘符
    - 在 `Select card` 选中目标盘符
    - 点击右下角 `Format` 
    - 等待弹框提示 `successful`

<img src="./../static/System_Development/format.gif" >


-  打开Etcher

    - 解压镜像，得到 .img镜像文件
    - 点击`Flash from file`,选中想要烧录的镜像包
    - 点击`Select target`选中sd卡
    - 点击`Flash`烧录
    - 等待烧录完成

<img src="./../static/System_Development/flash.gif" >


到此就已经结束烧录了。
