主线Kernel基础编译
=================================

.. contents:: 本文目录

安装交叉编译器
---------------------------------

网盘地址：http://pan.baidu.com/s/1hsf22fq

国外用户：https://releases.linaro.org/components/toolchain/binaries/latest/arm-linux-gnueabihf/

.. code-block:: bash

   wget https://releases.linaro.org/components/toolchain/binaries/latest/arm-linux-gnueabihf/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf.tar.xz
   tar xvf gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf.tar.xz
   mv gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf /opt/
   vim /etc/bash.bashrc
   # add: PATH="$PATH:/opt/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf/bin"
   arm-linux-gnueabihf-gcc -v

下载编译linux源码
---------------------------------

(默认是zero-4.10.y分支)：

.. code-block:: bash

   git clone https://github.com/Lichee-Pi/linux.git
   cd linux
   make ARCH=arm licheepi_zero_defconfig
   make ARCH=arm menuconfig   #add bluethooth, etc.
   make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- -j16
   make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- -j16 INSTALL_MOD_PATH=out modules
   make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- -j16 INSTALL_MOD_PATH=out modules_install
   
编译完成后，zImage在arch/arm/boot/下，驱动模块在out/下
   