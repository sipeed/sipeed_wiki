emdebian根文件系统
=========================================

.. contents:: 本文目录

如果想要更接近桌面系统的根文件系统，emdebian是不二之选。emdebian也是深度可定制，大小从不到100M到上G均可配置。但这个大小基本上无法使用spi flash了，只能使用tf卡或者emmc。优点是有包管理系统，可以直接apt-get install来安装新软件包。

环境搭建
-----------------------------------------

安装依赖包
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``sudo apt-get install multistrap qemu qemu-user-static binfmt-support dpkg-cross``

建立工作目录：
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    mkdir emdebian
    cd emdebian
    mkdir mindb
    cd mindb

编辑multistrap_mindb.conf配置文件
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

示例如下：

具体语法请参考：https://wiki.debian.org/Multistrap

这里使用了较快的清华大学的镜像站，身在国外的朋友可以视情况更改。

.. code-block:: conf

    [General]
    directory=target-rootfs
    cleanup=true
    noauth=true
    unpack=true
    debootstrap=Debian Net Utils
    aptsources=Debian 

    [Debian]
    packages=apt kmod lsof
    source=http://ftp2.cn.debian.org/debian/
    keyring=debian-archive-keyring
    suite=stretch
    components=main contrib non-free

    [Net]
    #Basic packages to enable the networking
    packages=netbase net-tools ethtool udev iproute iputils-ping ifupdown isc-dhcp-client ssh
    source=http://ftp2.cn.debian.org/debian/

    [Utils]
    #General purpose utilities
    packages=locales adduser vim less wget dialog usbutils
    source=http://ftp2.cn.debian.org/debian/

创建根文件系统
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``sudo multistrap -a armhf -f multistrap_mindb.conf``

执行完成后，target-rootfs即是所需的根文件系统。

配置软件包
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

使用QEMU来配置软件包，将target-rootfs作为root挂载来操作。

.. code-block:: bash

    sudo cp /usr/bin/qemu-arm-static target-rootfs/usr/bin
    sudo mount -o bind /dev/ target-rootfs/dev/
    sudo LC_ALL=C LANGUAGE=C LANG=C chroot target-rootfs dpkg --configure -a
    #这里就可以模拟板子情况执行相关命令，比如安装额外的软件包
    sudo umount target-rootfs/dev/	#最后记得卸载
    
其中出现选择系统shell的提示框，选否，即不使用dash。


做最后的一些配置
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    #!/bin/sh
    #Directory contains the target rootfs
    TARGET_ROOTFS_DIR="target-rootfs"
    #Board hostname
    filename=$TARGET_ROOTFS_DIR/etc/hostname
    echo acqua > $filename
    #Default name servers
    filename=$TARGET_ROOTFS_DIR/etc/resolv.conf
    echo nameserver 8.8.8.8 > $filename
    echo nameserver 8.8.4.4 >> $filename
    #Default network interfaces
    filename=$TARGET_ROOTFS_DIR/etc/network/interfaces
    echo auto eth0 >> $filename
    echo allow-hotplug eth0 >> $filename
    echo iface eth0 inet dhcp >> $filename
    #eth0 MAC address
    echo hwaddress ether 00:04:25:12:34:56 >> $filename
    #Set the the debug port
    filename=$TARGET_ROOTFS_DIR/etc/inittab
    echo T0:2345:respawn:/sbin/getty -L ttyS0 115200 vt100 >> $filename
    #Set rules to change wlan dongles
    filename=$TARGET_ROOTFS_DIR/etc/udev/rules.d/70-persistent-net.rules
    echo SUBSYSTEM=='"net", ACTION=="add", DRIVERS=="?", ATTR{address}=="", ATTR{dev_id}=="0x0", ATTR{type}=="1", KERNEL=="wlan*", NAME="wlan0"' > $filename
    #microSD partitions mounting
    filename=$TARGET_ROOTFS_DIR/etc/fstab
    echo /dev/mmcblk0p1 /boot vfat noatime 0 1 > $filename
    echo /dev/mmcblk0p2 / ext4 noatime 0 1 >> $filename
    echo proc /proc proc defaults 0 0 >> $filename
    #Add the standard Debian non-free repositories useful to load
    #closed source firmware (i.e. WiFi dongle firmware)
    filename=$TARGET_ROOTFS_DIR/etc/apt/sources.list
    echo deb http://http.debian.net/debian/ stretch main contrib non-free > $filename

设置密码和其它操作
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    sudo chroot target-rootfs passwd
    sudo LC_ALL=C LANGUAGE=C LANG=C chroot target-rootfs apt-get install packagename

修改 target-rootfs/etc/ssh/sshd_config来使能root登录

*PermitRootLogin yes*
