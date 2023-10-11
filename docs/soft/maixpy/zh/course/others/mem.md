---
title: 内存管理
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy  内存管理
---

在 MaixPy 中， 目前使用了两种内存管理， 一种是 GC（垃圾回收）， 另一种是系统堆内存， 两者同时存在。

比如：芯片有 6MiB 内存，加入固件使用了前面的 2MiB， 还剩 4MiB， 默认 `GC`使用 512KiB， 剩下的给系统堆内存管理。

* 在`mpy`层面写的代码， 变量都是存在`GC`管理的内存块中，比如定义一个变量`a = [1,2,3,4]`, 如果`GC'`内存不足了， 会自动触发`gc.collect()`函数的执行， `GC`会自动把没有在使用了的变量给销毁，留出来空间给新的变量使用。
> `GC`使用`标记-清除`的方式进行内存回收，有兴趣可以看[这里](https://neucrack.com/p/46)
* 因为`GC`要扫描内存， 如果除了程序占用的内存，剩下的都给`GC`，那每次扫描需要耗费大量时间，所以分成了两种内存。 堆内存由 `C`层面的代码控制，主要用于图片内存， AI内存， LCD 内存， 以及模型加载到内存等

`GC` 内存的总大小是可以设置的， 所以，根据具体的使用情况可以适当修改`GC`内存大小， 比如：
* 为了加载更大的模型，可以把 `GC`内存设置小一点
* 如果分配新的变量提示内存不足， 可以适当将`GC`内存设置大一点即可
* 如果都不够了， 就要考虑缩减固件大小，或者优化代码了

设置`GC`内存大小示例：

```python
from Maix import utils
import machine

print(utils.gc_heap_size())

utils.gc_heap_size(1024*1024) # 1MiB
machine.reset()
```

注意修改后需要重启生效

查看内存分配情况：

```python
import gc

print(gc.mem_free() / 1024) # stack mem

import Maix

print(Maix.utils.heap_free() / 1024) # heap mem

'''
>>> 
raw REPL; CTRL-B to exit
>OK
352.0937
4640.0
>
MicroPython v0.5.1-136-g039f72b6c-dirty on 2020-11-18; Sipeed_M1 with kendryte-k210
Type "help()" for more information.
>>> 
'''
```
