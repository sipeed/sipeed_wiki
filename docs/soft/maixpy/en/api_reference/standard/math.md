---
title: math-mathematical functions
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: math-mathematical functions
---



This module implements a subset of the corresponding CPython module, as described below. For more information, please refer to the original CPython documentation: [math](https://docs.python.org/3.5/library/math.html#module-math).

The `math` module provides some basic mathematical functions for handling floating point numbers.


## Function

### math.acos(x)

Returns the arc cosine of `x`.

### math.acosh(x)

Returns the inverse hyperbolic cosine of `x`.

### math.asin(x)

Returns the arc sine of `x`.

### math.asinh(x)

Returns the inverse hyperbolic sine of `x`.

### math.atan(x)

Returns the arc tangent of `x`.

### math.atan2(y, x)

Returns the principal value of the arctangent of `y` /`x`.

### math.atanh(x)

Returns the inverse hyperbolic tangent of `x`.

### math.ceil(x)

Returns an integer, "x" is rounded to positive infinity.

### math.copysign(x, y)

Return `x` with the sign of `y`.

### math.cos(x)

Returns the cosine of `x`.


### math.cosh(x)

Returns the hyperbolic cosine of `x`

### math.degrees(x)

Returns the radians `x` converted to degrees.

### math.erf(x)

Error function that returns `x`.

### math.erfc(x)

Returns the complementary error function of `x`.

### math.exp(x)

Returns the exponent of `x`.

### math.expm1(x)

Return `exp(x)-1`.

### math.fabs(x)

Returns the absolute value of `x`.

### math.floor(x)

Returns an integer, "x" is rounded towards negative infinity.

### math.fmod(x, y)

Returns the remainder of `x` /`y`.

### math.frexp(x)

Decompose floating point numbers into mantissa and exponent. The returned value is the tuple `(m, e)`, so that `x == m * 2 ** e` is completely correct. If `x == 0`, the function returns `(0.0,0)`, otherwise the relationship `0.5 <= abs(m)<1` holds.

### math.gamma(x)

Returns the gamma function of `x`.

### math.isfinite(x)

If `x` is finite, it returns True.

### math.isinf(x)

If `x` is infinite, it returns True.

### math.isnan(x)

If `x` is not a number, it returns True

### math.ldexp(x, exp)

Return `x *(2 ** exp)`.

### math.lgamma(x)

Returns the natural logarithm of the gamma function of `x`.

### math.log(x)

Returns the natural logarithm of `x`.

### math.log10(x)

Returns the base 10 logarithm of `x`.

### math.log2(x)

Returns the base-2 logarithm of `x`.

### math.modf(x)

Returns a tuple of two floating-point numbers, the fraction and integer part of "x". Both return values ​​have the same sign as `x`.

### math.pow(x, y)

Return `x` to the power of'y`.

### math.radians(x)

Returns the degree `x` converted to radians.

### math.sin(x)

Returns the sine of `x`.

### math.sinh(x)

Returns the hyperbolic sine of `x`.

### math.sqrt(x)

Returns the square root of `x`.

### math.tan(x)

Returns the tangent of `x`.

### math.tanh(x)

Returns the hyperbolic tangent of `x`.

### math.trunc(x)

Returns an integer, "x" is rounded towards 0.

## Constants

### math.e

The basis of natural logarithm

### math.pi

Ratio of circumference to diameter
