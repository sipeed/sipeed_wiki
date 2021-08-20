# spi-flash 启动适配


对于从spi-flash启动系统，需要对 uboot / dts /内核配置都有所修改，打包与烧写请参考[一键烧录及脚本使用说明](./onekey.md)

以下将以16M flash为例，介绍 spi flash 的适配过程。

## 分区规划


下表为分区规划表：

|分区序号|分区大小|分区作用|地址空间及分区名
|----|----|----|----|
|mtd0 | 1MB (0x100000) | spl+uboot | 0x0000000-0x0100000 : “uboot”|
|mtd1 | 64KB (0x10000) | dtb文件 | 0x0100000-0x0110000 : “dtb”|
|mtd2 | 4MB (0x400000) | linux内核 | 0x0110000-0x0510000 : “kernel”|
|mtd3 | 剩余 (0xAF0000) | 根文件系统 | 0x0510000-0x1000000 : “rootfs”|


## uboot 修改


以下是对 uboot 进行适配的流程描述；

### bootcmd修改

在uboot源码目录下 进入 ./include/configs/

```
#define CONFIG_BOOTCOMMAND   "sf probe 0:50000000; "                           \    
                            "sf read 0x80C00000 0x100000 0x4000; "  \
                            "sf read 0x80008000 0x110000 0x400000; " \
                            "bootz 0x80008000 - 0x80C00000"
```

按照行数解释如下：

> 1.  挂载 spi-flash
> 2.  读取 spi-flash 1M（0x100000）位置 64KB(0x4000)大小的 dtb 到地址
>     0x80C00000
> 3.  读取 spi-flash 1M+64K（0x110000）位置 4MB(0x400000)大小的 zImage
>     到地址 0x80008000
> 4.  从 0x80008000 启动内核，从 0x80C00000 读取设备树配置

回到 uboot 源码一级目录，`make ARCH=arm menuconfig` 进入TUI配置；

取消勾选 *[ ] Enable a default value for bootcmd*

### bootargs修改

勾选 *[\*] Enable boot arguments；*

在下方一项中填入 bootargs 参数:

    console=ttyS0,115200 panic=5 rootwait root=/dev/mtdblock3 rw rootfstype=jffs2

(root=/dev/mtdblock3 指的是mtd设备第三分区，分区指定在dts中声明)

### dts 修改

修改内核源码目录下的 ./arch/arm/boot/dts/suniv-f1c100s-licheepi-nano.dts

``` 
&spi0 {
    pinctrl-names = "default";
    pinctrl-0 = <&spi0_pins_a>;
    status = "okay";
    spi-max-frequency = <50000000>;
    flash: w25q128@0 {
        #address-cells = <1>;
        #size-cells = <1>;
        compatible = "winbond,xt25f128b", "jedec,spi-nor";
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
```

此处在dts中为mtd设备预先划分好了分区内容，内核将会自动解析

另一种通过bootargs传递给内核进行解析分区信息的方法，请参考 [Lichee Zerospi-flash启动](http://zero.lichee.pro/%E7%B3%BB%E7%BB%9F%E5%BC%80%E5%8F%91/SPI_flash_build.html#id4)

内核配置修改
------------

勾选 File systems ‣ Miscellaneous filesystems ‣ Journalling Flash File
System v2 (JFFS2) support

![jffs2](https://box.kancloud.cn/3be64c60667c0aa3a906f095171d1fda_1396x746.png)

修改源码下的 ./drivers/mtd/spi-nor.c


	添加对应spi-flash；如 xt25f128b :

```
static const struct flash_info spi_nor_ids[] = {
	...
	{ "w25q128", INFO(0xef4018, 0, 64 * 1024, 256, SECT_4K) },	//在此行后添加
	{ "xt25f128b", INFO(0x0bf4018, 0, 64 * 1024, 256, 0) },	//添加新spi-flash
	...
}

```

## 二进制bin 打包


以16M 大小flash镜像打包脚本为例：

```
#!/bin/sh
UBOOT_FILE=./u-boot/u-boot-sunxi-with-spl.bin
DTB_FILE=./Linux/arch/arm/boot/dts/suniv-f1c100s-licheepi-nano.dtb
KERNEL_FILE=./Linux/arch/arm/boot/zImage
ROOTFS_FILE=./buildroot-2021.02.4/output/images/rootfs.tar
MOD_FILE=./Linux/out/lib/modules/4.15.0-rc8-licheepi-nano+

dd if=/dev/zero of=flashimg.bin bs=1M count=16 &&\
dd if=$UBOOT_FILE of=flashimg.bin bs=1K conv=notrunc &&\
dd if=$DTB_FILE of=flashimg.bin bs=1K seek=1024 conv=notrunc &&\
dd if=$KERNEL_FILE of=flashimg.bin bs=1K seek=1088 conv=notrunc &&\
mkdir rootfs
tar -xvf $ROOTFS_FILE -C ./rootfs &&\
cp -r $MOD_FILE rootfs/lib/modules/ &&\

#为根文件系统制作jffs2镜像包
#--pad参数指定 jffs2大小
#由此计算得到 0x1000000(16M)-0x10000(64K)-0x100000(1M)-0x400000(4M)=0xAF0000
mkfs.jffs2 -s 0x100 -e 0x10000 --pad=0xAF0000 -d rootfs/ -o jffs2.img &&\
dd if=jffs2.img of=flashimg.bin bs=1K seek=5184 conv=notrunc &&\
rm -rf rootfs &&\
rm jffs2.img
```

以上脚本通过对一个生成的16M空bin文件填充 uboot、dtb、kernel、rootfs 生成
16M 镜像，如需修改，请注意各个文件的大小，修改成对应地址（注意对齐）。

至此，SPI系统各部分已编译完成，通过sunxi-fel进行烧写即可；

## bin 烧录


    sudo sunxi-fel -p spiflash-write 0 $YOUR_IMG_FILE

或请参考镜像包中的 write\_flash.sh 烧录脚本；

启动后使用 账号：root 密码：licheepi 登录

> **交流与答疑**
> 对于本节内容，如有疑问，欢迎到 [SPI Flash系统编译交流帖](http://bbs.lichee.pro/d/31-spi-flash) 提问或分享经验。

## 附录 1.启动日志

```
U-Boot 2018.01-05688-ga9729b3241 (Aug 18 2021 - 11:38:59 +0800) Allwinner Technology

CPU:   Allwinner F Series (SUNIV)
Model: Lichee Pi Nano
DRAM:  32 MiB
MMC:   SUNXI SD/MMC: 0
SF: Detected xt25f128b with page size 256 Bytes, erase size 4 KiB, total 16 MiB
*** Warning - bad CRC, using default environment

Setting up a 800x480 lcd console (overscan 0x0)
In:    serial@1c25000
Out:   serial@1c25000
Err:   serial@1c25000
Net:   No ethernet found.
starting USB...
No controllers found
Hit any key to stop autoboot:  0 
SF: Detected xt25f128b with page size 256 Bytes, erase size 4 KiB, total 16 MiB
device 0 offset 0x100000, size 0x4000
SF: 16384 bytes @ 0x100000 Read: OK
device 0 offset 0x110000, size 0x400000
SF: 4194304 bytes @ 0x110000 Read: OK
## Flattened Device Tree blob at 80c00000
   Booting using the fdt blob at 0x80c00000
   Loading Device Tree to 80e03000, end 80e07f36 ... OK

Starting kernel ...

[    0.000000] Booting Linux on physical CPU 0x0
[    0.000000] Linux version 4.15.0-rc8-licheepi-nano+ (wangxi@ThinkPad-X1-Carbon-6th) (gcc version 7.2.1 20171011 (Linaro GCC 7.2-2017.11)) #1 Tue Aug 17 19:20:35 CST 2021
[    0.000000] CPU: ARM926EJ-S [41069265] revision 5 (ARMv5TEJ), cr=0005317f
[    0.000000] CPU: VIVT data cache, VIVT instruction cache
[    0.000000] OF: fdt: Machine model: Lichee Pi Nano
[    0.000000] Memory policy: Data cache writeback
[    0.000000] random: fast init done
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 8128
[    0.000000] Kernel command line: console=ttyS0,115200 panic=5 rootwait root=/dev/mtdblock3 rw rootfstype=jffs2
[    0.000000] Dentry cache hash table entries: 4096 (order: 2, 16384 bytes)
[    0.000000] Inode-cache hash table entries: 2048 (order: 1, 8192 bytes)
[    0.000000] Memory: 22688K/32768K available (6144K kernel code, 234K rwdata, 1344K rodata, 1024K init, 233K bss, 10080K reserved, 0K cma-reserved, 0K highmem)
[    0.000000] Virtual kernel memory layout:
[    0.000000]     vector  : 0xffff0000 - 0xffff1000   (   4 kB)
[    0.000000]     fixmap  : 0xffc00000 - 0xfff00000   (3072 kB)
[    0.000000]     vmalloc : 0xc2800000 - 0xff800000   ( 976 MB)
[    0.000000]     lowmem  : 0xc0000000 - 0xc2000000   (  32 MB)
[    0.000000]     pkmap   : 0xbfe00000 - 0xc0000000   (   2 MB)
[    0.000000]     modules : 0xbf000000 - 0xbfe00000   (  14 MB)
[    0.000000]       .text : 0x(ptrval) - 0x(ptrval)   (7136 kB)
[    0.000000]       .init : 0x(ptrval) - 0x(ptrval)   (1024 kB)
[    0.000000]       .data : 0x(ptrval) - 0x(ptrval)   ( 235 kB)
[    0.000000]        .bss : 0x(ptrval) - 0x(ptrval)   ( 234 kB)
[    0.000000] SLUB: HWalign=32, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
[    0.000000] NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
[    0.000051] sched_clock: 32 bits at 24MHz, resolution 41ns, wraps every 89478484971ns
[    0.000120] clocksource: timer: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 79635851949 ns
[    0.000748] Console: colour dummy device 80x30
[    0.000841] Calibrating delay loop... 203.16 BogoMIPS (lpj=1015808)
[    0.070249] pid_max: default: 32768 minimum: 301
[    0.070574] Mount-cache hash table entries: 1024 (order: 0, 4096 bytes)
[    0.070619] Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes)
[    0.072204] CPU: Testing write buffer coherency: ok
[    0.074118] Setting up static identity map for 0x80100000 - 0x80100058
[    0.076819] devtmpfs: initialized
[    0.083560] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
[    0.083641] futex hash table entries: 256 (order: -1, 3072 bytes)
[    0.083927] pinctrl core: initialized pinctrl subsystem
[    0.086209] NET: Registered protocol family 16
[    0.088156] DMA: preallocated 256 KiB pool for atomic coherent allocations
[    0.090104] cpuidle: using governor menu
[    0.114953] SCSI subsystem initialized
[    0.115342] usbcore: registered new interface driver usbfs
[    0.115497] usbcore: registered new interface driver hub
[    0.115726] usbcore: registered new device driver usb
[    0.116195] pps_core: LinuxPPS API ver. 1 registered
[    0.116226] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.116296] PTP clock support registered
[    0.116864] Advanced Linux Sound Architecture Driver Initialized.
[    0.118475] clocksource: Switched to clocksource timer
[    0.147854] NET: Registered protocol family 2
[    0.149563] TCP established hash table entries: 1024 (order: 0, 4096 bytes)
[    0.149647] TCP bind hash table entries: 1024 (order: 0, 4096 bytes)
[    0.149697] TCP: Hash tables configured (established 1024 bind 1024)
[    0.150083] UDP hash table entries: 256 (order: 0, 4096 bytes)
[    0.150159] UDP-Lite hash table entries: 256 (order: 0, 4096 bytes)
[    0.150699] NET: Registered protocol family 1
[    0.152849] NetWinder Floating Point Emulator V0.97 (double precision)
[    0.154808] Initialise system trusted keyrings
[    0.155331] workingset: timestamp_bits=30 max_order=13 bucket_order=0
[    0.171845] jffs2: version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
[    0.187710] Key type asymmetric registered
[    0.187756] Asymmetric key parser 'x509' registered
[    0.187980] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 251)
[    0.188019] io scheduler noop registered
[    0.188037] io scheduler deadline registered
[    0.189023] io scheduler cfq registered (default)
[    0.189066] io scheduler mq-deadline registered
[    0.189086] io scheduler kyber registered
[    0.190307] sun4i-usb-phy 1c13400.phy: Couldn't request ID GPIO
[    0.200698] suniv-pinctrl 1c20800.pinctrl: initialized sunXi PIO driver
[    0.389750] Serial: 8250/16550 driver, 8 ports, IRQ sharing disabled
[    0.396809] console [ttyS0] disabled
[    0.417093] 1c25000.serial: ttyS0 at MMIO 0x1c25000 (irq = 23, base_baud = 6250000) is a 16550A
[    0.858241] console [ttyS0] enabled
[    0.869124] panel-simple panel: panel supply power not found, using dummy regulator
[    0.900331] loop: module loaded
[    0.904340] SCSI Media Changer driver v0.25 
[    0.912459] m25p80 spi0.0: xt25f128b (16384 Kbytes)
[    0.917422] 4 ofpart partitions found on MTD device spi0.0
[    0.923010] Creating 4 MTD partitions on "spi0.0":
[    0.927858] 0x000000000000-0x000000100000 : "u-boot"
[    0.935841] 0x000000100000-0x000000110000 : "dtb"
[    0.943424] 0x000000110000-0x000000510000 : "kernel"
[    0.951257] 0x000000510000-0x000001000000 : "rootfs"
[    0.959588] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    0.966129] ehci-platform: EHCI generic platform driver
[    0.971774] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    0.978008] ohci-platform: OHCI generic platform driver
[    0.983744] usbcore: registered new interface driver usb-storage
[    0.990886] udc-core: couldn't find an available UDC - added [g_cdc] to list of pending drivers
[    1.000090] i2c /dev entries driver
[    1.058608] sunxi-mmc 1c0f000.mmc: base:0x5e6e6c4f irq:19
[    1.066298] usbcore: registered new interface driver usbhid
[    1.072015] usbhid: USB HID core driver
[    1.095111] NET: Registered protocol family 17
[    1.099787] Key type dns_resolver registered
[    1.106510] Loading compiled-in X.509 certificates
[    1.123050] sun4i-drm display-engine: bound 1e60000.display-backend (ops 0xc0736c58)
[    1.131937] sun4i-drm display-engine: bound 1c0c000.lcd-controller (ops 0xc0735f3c)
[    1.139747] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    1.146355] [drm] No driver support for vblank timestamp query.
[    1.284852] Console: switching to colour frame buffer device 100x30
[    1.324570] sun4i-drm display-engine: fb0:  frame buffer device
[    1.331720] [drm] Initialized sun4i-drm 1.0.0 20150629 for display-engine on minor 0
[    1.340961] usb_phy_generic usb_phy_generic.0.auto: usb_phy_generic.0.auto supply vcc not found, using dummy regulator
[    1.353037] musb-hdrc musb-hdrc.1.auto: MUSB HDRC host driver
[    1.358971] musb-hdrc musb-hdrc.1.auto: new USB bus registered, assigned bus number 1
[    1.369307] hub 1-0:1.0: USB hub found
[    1.373247] hub 1-0:1.0: 1 port detected
[    1.378985] using random self ethernet address
[    1.383523] using random host ethernet address
[    1.389924] usb0: HOST MAC 22:8a:8d:91:11:6e
[    1.394315] usb0: MAC ea:69:6d:6e:87:be
[    1.398306] g_cdc gadget: CDC Composite Gadget, version: King Kamehameha Day 2008
[    1.405900] g_cdc gadget: g_cdc ready
[    1.410628] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[    1.428340] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
[    1.435272] vcc3v3: disabling
[    1.438260] ALSA device list:
[    1.441317]   #0: Loopback 1
[    1.445124] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
[    1.453883] cfg80211: failed to load regulatory.db
[    1.562738] random: crng init done
[    2.123045] jffs2: notice: (1) jffs2_build_xattr_subsystem: complete building xattr subsystem, 0 of xdatum (0 unchecked, 0 orphan) and 0 of xref (0 dead, 0 orphan) found.
[    2.143057] VFS: Mounted root (jffs2 filesystem) on device 31:3.
[    2.151702] devtmpfs: mounted
[    2.161730] Freeing unused kernel memory: 1024K
Starting syslogd: OK
Starting klogd: OK
Running sysctl: OK
Initializing random number generator: OK
Saving random seed: OK
Starting network: OK

Welcome to Buildroot
buildroot login: 
```