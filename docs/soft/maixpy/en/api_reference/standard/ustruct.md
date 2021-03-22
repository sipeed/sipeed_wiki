---
title: ustruct-Packing and unpacking primitive data types
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: ustruct-packing and unpacking primitive data types
---



This module implements a subset of the corresponding `CPython` module, as described below. For more information, please refer to the original CPython documentation: [struct](https://docs.python.org/3.5/library/struct.html#module-struct).

Supported size/byte order prefixes: `@`, `<`, `>`, `!`.

Supported format codes: `b`, `B`, `h`, `H`, `i`, `I`, `l`, `L`, `q`, `Q`, `s`, ` P`, `f`, `d` (the latter 2 depends on floating point support).

## Function

### calcsize

```python
ustruct.calcsize(fmt)
```

Returns the number of bytes required to store the given `fmt`.

### pack

```python
ustruct.pack(fmt, v1, v2, ...)
```

Pack the values ​​`v1`, `v2`, `...` according to the format string `fmt`. The return value is a bytes object of the encoded value.

### pack_into

```python
ustruct.pack_into(fmt, buffer, offset, v1, v2, ...)
```

According to the format string `fmt`, the values ​​`v1`, `v2`, `...` are packed into a buffer starting from offset. Counting from the end of the buffer may be negative.

### unpack

```python
ustruct.unpack(fmt, data)
```

Unpack from `data` according to the format string `fmt`. The return value is a tuple of decompressed values.

### unpack_from

```python
ustruct.unpack_from(fmt, data, offset=0)
```

According to the format string `fmt` starts from `offset` and unpacks from `data`. `offset` may be a negative number, counting from the end of the buffer. The return value is a tuple of decompressed values.
