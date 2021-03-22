---
title: 如何编译
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 如何编译
---


本文是为了帮助一些想要成为开发者的用户而写的开源项目の开发文档。

## 获取 maixpy 开源项目

请准备 linux 系统环境（在 Windows 上使用 WSL 也可以），挂上 XXX 代理，输入 `git clone https://github.com/sipeed/MaixPy` 拉取 MaixPy 仓库代码和子模块，确保拿到后阅读目录下的 [build.md](https://github.com/sipeed/MaixPy/blob/master/build.md) 文档。

> 没有代理的同学可以用 github 镜像站列表（`https://github.com/rc1844/fastgithub`）加速拉取 maixpy 仓库，请不要用 gitee 拉取 maixpy 仓库，会掉子模块仓库的。

```
juwan@juwan-N85-N870HL:~$ git clone https://gitclone.com/github.com/sipeed/MaixPy
正克隆到 'MaixPy'...
remote: 对象计数中: 77517, 完成.
remote: 压缩对象中: 100% (20929/20929), 完成.
remote: Total 77517 (delta 56791), reused 76050 (delta 55761)
接收对象中: 100% (77517/77517), 53.62 MiB | 972.00 KiB/s, 完成.
处理 delta 中: 100% (56791/56791), 完成.
juwan@juwan-N85-N870HL:~$ cd MaixPy/
juwan@juwan-N85-N870HL:~/MaixPy$ git submodule update --recursive --init
子模组 'components/kendryte_sdk/kendryte-standalone-sdk'（https://github.com/sipeed/kendryte-standalone-sdk）已对路径 'components/kendryte_sdk/kendryte-standalone-sdk' 注册
子模组 'components/micropython/core'（https://github.com/micropython/micropython.git）已对路径 'components/micropython/core' 注册
子模组 'components/micropython/port/src/lvgl/lv_bindings'（https://github.com/littlevgl/lv_binding_micropython.git）已对路径 'components/micropython/port/src/lvgl/lv_bindings' 注册
子模组 'components/micropython/port/src/ulab/micropython-ulab'（https://github.com/Neutree/micropython-ulab.git）已对路径 'components/micropython/port/src/ulab/micropython-ulab' 注册
子模组 'components/spiffs/core'（https://github.com/pellepl/spiffs.git）已对路径 'components/spiffs/core' 注册
子模组 'tools/flash/kflash_py'（https://github.com/sipeed/kflash.py.git）已对路径 'tools/flash/kflash_py' 注册
子模组 'tools/kconfig/Kconfiglib'（https://github.com/ulfalizer/Kconfiglib.git）已对路径 'tools/kconfig/Kconfiglib' 注册
子模组 'tools/spiffs/mkspiffs'（https://github.com/igrr/mkspiffs.git）已对路径 'tools/spiffs/mkspiffs' 注册
正克隆到 '/home/juwan/MaixPy/components/kendryte_sdk/kendryte-standalone-sdk'...
正克隆到 '/home/juwan/MaixPy/components/micropython/core'...
```

注意，这之后拉取子仓库是没有加速的，会从 github 试图拉取，你也可以用同样的方法单独拉取子模块位置（在 `.gitmodules` 中定义），本篇文档是无法帮你解决网络问题的。

> 如果 https://gitclone.com 挂了，就自己想办法找其他线路吧。

如何确认最终子模块是否拉取完整，可以输入 `git submodule status`，不完整请不要进行编译，必出错误。

```shell
juwan@juwan-N85-N870HL:~/Desktop/maixpy$ git submodule status 
 7fdb511fe61026eec5874885de5981c4f60f664d components/kendryte_sdk/kendryte-standalone-sdk (v0.5.2-181-g7fdb511)
 ced340d739e84737dd5c8e6b4ab9af2ea44e29e7 components/micropython/core (v1.11-64-gced340d73)
 ddf09164ee1711a61169030a7ee8bf370ee5743f components/micropython/port/src/lvgl/lv_bindings (remotes/origin/dev-6.0-32-gddf0916)
 c315a571df49a19b843f7dffc300c21ccb7d4edd components/micropython/port/src/ulab/micropython-ulab (0.24-27-gc315a57)
 ec68ba8208d7550860e4e78299d58a529b88bf85 components/spiffs/core (0.2-234-gec68ba8)
 1ef6f4c0b2cb8b1872b6ffe9337f4e02d5487fa6 tools/flash/kflash_py (v1.0-79-g1ef6f4c)
 53c72959ac4d71f99913e4b0eea99261a6585430 tools/kconfig/Kconfiglib (v12.12.1-14-g53c7295)
 983970e40ff381d95d68a9bddff70c4d9921021b tools/spiffs/mkspiffs (0.2.3-6-g983970e)
```

### 编译 maixpy 开源项目

> 这节内容假设你没有任何搭建交叉编译链的经验。

首先按 [build.md](https://github.com/sipeed/MaixPy/blob/master/build.md) 顺序执行各种操作即可，如果你不会英文你可以开翻译机。

步骤说明如下：

- 给 linux 环境安装必须的编译工具和 Python 模块，确保 cmake / make / python3 可用。
- 设置 toolchain 工具链到系统 `/opt/kendryte-toolchain/` 目录下，方便 SDK 寻找编译工具，确保存在 /opt/kendryte-toolchain/bin/riscv64-unknown-elf-gcc 编译工具。
- 进入到 MaixPy 的具体硬件项目下 `cd projects/maixpy_k210` 然后输入 `python3 project.py build` 开始编译。

整个编译步骤就这样结束了， 编译成功后你就会在 `projects/maixpy_k210` 目录下得到一个 build 文件夹，里面有如下文件：

- maixpy.bin 将要被烧录到 0x000000 地址的 K210 固件。
- maixpy.txt 当前固件对应的反编译代码内容，辅助你排查 core dump 的指针地址的信息。

其他文件是编译过程中产生的 .a 和 .o 中间编译文件，可忽略。

### 烧录 maixpy 固件到你的硬件

现在你拿到了 maixpy.bin 固件，插入硬件，然后使用 `python3 project.py -B goE -p /dev/ttyUSB1 -b 1500000 flash` 烧录硬件，以 `-B` 参数为例。

```shell
juwan@juwan-N85-N870HL:~/Desktop/maixpy/projects/maixpy_k210$ python3 project.py -h
-- SDK_PATH:/home/juwan/Desktop/maixpy
maixpy
usage: project.py [-h] [-p PORT] [-b BAUDRATE] [-t] [-n] [-s] [-B {dan,bit,bit_mic,goE,goD,maixduino,kd233,auto}] [-S] [--toolchain PATH] [--toolchain-prefix PREFIX]
                  [--config_file PATH] [--verbose]
                  {config,build,rebuild,menuconfig,clean,distclean,clean_conf,flash}

build tool, e.g. `python project.py build`
```

其中 `-B goE` 是选择版型，可选的项有 `dan,bit,bit_mic,goE,goD,maixduino,kd233,auto` 表示烧录方式，这个和具体硬件有很大关系。

- bit 通常对应使用 CH340 的芯片。

- maixduino 通常对应使用 CH552 的芯片。

具体你可以多种试试，还可以选择烧录频率 115200 、1500000 的 BAUDRATE 选择，当然，无论是哪种配置，只要能烧录进去就行，更多的使用方法你需要查看 -h 的帮助说明。

常见的烧录过程如下：

```shell
➜  maixpy_k210_minimum git:(master) ✗ sudo kflash -b 1500000 -p /dev/ttyUSB0 build/maixpy.bin
[sudo] fqr 的密码： 
[INFO] COM Port Selected Manually:  /dev/ttyUSB0 
[INFO] Default baudrate is 115200 , later it may be changed to the value you set. 
[INFO] Trying to Enter the ISP Mode... 
._
[INFO] Automatically detected goE/kd233 

[INFO] Greeting Message Detected, Start Downloading ISP 
Downloading ISP: |============================================================================================================| 100.0% 10kiB/s
[INFO] Booting From 0x80000000 
[INFO] Wait For 0.1 second for ISP to Boot 
[INFO] Boot to Flashmode Successfully 
[INFO] Selected Baudrate:  1500000 
[INFO] Baudrate changed, greeting with ISP again ...  
[INFO] Boot to Flashmode Successfully 
[INFO] Selected Flash:  On-Board 
[INFO] Initialization flash Successfully 
Programming BIN: |============================================================================================================| 100.0% 47kiB/s
[INFO] Rebooting... 
```

### 命令行连接硬件 & 运行代码

到这一步基本都会使用了吧。

这里推荐一下开发时的一些 linux 或 micropython 的快速操作，首先可以使用 minicom 或 picocom 串口工具进入 MicroPython 终端（在烧录命令后加上 ` && picocom /dev/ttyUSB0 -b 115200` 就可以了），接着进入到 micropython 可以按下 Ctrl + E 进入粘贴模式，然后粘贴代码后输入 Ctrl + D 结束输入运行代码。

```python
>>> 
hello world!
>>> 
```

这样你就完成了快速的验证和开发，但如果你是要调试某一段功能代码，你可以通过 [mpfshell-lite](https://github.com/junhuanchen/mpfshell-lite) 直接命令行上传代码，复位就运行，然后报错和调试。

> 底层开发动态语言经常这样操作，所以要感谢所有做解释器接口的开发者做了大量的接口验证。

## MaixPy 项目应用说明

假设已经知道如何使用 MaixPy 工程进行开发、编译、烧录，接下来将深入介绍一些工具的用法，这里面只交待一些常见用法，并不会展开细节说明。

### 介绍 cmake 的工程编译方法

cmake 是通过 CMakeLists.txt 编写代码和规则后编译生成 Makefile 的工具，用法和细节自行百度，这里有一个结构简单的 cmake 工程[Get_static_library_by_cmake](https://github.com/junhuanchen/Get_static_library_by_cmake.git)供你运行和参考学习。


在没有 cmake 之前，都是使用 makefile 的方式进行工程管理，直到今天 micropython 官方也依然是使用双层 Makefile + inclue(makefile) 的工程管理多版型硬件的方法。

但 MaixPy 只把 micropython 当做一个依赖库包加入到自己的环境当中，所以实际上 MaixPy 的软件架构设计是围绕着 K210 软件组件的形式进行构建的。

因此可以来到 maixpy 文件夹里存在一个 hello_world 的工程，让看看它是怎么构成的。

- hello_world
  - build
  - compile
  - main
  - CMakeLists.txt
  - config_defaults.mk
  - project.py

MaixPy 项目已经准备了一个模板提供给你进行 K210 的项目构建，这里忽略项目构建的过程，重点关注需要可以编译链接的工程配置部分，也就是 main 下的 CMakeLists.txt ，它的内容如下。

```cmake

############### Add include ###################
# list(APPEND ADD_INCLUDE "include"
#     )
# list(APPEND ADD_PRIVATE_INCLUDE "")
###############################################

############ Add source files #################
list(APPEND ADD_SRCS  "src/main.cpp"
    )
# aux_source_directory(src ADD_SRCS)
# list(REMOVE_ITEM COMPONENT_SRCS "src/test2.c")
###############################################

###### Add required/dependent components ######
list(APPEND ADD_REQUIREMENTS kendryte_sdk)
###############################################

############ Add static libs ##################
# list(APPEND ADD_STATIC_LIB "lib/libtest.a")
###############################################

register_component()

```

可以看到 `ADD_SRCS` 链接了一个 `src/main.cpp` 代码文件作为程序入口。

通过 `ADD_REQUIREMENTS` 就可以加载其他地方的模块进来，例如 `list(APPEND ADD_REQUIREMENTS kendryte_sdk)` 则请求了 `kendryte_sdk` 这个 SDK 包。

如果想要链接自己的 nncase 库呢？其他库代码呢？

可以直接则改为绝对路径下的 `LINK_DIRECTORIES(/home/juwan/maixpy/projects/maixpy_old/main/src/nncase)` 的代码就可以了，这样做的前提是这个库是由 cmake 工程的方式提供的。

> 这里示范了如何在编译调用自己的 nncase 库，结合这些关键讯息再去阅读工程，应该就可以较为轻松的用起来了吧。

### 如何打包 micropython spiffs 文件系统分享出来

如果你深入使用了 MaixPy 进行开发，你会发现 MaixUI 提供了一种文件系统文件（img），当你刷入这个 UI 系统一样的 img ，你就会在烧录后直接进入 UI 界面。

需要知道 MicroPython 是从 0x0 开始的程序，在程序中会通过 spiffs 在 Flash 的 [0xD00000, (0xD00000 + 0x300000)) 区间构建 VFS （虚拟文件系统），是由 maixpy/projects/maixpy_xxxxx/config_defaults.mk 中定义得到的。

```makefile
CONFIG_SPIFFS_SIZE=0x300000
CONFIG_SPIFFS_START_ADDR=0xD00000
```

> 这里只讨论工具的使用，而不对其实现做详解。

而 [spiffs](https://github.com/pellepl/spiffs) 是不支持目录结构的，那么我们会发现 ui 的 img 在 flash 里的文件名称会存在 `lib/core.py` 这样的名称，而正常情况下我们是不可能将这个文件创建起来的，所以要通过工具将其打包。

在 tools/spiffs/mkspiffs 目录下有 gen_spiffs_image.py 脚本完成这个打包镜像的功能，用法请看 tools/spiffs/README.md 说明。

- 在 spiffs 目录下准备一个 fs 文件夹，包含你要打包的代码或资源文件内容。
- 执行 `python gen_spiffs_image.py ../../projects/maixpy_k210/config_defaults.mk` 即可得到 maixpy_spiffs.img 二进制文件。
- 将上述得到的 img 烧入到 0xD00000 就恢复 micropython 的文件系统里的内容。

如果你做了一些小系统，用这样的方式发布，用户拿到你提供的 img 文件，烧入就可以立刻得到和你一样的环境啦，这其实和基于 Linux 系统发布某系统镜像的结构是一样的。

现在，你学会了吗？

### MaixPy 的持续集成服务（Travis CI）

Travis CI 提供的是持续集成服务（Continuous Integration，简称 CI）。它绑定 Github 上面的项目，只要有新的代码，就会自动抓取。然后，提供一个运行环境，执行测试，完成构建，还能部署到服务器。

提及一下 MaixPy 是有借助 travis + tools/release.sh 完成项目的编译后，将编译目录上传到了发布服务器上从而完成了每日构建，这常见于各类包的自动化构建与编译，感兴趣不妨自己亲手试试。

> [持续集成服务 Travis CI 教程](http://www.ruanyifeng.com/blog/2017/12/travis_ci_tutorial.html)

### 如何更好的阅读开源项目源代码

说到这里，以个人的角度来看，基于阅读代码这种基本功要求之外，想要更好的阅读源代码，对于不同的项目有不同的组织架构，任何一位刚进入这个行业的初学者，可以用亲身经历的项目作为切入点，逐渐从项目架构、源码、编译、测试、发布软件等方面建立起完整的软件工程意识，围绕此进行知识的深入学习也是一种不错的手段，希望你能通过这篇文章建立起完整的软件工程体系吧。

## 最后的参考资料

- bing.com + keyword + yourself 
