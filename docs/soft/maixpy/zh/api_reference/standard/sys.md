---
title: sys – 系统特定功能
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: sys – 系统特定功能
---



该模块实现了相应CPython模块的子集，如下所述。 有关更多信息，请参阅原始CPython文档：[sys](https://docs.python.org/3.5/library/sys.html#module-sys).

## 功能函数

### sys.exit(retval=0)

使用给定的退出代码终止当前程序。 根据此，此函数引发“SystemExit”异常。 如果给出了一个参数，它的值作为`SystemExit`的参数给出。

### sys.print_exception(exc, file=sys.stdout)

使用回溯到类文件对象文件（或默认情况下为`sys.stdout`）打印异常。

> **和 CPython 的不同**
> 这是一个函数的简化版本，它出现在CPython的回溯模块中。 与traceback.print_exception（）不同，此函数只接受异常值而不是异常类型，异常值和回溯对象; file参数应该是位置的; 不支持其他参数。 可以在micropython-lib中找到与CPython兼容的回溯模块。

## 常量

### sys.argv

当前程序启动时的可变参数列表。

### sys.byteorder

系统的字节顺序（“小端”或“大端”`）。

### sys.implementation

包含有关当前Python实现的信息的对象。 对于MicroPython，它具有以下属性：

* name - 字符串“micropython”
* version - 元组 (major, minor, micro), e.g. (1, 7, 0)

此对象是区分MicroPython与其他Python实现的推荐方法（请注意，它仍然可能不存在于非常小的端口中）。

> **和 CPython 的不同**
> CPython要求为此对象提供更多属性，但实际有用的最低要求是在MicroPython中实现的。

### sys.maxsize

本机整数类型可以在当前平台上保存的最大值，或MicroPython整数类型可表示的最大值，如果它小于平台最大值（对于没有长int支持的MicroPython端口的情况）。

此属性对于检测平台的“位数”（32位与64位等）非常有用。 建议不要直接将此属性与某个值进行比较，而是计算其中的位数：

```python
bits = 0
v = sys.maxsize
while v:
    bits += 1
    v >>= 1
if bits > 32:
    # 64-bit (or more) platform
    ...
else:
    # 32-bit (or less) platform
    # Note that on 32-bit platform, value of bits may be less than 32
    # (e.g. 31) due to peculiarities described above, so use "> 16",
    # "> 32", "> 64" style of comparisons.
```

### sys.modules

加载模块的字典。 在某些端口上，它可能不包含内置模块。

### sys.path

用于搜索导入模块的可变目录列表。

### sys.platform

运行 MicroPython 的平台。 对于OS / RTOS端口，这通常是OS的标识符，例如，` “LINUX”`。 对于裸金属端口，它是电路板的标识符，例如 `“pyboard”`用于原始的 MicroPython 参考板。 因此，它可用于区分一块板与另一块板。 如果您需要检查您的程序是否在 MicroPython 上运行（与其他 Python 实现相比），请使用`sys.implementation`。

### sys.stderr

标准错误 `stream`.

### sys.stdin

标准输入 `stream`.

### sys.stdout

标准输出 `stream`.

### sys.version

实现的 Python 版本， 返回一个字符串

### sys.version_info

实现的 Python 版本， 返回一个由整数组成的元组



