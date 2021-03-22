---
title: uerrno — system error code
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: uerrno — system error code
---




This module implements a subset of the corresponding CPython module, as described below. For more information, please refer to the original CPython documentation: [errno](https://docs.python.org/3.5/library/errno.html#module-errno).

This module describes the error identifier of the `OSError` error. The specific code inventory depends on `Micropython porting`, and the error will be explained in the specific error function.


## Constant

### EEXIST, EAGAIN, etc.

Error codes based on ANSI C / POSIX standards. All error codes begin with "E". As mentioned above, the code inventory depends on the port of MicroPython. Errors can usually be accessed as `exc.args[0]`, where `exc` is an instance of `OSError`. Example usage:

```python
try:
    uos.mkdir("my_dir")
except OSError as exc:
    if exc.args[0] == uerrno.EEXIST:
        print("Directory already exists")
```

### uerrno.errorcode

The dictionary maps numeric error codes to strings with signed error codes (see above):

```python
>>> print(uerrno.errorcode[uerrno.EEXIST])
EEXIST
```
