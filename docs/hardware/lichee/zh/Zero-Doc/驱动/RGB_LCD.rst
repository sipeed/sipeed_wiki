点屏之RGB屏
=============================

.. contents:: 本文目录

Zero默认支持800x480和480x272这两种常见分辨率的的RGB屏幕。

这两种分辨率的屏幕，直接在编译时候选择对应的分辨率即可。

Zero还可以接RGB2VGA小板或者RGB2LVDS小板来驱动VGA液晶屏或者LVDS屏幕，这时候就需要自己改动屏幕参数了。

Uboot屏幕参数
----------------------------

修改FB大小

FB大小为 分辨率x4：

    800x480x4=1.5M
    800x600x4=1.8M
    1024x600x4=2.4M
    1024x768x4=3M
    1024x1024x4=4M


默认uboot里预留了2M的FB，对于1024x600以上的屏幕无法显示。

需要修改 *u-boot/include/configs/sunxi-common.h* 文件

``296 #define CONFIG_SUNXI_MAX_FB_SIZE (2 << 20)``

改为

``296 #define CONFIG_SUNXI_MAX_FB_SIZE (3 << 20)``

增加时序文件

默认配置文件在u-boot/configs/LicheePi_Zero_800x480LCD_defconfig等，可以根据自己的需要来新增文件，比如：

*u-boot/configs/LicheePi_Zero_1024x768LCD_defconfig*

*7CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:87,ri:40,up:31,lo:13,hs:1,vs:1,sync:3,vmode:0"*

改为

*CONFIG_VIDEO_LCD_MODE="x:1024,y:768,depth:24,pclk_khz:32000,le:198,ri:120,up:21,lo:821,hs:2,vs:2,sync:3,vmode:0"*

（时钟太高>60M貌似会hang？）

这里有个小脚本可以把fex文件的时序转换成uboot的时序：

.. code-block:: bash

    #!/usr/bin/env ruby

    if !ARGV[0] || !File.exists?(ARGV[0]) then
    abort "Usage: ruby #{__FILE__} [fex_file_name]\n"
    end

    def parse_fex_section(filename, section)
    results = {}
    current_section = ""
    File.open(filename).each_line {|l|
        current_section = $1 if l =~ /^\[(.*?)\]/
        next if current_section != section
        results[$1] = $2.strip if l =~ /^(\S+)\s*\=\s*(.*)/
        results[$1] = $2.to_i if l =~ /^(\S+)\s*\=\s*(\d+)\s*$/
    }
    return results
    end

    def print_video_lcd_mode(lcd0_para, vt_div)
    x        = lcd0_para["lcd_x"]
    y        = lcd0_para["lcd_y"]
    depth    = { 0 => 24, 1 => 18 }[lcd0_para["lcd_frm"]]
    pclk_khz = lcd0_para["lcd_dclk_freq"] * 1000
    hs       = [1, (lcd0_para["lcd_hv_hspw"] || lcd0_para["lcd_hspw"])].max
    vs       = [1, (lcd0_para["lcd_hv_vspw"] || lcd0_para["lcd_vspw"])].max
    le       = lcd0_para["lcd_hbp"] - hs
    ri       = lcd0_para["lcd_ht"] - x - lcd0_para["lcd_hbp"]
    up       = lcd0_para["lcd_vbp"] - vs
    lo       = lcd0_para["lcd_vt"] / vt_div - y - lcd0_para["lcd_vbp"]

    abort "Unsupported 'lcd_frm' parameter" if !depth

    printf("CONFIG_VIDEO_LCD_MODE=\"" +
            "x:#{x},y:#{y},depth:#{depth},pclk_khz:#{pclk_khz}," +
            "le:#{le},ri:#{ri},up:#{up},lo:#{lo},hs:#{hs},vs:#{vs}," +
            "sync:3,vmode:0\"\n")
    end

    lcd0_para = parse_fex_section(ARGV[0], "lcd0_para")
    abort "Not a valid 'lcd0_para' section" if lcd0_para["lcd_used"] != 1

    printf("== for sun[457]i ==\n")
    print_video_lcd_mode(lcd0_para, 2)

    printf("\n== for sun[68]i ==\n")
    print_video_lcd_mode(lcd0_para, 1)

