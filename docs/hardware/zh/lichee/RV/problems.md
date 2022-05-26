---
title: 相关问题
keywords: debian, Rv, Problam, apt, img, sipeed
---

## apt 相关

- 在使用默认debian镜像时，如果进行apt操作，发现以下报错：
  
> GPG error: http://ftp.ports.debian.org/debian-ports sid InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY E852514F5DF312F6

说明内置的密钥到期了，需要手工更新下密钥；下面是两种下载密钥的方式：
 - 网页下载：https://packages.debian.org/sid/all/debian-ports-archive-keyring/download
 - wget方式 `wget http://ftp.cn.debian.org/debian/pool/main/d/debian-ports-archive-keyring/debian-ports-archive-keyring_2022.02.15_all.deb`
  
将密钥拷贝（使用scp或者lrzsz工具）到LicheeRV板上，执行：

> sudo dpkg -i debian-ports-archive-keyring_2022.02.15_all.deb

即可更新密钥，然后可以正常进行apt更新：`sudo apt-get update`

## 启动无反应

- 确认自己在使用 PhoenixCard 的时候选择的是 `启动卡`
  ![](./../assets/RV/flash.png)
- 对于使用Tina系统的是可以用adb终端来连接进行通信
  直接将电脑与核心板相连即可
  ![](./../assets/RV/adb-shell.png)
- 对于debian系统只能使用串口来通信

## 86 panel 烧录后屏幕无反应/显示不对

需要在linux系统中使用下面命令来和对应的fex文件来覆盖板级配置
fex下载地址 https://dl.sipeed.com/shareURL/LICHEE/D1/Lichee_RV/SDK/board
覆盖指令为
```bash
sudo dd if=boot_package_XXX.fex of=/dev/sdX bs=1K seek=16400
```
上面命令中的 sdX 为 TF 卡在 linux 系统中的命名。

有问题的话可以去[论坛](https://bbs.sipeed.com/)发帖

