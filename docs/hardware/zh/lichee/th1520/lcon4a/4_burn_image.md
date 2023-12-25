---
title: 烧录镜像
keywords: Linux, Lichee, TH1520, Console, RISCV, image
update:
  - date: 2023-12-08
    version: v1.0
    author: ztd
    content:
      - Release docs
  - date: 2023-12-21
    version: v1.1
    author: LordCasser
    content:
      - Update doc for flashing u-boot+spl
---

## 使用fastboot

1. 拆掉SSD后盖

2. 找到BOOT按键和RST按键

![boot_and_rst_key](./assets/burn_image/boot_and_rst_key.png)

3. 按着BOOT按键，然后按键盘上的电源按键开机，然后连接typec口到另外一台机器。

![typec_connect](./assets/burn_image/typec_connect.png)

4. 在另外一台机器上下载用于烧录的镜像: [点我下载](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lcon4a/3_images.html)

5. 在另外一台机器上执行 `fastboot flash ram u-boot-with-spl-console.bin`

6. 在另外一台机器上执行 `fastboot reboot`

7. 在另外一台机器上执行 `fastboot flash uboot u-boot-with-spl-console.bin`

8. 在另外一台机器上执行 `fastboot flash boot boot.ext4`

9. 在另外一台机器上执行 `fastboot flash root root.ext4`

10. 按下 BOOT 旁边的 RST 按键重启笔记本。

## 直接使用dd命令烧录u-boot+spl（用于更新）

1. 在当前荔枝派中下载好镜像：[点我下载](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lcon4a/3_images.html)，也可以使用sftp等方式传入

2. 切换到root用户 `sudo su`，并使用bash `bash`

3. 使分区可写 `echo 0 > /sys/block/mmcblk0boot0/force_ro`

4. 烧录镜像 `dd if=u-boot-with-spl-console.bin of=/dev/mmcblk0boot0`

5. 重新开启保护锁 `echo 1 > /sys/block/mmcblk0boot0/force_ro`

6. 重新启动
