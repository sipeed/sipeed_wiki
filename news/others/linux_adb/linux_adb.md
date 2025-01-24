---
title: Linux 连接不上 adb 设备
keywords: Linux, adb
date: 2022-07-21
tags: Linux, adb
---

这里写一下 Linux 系统下连接 M2Dock 后可能出现的 adb 问题

```bash
user@ubuntu:~$ adb shell
error: insufficient permissions for device 
```

<!-- more -->

在 linux 系统下连接 M2Dock 之后，使用 `adb shell` 后出现 `error: insufficient permissions for device` 。

```bash
user@ubuntu:~$ adb shell
error: insufficient permissions for device 
```

这时我们应该使用命令 `lsusb` 来查看一下是否成功连接到系统了

```bash
lee@ubuntu:~$ lsusb
Bus 001 Device 002: ID 18d1:0002 Google Inc. 
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

比如上面的 `Google Inc` 就代表 adb 设备。
执行 `lsusb` 没有 `Google Inc` 显示的话，就先检查一下 M2Dock 是否正常启动了（手摸屏幕试试温度是最快的方法），确定正常启动后可以更换数据线或者使用别的 USB 口等方式来尝试成功连接到电脑。

根据上面显示出来的 `Bus 001 Device 002: ID 18d1:0002 Google Inc.` 信息，我们需要在 `/etc/udev/rules.d/` 新建一个名为 `51-android.rules` 的文件，其内容应该为 `SUBSYSTEM=="usb", ATTRS{idVendor}=="18d1", ATTRS{idProduct}=="0002",MODE="0666"` ，其中 `ATTRS{idVendor}` 和 `ATTRS{idProduct}` 的值应该根据前面 `lsusb` 命令中的而修改，这里自己注意一下；最后更改文件权限：

> 小白一键式命令

```bash
sudo echo "SUBSYSTEM=="usb", ATTRS{idVendor}=="18d1", ATTRS{idProduct}=="0002",MODE="0666"" | sudo tee /etc/udev/rules.d/51-android.rules
sudo chmod a+x /etc/udev/rules.d/51-android.rules
sudo udevadm control --reload-rules
sudo service udev restart
sudo udevadm trigger
adb kill-server
adb start-server
```

上面的代码中，第一行写入了 `SUBSYSTEM=="usb", ATTRS{idVendor}=="18d1", ATTRS{idProduct}=="0002",MODE="0666"` 内容到 `/etc/udev/rules.d/51-android.rules` 文件。
第二行更改了对应的文件权限，最后重启了一下 adb 服务将权限激活。

接着重新插拔 USB，在使用 `adb shell` 就发现可以正常操作 M2Dock 了。

有什么问题的话可以在下方留言来一起探讨
