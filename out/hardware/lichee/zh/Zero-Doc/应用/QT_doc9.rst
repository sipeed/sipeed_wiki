Qt去除鼠标指针显示
===================================

.. contents:: 本文目录

qt全屏显示
-----------------------------------

主要是设置setWindowFlags 可以这样使用全屏幕

.. code-block:: cpp

    yourwidget->setWindowFlags(Qt::window | Qt::FramelessWindowHint); //第一个Qt::window表示此widget是窗口类型，第二个参数使用无框架就是没有标题，状态栏等。具体参考
    $QTPATH/examples/widgets/windowflags/

Qt Embedded Linux下隐藏鼠标箭头
----------------------------------------------------

1. 编译Qt库的时候添加编译选项QT_NO_CURSOR，这样cursor相关的代码统统不会被编译进去，自然鼠标光标也不会出现在程序中。

   -no-mouse-tslib
2. 只希望在某个QWidget下不出现鼠标光标，则只要对这个widget调用

   ``QWidget::setCursor(QCursor(Qt::BlankCursor))``，其它的窗口仍将出现鼠标。
3.在main函数中，实例化了APPLICATION后，调用

   ``QApplication::setOverrideCursor(Qt::BlankCursor);``
4. 任一控件下显示与关闭鼠标

    .. code-block:: cpp

      this->setCursor(Qt::BlankCursor); //隐藏鼠标

      this->setCursor(Qt::ArrowCursor); //显示正常鼠标

   this改为需要隐藏鼠标的部件，就可以令当鼠标移动到该部件时候，效果生效。
   
   以上的都需要动一下鼠标才会消失，不知道不是我没有搞好，下面一启动就可以隐藏起来
   
5. 调用下面函数

   ``QWSServer::setCursorVisible(false);``

   这是一个静态函数，可以在main()函数中，实例化QApplication以后调用，这样整个程序将不会出现鼠标的光标。注意必须包含头文件。	//但是在程序启动时会闪现一下光标

源代码
------------------------------------

*src/corelib/global/qfeatures.h*
