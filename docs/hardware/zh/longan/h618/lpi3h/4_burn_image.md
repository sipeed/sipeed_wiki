---
title: 烧录镜像
keywords: Linux, Longan, H618, SBC, ARM, image
update:
  - date: 2023-12-08
    version: v1.0
    author: ztd
    content:
      - Release docs
---

## 准备工作

### 获取镜像

参见上一章[镜像集合](https://wiki.sipeed.com/hardware/zh/longan/h618/lpi3h/3_images.html)，选取需要的镜像下载。

### 获取烧录工具

烧录镜像至 SD 卡的工具常见的有 balenaEtcher，rufus 等，这里以 balenaEtcher 为例，首先去[balenaEtcher官网](https://etcher.balena.io/#download-etcher)下载并安装该软件。
Linux 下也可以使用 dd 命令直接写入。

## 烧录镜像

### 烧录镜像至 SD 卡

准备好要烧录的镜像后，打开 balenaEtcher，先选择要烧录的镜像文件：

![select_image](./assets/burn_image/select_image.png)

然后选择要烧录的目标设备：

![select_device](./assets/burn_image/select_device.png)

最后点击烧录，等待烧录完成后，就得到了包含启动镜像的 SD 卡：

![flash_image](./assets/burn_image/flash_image.png)

Windows 系统和 Linux 的步骤类似。

### 烧录镜像至 EMMC

**注意需要使用20240106及以上版本的镜像**

先将要烧录的镜像文件拷贝至预先制作好的启动TF卡中，然后进入到系统使用 dd 命令将镜像文件写入 EMMC：
```shell
# 假设镜像文件复制到 /opt/ 目录下
dd if=/opt/your_image_file of=/dev/mmcblk1
sync
```
等到烧录完成后，拔掉 SD 卡，即可从EMMC进入系统。
