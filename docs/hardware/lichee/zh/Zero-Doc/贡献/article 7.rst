Qt5 移植到 licheepi zero
===================================

.. contents:: 本文目录

.. admonition:: 环境

    - host:Ubuntu14.04 64 位
    - target:licheepi（全志 v3s）
    - 文件系统： mindb
    - 交叉编译链： gcc-linaro-6.3.1-2017.02-x86_64_arm-linux-gnueabihf.tar.xz
    - tslib 源代码： tslib-1.4.tar.gz
    - tslib 安装目标路径： /usr/local/tslib1.4
    - QT 源代码： qt-everywhere-opensource-src-5.4.1.tar.gz
    - QT 安装目标路径： /usr/local/qt5.4.1

安装步骤：

    本文主要讲述 QT 的移植过程， tslib 的移植过程可以搜索《 tslib1.4 移植全过程》参考，如果不需要触摸屏，
    
    可以不用移植 tslib。

1. 准备工作
-----------------------------------

确保以下软件已安装，

.. code-block:: bash

   sudo apt-get install xorg-dev libfontconfig1-dev \
   libfreetype6-dev libx11-dev libxcursor-dev libxext-dev \
   libxfixes-dev libxft-dev libxi-dev libxrandr-dev libxrender-dev

2. 配置
-----------------------------------

1) 解压源代码 qt-everywhere-opensource-src-5.4.1.tar.gz，并进入源代码文件夹

.. code-block:: bash

    tar xzf qt-everywhere-opensource-src-5.4.1.tar.gz
    cd qt-everywhere-opensource-src-5.4.1/

2) 指定所用平台的 arm 架构以及交叉编译器：

   ``vi qtbase/mkspecs/linux-arm-gnueabi-g++/qmake.conf``

改成以下内容，实际应需要根据自己的开发环境作出相应改变：

.. code-block:: python

    #
    # qmake configuration for building with arm-linux-gnueabi-g++
    #

    MAKEFILE_GENERATOR = UNIX
    CONFIG += incremental
    QMAKE_INCREMENTAL_STYLE = sublib
    QT_QPA_DEFAULT_PLATFORM = linuxfb
    QMAKE_CFLAGS_RELEASE += -O2 -march=armv7-a
    QMAKE_CXXFLAGS_RELEASE += -O2 -march=armv7-a
    include(../common/linux.conf)
    include(../common/gcc-base-unix.conf)
    include(../common/g++-unix.conf)
    QMAKE_INCDIR += /usr/local/tslib/include
    QMAKE_LIBDIR += /usr/local/tslib/lib
    执行modifications to g++.conf
    QMAKE_CC = arm-linux-gnueabihf-gcc -lts
    QMAKE_CXX = arm-linux-gnueabihf-g++ -lts
    QMAKE_LINK = arm-linux-gnueabihf-g++ -lts
    QMAKE_LINK_SHLIB = arm-linux-gnueabihf-g++ -lts
    执行modifications to linux.conf
    QMAKE_AR = arm-linux-gnueabihf-ar cqs
    QMAKE_OBJCOPY = arm-linux-gnueabihf-objcopy
    QMAKE_NM = arm-linux-gnueabihf-nm -P
    QMAKE_STRIP = arm-linux-gnueabihf-strip
    load(qt_config)

3) 根据自己的实际需求配置 Qt（此处是使用 tslib 的编译）：

.. code-block:: python

    ./configure \
    -prefix /usr/local/qt5.4.1 \
    -confirm-license \
    -opensource \
    -release \
    -make libs \
    -xplatform linux-arm-gnueabi-g++ \
    -optimized-qmake \
    -pch \
    -qt-sql-sqlite \
    -qt-libjpeg \
    -qt-libpng \
    -qt-zlib \
    -tslib \
    -no-opengl \
    -no-sse2 \
    -no-openssl \
    -no-nis \
    -no-cups \
    -no-glib \
    -no-dbus \
    -no-xcb \
    -no-xcursor -no-xfixes -no-xrandr -no-xrender \
    -no-separate-debug-info \
    -make examples -nomake tools -nomake tests -no-iconv

3. 编译安装
-----------------------------------

   ``sudo make && make install``

4. 移植 Qt 到 licheepi 开发板
-----------------------------------

完成上述步骤后， qt5.4.1 将被安装到 **/usr/local/qt5.4.1** 中。然后将/usr/local/中的 qt5.4.1 复制到开发板的
/opt/目录中，将/usr/local/中的 tslib 复制到开发板的/usr/local/中。

5. 设置开发板 Qt 环境变量：
-----------------------------------

   ``vi /etc/bash.bashrc``

添加下面内容：

.. code-block:: bash    

    export TSLIB_CONSOLEDEVICE=none
    export TSLIB_FBDEVICE=/dev/fb0
    export TSLIB_TSDEVICE=/dev/input/event1
    export TSLIB_CONFFILE=/usr/local/tslib/etc/ts.conf
    export TSLIB_PLUGINDIR=/usr/local/tslib/lib/ts
    export TSLIB_CALIBFILE=/etc/pointercal
    export LD_LIBRARY_PATH=/lib:/usr/lib:/usr/local/tslib/lib:/opt/qt5.4.1/lib
    export PATH=/bin:/sbin:/usr/bin/:/usr/sbin:/usr/local/tslib/bin
    export QT_QPA_PLATFORM_PLUGIN_PATH=/opt/qt5.4.1/plugins
    export QT_QPA_PLATFORM=linuxfb:tty=/dev/fb0
    export QT_QPA_FONTDIR=/opt/qt5.4.1/lib/fonts
    export QT_QPA_GENERIC_PLUGINS=tslib:$TSLIB_TSDEVICE

保存退出后使上面的环境变量生效：

  ``source /etc/bash.bashrc``

6. 运行一些 example：
-----------------------------------

.. code-block:: bash

   /opt/qt5.4.1/examples/touch/pinchzoom/pinchzoom
   /opt/qt5.4.1/examples/svg/embedded/fluidlauncher/fluidlauncher

我们可以看到用 linuxfb 方式的运行的 QT 是没有窗体边框的，这是 qt5 的一个特点，似乎是其为了更好的转移到手机等移动终端。

测试程序时候可能会提示某些库文件不存在，可以拷贝 ubuntu 主机中的交叉编译器下相应的库文件到 licheepi 开发板，然后添加环境变量是之生效。 不知道的话就都拷过去吧。

