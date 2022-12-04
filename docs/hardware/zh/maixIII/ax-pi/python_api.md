---
title: Maix-III AXera-Pi 开启 Python 编程吧！

---

## 前言

>**20221202** 后的系统镜像包内置了 `jupyter notebook`、`ax-pipline-api`、`pinpong` 的 **Python** 包。

为了帮助更多的初学者以及新手能快速的把 AXera-Pi 用起来，我们准备了一篇以 **jupyter notebook** 为例的 **Python** 文档。但在这之前需要准备好硬件设备，并根据前文的产品上手指南以及系统使用手册，如何在 AXera-Pi 上烧录及登陆系统、验证外设等一些 **Linux** 基础操作有一定的掌握了解，让我们后续开启 **Python** 编程的学习更如鱼得水！

## jupyter notebook

**Jupyter Notebook**：是基于网页的用于交互计算的应用程序。其可被应用于全过程计算：开发、文档编写、运行代码和展示结果。简而言之，它是以网页的形式打开，可以在网页页面中直接编写代码和运行代码，代码的运行结果也会直接在代码块下显示的程序。如在编程过程中需要编写说明文档，可在同一个页面中直接编写，便于作及时的说明和解释。
![jupyter_notebook](./../assets/jupyter_notebook.png)
### 基础用法

每个方框被称为单元格，单元格左侧会有 **蓝色** 或者 **绿色** 两种颜色。绿色表示编辑模式而蓝色表示命令模式。

**通用用法：**
- **Shift+ Enter：**运行单元格，且以命令模式切换到下一个单元格
- **Ctrl + Enter：**运行单元格，且进入命令模式
  
**编辑模式中：**

- **Esc**：进入命令模式
  
**命令模式中：**

- **h：**打开帮助
- **Enter：**进入编辑模式
- **x：**剪切单元格
- **c：**复制单元格
- **v：**粘贴单元格
- **dd：**删除整个单元格
- **ii：**终止运行
- **A：**向光标所在单元格上方添加单元格
- **B：**向下添加
- **M：**使得单元格变成 markdown 状态

<!-- ## 如何在 AXera-Pi 上启动？



## 如何连接 microbit 掌控版？
## 如何连接 ardunino 开发板？

待更新！

<!-- Python 编程大纲
1. 前言：为了方便用户快速把板子用起来 基于什么什么什么的基础 镜像内置了....
2. 介绍 jupyter notebook 
3. 基础用法
4. 如何在板子上启动
  - 终端/python 共用
  - 两种办法 直接用命令行启动 或者是用 python 启动
  - 在板子上的基础用法
5. 如何使用 python 连接 microbit/arduino?
  - 点灯
  - 使用 pinpong 库教程
  -  -->
<!-- ## Python API 编程

> 在 **20221125** 后更新的镜像内置了基于 ax-pipeline 的应用并支持可用 Python API 编程。

**ax_pipeline**：[点击查看相关仓库](https://github.com/junhuanchen/ax_pipeline_api)

使用之前需要替换最新 **20221125** 的镜像然后在终端安装 ax_pipeline_api 包。

```bash
pip3 install ax_pipeline_api -U
```
再使用以下命令行运行一下内置的 `pipeline.py` 即可在屏幕上看到效果

```bash
cd /home
python3 pipeline.py
```

关于如何修改摄像头型号、libxxx*so、model 之类的可以参考 readme 文档

### 支持 microbit 掌控板

连接 microbit 掌控版并使用 python 编程前需要准备好以下的材料。

- **microbit 掌控版以及 micro usb 数据线**
- **type-c usb 转接头**
- **Maix-III AXera-Pi 开发板以及 type-c 线** 
  
具体接线图待补充！

可在终端接入 `python3` 模式运行下方代码即可连接 microbit 掌控版并会看到 **hello world** 亮灯效果。

```bash
import time
from pinpong.board import Board,Pin
from pinpong.extension.microbit import *
Board("microbit","/dev/ttyACM0").begin()
display.show(Image.HEART)
while True:
    display.scroll("hello world")
```

![microbit](./../assets/microbit.jpg) --> -->