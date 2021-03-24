Zero Imager的使用
=================================

.. contents:: 本文目录

Zero imager是zero固件打包，烧录 工具集，使用zero imager可以方便地进行各种配置（主线，bsp；tf，spi）的镜像打包，烧录，修改等。

zero imager 目录
---------------------------------

:: 

    zepan@ubuntu:~/develop/zero_imager$ ls
    build  dtb  fex  img kernel  modules  overlay  README  rootfs  uboot

- build： 内有各种脚本，打包烧录等操作均需要进入该目录操作
- uboot：sdk生成的uboot镜像
- dtb：主线内核使用的dtb，会从sdk中拷贝到这里
- fex：bsp内核使用的fex，会从sdk里拷贝到这里
- img：打包完成的镜像
- kernel：sdk生成的zImage，按内核版本分类摆放
- modules：sdk生成的内核模块
- rootfs：各种预制的根文件系统，如rootfs-brmin.tar.gz
- overlay：在预制根文件系统上添加的内容

zero imager 板级配置
---------------------------------

在打包系统前，需要填写板级配置并生效。

全局环境变量
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

首先进入 build目录，编辑env.sh文件，填写正确的路径信息，这里需要编辑的是：

.. code-block:: bash

    # need edit as your env
    export _TOP_DIR=/home/zepan/develop/zero_imager
    export _KERNEL_MAINDIR="goofy_elion:/root/linux/"
    export _KERNEL_BSPDIR="goofy_elion:/root/lichee/linux-3.4/"
    export _UBOOT_DEVDIR="goofy_elion:/root/u-boot"
    export _BR_DEVDIR="goofy_elion:/root/buildroot-2017.08"
    export _CP_CMD="docker cp"
    ￥_LINUX_MAINDIR是你的主线linux sdk目录
    ￥_LINUX_BSPDIR是你的bsp inux sdk目录
    ￥_UBOOT_DEVDIR是你的uboot sdk目录
    ￥_CP_CMD是你的cp命令，如果sdk在本机上，就直接是cp，如果是在远程请自行填写cp命令

板级环境变量
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

然后进入configs目录，编辑或者新建你的板级配置文件，这里以 *env-dock-tfmain.sh* 为例介绍下。

板级环境变量配置文件名，命名为 " *env-板子名-启动介质名 内核种类.sh* "

其中的内容，其余部分可以拷贝，仅修改下面部分：

.. code-block:: bash

    #change here to your config
    export _CASE_NAME=dock
    export _BOOT_DEV=tf
    export _KERNEL_TYPE=main
    export _KERNEL_VER=4.14.14
    export _DT_NAME=sun8i-v3s-licheepi-zero-dock
    #export _DT_NAME=sun8i-v3s-licheepi-zero-with-800x480-lcd
    export _ROOTFS_TYPE=brmin
    export _IMG_SIZE=128
    export _UBOOT_SIZE=1
    export _CFG_SIZEKB=0
    export _P1_SIZE=4

这里主要就是填写你的板子使用的镜像的配置信息：

    启动介质是tf或者spi，
    内核种类是main或者bsp，
    内核版本按实际填写，
    DT即设备树配置名，
    根文件系统类型即rootfs目录下的名字后缀。
    设定的镜像大小，以MB为单位，下同。
    UBOOT分区大小。
    SPI 启动时使用的FEX/DTB分区大小（单位KB）。
    第一分区大小（tf启动时放置内核和dtb等，spi启动时放置内核）。

注意这里会自动生成板子配置后缀名：

.. code-block:: bash

    export _SUFFIX=$_CASE_NAME-$_BOOT_DEV$_KERNEL_TYPE

如 dock-tfmain

生效板级配置
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在build目录下执行 ``source configs/env-dock-tfmain.sh`` 即可生效对应配置。

执行后会在build目录下生成 *boot.scr* 启动脚本。

每次打开新终端 请先执行一遍该命令来导入配置。

镜像更新，打包命令
---------------------------------

:: 

    pull_uboot.sh：从sdk里更新uboot
    pull_kernel.sh: 从sdk里更新zImage和dts和modules
    pull_br.sh: 从sdk更新buildroot生成的根文件系统
    pack_img.sh: 打包img到dd文件，生成文件在img目录下

局部更新镜像内容，可以在overlay下对应目录拷贝需要的文件，打包镜像时会将文件写入根文件系统的对应目录。

TF镜像烧录命令
---------------------------------

:: 

    write_dd.sh /dev/sdX: 一键烧录dd镜像，小白专用
    //以下为调试时逐个分区调试使用的烧录脚本
    write_all.sh /dev/sdX: 一键烧录
    write_partion.sh /dev/sdX: 对tf卡分区
    write_mkfs.sh /dev/sdX: tf卡格式化
    write_boot.sh /dev/sdX: 烧录uboot
    write_p1.sh /dev/sdX: 烧录第一分区
    write_p2.sh /dev/sdX: 烧录第二分区
    write_overlay.sh /dev/sdX: 烧录overlay
    write_swap.sh /dev/sdX: 启用swap
