---
title: uzlib — zlib decompression
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: uzlib — zlib decompression
---


This module implements a subset of the corresponding CPython module, as described below. For more information, please refer to the original CPython documentation: [zlib](https://docs.python.org/3.5/library/zlib.html#module-zlib).

This module allows to decompress binary data compressed using the [DEFLATE](https://en.wikipedia.org/wiki/DEFLATE) algorithm (usually used in the zlib library and gzip archiver).

Compression has not yet been implemented.

## Function

### decompress

Unzip

```python
uzlib.decompress(data, wbits=0, bufsize=0)
```

#### Parameters

* `wbits`: DEFLATE dictionary window size used during compression (8-15, dictionary size is a power of 2 of this value). In addition, if the value is positive, the data is assumed to be a zlib stream (using the zlib header). Otherwise, if it is negative, it is assumed to be the original DEFLATE stream.

* `bufsize`: The parameter is used for compatibility with CPython and can be ignored.

#### return value

Return the decompressed data as `bytes` type.

### DecompIO

Create a stream wrapper that allows transparent decompression of compressed data in another stream. This allows processing of compressed streams with data larger than the available heap size. In addition to the values ​​described in decompress(), `wbits` can take the value 24..31 (16+8..15), which means that the input stream has a gzip header.

```python
class uzlib.DecompIO(stream, wbits=0)
```

## Difference from CPython

This class is a MicroPython extension. It is included on a temporary basis and may be changed or deleted extensively in future versions.
