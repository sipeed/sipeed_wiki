---
title: ujson – JSON encoding and decoding
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: ujson – JSON encoding and decoding
---



该模块实现了相应 CPython 模块的子集，如下所述。有关更多信息，请参阅原始 CPython 文档：[json](https://docs.python.org/3.5/library/json.html#module-json).

此模块允许在 Python 对象和 JSON 数据格式之间进行转换。

## 函数

### dump

```python
ujson.dump(obj, stream)
```

将 `obj` 序列化化为 JSON 字符串，将其写入给定的流。

### dumps

```python
ujson.dumps(obj)
```

返回表示为 JSON 字符串的 `obj`。

### load

```python
ujson.load(stream)
```

解析给定的流，将其解释为 JSON 字符串并将数据反序列化为 Python 对象。返回结果对象。

解析继续，直到遇到文件结尾。如果未正确形成流中的数据，则会引发 ValueError。

### loads

```python
ujson.loads(str)
```

解析JSON str并返回一个对象。如果字符串格式出错，则引发ValueError。

