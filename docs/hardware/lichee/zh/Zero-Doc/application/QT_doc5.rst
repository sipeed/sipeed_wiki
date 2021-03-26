Qt5.x移植到Qt4.8
===================================

.. contents:: 本文目录

在使用Qt5.x之后，发现Qt5.x还是比Qt4.8臃肿很多，所以在空间受限的设备上，还是建议使用Qt4.8.

这里记录Qt5.x的程序移植到Qt4.8上会遇到的一些问题。

QtSerialPort 移植
-----------------------------------

QtSerialPort是Qt5.3之后自带的，所以在Qt4.8上我们需要手工安装。

Qt串口模块5.5开始不再支持Qt4，所以建议用最后一个版本，*qtserialport-opensource-src-5.4.2*

pro里加上CONFIG += serialport

在这里下载： https://pan.baidu.com/s/1o6UVlk2

解压，打开其中的工程
   
   http://pkgs.fedoraproject.org/repo/pkgs/udev/udev-182.tar.xz/d0a1ac9501d7c4ae68839d1b601592b8/udev-182.tar.xz

.. code-block:: bash

    sudo apt-get install libblkid-dev libkmod-dev libgirepository1.0-dev

    ./configure --prefix=/opt/qt4.8.7-arm/ --target=arm-linux-gnueabihf --host=arm-linux-gnueabihf LD=arm-linux-gnueabihf-ld --with-pci-ids-path=/var/share/pci.ids

线程延时
----------------------------------

QThread::msleep(100);

线程延时100ms改成：

.. code-block:: cpp

    QEventLoop eventloop;
    QTimer::singleShot(100, &eventloop, SLOT(quit()));
    eventloop.exec();

中文乱码
----------------------------------

在最前面加上：

.. code-block:: cpp

    QTextCodec *codec = QTextCodec::codecForName("UTF-8");
    QTextCodec::setCodecForTr(codec);
    QTextCodec::setCodecForLocale(codec);
    QTextCodec::setCodecForCStrings(codec);

C++11
----------------------------------

:: 

    /home/zepan/develop/Second/wifiscanthread.h:16: warning: non-static data member initializers only available with -std=c++11 or -std=gnu++11
        bool stopped = false;
                        ^~~~~

无法打开显示设备
----------------------------------

.. code-block:: bash

    root@LicheePi:~# ./Second4.8 
    QWSSocket::connectToLocalFile could not connect:: Connection refused
    QWSSocket::connectToLocalFile could not connect:: Connection refused
    ^C
    root@LicheePi:~#./Second4.8 -qws
    QLock::QLock: Cannot create semaphore /tmp/qtembedded-0/QtEmbedded-0 'd' (38, Function not implemented)
    Cannot get display lock
    Aborted

最近查看Qt源码才发现，Qt需要用到System V IPC进行进程间通信，而Android的进程间通信用的是谷歌自己的方式，所以Qt根本无法实现进程间的通信，自然无法正常启动。

重新配置内核，打开 System V IPC选项，问题解决。

参考文章
----------------------------------

http://blog.csdn.net/yuyu414/article/details/42400721
