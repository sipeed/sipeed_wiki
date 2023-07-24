---
title: 典型应用
keywords: Linux, Lichee, TH1520, SBC, RISCV, application
update:
  - date: 2023-07-20
    version: v1.1
    author: ztd
    content:
      - Update docs
  - date: 2023-05-08
    version: v1.0
    author: wonder
    content:
      - Release docs
---

## llama.cpp

llama 是 META 开源的大语言模型，[llama.cpp](https://github.com/ggerganov/llama.cpp) 是 ggerganov 开源的纯 cpp 运行的 llama 推理项目。
感谢 llama.cpp 这个优秀的项目，我们可以在 LicheePi 4A 上运行 LLM。

笔者在早些时候稍微修改了 llama.cpp [https://github.com/Zepan/llama.cpp](https://github.com/Zepan/llama.cpp)，使其可以在更小内存（低至 700MB 左右）运行 7B 模型。

可以看到 TH1520 花费约 6s 计算一个 token（未使用 V 扩展加速，V 扩展加速预计可加速 4～8 倍，如果你加入了 V 扩展支持，欢迎投稿！）
![llama_th1520](./assets/application/llama_th1520.png)  

同时还简单测试了下在入门级 C906 内核上运行7B模型的可行性，由于 D1 的内存过小，使用了 mmap 方式只读扩展，所以引入了大量低速 IO 操作，使得运行速度大为降低，最后仅 18s/token

![llama_d1](./assets/application/llama_d1.png)  

## YOLOX 目标检测

本教程是一个如何在 LPi4A（LicheePi 4A） 开发板平台上部署 [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) 模型完成目标检测的示例。
教程中包括了：
- 在 LPi4A 开发版上安装 Python 环境
- 使用 YOLOX 项目中的源码执行模型

教程遵循通常的模型部署流程：
1. LPi4A 上的基础 Python 环境配置
2. 获取 yolox 源码和模型
3. 安装 yolox 所依赖的 python 包
4. LPi4A 上的使用 HHB-onnxruntime 执行示例

**基础 Python 环境配置**
**基本软硬件配置**

参考 LPi4A 的 《[开箱体验](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a/2_unbox.html)》中的描述，正确安装好开发板，上电启动后以 root 权限进入。

确保已联网的状态下，更新 apt 源
```bash
sudo apt update
```

安装一些软件，用于示例中后续使用
```bash
sudo apt install wget git vim
```

安装 SHL 库
```bash
wget https://github.com/T-head-Semi/csi-nn2/releases/download/v2.4-beta.1/c920.tar.gz
tar xf c920.tar.gz
cp c920/lib/* /usr/lib/riscv64-linux-gnu/ -rf
```


**Python 环境配置**
LPi4A 烧录的系统中已默认安装 python 3.11 版本。可以使用如下命令确认
```bash
python --version
```

后续均以 python3.11 版本为例，其他版本在安装依赖时需要修改到对应版本的命令。
各种 python 程序软件依赖的软件包大多可通过 pip 安装，可以使用如下命令安装 pip
```bash
apt install python3-pip
```

安装其他python包之前，先安装 venv 包，用于创建python虚拟环境
```bash
apt install python3.11-venv
```

创建 python虚拟环境，并激活
```bash
cd /root
python3 -m venv ort
source /root/ort/bin/activate
```


至此，基本 python 环境已经创建完成，与其他体系结构类似，可以直接通过 pip install 安装纯 python 包。

opencv 安装是会依赖其他 python 包，如果 pip 不能自动下载，则可以先手动安装依赖项的安装包。如何获取安装包可以参考 [下载 riscv whl](https://www.yuque.com/za4k4z/uzn618/zsp0krgg9dlp0fhx)。

**获取 YOLOX 模型**

[YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) 是一个类 YOLO 的目标检测模型，有相当优异的性能表现。
可以直接下载 github 上的源码和模型
```bash
git clone https://github.com/Megvii-BaseDetection/YOLOX.git
cd YOLOX/demo/ONNXRuntime
wget https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_s.onnx
```

**修改源码**

本教程将使用 HHB-onnxruntime 执行模型，因此切换到。在源码中的 onnxruntime 示例目录，修改文件 demo/ONNXRuntime/onnx_inference.py 的开头新增两行代码
```bash
#!/usr/bin/env python3
# Copyright (c) Megvii, Inc. and its affiliates.

+import sys
+sys.path.insert(0, "../../")
+
import argparse
import os
```
代码中使用 sys.path.insert 指定搜索路径，以此免去从源码中安装 YOLOX 的安装包的操作。

**安装依赖包**

RISC-V 体系结构的 python 生态还有欠缺，未来完善之后，YOLOX 中依赖的包可以通过 [requirements.txt](https://github.com/Megvii-BaseDetection/YOLOX/blob/main/requirements.txt) 文件直接安装。
本教程中的 YOLOX 示例依赖了较多的 python 包，下载预编译好的 python 包
```bash
git clone -b python3.11 https://github.com/zhangwm-pt/prebuilt_whl.git
cd prebuilt_whl
```

可以按照以下顺序，手工处理。
```bash
pip install numpy-1.25.0-cp311-cp311-linux_riscv64.whl
pip install opencv_python-4.5.4+4cd224d-cp311-cp311-linux_riscv64.whl
pip install kiwisolver-1.4.4-cp311-cp311-linux_riscv64.whl
pip install Pillow-9.5.0-cp311-cp311-linux_riscv64.whl
pip install matplotlib-3.7.2.dev0+gb3bd929cf0.d20230630-cp311-cp311-linux_riscv64.whl
pip install pycocotools-2.0.6-cp311-cp311-linux_riscv64.whl
pip3 install loguru-0.7.0-py3-none-any.whl
pip3 install torch-2.0.0a0+gitc263bd4-cp311-cp311-linux_riscv64.whl
pip3 install MarkupSafe-2.1.3-cp311-cp311-linux_riscv64.whl
pip3 install torchvision-0.15.1a0-cp311-cp311-linux_riscv64.whl
pip3 install psutil-5.9.5-cp311-abi3-linux_riscv64.whl
pip3 install tqdm-4.65.0-py3-none-any.whl
pip3 install tabulate-0.9.0-py3-none-any.whl
```

安装过程中会涉及到其他纯 python 依赖包，pip 会自动从官方源下载。

**安装 HHB-onnxruntime**

HHB-onnxuruntime 是移植了 SHL 后端（execution providers），让 onnxruntime 能复用到 SHL 中针对玄铁 CPU 的高性能优化代码。

```bash
wget https://github.com/zhangwm-pt/onnxruntime/releases/download/riscv_whl/onnxruntime-1.14.1-cp311-cp311-linux_riscv64.whl
pip install onnxruntime-1.14.1-cp311-cp311-linux_riscv64.whl
```

**执行**

在示例目录中执行 onnx_inference.py 示例

```bash
python3 onnx_inference.py -m yolox_s.onnx -i soccer.jpg -o outdir -s 0.3 --input_shape 640,640
```

`python3 onnx_inference.py -m yolox_s.onnx -i soccer.jpg -o outdir -s 0.3 --input_shape640,640`

参数说明：
- -m：指定模型
- -i：指定图片
- -o：指定输出目录
- -s：指定检测的阈值
- --input_shape：指定检测时使用的图片尺寸

**参考结果**

本教程中输入如下图，是运动员踢足球的图片，预期的检测结果是检测到两个人和一个足球。

> 图片来源于网络

![yolox_detection_soccer_input.jpg](./assets/application/yolox_detection_soccer_input.jpg)

示例正常执行后，会在 outdir 目录下生成结果图片 soccer.jpg。图片中会用框画出检测到的目标，并标注概率，效果如下图：

![yolox_detection_soccer_output.jpg](./assets/application/yolox_detection_soccer_output.jpg)

## Docker

首先安装所需要的软件包
```shell
sudo apt-get update
sudo apt-get install docker docker-compose
```

安装完成后，使用 `sudo docker info` 命令验证安装是否成功：  
```shell
sipeed@lpi4a:~$ sudo docker info
Client: 
 Context: default
 Debug Mode: false  
Server:
 Containers: 0
  Running: 0 
  Paused: 0  
  Stopped: 0 
 Images: 0
 Server Version: 20.10.24+dfsg1 
 Storage Driver: overlay2 
  Backing Filesystem: extfs  
  Supports d_type: true
  Native Overlay Diff: true  
  userxattr: false  
 Logging Driver: json-file
 Cgroup Driver: systemd
 Cgroup Version: 2
 Plugins:
  Volume: local  
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog 
 Swarm: inactive 
 Runtimes: io.containerd.runc.v2 io.containerd.runtime.v1.linux runc 
 Default Runtime: runc 
 Init Binary: docker-init 
 containerd version: 1.6.20~ds1-1+b1
 runc version: 1.1.5+ds1-1+b1
 init version:
 Security Options:
  seccomp 
Profile: default 
  cgroupns
 Kernel Version: 5.10.113-gfac22a756532
 Operating System: Debian GNU/Linux 12 (bookworm)  
 OSType: linux
 Architecture: riscv64 
 CPUs: 4  
 Total Memory: 15.47GiB
 Name: lpi4a 
 ID: MCKE:SEGQ:EBUX:ZMLC:P2WK:GIJ7:XAEQ:F56H:73HK:C3L5:IA5A:7GJI  
 Docker Root Dir: /var/lib/docker
 Debug Mode: false  
 Registry: https://index.docker.io/v1/ 
 Labels:  
 Experimental: false
 Insecure Registries:  
  127.0.0.0/8
 Live Restore Enabled: false
```

若想让普通用户也有 Docker 的执行权限，可以执行以下命令来实现：  
```shell
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```
这些命令添加普通用户权限的用户名到 `docker` 用户组，并激活组权限。若不添加，则每次执行 Docker 相关命令时，需要以 sudo 权限来执行。

接下来，我们拉取 hello-world 镜像体验 Docker 的使用：  
```shell
sipeed@lpi4a:~$ docker pull hello-world
Using default tag: latest
latest: Pulling from library/hello-world   
b102dd09f2b3: Pull complete 
Digest: sha256:926fac19d22aa2d60f1a276b66a20eb765fbeea2db5dbdaafeb456ad8ce81598      
Status: Downloaded newer image for hello-world:latest    
docker.io/library/hello-world:latest 
```

接下来，启动刚刚拉取下来的容器：
```shell
sipeed@lpi4a:~$ docker run hello-world
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

查看 hello-world 镜像的相关信息：
```shell
sipeed@lpi4a:~$ docker images hello-world
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
hello-world   latest    eb6f80695a28   2 months ago   4.98kB
```

若要体验更完整的镜像，去[这里](https://hub.docker.com/)搜索想要使用的发行版名称，拉取即可。

## Minecraft Server

这里以`1.20.1`版本为例，LPi4A 作为 Server，电脑端（Ubuntu 22.04）作为 Client。

首先在[这里](https://github.com/fizzed/nitro/releases/tag/builds)下载由 Fizzed 优化的 nitro JDK 19，下载完成后解压，重命名文件夹并移动到 `/opt/` 目录下：
```shell
tar xvf fizzed19.36-jdk19.0.1-linux_riscv64.tar.gz
sudo mv fizzed19.36-jdk19.0.1-linux_riscv64 /opt/jdk_19
```

测试该 JDK 是否可用：
```shell
sipeed@lpi4a:~$ /opt/jdk_19/bin/java -version
openjdk version "19.0.1" 2022-09-20
OpenJDK Runtime Environment Fizzed19.36 (build 19.0.1+10)
OpenJDK 64-Bit Server VM Fizzed19.36 (build 19.0.1+10, mixed mode)
```

若出现版本号则可用。若已经预装了别的版本的 JDK，那么可以更改下软连接，先查看原先的软链接信息，记录下方便后面改回来：
```shell
sipeed@lpi4a:~$ ls /usr/bin/java -l
lrwxrwxrwx 1 root root 22 Apr 26 10:40 /usr/bin/java -> /etc/alternatives/java
```

然后更改软链接指向刚刚安装的 JDK：
```shell
sudo rm /usr/bin/java
sudo ln -s /opt/jdk_19/bin/java /usr/bin/java
```

使用命令验证软链接是否配置成功：
```shell
java -version
```
出现版本，则配置成功。

接下来，在[这里](https://www.minecraft.net/zh-hans/download)下载原版服务端 jar 文件到 LPi4A，注意版本为`1.20.1`，然后在 LPi4A 上先执行：
```shell
java -jar server.jar nogui
```

若出现提示
```shell
[ServerMain/WARN]: Failed to load eula.txt
[ServerMain/INF0]:You need to agree to the EULA in order to run the server. Go to e ula.txt for more info.
```

则将当前目录下的 `eula.txt`文件中对应行改为的 false 改为 true：
```shell
eula=true
```

保存后退出，重新启动服务器，第一次启动会比较慢，耐心等待，启动完成后会显示启动用时（下列用时并非第一次启动用时）：
```shell
[03:51:02] [Server thread/INFO]: Time elapsed: 36394 ms
[03:51:02] [Server thread/INFO]: Done (52.927s)! For help, type "help"
```

接下来，在 PC 端启动客户端后即可连接，建议使用第三方客户端启动器 HMCL（下载链接https://hmcl.huangyuhui.net/download/）。
下载完成后，启动 HMCL：
```shell
java -jar HMCL-3.5.5.jar
```

可以直接在启动器中下载`1.20.1`版本，并且配置好游戏账户，然后即可进入游戏，进入游戏后，输入 服务器 IP（LPi4A 的 IP）添加服务器后即可连接（确保电脑和 LPi4A 处于同一网络下），效果如下：
![mc_server_menu](./assets/application/mc_server_menu.png)

> 注意，若想改回原来版本的 JDK，则执行：
> ```shell
> sudo rm /usr/bin/java
> sudo ln -s /opt/jdk_19/bin/java /etc/alternatives/java
> ``` 

## Wine-CE

首先在[这里](https://gitee.com/wine-ce/wine-ce/releases/tag/v8.9)下载 `wine-ce_dlls_8.9.0.all.tar.xz`，`wine-ce_core_8.9.0.riscv64.tar.xz`这两个文件，这里假设下载到用户主目录（撰写该文档时最新版本为8.9）。

然后根据文档中的步骤进行安装：
```shell
sudo apt install fonts-liberation fonts-wine glib-networking libpulse0 gstreamer1.0-plugins-good gstreamer1.0-x libaa1 libaom3 libasound2-plugins  libcaca0 libcairo-gobject2 libcodec2-1.0 libdav1d6 libdv4 libgdk-pixbuf-2.0-0 libgomp1 libgpm2 libiec61883-0 libjack-jackd2-0 libmp3lame0 libncurses6 libncursesw6 libnuma1 libodbc2 libproxy1v5 libraw1394-11 librsvg2-2 librsvg2-common libsamplerate0 libshine3 libshout3 libslang2 libsnappy1v5 libsoup2.4-1 libsoxr0 libspeex1 libspeexdsp1 libtag1v5 libtag1v5-vanilla libtwolame0 libva-drm2 libva-x11-2 libva2 libvdpau1 libvkd3d-shader1 libvkd3d1 libvpx7 libwavpack1 libwebpmux3 libx265-199 libxdamage1 libxvidcore4 libzvbi-common libzvbi0 mesa-va-drivers mesa-vdpau-drivers va-driver-all vdpau-driver-all vkd3d-compiler

sudo tar -Jxvf wine-ce_core_8.9.0.riscv64.tar.xz -C /opt/
sudo tar -Jxvf wine-ce_dlls_8.9.0.all.tar.xz -C /opt/
sudo ln -sf /opt/wine-ce/bin/wine /usr/bin/wine
sudo ln -sf /opt/wine-ce/bin/winecfg /usr/bin/winecfg
rm -rf ~/.wine
```

接下来进行一些初始化设置：  
```shell
winecfg
```

这里使用的设置如下：

![wine_ce_settings](./assets/application/wine_ce_settings.png)

设置完成后，即可运行 Windows 下的程序，比如这里的命令运行 Windows 下的记事本
```shell
wine notepad.exe
```

![wine_ce_use](./assets/application/wine_ce_use.png)

## SuperTuxKart

SuperTuxKart 是一款 3D 开源街机赛车游戏，有各种角色、赛道和模式可供选择。在 LPi4A 上也可以通过源码编译来体验：  

首先安装依赖：
```shell
sudo apt-get install build-essential cmake libbluetooth-dev libsdl2-dev \
libcurl4-openssl-dev libenet-dev libfreetype6-dev libharfbuzz-dev \
libjpeg-dev libogg-dev libopenal-dev libpng-dev \
libssl-dev libvorbis-dev libmbedtls-dev pkg-config zlib1g-dev
```

接下来参考[文档](https://github.com/supertuxkart/stk-code/blob/master/INSTALL.md#building-supertuxkart-on-linux)步骤编译：
```shell
# clone and configure src
git clone https://github.com/supertuxkart/stk-code stk-code
svn co https://svn.code.sf.net/p/supertuxkart/code/stk-assets stk-assets

# go into the stk-code directory
cd stk-code

# create and enter the cmake_build directory
mkdir cmake_build
cd cmake_build

# run cmake to generate the makefile
cmake .. -DBUILD_RECORDER=off -DNO_SHADERC=on

# compile
make -j$(nproc)
```

编译完成后，在当前目录下的 `bin/` 文件夹中即可找到 `supertuxkart` 程序。运行即可：
```shell
./bin/supertuxkart
```

效果如下：

![supertuxkart_play](./assets/application/supertuxkart_play.png)

## 其它

欢迎投稿～ 投稿接受后可得￥5～150（$1~20）优惠券！