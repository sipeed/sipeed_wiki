---
title: sys-system specific functions
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: sys-system specific functions
---



This module implements a subset of the corresponding CPython module, as described below. For more information, please refer to the original CPython documentation: [sys](https://docs.python.org/3.5/library/sys.html#module-sys).

## Function

### sys.exit(retval=0)

Terminate the current program with the given exit code. According to this, this function raises the "SystemExit" exception. If a parameter is given, its value is given as the parameter of `SystemExit`.

### sys.print_exception(exc, file=sys.stdout)

Use traceback to file-like object files (or `sys.stdout` by default) to print exceptions.

> **Difference from CPython**
> This is a simplified version of a function that appears in the backtracking module of CPython. Unlike traceback.print_exception(), this function only accepts outliers instead of exception types, outliers and traceback objects; the file parameter should be positional; other parameters are not supported. A traceback module compatible with CPython can be found in micropython-lib.

## Constant

### sys.argv

The variable parameter list when the current program is started.

### sys.byteorder

The byte order of the system ("little endian" or "big endian"`).

### sys.implementation

An object containing information about the current Python implementation. For MicroPython, it has the following attributes:

* name-the string "micropython"
* version-tuple (major, minor, micro), e.g. (1, 7, 0)

This object is the recommended way to distinguish MicroPython from other Python implementations (note that it may still not exist in very small ports).

> **Difference from CPython**
> CPython requires more attributes for this object, but the minimum requirement to actually be useful is implemented in MicroPython.

### sys.maxsize

The maximum value that the native integer type can save on the current platform, or the maximum value that the MicroPython integer type can represent, if it is less than the platform maximum value (for the MicroPython port without long int support).

This attribute is very useful for detecting the "bitness" of the platform (32-bit and 64-bit, etc.). It is recommended not to directly compare this attribute with a value, but to calculate the number of digits:

```python
bits = 0
v = sys.maxsize
while v:
    bits += 1
    v >>= 1
if bits> 32:
    # 64-bit (or more) platform
    ...
else:
    # 32-bit (or less) platform
    # Note that on 32-bit platform, value of bits may be less than 32
    # (e.g. 31) due to peculiarities described above, so use "> 16",
    # "> 32", "> 64" style of comparisons.
```

### sys.modules

Load the dictionary of the module. On some ports, it may not contain built-in modules.

### sys.path

A variable directory list for searching imported modules.

### sys.platform

The platform on which MicroPython is running. For OS/RTOS ports, this is usually the identifier of the OS, for example, `"LINUX"`. For bare metal ports, it is the identifier of the circuit board, such as `"pyboard"` for the original MicroPython reference board. Therefore, it can be used to distinguish one board from another. If you need to check whether your program is running on MicroPython (compared to other Python implementations), please use `sys.implementation`.

### sys.stderr

Standard error `stream`.

### sys.stdin

Standard input `stream`.

### sys.stdout

Standard output `stream`.

### sys.version

The implemented Python version, returns a string

### sys.version_info

The implemented Python version, which returns a tuple of integers
