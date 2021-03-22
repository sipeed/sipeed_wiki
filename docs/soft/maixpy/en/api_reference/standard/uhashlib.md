---
title: uhashlib-hash algorithm
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: uhashlib-hash algorithm
---



This module implements a subset of the corresponding [CPython](http://docs.micropython.org/en/latest/reference/glossary.html#term-cpython) module, as described below. For more information, please refer to the original CPython documentation: [hashlib](https://docs.python.org/3.5/library/hashlib.html#module-hashlib).

This module implements a hash algorithm for binary data. The exact list of available algorithms depends on the board. Among the algorithms that can be implemented:

The latest modern hash algorithm of the SHA256-SHA2 series. It is suitable for password security purposes. Unless it has a specific code size limit, it is recommended to include it in the MicroPython kernel, and it is recommended that any development board provides this feature.

There is hardware acceleration in K210, not software calculation

[Example](https://github.com/sipeed/MaixPy_scripts/blob/master/basic/demo_sha256.py):
```python
a = bytes([0]*65)
b = hashlib.sha256(a)
c = b.digest()
print(c)
```

## Constructor

## Class uhashlib.sha256([data])

Create a SHA256 hash object and selectively feed data into it.


## Method

### hash.update(data)

Enter more binary data into the hash.

### hash.digest()

Returns the hash of all data passed through the hash as a bytes object. After calling this method, no more data can be fed into the hash.

**Note**: In `micropython`, using this function will complete the final calculation, instead of simply displaying the result, it can only be called once. If you want to use this value multiple times, please save it to a variable
```python
c = b.digest()
print(c)
```
Multiple calls will find that the return value is different
```python
c = b.digest()
d = b.digest()
print(c == d) # False
```

### hash.hexdigest()

This method is not implemented. Use `ubinascii.hexlify(hash.digest())` to get a similar effect.
