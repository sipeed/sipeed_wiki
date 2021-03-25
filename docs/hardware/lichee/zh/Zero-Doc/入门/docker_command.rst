Docker命令速查
=========================================

.. contents:: 本文目录

Docker概念
-----------------------------------------

:guilabel:`镜像` ：只读的模板

:guilabel:`容器` ：负责应用程序的运行。是从镜像创建的运行实例，互相隔离，安全的平台。

:guilabel:`镜像只读` :容器在启动时创建一层可写层作为最上层。（类似overlayfs）

:guilabel:`仓库` ：集中存放镜像的地方，和github类似。https://hub.docker.com/

Docker 安装
-----------------------------------------

.. code-block:: bash

    sudo apt-get install docker.io		
    sudo gpasswd -a your_user_name docker		#加入用户组
    sudo service docker restart		
    newgrp - docker		#使用新用户组，或者也可以断开终端重连生效
    docker version		#查看docker版本信息

docker下各文件默认存放在/var/lib/docker下

   ``du -h --max-depth=1 /var/lib/docker		#查看docker目录大小``

Docker镜像操作
-----------------------------------------

.. code-block:: bash

   docker search licheepi		#搜索镜像
   docker pull zepan/licheepi		#下载镜像
   docker run zepan/licheepi apt-get install -y xxx		#在镜像中执行命令，安装某软件
   docker commit -m="install something" -a="zepan"  container_id zepan/licheepi 
   docker login
   docker push	zepan/licheepi

Docker容器操作
-----------------------------------------

运行交互式的容器
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run -i -t learn/tutorial /bin/bash        //开启一个交互式虚拟终端
           -i    交互式
           -t     虚拟终端
           -d    后台
           -P    端口映射
   
   docker port  id    //查看端口映射情况 
   
   docker inspect  id    //查看容器详细状态

启动容器（后台模式）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run -d learn/tutorial /bin/sh -c "while true; do echo hello world; sleep 1; done"
   返回容器id：350807154a3dd17309b23bb9a9a9897dd3fc91667a7d176aca42f390808e3019

通过ps查看正在运行的容器实例
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   zepan@ubuntu:~$ docker ps
   CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
   350807154a3d        learn/tutorial      "/bin/sh -c 'while..."   31 seconds ago      Up 30 seconds                           blissful_lamport
   docker ps -l    //查看最后运行的容器
   docker ps -a    //查看所有容器

查看对应容器的输出：
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
    
    docker logs 3508 或 blissful_lamport
    docker logs -f    xxxx        //类似tail -f

停止/开始/重启容器：
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    docker stop 3508        //通过发送信号方式停止
    docker kill 3508           //kill方式停止
    docker start 3508        //start -i  交互式执行
    docker restart 3508

删除容器
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    docker remove 3508
    docker rm `docker ps -a -q`        //删除所有容器

主机容器互拷数据
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    docker cp id:/xxx/xx   /yyy/yy/
    docker cp  /yyy/yy/    id:/xxx/xx  
            
开启容器的ssh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    docker run -d -p 6666:22 zepan/licheepi /usr/sbin/sshd -D
