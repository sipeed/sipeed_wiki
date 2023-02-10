---
title: Maix-III AXera-Pi SDK development
---

> Before reading, it's necessary to know basic usage about `gcc` and `make`.

## Preparation

We have told basic operation like burning system and using AXera-Pi in previous article, which help you know how to use AXera-Pi.

For embedded linux, we usually use cross-compile technology to compile out the application for target linux device.

A cross compiler is a compiler capable of creating executable code for a platform other than the one on which the compiler is running. For example, a cross compiler executes on machine X and produces machine code for machine Y. 

Normally our computer have better performance than target embedded linux device, compiling the executable on our computer, then run the application on target embedded linux device. This saves more time than compiling and running on target embedded linux device.

For example, `ax-sample` takes more than 10 minutes to be compiled on AXera-Pi, but it takes less than one minute on your computer.

Above all, for embedded development, coree-compile technology is commom and it's necessary to know about this if you want to save your time.

## Transfer files

Compiling out the application on our computer, we need send the application to AXera-Pi.

- `SSH` (Secure Shell) enables secure system administration and file transfers over insecure networks. 
- `Serial` application tool is OK to transfer files but it's too slow.

### Transfer file with SSH

There are many good SSH application on Windows, here we use [Mobaxterm](https://mobaxterm.mobatek.net/) to login AXera-Pi and Transfer file.

[Mobaxterm Usage Demo](https://mobaxterm.mobatek.net/demo.html)

![mobaxterm_transfer_file](./assets/dev_prepare/mobaxterm_transfer_file.jpg)

Besides, [Vscode](https://code.visualstudio.com/) is also a gooe idea for transfering file. Install the [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) and [Remote Explorer](https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-explorer) extensions, then login to AXera-Pi via vscode SSH.

![transfer_file_vscode](./assets/flash_system/transfer_file_vscode.jpg)

### Transfer file with scp

scp means `ssh + cp`.

Here is the command to transfer file.

```bash
scp [option] /path/to/source/file user@server-ip:/path/to/destination/directory
```

- `/path/to/source/file` Target file/folder sent from host to device
- `user@server-ip` : Remote target device IP address.
- `/path/to/destination/directory` Target device directory to receive the file/folder

###  Use card reader

Because of different file system, it's only suggested to use this way if operating system of your computer is Linux.

### Transfer file with UART

For linux users, install `lrzsz` first (`sudo apt-git install lrzsz`) and use it to finish this

Windows user can use Mobaxterm to transfer file between computer and AXera-Pi via USB-UART connection.

## Compile on AXera-Pi

Here we tell how to compile application on AXera-Pi.

Because serial port connector is slow and can be only opened by only one application at one time, we usually login to AXera-Pi by SSH, which we can open many terminals and enter different commands in dirrerent ssh terminal at the same time.

![ssh_mutiple_terminals](./assets/dev_prepare/ssh_mutiple_terminals.jpg)

### Vscode remote

We have told how to login to AXera-Pi via SSH with vscode, login to AXera-Pi by Vscode first, make sure not install [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) extension of vscode on AXera-Pi, this extension may close SSH connnection.

Click ① and ② to open a SSH connection.

![vscode_ssh_connect](./assets/dev_prepare/vscode_ssh_connect.jpg)

Here we take `192.168.233.1` IP address as example, make sure not forget add username `root` at first.

`root@IP_address`

![vscode_ssh_connect_example_ip](./assets/dev_prepare/vscode_ssh_connect_example_ip.jpg)

Choose platform `Linux` and `Continue`.

<img alt="vscode_ssh_connect_linux_platform" src="./assets/dev_prepare/vscode_ssh_connect_linux_platform.jpg" width="45%">
<img alt="vscode_ssh_connect_continue" src="./assets/dev_prepare/vscode_ssh_connect_continue.jpg" width="45%">

Eenter password `root` to login

![vscode_ssh_connect_enter_password](./assets/dev_prepare/vscode_ssh_connect_enter_password.jpg)

Succeed logining to AXera-Pi.

![vscode_ssh_connect_succeed_login](./assets/dev_prepare/vscode_ssh_connect_succeed_login.jpg)

Click `Open Folder` to see your AXera-Pi directory structure.

![transfer_file_vscode](./assets/flash_system/transfer_file_vscode.jpg)

Use command <code>Ctrl + Shift + `</code> to new a terminal, run following command to compile <code>libmiax</code> application.

Example compiling command:

```bash
cd /home/libmaix/examples/axpi/ # Open source code directory
python3 project.py build # Compile the project
fbon # Enable screen control
./dist/start_app.sh # Run compiled out application
```

![compiling_example_code](./assets/dev_prepare/compiling_example_code.jpg)

Running the commands above, screen displays camera content, use `Ctrl + c` to stop this application if you want to do other task.

![compiling_stop_example](./assets/dev_prepare/compiling_stop_example.jpg)

### Mobaxterm

Using Mobaxtern to login AXera-Pi is a good idea for windows user.

Complie libmaix example on AXera-Pi:

![mobaxterm_compile_application](./assets/dev_prepare/mobaxterm_compile_application.jpg)

## Cross compiling on computer

We compile out the application for AXera-Pi on our computer first. 

AXera-Pi is based on Cortex-A7 arm architecture, while normally our computer is based on x86-64 architecture, these two different architectures are based on different instruction set.

The binary executable program normally can not be executed on the same OS if the cpu architecture is not the same because different architecture means different instruction set.

We can install the compiler for arm architecture on our computer, compiled by this compiler, we get the program which can execute on arm architecture device like AXera-Pi.

Here we compile the program based on ubuntu, then send the compiled program to AXera-Pi and run on it.

Install the compiler for AXera-Pi first.

```bash
sudo apt install gcc-arm-linux-gnueabihf
```

Run following command to check your installation.

```bash
arm-linux-gnueabihf-gcc
```

The result should be as following.

![arm_linux_gxx_file_not_found](./assets/dev_prepare/arm_linux_gxx_file_not_found.jpg)

New a C file named `cross_test.c`, and compile it by `arm-linux-gnueabihf-gcc`. The content of the C file like this:

```c
#include <stdio.h>
int main(){
    printf("Hello, AxPi!\n");
    return 0;
}
```

Then use following command to compile the C file.

```bash
arm-linux-gnueabihf-gcc -o test cross_test.c -static
```

Then we get the executable file named `test` on our computer, and if we run `./test`, it says `Exec format error`. Check file format of `test`, we can see it's `ELF 32-bit LSB executable, ARM, EABI5`

![test_program_example](./assets/dev_prepare/test_program_example.jpg)

So it can only be executed on Axera-Pi, sending the `test` executable file to AxPi, and on Axera-Pi this program works well.

```bash
csp test root@192.168.233.1:/home
```

By this command, we succeed upload the `test` executable file to Axera-Pi via rndis protocol by `scp` commmand. And note that the password requirement of running command above is `root`.

Then we can run `test` executable file on Axera-Pi.

![hello_axpi](./assets/dev_prepare/hello_axpi.jpg)

We finish cross-compile.



简而言之，更换了桌面系统和编译链，那源码中对应的一些依赖文件肯定也会发生改变，这需要看所用的 sdk 是如何解决这个问题的，通常来说只需要换交叉编译链和修改链接目录即可。

上文介绍了如何在 linux 系统上编译运行 libmaix 项目，以及如何在 linux 系统上交叉编译 libmaix 项目，希望对大家有所帮助，只要掌握了如何管理开发环境和如何编译运行 linux 的程序，接下来就可以基于我们提供的 sdk 开发属于自己的项目了。

在这里「大佬鼠」推荐自己的开发流程和方法，最开始就是先在板子上本地编译测试现有的代码和功能，然后根据 [[maixpy3 axpi] 编辑发布 debian 镜像与在 PC 上交叉编译程序 ](https://www.cnblogs.com/juwan/p/16769237.html) 来安装 docker arm 虚拟机。

接着，将之前烧录到板子里的根文件系统（.img）通过 losetup + mount + chroot 挂载（.img）出来，这时候你就会得到和板子一样的 arm 虚拟机环境，就可以直接本地编译啦！不过，这个方法需要学习 docker 的安装喔，包括后面的模型开发也上会用到 docker 的。

> 如果你不嫌麻烦的话，可以选择配置交叉编译链、板子依赖的头文件、第三方链接库后才能进行程序的编译，但这个 docker arm 虚拟机的方法是最省事的，甚至还可以通过读卡器（或网络）挂载板子里的根文件系统进行编译。

* [什么是交叉编译？](https://cn.bing.com/search?q=%E4%BB%80%E4%B9%88%E6%98%AF%E4%BA%A4%E5%8F%89%E7%BC%96%E8%AF%91%EF%BC%9F)
* [超详细解答vscode如何远程连接Linux以及可能会出现的一些问题](https://blog.csdn.net/cxn15335120506/article/details/123238233)
* [vscode remote](https://code.visualstudio.com/docs/remote/remote-overview)
* [ssh scp 是什么？](https://cn.bing.com/search?q=ssh+scp+%E6%98%AF%E4%BB%80%E4%B9%88%EF%BC%9F)
* [libmaix](https://github.com/sipeed/libmaix)
* [mobaxterm](https://mobaxterm.mobatek.net)
* [arm-linux-gnueabihf-gcc](https://packages.ubuntu.com/focal/gcc-arm-linux-gnueabihf)

## 获取 SDK 源码

前文介绍了基础的开发环境搭建和使用方法，你应该了解什么是本地编译和交叉编译，下面开始介绍如何使用这些 sdk 源码开发程序。

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
>! 注意 `--recursive` 参数是必须的，用以克隆子模块，否则会缺代码。

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

### 借助 libmaix 实现（开发难度最小，适合验证）

基于 libmaix 的 axpi 项目进行开源快速验证效果，代码简单易懂，基于在线服务完成模型部署，只用于新手上路，与 ax-sample 的模型一起被支持。

- [axpi](https://github.com/sipeed/libmaix/tree/release/examples/axpi)
- [axpi_classification_cam](https://github.com/sipeed/libmaix/tree/release/examples/axpi_classification_cam)
- [axpi_yolov5_cam](https://github.com/sipeed/libmaix/tree/release/examples/axpi_yolov5_cam)

> 20221113 目前仓库只保证用户初次上手时能够不报错的安全调用 AI 模型，不代表芯片的最好效果。

### 借助 ax-pipeline 实现（开发难度适中，适合优化）

到了这里要有基本的芯片 bsp sdk 开发的基础（axpi_bsp_sdk），这部分会略显专业一些，这个仓库目前追求最高性能的效果。

- [准备编译环境](https://github.com/AXERA-TECH/ax-pipeline/blob/main/docs/compile.md)
- [如何更换自己训练的 yolov5 模型？](https://github.com/AXERA-TECH/ax-pipeline/blob/main/docs/how_to_deploy_custom_yolov5_model.md)
- [如何部署自己的其他模型](https://github.com/AXERA-TECH/ax-pipeline/blob/main/docs/how_to_deploy_custom_model.md)

### 借助 ipcdemo 实现（开发难度最大，适合落地）

基于 axpi_bsp_sdk 的 ipcdemo 商用视频推流应用，由于源码过于复杂，需要有上述基础才能介入。

- [axpi_bsp_sdk/app/IPCDemo](https://github.com/sipeed/axpi_bsp_sdk/tree/main/app/IPCDemo)