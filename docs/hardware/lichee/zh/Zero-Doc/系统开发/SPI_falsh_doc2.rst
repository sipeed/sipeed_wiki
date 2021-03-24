overlayfs的使用
=====================================================

.. contents:: 本文目录

前面简单做的jffs2文件系统，没有经过压缩，体积比较大，在spi flash中放不了多少东西。

这里介绍使用overlayfs有效利用flash空间。（著名的openwrt上用的就是这一套）

squashfs 使用
-----------------------------------------------------

squashfs是只读压缩文件系统，我们把相对固定的根文件系统部分使用squash压缩存储。

把目录文件放在rootfs下，然后执行

   ``mksquashfs rootfs rootfs-sq.img``

即可获得squashfs的根文件系统。

启动squashfs需要改动uboot的环境变量：

.. code-block:: c
   :caption: include/configs/sun8i.h

    #define CONFIG_BOOTARGS      "console=ttyS0,115200 earlyprintk panic=5 rootwait " \
                                "mtdparts=spi32766.0:1M(uboot)ro,64k(dtb)ro,4M(kernel)ro,-(rootfs) root=31:03 rw rootfstype=squashfs

以及在内核编译时选上相应选项。

在启动系统后可以在/proc/filesystems 查看系统支持的文件系统：

.. code-block:: bash

    # cat /proc/filesystems 
    nodev	sysfs
    nodev	rootfs
    nodev	ramfs
    nodev	bdev
    nodev	proc
    nodev	cgroup
    nodev	cgroup2
    nodev	tmpfs
    nodev	devtmpfs
    nodev	configfs
    nodev	debugfs
    nodev	sockfs
    nodev	pipefs
    nodev	rpc_pipefs
    nodev	devpts
        squashfs
        vfat
    nodev	nfs
    nodev	nfs4
    nodev	jffs2
    nodev	overlay

overlayfs使用
-----------------------------------------------------

overlayfs 顾名思义，就是一种覆盖式的文件系统。

常见用法是，底层文件系统只读，上层文件系统可读写；著名的docker就是使用的overlayfs。

在嵌入式应用中，底层只读系统一般使用squashfs，上层使用jffs2.

首先我们重新分区：

.. code-block:: c

    #define CONFIG_BOOTARGS      "console=ttyS0,115200 earlyprintk panic=5 rootwait " \
                                "mtdparts=spi32766.0:1M(uboot)ro,64k(dtb)ro,4M(kernel)ro,16M(rootfs) -(data) root=31:03 rw rootfstype=squashfs

这样就是给固定只读的rootfs划分了16M空间，剩余空间约10.9M划分给可读写的数据分区。

同时在只读根文件系统下新建overlay目录。

开机启动后，执行以下命令来挂载overlayfs：

注意需要使用正规mount命令，而不是busybox的mount命令才能挂载

.. code-block:: bash

    mount -n -t jffs2 /dev/mtdblock4  /overlay
    mount -n -t overlay overlayfs:/overlay -o lowerdir=/,upperdir=/overlay,workdir=/workdir /mnt
