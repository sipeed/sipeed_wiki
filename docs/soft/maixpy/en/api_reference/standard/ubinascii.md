---
title: ubinascii-Binary/ASCII conversion
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: ubinascii-Binary/ASCII conversion
---



This module implements a subset of the corresponding CPython module, as described below. For more information, please refer to the original CPython documentation: [binascii](https://docs.python.org/3.5/library/binascii.html#module-binascii).

The module implements the conversion between binary data and its various codes in ASCII format (two directions).

## Function

### ubinascii.hexlify(data[, sep])

Convert binary data to hexadecimal representation. Returns a byte string.

#### Difference with CPython

If the additional parameter sep is provided, it will be used as a separator between hexadecimal values.

### ubinascii.unhexlify(data)

Convert hexadecimal data to binary representation. Returns a byte string. (Ie the inverse of hexlify)

### ubinascii.a2b_base64(data)

Decode base64-encoded data, ignoring invalid characters in the input. Comply with [RFC 2045 s.6.8.](https://tools.ietf.org/html/rfc2045#section-6.8) Return a bytes object.

### ubinascii.b2a_base64(data)

Encode binary data in base64 format, as described in [RFC 3548](https://tools.ietf.org/html/rfc3548.html). Returns the encoded data, followed by a newline character, as a bytes object.
