---
title: Mainline Linux
keywords: Linux, Longan, H618, SBC, ARM, Kernel, SDK, Develop
update:
  - date: 2023-12-08
    version: v1.0
    author: ztd
    content:
      - Release docs
---

This document takes Ubuntu 22.04 as an example to demonstrate how to build a LonganPi 3H development environment and develop mainline Linux.
Before the official merger into the mainline, it is necessary to pull the Github repository to obtain patch development, which is expected to be merged into the mainline Linux in 2024Q1.

## Environment Configuration
First, use git to pull the repository to the local, and install the toolchain:
```shell
sudo apt install gcc-aarch64-linux-gnu mmdebstrap git 
git clone https://github.com/sipeed/LonganPi-3H-SDK.git
```

## Build
Then go to the directory where the repository is located and run the script to get the uboot, kernel, dtb and rootfs built.
```shell
cd LonganPi-3H-SDK
./mkatf.sh
./mklinux.sh
./mkuboot.sh
./mkrootfs.sh
```

The generated Image files, device tree files will be copied to the overlay/boot/ folder under the repository directory. The generated kernel modules will be copied to the overlay/usr/ folder under the repository directory.

Next, we will introduce the main files and their functions in the SDK repository:

The `linux` folder stores the kernel patch files, which will be automatically applied to the kernel source code when running mklinux.sh.

The `uboot` folder stores the U-Boot patch files, which will be automatically applied to the U-Boot source code when running mkuboot.sh.

The `overlay` folder contains some necessary files that will be automatically overlayed to the constructed rootfs when running mkrootfs.sh. mkrootfs.sh is used to build the required root file system for burning, you can choose whether to skip the construction of the Debian rootfs according to actual needs, see the script comments for details.

After the construction is complete, the next step is to introduce how to make a TF card for booting and how to package the burnable TF card boot image.

## Make a boot TF card

To prepare a TF card, first format it.

Then partition the TF card (please modify the commands below to the proper drive letter for your own TF card, carefully verify and operate prudently), the following steps use fdisk to add two partitions to the TF card, the boot partition size is 64M, and the remaining space is allocated to the root file system (U-Boot is burned to the raw partition, which is usually located in the first 1M of the TF card space):
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
Then pressing Enter twice, the remaining space will be allocated to the root file system. After partitioning is complete, do not exit fdisk yet, and still need to set the first partition as the boot partition:
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
After setting, input p to check if the partition information just set is correct:
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

Once verified the partition information is correct, input w and press Enter to write the partition table configuration:
```shell
Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
```

Next, format the **partitions**:
```shell
sudo mkfs.vfat -F 32 -n "boot" /dev/sdc1
sudo mke2fs -t ext4 -F -L "rootfs" /dev/sdc2
```

Then flash uboot：
```shell
sudo dd if=build/u-boot-sunxi-with-spl.bin of=/dev/sdc bs=1k seek=8 conv=fsync
```

Flash kernel：
```shell
mkdir -p /tmp/kernel
sudo mount /dev/sdc1 /tmp/kernel
sudo cp -r overlay/boot/* /tmp/kernel
sync
sudo umount /tmp/kernel
```

Flash rootfs：
```shell
mkdir -p /tmp/rootfs
sudo mount /dev/sdc2 /tmp/rootfs
sudo tar -vxf build/rootfs.tar -C /tmp/rootfs/
sync
sudo umount /tmp/rootfs
```

Now we get a boot TF card.

## Make a boot TF card image

First, create an empty img file:
```shell
export DATE=$(date +"%Y%m%d")
dd if=/dev/zero of=LPI3H_${DATE}.img bs=1M count=3072
```

Then partition the img file. Similarly, use the fdisk command to divide it into a boot partition and a rootfs partition:
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

Use fdisk -l LPI3H_${DATE}.img to view the partition information:
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

After partitioning, use the losetup command to set up the loop device:
```shell
sudo losetup -f LPI3H_${DATE}.img
# fdisk 查看的分区信息用于挂载
# sudo losetup -f -o $[Start*512] --sizelimit $[Sectors*512] LPI3H_${DATE}.img
sudo losetup -f -o $[2048*512] --sizelimit $[131072*512] LPI3H_${DATE}.img
sudo losetup -f -o $[133120*512] --sizelimit $[6158336*512] LPI3H_${DATE}.img
```


`sudo losetup -l | grep LPI3H`  to check the loop device information:
```shell
/dev/loop23   67108864  1048576         0  0 LPI3H_20231215.img               0     512
/dev/loop24 2616197120 68157440         0  0 LPI3H_20231215.img               0     512
/dev/loop3           0        0         0  0 LPI3H_20231215.img               0     512
```

According to the loop device information found above, continue with the following operations.

Next, format the **partitions**:
```shell
sudo mkfs.fat /dev/loop23
sudo mkfs.ext4 /dev/loop24
```

And flash the uboot, kernel, rootfs into the img files:
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


According to the instructions on the [burn image](https://wiki.sipeed.com/hardware/en/longan/h618/lpi3h/4_burn_image.html) page, here are the steps to burn the obtained img image file to the TF card: