移植QT5.9.1
===================================

.. contents:: 本文目录

移植完成tslib之后，就可以进行QT本体的移植了，目前最新版本为5.9.1。

注意QT本体编译时间较长，笔记本上会耗时2~3小时，我使用的32线程服务器的编译时间为9分钟左右。

下载QT5.9.1
-----------------------------------

.. code-block:: bash

    wget http://download.qt.io/official_releases/qt/5.9/5.9.1/single/qt-everywhere-opensource-src-5.9.1.tar.xz
    tar xf qt-everywhere-opensource-src-5.9.1.tar.xz	#这里解压也需要30s左右，别以为死机了。。
    cd qt-everywhere-opensource-src-5.9.1
    ./configure --help >help.txt   #QT的配置较为复杂，进来先看看帮助文档，在本节最后附录里有翻译

一般来说，我们需要编译主机和目标板两个版本的qt：
   
   主机版可以用于前期的gui的设计调试；目标板用于实际产品的验证。

编译X11版本
------------------------------------

主机版一般是X11，配置如下：

.. code-block:: bash
   :caption: cfg_X11.sh

    #!/bin/bash
    ./configure -prefix /opt/qt-5.9.1-x11 -opensource -make tools   
    #安装位置，开源版本，编译qt工具（makeqpf,qtconfig）
    make -j32
    sudo make install

运行该脚本，首次配置用时1分钟左右。编译一次参考时间：

:: 

    real	9m17.309s
    user	206m59.052s
    sys	17m30.300s

所以单核虚拟机编译需要三小时左右。

编译完成后install也需要1分钟左右。

安装完成后在/opt/qt-5.9.1-x11下可见安装的文件。

交叉编译arm版本
------------------------------------

注意，在第二次编译前，先 ``make clean`` 下。如果编译时候仍有错误，可以重新解压编译。

交叉编译，需要配置 xplatform选项，比如要在arm-linux平台上移植Qt的话，就在配置项中加上 ``-xplatform linux-arm-gnueabi-g++`` ，这个是平台名字，Qt5支持的交叉平台都可在源码顶层目录中的 */qtbase/mkspecs/* 下找到。

首先我们需要编辑 *qtbase/mkspecs/linux-arm-gnueabi-g++/qmake.conf*：

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

    #!/bin/sh
    ./configure -verbose \
    -prefix /opt/qt5.9.1-arm \
    -confirm-license \
    -opensource \
    -release \
    -make libs \
    -xplatform linux-arm-gnueabi-g++ \
    -optimized-qmake \
    -pch \
    -sql-sqlite -sqlite \
    -qt-libjpeg \
    -qt-libpng \
    -qt-zlib \
    -tslib \
    -no-opengl \
    -no-sse2 \
    -no-openssl \
    -no-cups \
    -no-glib \
    -no-dbus \
    -no-xcb \
    -no-separate-debug-info \
    -I/opt/tslib/include -L/opt/tslib/lib \
    -make examples -make tools -nomake tests -no-iconv
    
.. code-block:: bash

    make -j32
    sudo make install

完成后，相关文件在 */opt/qt5.9.1-arm* 下。

向开发板添加Qt库
---------------------------------------------

首先将 */opt/qt5.9.1-arm* 和 */opt/tslib* 复制到开发板的对应目录下

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

保存后生效上述内容： ``source /etc/bash.bashrc``

参考资料
----------------------------------

http://blog.csdn.net/newthinker_wei/article/details/39560109

http://www.linuxidc.com/Linux/2014-03/98079.htm

附录：QT配置帮助文件 翻译
------------------------------------

Usage: configure [options] [assignments]

在命令行使用VAR=value来配置变量。

每个大写的库名（用-list-libraries可以查看），支持这些后缀：

:: 

    _INCDIR, _LIBDIR, _PREFIX (INCDIR=PREFIX/include, LIBDIR=PREFIX/lib),
    _LIBS, and - on Windows and Darwin - _LIBS_DEBUG and _LIBS_RELEASE. E.g.,
    ICU_PREFIX=/opt/icu42 ICU_LIBS="-licui18n -licuuc -licudata".

同时支持操作 QMAKE_* 变量，来修改mkspec里指定的值，比如QMAKE_CXXFLAGS+=-g3.

**顶层安装路径：**

:: 

    -prefix ...... 目标路径（在开发板上的绝对路径）
    [如果使能了developer-build，就是/usr/local/Qt-$QT_VERSION, $PWD]
    -extprefix ... 安装路径（在主机上的路径，比prefix更多一个前置路径），可不写
    [SYSROOT/PREFIX]
    -hostprefix [dir] .. The installation directory for build tools running on
    the host machine. If [dir] is not given, the current
    build directory will be used. [EXTPREFIX]
    -external-hostbindir ... Path to Qt tools built for this machine.
    Use this when -platform does not match the current
    system, i.e., to make a Canadian Cross Build.

**微调安装路径的分布** ，注意除了-sysconfdir外的所有目录需要在 *-prefix/-hostprefix* 下。

（这里基本可以不配置）

:: 

    -bindir ......... Executables [PREFIX/bin]
    -headerdir ...... Header files [PREFIX/include]
    -libdir ......... Libraries [PREFIX/lib]
    -archdatadir .... Arch-dependent data [PREFIX]
    -plugindir ...... Plugins [ARCHDATADIR/plugins]
    -libexecdir ..... Helper programs [ARCHDATADIR/bin on Windows,
    ARCHDATADIR/libexec otherwise]
    -importdir ...... QML1 imports [ARCHDATADIR/imports]
    -qmldir ......... QML2 imports [ARCHDATADIR/qml]
    -datadir ........ Arch-independent data [PREFIX]
    -docdir ......... Documentation [DATADIR/doc]
    -translationdir . Translations [DATADIR/translations]
    -sysconfdir ..... Settings used by Qt programs [PREFIX/etc/xdg]
    -examplesdir .... Examples [PREFIX/examples]
    -testsdir ....... Tests [PREFIX/tests]

    -hostbindir ..... Host executables [HOSTPREFIX/bin]
    -hostlibdir ..... Host libraries [HOSTPREFIX/lib]
    -hostdatadir .... Data used by qmake [HOSTPREFIX]

**对剩余的选项的约定：**

:: 

    当一个选项描述符在一系列方括号内的变量之后，这个选项的解释是：
    空选项表示yes； 所有其他值是可能的前缀，比如-no-gui.
    Values are listed in the order they are tried if not specified;
    'auto' 是 'yes/no'的简写. 单个 'yes' 和 'no' 表示没有自动检测的二进制选项。

**可配置的meta：**

:: 

    -help, -h ............ Display this help screen
    -verbose, -v ......... Print verbose messages during configuration
    -continue ............ Continue configure despite errors
    -redo ................ Re-configure with previously used options.
    Additional options may be passed, but will not be
    saved for later use by -redo.
    -recheck ............. Discard cached negative configure test results.
    Use this after installing missing dependencies.
    -recheck-all ......... Discard all cached configure test results.
    -feature- ... Enable 
    -no-feature- Disable [none]
    -list-features ....... List available features. Note that some features
    have dedicated command line options as well.

    -list-libraries ...... List possible external dependencies.

**构建选项：**

:: 

    -opensource .......... Build the Open-Source Edition of Qt
    -commercial .......... Build the Commercial Edition of Qt
    -confirm-license ..... Automatically acknowledge the license
    -release ............. Build Qt with debugging turned off [yes]
    -debug ............... Build Qt with debugging turned on [no]
    -debug-and-release ... Build two versions of Qt, with and without
    debugging turned on [yes] (Apple and Windows only)
    -optimize-debug ...... Enable debug-friendly optimizations in debug builds
    [auto] (Not supported with MSVC)
    -optimize-size ....... Optimize release builds for size instead of speed [no]
    -optimized-tools ..... Build optimized host tools even in debug build [no]
    -force-debug-info .... Create symbol files for release builds [no]
    -separate-debug-info . Split off debug information to separate files [no]
    -strip ............... Strip release binaries of unneeded symbols [yes]
    -force-asserts ....... Enable Q_ASSERT even in release builds [no]
    -developer-build ..... Compile and link Qt for developing Qt itself
    (exports for auto-tests, extra checks, etc.) [no]
    -shared .............. Build shared Qt libraries [yes] (no for UIKit)
    -static .............. Build static Qt libraries [no] (yes for UIKit)
    -framework ........... Build Qt framework bundles [yes] (Apple only)
    -platform ... Select host mkspec [detected]
    -xplatform .. Select target mkspec when cross-compiling [PLATFORM]
    -device ....... Cross-compile for device 
    -device-option <key=value> ... Add option for the device mkspec

    -appstore-compliant .. Disable code that is not allowed in platform app stores.
    This is on by default for platforms which require distribution
    through an app store by default, in particular Android,
    iOS, tvOS, watchOS, and Universal Windows Platform. [auto]
    -qtnamespace .. Wrap all Qt library code in 'namespace {...}'.
    -qtlibinfix .. Rename all libQt5*.so to libQt5*.so.

    -testcocoon .......... Instrument with the TestCocoon code coverage tool [no]
    -gcov ................ Instrument with the GCov code coverage tool [no]
    -sanitize {address|thread|memory|undefined}
    Instrument with the specified compiler sanitizer.
    -c++std .... Select C++ standard [c++1z/c++14/c++11]
    (Not supported with MSVC)

    -sse2 ................ Use SSE2 instructions [auto]
    -sse3/-ssse3/-sse4.1/-sse4.2/-avx/-avx2/-avx512
    Enable use of particular x86 instructions [auto]
    Enabled ones are still subject to runtime detection.
    -mips_dsp/-mips_dspr2 Use MIPS DSP/rev2 instructions [auto]
    -qreal ........ typedef qreal to the specified type. [double]
    Note: this affects binary compatibility.

    -R .......... Add an explicit runtime library path to the Qt
    libraries. Supports paths relative to LIBDIR.
    -rpath ............... Link Qt libraries and executables using the library
    install path as a runtime library path. Similar to
    -R LIBDIR. On Apple platforms, disabling this implies
    using absolute install names (based in LIBDIR) for
    dynamic libraries and frameworks. [auto]

    -reduce-exports ...... Reduce amount of exported symbols [auto]
    -reduce-relocations .. Reduce amount of relocations [auto] (Unix only)
    -plugin-manifests .... Embed manifests into plugins [no] (Windows only)
    -static-runtime ...... With -static, use static runtime [no] (Windows only)
    -pch ................. Use precompiled headers [auto]
    -ltcg ................ Use Link Time Code Generation [no]
    -use-gold-linker ..... Use the GNU gold linker [auto]
    -incredibuild-xge .... Use the IncrediBuild XGE [no] (Windows only)
    -make-tool .... Use to build qmake [nmake] (Windows only)
    -mp .................. Use multiple processors for compilation (MSVC only)

    -warnings-are-errors . Treat warnings as errors [no; yes if -developer-build]
    -silent .............. Reduce the build output so that warnings and errors
    can be seen more easily

**构建环境：**

:: 

    -sysroot ....... Set as the target sysroot
    -gcc-sysroot ......... With -sysroot, pass --sysroot to the compiler [yes]

    -pkg-config .......... Use pkg-config [auto] (Unix only)

    -D .......... Pass additional preprocessor define
    -I .......... Pass additional include path
    -L .......... Pass additional library path
    -F .......... Pass additional framework path (Apple only)

    -sdk ........... Build Qt using Apple provided SDK . The argument
    should be one of the available SDKs as listed by
    'xcodebuild -showsdks'.
    Note that the argument applies only to Qt libraries
    and applications built using the target mkspec - not
    host tools such as qmake, moc, rcc, etc.

    -android-sdk path .... Set Android SDK root path [$ANDROID_SDK_ROOT]
    -android-ndk path .... Set Android NDK root path [$ANDROID_NDK_ROOT]
    -android-ndk-platform Set Android platform
    -android-ndk-host .... Set Android NDK host (linux-x86, linux-x86_64, etc.)
    [$ANDROID_NDK_HOST]
    -android-arch ........ Set Android architecture (armeabi, armeabi-v7a,
    arm64-v8a, x86, x86_64, mips, mips64)
    -android-toolchain-version ... Set Android toolchain version
    -android-style-assets Automatically extract style assets from the device at
    run time. This option makes the Android style behave
    correctly, but also makes the Android platform plugin
    incompatible with the LGPL2.1. [yes]

**组件选择**

:: 

    -skip ......... Exclude an entire repository from the build.
    -make ......... Add to the list of parts to be built.
    Specifying this option clears the default list first.
    [libs and examples, also tools if not cross-building,
    also tests if -developer-build]
    -nomake ....... Exclude from the list of parts to be built.
    -compile-examples .... When unset, install only the sources of examples [yes]
    -gui ................. Build the Qt GUI module and dependencies [yes]
    -widgets ............. Build the Qt Widgets module and dependencies [yes]
    -no-dbus ............. Do not build the Qt D-Bus module
    [default on Android and Windows]
    -dbus-linked ......... Build Qt D-Bus and link to libdbus-1 [auto]
    -dbus-runtime ........ Build Qt D-Bus and dynamically load libdbus-1 [no]
    -accessibility ....... Enable accessibility support [yes]
    Note: Disabling accessibility is not recommended.
    -qml-debug ........... Enable QML debugging support [yes]

    Qt comes with bundled copies of some 3rd party libraries. These are used
    by default if auto-detection of the respective system library fails.

**核心选项**

:: 

    -doubleconversion .... Select used double conversion library [system/qt/no]
    No implies use of sscanf_l and snprintf_l (imprecise).
    -glib ................ Enable Glib support [no; auto on Unix]
    -eventfd ............. Enable eventfd support
    -inotify ............. Enable inotify support
    -iconv ............... Enable iconv(3) support [posix/sun/gnu/no] (Unix only)
    -icu ................. Enable ICU support [auto]
    -pcre ................ Select used libpcre2 [system/qt]
    -pps ................. Enable PPS support [auto] (QNX only)
    -zlib ................ Select used zlib [system/qt]

**日志后端**

:: 

    -journald .......... Enable journald support [no] (Unix only)
    -syslog ............ Enable syslog support [no] (Unix only)
    -slog2 ............. Enable slog2 support [auto] (QNX only)

**网络选择**

:: 

    -ssl ................. Enable either SSL support method [auto]
    -no-openssl .......... Do not use OpenSSL [default on Apple and WinRT]
    -openssl-linked ...... Use OpenSSL and link to libssl [no]
    -openssl-runtime ..... Use OpenSSL and dynamically load libssl [auto]
    -securetransport ..... Use SecureTransport [auto] (Apple only)
    -sctp ................ Enable SCTP support [no]

    -libproxy ............ Enable use of libproxy [no]
    -system-proxies ...... Use system network proxies by default [yes]

**Gui, 打印, 挂件选择**

:: 

    -cups ................ Enable CUPS support [auto] (Unix only)

    -fontconfig .......... Enable Fontconfig support [auto] (Unix only)
    -freetype ............ Select used FreeType [system/qt/no]
    -harfbuzz ............ Select used HarfBuzz-NG [system/qt/no]
    (Not auto-detected on Apple and Windows)
    -gtk ................. Enable GTK platform theme support [auto]

    -lgmon ............... Enable lgmon support [auto] (QNX only)

    -no-opengl ........... Disable OpenGL support
    -opengl ........ Enable OpenGL support. Supported APIs:
    es2 (default on Windows), desktop (default on Unix),
    dynamic (Windows only)
    -opengles3 ........... Enable OpenGL ES 3.x support instead of ES 2.x [auto]
    -angle ............... Use bundled ANGLE to support OpenGL ES 2.0 [auto]
    (Windows only)
    -combined-angle-lib .. Merge LibEGL and LibGLESv2 into LibANGLE (Windows only)

    -qpa .......... Select default QPA backend (e.g., xcb, cocoa, windows)
    -xcb-xlib............. Enable Xcb-Xlib support [auto]

**平台后端：**

:: 

    -direct2d .......... Enable Direct2D support [auto] (Windows only)
    -directfb .......... Enable DirectFB support [no] (Unix only)
    -eglfs ............. Enable EGLFS support [auto; no on Android and Windows]
    -gbm ............... Enable backends for GBM [auto] (Linux only)
    -kms ............... Enable backends for KMS [auto] (Linux only)
    -linuxfb ........... Enable Linux Framebuffer support [auto] (Linux only)
    -mirclient ......... Enable Mir client support [no] (Linux only)
    -xcb ............... Select used xcb-* libraries [system/qt/no]
    (-qt-xcb still uses system version of libxcb itself)

**输入后端**

:: 

    -evdev ............. Enable evdev support [auto]
    -imf ............... Enable IMF support [auto] (QNX only)
    -libinput .......... Enable libinput support [auto]
    -mtdev ............. Enable mtdev support [auto]
    -tslib ............. Enable tslib support [auto]
    -xinput2 ........... Enable XInput2 support [auto]
    -xkbcommon-x11 ..... Select xkbcommon used in combination with xcb
    [system/qt/no]
    -xkb-config-root ... With -qt-xkbcommon-x11, set default XKB config
    root [detect]
    -xkbcommon-evdev ... Enable X-less xkbcommon in combination with libinput
    [auto]

**图像格式**

:: 

    -gif ............... Enable reading support for GIF [auto]
    -ico ............... Enable support for ICO [yes]
    -libpng ............ Select used libpng [system/qt/no]
    -libjpeg ........... Select used libjpeg [system/qt/no]

**数据库选项**

:: 

    -sql- ........ Enable SQL plugin. Supported drivers:
    db2 ibase mysql oci odbc psql sqlite2 sqlite tds
    [all auto]
    -sqlite .............. Select used sqlite3 [system/qt]

**Qt3D 选项**

:: 

    -assimp .............. Select used assimp library [system/qt/no]
    -qt3d-profile-jobs ... Enable jobs profiling [no]
    -qt3d-profile-gl ..... Enable OpenGL profiling [no]

**多媒体选项**

:: 

    -pulseaudio .......... Enable PulseAudio support [auto] (Unix only)
    -alsa ................ Enable ALSA support [auto] (Unix only)
    -no-gstreamer ........ Disable support for GStreamer
    -gstreamer [version] . Enable GStreamer support [auto]
    With no parameter, 1.0 is tried first, then 0.10.
    -mediaplayer-backend ... Select media player backend (Windows only)
    Supported backends: directshow (default), wmf
