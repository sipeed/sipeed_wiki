---
title: uzlib  — zlib 解压缩
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: uzlib  — zlib 解压缩
---


该模块实现了相应CPython模块的子集，如下所述。有关更多信息，请参阅原始CPython文档：[zlib](https://docs.python.org/3.5/library/zlib.html#module-zlib)。

该模块允许解压使用 [DEFLATE](https://en.wikipedia.org/wiki/DEFLATE) 算法压缩的二进制数据（通常用于zlib库和gzip存档器）。

压缩尚未实现。

## 函数

### decompress

解压

```python
uzlib.decompress(data, wbits=0, bufsize=0)
```

#### 参数

* `wbits`： 压缩期间使用的 DEFLATE 字典窗口大小（8-15，字典大小是该值的2的幂）。 另外，如果值为正，则假定数据为 zlib 流（使用 zlib 头）。 否则，如果它是负数，则假定它是原始 DEFLATE 流。 

* `bufsize`： 参数用于与CPython兼容， 可忽略。

#### 返回值

将解压缩的数据作为`bytes`类型返回。 

### DecompIO

创建一个流包装器，允许对另一个流中的压缩数据进行透明解压缩。 这允许处理具有大于可用堆大小的数据的压缩流。 除了decompress（）中描述的值之外，`wbits`可以取值 24..31（16+8..15），这意味着输入流具有gzip头。

```python
class uzlib.DecompIO(stream, wbits=0)
```

## 与 CPython 的不同

这个类是MicroPython扩展。它包含在临时基础上，可能会在以后的版本中进行大量更改或删除。


