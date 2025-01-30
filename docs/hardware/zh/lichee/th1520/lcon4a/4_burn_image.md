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

## 镜像下载:

https://github.com/0x754C/sipeed-th1520-laptop-extra/releases

## 全量镜像

### 通过 typeC 口烧录

1. 拆掉SSD后盖

2. 找到BOOT按键和RST按键

![boot_and_rst_key](./assets/burn_image/boot_and_rst_key.png)

3. 按着BOOT按键，然后按键盘上的电源按键开机，然后将 console 连接 typec 口到烧录镜像的 PC。

![typec_connect](./assets/burn_image/typec_connect.png)

4. 在烧录镜像的 PC 上下载用于烧录的镜像: [点我下载](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lcon4a/3_images.html)


5. 执行烧录指令:

```
fastboot flash ram u-boot-with-spl-console.bin
fastboot reboot
fastboot flash uboot u-boot-with-spl-console.bin
fastboot flash boot boot.ext4
fastboot flash root root.ext4
```

10. 按下 BOOT 旁边的 RST 按键重启 Console 笔记本。

### 通过 u-boot 进行网络烧录

1. console 连接网线（注意和用于烧录镜像的 PC 处于同一局域网中）

2. 用串口工具连接 console 上的串口，上电，进入到 uboot 命令行中

3. console 执行 dhcp 命令分配一个 ip 地址

4. console 执行 fastboot udp 开启监听

5. 烧录镜像的 PC 机上运行如下命令
```shell
./fastboot -s udp:board_ip flash uboot uboot-xxxx.bin
./fastboot -s udp:board_ip flash boot boot-xxxx.ext4
./fastboot -s udp:board_ip flash root root-xxxx.ext4
```

效果如下：
![fastboot_udp](./assets/burn_image/fastboot_udp.png)
