---
title: ujson – JSON encoding and decoding
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: ujson – JSON encoding and decoding
---



This module implements a subset of the corresponding CPython module, as described below. For more information, please refer to the original CPython documentation: [json](https://docs.python.org/3.5/library/json.html#module-json).

This module allows conversion between Python objects and JSON data formats.

## Function

### dump

```python
ujson.dump(obj, stream)
```

Serialize `obj` into a JSON string and write it to the given stream.

### dumps

```python
ujson.dumps(obj)
```

Returns `obj` represented as a JSON string.

### load

```python
ujson.load(stream)
```

Parse the given stream, interpret it as a JSON string and deserialize the data into Python objects. Return the result object.

The parsing continues until the end of the file is encountered. If the data in the stream is not formed correctly, a ValueError will be raised.

### loads

```python
ujson.loads(str)
```

Parse the JSON str and return an object. If the string format is wrong, ValueError is raised.
