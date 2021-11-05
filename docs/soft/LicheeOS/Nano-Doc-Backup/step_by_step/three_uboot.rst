编译和配置uboot
====================================

.. contents:: 本文目录

------------------------------------

1. 克隆uboot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  ``git clone https://github.com/Lichee-Pi/u-boot.git -b nano-v2018.01``

2. 载入默认配置
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 如果需要生成在sdram里启动的uboot

  ``make ARCH=arm licheepi_nano_defconfig``

- 如果需要生成在spiflash里启动的uboot

  ``make ARCH=arm licheepi_nano_spiflash_defconfig``

3. 编译时可能遇到的问题以及解决办法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- /bin/sh: 1: cc: not found

  ``sudo apt install gcc``

- *** Configuration file ".config" not found!

  请检查当前用户是否有当前文件夹的读写权限,然后再次载入默认配置.

- /bin/sh: 1: python: not found

  ``sudo apt install python``

- unable to execute 'swig': No such file or directory
error: command 'swig' failed with exit status 1

  ``apt install swig``

- scripts/dtc/pylibfdt/libfdt_wrap.c:149:11: fatal error: Python.h: No such file or directory

  ``apt install python-dev``

- /bin/sh: 1: bc: not found

  ``apt install bc``

3. 测试uboot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
