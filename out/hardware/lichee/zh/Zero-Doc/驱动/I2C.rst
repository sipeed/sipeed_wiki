I2C操作
=============================

.. contents:: 本文目录

使能设备树节点
-----------------------------

.. code-block:: bash
   :caption: arch/arm/boot/dts/sun8i-v3s-licheepi-zero.dts

    &i2c0 {
            status = "okay";

            ns2009: ns2009@48 {
                    compatible = "nsiway,ns2009";
                    reg = <0x48>;
            };
            sht21: sht21@40 {
                    compatible = "sht21";
                    reg = <0x40>;
            }；
            atmel_mxt_ts@4a {
                    compatible = "atmel,atmel_mxt_ts";
                    reg = <0x4a>;
                    /*interrupt-parent = <&pio>;
                    interrupts = <6 5 IRQ_TYPE_LEVEL_LOW>;*/ //省引脚，使用轮训方式
            };
    };

使用i2c-tools
------------------------------------

:: 

    root@LicheePi:~# i2cdetect -l	  #查看系统使能的i2c总线，这里只有i2c0一个
    i2c-0	i2c       	mv64xxx_i2c adapter             	I2C adapter
    root@LicheePi:~# i2cdetect -r -y 0	//检测总线上的设备。-y表示省去交互式
        0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    40: 40 -- -- -- -- -- -- -- UU -- 4a -- -- -- -- -- 
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    70: -- -- -- -- -- -- -- --

这里的40,48,4a 分别是sht21温湿度传感器，ns2009电阻式触摸传感器，mxt336T电容式触摸传感器。

i2c上读写数据：

.. code-block:: bash

    i2cset -y 1 0x40 0x00 0x13
    i2cget -y 1 0x40 0x00  

sht21 传感器使用
--------------------------------------

.. code-block:: bash

    insmod sht21.ko
    echo sht21 0x40 > /sys/bus/i2c/devices/i2c-0/new_device
    ls /sys/class/hwmon/hwmon0
        device           name   subsystem    uevent
        humidity1_input  power  temp1_input
    cat /sys/class/hwmon/hwmon0/temp1_input
        25201		#毫摄氏度，即25.201摄氏度
    cat /sys/class/hwmon/hwmon0/humidity1_input
        58872		#毫百分之1，即58.872%RH

参考文档
-------------------------------------

| https://blog.dbrgn.ch/2017/2/6/read-sht21-sensor-from-linux-raspberry-pi/
| http://www.360doc.com/content/14/1008/11/7775902_415207889.shtml

   http://blog.csdn.net/AJ_chenrui/article/details/51202689
