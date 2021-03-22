---
title: How to complie
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: How to complie
---


This article is an open source project development document written to help some users who want to become developers.

## Get maixpy ​​open source project

Please prepare the linux system environment (WSL on Windows is also possible), hook up the XXX proxy, enter `git clone https://github.com/sipeed/MaixPy` to pull the MaixPy warehouse code and submodules, and make sure to read the catalog after you get it [Build.md](https://github.com/sipeed/MaixPy/blob/master/build.md) document under.

> Students who do not have an agent can use the github mirror station list (`https://github.com/rc1844/fastgithub`) to accelerate the pull of the maixpy ​​repository. Please do not use gitee to pull the maixpy ​​repository, which will drop the submodule repository.

```
juwan@juwan-N85-N870HL:~$ git clone https://gitclone.com/github.com/sipeed/MaixPy
Cloning to'MaixPy'...
remote: Object count: 77517, completed.
remote: Compressed object: 100% (20929/20929), complete.
remote: Total 77517 (delta 56791), reused 76050 (delta 55761)
Among the recipients: 100% (77517/77517), 53.62 MiB | 972.00 KiB/s, completed.
Processing delta: 100% (56791/56791), complete.
juwan@juwan-N85-N870HL:~$ cd MaixPy/
juwan@juwan-N85-N870HL:~/MaixPy$ git submodule update --recursive --init
The submodule'components/kendryte_sdk/kendryte-standalone-sdk' (https://github.com/sipeed/kendryte-standalone-sdk) has been registered to the path'components/kendryte_sdk/kendryte-standalone-sdk'
The submodule'components/micropython/core' (https://github.com/micropython/micropython.git) has been registered to the path'components/micropython/core'
The submodule'components/micropython/port/src/lvgl/lv_bindings' (https://github.com/littlevgl/lv_binding_micropython.git) has been registered to the path'components/micropython/port/src/lvgl/lv_bindings'
The submodule'components/micropython/port/src/ulab/micropython-ulab' (https://github.com/Neutree/micropython-ulab.git) has been updated to the path'components/micropython/port/src/ulab/micropython -ulab' sign up
The submodule'components/spiffs/core' (https://github.com/pellepl/spiffs.git) has been registered to the path'components/spiffs/core'
The submodule'tools/flash/kflash_py' (https://github.com/sipeed/kflash.py.git) has been registered to the path'tools/flash/kflash_py'
The submodule'tools/kconfig/Kconfiglib' (https://github.com/ulfalizer/Kconfiglib.git) has been registered to the path'tools/kconfig/Kconfiglib'
The submodule'tools/spiffs/mkspiffs' (https://github.com/igrr/mkspiffs.git) has been registered to the path'tools/spiffs/mkspiffs'
Cloning to'/home/juwan/MaixPy/components/kendryte_sdk/kendryte-standalone-sdk'...
Cloning to'/home/juwan/MaixPy/components/micropython/core'...
```

Note that there is no acceleration in pulling the sub-repository after this, and you will try to pull it from github. You can also use the same method to pull the sub-module location separately (defined in `.gitmodules`). This document cannot help you Solve network problems.

> If https://gitclone.com is down, try to find other lines by yourself.

How to confirm whether the final submodule is pulled completely, you can enter `git submodule status`, please do not compile if it is incomplete, there will be errors.

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

### Compile maixpy ​​open source project

> This section assumes that you do not have any experience in building cross-compilation chains.

First press [build.md](https://github.com/sipeed/MaixPy/blob/master/build.md) to perform various operations in order. If you don’t speak English, you can open a translator.

The steps are as follows:

- nstall the necessary compilation tools and Python modules for the linux environment, and make sure cmake / make / python3 are available.
- Set the toolchain toolchain to the directory `/opt/kendryte-toolchain/` in the system to facilitate the SDK to find the compilation tool, and ensure that the /opt/kendryte-toolchain/bin/riscv64-unknown-elf-gcc compilation tool exists.
- Enter `cd projects/maixpy_k210` under the specific hardware project of MaixPy and enter `python3 project.py build` to start compiling.

This is the end of the entire compilation step. After successful compilation, you will get a build folder in the `projects/maixpy_k210` directory, which contains the following files:

- maixpy.bin will be burned to the K210 firmware at address 0x000000.
- maixpy.txt The content of the decompiled code corresponding to the current firmware, to help you check the information of the pointer address of the core dump.

Other files are .a and .o intermediate files generated during the compilation process and can be ignored.

### Burn maixpy ​​firmware to your hardware

Now you get the maixpy.bin firmware, insert the hardware, and then use `python3 project.py -B goE -p /dev/ttyUSB1 -b 1500000 flash` to burn the hardware. Take the `-B` parameter as an example.

```shell
juwan@juwan-N85-N870HL:~/Desktop/maixpy/projects/maixpy_k210$ python3 project.py -h
- SDK_PATH:/home/juwan/Desktop/maixpy
maixpy
usage: project.py [-h] [-p PORT] [-b BAUDRATE] [-t] [-n] [-s] [-B {dan,bit,bit_mic,goE,goD,maixduino,kd233,auto }] [-S] [--toolchain PATH] [--toolchain-prefix PREFIX]
                  [--config_file PATH] [--verbose]
                  {config,build,rebuild,menuconfig,clean,distclean,clean_conf,flash}

build tool, e.g. `python project.py build`
```

Among them, `-B goE` is the choice of version, and the optional items are `dan, bit, bit_mic, goE, goD, maixduino, kd233, auto` indicating the burning method, which has a lot to do with the specific hardware.

- Bit usually corresponds to the chip using CH340.

- maixduino usually corresponds to the chip using CH552.

Specifically, you can try a variety of options, and you can also choose the BAUDRATE option of burning frequency 115200 and 1.500000. Of course, no matter which configuration, as long as it can be burned in, you need to check the help description of -h for more usage methods.

The common burning process is as follows:

```shell
➜ maixpy_k210_minimum git:(master) ✗ sudo kflash -b 1500000 -p /dev/ttyUSB0 build/maixpy.bin
[sudo] fqr password:
[INFO] COM Port Selected Manually: /dev/ttyUSB0
[INFO] Default baudrate is 115200, later it may be changed to the value you set.
[INFO] Trying to Enter the ISP Mode...
._
[INFO] Automatically detected goE/kd233

[INFO] Greeting Message Detected, Start Downloading ISP
Downloading ISP: |============================================ ================================================= ============| 100.0% 10kiB/s
[INFO] Booting From 0x80000000
[INFO] Wait For 0.1 second for ISP to Boot
[INFO] Boot to Flashmode Successfully
[INFO] Selected Baudrate: 1500000
[INFO] Baudrate changed, greeting with ISP again ...
[INFO] Boot to Flashmode Successfully
[INFO] Selected Flash: On-Board
[INFO] Initialization flash Successfully
Programming BIN: |============================================= ================================================= ============| 100.0% 47kiB/s
[INFO] Rebooting...
```

### Command line to connect hardware & run code

You can basically use it up to this step.

Here is a recommendation for some quick operations of linux or micropython during development. First, you can use minicom or picocom serial tool to enter the MicroPython terminal (add `&& picocom /dev/ttyUSB0 -b 115200` after the burning command), then When entering micropython, you can press Ctrl + E to enter the paste mode, and then paste the code and enter Ctrl + D to end the input of the running code.

```python
>>>
hello world!
>>>
```

In this way, you have completed quick verification and development, but if you want to debug a certain piece of functional code, you can upload the code directly through the command line via [mpfshell-lite](https://github.com/junhuanchen/mpfshell-lite) , Reset and run, and then report an error and debug.

> Low-level development of dynamic languages ​​often operate in this way, so we want to thank all developers who do interpreter interfaces for doing a lot of interface verification.

## MaixPy project application description

Assuming that you already know how to use MaixPy project to develop, compile, and burn, then I will introduce the usage of some tools in depth, here only some common usage will be explained, and no detailed explanation will be expanded.

### Introduce cmake's project compilation method

cmake is a tool that compiles and generates Makefile after writing code and rules through CMakeLists.txt. The usage and details are independent of Baidu. Here is a simple structured cmake project [Get_static_library_by_cmake](https://github.com/junhuanchen/Get_static_library_by_cmake.git) for You run and learn by reference.


Before cmake, makefiles were used for project management. Until today, micropython officially still uses a double-layer Makefile + inclue (makefile) project to manage multi-version hardware.

But MaixPy only adds micropython to its environment as a dependent library package, so in fact the software architecture design of MaixPy is built around the form of K210 software components.

So you can go to the hello_world project in the maixpy ​​folder to see how it is composed.

- hello_world
  - build
  - compile
  - main
  - CMakeLists.txt
  - config_defaults.mk
  - project.py

The MaixPy project has prepared a template for you to build the K210 project. Ignore the process of project construction here, and focus on the project configuration part that needs to be compiled and linked, that is, CMakeLists.txt under main. Its content is as follows.

```cmake

############### Add include ##################
# list(APPEND ADD_INCLUDE "include"
#)
# list(APPEND ADD_PRIVATE_INCLUDE "")
############################################

############ Add source files #################
list(APPEND ADD_SRCS "src/main.cpp"
    )
# aux_source_directory(src ADD_SRCS)
# list(REMOVE_ITEM COMPONENT_SRCS "src/test2.c")
############################################

###### Add required/dependent components ######
list(APPEND ADD_REQUIREMENTS kendryte_sdk)
############################################

############ Add static libs ##################
# list(APPEND ADD_STATIC_LIB "lib/libtest.a")
############################################

register_component()

```

You can see that `ADD_SRCS` links a `src/main.cpp` code file as the program entry.

You can load modules from other places through `ADD_REQUIREMENTS`. For example, `list(APPEND ADD_REQUIREMENTS kendryte_sdk)` requests the SDK package `kendryte_sdk`.

What if you want to link your own nncase library? What about other library codes?

It can be directly changed to the code of `LINK_DIRECTORIES(/home/juwan/maixpy/projects/maixpy_old/main/src/nncase)` under the absolute path. The premise of this is that the library is provided by the cmake project of.

> Here is a demonstration of how to call your own nncase library during compilation, and read the project after combining these key information. It should be easier to use.

### How to package the micropython spiffs file system and share it

If you use MaixPy for development, you will find that MaixUI provides a file system file (img). When you flash the same img as the UI system, you will directly enter the UI interface after burning.

You need to know that MicroPython is a program starting from 0x0. In the program, the VFS (virtual file system) will be constructed in the [0xD00000, (0xD00000 + 0x300000)) interval of Flash through spiffs, which is defined in maixpy/projects/maixpy_xxxxx/config_defaults.mk owned.

```makefile
CONFIG_SPIFFS_SIZE=0x300000
CONFIG_SPIFFS_START_ADDR=0xD00000
```

> Only the use of tools is discussed here, without detailed explanation of its implementation.

And [spiffs](https://github.com/pellepl/spiffs) does not support directory structure, then we will find that the file name of ui's img in flash will have a name like `lib/core.py`, Under normal circumstances, it is impossible for us to create this file, so we need to package it with tools.

There is a gen_spiffs_image.py script in the tools/spiffs/mkspiffs directory to complete the function of this packaged image. For usage, please refer to the instructions in tools/spiffs/README.md.

- Prepare an fs folder under the spiffs directory, which contains the code or resource file content you want to package.
- Execute `python gen_spiffs_image.py ../../projects/maixpy_k210/config_defaults.mk` to get the maixpy_spiffs.img binary file.
- Burn the img obtained above to 0xD00000 to restore the content in the micropython file system.

If you make some small systems and publish them in this way, users will get the img file you provided and burn them in and you will immediately get the same environment as you. This is actually the same as publishing a system image based on a Linux system. of.

Now, have you learned it?

### MaixPy's continuous integration service (Travis CI)

Travis CI provides continuous integration services (Continuous Integration, CI for short). It binds the projects on Github, as long as there is new code, it will be automatically crawled. Then, provide a running environment, perform tests, complete the build, and deploy to the server.

Mention that MaixPy uses travis + tools/release.sh to compile the project and upload the compilation directory to the release server to complete the daily build. This is common in the automated build and compilation of various packages. You may be interested Try it yourself.

> [Continuous Integration Service Travis CI Tutorial](http://www.ruanyifeng.com/blog/2017/12/travis_ci_tutorial.html)

### How to better read open source project source code

Having said that, from a personal point of view, in addition to the basic requirement of reading code, if you want to better read the source code, there are different organizational structures for different projects. Any beginner who has just entered the industry , You can use the project you have experienced as an entry point, and gradually establish a complete software engineering awareness from the aspects of project architecture, source code, compilation, testing, and software release. It is also a good method to conduct in-depth knowledge learning around this, I hope you You can build a complete software engineering system through this article.

## Final reference

- bing.com + keyword + yourself
