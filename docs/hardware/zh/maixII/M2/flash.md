---
title: MaixII-Dock 烧录系统
keywords: MaixII, MaixPy3, Python, Python3, M2dock
desc: maixpy  MaixII M2dock 烧录系统
update:
  - date: 2021.03.20
    author: dls
    content: 新建文档，开始编写内容
  - date: 2021.12.8
    author: Rui & 点灯鼠
    content: 整理并更新烧录方式
  - date: 2022.3.8
    author: Rui
    content: 修改烧录的注意事项
  - date: 2023.7.31
    author: Neucrack
    content: 精简描述， 解决修复 livesuit 无法使用的问题
---

> 注意事项！
> - 烧录会清空 TF 卡中所有数据，有重要数据请提前备份
> - 部分 AMD 平台的电脑存在无法烧录的情况
> - 少部分 TF 卡可能无法烧录镜像，建议用户购买官方的镜像 TF 卡

## 烧录系统简介

因为 MAIX-II 的芯片是 V831，需要运行一个操作系统（Linux），软件都是在这个操作系统的基础上运行的。
所以我们需要学会如何烧录系统（/升级系统），方便更新系统和出现问题时重刷系统。


## 获取系统镜像文件

从[下载站](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/release)获取最新的 V831 系统镜像,得到一个压缩包，解压之后就得到一个 .img 文件，这个就是系统镜像文件

> 如果下载站下载的很慢，建议使用百度网盘进行下载，下载站的下载带宽有限。链接：[点我](https://pan.baidu.com/s/1vCExI3_48Q90JrxO70JdiQ)

### 系统镜像文件命名说明

比如 `v831-m2dock-maixhub-0.5.1-20220701.zip`和 ` v831-m2dock-maixpy3-0.5.1-20220701.zip`：

| 名称          | 含义                                                                                                              |
| ------------- | ----------------------------------------------------------------------------------------------------------------- |
| maixhub-0.5.1(推荐) | 此镜像是内置了 [MaixPy3](https://wiki.sipeed.com/maixpy3)`0.5.1`的版本，且内置 [maixhub app](https://maixhub.com/app/1)        |
| maixpy3-0.5.1 | 此镜像是内置了 [MaixPy3](https://wiki.sipeed.com/maixpy3)`0.5.1`的版本，但其中 **无** 内置 [maixhub app](https://maixhub.com/app/1) |

> 注意点：
> * 上述镜像均为开源版，如果需要从 Flash 启动而不是从 TF 卡启动的镜像，请联系 support@sipeed.com 或者商业支持。
> * 内置 maixhub app 的镜像就是没有内置 maixhub app 版本在 `/root/app` 放置了 [maixhub app](https://maixhub.com/app/1)

## Windows 上使用 PhoenixCard 烧录镜像

PhoenixCard 是用来烧录全志科技芯片的工具，前者通过 USB 烧录到板载的 flash，后者用于烧录镜像到 TF 卡中。

PhoenixSuit 和 PhoenixCard 是常用来烧录全志科技芯片的两种工具，前者通过 USB 烧录到板载的 flash，后者用于烧录镜像到 TF 卡中。

零售开源版的 M2 模组上没有焊接 Flash，因此需要使用 TF 卡来作为启动介质，需要用 PhoenixCard 烧录镜像到 TF 卡中来启动

### 准备工作

1. 烧录工具 [PhoenixCard](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/tools)

2. 系统 [镜像](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/release)

3. 内存卡格式化工具 [SD Card Formatter](https://www.sdcard.org/downloads/formatter/eula_windows/SDCardFormatterv5_WinEN.zip)

### 系统烧录

1. 将内存卡通过读卡器接到电脑的 USB 口，如果弹出格式化通知的话，点击取消即可

     ![windows_format_tf](./asserts/windows_format_tf.png)

2. 打开 SD Card Formatter 软件，对内存卡进行格式化。Refresh（刷新）后点击Format（格式化），注意不要格式化错了分区。

     ![image-20210802102810041](./../../../assets/maixII/V831/image-20210802102810041.png)

3. 打开PhoenixCard
     - 选择 `启动卡` 选项
     - 选择正确的盘符
     - 点击 `烧卡`
     - 根据状态栏的颜色可以判断烧录结果：红色的话说明烧录失败了，建议使用[SD card Formatter](https://www.sdcard.org/downloads/formatter/eula_windows/SDCardFormatterv5_WinEN.zip)格式化后再重新烧录一次；绿色表示则一切正常。

   ![image-20210802104155132](./../../../assets/maixII/V831/image-20210802104155132.png)

## Linux(Ubuntu) 使用 Livesuit 烧录

### 安装烧录工具 Livesuit 

> **每次更新系统 linux kernel 之后需要重新安装软件**

1. 安装依赖 dkms

     ```shell
     sudo apt install dkms
     ```

1. 安装 libpng1.2（一定要使用这个版本）

     ```shell
     wget http://archive.ubuntu.com/ubuntu/pool/main/libp/libpng/libpng_1.2.54.orig.tar.xz
     tar xvf  libpng_1.2.54.orig.tar.xz
     ```

     ```shell
     cd libpng-1.2.54
     ./autogen.sh
     ./configure
     make -j8
     sudo make install
     ```

     更新链接库:

     ```shell
     sudo ldconfig
     ```

1. 安装 **livesuit**

     ```shell
     git clone https://github.com/linux-sunxi/sunxi-livesuite.git
     cd sunxi-livesuite
     cd awusb
     sudo dkms install .
     ```
     > **问题1**： 报错`make[2]: *** 没有规则可制作目标“arch/x86/entry/syscalls/syscall_32.tbl”，由“arch/x86/include/generated/uapi/asm/unistd_32.h” 需求。 停止。`的话，
     > 参考[issue](https://github.com/linux-sunxi/sunxi-livesuite/issues/17)修改Makefile的 `SUBDIR`字符为`M`就可以编译通过的到`ko`文件。
     >
     > **问题2**： 遇到`module: x86/modules: Skipping invalid relocation target, existing value is nonzero for type 1, loc 0000000094ea3f48, val ffffffffc2034d37`
     > ```
     > sudo apt update && sudo apt upgrade
     > sudo apt remove --purge linux-headers-*  # 可以具体一个一个移除
     > sudo apt autoremove && sudo apt autoclean
     > sudo apt install linux-headers-`uname -r`
     > ```
     保证`sudo dkms install .`成功执行

     ```
          cd ..
          chmod +x LiveSuit.sh
          sudo ./LiveSuit.sh
     ```
     **注意一定要加 sudo**

### 使用 Livesuit 烧录

`sudo livesuit` 打开烧录工具，并点击“固件”选择镜像文件

![](./asserts/flash_15.png)

不插入 SD 卡，将 V831 USB OTG 接口连接到 PC, 提示是否格式化分区，这时候插入 SD 卡，之后点击 `YES`

![](./asserts/flash_17.png)

等待烧录完成，提示“固件升级成功”，即可断开 USB ，至此固件烧录完毕

![](./asserts/flash_19.png)

![](./asserts/flash_21.png)


## 其它

### 烧录系统到 flash 中

[烧录方式](./no_sd_flash.md)

### 无读卡器烧录方式

[烧录方式](./PhoenixSuit.md)

### 使用 dd 烧录

官方没有做 MaixII-Dock 的 dd 镜像相关支持，可以自己烧录到 TF 卡后，用读卡器在电脑上自行制作。
> 这里有个不算完美方法的[参考](https://www.cnblogs.com/USTHzhanglu/p/15431249.html)。
