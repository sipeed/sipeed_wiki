jffs2文件系统挂载不上的常见原因
=====================================================

.. contents:: 本文目录

内核命令行不正确
-----------------------------------------------------

:: 

   [ 0.000000] Kernel command line: console=ttyS0,115200 earlyprintk panic=5 rootwait mtdparts=spi32766.0:1M(uboot)ro,64k(dtb)ro,4M(kernel)ro,3008k(rootfs) root=31:03 rw rootfstype=jffs2

内核命令行应正确显示分区信息，如果分区信息不正确则无法正确挂载。

分区信息在 *include/configs/sun8i.h* 里修改

.. code-block:: c
   :caption: vi include/configs/sun8i.h
    
    #define CONFIG_BOOTCOMMAND   "sf probe 0; "                           \
                                "sf read 0x41800000 0x100000 0x10000; "  \
                                "sf read 0x41000000 0x110000 0x400000; " \
                                "bootz 0x41000000 - 0x41800000"

    #define CONFIG_BOOTARGS      "console=ttyS0,115200 earlyprintk panic=5 rootwait " \
                                "mtdparts=spi32766.0:1M(uboot)ro,64k(dtb)ro,4M(kernel)ro,-(rootfs) root=31:03 rw rootfstype=jffs2"

识别不到分区
-----------------------------------------------------

正常识别到分区，应该报以下信息：

:: 

    [    0.862858] m25p80 spi32766.0: w25q128 (16384 Kbytes)
    [    0.867927] in cmdline partion
    [    0.871123] p4 : size=100000
    [    0.874005] p4 : size=10000
    [    0.876796] p4 : size=400000
    [    0.879714] p4 : size=2f0000
    [    0.882596] spi32766.0: parser cmdlinepart: 4
    [    0.886949] 4 cmdlinepart partitions found on MTD device spi32766.0
    [    0.893230] Creating 4 MTD partitions on "spi32766.0":
    [    0.898374] 0x000000000000-0x000000100000 : "uboot"
    [    0.904828] 0x000000100000-0x000000110000 : "dtb"
    [    0.910973] 0x000000110000-0x000000510000 : "kernel"
    [    0.917258] 0x000000510000-0x000000800000 : "rootfs"

如果没有显示以上信息，则需要确认有无勾选相关驱动

进入到 :menuselection:`Device Drivers --> Memory Technology Device (MTD) support` ，

确保选择上mtd的 **<*> Command line partition table parsing** 支持，该项目用来解析uboot传递过来的flash分区信息。

以及SPI-NOR 设备的支持。

添加对jffs2文件系统的支持，路径在 :menuselection:`File systems --> Miscellaneous filesystems --> Journalling Flash File System v2 (JFFS2) support`

jffs2 Magic bitmask 错误
-----------------------------------------------------

:: 

    jffs2: Node at 0x00000f6c with length 0x00000144 would run over the end of the erase block
    [    1.133830] jffs2: Perhaps the file system was created with the wrong erase size?
    [    1.141435] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00000f70: 0x0144 instead
    [    1.150994] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00000f74: 0x912a instead
    [    1.160547] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00000f78: 0x0002 instead
    [    1.170127] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00000f7c: 0x000d instead
    [    1.180689] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00000f80: 0x81a4 instead
    [    1.190183] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00000f84: 0x03e8 instead
    [    1.199668] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00000f88: 0x11d8 instead
    [    1.209151] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00000f8c: 0xdec2 instead
    [    1.218634] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00000f90: 0xdec2 instead
    [    1.228102] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00000f94: 0xdec2 instead
    [    1.237581] jffs2: Further such events for this erase block will not be printed
    [    1.245110] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00001000: 0x3fb1 instead
    [    1.254615] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00001004: 0x1a28 instead
    [    1.264102] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00001008: 0x7f01 instead
    [    1.273586] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x0000100c: 0x505d instead
    [    1.283098] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00001010: 0x84c8 instead
    [    1.292588] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00001014: 0xd8d1 instead
    [    1.302072] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00001018: 0x4001 instead
    [    1.311555] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x0000101c: 0x8485 instead
    [    1.321033] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00001020: 0x65b1 instead
    [    1.330514] jffs2: jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00001024: 0x5d81 instead

该错误有若干种可能：

1. jffs2镜像生成错误

   ``mkfs.jffs2 -s 0x100 -e 0x10000 -p 0xAF0000 -d rootfs-brmin -o jffs2-brmin.img``

   - 这里-s代表页大小，普通spi nor flash的页大小是256字节，即0x100
   - -e表示擦除的块大小，普通spi nor flash的块大小是64K字节，即0x10000
   - -p表示分区大小，在生成时会擦除分区大小的flash初始化。
   - 这里必须和uboot里指定的分区大小一致，否则会出现脏页。
2. 内核使用了扇区擦除

   - mkfs.jffs2 使用的最小擦除尺寸是8KB，而spi flash的扇区大小是4KB，所以按照扇区擦除的话，会无法使用，所以必须使用块擦除。
   - 编译内核前先确认下drivers/mtd/spi-nor/spi-nor.c里，自己使用的flash的相关信息
   - ``#define SECT_4K BIT(0) /* SPINOR_OP_BE_4K works uniformly */``
   - 如果发现信息里有SECT_4K，则会导致jffs2不能正常擦除（64KB），需要去掉该flag。

其它摘录
-----------------------------------------------------


:: 

    Question1：JFFS2 error: (1) jffs2_build_inode_pass1: child dir "alsa" (ino #1159) of dir ino #1074 appears to be a hard link
    JFFS2 error: (1) jffs2_build_inode_pass1: child dir "l" (ino #1170) of dir ino #1075 appears to be a hard link
    原由 : flash没有erase彻底.
    VFS: Mounted root (jffs2 filesystem) on device 31:1. Freeing init memory: 136K
    JFFS2 notice: (1) check_node_data: wrong data CRC in data node at 0x0f0a7f78: read 0x4462b066, calculated 0x48ea177f.
    JFFS2 error: (488) jffs2_do_read_inode_internal: Argh. Special inode #139 with mode 0x61b0 had more than one node iget() failed for ino #139 mknod: /dev/null: File exists
    Populating /dev using udev: udevd (499): /proc/499/oom_adj is deprecated, please use /proc/499/oom_score_adj instead.
    JFFS2 error: (500) jffs2_do_read_inode_internal: Argh. Special inode #1123 with mode 0x21b0 had more than one node iget() failed for ino #1123
    Question2：jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x00000024: 0x2b10 instead
    mkfs.jffs2 -s 的参数问题 对照FLASH的大小再重新生成镜像文件过即可 The answer this means that the data on your flash device is not a valid JFFS2 file system.
    There is no single solution for this problem, but we will try to provide you some ideas how to fix this.
    The first question you should try to answer is "why the data on my flash device is incorrect so that JFFS2 rejects to deal with it?". There are may be a plenty of reasons, e.g.:
    you flash driver is severely buggy so it reads trash instead of valid data;
    you flashed some trash instead of a valid JFFS2 image;
    you did not manage to flash JFFS2 image correctly so that you ended up with
    garbage on your flash, although the original image was perfectly fine;
    you forgot to erase your flash before flashing it, etc.
    Anyways, JFFS2 wouldn't complain if it was able to find correct data. As it does complain, there is something wrong with the data it reads.
    One common mistake is to use /dev/mtdX or /dev/mtdblockX devices to flash JFFS2 images on NAND flashes. E.g.
    cp jffs2_fs.img /dev/mtd2
    This is incorrect because when dealing with NAND flashes one has to skip bad
    eraseblocks and write only in NAND page size chunks. Please, use the nandwrite utility instead.
    Also please, do not forget to erase your flash before flashing the image. You may use the
    flash_eraseall utility for this. And it makes sense to make sure the erase functionality
    actually works by reading the erased MTD device back and checking that only 0xFF bytes were read.
    You may try to check if your flash driver works correctly and if you flashed the file system image correctly by means of reading the flash back after you have flashed your image, and compare the read image with the original one. Please, use the nandread utility to read from NAND flashes.
    You can also do the following experiment to make sure JFFS2 works well. Erase your MTD device and mount it to JFFS2. You will end up with an empty file system. Copy some files to the JFFS2 file system and unmount it. Then mount it again and see if it mounts without problems. If it does, this is most probably not a JFFS2 bug.
    Question3：Empty flash at 0xXXXXXXXX ends at 0xXXXXXXXX
    This message is generated if a block of data is partially written. It is generally not a sign of any problem.
    Question4：Name CRC failed on node at 0x00b620c8: Read 0x640c8ca3, calculated 0x795111fe
    重启，则不会有如上CRC错误信息。 问题原因：
    我在烧写jffs2 img之前，使用fis init -f 来擦除flash。fis init -f 命令执行完以后，flash空间就都是0xFF了！即使在mkfs.jffs2的时候使用'-p'参数指定最终输出img的大小，但是超出文件系统的部分也会被填充为0xFF!但这可不是jffs2的格式！
    我用fis create分了5M多（0x590000）的分区，但是jffs2fs.img只有不到3M（0x250000），那么把它烧写到flash以后，分区中除了jffs2 img之外剩余的flash空间（大概2M）全是0xFF，这不是jffs2要求的格式，所以，会发出CRC错误的信息。假如有一种工具，他可以将flash format为jffs2的格式，那么就不会出现这个问题了。目前我还没有找到这种工具，但是，可以确信的是：上面的CRC错误是不影响jffs2文件系统的使用
    http://blog.chinaunix.net/space.php?uid=20727076&do=blog&id=1885384

    Question5: VFS: Mounted root (jffs2 filesystem) readonly.
    Freeing unused kernel memory: 304k freed Error -3 while decompressing! 804878c4(1884)->81200000(16384)
    Failed to execute /linuxrc. Attempting defaults...
    Kernel panic - not syncing: No init found. Try passing init= option to kernel.
    原由 : 没有仔细看 mkfs.jffs2 的手册, 须要指定-b参数, 大小与PAGE_SIZE一样 (查看.config文件 CONFIG_PAGE_SIZE_16KB=y).
    Question6:
    共提示以下几种错误：
    Empty flash at 0x00258c88 ends at 0x00258c8c
    jffs2_scan_inode_node(): CRC failed on node at 0x002873f0: Read 0x50dc72ec, calculated 0xafbffd1d
    jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x002d24ac: 0x000d instead JFFS2 notice: (1) jffs2_build_xattr_subsystem: complete building xattr subsystem, 0 of xdatum (0 unchecked, 0 orphan) and 0 of xref (0 dead, 0 orphan) found. VFS: Mounted root (jffs2 filesystem). Freeing init memory: 124K
    JFFS2 notice: (1) check_node_data: wrong data CRC in data node at 0x00012000: read 0x1a9bfab2, calculated 0xdc27bef6.
    JFFS2 notice: (728) read_dnode: wrong data CRC in data node at 0x0000e438: read 0x3dcf6001, calculated 0xcb81f1ee.
    JFFS2 warning: (1) jffs2_do_read_inode_internal: no data nodes found for ino #14 JFFS2 notice: (1) jffs2_do_read_inode_internal: but it has children so we fake some modes for it
    Failed to execute /linuxrc. Attempting defaults...
    Kernel panic - not syncing: No init found. Try passing init= option to kernel. 分析：
    记得JFFS2是采用自己的ECC算法，但是在内核中又打开了S3C2410_HARDWARE_ECC 解决方案： 去掉硬件ECC
