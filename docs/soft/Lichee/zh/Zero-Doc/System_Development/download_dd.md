---
title: linux烧录镜像

---

## 准备

- 先去[下载站 - Sipeed](https://dl.sipeed.com/shareURL/LICHEE/Zero/) 或者 [百度网盘](https://eyun.baidu.com/s/3htTXfaG#sharelink/parent_path=%2F%E6%B7%B1%E5%9C%B3%E7%9F%BD%E9%80%9F%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&path=%2F%E4%B8%8B%E8%BD%BD%E7%AB%99%E6%96%87%E4%BB%B6%2FLICHEE%2FZero) 获取镜像。
  余下内容以 Zero_pub_V0.3.gz [点我跳转](https://dl.sipeed.com/shareURL/LICHEE/Zero/SDK) 压缩包里面的镜像为例

- TF卡

- X86-Linux 系统

## 烧录步骤

### 获得SD卡路径

打开 Linux 的终端界面（也就是命令行）
插入内存卡
使用 `sudo fdisk -l` 命令查看内存卡

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

使用`umount`命令取消挂载

```shell
(base) [Desktop] umount /dev/sdb1                                              
(base) [Desktop] umount /dev/sdb2 
```

### 写入镜像

- 写入前自行先解压出 .`img` 文件

这里使用 `dd` 来烧录镜像，一般 dd 指令的基本用法如下：

`sudo dd if=镜像 of=/dev/卷标 `

例如我们使用下面的命令来烧录：

```bash
sudo dd if=test.img of=/dev/sdb bs=1M status=progress oflag=direct
```

if 后面接的是想要烧录的镜像，of 指向烧录位置，可以是设备或者文件，bs指块大小，status 为显示烧录状态，oflag表示dd方式，这里选择直连（即不复制到内存中）

等到终端自行退出到可输入模式后就已经完成烧录了
