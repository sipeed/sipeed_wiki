---
title: 烧录镜像
keywords: Linux, Lichee, TH1520, Console, RISCV, image
update:
  - date: 2023-12-08
    version: v1.0
    author: ztd
    content:
      - Release docs
---


## 最小镜像

针对使用 8+8 内测版核心板的用户，全量烧录镜像会因为容量不够从而无法烧录，可以先在[这里](https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ)下载烧录开发板的 BASIC 镜像，然后进行部分替换，即可得到适用于 console 的最小镜像。

需要替换的部分可以在[github](https://github.com/sipeed/LicheePi4A-Build/releases)中下载。
下载完成后，使用 scp 上传到开发板，然后在开发板上执行如下命令即可完成替换：
```shell
sudo apt update
sudo apt install squashfs-tools
unsquashfs overlay_20231215.sqfs
sudo cp -r squashfs-root/* /
```

替换完成后，再烧录一下 console 对应的 u-boot（注意是只烧录u-boot），烧录完成后重启即可。

## 全量镜像

1. 拆掉SSD后盖

2. 找到BOOT按键和RST按键

![boot_and_rst_key](./assets/burn_image/boot_and_rst_key.png)

3. 按着BOOT按键，然后按键盘上的电源按键开机，然后将 console 连接 typec 口到烧录镜像的 PC。

![typec_connect](./assets/burn_image/typec_connect.png)

4. 在烧录镜像的 PC 上下载用于烧录的镜像: [点我下载](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lcon4a/3_images.html)

5. 在烧录镜像的 PC 上执行 `fastboot flash ram u-boot-with-spl-console.bin`

6. 在烧录镜像的 PC 上执行 `fastboot reboot`

7. 在烧录镜像的 PC 上执行 `fastboot flash uboot u-boot-with-spl-console.bin`

8. 在烧录镜像的 PC 上执行 `fastboot flash boot boot.ext4`

9. 在烧录镜像的 PC 上执行 `fastboot flash root root.ext4`

10. 按下 BOOT 旁边的 RST 按键重启 Console 笔记本。