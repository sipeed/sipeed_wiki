Qt字体相关
===================================

.. contents:: 本文目录

支持的字体
-----------------------------------

嵌入式Qt支持4中格式的字体，分别是：
   1. TrueType(TTF) 可缩放字体格式，桌面系统中主要使用的字体
   2. PostscripType(PFA/PFB) 可缩放字体格式，打印主要使用的字体，可TTF类似
   3. **Bitmap Distribution Format fonts (BDF) ** 不可缩放字体的标准格式，在X11平台系统中可以找到
   4. Qt Prerendered Font (QPF) Qt预渲染字体，专用于嵌入式Qt的一种字体格式

QPF字体格式是嵌入式Qt内置支持的字体，可以使用QT SDK中提供的makeqpf工具利用前三种字体文件来生成。

而其它的字体格式是否支持则是可以进行裁剪定制的，可以去掉对TTF、BDF字体的支持以降低Qt库的空间占用，通过定义下面的Qt特性宏：

.. code-block:: bash

    /*
    TrueType (TTF and TTC) font file format, only used by Qt/Embedded.
    */
    #define QT_NO_TRUETYPE	 

    /*
    Bitmap Distribution Format (BDF) font file format, only used by Qt/Embedded.
    */
    #define QT_NO_BDF

当然，不定义这两个宏则表示支持TTF、BDF字体。

因为QPF是预渲染的，嵌入式Qt使用它时不需要读取和解析它，只需要进行简单快速的映射，因此它对内存的消耗是最小的。

因此一种方法是利用TTF和BDF字体文件制作好需要的QPF字体文件，然后移除对两者的支持。

TTF、PFA和QPF字体都支持字体的反锯齿，即使字体尽量显示的圆滑而不会有锯齿感，从而提供更好的可读性和观感，特别是在低分辨率设备上，但是这是以消耗更多的内存和空间为代价的，大概是不反锯齿的八倍。

对于所有的字体文件，嵌入式Qt都是使用Unicode编码的格式。

使用字体文件
------------------------------------

当Qt应用运行时，它会到以下两个目标之一去寻找规定的字体定义文件fontdir：

.. code-block:: bash

    $QTDIR/lib/fonts/fontdir    QTDIR是一般使用Qte都会定义的环境变量
    /usr/local/qt-embedded/lib/fonts/fontdir  可能是默认的qt安装路径

fontdir文件定义了Qt应用可以使用的字体格式、大小和文件等内容。fontdir文件的内容和字体条目定义的格式可以参考如下的示例文件，文件中有相应的说明：

一个典型的FONTDIR文件的内容如下所示：

:: 

    fixed fixed_120_50.qpf QPF n 50 120
    helvetica helvetica_80_50.qpf QPF n 50 80
    helvetica helvetica_120_50.qpf QPF n 50 120 u
    helvetica helvetica_120_75.qpf QPF n 75 120 u
    helvetica helvetica_140_75.qpf QPF n 75 140
    helvetica helvetica_180_75.qpf QPF n 75 180

文件中每行都标识一个特定的字库，每个段的含义是：

:: 

    第一列为name，
    第二列为file，
    第三列为renderer，相当于字型格式，所以有BDF，TTT，QPF等选择。
    第四列n表示iitalic，表示是否为斜体字。
    第五列表示weight，其中50表示Normal，75表示Bold。
    第六列表示size，例如：120表示12pt。
    第七列为flags，有下面三个选择：
        s=smooth(anti-aliased)
        u =unicode range when saving 
            (default is Latin 1 a = ASCII range when saving(default is Latin 1))

你可以在文件中添加其它的字体格式条目，前提是你有相应的字体文件，不然加了也没用。

关于文件中的渲染引擎renderer
---------------------------------------------

上面也提到了，renderer只能是BDF或者FT，BDF对应BDF字体文件，而FT是FreeType的缩写，FreeType是一个强大的库用来实现渲染TTF/TTC和PFA字体，在嵌入式QT库的编译配置时可以选择是否支持。
注意到没有QPF渲染引擎的说法，这是因为QPF字体文件的使用是不需要在fontdir文件中定义的，只需要将QPF字体文件放到和fontdir文件同一级目录下就可以，但是QPF字体文件的命名必须符合Qte的规范：

::

    name_size_weightitalicflag.qpf

    e.g:
        wenquanyi_160_75.qpf   16pt文泉驿粗体，不支持斜体
        wenquanyi_160_50i.qpf  16pt文泉驿正常，支持斜体

关于文件中的字体大小size
---------------------------------------------

size的大小是字体大小*10，也就是12pt字体的size是120，但是我对pt这个单位没有什么概念，所以我特意查找对比了一下字体大小的单位表示，整理如下：

- 小五号:9pt, 五号:10.5pt, 小四号:12pt
- 四号:13.75pt(磅), 三号:15.75pt(磅), 二号:21pt
- 中文最小字号:八号;2.83pt = 1mm, 28.3pt = 1cm = 一号字体(27.5pt)

字体大小对应的点阵:

- 9pt:1212(96dpi),1515(120dpi);
- 12pt: 1515(96dpi),1919(120dpi)

不过在实际的嵌入式设备上显示时好像和这种字体大小在word上的显示不太一致，如前面的16pt文泉驿字体在设备上显示的大小感觉和word中的小四号字体差不多大。

关于中文字体支持
--------------------------------------------

步入重点，如果需要支持中文字体，显然就需要有对应的中文字体文件。

前面提到的unifont.bdf文件和文泉驿字体文件都是可以支持中文的，也可以从对应的网站上下载到官方的字体文件。

而文泉驿字体在Linux系统X11平台上也是使用的比较多的，所以可以直接取用。

关于QPF字体文件生成的捷径
--------------------------------------------

前面提到可以使用makeqpf工具通过TTF、BDF字体文件来生成QPF字体文件，这就需要编译makeqpf工具，然后自己一个个去进行相应的转换，你还可能不确定会使用到哪些字体。

另一种更方便快捷的方法是让Qt应用自动完成需要使用字体的QPF生成，方法就是在运行Qt应用时，加上 -savefonts 选项。此时应用会将所有使用到的非QPF字体自动转换生成QPF字体文件并保存下来。

然后你就可以去掉TTF、BDF支持，支持使用QPF字体文件进行部署了。

参考资料
--------------------------------------------

http://doc.qt.io/qt-5/qt-embedded-fonts.html
