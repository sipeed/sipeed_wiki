---
title: Maix-III AXera-Pi 开启 Python 编程吧！

---
## 什么是 Python?

待更新

## 与 C++ 相比有什么区别？ 

待更新

<!-- >**20221202** 后的系统镜像包内置了 `jupyter notebook`、`ax-pipline-api`、`pinpong` 的 **Python** 包。

为了帮助更多的初学者以及新手能快速的把 AXera-Pi 用起来，我们准备了一篇以 **jupyter notebook** 为例的 **Python** 文档。但在这之前需要准备好硬件设备，并根据前文的产品上手指南以及系统使用手册，如何在 AXera-Pi 上烧录及登陆系统、验证外设等一些 **Linux** 基础操作有一定的掌握了解，让我们后续开启 **Python** 编程的学习更如鱼得水！ -->

## jupyter notebook

**Jupyter Notebook**：是基于网页的用于交互计算的应用程序。其可被应用于全过程计算：开发、文档编写、运行代码和展示结果。简而言之，它是以网页的形式打开，可以在网页页面中直接编写代码和运行代码，代码的运行结果也会直接在代码块下显示的程序。如在编程过程中需要编写说明文档，可在同一个页面中直接编写，便于作及时的说明和解释。
![jupyter_notebook](./../assets/jupyter_notebook.png)

### 如何启动并访问？

基于 AXera-Pi 前面章节的学习，我们可以借助产品上手以及系统使用手册，掌握一定的如何在 AXera-Pi 上烧录及登录系统、验证外设等一些基础的 Linux 操作，让我们在后续的学习 Python 更如鱼得水！

- [产品上手指南](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/flash_system.html)
- [系统使用手册](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/basic_usage.html)

**启动前需要进行准备工作：**

我们需要准备一台 AXera-Pi 设备，并通电接入 PC 端登录上终端，使用 `ifcomfig -a` 查询 IP 地址已作后续访问 `jupyter Notebook` 备用。

**如何启动并访问 jupyter Notebook：**

当得知设备的 IP 地址后在终端输入 `jupyter notebook` 命令启动它，终端会返回启动信息。

![api_adb](./../assets/api_adb.jpg)

这时我们可以打开任意浏览器，输入准备工作查询到的 `eth0` 或 `wlan0` IP 地址后缀加上 `:8888`**（例：192.168.2.49:8888）**后即可直接访问网页。网页会提醒你需要输入密码 **`Password:root`** 访问。
![api_root](./../assets/api_root.png)

## 如何使用 Notebook ？

<!-- jupyter Notebook 本质上是一个 web 应用程序，我们可以在上面书写代码，但是代码本身的运行环境是需要自己安装的，没有运行环境，即使是在 jupyter notebook 里面书写的代码怡然没有办法运行。因为代码本身，web 应用程序是不认识的。

幸运的是，在使用anaconda安装的时候，会默认将安装jupyter，而且会安装一个Python的运行环境，所以打开jupyter的时候，可以直接看见这个运行环境，在jupyter里面称之为内核kernel，如下所示：

在右上角点击下拉按钮，会得到如图所示的结果， -->

<!-- ![]() -->

**Python3：**表示的就是默认的python3 kernel，它是随着anaconda一起安装的；

**Text File：**表示的是新建一个文本文件

**Folder：**表示的是新建一个文件夹

**Terminal：**表示的是在浏览器中新建一个用户终端，类似于 shell/adb 终端

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

<!-- ## 如何使用 Python Pillow 进行图像处理并显示？

## 如何使用 Python 调用 Ai 模型获取结果？

## 如何使用 Python 调用 opencv 或 numpy ？

## 如何使用控制 arduino uno 或 microbit ？ -->

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