---
title: uerrno — 系统错误代码
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: uerrno — 系统错误代码
---




该模块实现了相应CPython模块的子集，如下所述。有关更多信息，请参阅原始CPython文档：[errno](https://docs.python.org/3.5/library/errno.html#module-errno)。

该模块描述了 `OSError` 错误的错误标识。特定的代码库存取决于 `Micropython 的移植`， 错误会在特定的会出现错误的函数进行说明。


## 常量

### EEXIST, EAGAIN, 等

基于 ANSI C / POSIX 标准的错误代码。所有错误代码均以 “E” 开头。如上所述，代码库存取决于 MicroPython 的移植。错误通常可以作为`exc.args [0]`访问，其中`exc`是`OSError`的一个实例。用法示例：

```python
try:
    uos.mkdir("my_dir")
except OSError as exc:
    if exc.args[0] == uerrno.EEXIST:
        print("Directory already exists")
```

### uerrno.errorcode

字典将数字错误代码映射到带有符号错误代码的字符串（参见上文）：

```python
>>> print(uerrno.errorcode[uerrno.EEXIST])
EEXIST
```


