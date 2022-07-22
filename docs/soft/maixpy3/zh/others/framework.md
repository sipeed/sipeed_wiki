---
title: MaixPy3 架构介绍
keywords: MaixPy, MaixPy3, Python, Python3, MicroPython
desc: maixpy doc: 认识项目整体框架（开发文档）
---

## 前言：开发基础

> 本文为大佬鼠为开发者写下的指导文，希望你可以基于此进入嵌入式开发的领域。

想要让 MaixPy3 软件体系更合乎你的心意，你需要花一点时间了解一下它的整体架构。

掌握了它后，你就可以得到一个非常巨大的究极缝合怪，里面有开源的大量的代码供你测试和参考。

这一切需要你需要具备以下基础技能：

- 拥有一台 Linux 系统的电脑，至少安装了 Ubuntu20 也可以是你喜欢的桌面操作系统。
- 知道什么是 gcc 、python3 、 opencv 、openmv 等相关软件的基础用法。
- 最好有过 openwrt 、 buildroot 、debian 等 linux 的应用基础。
- 了解 python3 的编译与安装，了解什么是交叉编译安装软件。

如果你完全不知道上面的内容，你可以到网上获取一些资料学习一些基本内容后再继续会好一些。

## 项目架构一览

鼠鼠我设计的这个项目是基于 linux cpython 自顶向下设计的，它受到以下需求约束。

- 用户需要 Python 语言调参验证原型功能，也需要 C / C++ 优化性能和减少内存占用用于开发商业项目。

- 尽可能最大程度的跨平台支持 Python / C++ / C 开发框架。

所以形成了两大 [libmaix](github.com/sipeed/libmaix) [maixpy3](github.com/sipeed/maixpy3) 开发仓库，前者为 C / C++ ，后者为 Python / C / C++ 实现。

对应的系统层级关系如下：

```bash
+----------------------------------------+
|                                        |
|    User develop sipeed all product.    |
|                                        |
+----------------------------------------+

+-----------------+     +----------------+
|                 |     |                |
| Run Python Code |     | Run C/C++ Code |
|                 |     |                |
+--------^--------+     +-------^--------+
         |                      |
   +-----+-----+                |
   |           |                |
   |  maixpy3  |                |
   |           |                |
   +-----^-----+                |
         |                      |
    +----+----+                 |
    |         |                 |
    | libmaix +-----------------+
    |         |
    +----^----+
         |
+----------------------------------------+
|  +-------------+                       |
|  |             |   openwrt   debian    |
|  |    Linux    |                       |
|  |             |   armbian   ubuntu    |
|  +-------------+                       |
+-------------------------+------------+-+
      ^        ^          ^            ^
      |        |          |            |
+-----++ +-----++ +-------++ +---------+-+
|      | |      | | x86/64 | |  AX620A   |
| V83X | | R329 | | debian | |   V85X    |
|      | |      | | ubuntu | |  more...  |
+------+ +------+ +--------+ +-----------+

```

所以项目的目录结构如下：

```bash

juwan@juwan-n85-dls:~/v83x/MaixPy3$ tree -I build -I "source|test|reference|common|CMake|words|waves|utils|asr_lib|tea|assets|tools|inc|src|lib|include|compile|dist|main|example|doc|lvgl" -P . > result.log
juwan@juwan-n85-dls:~/v83x/MaixPy3$ cat result.log
.
├── docs
├── envs
├── ext_modules
│   ├── libi2c
│   │   └── tests
│   ├── libmaix
│   │   ├── components
│   │   │   ├── libmaix
│   │   │   ├── maix_cv_image
│   │   │   ├── maix_speech
│   │   │   │   ├── Maix-Speech
│   │   │   │   │   ├── components
│   │   │   │   │   └── projects
│   │   │   │   │       └── maix_asr
│   │   │   │   └── mfcc-with-vad
│   │   │   │       └── alsa
│   │   │   │           └── sound
│   │   │   └── third_party
│   │   │       ├── apriltag
│   │   │       ├── cJSON
│   │   │       ├── imlib
│   │   │       ├── libjpeg
│   │   │       ├── sqlite3
│   │   │       └── zbar
│   │   └── examples
│   │       ├── camera
│   │       ├── display
│   │       ├── hello-world
│   │       ├── imlib_test
│   │       ├── mpp_v83x_vivo
│   │       ├── nn_mask
│   │       ├── nn_r329_mobilenet2
│   │       ├── nn_r329_shufflenet
│   │       ├── nn_resnet
│   │       ├── nn_retinaface
│   │       ├── nn_retinaface_mdsc
│   │       ├── nn_yolo_20class_mdsc
│   │       ├── nn_yolo2_card_mdsc
│   │       ├── nn_yolo2_person_mdsc
│   │       ├── nn_yolo_number
│   │       ├── nn_yolo_person
│   │       ├── nn_yolo_traffic
│   │       ├── self_learn_classifier
│   │       ├── speech_asr
│   │       ├── speech_mfcc
│   │       └── third_party_demo
│   ├── _maix
│   ├── _maix_camera
│   ├── _maix_display
│   ├── _maix_image
│   ├── _maix_nn
│   ├── _maix_nn_decoder
│   ├── _maix_nn_functional
│   ├── _maix_nn_mdsc
│   ├── _maix_nn_new
│   ├── _maix_speech
│   └── _maix_vivo
├── maix
│   ├── _maix_vision_
│   └── nn
│       ├── app
│       │   ├── classifier
│       │   └── face
│       └── decoder
└── tests
    ├── general
    └── maix_v831

68 directories, 0 files

```

可以得知我们开发的层级关系是对应起来的。

- 在 libmaix 中开发的成果会被转化成 maixpy3 的接口，通过了底层 C/C++ 开发 components 的 examples 测试，这样就不用在 Python 解释器中开发第二遍，因为在 Python 解释器里调试是非常困难的。

- 想要适配 MaixPy3 就需要在 libmaix 中移植新的平台，并且经过适配 display / camera / image / nn 等适配，目前已经适配了 V83X / R329 / desktop （无 nn 模块）等平台，按这个流程来适配一个新的芯片平台。

- 如果有新功能、新的试验代码，不一定会立刻提交提供给社区用户，而是采用 libmaix examples 的方式去验证、测试、合并，这样可以处理一些不好跨平台的实现，直到大多数平台都满足要求了就可以合并回 maixpy3 的仓库代码里。

- 接口采用迭代的方式去实现，比如同样的功能可以使用 C 开发也可以 C++ 开发，但最终链接回特定位置的模块是可以选择的，而这部分的选择交给 MaixPy 的 maix 模块来控制 import 的模块。

## 产品的开发、测试、发布顺序

一般划分为以下几类：

- 系统移植

- 驱动适配

- 图像处理

- 神经网络

## 用户应用公开的标准

最好按这个流程来走，不然很大概率会返工。

- 测试文档

- 用户文档

- 开发文档

