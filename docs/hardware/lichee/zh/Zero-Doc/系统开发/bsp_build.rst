BSP源码下载与编译
===================================

.. contents:: 本文目录

BSP内核剥离
-----------------------------------

BSP内核对摄像头驱动支持较好，所以在摄像头应用中有必要使用BSP内核。

官方SDK中camdriod与lichee linux内核绑定，而camdriod比较庞大，所以我们只需抽取lichee linux内核，而抛弃camdriod代码。

单独使用lichee linux的方法是：（构建走读见后一节）

解压 *buildroot/dl/gcc-linarno.tar.gz* 到 *lichee/out/sun8iw8p1/linux/common/buildroot/external-toolchain*，并加入环境变量（这步其实在下一步里包含了）

执行 *build_tiger-cdr.sh*

执行过程中会生成内核文件：

:: 

   Image Name:   Linux-3.4.39
   Created:      Tue Sep  5 06:55:03 2017
   Image Type:   ARM Linux Kernel Image (uncompressed)
   Data Size:    2275400 Bytes = 2222.07 kB = 2.17 MB
   Load Address: 40008000
   Entry Point:  40008000
     Image arch/arm/boot/uImage is ready
   'arch/arm/boot/Image' -> 'output/bImage'
   'arch/arm/boot/uImage' -> 'output/uImage'
   'arch/arm/boot/zImage' -> 'output/zImage'
   Building modules
   
   compile Kernel successful

从主线uboot启动内核，一般使用uImage。

BSP内核配置
-----------------------------------

BSP内核源码在lichee/linux-3.4下。

通过 ``make ARCH=arm menuconfig`` 来配置内核。

我们可以使能摄像头需要修改的一些内核配置：

.. code-block:: sh
   :caption: 使能USB摄像头驱动：

   -> Device Drivers                     
     x       -> Multimedia support (MEDIA_SUPPORT [=y])                                                            
     x         -> Video capture adapters (VIDEO_CAPTURE_DRIVERS [=y])                                     
     x           -> V4L USB devices (V4L_USB_DRIVERS [=y])  
     x				-><M>   USB Video Class (UVC)  CONFIG_USB_VIDEO_CLASS

.. code-block:: sh
   :caption: 使能DVP/MIPI摄像头

   -> Device Drivers                                                                  
     x       -> Multimedia support (MEDIA_SUPPORT [=y])                                                            
     x         -> Video capture adapters (VIDEO_CAPTURE_DRIVERS [=y])                                    
     x           -> V4L platform devices (V4L_PLATFORM_DRIVERS [=y])                                   
     x             -> SoC camera support (SOC_CAMERA [=y]) 
     x x                          <M>     ov2640 camera support                                                               
     x x                          <M>     ov5647 camera support
     x x                          <M>   sunxi video front end (camera and etc)driver                            
     x x                          <M>     v4l2 driver for SUNXI
      <*>   sunxi video encoder and decoder support 

由于camdriod原始的内核配置是为了在spi nor flash上运行而配置的，没有ext4支持，所以需要额外添加ext4支持：
   
.. code-block:: sh

   <*> The Extended 4 (ext4) filesystem                                                            
     x x                          [*]   Use ext4 for ext2/ext3 file systems (NEW)                                         
     x x                          [*]   Ext4 extended attributes (NEW)                                                         
     x x                          [ ]     Ext4 POSIX Access Control Lists (NEW)                                             
     x x                          [ ]     Ext4 Security Labels (NEW)                                                              
     x x                          [ ]   EXT4 debugging support (NEW)                                                         
     x x                          [ ] JBD2 (ext4) debugging support (NEW) 

另外还要加上CONFIG_LBDAF（大文件支持，否则无法挂载文件系统）

.. code-block:: sh

   -> Enable the block layer (BLOCK [=y])  
   [*]   Support for large (2TB+) block devices and files

再加上CGROUPS支持：

.. code-block:: sh

   -> General setup
    [*] Control Group support  ---> 

如果在文件系统（如debian）中使用了SWAP等特性，则还需要在内核中开启SWAP。

debian下还需要开启 FHANDLE 特性，否则会出现以下错误

:: 

   A start job is running for dev-ttyS0.device
   timeout

如果需要使用wifi功能，则还需要勾选RTL8723BS的支持（注意需要选择模块方式），和AW_RF_PM选项。

以及下节所说的fex修改。

uboot启动BSP内核
-----------------------------------

使用主线uboot启动BSP内核，需要修改下启动脚本，放入BSP内核需要的 *script.bin* 配置文件（相当于主线linux的dtb）

.. code-block:: sh
   :caption: 修改boot.cmd:

   setenv bootargs console=ttyS0,115200 panic=5 rootwait root=/dev/mmcblk0p2 earlyprintk rw
   setenv bootm_boot_mode sec
   setenv machid 1029
   load mmc 0:1 0x41000000 uImage
   load mmc 0:1 0x41d00000 script.bin
   bootm 0x41000000

重新生成boot.scr:
   
   ``mkimage -C none -A arm -T script -d boot.cmd boot.scr``

将boot.scr放入第一分区。

再配置生成script.bin.

复制一份 *lichee/tools/pack/chips/sun8iw8p1/configs/tiger-cdr/sys_config.fex*

修改其中的摄像头配置：

首先修改SD卡检测策略，设置为不检测，默认插入

  ``sdc_detmode=3``

使能RTL8723bs无线网卡的话，需要使能mmc1，也设置为不检测sd卡。

在设置摄像头型号，csi0是mipi摄像头，csi1是dvp摄像头。

这里默认以mipi摄像头为ov5647, dvp摄像头为ov2640 为例。

.. code-block:: dts

   ;--------------------------------------------------------------------------------
   ;vip (video input port) configuration
   ;vip_used: 0:disable 1:enable
   ;vip_mode: 0:sample one interface to one buffer 1:sample two interface to one buffer
   ;vip_dev_qty: The quantity of devices linked to capture bus
   ;
   ;vip_define_sensor_list: If you want use sensor detect function, please set vip_define_sensor_list = 1, and
   ;                                    verify that file /system/etc/hawkview/sensor_list_cfg.ini is properly configured!
   ;
   ;vip_dev(x)_pos: sensor position, "rear" or "front", if vip_define_sensor_list = 1,vip_dev(x)_pos must be configured!
   ;
   ;vip_dev(x)_isp_used 0:not use isp 1:use isp
   ;vip_dev(x)_fmt: 0:yuv 1:bayer raw rgb
   ;vip_dev(x)_stby_mode: 0:not shut down power at standby 1:shut down power at standby
   ;vip_dev(x)_vflip: flip in vertical direction 0:disable 1:enable
   ;vip_dev(x)_hflip: flip in horizontal direction 0:disable 1:enable
   ;vip_dev(x)_iovdd: camera module io power handle string, pmu power supply
   ;vip_dev(x)_iovdd_vol: camera module io power voltage, pmu power supply
   ;vip_dev(x)_avdd: camera module analog power handle string, pmu power supply
   ;vip_dev(x)_avdd_vol: camera module analog power voltage, pmu power supply
   ;vip_dev(x)_dvdd: camera module core power handle string, pmu power supply
   ;vip_dev(x)_dvdd_vol: camera module core power voltage, pmu power supply
   ;vip_dev(x)_afvdd: camera module vcm power handle string, pmu power supply
   ;vip_dev(x)_afvdd_vol: camera module vcm power voltage, pmu power supply
   ;x indicates the index of the devices which are linked to the same capture bus
   ;fill voltage in uV, e.g. iovdd = 2.8V, vip_devx_iovdd_vol = 2800000
   ;fill handle string as below:
   ;axp22_eldo3
   ;axp22_dldo4
   ;axp22_eldo2
   ;fill handle string "" when not using any pmu power supply
   ;--------------------------------------------------------------------------------
   
   [csi0]
   vip_used                 = 1
   vip_mode                 = 0
   vip_dev_qty              = 1
   vip_define_sensor_list   = 0
   vip_csi_mck              = port:PE20<3><default><default><default>
   vip_csi_sck              = port:PE21<2><default><default><default>
   vip_csi_sda              = port:PE22<2><default><default><default>
   vip_dev0_mname           = "h22_mipi"
   vip_dev0_pos             = "rear"
   vip_dev0_lane            = 1
   vip_dev0_twi_id          = 0
   vip_dev0_twi_addr        = 0x60
   vip_dev0_isp_used        = 1
   vip_dev0_fmt             = 1
   vip_dev0_stby_mode       = 0
   vip_dev0_vflip           = 0
   vip_dev0_hflip           = 0
   vip_dev0_iovdd           = ""
   vip_dev0_iovdd_vol       = 3000000
   vip_dev0_avdd            = "csi-avdd"
   vip_dev0_avdd_vol        = 3000000
   vip_dev0_dvdd            = "csi-dvdd"
   vip_dev0_dvdd_vol        = 3000000
   vip_dev0_afvdd           = ""
   vip_dev0_afvdd_vol       = 2800000
   vip_dev0_power_en        =
   vip_dev0_reset           = port:PG00<1><default><default><default>
   vip_dev0_pwdn            = port:PG01<1><default><default><default>
   vip_dev0_flash_en        =
   vip_dev0_flash_mode      =
   vip_dev0_af_pwdn         =
   vip_dev0_act_used        = 0
   vip_dev0_act_name        = "dw9714_act"
   vip_dev0_act_slave       = 0x18
   vip_dev1_mname           = ""
   vip_dev1_pos                 = "front"
   vip_dev1_lane            = 1
   vip_dev1_twi_id          = 0
   vip_dev1_twi_addr        =
   vip_dev1_isp_used        = 0
   vip_dev1_fmt             = 1
   vip_dev1_stby_mode       = 0
   vip_dev1_vflip           = 0
   vip_dev1_hflip           = 0
   vip_dev1_iovdd           = ""
   vip_dev1_iovdd_vol       = 2800000
   vip_dev1_avdd            = ""
   vip_dev1_avdd_vol        = 2800000
   vip_dev1_dvdd            = ""
   vip_dev1_dvdd_vol        = 1500000
   vip_dev1_afvdd           = ""
   vip_dev1_afvdd_vol       = 2800000
   vip_dev1_power_en        =
   vip_dev1_reset           =
   vip_dev1_pwdn            =
   vip_dev1_flash_en        =
   ;fill handle string as below:
   ;axp22_eldo3
   ;axp22_dldo4
   ;axp22_eldo2
   ;fill handle string "" when not using any pmu power supply
   ;--------------------------------------------------------------------------------
   
   [csi0]
   
   vip_used                 = 1
   vip_mode                 = 0
   vip_dev_qty              = 1
   vip_define_sensor_list   = 0
   vip_csi_mck              = port:PE20<3><default><default><default>
   vip_csi_sck              = port:PE21<2><default><default><default>
   vip_csi_sda              = port:PE22<2><default><default><default>
   vip_dev0_mname           = "h22_mipi"
   vip_dev0_pos             = "rear"
   vip_dev0_lane            = 1
   vip_dev0_twi_id          = 0
   vip_dev0_twi_addr        = 0x60
   vip_dev0_isp_used        = 1
   vip_dev0_fmt             = 1
   vip_dev0_stby_mode       = 0
   vip_dev0_vflip           = 0
   vip_dev0_hflip           = 0
   vip_dev0_iovdd           = ""
   vip_dev0_iovdd_vol       = 3000000
   vip_dev0_avdd            = "csi-avdd"
   vip_dev0_avdd_vol        = 3000000
   vip_dev0_dvdd            = "csi-dvdd"
   vip_dev0_dvdd_vol        = 3000000
   vip_dev0_afvdd           = ""
   vip_dev0_afvdd_vol       = 2800000
   vip_dev0_power_en        =
   vip_dev0_reset           = port:PG00<1><default><default><default>
   vip_dev0_pwdn            = port:PG01<1><default><default><default>
   vip_dev0_flash_en        =
   vip_dev0_flash_mode      =
   vip_dev0_af_pwdn         =
   vip_dev0_act_used        = 0
   vip_dev0_act_name        = "dw9714_act"
   vip_dev0_act_slave       = 0x18
   vip_dev1_mname           = ""
   vip_dev1_pos                 = "front"
   vip_dev1_lane            = 1
   vip_dev1_twi_id          = 0
   vip_dev1_twi_addr        =
   vip_dev1_isp_used        = 0
   vip_dev1_fmt             = 1
   vip_dev1_stby_mode       = 0
   vip_dev1_vflip           = 0
   vip_dev1_hflip           = 0
   vip_dev1_iovdd           = ""
   vip_dev1_iovdd_vol       = 2800000
   vip_dev1_avdd            = ""
   vip_dev1_avdd_vol        = 2800000
   vip_dev1_dvdd            = ""
   vip_dev1_dvdd_vol        = 1500000
   vip_dev1_afvdd           = ""
   vip_dev1_afvdd_vol       = 2800000
   vip_dev1_power_en        =
   vip_dev1_reset           =
   vip_dev1_pwdn            =
   vip_dev1_flash_en        =
   vip_dev1_flash_mode      =
   vip_dev1_af_pwdn         =
   
   [csi1]
   vip_used                 = 0
   vip_mode                 = 0
   vip_dev_qty              = 1
   vip_define_sensor_list   = 0
   vip_csi_pck              = port:PE00<2><default><default><default>
   vip_csi_mck              = port:PE01<2><default><default><default>
   vip_csi_hsync            = port:PE02<2><default><default><default>
   vip_csi_vsync            = port:PE03<2><default><default><default>
   vip_csi_d0               = port:PE04<2><default><default><default>
   vip_csi_d1               = port:PE05<2><default><default><default>
   vip_csi_d2               = port:PE06<2><default><default><default>
   vip_csi_d3               = port:PE07<2><default><default><default>
   vip_csi_d4               = port:PE08<2><default><default><default>
   vip_csi_d5               = port:PE09<2><default><default><default>
   vip_csi_d6               = port:PE10<2><default><default><default>
   vip_csi_d7               = port:PE11<2><default><default><default>
   vip_csi_d8               = port:PE12<2><default><default><default>
   ;vip_csi_d9               = port:PE13<2><default><default><default>
   vip_csi_d10               = port:PE14<2><default><default><default>
   vip_csi_d11               = port:PE15<2><default><default><default>
   
   vip_csi_sck               = port:PE21<2><default><default><default>
   vip_csi_sda               = port:PE22<2><default><default><default>
   
   vip_dev0_mname           = "ov5640"
   vip_dev0_pos             = "front"
   vip_dev0_twi_id          = 4
   vip_dev0_twi_addr        = 0x78
   vip_dev0_isp_used        = 0
   vip_dev0_fmt             = 0
   vip_dev0_stby_mode       = 0
   vip_dev0_vflip           = 0
   vip_dev0_hflip           = 0
   vip_dev0_iovdd           = ""
   vip_dev0_iovdd_vol       = 2800000
   vip_dev0_avdd            = ""
   vip_dev0_avdd_vol        = 2800000
   vip_dev0_dvdd            = ""
   vip_dev0_dvdd_vol        = 1500000
   vip_dev0_afvdd           = ""
   vip_dev0_afvdd_vol       = 2800000
   vip_dev0_power_en        =
   vip_dev0_reset           = port:PE23<1><default><default><default>
   vip_dev0_pwdn            = port:PE24<1><default><default><default>
   vip_dev0_flash_en        =
   vip_dev0_flash_mode      =
   vip_dev0_af_pwdn         =
   
   vip_dev0_act_used        = 0
   vip_dev0_act_name        = "ad5820_act"
   vip_dev0_act_slave       = 0x18
   
   vip_dev1_mname           = "gc2035"
   vip_dev1_pos                 = "front"
   vip_dev1_lane            = 1
   vip_dev1_twi_id          = 4
   vip_dev1_twi_addr        = 0x78
   vip_dev1_isp_used        = 0
   vip_dev1_fmt             = 1
   vip_dev1_stby_mode       = 0
   vip_dev1_vflip           = 0
   vip_dev1_hflip           = 0
   vip_dev1_iovdd           = ""
   vip_dev1_iovdd_vol       = 2800000
   vip_dev1_avdd            = ""
   vip_dev1_avdd_vol        = 2800000
   vip_dev1_dvdd            = ""
   vip_dev1_dvdd_vol        = 1500000
   vip_dev1_afvdd           = ""
   vip_dev1_afvdd_vol       = 2800000
   vip_dev1_power_en        =
   vip_dev1_reset           =
   vip_dev1_pwdn            =
   vip_dev1_flash_en        =
   vip_dev1_flash_mode      =
   vip_dev1_af_pwdn         =

| 将其中的摄像头信息改成自己使用的摄像头信息。
| 保存，并使用 ``fex2bin sys_config.fex script.bin`` 生成script.bin文件。

   将script.bin也放入第一分区。

| 再将前面编译的uImage放入第一分区。

   此时就可以使用主线Uboot启动bsp内核了。
