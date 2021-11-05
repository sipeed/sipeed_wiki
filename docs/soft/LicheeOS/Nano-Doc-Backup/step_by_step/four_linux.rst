编译和配置linux
====================================

.. contents:: 本文目录

------------------------------------

1. 克隆linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  ``git clone https://github.com/Lichee-Pi/linux.git --depth=1 -b nano-4.14-exp``

2. 载入默认配置
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 下载配置文件

  ``wget http://nano.lichee.pro/_static/step_by_step/lichee_nano_linux.config``

- 修改下载的配置文件名为.config

  ``mv lichee_nano_linux.config ./config``

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 编译

  ``make ARCH=arm``

- 系统默认的账号密码

  账号：root

  密码：licheepi
