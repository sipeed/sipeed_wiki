---
title: dd镜像烧录

---

## 简介

在windows环境下可以方便的运用Win32DiskImage等工具烧录，而Linux环境下，用dd命令烧录不妨是个好选择，今天，本篇介绍dd烧录的操作步骤以及需注意的细节

两面性：

- 优点：对于喜欢此方式烧录镜像的人来说方便快捷

- 缺点：要敲命令行（对于初学者来说也是个学习了解类Linux环境的机会）

材料准备：

- 内存卡+读卡器+荔枝派Zero+支持完整指令集的x86设备一台（电脑）

或：

- U盘+荔枝派Zero+支持完整指令集的x86设备一台（电脑）

推荐待烧录存储器大小：512MB及以上

镜像下载位址：

- [下载站 - Sipeed](https://dl.sipeed.com/shareURL/LICHEE/Zero/SDK)

## dd烧录步骤


### 查看盘符路径

首先，打开Linux的终端机界面（也就是命令行）
插入一个大小合适的U盘或内存卡与读卡器的组合（荔枝派Zero较适于内存卡）
随便敲一个Fdisk -l 命令 便会有一堆文字列出

```shell
(base) [Desktop] sudo fdisk -l  

Disk /dev/sdb: 1.84 GiB, 1977614336 bytes, 3862528 sectors
Disk model: SD Card Reader  
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xfb8e04f1

Device     Boot Start    End Sectors  Size Id Type
/dev/sdb1        2048  67583   65536   32M  6 FAT16
/dev/sdb2       67584 980991  913408  446M 83 Linux
```

可以看出SD卡的盘符是/dev/sdb

### 取消系统对于该盘符的挂载


使用umount取消挂载

```shell
(base) [Desktop] umount /dev/sdb1                                              
(base) [Desktop] umount /dev/sdb2 
```

### 写入镜像

也就是dd命令

`sudo dd if=源路径 of=/dev/卷标 bs=1m［‘bs’为一次填充的容量］`

例如：

```
gzip -dc image/licheepi_zero_800x480_kernel.gz |sudo dd of=/dev/sdb bs=1M status=progress oflag=direct
```

gzip -d是解压镜像文件 -c是输出到标准输出，通过管道|传递给dd，of指向烧录位置，可以是设备或者文件，bs指块大小，status可以显示dd状态，oflag表示dd方式，这里选择直连（即不复制到内存中）



### 弹出内存卡


下电拔卡

或敲 `eject [内存卡位置]`

然后热插拔

### 完成前的事项


将内存卡装载到荔枝派Zero，上电运行，您就可开启您的荔枝派Linux之途
