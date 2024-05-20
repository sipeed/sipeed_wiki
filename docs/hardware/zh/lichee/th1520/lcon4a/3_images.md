---
title: 镜像集合
keywords: Linux, Lichee, TH1520, Console, RISCV, image
update:
  - date: 2023-12-08
    version: v1.0
    author: ztd
    content:
      - Release docs
---

## Sipeed官方镜像

https://github.com/0x754C/sipeed-th1520-laptop-extra/releases

linux-image-*.deb 是sipeed提供的内核安装包，如果只想升级内核可以安装这个，安装前记得更新到对应版本的uboot，以及备份文件。

sipeed-th1520-laptop-extra-*.deb 是sipeed提供的附加文件安装包，包括配置文件，测试工具，和EC固件。

u-boot-with-spl-*.bin 是uboot文件，请选择你电路板对应型号的uboot进行烧写，烧写前记得备份文件，如果烧写错误的uboot可能会导致无法开机。

boot|root-*.ext.xz 是分区镜像，如果想整个重新烧录，使用这个。

## Sipeed官方镜像(旧版)

Sipeed 官方镜像基于 Debian 系统修改适配。 

默认镜像的帐号密码配置如下：
账户： `sipeed`，密码：`licheepi`；
账户：`debian`，密码： `debian`；
root 账户默认没有设置密码。

镜像下载：
[百度网盘](https://pan.baidu.com/s/11xiphA-9OAGTaZBY8kTNEg) 提取码: h3gv
[mega网盘](https://mega.nz/folder/p0oiwCqI#EFGgwRnoB9mX14pKI2pu4Q)

烧录方式请参考[烧录镜像](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lcon4a/4_burn_image.html)
