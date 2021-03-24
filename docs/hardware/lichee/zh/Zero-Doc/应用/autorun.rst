开机自启动
===================================

.. contents:: 本文目录

buildroot 根文件系统
-----------------------------------

修改/etc/inittab:

   ``ttyS0::respawn:/root/logintest -L ttyS0 115200 vt100``

新建logintest：

.. code-block:: bash

    #!/bin/sh
    /bin/login -f root

自启动任务在 */etc/init.d/rcS* 中加入即可

export 相关环境变量在 */etc/profile* 中加入。

开机免登陆
-----------------------------------

修改mingetty：
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

http://www.filewatcher.com/m/mingetty-1.07.tar.gz.13435-0.html

.. code-block:: c
   :caption: 修改mingetty.c中的代码

    第352行的char *logname, *s;
    更改为char *logname = "root", *s;
    把第409-415行注释
    /* if (autologin) {
    do_prompt (0);
    printf ("login: %s (automatic login)\n", autologin);
    logname = autologin;
    } else
    while ((logname = get_logname ()) == 0)
    /* do nothing */ /*; */

修改makefile

   CC=arm-none-linux-gnueabi-gcc	//本机编译则不用
   编译生成mingetty
   将生成的mingetty程序拷贝到根文件系统的/sbin目录下

修改login
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

http://www.filewatcher.com/_/?q=util-linux-2.13-pre7.tar.bz2

修改login.c中的代码

:: 

    把344行的passwd_req = 1;
    更改为passwd_req = 0;
    在文件中添加locale.h头文件
    #include <locale.h>

编译生成login

    ``gcc -o login login.c ../lib/setproctitle.c checktty.c -Wall -lcrypt -I ../include/``

更新login

   将生成的login 程序拷贝到根文件系统的/bin目录下，结束。

修改inittab文件
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

将跟文件系统/etc/inittab文件中的最后的登录语句

   ``S2:2345:respawn:/sbin/mingetty ttyS0``

将修改后的根文件系统重新下载到系统中，系统启动时就会直接登录。不需要输入用户名及密码了。

开机屏幕不显示log
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在 *boot.scr* 中去掉tty0即可
