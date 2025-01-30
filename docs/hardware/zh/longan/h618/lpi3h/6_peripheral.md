---
title: 外设使用
keywords: Linux, Longan, H618, SBC, ARM, Peripheral
update:
  - date: 2023-12-08
    version: v1.0
    author: ztd
    content:
      - Release docs
---


## SoC 相关
 
### CPU 运行频率

```shell
sudo cat /sys/devices/system/cpu/cpu*/cpufreq/cpuinfo_cur_freq
```
单位为 KHz
注意系统自带温控策略，当系统过于空闲或者温度过高时，都会降频。

## PWM

TODO 

## GPIO

![io_map](./assets/peripheral/io_map.jpeg)

![pin_num](./assets/peripheral/pin_num.png)

参考上面的两个表格，可以找到要使用的 GPIO 对应的位置和序号，以点亮底板上的两个 LED 灯为例，可以使用命令在用户空间操作对应的 GPIO：

使用前先检查 GPIO 是否被占用
```shell
sudo cat /sys/kernel/debug/gpio
```

```shell
num=194
echo ${num} > /sys/class/gpio/export  
echo out > /sys/class/gpio/gpio${num}/direction 
echo 0 > /sys/class/gpio/gpio${num}/value
num=196
echo ${num} > /sys/class/gpio/export  
echo out > /sys/class/gpio/gpio${num}/direction 
echo 0 > /sys/class/gpio/gpio${num}/value
```

除了上述方法外，还可以通过 C 语言的 libgpiod 库来操作 GPIO，下面仍然以底板上的 LED 灯为例

```c
#include <gpiod.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int i;
    int ret;

    struct gpiod_chip * chip;
    struct gpiod_line * line;

    chip = gpiod_chip_open("/dev/gpiochip0");
    if(chip == NULL)
    {
        printf("gpiod_chip_open error\n");
        return -1;
    }

    line = gpiod_chip_get_line(chip, 194);
    if(line == NULL)
    {
        printf("gpiod_chip_get_line error\n");
        gpiod_line_release(line);
    }

    ret = gpiod_line_request_output(line,"gpio",0);
    if(ret < 0)
    {
        printf("gpiod_line_request_output error\n");
        gpiod_chip_close(chip);
    }

    for(i = 0; i < 10; i++)
    {
        gpiod_line_set_value(line,1);
        sleep(1);
        gpiod_line_set_value(line,0);
        sleep(1);
    }

    gpiod_line_release(line);
    gpiod_chip_close(chip);

    return 0;
}
```

首先安装需要的依赖：
```shell
sudo apt update
sudo apt install build-essential libgpiod-dev gpiod
```

编译后，需要使用 root 权限来执行程序：
```shell
gcc gpio.c -I /usr/include/ -L /usr/lib/aarch64-linux-gnu/ -lgpiod -o gpio
sudo ./gpio
```

libgpiod 也提供了一些命令来操作 gpio，常用的命令如下：
gpiodetect：列出所有的 GPIO 控制器 
```shell
sudo gpiodetect
```
gpioinfo：列出 GPIO 控制器的引脚情况，可以查看哪些引脚已经被使用
```shell
sudo gpioinfo gpiochip0
```
gpioset：设置 GPIO 引脚的状态
```shell
sudo gpioset gpiochip0 196=0
```
gpioget：获取 GPIO 引脚状态
```shell
sudo gpioget gpiochip0 196
```

## UART 

### 系统串口

LonganPi 3H 的系统串口是 UART0,在侧边插针中有引出。  

![uart_pin](./assets/peripheral/uart_pin.png)  

你可以使用 USB 转串口模块连接该串口，即 `U0-RX` 和 `U0-TX`，注意交叉连接，以及 GND 连接(下图中还多接了一根供电线，若用 typeC 口供电可以不接这根供电线)。

![uart_connect](./assets/peripheral/uart_connect.png)  

连接完成后，即可使用串口工具进行通信，Windows 下推荐 `XShell`，`mobaterm`，Linux下推荐 `minicom`   
设置串口波特率为 `115200`，即可在串口终端下登录并进行指令操作：  
> 注：刚连接后可以敲几个回车查看是否有反应，如果没有反应则检查接线或者串口配置


### 一般串口

除系统串口 UART0 外，设备树中也默认使能了 UART1，UART2，UART3，UART4 串口，可以根据需要使用。

#### 查看串口设备

```bash
ls /dev/ttyS*
```

#### 查看串口的波特率等信息

```bash
stty -F /dev/ttyS1 -a 
```

#### 设置串口波特率、数据模式

```bash
stty -F /dev/ttyS1 ispeed 115200 ospeed 115200 cs8
```

#### 查看串口数据

```bash
cat /dev/ttyS1
```

#### 发送串口数据

```bash
echo "LonganPi3H" > /dev/ttyS1
```

#### 其它方法

也可以使用`minicom`，或者pyserial库进行串口操作，请用户自行查找相关资料使用。若要使用非常见波特率，可以使用`picocom`。

## I2C

TODO

## SPI

TODO

## HDMI 显示

LonganPi 3H 最高支持 4k 分辨率的显示，效果如图所示：

![hdmi_connect](./assets/peripheral/hdmi_connect.jpg)

若插入 HDMI 显示器后没有显示，可以尝试在命令行中使用 xrandr 来更换显示配置参数。

首先导出 DISPLAY 变量
```shell
export DISPLAY=:0.0
```

然后用 xrandr 查看可用的参数：
```shell
sipeed@lpi3h-ce8e:~$ xrandr                                                     
Screen 0: minimum 320 x 200, current 1920 x 1080, maximum 8192 x 8192           
HDMI-1 connected 1920x1080+0+0 (normal left inverted right x axis y axis) 255mm 
x 220mm                                                                         
   1920x1080     60.00*+  60.00    59.94                                        
   1400x1050     59.95                                                          
   1280x1024     75.02    60.02                                                 
   1440x900      59.90                                                          
   1280x960      60.00                                                          
   1152x864      75.00                                                          
   1280x720      60.00    59.94                                                 
   1024x768      75.03    70.07    60.00                                        
   832x624       74.55                                                          
   800x600       72.19    75.00    60.32    56.25                               
   640x480       75.00    72.81    66.67    60.00    59.94                      
   720x400       70.08                                                          
```

根据上述命令的输出，我们可以尝试更换分辨率，帧率等配置，比如更换为 1440x900 分辨率：
```shell
xrandr xrandr --output HDMI-1 --mode 1440x900
```
有些参数可能会导致屏幕不亮，遇到插入 HDMI 显示器无显示时，可以用这个命令来调整至能亮的显示参数，也可以在系统设置中的 Dispaly 图形化菜单中调节。

若发现使用较高分辨率时有闪屏问题，可以尝试在图形化的设置显示的菜单中降低刷新率。

## HDMI 音频

TODO

## GPU

TODO


## 其它
欢迎投稿～ 投稿接受后可得￥5～150（$1~20）优惠券！