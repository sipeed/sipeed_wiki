BSP内核构建走读
===================================

.. contents:: 本文目录


camdriod中对lichee的构建过程
-----------------------------------

使用BSP内核的话，需要使用官方sdk编译camdriod并从中取出uImage。

鉴于camdriod较大，所以我们先简单走读下camdriod中对lichee的构建过程，扣出这部分内容。

camdriod的构建脚本：

.. code-block:: bash

   #!/bin/bash
   source build/envsetup.sh &&
   lunch &&
   mklichee &&
   extract-bsp &&
   make -j8 &&
   pack
   
*source build/envsetup.sh* 这里是include各种环境变量，比如就添加了 *tiger_cdr-eng* 选项，这里先不管它。

lunch就是选择目标板配置了，是在 *build/envsetup.sh* 中的函数。

接着就是关键的mklichee了，在 *device/softwinner/common/vendorsetup.sh* 里，深入看下：

.. code-block:: bash
   :caption: 首先是一堆常量定义，放这里备查 

    function set_environment()
    {
            LICHEE_CHIP="sun8iw8p1"
            export CAMLINUX_BUILD_TOP=`pwd`
            export DEVICE_DIR=$CAMLINUX_BUILD_TOP/device/softwinner
            export TARGET_OUT=$CAMLINUX_BUILD_TOP/output
            export OUT_DIR=$CAMLINUX_BUILD_TOP/out
            export LICHEE_DIR=$CAMLINUX_BUILD_TOP/../lichee
            export LICHEE_OUT_DIR=$LICHEE_DIR/out/sun8iw8p1/linux
            export BR_ROOTFS_DIR=$TARGET_OUT/target
            export LICHEE_BR_DIR=${LICHEE_DIR}/buildroot
            export LICHEE_KERN_DIR=${LICHEE_DIR}/linux-3.4
            export LINUXOUT_MODULE_DIR=$LICHEE_KERN_DIR/output/lib/modules/*/*
            export LICHEE_KERN_OUTDIR=$LICHEE_KERN_DIR/output
            export LICHEE_TOOLS_DIR=${LICHEE_DIR}/tools
            export LICHEE_UBOOT_DIR=${LICHEE_DIR}/brandy/u-boot-2011.09
    }

.. code-block:: bash
   :caption: mklichee本体：

    function mklichee()
    {
        mksetting		#显示目前的配置信息
        mk_info "build lichee ..."
            mkbr && mkkernel
        #    mkbr && mkkernel && mkuboot
        [ $? -ne 0 ] && return 1
            return 0
    }

mkbr是运行了 ``buildroot/scripts/build.sh buildroot linux sun8iw8p1``

.. code-block:: bash
   :caption: gcc-linaro.tar.bz2

    function mkbr()
    {
        mk_info "build buildroot ..."
        local build_script
        build_script="scripts/build.sh"
            LICHEE_PLATFORM="linux"

        (cd ${LICHEE_BR_DIR} && [ -x ${build_script} ] && ./${build_script} "buildroot" ${LICHEE_PLATFORM} ${LICHEE_CHIP})
        [ $? -ne 0 ] && mk_error "build buildroot Failed" && return 1
        mk_info "build buildroot OK."
    }

.. code-block:: bash
   :caption: build.sh写着：

    if [ "x${LICHEE_PLATFORM}" = "xlinux" ] ; then
        build_buildroot
        export PATH=${LICHEE_BR_OUT}/external-toolchain/bin:$PATH
        build_external
    else
        build_toolchain

LICHEE_PLATFORM并没有被传入，实际执行的是下面这个build_toolchain：

.. code-block:: bash
   :caption: build_toolchain：

    build_toolchain()
    {
        local tooldir="${LICHEE_BR_OUT}/external-toolchain"
        mkdir -p ${tooldir}
        if [ -f ${tooldir}/.installed ] ; then
            printf "external toolchain has been installed\n"
        else
            printf "installing external toolchain\n"
            printf "please wait for a few minutes ...\n"
            tar --strip-components=1 \
                -jxf ${LICHEE_BR_DIR}/dl/gcc-linaro.tar.bz2 \
                -C ${tooldir}
            [ $? -eq 0 ] && touch ${tooldir}/.installed
        fi

        export PATH=${tooldir}/bin:${PATH}
    }

这里LICHEE_BR_OUT是 *lichee/out/sun8iw8p1/linux/common/buildroot*

LICHEE_BR_DIR是lichee/buildroot, 需要先导入。

这里使用的linaro版本比较老。注意如果使用较新的gcc反而会出错。

这里就是解压了linaro-gcc，并加入到环境变量。

mkbr看完了，接下来看mkkernel。

.. code-block:: bash
   :caption: mkkernel

    function mkkernel()
    {
    local platformdef=$tdevice
        if [ ! -n $tdevice ]; then
                echo "Please lunch device"
                return 1
        fi

        echo "Make the kernel"  
        echo "platformdef="${platformdef}
        (cd ${LICHEE_KERN_DIR}/; ./build.sh -p ${platformdef})
        [ $? -ne 0 ] && mk_error "build mkkernel fail" && return 1
    echo "Make the kernel finish"
        return 0
    }

执行的是lichee/linux-3.4/build.sh, 跟下去是执行了：
   
   ``./scripts/build_${PLATFORM}.sh all``

看script目录下，有：

:: 

    build_crane-cdr.sh      
    build_crane-ipc.sh      
    build_crane-sdv.sh      
    build_crane-standard.sh 
    build_rootfs.sh         
    build.sh                
    build_sun6i.sh         
    build_sun8iw8p1.sh      
    build_tiger-cdr.sh      
    build_tiger-ipc.sh      
    build_tiger-standard.sh

就是代表的可以构建的板子型号。我们实际编译的时候只需要执行 *build_tiger-cdr.sh* 即可。

综上所述，需要剥离camdriod所用的lichee内核，只需要：

   1. 解压buildroot/dl/gcc-linarno.tar.gz 到lichee/out/sun8iw8p1/linux/common/buildroot/external-toolchain，并加入环境变量（这步其实在下一步里包含了）
   2. 执行build_tiger-cdr.sh

启动信息
-----------------------------------

.. code-block:: python

    Starting kernel ...

    [sun8i_fixup]: From boot, get meminfo:
        Start:	0x40000000
        Size:	64MB
    ion_carveout reserve: 28m@0 28m@0
    ion_reserve_common: ion reserve: [0x42400000, 0x44000000]!
    [    0.000000] Booting Linux on physical CPU 0
    [    0.000000] Linux version 3.4.39 (root@bf756b445919) (gcc version 4.6.3 20120201 (prerelease) (crosstool-NG linaro-1.13.1-2012.02-20120222 - Linaro GCC 2012.02) ) #29 Wed Nov 29 10:53:16 UTC 2017
    [    0.000000] bootconsole [earlycon0] enabled
    [    0.000000] Initialized persistent memory from 41d20800-41d307ff
    [    0.000000] Kernel command line: console=ttyS0,115200 panic=5 rootwait root=/dev/mmcblk0p2 earlyprintk rw
    [    0.000000] PID hash table entries: 256 (order: -2, 1024 bytes)
    [    0.000000] Dentry cache hash table entries: 8192 (order: 3, 32768 bytes)
    [    0.000000] Inode-cache hash table entries: 4096 (order: 2, 16384 bytes)
    [    0.000000] Memory: 64MB = 64MB total
    [    0.000000] Memory: 29312k/29312k available, 36224k reserved, 0K highmem
    [    0.000000] Virtual kernel memory layout:
    [    0.000000]     vector  : 0xffff0000 - 0xffff1000   (   4 kB)
    [    0.000000]     fixmap  : 0xfff00000 - 0xfffe0000   ( 896 kB)
    [    0.000000]     vmalloc : 0xc4800000 - 0xff000000   ( 936 MB)
    [    0.000000]     lowmem  : 0xc0000000 - 0xc4000000   (  64 MB)
    [    0.000000]     modules : 0xbf000000 - 0xc0000000   (  16 MB)
    [    0.000000]       .text : 0xc0008000 - 0xc050d000   (5140 kB)
    [    0.000000]       .init : 0xc050d000 - 0xc0530000   ( 140 kB)
    [    0.000000]       .data : 0xc0530000 - 0xc05ab500   ( 494 kB)
    [    0.000000]        .bss : 0xc05ab524 - 0xc068c28c   ( 900 kB)
    [    0.000000] NR_IRQS:544
    [    0.000000] Architected local timer running at 24.00MHz.
    [    0.000000] Switching to timer-based delay loop
    [    0.000000] sched_clock: 32 bits at 24MHz, resolution 41ns, wraps every 178956ms
    [    0.000000] Console: colour dummy device 80x30
    [    0.014545] Calibrating delay loop (skipped), value calculated using timer frequency.. 4800.00 BogoMIPS (lpj=24000000)
    [    0.022936] pid_max: default: 32768 minimum: 301
    [    0.027778] Mount-cache hash table entries: 512
    [    0.030637] CPU: Testing write buffer coherency: ok
    [    0.035150] Setting up static identity map for 0x40396048 - 0x403960a0
    [    0.040773] devtmpfs: initialized
    [    0.045346] pinctrl core: initialized pinctrl subsystem
    [    0.049168] NET: Registered protocol family 16
    [    0.050362] DMA: preallocated 128 KiB pool for atomic coherent allocations
    [    0.056956] script_sysfs_init success
    [    0.060951] gpiochip_add: registered GPIOs 0 to 223 on device: sunxi-pinctrl
    [    0.068164] sunxi-pinctrl sunxi-pinctrl: initialized sunXi PIO driver
    [    0.070438] gpiochip_add: registered GPIOs 1024 to 1031 on device: axp-pinctrl
    [    0.078235] persistent_ram: uncorrectable error in header
    [    0.080020] persistent_ram: no valid data in buffer (sig = 0x75371537)
    [    0.091722] console [ram-1] enabled
    [    0.092266] Not Found clk pll_isp in script 
    [    0.094113] Not Found clk pll_video in script 
    [    0.098719] Not Found clk pll_ve in script 
    [    0.100012] Not Found clk pll_periph0 in script 
    [    0.104666] Not Found clk pll_de in script 
    [    0.113517] bio: create slab <bio-0> at 0
    [    0.113966] pwm module init!
    [    0.118375] SCSI subsystem initialized
    [    0.120028] usbcore: registered new interface driver usbfs
    [    0.125313] usbcore: registered new interface driver hub
    [    0.130165] usbcore: registered new device driver usb
    [    0.135149] twi_chan_cfg()340 - [twi0] has no twi_regulator.
    [    0.140018] twi_chan_cfg()340 - [twi1] has no twi_regulator.
    [    0.146123] Linux video capture interface: v2.00
    [    0.150126] gpiochip_add: gpios 1024..1028 (axp_pin) failed to register
    [    0.156916] Advanced Linux Sound Architecture Driver Version 1.0.25.
    [    0.160794] Switching to clocksource arch_sys_counter
    [    0.171015] NET: Registered protocol family 2
    [    0.171466] IP route cache hash table entries: 1024 (order: 0, 4096 bytes)
    [    0.177306] TCP established hash table entries: 2048 (order: 2, 16384 bytes)
    [    0.184207] TCP bind hash table entries: 2048 (order: 1, 8192 bytes)
    [    0.190440] TCP: Hash tables configured (established 2048 bind 2048)
    [    0.196921] TCP: reno registered
    [    0.200126] UDP hash table entries: 256 (order: 0, 4096 bytes)
    [    0.206122] UDP-Lite hash table entries: 256 (order: 0, 4096 bytes)
    [    0.212647] NET: Registered protocol family 1
    [    0.217253] standby_mode = 1. 
    [    0.219870] wakeup src cnt is : 3. 
    [    0.223491] pmu1_enable = 0x0. 
    [    0.226639] config_pmux_para: script_parser_fetch err. 
    [    0.232034] pmu2_enable = 0x0. 
    [    0.235126] add_sys_pwr_dm: get ldo name failed
    [    0.239818] add_sys_pwr_dm: get ldo name failed
    [    0.244317] add_sys_pwr_dm: get ldo name failed
    [    0.248900] add_sys_pwr_dm: get ldo name failed
    [    0.253610] add_sys_pwr_dm: get ldo name failed
    [    0.258090] add_sys_pwr_dm: get ldo name failed
    [    0.262796] add_sys_pwr_dm: get ldo name failed
    [    0.267274] add_sys_pwr_dm: get ldo name failed
    [    0.271877] add_sys_pwr_dm: get ldo name failed
    [    0.276566] add_sys_pwr_dm: get ldo name failed
    [    0.281061] after inited: sys_mask config = 0x0. 
    [    0.285927] dynamic_standby enalbe = 0x0. 
    [    0.290049] sunxi_reg_init enter
    [    0.295521] squashfs: version 4.0 (2009/01/31) Phillip Lougher
    [    0.299326] jffs2: version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
    [    0.306584] msgmni has been set to 57
    [    0.311246] io scheduler noop registered
    [    0.313995] io scheduler deadline registered
    [    0.318410] io scheduler cfq registered (default)
    [    0.323712] [DISP]disp_module_init
    [    0.326990] cmdline,disp=
    [    0.329889] [DISP] disp_get_rotation_sw,line:68:disp 0 out of range? g_rot_sw=0
    [    0.336609] [DISP] disp_init_connections,line:289:NULL pointer: 0, 0
    [    0.344754] [DISP] Fb_map_kernel_logo,line:924:Fb_map_kernel_logo failed!
    [    0.352381] [DISP] disp_sys_power_enable,line:387:some error happen, fail to get regulator 
    [    0.358275] [DISP] disp_sys_gpio_set_value,line:374:OSAL_GPIO_DevWRITE_ONEPIN_DATA, hdl is NULL
    [    0.367297] [DISP]disp_module_init finish
    [    0.371458] sw_uart_get_devinfo()1503 - uart0 has no uart_regulator.
    [    0.378007] uart0: ttyS0 at MMIO 0x1c28000 (irq = 32) is a SUNXI
    [    0.383640] sw_uart_pm()890 - uart0 clk is already enable
    [    0.389159] sw_console_se󙞠  0.397781] console [ttyS0] enabled, bootconsole disabled
    [    0.397781] console [ttyS0] enabled, bootconsole disabled
    [    0.405808] sunxi_spi_chan_cfg()1376 - [spi-0] has no spi_regulator.
    [    0.417215] spi spi0: master is unqueued, this is deprecated
    [    0.423980] m25p_probe()988 - Use the Dual Mode Read.
    [    0.429818] m25p80 spi0.0: found W25q128, expected at25df641
    [    0.436364] m25p80 spi0.0: W25q128 (16384 Kbytes)
    [    0.442069] Creating 4 MTD partitions on "spi0.0":
    [    0.447623] 0x000000000000-0x000000100000 : "uboot"
    [    0.454335] 0x000000100000-0x000000110000 : "script"
    [    0.461007] 0x000000110000-0x000000510000 : "kernel"
    [    0.467737] 0x000000510000-0x000001000000 : "rootfs"
    [    0.474560] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
    [    0.502308] sunxi-ehci sunxi-ehci.1: SW USB2.0 'Enhanced' Host Controller (EHCI) Driver
    [    0.511538] sunxi-ehci sunxi-ehci.1: new USB bus registered, assigned bus number 1
    [    0.520232] sunxi-ehci sunxi-ehci.1: irq 104, io mem 0xf1c1a000
    [    0.540038] sunxi-ehci sunxi-ehci.1: USB 0.0 started, EHCI 1.00
    [    0.547565] hub 1-0:1.0: USB hub found
    [    0.552045] hub 1-0:1.0: 1 port detected
    [    0.557035] sunxi-ehci sunxi-ehci.1: remove, state 1
    [    0.562716] usb usb1: USB disconnect, device number 1
    [    0.570093] [DISP] disp_lcd_pwm_enable,line:1021:pwm device hdl is NULL
    [    0.577820] sunxi-ehci sunxi-ehci.1: USB bus 1 deregistered
    [    0.594381] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
    [    0.621611] sunxi-ohci sunxi-ohci.1: SW USB2.0 'Open' Host Controller (OHCI) Driver
    [    0.630292] sunxi-ohci sunxi-ohci.1: new USB bus registered, assigned bus number 1
    [    0.638963] sunxi-ohci sunxi-ohci.1: irq 105, io mem 0xf1c1a400
    [    0.704775] hub 1-0:1.0: USB hub found
    [    0.709188] hub 1-0:1.0: 1 port detected
    [    0.714159] sunxi-ohci sunxi-ohci.1: remove, state 1
    [    0.719942] usb usb1: USB disconnect, device number 1
    [    0.726383] sunxi-ohci sunxi-ohci.1: USB bus 1 deregistered
    [    0.742856] Initializing USB Mass Storage driver...
    [    0.748591] usbcore: registered new interface driver usb-storage
    [    0.755417] USB Mass Storage support registered.
    [    0.761162] file system registered
    [    0.766892] android_usb gadget: Mass Storage Function, version: 2009/09/11
    [    0.774821] android_usb gadget: Number of LUNs=1
    [    0.780100]  lun0: LUN: removable file: (no medium)
    [    0.786312] android_usb gadget: android_usb ready
    [    0.791843] sunxikbd_script_init: key para not found, used default para. 
    [    0.800884] sunxi-rtc sunxi-rtc: rtc core: registered sunxi-rtc as rtc0
    [    0.808628] [VFE]cci probe start cci_sel = 0!
    [    0.813793] [VFE]cci probe end cci_sel = 0!
    [    0.818593] [VFE]cci_init end
    [    0.822038] [VFE]Welcome to Video Front End driver
    [    0.827986] [VFE]pdev->id = 0
    [    0.831435] [VFE]dev->mipi_sel = 0
    [    0.835324] [VFE]dev->vip_sel = 0
    [    0.839114] [VFE]dev->isp_sel = 0
    [    0.849164] [VFE_WARN]vfe vpu clock is null
    [    0.860599] [VFE]pdev->id = 1
    [    0.864021] [VFE]dev->mipi_sel = 1
    [    0.868014] [VFE]dev->vip_sel = 1
    [    0.871864] [VFE]dev->isp_sel = 0
    [    0.875672] [VFE]probe_work_handle start!
    [    0.880358] [VFE]..........................vfe clk open!.......................
    [    0.889010] [VFE]v4l2 subdev register input_num = 0
    [    0.894683] [VFE_WARN]vfe vpu clock is null
    [    0.899688] [VFE_ERR]vip1 request pinctrl handle for device [csi1] failed!
    [    0.907603] [VFE_ERR]get regulator csi_avdd error!
    [    0.913056] [VFE_ERR]vfe_device_regulator_get error at input_num = 0
    [    0.920482] [VFE]vfe_init end
    [    0.924426] platform reg-20-cs-dcdc2: Driver reg-20-cs-dcdc2 requests probe deferral
    [    0.933586] [VFE]V4L2 device registered as video0
    [    0.938969] [VFE]..........................vfe clk close!.......................
    [    0.947676] platform reg-20-cs-dcdc3: Driver reg-20-cs-dcdc3 requests probe deferral
    [    0.956440] [VFE]probe_work_handle end!
    [    0.960938] [VFE]probe_work_handle start!
    [    0.965515] [VFE]..........................vfe clk open!.......................
    [    0.974033] platform reg-20-cs-ldo1: Driver reg-20-cs-ldo1 requests probe deferral
    [    0.982739] platform reg-20-cs-ldo2: Driver reg-20-cs-ldo2 requests probe deferral
    [    0.991682] [VFE]v4l2 subdev register input_num = 0
    [    0.997227] [VFE]vfe sensor detect start! input_num = 0
    [    1.003274] [VFE]Find sensor name is "ov2640", i2c address is 60, type is "YUV" !
    [    1.011824] [VFE]Sub device register "ov2640" i2c_addr = 0x60 start!
    [    1.018998] [VFE_ERR]Error registering v4l2 subdevice No such device!
    [    1.026388] [VFE_ERR]vfe sensor register check error at input_num = 0
    [    1.033813] platform reg-20-cs-ldo3: Driver reg-20-cs-ldo3 requests probe deferral
    [    1.042602] platform reg-20-cs-ldo4: Driver reg-20-cs-ldo4 requests probe deferral
    [    1.051390] platform reg-20-cs-ldoio0: Driver reg-20-cs-ldoio0 requests probe deferral
    [    1.060339] sunxi_wdt_init_module: sunxi WatchDog Timer Driver v1.0
    [    1.067734] sunxi_wdt_probe: devm_ioremap return wdt_reg 0xf1c20ca0, res->start 0x01c20ca0, res->end 0x01c20cbf
    [    1.079242] [VFE]V4L2 device registered as video1
    [    1.084960] [VFE]..........................vfe clk close!.......................
    [    1.093623] sunxi_wdt_probe: initialized (g_timeout=16s, g_nowayout=0)
    [    1.101032] wdt_enable, write reg 0xf1c20cb8 val 0x00000000
    [    1.107445] wdt_set_tmout, write 0x000000b0 to mode reg 0xf1c20cb8, actual timeout 16 sec
    [    1.116779] [VFE]probe_work_handle end!
    [    1.127839] sunxi_leds_fetch_sysconfig_para leds is not used in config
    [    1.135343] =========script_get_err============
    [    1.140895] usbcore: registered new interface driver usbhid
    [    1.147192] usbhid: USB HID core driver
    [    1.152295] ashmem: initialized
    [    1.156010] logger: created 256K log 'log_main'
    [    1.161344] logger: created 32K log 'log_events'
    [    1.166840] logger: created 32K log 'log_radio'
    [    1.173330] logger: created 32K log 'log_system'
    [    1.181135] *******************Try sdio*******************
    [    1.188578] script_get_item return type err, consider it no ldo
    [    1.196448] asoc: sndcodec <-> sunxi-codec mapping ok
    [    1.203087] *******************Try sd *******************
    [    1.210630] TCP: cubic registered
    [    1.214424] NET: Registered protocol family 17
    [    1.219580] VFP support v0.3: implementor 41 architecture 2 part 30 variant 7 rev 5
    [    1.228464] ThumbEE CPU extension supported.
    [    1.233373] Registering SWP/SWPB emulation handler
    [    1.243467] platform reg-20-cs-ldoio0: Driver reg-20-cs-ldoio0 requests probe deferral
    [    1.252523] platform reg-20-cs-ldo4: Driver reg-20-cs-ldo4 requests probe deferral
    [    1.261210] platform reg-20-cs-ldo3: Driver reg-20-cs-ldo3 requests probe deferral
    [    1.269839] platform reg-20-cs-ldo2: Driver reg-20-cs-ldo2 requests probe deferral
    [    1.278387] platform reg-20-cs-ldo1: Driver reg-20-cs-ldo1 requests probe deferral
    [    1.287040] platform reg-20-cs-dcdc3: Driver reg-20-cs-dcdc3 requests probe deferral
    [    1.295877] platform reg-20-cs-dcdc2: Driver reg-20-cs-dcdc2 requests probe deferral
    [    1.304676] sunxi-rtc sunxi-rtc: setting system clock to 1970-01-01 00:52:23 UTC (3143)
    [    1.315547] ALSA device list:
    [    1.318966]   #0: audiocodec
    [    1.322763] Waiting for root device /dev/mmcblk0p2...
    [    1.330265] mmc0: new high speed SDHC card at address 0007
    [    1.336986] mmcblk0: mmc0:0007 SD16G 14.4 GiB 
    [    1.344244]  mmcblk0: p1 p2
    [    1.348240] mmcblk mmc0:0007: Card claimed for testing.
    [    1.354284] mmc0:0007: SD16G 14.4 GiB 
    [    1.358650] platform reg-20-cs-dcdc2: Driver reg-20-cs-dcdc2 requests probe deferral
    [    1.367505] *******************sd init ok*******************
    [    1.373971] platform reg-20-cs-dcdc3: Driver reg-20-cs-dcdc3 requests probe deferral
    [    1.382857] platform reg-20-cs-ldo1: Driver reg-20-cs-ldo1 requests probe deferral
    [    1.392791] platform reg-20-cs-ldo2: Driver reg-20-cs-ldo2 requests probe deferral
    [    1.401342] platform reg-20-cs-ldo3: Driver reg-20-cs-ldo3 requests probe deferral
    [    1.409966] platform reg-20-cs-ldo4: Driver reg-20-cs-ldo4 requests probe deferral
    [    1.418782] platform reg-20-cs-ldoio0: Driver reg-20-cs-ldoio0 requests probe deferral
    [    1.430110] fs_names=/dev/root
    [    1.433712] fs_name=ext3
    [    1.439951] EXT4-fs (mmcblk0p2): couldn't mount as ext3 due to feature incompatibilities
    [    1.451442] err=-22
    [    1.453911] fs_name=ext2
    [    1.456821] *******************Try sdio*******************
    [    1.465105] EXT4-fs (mmcblk0p2): couldn't mount as ext2 due to feature incompatibilities
    [    1.474453] err=-22
    [    1.476890] fs_name=ext4
    [    1.489053] mmc1: new high speed SDIO card at address 0001
    [    1.495719] *******************sdio init ok*******************
    [    2.726144] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
    [    2.735371] VFS: Mounted root (ext4 filesystem) on device 179:2.
    [    2.742251] err=0
    [    2.747567] devtmpfs: mounted
    [    2.751204] Freeing init memory: 140K
    [    2.930884] systemd[1]: systemd 215 running in system mode. (+PAM +AUDIT +SELINUX +IMA +SYSVINIT +LIBCRYPTSETUP +GCRYPT +ACL +XZ -SECCOMP -APPARMOR)
    [    2.946338] systemd[1]: Detected architecture 'arm'.

    Welcome to Debian GNU/Linux 8 (jessie)!

    [    3.001376] systemd[1]: Failed to insert module 'autofs4'
    [    3.007740] systemd[1]: Failed to insert module 'ipv6'
    [    3.016049] systemd[1]: Set hostname to <LicheePi>.
    [    3.386763] systemd[1]: Cannot add dependency job for unit dbus.socket, ignoring: Unit dbus.socket failed to load: No such file or directory.
    [    3.401457] systemd[1]: Cannot add dependency job for unit display-manager.service, ignoring: Unit display-manager.service failed to load: No such file or directory.
    [    3.420884] systemd[1]: Expecting device dev-ttyS0.device...
            Expecting device dev-ttyS0.device...
    [    3.450242] systemd[1]: Starting Forward Password Requests to Wall Directory Watch.
    [    3.459321] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
    [    3.468062] systemd[1]: Starting Remote File Systems (Pre).
    [  OK  ] Reached target Remote File Systems (Pre).
    [    3.490182] systemd[1]: Reached target Remote File Systems (Pre).
    [    3.497335] systemd[1]: Starting Dispatch Password Requests to Console Directory Watch.
    [    3.506789] systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
    [    3.515820] systemd[1]: Starting Paths.
    [  OK  ] Reached target Paths.
    [    3.540183] systemd[1]: Reached target Paths.
    [    3.545244] systemd[1]: Starting Encrypted Volumes.
    [  OK  ] Reached target Encrypted Volumes.
    [    3.570180] systemd[1]: Reached target Encrypted Volumes.
    [    3.576595] systemd[1]: Set up automount Arbitrary Executable File Formats File System Automount Point.
    [    3.587363] systemd[1]: Starting Swap.
    [  OK  ] Reached target Swap.
    [    3.610166] systemd[1]: Reached target Swap.
    [    3.615133] systemd[1]: Expecting device dev-mmcblk0p1.device...
            Expecting device dev-mmcblk0p1.device...
    [    3.640202] systemd[1]: Starting Root Slice.
    [  OK  ] Created slice Root Slice.
    [    3.660178] systemd[1]: Created slice Root Slice.
    [    3.665716] systemd[1]: Starting /dev/initctl Compatibility Named Pipe.
    [  OK  ] Listening on /dev/initctl Compatibility Named Pipe.
    [    3.690188] systemd[1]: Listening on /dev/initctl Compatibility Named Pipe.
    [    3.698235] systemd[1]: Starting Delayed Shutdown Socket.
    [  OK  ] Listening on Delayed Shutdown Socket.
    [    3.720181] systemd[1]: Listening on Delayed Shutdown Socket.
    [    3.726873] systemd[1]: Starting Journal Socket (/dev/log).
    [  OK  ] Listening on Journal Socket (/dev/log).
    [    3.750183] systemd[1]: Listening on Journal Socket (/dev/log).
    [    3.757124] systemd[1]: Starting udev Control Socket.
    [  OK  ] Listening on udev Control Socket.
    [    3.780183] systemd[1]: Listening on udev Control Socket.
    [    3.786538] systemd[1]: Starting udev Kernel Socket.
    [  OK  ] Listening on udev Kernel Socket.
    [    3.810188] systemd[1]: Listening on udev Kernel Socket.
    [    3.816409] systemd[1]: Starting User and Session Slice.
    [  OK  ] Created slice User and Session Slice.
    [    3.840194] systemd[1]: Created slice User and Session Slice.
    [    3.846923] systemd[1]: Starting Journal Socket.
    [  OK  ] Listening on Journal Socket.
    [    3.870194] systemd[1]: Listening on Journal Socket.
    [    3.876115] systemd[1]: Starting Sockets.
    [  OK  ] Reached target Sockets.
    [    3.900178] systemd[1]: Reached target Sockets.
    [    3.905463] systemd[1]: Starting System Slice.
    [  OK  ] Created slice System Slice.
    [    3.930189] systemd[1]: Created slice System Slice.
    [    3.935980] systemd[1]: Started Create list of required static device nodes for the current kernel.
    [    3.946850] systemd[1]: Mounting Debug File System...
            Mounting Debug File System...
    [    3.972002] systemd[1]: Mounted POSIX Message Queue File System.
    [    3.985664] systemd[1]: Starting Load Kernel Modules...
            Starting Load Kernel Modules...
    [    4.016065] systemd[1]: Started Set Up Additional Binary Formats.
    [    4.024319] systemd[1]: Mounted Huge Pages File System.
    [    4.036274] systemd[1]: Starting udev Coldplug all Devices...
            Starting udev Coldplug all Devices...
    [    4.062631] systemd[1]: Starting Create Static Device Nodes in /dev...
            Starting Create Static Device Nodes in /dev...
    [    4.092537] systemd[1]: Starting system-getty.slice.
    [  OK  ] Created slice system-getty.slice.
    [    4.112748] systemd[1]: Created slice system-getty.slice.
    [    4.122317] systemd[1]: Starting system-serial\x2dgetty.slice.
    [  OK  ] Created slice system-serial\x2dgetty.slice.
    [    4.150268] systemd[1]: Created slice system-serial\x2dgetty.slice.
    [    4.157615] systemd[1]: Started File System Check on Root Device.
    [    4.164807] systemd[1]: Starting Journal Service...
            Starting Journal Service...
    [  OK  ] Started Journal Service.
    [    4.210299] systemd[1]: Started Journal Service.
    [  OK  ] Reached target Slices.
    [  OK  ] Mounted Debug File System.
    [  OK  ] Started Load Kernel Modules.
    [  OK  ] Started Create Static Device Nodes in /dev.
            Starting udev Kernel Device Manager...
            Starting Apply Kernel Variables...
    [  OK  ] Started udev Kernel Device Man[    4.372555] systemd-udevd[69]: starting version 215
    ager.
    [  OK  ] Started udev Coldplug all Devices.
    [  OK  ] Started Apply Kernel Variables.
            Starting Copy rules generated while the root was ro...
            Starting LSB: Set preliminary keymap...
    [  OK  ] Started Copy rules generated while the root was ro.
    [  OK  ] Started LSB: Set preliminary keymap.
            Starting Remount Root and Kernel File Systems...
    [    4.640531] EXT4-fs (mmcblk0p2): re-mounted. Opts: (null)
    [  OK  ] Started Remount Root and Kernel File Systems.
    [  OK  ] Reached target Local File Systems (Pre).
            Starting Load/Save Random Seed...
    [  OK  ] Reached target Sound Card.
    [  OK  ] Started Load/Save Random Seed.
    [    5.012110] [VFE]vfe_open
    [  OK  [    5.043465] [VFE]vfe_open
    ] Found device /dev/mmcblk0p1.
    [    5.058511] [VFE]..........................vfe clk open!.......................
    [    5.082179] [VFE]..........................vfe clk open!.......................
    [  OK  ] Found device /dev/ttyS0.
    [    5.112320] [VFE]vfe_open ok
    [    5.115853] [VFE]vfe_close
    [    5.118958] [VFE]vfe select input flag = 0, s_input have not be used .
    [    5.126480] [VFE]..........................vfe clk close!.......................
    [    5.144821] [VFE]vfe_open ok
    [    5.148348] [VFE]vfe_close
    [    5.151598] [VFE]vfe select input flag = 0, s_input have not be used .
    [    5.158972] [VFE]..........................vfe clk close!.......................
            Mounting /boot...
    [    5.224773] [VFE]vfe_close end
    [    5.282919] [VFE]vfe_close end
    [  OK  ] Mounted /boot.
    [  OK  ] Reached target Local File Systems.
            Starting Create Volatile Files and Directories...
    [  OK  ] Reached target Remote File Systems.
            Starting Trigger Flushing of Journal to Persistent Storage...
            Starting LSB: Set console font and keymap...
            Starting LSB: Raise network interfaces....
    [  OK  ] Started LSB: Set console font and keymap.
    [    5.519209] systemd-journald[65]: Received request to flush runtime journal from PID 1
    [  OK  ] Started Trigger Flushing of Journal to Persistent Storage.
    [  OK  ] Started Create Volatile Files and Directories.
            Starting Update UTMP about System Boot/Shutdown...
    [  OK  ] Started Update UTMP about System Boot/Shutdown.
    [  OK  ] Started LSB: Raise network interfaces..
    [  OK  ] Reached target Network.
    [  OK  ] Reached target System Initialization.
    [  OK  ] Reached target Timers.
            Starting Restore Sound Card State...
    [  OK  ] Reached target Basic System.
            Starting Regular background program processing daemon...
    [  OK  ] Started Regular background program processing daemon.
            Starting OpenBSD Secure Shell server...
    [  OK  ] Started OpenBSD Secure Shell server.
            Starting /etc/rc.local Compatibility...
            Starting Permit User Sessions...
            Starting getty on tty2-tty6 if dbus and logind are not available...
    [  OK  ] Started Restore Sound Card State.
    [  OK  ] Started /etc/rc.local Compatibility.
    [  OK  ] Started Permit User Sessions.
            Starting Getty on tty2...
    [  OK  ] Started Getty on tty2.
            Starting Getty on tty1...
    [  OK  ] Started Getty on tty1.
            Starting Serial Getty on ttyS0...
    [  OK  ] Started Serial Getty on ttyS0.
    [  OK  ] Started getty on tty2-tty6 if dbus and logind are not available.
            Starting Getty on tty6...
    [  OK  ] Started Getty on tty6.
            Starting Getty on tty5...
    [  OK  ] Started Getty on tty5.
            Starting Getty on tty4...
    [  OK  ] Started Getty on tty4.
            Starting Getty on tty3...
    [  OK  ] Started Getty on tty3.
    [  OK  ] Reached target Login Prompts.
    [  OK  ] Reached target Multi-User System.
    [  OK  ] Reached target Graphical Interface.
            Starting Update UTMP about System Runlevel Changes...
    [  OK  ] Started Update UTMP about System Runlevel Changes.

    Debian GNU/Linux 8 LicheePi ttyS0

    LicheePi login: root
