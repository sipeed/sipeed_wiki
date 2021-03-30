开机logo替换
===================================

.. contents:: 本文目录

uboot启动界面的版本信息隐藏
-----------------------------------

*drivers/video/cfb_console.c* 中加上 ``CONFIG_HIDE_LOGO_VERSION`` ，可以隐藏uboot的版本信息。

uboot开机画面更换
-----------------------------------

Uboot的开机logo默认情况（只定义了 ``CONFIG_VIDEO_LOGO``）是企鹅logo，这个是存在于uboot代码中的一个头文件（ *include/video_logo.h* 或 *bmp_logo.h*），这个是一个巨大的结构体，其中保存着图片每个像素点的色彩数据。

准备一张jpeg图片，通过命令行处理为8bit BMP图片
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash


   #!/bin/sh
   #install Netpbm first
   jpegtopnm $1 | ppmquant 31 | ppmtobmp -bpp 8 > $2

使用方法： （脚本名） （ 待处理的JPG图片名） （输出文件名）

//这种方式出来的图不如用专业图片处理软件的好

将bmp文件放入/tools/logos中，并修改/tools/下的Makefile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Generated LCD/video logo
   LOGO_H = $(OBJTREE)/include/bmp_logo.h
   LOGO-$(CONFIG_LCD_LOGO) += $(LOGO_H)
   LOGO-$(CONFIG_VIDEO_LOGO) += $(LOGO_H)
   ifeq ($(LOGO_BMP),)
   LOGO_BMP= logos/mylogo.bmp
   endif
   ifeq ($(VENDOR),atmel)
   LOGO_BMP= logos/atmel.bmp
   endif
   ifeq ($(VENDOR),esd)
   LOGO_BMP= logos/esd.bmp
   endif
   ifeq ($(VENDOR),freescale)
   LOGO_BMP= logos/freescale.bmp
   endif
   ifeq ($(VENDOR),ronetix)
   LOGO_BMP= logos/ronetix.bmp
   endif
   ifeq ($(VENDOR),syteco)
   LOGO_BMP= logos/syteco.bmp
   endif

将 *mylogo.bmp* 替换成你生成的logo

确认配置文件
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在 *include/configs/sun8i.h​* 中加入两个宏定义：

.. code-block:: bash

   #define CONFIG_VIDEO_LOGO
   #define CONFIG_VIDEO_BMP_LOGO

编译的时候，你的bmp文件会被 *tools/bmp_logo.c* 编译出的工具bmp_logo制作成 *include/bmp_logo.h*，并编译进uboot中。

重新编译u-boot即可得到显示新logo的u-boot。
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip:: 

    相关代码在drivers/video/cfb_console.c下

.. code-block:: c

   #ifdef CONFIG_VIDEO_LOGO
           /* Plot the logo and get start point of console */
           debug("Video: Drawing the logo ...\n");
           video_console_address = video_logo();
   
drv_video_init -> cfg_video_init

linux开机画面更换
-----------------------------------

方法一
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*drivers/video/logo/logo_linux_clut224.ppm* 是默认的启动Logo图片，把自己的Logo图片（png格式）转换成ppm格式，替换这个文件，同时删除 *logo_linux_clut224.c logo_linux_clut224.o* 文件，重新编译

具体方法：

.. code-block:: bash

   #sudo apt-get install netpbm
   #pngtopnm your_boot.png > logo_linux_clut2240.pnm
   #pnmquant 224 logo_linux_clut2240.pnm > logo_linux_clut2241.pnm
   #pnmtoplainpnm logo_linux_clut2241.pnm > logo_linux_clut224.ppm
   #cp drivers/video/logo/logo_linux_clut224.ppm drivers/video/logo/logo_linux_clut224.ppm.bak
   #cp pic/logo_linux_clut224.ppm drivers/video/logo/logo_linux_clut224.ppm

注：先把png转换成pnm格式，但内核的Logo最高只支持224色，需要把颜色转换成224色，最后把pnm转成ppm，文件名必须是 **logo_linux_clut224.ppm** 。

注意在kernel的menuconfig里需要使能LOGO。

方法二
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

用RedHat9.0自带的图片编辑工具GIMP(其他发行版自己安装就行了)。

1. 将颜色数改为224（在GIMP中一次选择 图像->模式->索引。如下图所示）。
2. 调整大小：宽高都小两像素，否则不显示。
3. 另存为，保存为ppm格式，在弹出的对话框中选择Ascii，然后复制到Logo文件夹替换原来的文件，同时删除 *logo_linux_clut224.c logo_linux_clut224.o* 文件。

隐藏启动光标
-----------------------------------

在内核的当前目录进入到 *drivers/video/console/fbcon.c* 文件

将 ``static void fb_flashcursor(void *private)，static void fbcon_cursor(struct vc_data *vc, int mode)`` 用空函数替换。

另一种禁止光标的方法：

.. code-block:: bash
   :caption: drivers/video/console/Makefile

   #obj-$(CONFIG_FRAMEBUFFER_CONSOLE) += fbcon.o bitblit.o font.o softcursor.o
   obj-$(CONFIG_FRAMEBUFFER_CONSOLE) += fbcon.o bitblit.o font.o

编译遇到一个 *soft_cursor* 没有定义的问题问题，注释代码：

.. code-block:: c
   :caption: drivers/video/console/bitblit.c

    //ABING
    //      if (err)
    //              soft_cursor(info, &cursor);
