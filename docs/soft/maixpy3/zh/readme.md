---
title: 什么是 MaixPy3 ？
keywords: Maixpy3官方文档
desc: maixpy doc: MaixPy3 是什么？能做什么？
---

<p align="center">
    <img src="./assets/images/main.png" style="width:480px; height:320px;" />
</p>

# MaixPy3 ![GitHub forks](https://img.shields.io/github/forks/sipeed/maixpy3.svg?style=social) ![GitHub stars](https://img.shields.io/github/stars/sipeed/maixpy3.svg?style=social) ![GitHub watchers](https://img.shields.io/github/watchers/sipeed/maixpy3.svg?style=social)

[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) [![PyPI version](https://badge.fury.io/py/maixpy3.svg)](https://badge.fury.io/py/maixpy3) ![Python](https://img.shields.io/badge/Python-3.5↗-ff69b4.svg) ![issue](https://img.shields.io/github/issues/sipeed/maixpy3.svg)

2020 年由 [Sipeed](https://www.sipeed.com/) 推出的 MaixPy3 开源软件是基于 [cpython](https://github.com/python/cpython) 的 Python3 集成环境包，意在借助 Python 编程语言，简化和统一 Linux 嵌入式设备上开发 AIoT （人工智能物联网） = AI（人工智能） + IoT（物联网）应用的流程，产品的特色主要侧重于视觉或听觉的 AI 应用评估和落地。

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
- 使用过同类评估或开发板的

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
- 访问硬件外设的 Python 驱动代码，支持常见的各类传感器。
- 在 GitHub 开源的 [MaixPy3](https://github.com/sipeed/MaixPy3) 仓库。

说了这么多，不妨来看一下产品的介绍吧！（目前先占个坑）

<iframe src="//player.bilibili.com/player.html?aid=549271067&bvid=BV1Uq4y1u7R4&cid=444211683&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

> “Life is short. You need Python.”
