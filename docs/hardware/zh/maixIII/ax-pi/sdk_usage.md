---
title: Maix-III 系列 AXera-Pi 开发板 SDK 使用介绍
---

## 获取 SDK 源码

上一篇介绍了基础的开发环境搭建和使用方法，你应该了解什么是本地编译和交叉编译，这一篇介绍如何使用这些 sdk 源码开发程序。

- [libmaix](https://github.com/sipeed/libmaix)

由 sipeed 提供在 linux 平台统一的嵌入式开发环境，主要有摄像头、屏幕、视觉、图像处理、NPU pipiline 相关的实机部署例程，适合刚入门嵌入式 linux 开发的同学使用。

- [ax-sample](https://github.com/AXERA-TECH/ax-samples)

由爱芯提供 AI 模型的开发与评估验证，提供给有经验的 AI 开发者使用，不涉及任何硬件外设有关的内容。

- [axpi_bsp_sdk](https://github.com/sipeed/axpi_bsp_sdk)

芯片商用时所用的 bsp 开发包，这里主要提供的是芯片的原始开发资料，如 uboot 、 linux 、 msp 、msp 等工程代码，这个部分是逐步开源的，你可以从这里得到商业评估用的代码，例如 ipcdemo 这样的程序，但这些代码会很复杂且高耦合，适合有经验的同行出于商业落地的目的使用。

- [ax-pipeline](https://github.com/AXERA-TECH/ax-pipeline)

基于 axpi_bsp_sdk 制作的 AI 部署高性能仓库，在这里主要用于该项目基于 AXera-Pi 展示 ISP、图像处理、NPU、编码、显示 等功能模块软件调用方法，方便社区开发者进行快速评估和二次开发自己的多媒体应用。

### libmaix

这是一个适用于 sipeed 所用 linux 芯片开发的 C/C++ 基础开发框架，使用 cmake 构建，提供了许多开箱参考的案例，还有一些第三方库代码的链接，如 opencv openmv 这些视觉库的链接。

SDK 源码在 [libmaix](https://github.com/sipeed/libmaix)， 需要使用 git 命令下载：

```bash
git clone https://github.com/sipeed/libmaix.git --recursive
```
>! 注意这里`--recursive` 参数是必须的，用来下载仓库里面的子模块，如果没有这个参数，代码会不完整，导致编译出错

> 中国国内可能下载速度较慢，可以多取消重试几次，可能会遇到速度快的节点，当然最好还是通过设置代理来加速下载。

另外， AI 模型及例程在 [MaixHub 模型库](https://maixhub.com/model/zoo) 可以找到， 以及 [AXERA-TECH/ax-samples](https://github.com/AXERA-TECH/ax-samples) 仓库。

## 编译 SDK 源码

回顾一下前文的内容，编译有两种方式：

* 直接在开发板上编译：编译速度较慢，但是不需要额外的环境配置。
* 在 PC 上编译，然后拷贝可执行文件到开发板，也就是交叉编译： 编译速度更快，但是需要额外的环境配置。

### [libmaix](https://github.com/sipeed/libmaix)

> /home/ 目录已预置，可以 git pull 联网拉取更新。

对于 `libmaix`， 按照其`README.md` 文件描述的方法编译即可， 不过需要在`menuconfig`命令中选择 `AXera-Pi` 作为编译目标。

这里简要介绍一下编译过程（libmaix 目前还未稳定，未来可能会有大的更新），实际以[libmaix 仓库](https://github.com/sipeed/libmaix)代码和说明为准。

* 先安装依赖
```
apt install build-essential cmake python3 sshpass git
```
> sshpass 也可以不安装， build-essential, cmake, git, python3 必须安装

* 克隆仓库到本地或者开发板
```
git clone https://github.com/sipeed/libmaix --recursive
```
>! 注意 `--recursive` 参数是必须的，用以克隆子模块，否则会缺代码

这里以在开发板上编译为例：

```bash
cd /home/libmaix # git clone https://github.com/sipeed/libmaix --recursive
cd examples/axpi
python3 project.py distclean
# python3 project.py menuconfig # 可以配置相关参数
python3 project.py build        # 如果增加文件了，需要 python3 project.py rebuild 命令
./dist/start_app.sh             # 运行示例程序
```

### [ax-samples](https://github.com/AXERA-TECH/ax-samples)

> /home/ 目录已预置，可以 git pull 联网拉取更新。

[ax-samples](https://github.com/AXERA-TECH/ax-samples) 是爱芯官方提供的例程，包含了一些 AI 模型和运行代码，编译完能直接在开发板上运行，只不过输入是图片，不是摄像头。
进入开发板终端，执行以下代码：

```bash
cd /home/ax-samples # git clone https://github.com/AXERA-TECH/ax-samples.git
mkdir build
cd build
cmake ..
make install
```

然后就能在`ax-samples/build/install/bin/`目录下找到编译好的可执行文件。

### [axpi_bsp_sdk](https://github.com/sipeed/axpi_bsp_sdk)

回到芯片原厂开发的环境，这需要有经验的嵌入式 Linux 开发者来操作，直接看 readme 进行操作，文档在 docs 目录下。

#### What is this?

this is a ax620 linux bsp sdk form AX620_R1.22.2801_Sipeed. currently it is application layer open source.

```bash
juwan@juwan-n85-dls:~/GIT_AX620_SDK_V0.31.0_P23/sipeed/axpi_bsp_sdk$ tree -L 1
.
├── app
├── build
├── msp
├── readme.md
├── rootfs
└── third-party

5 directories, 1 file
```

#### ready arm gcc

```bash
git clone https://github.com/sipeed/axpi_bsp_sdk.git

cd axpi_bsp_sdk

wget http://releases.linaro.org/components/toolchain/binaries/latest-7/arm-linux-gnueabihf/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf.tar.xz

sudo tar -xvf gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf.tar.xz -C /opt/

```

#### how to compile

- bsp msp sample

```bash

cd msp/sample/

export PATH="/opt/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf/bin/:$PATH" && make p=AX620_demo all install

```

- third-party libs

```bash

cd third-party

export PATH="/opt/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf/bin/:$PATH" && make p=AX620_demo all install

```

- bsp app ipcdemo

```bash

cd app/

export PATH="/opt/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf/bin/:$PATH" && make p=AX620_demo all install

```

- bsp msp component lib, such as `cd app/msp/component/common && make xxxx`.

```
juwan@juwan-n85-dls:~/GIT_AX620_SDK_V0.31.0_P23/sipeed/axpi_bsp_sdk/msp/component$ tree -L 1
.
├── axsyslog
├── common
└── thermal

4 directories, 0 files
```

#### run your program

- on pc

```
sshpass -p root scp ./vo_fb/sample_vo_fb root@192.168.233.1:/opt/bin/sample_vo_fb
```

- on board

```

chmod 777 /opt/bin/sample_vo_fb

/opt/bin/sample_vo_fb -v dsi0@480x854@60 -m 0 &

fbv /home/examples/480x360.jpg

killall sample_vo_fb

```

## 组合 SDK 和 AI 模型例程

比如我们要跑一个视觉 AI 模型，需要用到摄像头，屏幕，还有 AI 模型，你需要借助以下仓库代码完成这个目标。

### 借助 libmaix 实现（难度最小）

基于 libmaix 的 axpi 项目进行开源快速验证效果，代码简单易懂，基于在线服务完成模型部署，只用于新手上路，与 ax-sample 的模型一起被支持。

- [axpi](https://github.com/sipeed/libmaix/tree/release/examples/axpi)
- [axpi_classification_cam](https://github.com/sipeed/libmaix/tree/release/examples/axpi_classification_cam)
- [axpi_yolov5_cam](https://github.com/sipeed/libmaix/tree/release/examples/axpi_yolov5_cam)

> 20221113 目前仓库只保证用户初次上手时能够不报错的安全调用 AI 模型，不代表芯片的最好效果。

### 借助 ax-pipeline 实现（难度适中）

到了这里要有基本的芯片 bsp sdk 开发的基础（axpi_bsp_sdk），这部分会略显专业一些，这个仓库目前追求最高性能的效果。

- [准备编译环境](https://github.com/AXERA-TECH/ax-pipeline/blob/main/docs/compile.md)
- [如何更换自己训练的 yolov5 模型？](https://github.com/AXERA-TECH/ax-pipeline/blob/main/docs/how_to_deploy_custom_yolov5_model.md)
- [如何部署自己的其他模型](https://github.com/AXERA-TECH/ax-pipeline/blob/main/docs/how_to_deploy_custom_model.md)

### 借助 ipcdemo 实现（难度最大）

基于 axpi_bsp_sdk 的 ipcdemo 商用视频推流应用，由于源码过于复杂，需要有上述基础才能介入。

- [axpi_bsp_sdk/app/IPCDemo](https://github.com/sipeed/axpi_bsp_sdk/tree/main/app/IPCDemo)
