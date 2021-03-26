Qt裁剪
===================================

.. contents:: 本文目录

默认编译出来的Qt库是很大的，有几十M，甚至上百M。

为了将Qt库放入小容量的SPI flash中，我们需要去除不必要的库，裁剪必要的库。

去除不必要的库
-----------------------------------

裁剪feature
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:: 

    ./src/corelib/global/qfeatures.h
    ./configure -qconfig myfile

针对嵌入式版本的配置
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Qt的嵌入式版本本身就支持feature裁剪，我们可以充分利用这一特性让Qt库尽量变小。具体的做法是要做一个自己的 *qconfig-[myconfig].h* 特性文件，该文件中定义你要去掉Qt中的哪些feature。在configure的时候加“ *-qconfig myconfig* ” 选项， Qt就会根据你给出的配置文件来编译，以达到裁剪的目的。这里要强调一下，这种裁剪方式只适用于嵌入式版本。这里的myconfig可以用任何你喜欢的名字来代替。

在qt的代码中已经给出了一些qconfig头文件的例子，默认编译采用full config也就是

不裁剪任何feature。所有Qt预定义好的qconfig文件，可以在 *src/corelib/global/* 下找到，包括 *qconfig-minimal.h, qconfig-small.h, qconfig.medium.h,qconfig-large.h和qconfig-dist.h*，也就是从裁剪量由多到少都有据可依。如果要添加你自己的配置文件，要在 *src/corelib/global* 下建立一个形如qconfig-xxx.h的文件，这个xxx也就是你要在configure的时候传入的qconfig参数。

笔者测试使用的Qt版本是4.4.1，这个版本的build system有个小毛病，就是如果你指定的qconfig参数实际上没有 *qconfig-xxx.h* 文件对应， build不会停止，它只会给出一个不起眼的提示，编译过程会继续， 这一点挺让人费解的。而且这种情况下Qt编译使用的配置基本上和fullconfig相同，鉴于它的让人迷惑的举动，个人觉得有必要提醒大家一下，使用自定义qconfig的时候一定要确定配置文件放对了位置，而且qconfig参数给的正确。

一般我们的建议是在桌面上测试阶段编译一个full的版本，再根据你的项目使用Qt feature的情况总结哪些可去掉的feature。 feature之间有千丝万缕的依赖关系，这个问题也是困扰很多人的难点所在。具体的依赖可以查阅 *src/corelib/global/qfeatures.h* 和 *src/corelib/global/qfeatures.txt* （描述依赖关系的文档）。另外，Qt里还提供了一个可视化的配置依赖的工具，叫做qconfig，在 *QTDIR/tools/qconfig* 目录。该工具需要基于Qt桌面版本编译。

如在我的linux系统下可以用下面的命令来编译：

.. code-block:: bash

    cd qt-embedded-linux-commercial-4.4.1/tools/qconfig
    /usr/local/Trolltech/Qt-4.4.3/bin/qmake
    make

编译成功后运行 ``./qconfig``，初始要打开qfeatures.txt. Qconfig读取该文件生成一个树状图，该图很清楚的显示出feature之间的依赖关系。如下图所示，如果你去掉了LINEEDIT这个feature，用到该控件的combobox也就不能继续使用了。有了这个工具裁剪Qt变得简洁直观，方便了很多。

选定了你要去掉的feature后点击菜单 :menuselection:`File --> Save As..` 会弹出保存文件的页面，文件名字应该定义成 *qconfig-xxx.h* 的形式，这样你在configure的时候就可以传入相应的qconfig参数了。

你还可以通过选择 :menuselection:`File --> Open` 打开现有的 *qconfig-xxx.h* 文件，通过修改已经有的文件更快的编辑配置。

根据笔者测试，未经裁剪的qte4.4.1编译出来为：

:: 

    libQtCore.so是2.6M  
    libQtGui.so是9.5M 

如果用small来编译，就能缩小为：

:: 

    libQtCore.so是2.0M  
    libQtGui.so是5.7M 

差异还是比较明显的。

使用静态编译
------------------------------------

- 在编译Qt库时使用 *-static* 选项
- 重新编译qtserial等库，并install
- 在pro里加上 ``QT += core gui sql serialport``
- 程序改为release

实测减少有限
