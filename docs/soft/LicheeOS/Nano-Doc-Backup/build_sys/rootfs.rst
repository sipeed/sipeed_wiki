根文件系统编译
==========================

.. contents:: 本文目录

使用buildroot构建根文件系统
---------------------------------

buildroot可用于构建小型的linux根文件系统。

大小最小可低至2M，与内核一起可以放入最小8M的spi flash中。

buildroot中可以方便地加入第三方软件包（其实已经内置了很多），省去了手工交叉编译的烦恼。

下载安装
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

首先安装一些依赖，比如linux头文件：

    ``apt-get install linux-headers-$(uname -r)``

然后下载安装：

.. code-block:: bash

    wget https://buildroot.org/downloads/buildroot-2017.08.tar.gz
    tar xvf buildroot-2017.08.tar.gz
    cd buildroot-2017.08/
    make menuconfig

配置
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

此处为免去另外配置工具链的步骤，使用了 buildroot 自动下载工具链执行的选项；

同内核编译一样，请下载 buildroot 的 `.config <https://fdvad021asfd8q.oss-cn-hangzhou.aliyuncs.com/migrate/buildroot.config>`_ 文件，重命名为 .config 后放到 buildroot目录下；

.. tip:: 若编译时，buildroot下载软件包速度太慢，请下载 `dl.zip <https://pan.baidu.com/s/1_tBdX9K7fOkH9JdXZ_MdiQ>`_ ，将其中的软件包解压至 :menuselection:`buildroot --> dl` 下；

使用：

    ``make menuconfig``

进行配置，添加或删除指定的软件包；

一些配置的简单说明
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:: 

    Target options  --->

        Target Architecture Variant (arm926t)  --->   // arm926ejs架构
    [ ] Enable VFP extension support                  // Nano 没有 VFP单元，勾选会导致某些应用无法运行
        Target ABI (EABI)  --->
        Floating point strategy (Soft float)  --->    // 软浮点

    System configuration  --->

        (Lichee Pi) System hostname                   // hostname
        (licheepi) Root password                      // 默认账户为root 密码为licheepi
        [*] remount root filesystem read-write during boot  // 启动时重新挂在文件系统使其可读写 

编译
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``make``

    >>> 有时候构建会出现莫名其妙的错误，make clean下会ok？

编译的过程如果带上下载软件包的时间比较漫长，很适合喝杯茶睡个午觉；(buildroot不能进行多线程编译)

编译完成的镜像包，是在 :menuselection:`buildroot-2017.08 --> output -->images --> rootfs.tar` 中找到；

安装到第二分区
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

将镜像包复制到第二分区后，解压即可

.. code-block:: bash

    # 请修改设备号
    
    sudo umount /dev/sdX2
    sudo mount /dev/sdX2 /mnt
    sudo cp ./rootfs.tar /mnt/
    sudo tar -xf /mnt/rootfs.tar
    sudo rm /mnt/rootfs.tar
    sync
    sudo umount /dev/sdX2

另：检查 rootfs文件下的 /etc/inittab 是否已有以下声明：

    ``ttyS0::respawn:/sbin/getty -L ttyS0 115200 vt100 # GENERIC_SERIAL    // 串口登录使能`` 

.. admonition:: 交流与答疑
    
    对于本节内容，如有疑问，欢迎到 `根文件系统编译交流帖 <http://bbs.lichee.pro/d/27-->`_ 提问或分享经验。