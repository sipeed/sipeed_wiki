---
title: 主线 Linux
keywords: Linux, Longan, H618, SBC, ARM, Kernel, SDK, Develop
update:
  - date: 2023-12-08
    version: v1.0
    author: ztd
    content:
      - Release docs
---

该文档以 Ubuntu 22.04 为例，演示如何搭建 LonganPi 3H 开发环境并进行主线Linux的开发。

在正式合并入主线前，需要拉取 Github 仓库，获取patch开发，预计将于 2024Q1 合并入主线Linux。

## 环境配置
首先用 git 拉取仓库到本地，并安装工具链：
```shell
sudo apt install gcc-aarch64-linux-gnu mmdebstrap git 
git clone https://github.com/sipeed/LonganPi-3H-SDK.git
```

## 构建
然后进入到仓库所在目录，运行其中的脚本即可得到构建出的 uboot, kernel, dtb 和 rootfs。
```shell
cd LonganPi-3H-SDK
./mkatf.sh
./mklinux.sh
./mkuboot.sh
./mkrootfs.sh
```

生成的 Image 文件，设备树文件，会复制到该仓库目录下的 overlay/boot/ 文件夹中，生成的内核模块会复制到该仓库目录下的 overlay/usr/ 文件夹中。

接下来介绍 SDK 仓库的主要文件构成及其作用：
`linux` 文件夹下，存放的是 kernel 的 patch 文件，在运行 mklinux.sh 时会自动将这些 patch 打入到 kernel 源码中。

`uboot` 文件夹下，存放的是 uboot 的 patch 文件， 在运行 mkuboot.sh 时会自动将这些 patch 打入到uboot 源码中。

`overlay` 文件夹下有一些必要的文件，在运行 mkrootfs.sh 时会自动将这些文件覆盖到构建出来的 rootfs 中。
mkrootfs.sh 用于构建烧录所需要的根文件系统，可以根据需要选择是否跳过 debian rootfs 的构建，具体请看脚本中的注释。

构建完成后，接下来介绍如何制作一张启动 TF 卡，以及如何打包制作可烧录的 TF 卡启动镜像。

## 制作启动 TF 卡

准备一张 TF 卡，先进行格式化。
然后对 TF 卡进行分区（下面中的命令请修改为自己 TF 卡对应的**盘符**，请仔细核对并谨慎操作），下面步骤使用 fdisk 为 TF 添加两个分区，boot 分区大小为 64M，剩余空间分配给根文件系统（uboot烧录到裸分区中，一般位于 TF 空间中的前1M）：
```shell
sudo fdisk /dev/sdc
n
p
1
2048
+64M
n
p
2
# 完整交互信息如下：
ztd@ztd-desktop:~$ sudo fdisk /dev/sdc

Welcome to fdisk (util-linux 2.37.2).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0x0d923c5e.

Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p): p
Partition number (1-4, default 1): 1
First sector (2048-60506111, default 2048): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-60506111, default 60506111): +64M

Created a new partition 1 of type 'Linux' and of size 64 MiB.

Command (m for help): n
Partition type
   p   primary (1 primary, 0 extended, 3 free)
   e   extended (container for logical partitions)
Select (default p): p
Partition number (2-4, default 2): 2
First sector (133120-60506111, default 133120): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (133120-60506111, default 60506111): 

Created a new partition 2 of type 'Linux' and of size 28.8 GiB.
```
接下来按两次回车，即可将剩余空间都分配给根文件系统。分区完成后，先不要退出 fdisk ，还需要设置第一个分区为 boot 分区：
```shell
t
1
c
a
1
# 完整交互信息如下：
Command (m for help): t
Partition number (1,2, default 2): 1
Hex code or alias (type L to list all): c

Changed type of partition 'Linux' to 'W95 FAT32 (LBA)'.

Command (m for help): a
Partition number (1,2, default 2): 1

The bootable flag on partition 1 is enabled now.
```
设置完成后，输入 p 来检查刚刚的分区信息是否有误：
```shell
Command (m for help): p
Disk /dev/sdc: 28.85 GiB, 30979129344 bytes, 60506112 sectors
Disk model: Storage Device  
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x0d923c5e

Device     Boot  Start      End  Sectors  Size Id Type
/dev/sdc1  *      2048   133119   131072   64M  c W95 FAT32 (LBA)
/dev/sdc2       133120 60506111 60372992 28.8G 83 Linux
```

确认无误后，输入 w 并按下回车将刚刚的分区信息写入：
```shell
Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
```

接下来对**分区**进行格式化：
```shell
sudo mkfs.vfat -F 32 -n "boot" /dev/sdc1
sudo mke2fs -t ext4 -F -L "rootfs" /dev/sdc2
```

格式化完成后烧录 uboot：
```shell
sudo dd if=build/u-boot-sunxi-with-spl.bin of=/dev/sdc bs=1k seek=8 conv=fsync
```

烧录 kernel：
```shell
mkdir -p /tmp/kernel
sudo mount /dev/sdc1 /tmp/kernel
sudo cp -r overlay/boot/* /tmp/kernel
sync
sudo umount /tmp/kernel
```

烧录 rootfs：
```shell
mkdir -p /tmp/rootfs
sudo mount /dev/sdc2 /tmp/rootfs
sudo tar -vxf build/rootfs.tar -C /tmp/rootfs/
sync
sudo umount /tmp/rootfs
```

完成上述步骤后，就得到了一张启动 TF 卡。

## 制作 TF 卡启动镜像

首先制作空的 img 文件：
```shell
export DATE=$(date +"%Y%m%d")
dd if=/dev/zero of=LPI3H_${DATE}.img bs=1M count=3072
```

接下来对该 img 文件进行分区操作。类似地，使用 fdisk 命令，将其分为 boot 分区和 rootfs 分区：
```shell
# 过程类似，此处不再赘述
fdisk LPI3H_${DATE}.img
n
p
1
2048
+64M
n
p
2
# 两次回车
t
1
c
a
1
w
```

使用 `fdisk -l LPI3H_${DATE}.img` 查看分区信息：
```shell
Disk LPI3H_20231215.img: 2.5 GiB, 2684354560 bytes, 5242880 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xf417d095

Device              Boot  Start     End Sectors  Size Id Type
LPI3H_20231215.img1 *      2048  133119  131072   64M  c W95 FAT32 (LBA)
LPI3H_20231215.img2      133120 5242879 5109760  2.4G 83 Linux
```

完成分区后，使用 losetup 命令设置循环设备：
```shell
sudo losetup -f LPI3H_${DATE}.img
# fdisk 查看的分区信息用于挂载
# sudo losetup -f -o $[Start*512] --sizelimit $[Sectors*512] LPI3H_${DATE}.img
sudo losetup -f -o $[2048*512] --sizelimit $[131072*512] LPI3H_${DATE}.img
sudo losetup -f -o $[133120*512] --sizelimit $[6158336*512] LPI3H_${DATE}.img
```


`sudo losetup -l | grep LPI3H` 查看循环设备信息：
```shell
/dev/loop23   67108864  1048576         0  0 LPI3H_20231215.img               0     512
/dev/loop24 2616197120 68157440         0  0 LPI3H_20231215.img               0     512
/dev/loop3           0        0         0  0 LPI3H_20231215.img               0     512
```

根据上面查到的循环设备信息，进行后面的操作。上面的信息中可以看到 /dev/loop3 是 img 文件，/dev/loop23 是 boot 分区，/dev/loop24 是 rootfs 分区。

对分区进行格式化
```shell
sudo mkfs.fat /dev/loop23
sudo mkfs.ext4 /dev/loop24
```

格式化完成后需要的文件 ：
```shell
# 写入 uboot
sudo dd if=build/u-boot-sunxi-with-spl.bin of=/dev/loop3 bs=1k seek=8 conv=fsync
# 写入 kernel：
mkdir -p /tmp/kernel
sudo mount /dev/loop23 /tmp/kernel
sudo cp -r overlay/boot/* /tmp/kernel

# 写入 rootfs：
mkdir -p /tmp/rootfs
sudo mount /dev/loop24 /tmp/rootfs
sudo tar -vxf build/rootfs.tar -C /tmp/rootfs/

# 取消挂载
sync
sudo umount /tmp/rootfs
sudo umount /tmp/kernel
sudo losetup -d /dev/loop23 # 删除 kernel 分区对应的的循环设备
sudo losetup -d /dev/loop24 # 删除 rootfs 分区对应的循环设备
sudo losetup -d /dev/loop3 # 删除 img 文件对应的循环设备
```

接下来，可以参考[烧录镜像](https://wiki.sipeed.com/hardware/zh/longan/h618/lpi3h/4_burn_image.html)把得到的 img 镜像文件烧录到 TF 卡中。