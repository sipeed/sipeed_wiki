移植tslib
===================================

.. contents:: 本文目录

tslib是电阻式触摸屏用于校准的一个软件库，是一个开源的程序，能够为触摸屏驱动获得的采样提供诸如滤波、去抖、校准等功能，通常作为触摸屏驱动的适配层，为上层的应用提供了一个统一的接口。
所以这里先编译安装tslib，这样在后面编译Qt的时候才能打包编译进去。

下载编译tslib
-----------------------------------

.. code-block:: bash

    sudo apt-get install libtool automake autogen autoconf libsysfs-dev
    git clone https://github.com/kergoth/tslib.git
    cd tslib
    echo  "ac_cv_func_malloc_0_nonnull=yes"  > tmp.cache
    ./autogen.sh
    ./configure --host=arm-linux-gnueabihf --cache-file=tmp.cache   --prefix=/opt/tslib CC=/opt/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-gcc
    make  
    sudo make install  

完成后tslib就被安装到了/opt/tslib目录下

参考资料
------------------------------------

http://blog.csdn.net/hpu11/article/details/53105947
