看门狗的使用
=============================

.. contents:: 本文目录

.. code-block:: bash

    echo 0 >/dev/watchdog0
    echo V >/dev/watchdog0

设置和获得超时值：

对于某些驱动来说，在上层使用SETTIMEOUT ioctl命令改变watchdog的超时值是可能的，那些驱动在他们的选项与中有WDIOF_SETTIMEOUT标志。参数是一个代表以秒为单位的超时值，驱动将在同一个变量中返回实际使用的超时值，这个超时值可能由于硬件的限制，而不同于所请求的超时值

.. code-block:: c

    int timeout = 45;
    ioctl(fd, WDIOC_SETTIMEOUT, &timeout);
    printf("The timeout was set to %d seconds\n", timeout);

如果设备的超时值的粒度只能到分钟，则这个例子可能实际打印"The timeout was set to 60 seconds"。

自从Linux 2.4.18内核，通过GETTIMEOUT ioctl命令查询当前超时值也是可能的：

.. code-block:: c

    ioctl(fd, WDIOC_GETTIMEOUT, &timeout);
    printf("The timeout was is %d seconds\n", timeout);
