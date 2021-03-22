---
title: cmath – mathematical functions for complex numbers
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: cmath – mathematical functions for complex numbers
---


This module implements a subset of the corresponding CPython module, as described below. For more information, please refer to the original CPython documentation: [cmath](https://docs.python.org/3.5/library/cmath.html#module-cmath).

The `cmath` module provides some basic mathematical functions for dealing with complex numbers.


## Function

### cos

```python
cmath.cos(z)
```

Returns the cosine of `z`.

### exp

```python
cmath.exp(z)
```

Returns the exponent of `z`.

### log

```python
cmath.log(z)
```

Returns the natural logarithm of `z`. The branch cuts along the negative real axis.

### log10

```python
cmath.log10(z)
```

Returns the base 10 logarithm of `z`. The branch cuts along the negative real axis.

### phase

```python
cmath.phase(z)
```

Returns the phase, range (-pi, +pi) of the number "z".

### polar

```python
cmath.polar(z)
```

Return the polar form of `z` as a tuple.

### rect

```python
cmath.rect(r, phi)
```

Returns the complex number of the modulus `r` and the phase `phi`.

### sin

```python
cmath.sin(z)
```

Returns the sine of `z`.

### sqrt

```python
cmath.sqrt(z)
```

Returns the square root of `z`.

## Constants

### cmath.e

The basis of natural logarithm

### cmath.pi

Ratio of circumference to diameter
