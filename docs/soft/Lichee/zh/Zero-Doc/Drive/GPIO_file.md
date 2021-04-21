---
title: 文件IO方式操作
---

GPIO编号及复用功能
==================

在Linux中，GPIO 使用0～MAX\_INT之间的整数标识。

对于32位CPU，每组GPIO 32个，引脚号就是按顺序排列。

LicheePi Zero的所有IO的复用功能及GPIO标识号为：

\>\> 总共52个IO，所有IO上电默认状态为高阻态, 驱动电流强度20mA \>\>
PB和PG具有中断功能

sysfs操作GPIO
=============

/sys/class/gpio目录下的三种文件：

-   export/unexport文件
-   gpioN指代具体的gpio引脚
-   gpio\_chipN指代gpio控制器

**export/unexport：**

-   /sys/class/gpio/export，只写，写入GPIO编号来向内核申请GPIO控制权（前提是没有内核代码申请这个gpio端口）,
    成功后会在目录下生成gpioN目录。
-   /sys/class/gpio/unexport和导出的效果相反。

**gpioN:**

指代某个具体的gpio端口, 内有以下属性文件：

**gpiochipN**

gpiochipN表示的就是一个gpio\_chip,用来管理和控制一组gpio端口的控制器，该目录下存在以下属性文件：

使用sysfs操作GPIO的例子：

    #echo 192 > /sys/class/gpio/export  #导出 PG0, GREEN
    #ls /sys/class/gpio/
    export     gpio192    gpiochip0  unexport
    #ls /sys/class/gpio/gpio192/
    active_low direction subsystem/ value device/ power/ uevent
    #echo "out" > /sys/class/gpio/gpio192/direction #设置为输出
    #echo 0 > /sys/class/gpio/gpio192/value #亮灯
    #echo 1 > /sys/class/gpio/gpio192/value #灭灯
    #echo "in" > /sys/class/gpio/gpio192/direction #设置为输入
    #cat /sys/class/gpio/gpio192/value #读取电平
    0

用户可以参考以上操作进行GPIO控制。

注意对重要引脚的导出操作可能会使系统崩溃。

LicheePi
Zero提供了简单的shell脚本进行GPIO读写(代码在https://github.com/Lichee-Pi/lichee-pi-zero/tree/master/SoftWare，下同)：

    gpio.sh init 192 out
    gpio.sh set 192 out
    gpio.sh get 192
    gpio.sh w 192 1
    gpio.sh r 192 
    gpio.sh deinit 192

附录（gpio.sh源码）
===================

~~~~ {.sourceCode .bash}
#!/bin/sh
function help()
{
echo "gpio.sh usage:"
echo "        gpio.sh init PG0 out"
echo "        gpio.sh set PG0 out"
echo "        gpio.sh get PG0"
echo "        gpio.sh w PG0 1"
echo "        gpio.sh r PG0"
echo "        gpio.sh deinit PG0"
}

if [ $# -lt 2 ]; then
        help;
        exit;
fi

portpin=`echo $2 | tr 'a-z' 'A-Z'`;
port=${portpin:1:1};
pin=${portpin:2:1};
#echo $port
#echo $pin
num=`printf "%d" "'$port"`;
num=`expr \( $num - 65 \) \* 32 + $pin`;
if [ $? -ne 0 ]; then
        help;
        exit                         
fi                                   
#echo $num                                

case $1 in                                            
        init)                                         
        echo $num > /sys/class/gpio/export            
        echo $3 > /sys/class/gpio/gpio${num}/direction
        ;;                                            
        set)                                           
        echo $3 > /sys/class/gpio/gpio${num}/direction 
        ;;                                             
        get)                                           
        echo `cat /sys/class/gpio/gpio${num}/direction`
        ;;                                             
        w)                                             
        echo $3 > /sys/class/gpio/gpio${num}/value
        ;;                                        
        r)                                        
        echo `cat /sys/class/gpio/gpio{num}/value`    
        ;;                                            
        deinit)                                       
        echo $num > /sys/class/gpio/unexport          
        ;;      
        *)                                            
        help                                          
        ;;                                            
esac  
~~~~
