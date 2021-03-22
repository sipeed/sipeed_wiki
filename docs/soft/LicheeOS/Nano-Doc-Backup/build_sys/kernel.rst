主线Linux编译
================================

.. contents:: 本文目录

源码下载
--------------------------------

完整下载命令为：

    ``git clone https://github.com/Icenowy/linux.git``

git拉取有时速度很慢，建议做如下配置：

    .. code-block:: bash

        sudo vim /etc/hosts
        # 添加下面两行
        192.30.253.112  github.com
        151.101.73.194 github.global.ssl.fastly.net
        # 添加完成
        # 可自行通过dns检测网站检测github.global.ssl.fastly.net，更换为更快的ip地址

完整拉取linux极大，建议只拉取单层分支，减少等待时间：

    ``git clone --depth=1 -b f1c100s-480272lcd-test https://github.com/Icenowy/linux.git``

配置
--------------------------------

下载 `.config <http://dl.sipeed.com/LICHEE/Nano/SDK/config>`_ 文件，放入源码主目录进行替换 (若下载时文件名有变，请重命名回 .config );

进行编译 
--------------------------------

.. tip:: 编译工具链为 arm-linux-gnueabi，工具链的安装请参考 uboot 编译部分

.. code-block:: bash

    make ARCH=arm menuconfig
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabi- -j4    #请自行修改编译线程数

生成的 zImage 在 :menuselection:`arch --> arm --> boot` 目录下；将其放入第一分区。

.. admonition:: 交流与答疑
    
    对于本节内容，如有疑问，欢迎到 `主线linux 编译交流帖 <http://bbs.lichee.pro/d/22-linux>`_ 提问或分享经验。
