---
title: gc – 内存回收
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: gc – 内存回收
---



该模块实现了相应CPython模块的子集，如下所述。有关更多信息，请参阅原始CPython文档：[gc](https://docs.python.org/3.5/library/gc.html#module-gc).

## 函数

### gc.enable()

启用自动垃圾回收。

### gc.disable()

禁用自动垃圾回收。仍然可以分配堆内存，仍然可以使用 `gc.collect()` 手动启动垃圾收集。

### gc.collect()

运行垃圾回收。

### gc.mem_alloc()

返回分配的堆 RAM 的字节数。

#### Difference to CPython

此功能是 MicroPython 扩展。

### gc.mem_free()

返回可用堆RAM的字节数，如果堆剩余数量未知，则返回-1。

#### 与CPython的区别

此功能是MicroPython扩展。

### gc.threshold([amount])

设置或查询其他GC分配阈值。通常，仅当不能满足新分配时，即在内存不足（OOM）条件下才触发集合。如果调用此函数，除了OOM之外，每次分配了大量字节后都会触发一个集合（总共，因为上一次分配了这么多的字节）。 amount通常被指定为小于完整堆大小，意图在堆耗尽之前触发集合，并希望早期集合可以防止过多的内存碎片。这是一种启发式度量，其效果因应用程序而异，以及量参数的最佳值。

不带参数调用函数将返回阈值的当前值。值-1表示禁用的分配阈值。

#### 与CPython的区别

此函数是MicroPython扩展。 CPython有一个类似的函数 - `set_threshold()`，但是由于不同的GC实现，它的签名和语义是不同的。

