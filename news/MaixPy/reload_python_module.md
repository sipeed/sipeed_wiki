---
title: 关于 MicroPython import 指定 flash 或 sd 分区的代码与重载 Python 模块的方法
keywords: MicroPython
date: 2022-06-09
tags: MicroPython, reload
---

如果在 maixpy (micropython) 上同时存在 flash 和 sd 等多个分区挂载 / 目录下，且均存在 boot.py 文件，如何加载指定分区下的 boot.py 模块代码呢？

<!-- more -->

[原文链接](https://www.cnblogs.com/juwan/p/14517375.html) https://www.cnblogs.com/juwan/p/14517375.html

`import boot` 时取决于 os 的 vfs (虚拟文件系统) 对象，它会根据 os.getcwd() 和 os.chdir('/sd') 决定代码寻找的位置（/sd 分区路径），如果是某目录下的代码，则可以使用类似 import test.boot 的结构来查找并 import 它。

示例：

```python
>>> os.chdir('/flash')
>>> import boot
flash: 2942
>>> os.getcwd()
'/flash'
>>> 
```

拓展来讲，如何重载 import boot 后的 boot 模块，管理 sys.modules 模块就行，如下示意。

```python
>>> import sys
>>> import boot
2433
>>> import boot
>>> sys.modules.pop('boot')
<module 'boot' from 'boot.py'>
>>> sys.modules.pop('boot')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: boot
>>> os.chdir('/flash')
>>> import boot
flash: 2479
>>> sys.modules.pop('boot')
<module 'boot' from 'boot.py'>
>>> os.chdir('/sd')
>>> import boot
2488
>>> sys.modules.pop('boot')
<module 'boot' from 'boot.py'>
>>>
```

即先使用 sys.modules.pop('boot') 后再重新 import 目标 boot 就行