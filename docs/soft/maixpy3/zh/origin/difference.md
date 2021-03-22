---
title: MaixPy 与 MaixPy3 的区别
keywords: MaixPy, MaixPy3, Python, Python3, MicroPython
desc: maixpy doc: MaixPy3
---

## 区别是？

因为使用 MaixPy 的同学可能有两类人群，一类是从 MicroPython 一路使用过来的，另一类是从 Python3 过来的，所以针对两边的差异，分别做一下说明。

可以这样理解，它们都是专门为 AIoT 提供的 Python 开发环境，提供了各种各样的模块。

- MaixPy 指的是基于 MicroPython 的环境制作的。

- MaixPy3 指的是基于 Linux Python3 的环境制作的。

> 前者是基于 MCU 无系统的，后者是基于 Linux 系统。

除了基本的 Python3 语法一致，在提供的模块方面的存在着不小的差异。

### Python3 与 MicroPython 的区别

大多数时候，Python 的发展以 Python3 为主，以下列出一些与 Python3 的差异化信息。

- MicroPython 和 Python3 在 Python 语法上保持高度的一致性，常用的标准语法命令都已经支持。

- MicroPython 虽然只实现了 Python3 的标准库和容器库的一些部分，常见容器库有同类功能，但不同名的模块，但大多算法类的 Python 逻辑代码是可以拿来即用的。

- MicroPython 兼容实现的 Python3 的异常机制、没有实现元类（metaclass）机制，独立的 GC 机制。

- 在许当不同的硬件微芯片（最低在 nRF51）的移植上， MicroPython 代码接口缺乏一致性，呈现碎片化。

- MicroPython 编译（mpy-corss）后得到的是 mpy ，而不是 Python3 的 pyc 文件。

- MicroPython 在移植 Python3 代码时，经常缺少各种方法，所以要习惯寻找同类接口，而它们的使用方法除了看文档外就只能看源码。

### 总结

- MaixPy 相比 MaixPy3 功能要更简单（简陋）。
- MaixPy 和 MaixPy3 的开发工具不同。
- MaixPy 标准库（MicroPython）相比 MaixPy3 有一定的不足。
- MaixPy 的外设驱动模块具体函数存在差异。
- 不同的芯片执行效率有差异，MaixPy 和 MaixPy3 的有着不同的内存与性能消耗。

> 如有更多欢迎补充。
