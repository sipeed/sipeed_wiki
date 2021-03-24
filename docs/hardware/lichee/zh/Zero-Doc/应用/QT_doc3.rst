移植QT4.8.7
===================================

.. contents:: 本文目录

之前移植了QT5.9.1，这里移植QT4.8.7就简单介绍下

下载QT4.8.7
-----------------------------------

.. code-block:: bash

    wget http://download.qt.io/official_releases/qt/4.8/4.8.7/qt-everywhere-opensource-src-4.8.7.tar.gz
    tar xf qt-everywhere-opensource-src-4.8.7.tar.gz
    cd qt-everywhere-opensource-src-4.8.7
    ./configure --help >help.txt   #QT的配置较为复杂，进来先看看帮助文档，在本节最后附录里有翻译

一般来说，我们需要编译主机和目标板两个版本的qt：

主机版可以用于前期的gui的设计调试；目标板用于实际产品的验证。

编译X11版本
------------------------------------

主机版一般是X11，配置如下：

.. code-block:: bash
   :caption: cfg_X11.sh
    
    #!/bin/bash
    ./configure -prefix /opt/qt-4.8.7-x11 -opensource -make tools   
    #安装位置，开源版本，编译qt工具（makeqpf,qtconfig）
    make -j32		#约10分钟
    sudo make install

安装完成后在 */opt/qt-4.8.7-x11* 下可见安装的文件。


交叉编译arm版本
----------------------------------------

注意，在第二次编译前，先 ``make clean`` 下。如果编译时候仍有错误，可以重新解压编译。

交叉编译，需要配置 xplatform选项，比如要在arm-linux平台上移植Qt的话，就在配置项中加上 **-xplatform linux-arm-gnueabi-g++** ，这个是平台名字，Qt5支持的交叉平台都可在源码顶层目录中的 mkspecs/ 下找到。

首先我们需要编辑 *mkspecs/qws/linux-arm-gnueabi-g++/qmake.conf* ：

加上：（注意，和tslib类似，这里要加上其它什么支持的话，也是交叉编译的库的路径）

.. code-block:: bash

    QT_QPA_DEFAULT_PLATFORM = linuxfb
    QMAKE_CFLAGS_RELEASE += -O2 -march=armv7-a -lts
    QMAKE_CXXFLAGS_RELEASE += -O2 -march=armv7-a -lts
    QMAKE_INCDIR += /opt/tslib/include /opt/sqlite3/include
    QMAKE_LIBDIR += /opt/tslib/lib /opt/sqlite3/lib


把 *arm-linux-gnueabihf-gcc* 改成 *arm-linux-gnueabi-gcc* 等。

然后再编辑配置脚本cfg_arm.sh

.. code-block:: bash

    #/bin/sh
    ./configure -verbose \
    -opensource \
    -confirm-license \
    -release -shared \
    -embedded arm \
    -xplatform qws/linux-arm-gnueabi-g++ \
    -depths 4,8,16,32 \
    -fast \
    -optimized-qmake \
    -pch \
    -qt-sql-sqlite \
    -qt-libjpeg \
    -qt-zlib \
    -qt-libpng \
    -qt-freetype \
    -little-endian -host-little-endian \
    -no-qt3support \
    -no-libtiff -no-libmng \
    -no-opengl \
    -no-mmx -no-sse -no-sse2 \
    -no-3dnow \
    -no-openssl \
    -no-webkit \
    -no-qvfb \
    -no-phonon \
    -no-nis \
    -no-opengl \
    -no-cups \
    -no-glib \
    -qt-gfx-transformed \
    -no-xcursor -no-xfixes -no-xrandr -no-xrender \
    -no-separate-debug-info \
    -nomake examples -make tools -make docs \
    -qt-mouse-tslib -I/opt/tslib/include -L/opt/tslib/lib

    make -j32
    sudo make install

完成后，相关文件在 */opt/qt4.8.7-arm* 下。

常见编译错误
--------------------------------

配置QT的时候，如果指定了-webkit，编译的时候会报错：

   ../3rdparty\javascriptcore\JavaScriptCore/wtf/TypeTraits.h:173:69:error: 'std::tr1' has not been declared

解决方法：
   
   修改QT源码目录下mkspecs/qws/linux-arm-gnueabi-g++/qmake.conf文件，加上一行：QMAKE_CXXFLAGS = $$QMAKE_CFLAGS -std=gnu++98

>>> /opt/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf/bin/../lib/gcc/arm-linux-gnueabihf/6.3.1/../../../../arm-linux-gnueabihf/bin/ld: warning: libts.so.0, needed by /home/wcz/qt-everywhere-opensource-src-4.8.7_arm/lib/libQtGui.so, not found (try using -rpath or -rpath-link)

提示没有tslib的库，当然了，提示中也清楚的说了(try using -rpath or -rpath-link)。

我们可以：
   
   1. 进入到编译报错的目录，在这里是“examples/network/broadcastreceiver“
   2. 修改这个目录中的Makefile文件，找到LFLAGS一行，在最后面加上”-Wl,-rpath,/opt/tslib/lib“，也就是手动指定tslib的目录。（这里还没清楚为何configure时的参数没起作用）
   3. 就地make
   4. 退回到主目录
   5. 继续make

上面的操作，如果每个Makefile都要编辑一遍的话，那就太麻烦了，我们偷偷懒。

针对Makefile的LFLAGS一行的特点，我们使用 *find、grep、awk、sed、xargs* 来完成这个操作，如下：

进入到出错目录的顶层，如上示例，我们进入到examples。

   ``cd examples``

   ``find . -name Makefile | xargs grep rpath-link | grep -v tslib | awk -F: '{fname[NR]=$1} END {for (i=1;i<=NR;i++){print fname[i]}}' | xargs sed -i 's/LFLAGS.*/& -Wl,-rpath,\/opt\/tslib\/lib/'``

<注意，这个命令会直接修改目录中最底层的每一个Makefile，请试验成功后再使用。>

向开发板添加Qt库
--------------------------------------

首先将 */opt/qt5.9.1-arm和/opt/tslib* 复制到开发板的对应目录下

然后设置开发板 Qt 环境变量， ``vi /etc/bash.bashrc``

添加下面内容：

.. code-block:: bash

    export TSLIB_CONSOLEDEVICE=none
    export TSLIB_FBDEVICE=/dev/fb0
    export TSLIB_TSDEVICE=/dev/input/event1
    export TSLIB_CONFFILE=/opt/tslib/etc/ts.conf
    export TSLIB_PLUGINDIR=/opt/tslib/lib/ts
    export TSLIB_CALIBFILE=/etc/pointercal
    export LD_LIBRARY_PATH=/lib:/usr/lib:/opt/tslib/lib:/opt/qt5.9.1-arm/lib
    export PATH=/bin:/sbin:/usr/bin/:/usr/sbin:/opt/tslib/bin
    export QT_QPA_PLATFORM_PLUGIN_PATH=/opt/qt5.9.1-arm/plugins
    export QT_QPA_PLATFORM=linuxfb:tty=/dev/fb0
    export QT_QPA_FONTDIR=/opt/qt5.9.1-arm/lib/fonts
    export QT_QPA_GENERIC_PLUGINS=tslib:$TSLIB_TSDEVICE
    export QWS_MOUSE_PROTO=Tslib:/dev/input/event0
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/optslib/lib:/opt/qt5.9.1-arm/lib:/usr/lib/arm-linux-gnueabihf/lib

保存后生效上述内容： ``source /etc/bash.bashrc``

br生成的文件系统则为：

.. code-block:: bash

    export TSLIB_CONSOLEDEVICE=none
    export TSLIB_FBDEVICE=/dev/fb0
    export TSLIB_TSDEVICE=/dev/input/event1
    export TSLIB_CONFFILE=/etc/ts.conf
    export TSLIB_PLUGINDIR=/usr/lib/ts
    export TSLIB_CALIBFILE=/etc/pointercal
    export LD_LIBRARY_PATH=/lib:/usr/lib
    export PATH=/bin:/sbin:/usr/bin/:/usr/sbin
    export QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/qt/plugins
    export QT_QPA_PLATFORM=linuxfb:tty=/dev/fb0
    export QT_QPA_FONTDIR=/usr/lib/qt/lib/fonts
    export QT_QPA_GENERIC_PLUGINS=tslib:$TSLIB_TSDEVICE
    export QWS_MOUSE_PROTO=Tslib:/dev/input/event1

参考资料
-----------------------------------

http://blog.csdn.net/armfpga123/article/details/52921558

http://blog.chinaunix.net/uid-29962009-id-5012060.html
