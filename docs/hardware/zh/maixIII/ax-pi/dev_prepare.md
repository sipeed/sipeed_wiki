---
title: Maix-III AXera-Pi 开发准备工作
---

> 本文假定你是一名不了解 linux 系统的开发方式的开发者，但知道 gcc 和 make 命令使用的相关专业工程师，如果你不了解 gcc 编译程序，可以先学习[Linux中gcc/g++ gdb make/Make 的基本使用和理解](https://blog.csdn.net/m0_46606290/article/details/123083945) 。

## 准备工作

欲善其事，必先利其器。在开始开发之前，需要准备好开发板、开发环境、开发工具等。

根据前面的章节，你掌握了开发板的 烧录系统 和 登录系统 等一系列 Linux 基础操作，这可以帮助你在开发过程中排查设备问题或调试驱动代码。

但接下来要开发程序就需要准备好开发环境和开发工具了，以下是给从来没接触过嵌入式 linux 系统开发的同学了解的内容，如软件工程的同学。

首先认识一下什么是交叉编译，通常来说，编译程序有交叉编译和本地编译两种情况，本地编译就是在本机上使用 gcc 进行编译运行程序（例如在 Visual Studio 上编译运行 hello world ），而交叉编译就是本机没有编译环境，需要在另一台机器上完成编译再送进来运行（例如在 Android Studio 上编译 apk 送到手机里安装程序运行）。

> 交叉编译是指在一种计算机架构上编译出另一种计算机架构的可执行程序。交叉编译的目的是为了在一种计算机架构上运行另一种计算机架构的程序。例如，可以在 x86 架构的计算机上编译出 ARM 架构的可执行程序，或者在 ARM 架构的计算机上编译出 x86 架构的可执行程序。交叉编译的目的是为了在一种计算机架构上运行另一种计算机架构的程序。例如，可以在 x86 架构的计算机上编译出 ARM 架构的可执行程序，或者在 ARM 架构的计算机上编译出 x86 架构的可执行程序。

两者的区别在于编译一些复杂大型软件，本机性能太弱内存又少，导致编译出来的时间太长，所以需要交叉编译来完成，比如 ax-sample 在本机完整编译需要十几分钟，而在一台高性能的桌面计算机上只需要数十秒即可。

所以从开发的角度来说，本机编译只是为了快速应用查看效果，真正得开发起来还是得交叉编译，就像原厂提供的 bsp sdk 一样，在计算机上完成编译后，再送进板子中运行。

## 本地编译

这里把 m3axpi 板子当作一台本地的微型 linux 服务器的角色来看待，使用 vscode remote 或 mobaxterm 这类远程开发工具连接到板子里，这样就可以得到一个本地的开发环境，可以在本地编辑代码后直接编译运行程序。

### vscode remote

vscode remote 是 vscode 的一个插件，可以直接连接到远程的 linux 服务器，然后在本地编辑代码，同步到远程服务器上编译运行，这里以一台 ubuntu20.04 的桌面计算机系统为例，只要能安装 vscode 编辑器软件计算机都行，这里只是为了示意如何连接到板子里。

安装插件：

```bash
sudo apt install code
code --install-extension ms-vscode-remote.remote-ssh
```

[附图]

连接到板子：

```bash
ssh root@192.168.233.1
```

[附图]

不想输入密码可以用 sshpass 类似这样。

```bash
sshpass -p root ssh root@192.168.233.1
```

接着就可以在 vscode 里编译运行 linux 系统的程序了，幸运的是在 debian 系统上可以直接通过 apt 得到本机的编译工具链，而不用交叉编译就可以直接编译运行程序，这些都已经提前准备好了，对用户来说可以节省不少搭建内部开发环境的时间。

所以可以直接在板子里编译运行 libmaix 项目：

```bash
cd /home/libmaix/examples/axpi/
python3 project.py build
fbon
./dist/start_app.sh
```

> 按 ctrl + c 中断停止程序直到退出。

附图：

### mobaxterm

在 Windows 上可以用 mobaxterm 这样的工具连接到板子进行 linux 服务器管理，但编译还是需要在 linux 系统上进行。

附图

## 交叉编译

在这之前已经有了本地编译，当发现本地内存和性能不能满足自身开发需求的时候，就要准备交叉编译了。

首先得有一台 linux 系统，如 ubuntu20.04 这样的桌面计算机，接着和上面一样，也可以在这台计算机上安装 vscode remote 或 idea clion 这类开发工具直接连接到板子里，这可以方便你编辑代码或传输文件。

### 更换交叉编译工具链

交叉编译工具链是用来编译 linux 系统的程序的，这里使用的是 arm-linux-gnueabihf 这个工具链，这个工具链是 debian / ubunutu 系统提供的，所以可以直接通过 apt 安装。

- `sudo apt install gcc-arm-linux-gnueabihf`

安装完成后，可以在 /usr/bin 目录下找到 `arm-linux-gnueabihf-gcc` 这个交叉编译工具，这个工具可以用来编译 linux 系统的程序。

```bash
juwan@juwan-n85-dls:~$ /usr/bin/arm-linux-gnueabihf-gcc -v
Using built-in specs.
COLLECT_GCC=arm-linux-gnueabihf-gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc-cross/arm-linux-gnueabihf/9/lto-wrapper
Target: arm-linux-gnueabihf
Configured with: ../src/configure -v --with-pkgversion='Ubuntu 9.4.0-1ubuntu1~20.04.1' --with-bugurl=file:///usr/share/doc/gcc-9/README.Bugs --enable-languages=c,ada,c++,go,d,fortran,objc,obj-c++,gm2 --prefix=/usr --with-gcc-major-version-only --program-suffix=-9 --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-libitm --disable-libquadmath --disable-libquadmath-support --enable-plugin --enable-default-pie --with-system-zlib --without-target-system-zlib --enable-libpth-m2 --enable-multiarch --enable-multilib --disable-sjlj-exceptions --with-arch=armv7-a --with-fpu=vfpv3-d16 --with-float=hard --with-mode=thumb --disable-werror --enable-multilib --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=arm-linux-gnueabihf --program-prefix=arm-linux-gnueabihf- --includedir=/usr/arm-linux-gnueabihf/include
Thread model: posix
gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1)
```

用本地编译同样的方式编译 libmaix 只是这一次多了一个 scp 拷贝文件夹的步骤，将 libmaix 编译出来的程序，上传到板子运行即可。

唯一不同的地方在于提供交叉编译链的地方需要修改，如：python3 project.py --board=axpi --toolchain /usr/bin --toolchain-prefix arm-linux-gnueabihf- config 之中的编译链可能会发生改变，这里需要根据你的实际情况进行修改，比如本机环境下可能有多个编译链，但一般来说是不需要修改的。

假设要移到另一台 X86 的 PC 上，还需要修改编译配置中所需要的依赖文件：

```
        list(APPEND ADD_INCLUDE "lib/arch/axpi/joint"
                                "lib/arch/axpi/opt/include"
                                "lib/arch/axpi/opt/include/opencv4"
        )
        "/lib/aarch64-linux-gnu/libm.so"
        "/lib/aarch64-linux-gnu/libpthread.so"
        "/lib/aarch64-linux-gnu/libopencv_videoio.so"
        "/lib/aarch64-linux-gnu/libopencv_highgui.so"
        "/lib/aarch64-linux-gnu/libopencv_imgcodecs.so"
        "/lib/aarch64-linux-gnu/libopencv_imgproc.so"
        "/lib/aarch64-linux-gnu/libopencv_core.so"
        "/lib/aarch64-linux-gnu/libopencv_freetype.so"
```

当换了编译链后也要修改到其他路径下的链接库：

```
        list(APPEND ADD_INCLUDE "lib/arch/axpi/joint"
                                "/opt/include"
                                "/usr//local/include/opencv4"
        )
        "/lib/arm-linux-gnueabihf/libm.so"
        "/lib/arm-linux-gnueabihf/libpthread.so"
        "/lib/arm-linux-gnueabihf/libopencv_videoio.so"
        "/lib/arm-linux-gnueabihf/libopencv_highgui.so"
        "/lib/arm-linux-gnueabihf/libopencv_imgcodecs.so"
        "/lib/arm-linux-gnueabihf/libopencv_imgproc.so"
        "/lib/arm-linux-gnueabihf/libopencv_core.so"
        "/lib/arm-linux-gnueabihf/libopencv_freetype.so"
```

当然，具体问题还需要具体分析，总之换了桌面系统和编译链，对应的一些文件可能也会发生改变。


**所以这里我提供了一种不用改变编译环境即可完成交叉编译，可以借助 `docker qemu` 虚拟机上完成板上交叉编译：[[maixpy3 axpi] 编辑发布 debian 镜像与在 PC 上交叉编译程序](https://www.cnblogs.com/juwan/p/16769237.html)**

## 总结

本文介绍了如何在 linux 系统上编译运行 libmaix 项目，以及如何在 linux 系统上交叉编译 libmaix 项目，希望对大家有所帮助。

只要掌握了如何管理开发环境和如何编译运行 libmaix 项目，接下来就可以基于官方提供的 sdk 开发属于自己的项目了。

## 参考

* [什么是交叉编译？](https://cn.bing.com/search?q=%E4%BB%80%E4%B9%88%E6%98%AF%E4%BA%A4%E5%8F%89%E7%BC%96%E8%AF%91%EF%BC%9F)
* [超详细解答vscode如何远程连接Linux以及可能会出现的一些问题](https://blog.csdn.net/cxn15335120506/article/details/123238233)
* [vscode remote](code.visualstudio.com/docs/remote/remote-overview)
* [ssh scp 是什么？](https://cn.bing.com/search?q=ssh+scp+%E6%98%AF%E4%BB%80%E4%B9%88%EF%BC%9F)
* [libmaix](github.com/sipeed/libmaix)
* [mobaxterm](mobaxterm.mobatek.net)
* [arm-linux-gnueabihf-gcc](packages.ubuntu.com/focal/gcc-arm-linux-gnueabihf)
