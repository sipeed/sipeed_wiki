# 一键烧录及脚本使用说明

```eval_rst
材料准备：    
    内存卡+读卡器+荔枝派Nano+支持完整指令集的x86设备一台（电脑）

镜像下载地址：
    https://pan.baidu.com/s/1smzuGS9
```

## 一键烧录镜像(Linux环境---TF卡启动)

镜像包中的image文件夹下的dd文件，已包含了相应的Bootloader、Kernel、文件系统等等，只需简单两步即可完成烧录；

1. 插上tf卡后，命令行执行 ``sudo fdisk -l`` 查看tf卡盘号；

2. 执行 ``sudo dd if=/path/to/your-dd-image of=/your/tf-card && sync`` 即可完成烧录

我们所提供的dd一键镜像包为兼容低存储的tf卡，仅为根文件系统留下有限的空间，若您需要存储某些大文件，请参阅后文 [脚本使用](#脚本的使用)

## 一键烧录镜像(Linux环境---16M spi-flash 启动)

在flash内容为空的情况下（fel模式下的一种情况）进行烧录时，通过micro-usb数据线将Nano与电脑连接，执行

``sudo sunxi-fel -p spiflash-write 0 Your-Flash-BIN``

若flash中已有系统，可通过：

1. 短接 1、4 两脚，重新上电，上电后松开短接，即可重新进入fel模式，进行再次下载
2. 在启动到内核前，回车进入uboot，执行 ``sf probe 0;sf erase 0 0x100000;reset``即可重新进入fel模式

## 一键烧录镜像(win环境---TF卡启动)

使用软件 **win32disk** 进行一键烧录，可到 [此处](http://www.onlinedown.net/soft/110173.html) 下载;

## 脚本的使用

镜像包内build文件夹下脚本，可通过使用配置脚本设置环境变量，帮助您进行固件烧写img构建

### 变量配置一次摸清

此处请注意两个脚本文件： configs 文件夹下的脚本文件（固件配置） 和 本目录下的 **env.sh**（公共环境配置）

首先来看 env.sh:

根据提示，前5个变量需要我们进行修改，分别是：

- _TOP_DIR          ---  镜像包所在的一级目录
- _KERNEL_MAINDIR   ---  主线Linux源码所在目录
- _UBOOT_DEVDIR     ---  Uboot源码所在目录
- _BR_DEVDIR        ---  Buildroot所在目录
- _CP_CMD           ---  复制命令(默认为docker拉取)

再来看configs文件夹下的脚本文件 ： **env-xxxxx.sh**

- 默认加载 env.sh 中的行动
- _SCREEN_PRAM      ---  选择屏幕大小版本（通过注释切换）（目前仅提供了480x272与800x480两种）
- _CASE_NAME        ---  各类文件的前缀名
- _BOOT_DEV         ---  默认启动设备
- _KERNEL_TYPE      ---  内核类型（主线或bsp）
- _KERNEL_VER       ---  内核版本号（menuconfig可见）
- _DT_NAME          ---  设备树名称
- _ROOTFS_TYPE      ---  自我定义
- _IMG_SIZE         ---  生成的镜像大小（越大，根文件系统剩余空间越多）
- _UBOOT_SIZE       ---  导入的Uboot大小
- _CFG_SIZEKB       ---  config文件大小（其值大小、是否为0与内核版本有关）
- _P1_SIZE          ---  给第一分区划分的大小（以 M 为单位）

```eval_rst
.. note::

    - 您若仅需烧写，修改好公共环境变量，固件配置可保持不变；
    - 您若需要编写自己的配置文件，请通过修改上述变量进行适配；
```

### 正确使用姿势

1. 按照上一节所述进行环境变量的配置
2. 执行以下命令

    ```bash
        cd configs
        source env-xxxxx.sh   # 生效环境变量
        cd ..                       # 返回上级目录
    ```
3. 使用 **write_all.sh /dev/sdX** (sdX修改为tf设备号)，一键对tf卡进行全套写入。
4. 若使用的是从 spi-flash 启动，则 **write_spiflash.sh** 即可将镜像写入16M flash
5. 生成镜像时使用 **pack_tf_img.sh** 生成tf镜像文件,**pack_flash_img.sh** 生成spi-flash镜像文件。

### 分区操作脚本

- write_all.sh        ---  为tf卡创建全套内容
- write_flash.sh      ---  为spi-flash写入全套内容
- write_dd.sh         ---  以dd镜像的方式写入全套内容（规定了分区信息）（生成方式见下一节）
- write_boot.sh       ---  向tf卡dd进Uboot
- write_mkfs.sh       ---  单纯的为两个分区进行硬盘格式化
- write_p1.sh         ---  单纯的向第一分区写入设备树内核等
- write_p2.sh         ---  单纯的向第二分区写入rootfs
- clear_partion.sh    ---  擦除分区表
- write_partion.sh    ---  写入分区表
- write_swap.sh       ---  增加swap

### 镜像生成 脚本

镜像生成最简单的方法是借助tf卡，手动或使用脚本向tf写入完结构，再dd出来，但手动生成较为琐碎且不灵活，所以我们在这里提供了脚本文件： **pack_tf_img.sh** 和 **pack_flash_img.sh**，能够判断镜像大小是否符合启动要求，且借助loop模拟创建设备，快速高效。

使用方法： **sh pack_tf_img.sh** 或 **sh pack_flash_img.sh** 即可

生成的镜像在 ./image 目录下；

### docker环境下拉取资源到本地

当您在docker环境下已经成功构建相应的系统各组件，以下脚本可以帮助到您：

- pull_uboot.sh    ---  从docker环境中拉取UBOOT到原生环境
- pull_kernel.sh   ---  从docker环境中拉取(主线)Kernel与构建好的驱动模块到原生环境
- pull_br.sh       ---  从docker环境中拉取rootfs与配置文件到原生环境

```eval_rst

    .. admonition:: 交流与答疑

        对于本节内容，如有疑问，欢迎到 `镜像烧录交流帖 <http://bbs.lichee.pro/d/32-->`_ 提问或分享经验。

```
