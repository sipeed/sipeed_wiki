BSP内核的摄像头使用
===================================

.. contents:: 本文目录

:: 

    Device Drivers -> 
     <*> Multimedia support  --->        
      <*>   sunxi video encoder and decoder support 	//视频编码器，包括h264/mpeg4/mpeg2/vc1/rmvb.  以模块形式编译，cedar_ve.ko

::

   [*]   Video capture adapters  --->  
   [*]   V4L platform devices  --->  

:: 

    --- V4L platform devices                                                                        
    < >   Support for timberdale Video In/LogiWIN                                                   
    <*>   SoC camera support                                                                        
    < >     imx074 support                                                                          
    < >     mt9m001 support                                                                         
    < >     mt9m111, mt9m112 and mt9m131 support                                                    
    < >     mt9t031 support                                                                         
    < >     mt9t112 support                                                                         
    < >     mt9v022 support                                                                         
    < >     rj54n1cb0c support                                                                      
    < >     tw9910 support                                                                          
    < >     platform camera support                                                                 
    <M>     ov2640 camera support                                                                   
    <M>     ov5642 camera support                                                                   
    < >     ov6650 sensor support                                                                   
    < >     ov772x camera support                                                                   
    < >     ov9640 camera support                                                                   
    < >     ov9740 camera support                                                                   
    < >   SuperH Mobile MIPI CSI-2 Interface driver                                                 
    < >   SuperH Mobile CEU Interface driver                                                        
    <*>   sunxi video front end (camera and etc)driver                                              
    <*>     v4l2 driver for SUNXI                                                                   
    Sensor CSI  ---> 

.. code-block:: bash

    < > ov2710_mipi                                                                                 
    < > ov4689                                                                                      
    < > ov4689 60fps                                                                                
    < > ar0330 mipi                                                                                 
    < > ov4689 sdv                                                                                  
    < > gc1004_mipi                                                                                 
    <M> h22_mipi                                                                                    
    < > nt99231_mipi

查看编译后的ko：

.. code-block:: python

    //触摸屏
    aw5306_ts.ko
    gt818_ts.ko
    gt82x.ko
    gt911_ts.ko
    ft5x_ts.ko
    gslX680.ko
    gslX680new.ko
    icn83xx_ts.ko
    gt9xx_ts.ko
    gt9xxf_ts.ko
    tu_ts.ko

    //杂项
    da380.ko	//加速度传感器
    fatfs.ko	//文件系统
    scsi_wait_scan.ko
    sw-device.ko	//Linux kernel modules for  Detection i2c device.
    uvcvideo.ko		//UVC摄像头

    //普通摄像头驱动  media/video/
    ov2640.ko
    ov5642.ko

    //V4L2
    videobuf-core.ko
    videobuf-dma-contig.ko
    videobuf2-core.ko
    videobuf2-memops.ko
    videobuf2-vmalloc.ko

    //VFE
    vfe_v4l2.ko			//media/video/sunxi-vfe
    vfe_os.ko
    vfe_subdev.ko
    cci.ko		//摄像头控制接口，sunxi-vfe/csi_cci
    h22_mipi.ko	   //media/video/sunxi-vfe/device/h22_mipi.ko

    //cedar  视频编码
    cedar_ve.ko   //media/cedar-ve/cedar_ve.ko

实际可以使用的是 *media/video/sunxi-vfe/* 下的摄像头驱动

::

    platform_cfg.h  
    bsp_common.c         
    config.c        
    config.h  
    vfe.c
    vfe.h
    vfe_os.c
    vfe_os.h
    vfe_os.ko
    vfe_subdev.c
    vfe_subdev.h
    vfe_subdev.ko
    vfe_v4l2.ko   
    //调焦器
    actuator        
    //摄像头控制器接口驱动
    csi             
    csi_cci      
    mipi_csi 
    //闪光灯
    flash_light
    //ISP相关
    isp_cfg  
    lib     //isp库
    platform	//不同主控芯片的配置
    //测试，功能
    test
    utility
    //支持的传感器
    device          
    
支持的传感器

:: 

    Makefile       gc0312.c       gc5004.c        hi257.c          nt99252.c       ov5640.c        s5k3h7.c       sp2518.c
    ar0330.c       gc0328.c       gc5004_mipi.c   hm5040.c         ov12830.c       ov5640_mipi.c   s5k4e1.c       sp2519.c
    ar0330_mipi.c  gc0328c.c      gs5604.c        hm5065.c         ov13850.c       ov5647.c        s5k4e1_mipi.c  sp5408.c
    bf3a03.c       gc0329.c       gt2005.c        hm8030.c         ov16825.c       ov5647_mipi.c   s5k4ec.c       sp5409.c
    built-in.o     gc1004_mipi.c  h22_mipi.c      hm8131.c         ov2640.c        ov5648.c        s5k4ec_mipi.c  t4k05.c
    camera.h       gc2035.c       h22_mipi.ko     imx179.c         ov2686.c        ov5650.c        s5k5e2ya.c     t8et5.c
    camera_cfg.h   gc2145.c       h22_mipi.mod.c  imx214.c         ov2710.c        ov7736.c        s5k5e2yx.c     tc358743.c
    gc0307.c       gc2155.c       h22_mipi.mod.o  imx219.c         ov2710_mipi.c   ov8825.c        siv121d.c
    gc0308.c       gc2235.c       h22_mipi.o      modules.builtin  ov4689.c        ov8850.c        sp0718.c
    gc0309.c       gc2355.c       h42_mipi.c      modules.order    ov4689_60fps.c  ov8858.c        sp0838.c
    gc0311.c       gc2355_mipi.c  hi253.c         nt99231_mipi.c   ov4689_sdv.c    ov8858_4lane.c  sp2508.c

可见zero配套的ov2640和ov5647都在其中。

但是他们不在menuconfig中，所以在上层的Kconfig中加入：

.. code-block:: bash

    config OV2640
            tristate "ov2640"
            default n
    config OV5647_MIPI
            tristate "ov5647_mipi"
            default n

在本层的Makefile中加入：

.. code-block:: sh

    obj-$(CONFIG_OV2640)            += ov2640.o
    obj-$(CONFIG_OV5647_MIPI)       += ov5647_mipi.o

重新在menuconfig中勾选，编译，即可得到：

:: 

   LD [M]  drivers/media/video/sunxi-vfe/device/ov2640.ko
   LD [M]  drivers/media/video/sunxi-vfe/device/ov5647_mipi.ko

将ko文件放入系统中，手动加载，然后使用fswebcam尝试拍照：

.. code-block:: sh

    root@LicheePi:~# fswebcam -d /dev/video0 --no-banner -r 320x240 capture.jpg
    [  255.199106] [VFE]vfe_open
    --- Opening /dev/video0...
    [  255.202406] [VFE]..........................vfe clk open!.......................
    Trying source module v4l2...[  255.213786] [VFE]vfe_open ok

    [  255.219628] [VFE_ERR]input index(0) > dev->dev_qty(1)-1 invalid!, device_valid_flag[0] = 0
    /dev/video0 opened.
    255.229491] [VFE]vfe_close
    mNo input was specified, using t[  255.235232] [VFE]vfe select input flag = 0, s_input have not be used .
    he first.
    Unable to qu[  255.245365] [VFE]..........................vfe clk close!.......................
    ery input 0.
    VIDIOC_EN[  255.256556] [VFE]vfe_close end
    UMINPUT: Invalid argument

跟踪相关信息，是在vfe.c,

函数 *static int vidioc_enum_input(struct file *file, void *priv, struct v4l2_input *inp)* 中：

.. code-block:: c

    2807         if (0 == dev->device_valid_flag[inp->index]) {
    2808                 vfe_err("input index(%d) > dev->dev_qty(%d)-1 invalid!, device_valid_flag[%d] = %d\n", inp->index, dev->dev_     qty,inp->index, dev->device_valid_flag[inp->index]);
    2809                 return -EINVAL;
    2810         }

即枚举摄像头时，发现device_valid_flag标志位不对，该标志位是在：

.. code-block:: c

    static void probe_work_handle(struct work_struct *work)
    if(vfe_sensor_register_check(dev,&dev->v4l2_dev,dev->ccm_cfg[input_num],&dev->dev_sensor[input_num],input_nu     m) == NULL)
    5126                 {
    5127                         vfe_err("vfe sensor register check error at input_num = %d\n",input_num);
    5128                         dev->device_valid_flag[input_num] = 0;
    5129                         //goto snesor_register_end;
    5130                 }
    5131                 else{
    5132                         dev->device_valid_flag[input_num] = 1;
    5133                 }

这个函数是在vfe_probe中调用，也即初始化时检测的。

vfe驱动加载过程：

- csi_cci/cci_platform_drv.c 加载cci.ko
- vfe.c vfe_os.ko加载
- vfe_subdev.ko
- vfe_v4l2.ko	//media/video/sunxi-vfe

查看开机启动信息：

:: 

    //cci.ko加载，即摄像头控制器初始化
    [    0.808628] [VFE]cci probe start cci_sel = 0!
    [    0.813793] [VFE]cci probe end cci_sel = 0!
    [    0.818593] [VFE]cci_init end

    //VFE驱加载
    [    0.822038] [VFE]Welcome to Video Front End driver
    [    0.827986] [VFE]pdev->id = 0
    [    0.831435] [VFE]dev->mipi_sel = 0
    [    0.835324] [VFE]dev->vip_sel = 0
    [    0.839114] [VFE]dev->isp_sel = 0
    [    0.849164] [VFE_WARN]vfe vpu clock is null
    [    0.849164] [VFE_WARN]vfe vpu clock is null
    [    0.860599] [VFE]pdev->id = 1
    [    0.864021] [VFE]dev->mipi_sel = 1
    [    0.868014] [VFE]dev->vip_sel = 1
    [    0.871864] [VFE]dev->isp_sel = 0
    [    0.875672] [VFE]probe_work_handle start!
    [    0.880358] [VFE]..........................vfe clk open!.......................
    [    0.880358] [VFE]..........................vfe clk open!.......................
    [    0.889010] [VFE]v4l2 subdev register input_num = 0
    [    0.894683] [VFE_WARN]vfe vpu clock is null
    [    0.894683] [VFE_WARN]vfe vpu clock is null
    [    0.899688] [VFE_ERR]vip1 request pinctrl handle for device [csi1] failed!
    [    0.907603] [VFE_ERR]get regulator csi_avdd error!
    [    0.913056] [VFE_ERR]vfe_device_regulator_get error at input_num = 0
    [    0.913056] [VFE_ERR]vfe_device_regulator_get error at input_num = 0
    [    0.920482] [VFE]vfe_init end
    [    0.920482] [VFE]vfe_init end

    //V4L2设备注册，生成video0
    [    0.933586] [VFE]V4L2 device registered as video0
    [    0.938969] [VFE]..........................vfe clk close!.......................
    [    0.938969] [VFE]..........................vfe clk close!.......................
    [    0.956440] [VFE]probe_work_handle end!
    [    0.960938] [VFE]probe_work_handle start!
    [    0.965515] [VFE]..........................vfe clk open!.......................
    [    0.965515] [VFE]..........................vfe clk open!.......................
    [    0.991682] [VFE]v4l2 subdev register input_num = 0
    [    0.997227] [VFE]vfe sensor detect start! input_num = 0
    [    0.997227] [VFE]vfe sensor detect start! input_num = 0
    [    1.003274] [VFE]Find sensor name is "ov2640", i2c address is 60, type is "YUV" !
    [    1.011824] [VFE]Sub device register "ov2640" i2c_addr = 0x60 start!
    [    1.018998] [VFE_ERR]Error registering v4l2 subdevice No such device!
    [    1.026388] [VFE_ERR]vfe sensor register check error at input_num = 0
    [    1.026388] [VFE_ERR]vfe sensor register check error at input_num = 0
    [    1.079242] [VFE]V4L2 device registered as video1
    [    1.084960] [VFE]..........................vfe clk close!.......................
    [    1.084960] [VFE]..........................vfe clk close!.......................
    [    1.116779] [VFE]probe_work_handle end!
    [    5.012110] [VFE]vfe_open
    [    5.012110] [VFE]vfe_open
    [    5.043465] [VFE]vfe_open
    [    5.043465] [VFE]vfe_open
    [    5.058511] [VFE]..........................vfe clk open!.......................
    [    5.058511] [VFE]..........................vfe clk open!.......................
    [    5.082179] [VFE]..........................vfe clk open!.......................
    [    5.082179] [VFE]..........................vfe clk open!.......................
    [    5.112320] [VFE]vfe_open ok
    [    5.112320] [VFE]vfe_open ok
    [    5.115853] [VFE]vfe_close
    [    5.115853] [VFE]vfe_close
    [    5.118958] [VFE]vfe select input flag = 0, s_input have not be used .
    [    5.118958] [VFE]vfe select input flag = 0, s_input have not be used .
    [    5.126480] [VFE]..........................vfe clk close!.......................
    [    5.126480] [VFE]..........................vfe clk close!.......................
    [    5.144821] [VFE]vfe_open ok
    [    5.144821] [VFE]vfe_open ok
    [    5.148348] [VFE]vfe_close
    [    5.148348] [VFE]vfe_close
    [    5.151598] [VFE]vfe select input flag = 0, s_input have not be used .
    [    5.151598] [VFE]vfe select input flag = 0, s_input have not be used .
    [    5.158972] [VFE]..........................vfe clk close!.......................
    [    5.158972] [VFE]..........................vfe clk close!.......................
    [    5.224773] [VFE]vfe_close end
    [    5.224773] [VFE]vfe_close end
    [    5.282919] [VFE]vfe_close end
    [    5.282919] [VFE]vfe_close end

.. code-block:: cpp
   :caption: vfe_sensor_register_check

    static struct v4l2_subdev *vfe_sensor_register_check(struct vfe_dev *dev,struct v4l2_device *v4l2_dev,struct ccm_config  *ccm_cfg,
                        struct i2c_board_info *sensor_i2c_board,int input_num )
    {
        int sensor_cnt,ret, sensor_num;
        struct sensor_item sensor_info;
        if(dev->vip_define_sensor_list == 1)
        {
            sensor_num = ccm_cfg->sensor_cfg_ini->detect_sensor_num;
            if(ccm_cfg->sensor_cfg_ini->detect_sensor_num == 0)	{
                sensor_num = 1;
            }
        } else {
            sensor_num = 1;
        }
        for(sensor_cnt=0; sensor_cnt<sensor_num; sensor_cnt++)
        {
            if(dev->vip_define_sensor_list == 1)
            {
                if(ccm_cfg->sensor_cfg_ini->detect_sensor_num > 0)
                    cpy_ccm_sub_device_cfg(ccm_cfg, sensor_cnt);
            }
            if(get_sensor_info(ccm_cfg->ccm, &sensor_info) == 0)
            {
                if(ccm_cfg->i2c_addr != sensor_info.i2c_addr)
                {
                    vfe_warn("Sensor info \"%s\" i2c_addr is different from sys_config!\n", sensor_info.sensor_name );
                    //vfe_warn("Sensor info i2c_addr = %d, sys_config i2c_addr = %d!\n", sensor_info.i2c_addr, ccm_cfg->i2c_addr);
                    //ccm_cfg->i2c_addr = sensor_info.i2c_addr;
                }
                if(ccm_cfg->is_bayer_raw != sensor_info.sensor_type)
                {
                    vfe_warn("Camer detect \"%s\" fmt is different from sys_config!\n", sensor_info_type[sensor_info.sensor_type]);
                    vfe_warn("Apply detect  fmt = %d replace sys_config fmt = %d!\n", sensor_info.sensor_type, ccm_cfg->is_bayer_raw);
                    ccm_cfg->is_bayer_raw = sensor_info.sensor_type;
                }
                if(sensor_info.sensor_type == SENSOR_RAW)
                {
                    ccm_cfg->is_isp_used = 1;
                }
                else
                {
                    ccm_cfg->act_used = 0;
                }
                vfe_print("Find sensor name is \"%s\", i2c address is %x, type is \"%s\" !\n",sensor_info.sensor_name,sensor_info.i2c_addr,
                                sensor_info_type[sensor_info.sensor_type]);
            }
            sensor_i2c_board->addr = (unsigned short)(ccm_cfg->i2c_addr>>1);
            strcpy(sensor_i2c_board->type,ccm_cfg->ccm);

            vfe_print("Sub device register \"%s\" i2c_addr = 0x%x start!\n",sensor_i2c_board->type, ccm_cfg->i2c_addr);
            ret = vfe_sensor_subdev_register_check(dev,v4l2_dev,ccm_cfg,sensor_i2c_board);
            if( ret == -1)
            {
                vfe_sensor_subdev_unregister(v4l2_dev,ccm_cfg,sensor_i2c_board);
                vfe_print("Sub device register \"%s\" failed!\n",sensor_i2c_board->type);
                ccm_cfg->sd =NULL;
                continue;
            }
            else if(ret == ENODEV ||ret == EFAULT)
            {
                continue;
            }
            else if(ret == 0)
            {
                vfe_print("Sub device register \"%s\" is OK!\n",sensor_i2c_board->type);
                break;
            }
        }
        return ccm_cfg->sd;
    }
