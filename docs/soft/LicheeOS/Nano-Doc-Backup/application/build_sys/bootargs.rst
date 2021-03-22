uboot传递参数
================================

.. contents:: 本文目录

再探 Uboot
--------------------------------

首先进入 uboot，控制台输入 ``printenv`` ，可看到控制台输出以下信息：

:: 

   arch=arm
   baudrate=115200
   board=sunxi
   board_name=sunxi
   --- 略去一些信息 ---
   boot_scripts=boot.scr.uimg boot.scr
   bootcmd=run distro_bootcmd
   cpu=arm926ejs

通过此命令我们可以看到 uboot 自动配置了一些启动命令与参数，其中变量 boot_scripts 指定了启动时要加载哪个命令文本文件，依据此处，我们进行 boot.scr 的构建；

建立 boot.cmd 并确认参数
--------------------------------

boot.scr 由 boot.cmd 生成，此处新建一个 boot.cmd 文件，并写入以下内容：

.. code-block:: bash

    setenv bootargs console=tty0 console=ttyS0,115200 panic=5 rootwait root=/dev/mmcblk0p2 rw 
    load mmc 0:1 0x80C00000 suniv-f1c100s-licheepi-nano.dtb
    load mmc 0:1 0x80008000 zImage
    bootz 0x80008000 - 0x80C00000

第一行setenv命令，设定了变量bootargs(启动参数)为：通过tty0和ttyS0串口输出启动信息；启动失败延迟5秒重启，根文件在TF卡的第二分区，可读写；

第二行指定了从TF中将设备树的dtb文件加载到0x80C00000的位置(地址参考自官方SDK)

第三行指定了将压缩后的内核zImage加载到0x80008000的位置

第四行为从加载地址启动内核的命令

生成 boot.scr
--------------------------------

:menuselection:`uboot --> tools -->mkimage` ，通过该程序生成boot.scr

为使用方便，建议将其：

    ``cp ./mkimage /usr/local/bin/mkimage``

生成 boot.scr

    ``mkimage -C none -A arm -T script -d boot.cmd boot.scr``

最后将其放入第一分区

.. admonition:: 交流与答疑

    对于本节内容，如有疑问，欢迎到 `Bootloader 与 RTOS 使用交流帖 <http://bbs.lichee.pro/d/21-bootloader-rtos>`_ 提问或分享经验。