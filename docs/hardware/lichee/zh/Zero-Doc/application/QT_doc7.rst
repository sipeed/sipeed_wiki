Qt移植总结
===================================

.. contents:: 本文目录

PC端步骤
-----------------------------------

交叉编译好qt-everywhere,内含关键的qmake

qmake用于配置qtcreator

目标板步骤
-----------------------------------

1. 拷贝qt5.9.1-arm， sqlite3，tslib（内含ts_calibrate） 到/opt下
2. 拷贝字体到/opt/qt5.9.1-arm/lib/fonts下
3. 之前交叉编译qt的工具链里的/usr/lib/arm-linux-gnueabihf/lib/libstdc++.so.6.0.22 覆盖当前的so
4. 编辑/etc/bash.bashrc， 加入环境变量：

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
5. 拷贝编译好的基于qt的应用程序到自定义目录下
