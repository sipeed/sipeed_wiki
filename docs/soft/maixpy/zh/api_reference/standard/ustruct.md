---
title: ustruct – 打包和解包原始数据类型
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: ustruct – 打包和解包原始数据类型
---



该模块实现了相应的`CPython`模块的子集，如下所述。有关更多信息，请参阅原始CPython文档： [struct](https://docs.python.org/3.5/library/struct.html#module-struct).

支持的大小/字节顺序前缀: `@`, `<`, `>`, `!`.

支持的格式代码： `b`, `B`, `h`, `H`, `i`, `I`, `l`, `L`, `q`, `Q`, `s`, `P`, `f`, `d` （后者2取决于浮点支持）。

## 函数

### calcsize

```python
ustruct.calcsize(fmt)
```

返回存储给定`fmt`所需的字节数。

### pack

```python
ustruct.pack(fmt, v1, v2, ...)
```

根据格式字符串`fmt`打包值`v1`，`v2`，`...`。返回值是编码值的字节对象。

### pack_into

```python
ustruct.pack_into(fmt, buffer, offset, v1, v2, ...)
```

根据格式字符串`fmt`将值`v1`，`v2`，`...`打包到从offset开始的缓冲区中。从缓冲区的末尾开始计数可能是负数。

### unpack

```python
ustruct.unpack(fmt, data)
```

根据格式字符串`fmt`从`data`解包。返回值是解压缩值的元组。

### unpack_from

```python
ustruct.unpack_from(fmt, data, offset=0)
```

根据格式字符串`fmt`从 `offset` 开始从`data`解包。 `offset`可能是负数，从缓冲区的末尾开始计数。返回值是解压缩值的元组。




