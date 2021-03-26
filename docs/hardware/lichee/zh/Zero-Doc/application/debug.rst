Segment Fault调试
===================================

.. contents:: 本文目录

在调试linux程序时经常会出现段错误，这里介绍常规的段错误定位方法，即使用core dump文件。

配置core dump
-----------------------------------

先设置允许的core dump文件大小。

.. code-block:: bash

    echo "ulimit -c 102400" >> /etc/profile		#ulimit -c unlimited 可以设置为无限
    source /etc/profile		#生效

使用 ``ulimit -c`` 来查看当前的core文件大小。

配置core 文件名
-----------------------------------

**/proc/sys/kernel/core_uses_pid** 可以控制产生的 core 文件的文件名中是否添加 pid 作为扩展 ，如果添加则文件内容为 1 ，否则为 0

配置core保存位置
-----------------------------------

core保存位置默认为当前目录下core名字

*proc/sys/kernel/core_pattern* 可以设置格式化的 core 文件保存位置或文件名 ，比如原来文件内容是 core-%e

可以这样修改 :
  
   ``echo "/corefile/core-%e-%p-%t" > core_pattern``

将会控制所产生的 core 文件会存放到 /corefile 目录下，产生的文件名为 core- 命令名 -pid- 时间戳

以下是参数列表 :

:: 

    %p - insert pid into filename 添加 pid
    %u - insert current uid into filename 添加当前 uid
    %g - insert current gid into filename 添加当前 gid
    %s - insert signal that caused the coredump into the filename 添加导致产生 core 的信号
    %t - insert UNIX time that the coredump occurred into filename 添加 core 文件生成时的 unix 时间
    %h - insert hostname where the coredump happened into filename 添加主机名
    %e - insert coredumping executable name into filename 添加命令名
