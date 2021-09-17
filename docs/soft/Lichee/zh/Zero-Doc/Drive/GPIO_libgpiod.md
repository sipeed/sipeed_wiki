---
title: C语言方式(libgpiod)
---
在linux4.8以后，可以通过libgpiod库控制gpio

首先在buildroot中生成libgpiod库，然后就可以编写c代码了。

```
#include <stdio.h>
#include <unistd.h>
#include <gpiod.h>
#define msleep(t) usleep((t)*1000)
int main(int argc, char const *argv[])
{
    struct gpiod_chip *chip;
    struct gpiod_line *line;
    struct gpiod_line_request_config config;
    int req;
    /* PH0=(H-1)*32+0=(7-1)*32+0=192 */
    int PH0=192;
    
    /* 打开 GPIO 控制器 */
    gpiochip0 = gpiod_chip_open("/dev/gpiochip0");
    if (!gpiochip0)
        return -1;
    
    /* 获取PH5引脚 */
    led = gpiod_chip_get_line(gpiochip0, PH5);

    if (!led)
    {
        gpiod_chip_close(gpiochip0);
        return -1;
    }

    config.consumer = "blink";
    config.request_type = GPIOD_LINE_REQUEST_DIRECTION_OUTPUT; // 输出模式
    
    /* 配置引脚 */
    reg = gpiod_line_request(led, &config, 0);
    if (reg)
    {
        fprintf(stderr, "led request error.\n");
        return -1;
    }

    while (1)
    {
        /* 设置引脚电平 */
        gpiod_line_set_value(led, 1);
        printf("set led to 0\n");
        msleep(500);
        gpiod_line_set_value(led, 0);
        printf("set led to 1\n");
        msleep(500);
    }

    return 0;
}
```

或者

```
#include <stdio.h>
#include <unistd.h>
#include <gpiod.h>
#define msleep(t) usleep((t)*1000)
int main(int argc, char const *argv[])
{
    struct gpiod_chip *gpiochip0;
    struct gpiod_line *led;
    struct gpiod_line_request_config config;
    int req;
    /* PH0=(H-1)*32+0=(7-1)*32+0=192 */
    int PH0=192;
    
    /* 打开 GPIO 控制器 */
    gpiochip0 = gpiod_chip_open("/dev/gpiochip0");
    if (!gpiochip0)
        return -1;
    
    /* 获取PH5引脚 */
    led = gpiod_chip_get_line(gpiochip0, PH5);

    if (!led)
    {
        gpiod_chip_close(gpiochip0);
        return -1;
    }
    
    /* 配置引脚  输出模式 name为“bilik” 初始电平为low*/
    req = gpiod_line_request_output(led, "blink", 0);
    if (req)
    {
        fprintf(stderr, "led request error.\n");
        return -1;
    }

    while (1)
    {
        /* 设置引脚电平 */
        gpiod_line_set_value(led, 1);
        printf("set led to 0\n");
        msleep(500);
        gpiod_line_set_value(led, 0);
        printf("set led to 1\n");
        msleep(500);
    }

    return 0;
}
```

对比python

```
import time
import gpiod as gpio
PG_BASE = (7-1)*32 # "PG"
gpiochip0 = gpio.chip("gpiochip0")
led = gpiochip0.get_line((PG_BASE + 1)) # "PG1"
config = gpio.line_request()
config.request_type = gpio.line_request.DIRECTION_OUTPUT
led.request(config)

while led:
        led.set_value(0)
        time.sleep(1)
        led.set_value(1)
        time.sleep(1)
```

可以看出api基本是一致的。

使用交叉编译生成led.o文件，丢到板子里。
需要注意的是，编译libgpiod需要的编译器内核版本需要大于4.8，不然会报configure: error: "libgpiod needs linux headers version >= v4.8.0"，也即是意味着

`arm-linux-gnueabihf`的版本要大于7

### 交叉编译配置

首先下载libgpiod源码

```
wget https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/snapshot/libgpiod-1.6.3.tar.gz
```

安装依赖

```
apt-get isntall autoconf
```

配置安装选项

```
./autogen.sh --enable-tools=no  --host=arm-linux-gnueabihf --prefix=/home/lithromantic/Desktop/led/source
```

--host指定交叉编译链，注意不带后缀

--prefix指定安装路径，必须是绝对路径。一般安装到工程目录下，也可以安装到一个固定的位置用于共享。

还需要注释一个define，不然会报`undefined reference to rpl_malloc`

`vim config.h`

划到最后尾，删除

```
/* Define to rpl_malloc if the replacement function should be used. */

#define malloc rpl_malloc
```

然后

```
make
make install
```



### 交叉编译

```
cd led
vim led.c
arm-linux-gnueabihf-gcc -o led led.c -I ./source/include  -L ./source/lib -lgpiod
```

`arm-linux-gnueabihf-gcc -o led` 使用arm编译器，-o 指定输出名为led

`-I ./source/include`  -I 指定头文件位置

`-L ./source/lib` -L 指定动态链接库位置

`-lgpiod` 指定使用的链接库

因为我们在荔枝派上已经安装了libgpiod，所以可以动态引用，如果需要静态编译，则需要在最后面添加  ` -static`

