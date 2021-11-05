spi-flash 启动适配
=====================================

.. contents:: 本文目录

对于从spi-flash启动系统，需要对 uboot / dts / 内核配置都有所修改，打包与烧写请参考 `一键烧录及脚本使用说明 <./onekey.html>`_ 

以下将以16M flash为例，介绍 spi flash 的适配过程。

分区规划
-------------------------------------

下表为分区规划表：

.. table:: 

    +--------+---------------+----------+------------------------------+
    |分区序号|   分区大小    | 分区作用 |       地址空间及分区名       |
    +========+===============+==========+==============================+
    |mtd0    |1MB (0x100000) |spl+uboot |0x0000000-0x0100000 : “uboot” |
    +--------+---------------+----------+------------------------------+
    |mtd1    |64KB (0x10000) |dtb文件   |0x0100000-0x0110000 : “dtb”   |
    +--------+---------------+----------+------------------------------+
    |mtd2    |4MB (0x400000) |linux内核 |0x0110000-0x0510000 : “kernel”|
    +--------+---------------+----------+------------------------------+
    |mtd3    |剩余 (0xAF0000)|根文件系统|0x0510000-0x1000000 : “rootfs”|
    +--------+---------------+----------+------------------------------+

uboot 修改
--------------------------------------

以下是对 uboot 进行适配的流程描述；

bootcmd修改
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``make ARCH=arm menuconfig``，进入 uboot 源码一级目录，勾选 Enable a default value for bootcmd ，并填入下方 bootcmd 的参数

:: 

   sf probe 0 50000000; \
   sf read 0x80C00000 0x100000 0x4000; \
   sf read 0x80008000 0x110000 0x400000; \
   bootz 0x80008000 - 0x80C00000

按照行数解释如下：

    1. 挂载 spi-flash
    2. 读取 spi-flash 1M（0x100000）位置 16KB(0x4000)大小的 dtb 到地址 0x80C00000
    3. 读取 spi-flash 1M+64K（0x110000）位置 4MB (0x400000)大小的 zImage 到地址 0x80008000
    4. 从 0x80008000 启动内核，从 0x80C00000 读取设备树配置

bootargs修改
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

勾选 *[\*] Enable boot arguments；*

在下方一项中填入 bootargs 参数:

``console=ttyS0,115200 panic=5 rootwait root=/dev/mtdblock3 rw rootfstype=jffs2``

(root=/dev/mtdblock3 指的是mtd设备第三分区，分区指定在dts中声明)

dts 修改
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

修改内核源码目录下的 ./arch/arm/boot/dts/suniv-f1c100s-licheepi-nano.dts

.. code-block:: c

    &spi0 {
        pinctrl-names = "default";
        pinctrl-0 = <&spi0_pins_a>;
        status = "okay";
        spi-max-frequency = <50000000>;
        flash: w25q128@0 {
            #address-cells = <1>;
            #size-cells = <1>;
            compatible = "winbond,w25q128", "jedec,spi-nor";
            reg = <0>;
            spi-max-frequency = <50000000>;
            partitions {
                compatible = "fixed-partitions";
                #address-cells = <1>;
                #size-cells = <1>;

                partition@0 {
                    label = "u-boot";
                    reg = <0x000000 0x100000>;
                    read-only;
                };

                partition@100000 {
                    label = "dtb";
                    reg = <0x100000 0x10000>;
                    read-only;
                };

                partition@110000 {
                    label = "kernel";
                    reg = <0x110000 0x400000>;
                    read-only;
                };

                partition@510000 {
                    label = "rootfs";
                    reg = <0x510000 0xAF0000>;
                };
            };
        };
    };

此处在dts中为mtd设备预先划分好了分区内容，内核将会自动解析

另一种通过bootargs传递给内核进行解析分区信息的方法，请参考 `Lichee Zero spi-flash 启动 <http://zero.lichee.pro/%E7%B3%BB%E7%BB%9F%E5%BC%80%E5%8F%91/SPI_flash_build.html#id4>`_

内核配置修改
-------------------------------------

勾选 File systems ‣ Miscellaneous filesystems ‣ Journalling Flash File System v2 (JFFS2) support

![jffs2](https://box.kancloud.cn/3be64c60667c0aa3a906f095171d1fda_1396x746.png)

修改源码下的 ./drivers/mtd/spi-nor.c

修改对应spi-flash；如 w25q128 :

.. code-block:: c

    { "w25q128", INFO(0xef4018, 0, 64 * 1024, 256, SECT_4K) },
    // 修改为 （不使用sector，使用块擦除）：
    { "w25q128", INFO(0xef4018, 0, 64 * 1024, 256, 0) },

**检查 SPI 驱动是否正确**

进入 Device Drivers ‣ SPI support，将 Allwinner A10 SoCs SPI controller 取消勾选，然后勾上下面的 Allwinner A31 SPI Controller

内核需要开启 **mtdblock** 的支持，device drivers ‣ Memory Technology Device (MTD) support ‣ Caching block device access to MTD devices

关闭 **initramfs/initrd** 的支持

::

    General setup --->
    [ ] Initial RAM filesystem and RAM disk (initramfs/initrd) support

二进制bin 打包
-------------------------------------

以16M 大小flash镜像打包脚本为例：

.. code-block:: sh

    dd if=/dev/zero of=flashimg.bin bs=1M count=16 &&\
    dd if=$YOUR_UBOOT_FILE of=flashimg.bin bs=1K conv=notrunc &&\
    dd if=$YOUR_DTB_FILE of=flashimg.bin bs=1K seek=1024  conv=notrunc &&\
    dd if=$YOUR_KERNEL_FILE of=flashimg.bin bs=1K seek=1088  conv=notrunc &&\
    mkdir rootfs
    tar -xzvf $YOUR_ROOTFS_FILE -C ./rootfs &&\
    cp -r $YOUR_MOD_FILE  rootfs/lib/modules/ &&\
    # 为根文件系统制作jffs2镜像包
    # --pad参数指定 jffs2大小  
    # 由此计算得到 0x1000000(16M)-0x10000(64K)-0x100000(1M)-0x400000(4M)=0xAF0000
    mkfs.jffs2 -s 0x100 -e 0x10000 --pad=0xAF0000 -d rootfs/ -o jffs2.img &&\
    dd if=jffs2.img of=$YOUR_IMG_FILE  bs=1K seek=5184  conv=notrunc &&\

以上脚本通过对一个生成的16M空bin文件填充 uboot、dtb、kernel、rootfs 生成 16M 镜像，如需修改，请注意各个文件的大小，修改成对应地址（注意对齐）。

至此，SPI系统各部分已编译完成，通过sunxi-fel进行烧写即可；

bin 烧录
-------------------------------------

``sudo sunxi-fel -p spiflash-write $YOUR_IMG_FILE``

或请参考镜像包中的 write_flash.sh 烧录脚本；

启动后使用 账号：root 密码：licheepi 登录

.. admonition:: 交流与答疑

        对于本节内容，如有疑问，欢迎到 `SPI Flash 系统编译交流帖 <http://bbs.lichee.pro/d/31-spi-flash>`_ 提问或分享经验。

附录 1.启动日志
-------------------------------------

:: 

    U-Boot 2018.01-05676-g00188782ee-dirty (May 19 2018 - 10:15:50 +0800) Allwinner Technology

    CPU:   Allwinner F Series (SUNIV)
    Model: Lichee Pi Nano
    DRAM:  32 MiB
    Using default environment

    Setting up a 480x272 lcd console (overscan 0x0)
    In:    serial@1c25000
    Out:   serial@1c25000
    Err:   serial@1c25000
    Net:   No ethernet found.
    starting USB...
    No controllers found
    Hit any key to stop autoboot:  0 
    SF: Detected w25q128bv with page size 256 Bytes, erase size 64 KiB, total 16 MiB
    device 0 offset 0x100000, size 0x4000
    SF: 16384 bytes @ 0x100000 Read: OK
    device 0 offset 0x110000, size 0x400000
    SF: 4194304 bytes @ 0x110000 Read: OK
    ## Flattened Device Tree blob at 80c00000
    Booting using the fdt blob at 0x80c00000
    Loading Device Tree to 80e4c000, end 80e511c8 ... OK

    Starting kernel ...

    [    0.000000] Booting Linux on physical CPU 0x0
    [    0.000000] Linux version 4.15.0-next-20180202-licheepi-nano+ (biglion@biglion-MRC-WX0) (gcc version 7.2.0 (Ubuntu/Linaro 7.2.8
    [    0.000000] CPU: ARM926EJ-S [41069265] revision 5 (ARMv5TEJ), cr=0005317f
    [    0.000000] CPU: VIVT data cache, VIVT instruction cache
    [    0.000000] OF: fdt: Machine model: Lichee Pi Nano
    [    0.000000] Memory policy: Data cache writeback
    [    0.000000] random: fast init done
    [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 8128
    [    0.000000] Kernel command line: console=ttyS0,115200 panic=5 rootwait root=/dev/mtdblock3 rw rootfstype=jffs2
    [    0.000000] Dentry cache hash table entries: 4096 (order: 2, 16384 bytes)
    [    0.000000] Inode-cache hash table entries: 2048 (order: 1, 8192 bytes)
    [    0.000000] Memory: 23752K/32768K available (5120K kernel code, 203K rwdata, 1148K rodata, 1024K init, 227K bss, 9016K reserve)
    [    0.000000] Virtual kernel memory layout:
    [    0.000000]     vector  : 0xffff0000 - 0xffff1000   (   4 kB)
    [    0.000000]     fixmap  : 0xffc00000 - 0xfff00000   (3072 kB)
    [    0.000000]     vmalloc : 0xc2800000 - 0xff800000   ( 976 MB)
    [    0.000000]     lowmem  : 0xc0000000 - 0xc2000000   (  32 MB)
    [    0.000000]     pkmap   : 0xbfe00000 - 0xc0000000   (   2 MB)
    [    0.000000]     modules : 0xbf000000 - 0xbfe00000   (  14 MB)
    [    0.000000]       .text : 0x(ptrval) - 0x(ptrval)   (6112 kB)
    [    0.000000]       .init : 0x(ptrval) - 0x(ptrval)   (1024 kB)
    [    0.000000]       .data : 0x(ptrval) - 0x(ptrval)   ( 204 kB)
    [    0.000000]        .bss : 0x(ptrval) - 0x(ptrval)   ( 228 kB)
    [    0.000000] SLUB: HWalign=32, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
    [    0.000000] NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
    [    0.000046] sched_clock: 32 bits at 24MHz, resolution 41ns, wraps every 89478484971ns
    [    0.000110] clocksource: timer: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 79635851949 ns
    [    0.000639] Console: colour dummy device 80x30
    [    0.000726] Calibrating delay loop... 239.61 BogoMIPS (lpj=1198080)
    [    0.070218] pid_max: default: 32768 minimum: 301
    [    0.070625] Mount-cache hash table entries: 1024 (order: 0, 4096 bytes)
    [    0.070670] Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes)
    [    0.071979] CPU: Testing write buffer coherency: ok
    [    0.073630] Setting up static identity map for 0x80100000 - 0x80100058
    [    0.075957] devtmpfs: initialized
    [    0.082006] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
    [    0.082069] futex hash table entries: 256 (order: -1, 3072 bytes)
    [    0.082348] pinctrl core: initialized pinctrl subsystem
    [    0.084280] NET: Registered protocol family 16
    [    0.085543] DMA: preallocated 256 KiB pool for atomic coherent allocations
    [    0.087223] cpuidle: using governor menu
    [    0.105860] SCSI subsystem initialized
    [    0.106112] pps_core: LinuxPPS API ver. 1 registered
    [    0.106138] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
    [    0.106201] PTP clock support registered
    [    0.107872] clocksource: Switched to clocksource timer
    [    0.133110] NET: Registered protocol family 2
    [    0.134463] tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 4096 bytes)
    [    0.134531] TCP established hash table entries: 1024 (order: 0, 4096 bytes)
    [    0.134585] TCP bind hash table entries: 1024 (order: 0, 4096 bytes)
    [    0.134629] TCP: Hash tables configured (established 1024 bind 1024)
    [    0.134920] UDP hash table entries: 256 (order: 0, 4096 bytes)
    [    0.134977] UDP-Lite hash table entries: 256 (order: 0, 4096 bytes)
    [    0.135483] NET: Registered protocol family 1
    [    0.137139] NetWinder Floating Point Emulator V0.97 (double precision)
    [    0.139083] Initialise system trusted keyrings
    [    0.139624] workingset: timestamp_bits=30 max_order=13 bucket_order=0
    [    0.152741] jffs2: version 2.2. (NAND) �© 2001-2006 Red Hat, Inc.
    [    0.166082] Key type asymmetric registered
    [    0.166121] Asymmetric key parser 'x509' registered
    [    0.166350] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 251)
    [    0.166381] io scheduler noop registered
    [    0.166397] io scheduler deadline registered
    [    0.167159] io scheduler cfq registered (default)
    [    0.167198] io scheduler mq-deadline registered
    [    0.167216] io scheduler kyber registered
    [    0.178208] suniv-pinctrl 1c20800.pinctrl: initialized sunXi PIO driver
    [    0.337019] Serial: 8250/16550 driver, 8 ports, IRQ sharing disabled
    [    0.343487] console [ttyS0] disabled
    [    0.363782] 1c25000.serial: ttyS0 at MMIO 0x1c25000 (irq = 24, base_baud = 6250000) is a 16550A
    [    0.783896] console [ttyS0] enabled
    [    0.794166] panel-simple panel: panel supply power not found, using dummy regulator
    [    0.803443] SCSI Media Changer driver v0.25 
    [    0.811012] m25p80 spi0.0: w25q128 (16384 Kbytes)
    [    0.815738] spi0.0: parsing partitions cmdlinepart
    [    0.821589] spi0.0: got parser (null)
    [    0.825276] spi0.0: parsing partitions ofpart
    [    0.829740] spi0.0: got parser ofpart
    [    0.833455] spi0.0: parser ofpart: 4
    [    0.837028] 4 ofpart partitions found on MTD device spi0.0
    [    0.842567] Creating 4 MTD partitions on "spi0.0":
    [    0.847372] 0x000000000000-0x000000100000 : "u-boot"
    [    0.854799] 0x000000100000-0x000000110000 : "dtb"
    [    0.861985] 0x000000110000-0x000000510000 : "kernel"
    [    0.869390] 0x000000510000-0x000001000000 : "rootfs"
    [    0.877118] i2c /dev entries driver
    [    0.909420] sunxi-mmc 1c0f000.mmc: base:0xba9bd67d irq:20
    [    0.917713] NET: Registered protocol family 17
    [    0.922406] Key type dns_resolver registered
    [    0.928846] Loading compiled-in X.509 certificates
    [    0.942725] sun4i-drm display-engine: bound 1e60000.display-backend (ops 0xc0633630)
    [    0.950770] sun4i-tcon 1c0c000.lcd-controller: Missing LVDS properties, Please upgrade your DT
    [    0.959464] sun4i-tcon 1c0c000.lcd-controller: LVDS output disabled
    [    0.966603] sun4i-drm display-engine: bound 1c0c000.lcd-controller (ops 0xc0632848)
    [    0.974412] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
    [    0.981082] [drm] No driver support for vblank timestamp query.
    [    1.015308] mmc0: queuing unknown CIS tuple 0x01 (3 bytes)
    [    1.022825] mmc0: queuing unknown CIS tuple 0x1a (5 bytes)
    [    1.026082] mmc0: queuing unknown CIS tuple 0x1b (8 bytes)
    [    1.033931] Console: switching to colour frame buffer device 60x34
    [    1.035256] mmc0: queuing unknown CIS tuple 0x80 (1 bytes)
    [    1.035333] mmc0: queuing unknown CIS tuple 0x81 (1 bytes)
    [    1.035398] mmc0: queuing unknown CIS tuple 0x82 (1 bytes)
    [    1.035458] mmc0: new high speed SDIO card at address 0001
    [    1.095728] sun4i-drm display-engine: fb0:  frame buffer device
    [    1.102801] [drm] Initialized sun4i-drm 1.0.0 20150629 for display-engine on minor 0
    [    1.111292] cfg80211: Loading compiled-in X.509 certificates for regulatory database
    [    1.127244] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
    [    1.135027] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
    [    1.143760] cfg80211: failed to load regulatory.db
    [    1.220764] random: crng init done
    [    3.486017] VFS: Mounted root (jffs2 filesystem) on device 31:3.
    [    3.493872] devtmpfs: mounted
    [    3.501502] Freeing unused kernel memory: 1024K
    [   11.022364] esp8089: module is from the staging directory, the quality is unknown, you have been warned.
    [   11.039883] 
    [   11.039883] ***** EAGLE DRIVER VER:bdf5087c3deb*****
    [   11.039883] 
    [   11.050727] esp_sdio_dummy_probe enter
    [   11.268002] esp_sdio_init power up OK
    [   11.733562] esp_host:bdf5087c3deb
    [   11.733562] esp_target: e826c2b3c9fd 57 18202
    [   11.733562] 
    [   11.743109] first normal exit
    [   11.746382] esp_sdio_remove enter
    [   11.750154] sif_disable_irq release irq failed
    [   11.868249] eagle_sdio: probe of mmc0:0001:1 failed with error -110
    ifconfig: SIOCGIFFLAGS: No such device
    Starting logging: OK
    Initializing random number generator... done.
    [   12.568573] mmc0: card 0001 removed

Welcome to Lichee Pi
Lichee login: 
