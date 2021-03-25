Docker开发环境
=========================================

.. contents:: 本文目录

docker安装
-----------------------------------------

什么是docker？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Docker 是一个开源的应用容器引擎，基于 Go 语言 并遵从Apache2.0协议开源。

Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。

容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。

本节只简单介绍docker开发环境的搭建，想要详细了解docker，可以查看本节的附录“Docker 命令速查”。

简而言之，我帮你搞好了docker镜像，你就不用自己再费力搭建啦。

docker下载安装
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   sudo apt-get install docker.io
   docker version

安装成功后可见版本信息

.. code-block:: bash

    Client version: 1.6.2
    Client API version: 1.18
    Go version (client): go1.2.1
    Git commit (client): 7c8fca2
    OS/Arch (client): linux/amd64
    FATA[0000] Get http:///var/run/docker.sock/v1.18/version: dial unix /var/run/docker.sock: permission denied. Are you trying to connect to a TLS-enabled daemon without TLS? 

默认情况下会报后面的错误，如果使用sudo就不会报错。不想每次都sudo的话，可以把用户加入到docker组。

.. code-block:: bash

   //如果还没有 docker group 就添加一个(默认安装后已经有了)
   //sudo groupadd docker
   //将用户加入该 group 内。然后退出并重新登录就生效啦。
   sudo gpasswd -a ${your_user_name} docker
   //重启 docker 服务
   sudo service docker restart
   //切换当前会话到新 group, 或者关掉终端重新连接也会生效
   //newgrp - docker

安装荔枝派开发镜像
-----------------------------------------

.. code-block:: bash

   docker pull zepan/licheepi
   docker run -d -p 6666:22 zepan/licheepi /usr/sbin/sshd -D

这样就安装并开启的容器ssh服务，只需连接主机的6666端口，以root用户，licheepi密码登录即可进行开发操作。
