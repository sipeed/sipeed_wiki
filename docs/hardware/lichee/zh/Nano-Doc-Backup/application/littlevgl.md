LittlevGL 使用
==============

LittlevGL 简介
--------------

LittlevGL
是一个开源免费的GUI，支持触摸屏操作，移植简单方便，开发者一直在不断完善更新。LittlevGL
自带了丰富的控件：窗口、按键、标签、list、图表等，还可以自定义控件；支持很多特效：透明、阴影、自动显示隐藏滚动条、界面切换动画、图标打开关闭动画、平滑的拖拽控件、分层显示、反锯齿、仅耗少量内存的字体等等。

LittlevGL 常见于
MCU级别的设备，支持各类输入输出接口与芯片，支持使用GPU，以C编写，对于
Nano来说十分适合。

![](https://littlevgl.com/home/main_cover.png)

具体的编写指导，请参考 [littlevGL官方文档](https://littlevgl.com/basics)

LittlevGL 下载
--------------

建立LittlevGL工程文件夹，在此文件夹下进行以下操作:
``` 

git clone https://github.com/littlevgl/lvgl.git
git clone https://github.com/littlevgl/lv_drivers.git
git clone https://github.com/littlevgl/lv_examples.git
```

LittlevGL 工程配置
------------------

此处用到三个配置文件，分别是：

> -   lvgl/lv\_conf\_templ.h
> -   lv\_drivers/lv\_drv\_conf\_templ.h
> -   lv\_examples/lv\_ex\_conf\_templ.h

将此三配置文件从模块文件夹中复制到项目文件夹，并将其命名为

> -   lv\_conf.h
> -   lv\_drv\_conf.h
> -   lv\_ex\_conf.h

添加 main.c 文件

``` 
#include "lvgl/lvgl.h"

/* 添加 fb 支持 */
#include "lv_drivers/display/fbdev.h"

int main(void)
{
    /*LittlevGL init*/
    lv_init();

    /*Linux frame buffer device init*/
    fbdev_init();

    /*Add a display the LittlevGL sing the frame buffer driver*/
    lv_disp_drv_t disp_drv;
    lv_disp_drv_init(&disp_drv);
    disp_drv.disp_flush = fbdev_flush;      /*It flushes the internal graphical buffer to the frame buffer*/
    lv_disp_drv_register(&disp_drv);

    /* 选择示例启动 */
    demo_create();

    /*Handle LitlevGL tasks (tickless mode)*/
    while(1) {
        lv_tick_inc(5);
        lv_task_handler();
        usleep(5000);
    }

    return 0;
}
```

此时工程文件目录如下所示：

![](https://fdvad021asfd8q.oss-cn-hangzhou.aliyuncs.com/migrate/2018-04-09%2013-15-15%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)

LittlevGL 板级配置
------------------

### lv\_conf.h

首先在 lv\_conf.h 中找到屏幕的定义，并进行修改；
此处修改为 800X480 或 480X272:

```
#define LV_HOR_RES (800)
#define LV_VER_RES (480)
```

### lv\_drv\_conf.h

再看到 lv\_drv\_conf.h，此文件中定义了输入输出设备的选择

main.c 中已经调用了 linux 下 framebuffer 设备，需要修改：

 `#define USE_FBDEV 1`

若有触摸屏，定义为从event0中解析触摸数据：

 `#define USE_EVDEV 1`

### lv\_ex\_conf.h

此配置文件定义你将要编译哪个应用示例：

```
#define USE_LV_BENCHMARK   0
#define USE_LV_DEMO        0
#define USE_LV_SYSMON      0
#define USE_LV_TERMINAL    0
#define USE_LV_TPCAL       0
```

选择一个示例，修改为 **1**;

对应的，我们要在 main.c 中进行修改，这里以demo作为示例：
1.  查看 lv\_examples --\> lv\_apps --\> demo --\> demo.c
2.  可以看到其创建函数为 **demo\_creat()**
3.  修改 main.c 中 while(1)循环前的一句为 **demo\_creat()**

配置完成。

### 添加触屏支持

lv\_drv\_conf.h 中我们要先配置为从 event0 中读取数据；

此时要添加 event输入支持所需的结构体；

```
void demo_create(void)
{
    lv_indev_drv_t indev_drv;
    lv_indev_drv_init(&indev_drv);          /*Basic initialization*/
    evdev_init();
    indev_drv.type = LV_INDEV_TYPE_POINTER; /*See below.*/
    indev_drv.read = evdev_read;            /*See below.*/
    lv_indev_drv_register(&indev_drv);      /*Register the driver in LittlevGL*/

    /*……………略……………*/
}
```

其他配置或移植文档，请参考 [porting](https://littlevgl.com/porting)

LittlevGL 编译
--------------

LittlevGL
示例程序需要自行编写Makefile或直接使用IDE自动寻找依赖关系进行编译；

> Nano提供了docker镜像包，可通过docker直接使用cmake编译，编译具体步骤请看cmake部分；

笔者本处使用了Clion进行了交叉编译尝试，并附上仅使用cmake来进行编译的步骤；

### Clion 配置

Clion的安装配置本处不再赘述，此处描述交叉编译相关步骤

Clion配置工程后，会自动生成 **CMakeLists.txt** ,此文件为 cmake 编译配置文件(Clion使用了cmake来进行构建)；

修改此文件配置，使其使用交叉编译工具进行编译；

```
cmake_minimum_required(VERSION 3.10)        # cmake 版本要高于或等于 3.10
project(Ui C)                               # 输出的二进制文件名

#set(CMAKE_C_STANDARD 11)                   # 注释掉原有的
SET(CROSS_COMPILE 1)                        # 设定交叉编译标志位
set(CMAKE_SYSTEM_NAME Linux)                # 设定目标系统为 linux
set(CMAKE_C_COMPILER "/usr/bin/arm-linux-gnueabi-gcc")  # 设定交叉编译链gcc所在位置

SET(TOOLCHAIN_DIR "/usr/bin/")              # 设定交叉编译链目录         
SET(CMAKE_FIND_ROOT_PATH  "/usr/arm-linux-gnueabi" "/usr/arm-linux-gnueabi/lib" "/usr/arm-linux-gnueabi/include") 
# lib 与 include 的目录，使用 ``arm-linux-gnueabi-gcc -v`` 也可输出目录相关信息

link_directories(/home/biglion/project/buildroot/rootfs/lib)          # 根文件系统的 lib (此处可参照cmake说明)

# 依赖信息～略～
```

修改后，编译即可，可执行文件输出在 *cmake-build-debug* 文件夹下；

### Cmake 配置

若您在本地构建，请下载[CMakeLists.txt](https://fdvad021asfd8q.oss-cn-hangzhou.aliyuncs.com/migrate/CMakeLists.txt)并自行修改lib/include/编译链等目录,确认您的cmake版本高于或等于 3.10 (要从官网下载编译安装)

在docker镜像中，已配置好 cmake；只需修改 CMakeLists.txt 中，rootfs的 lib
的目录地址；

>（比如先用 buildroot 构建好了根文件系统，
> 1.  rootfs.tar中包含了 lib ，可将rootfs.tar解压到某处或只取出lib
>     再进行指定
> 2.  或者在 buildroot-\>output-\>target 目录下,也包含了lib）

只需：

```
cd xxx           # 进入工程目录
mkdir build      # 将生成信息等放进新建的目录，令目录结构更为清爽
cd build
cmake ..         # cmake 生成 makefile
make             # 执行编译
```

生成可执行二进制文件就在 build 文件夹下，将其放进tf卡的根文件系统所在位置下，运行即可。

也可使用 [pc\_simulator](https://github.com/littlevgl/pc_simulator)进行效果预览；

> 若在编译过程中有依赖缺失、函数未定义等情况，请自行寻找对应函数，并添加头文件: )

> **交流与答疑**
> 对于本节内容，如有疑问，欢迎到 [GUI交流帖](http://bbs.lichee.pro/d/25-gui) 提问或分享经验。
