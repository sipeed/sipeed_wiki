编译和使用sunxi-tools
====================================

.. contents:: 本文目录

------------------------------------

1. 克隆sunxi-tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  ``git clone https://github.com/Icenowy/sunxi-tools.git -b f1c100s-spiflash``

2. 编译sunxi-tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 安装sunxi-tools依赖库

  ``sudo apt install libz libusb-1.0-0-dev``
  
- 编译

  ``make``

- 安装

  ``make install``

3. 使用sunxi-tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 查看芯片信息

  ``sudo sunxi-fel ver``

  AWUSBFEX soc=00001663(F1C100s) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000

- 列出所有芯片的信息

  ``sudo sunxi-fel -l``

- 加载并执行uboot的spl

  ``sudo sunxi-fel spl 文件名``

- 把文件内容写入内存指定地址(-p是显示写入进度)
  ``sudo sunxi-fel -p write 地址 文件名

- 调用指定地址的函数
  ``sudo sunxi-fel exec 地址``

- 显示spiflash的信息
  ``sudo sunxi-fel spiflash-info``

- 读取spiflash指定地址的数据并写入到文件
  ``sudo sunxi-fel spiflash-read 地址 长度 存放数据的文件路径``

- 写入指定文件的指定长度的内容到spiflash的指定地址
  ``sudo sunxi-fel spiflash-write 地址 长度 存放数据的文件路径``
