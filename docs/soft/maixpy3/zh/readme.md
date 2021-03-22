---
title: 什么是 MaixPy3 ？
keywords: maixpy3, linux, AIOT, 边缘计算
desc: maixpy doc: MaixPy 是什么？能做什么？
---

![MIT](https://img.shields.io/badge/license-MIT-blue.svg) [![PyPI version](https://badge.fury.io/py/MaixPy3.svg)](https://badge.fury.io/py/MaixPy3) ![Python](https://img.shields.io/badge/Python-3.5↗-ff69b4.svg) [![issue](https://img.shields.io/github/issues/sipeed/maixpy3.svg)](https://github.com/sipeed/maixpy3/issues)

MaixPy3 是基于 [cpython](https://github.com/python/cpython) 的 Python3 工具包，意在通过 Python 编程语言简化在 Linux 边缘设备上开发 AIoT （人工智能物联网） = AI（人工智能） + IoT（物联网）应用。


<div align="center" >
    <img src="./assets/images/main.png" style="width:480px; height:320px;" />
</div>

## 前言

物联网（Internet of Things，简称 IOT ）是指通过各种信息传感器、射频识别技术、全球定位系统、红外感应器、激光扫描器等各种装置与技术，实时采集任何需要监控、 连接、互动的物体或过程，采集其声、光、热、电、力学、化 学、生物、位置等各种需要的信息，通过各类可能的网络接入，实现物与物、物与人的泛在连接，实现对物品和过程的智能化感知、识别和管理。

AI 的介入让 IoT 有了连接的“大脑”。当 AI 、 IoT “一体化”后，“人工智能”逐渐向“应用智能”发展。深度学习需要物联网的传感器收集，物联网的系统，也需要靠人工智能做到正确的辨识、发现异常、预测未来。

而 2021 年 AIoT 边缘设备可能有如下应用场景：

涵盖领域：智能制造、工业物联网、智慧物流、智慧家居、智慧交通、智慧农业、智慧园区、智慧政务、智慧医疗、智慧零售等智能物联网各应用场景。

**所以 MaixPy3 会在 Python3 的基础上提供易用的 AI 功能模块**，如【**物体分类**】和【**人脸识别**】功能。

> 会优先适配 MaixPy 的物体检测、物体识别、物体分类等。由于芯片差异，部分功能可能不被实现。

## 以往嵌入式 Linux 设备是如何编程的？

当拿到一台嵌入式 Linux 边缘设备（例如：手机），与一台桌面计算机不同的是无法进行软件编译活动，那么要如何对它编程呢？

- 准备对应平台的交叉编译链
- 编写一段经典的 `hello world` 的 C 代码进行编译
- 链接各种依赖库
- 将编译好的程序送到目标设备上进行调试。

```c
#include <stdio.h>
int main() 
{
    printf("Hello, world\n");
    return 0
}
```

不出意外的话，你应该要花费不少时间学习如下内容。

- 学习如何编译程序
- 学习 C 语言语法
- 学习调试程序 Bug

那现在呢？

## “人生苦短，我用 Python 。”

如果你是下述人群，那么 Python 将会非常适合你。

- 对编程感兴趣却无从下手的
- 想轻松入门 AIoT 开发的
- 不了解，也不关心底层的
- 想愉快写代码（偷懒）的
- 想快速验证软硬件功能的

让我们使用 Python 编写一段经典的 `hello world` 程序吧！

```python
print('hello world')
print('1 + 1 = ?', 1 + 1)
```

### 体验一下？

<div align="center" >
    <iframe src="https://tool.lu/coderunner/embed/awD.html" style="width:90%; height:320px;" frameborder="0" mozallowfullscreen webkitallowfullscreen allowfullscreen></iframe>
</div>

> 在线 Python 编程 [runoob-python](https://www.runoob.com/try/runcode.php?filename=HelloWorld&type=python3) [google-colab](https://colab.research.google.com) 备用地址。

没错，现在你已经开始 Python 编程了。

## 就这？就这？？？

基于上述事实使用 MaixPy3 会给你带来如下编程体验。

- 使用 Python3 标准编程环境，而非 MicroPython 解释器。
- 提供专为 AIoT 应用开发有关的底层拓展模块。
- 支持不同芯片的 Linux 平台，自底向上的优化 Python 性能。
- 访问硬件外设的 Python 驱动代码，常见于各类传感器。
- 在 GitHub 开源的 [MaixPy3](https://github.com/sipeed/MaixPy3) 仓库。

说了这么多，不妨来看一些示例代码。

### 在屏幕上显示摄像头捕获的图像。

```python
from maix import display, camera

image = camera.capture()

display.show(image)
```

### 访问某个 I2C 外设，读写地址数据。

```python
from maix import i2c

i2c_device = '/dev/i2c-2'
device_address = 0x26
data_address = 0x01

i2c = i2c.I2CDevice(i2c_device, device_address)

i2c.write(data_address, b'\xAA')

print(i2c.read(data_address, 1))
```

### 加载 AI 模型后输入图像验证结果。

```python
from PIL import Image
from maix import nn

m = nn.load({
    "param": "resnet.param",
    "bin": "resnet.bin"
  }, opt={
    "model_type":  "awnn",
    "inputs": {
        "input0": (224, 224, 3)
    },
    "outputs": {
        "output0": (1, 1, 1000)
    },
    "first_layer_conv_no_pad": False,
    "mean": [127.5, 127.5, 127.5],
    "norm": [0.00784313725490196, 0.00784313725490196, 0.00784313725490196],
})

img = Image.open("input.jpg")
out = m.forward(img, quantize=True)
print(out.shape)
out = nn.F.softmax(out)
print(out.max(), out.argmax())
```

## 还想知道更多？

那就点选（↘）下一章节，了解更多吧！

> “Life is short. You need Python.”
