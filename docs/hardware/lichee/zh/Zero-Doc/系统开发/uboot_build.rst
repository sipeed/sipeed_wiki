Uboot 编译
===================================

.. contents:: 本文目录

基础编译
-----------------------------------

安装交叉编译器
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

网盘地址：http://pan.baidu.com/s/1hsf22fq

国外用户：https://releases.linaro.org/components/toolchain/binaries/latest/arm-linux-gnueabihf/

.. code-block:: bash

   wget https://releases.linaro.org/components/toolchain/binaries/latest/arm-linux-gnueabihf/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf.tar.xz
   tar xvf gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf.tar.xz
   mv gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf /opt/
   vim /etc/bash.bashrc
   # add: PATH="$PATH:/opt/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf/bin"
   source /etc/bash.bashrc
   arm-linux-gnueabihf-gcc -v
   sudo apt-get install device-tree-compiler

下载编译Uboot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
.. code-block:: bash

   git clone https://github.com/Lichee-Pi/u-boot.git -b v3s-current
   #or git clone https://github.com/Lichee-Pi/u-boot.git -b v3s-spi-experimental
   cd u-boot
   make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- LicheePi_Zero_800x480LCD_defconfig
   #or make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- LicheePi_Zero480x272LCD_defconfig
   #or make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- LicheePi_Zero_defconfig
   make ARCH=arm menuconfig
   time make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- 2>&1 | tee build.log

编译完成后，在当前目录下生成了u-boot-sunxi-with-spl.bin，可以烧录到8K偏移处启动。

Uboot结构简介
-----------------------------------

下面来看看该uboot中的目录结构

:: 

   ├── api                存放uboot提供的API接口函数
   ├── arch               平台相关的部分我们只需要关心这个目录下的ARM文件夹
   │   ├──arm
   │   │   └──cpu
   │   │   │   └──armv7
   │   │   └──dts	
   │   │   │   └──*.dts 存放设备的dts,也就是设备配置相关的引脚信息
   ├── board              对于不同的平台的开发板对应的代码
   ├── cmd                顾名思义，大部分的命令的实现都在这个文件夹下面。
   ├── common             公共的代码
   ├── configs            各个板子的对应的配置文件都在里面，我们的Lichee配置也在里面
   ├── disk               对磁盘的一些操作都在这个文件夹里面，例如分区等。
   ├── doc                参考文档，这里面有很多跟平台等相关的使用文档。
   ├── drivers            各式各样的驱动文件都在这里面
   ├── dts                一种树形结构（device tree）这个应该是uboot新的语法
   ├── examples           官方给出的一些样例程序
   ├── fs                 文件系统，uboot会用到的一些文件系统
   ├── include            头文件，所有的头文件都在这个文件夹下面
   ├── lib                一些常用的库文件在这个文件夹下面  
   ├── Licenses           这个其实跟编译无关了，就是一些license的声明
   ├── net                网络相关的，需要用的小型网络协议栈
   ├── post              上电自检程序
   ├── scripts           编译脚本和Makefile文件
   ├── spl               second program loader，即相当于二级uboot启动。
   ├── test              小型的单元测试程序。
   └── tools             里面有很多uboot常用的工具。

了解了uboot的基本结构，我们可以知道一些相关的配置在什么地方了。

- lichee的uboot配置文件放在confgs文件目录下面，名称为

:: 

   LicheePi_Zero_480x272LCD_defconfig 
   LicheePi_Zero_800x480LCD_defconfig 
   LicheePi_Zero_defconfig

这3个配置是根据不同的Zero显示设备进行的配置，使用其中之一即可，可在uboot目录下执行命令

   ``make LicheePi_Zero_defconfig``

这样配置就生效了。
