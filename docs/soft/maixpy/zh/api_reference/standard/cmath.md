---
title: cmath – 复数的数学函数
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: cmath – 复数的数学函数
---


该模块实现了相应CPython模块的子集，如下所述。有关更多信息，请参阅原始CPython文档: [cmath](https://docs.python.org/3.5/library/cmath.html#module-cmath).

`cmath` 模块提供了一些处理复数的基本数学函数。


## 函数

### cos

```python
cmath.cos(z)
```

返回`z`的余弦。

### exp

```python
cmath.exp(z)
```

返回`z`的指数。

### log

```python
cmath.log(z)
```

返回`z`的自然对数。分支切割沿负实轴。

### log10

```python
cmath.log10(z)
```

返回`z`的以10为底的对数。分支切割沿负实轴。

### phase

```python
cmath.phase(z)
```

返回数字“z”的相位，范围（-pi，+ pi）。

### polar

```python
cmath.polar(z)
```

作为元组返回`z`的极性形式。

### rect

```python
cmath.rect(r, phi)
```

返回模数`r`和相位`phi`的复数。

### sin

```python
cmath.sin(z)
```

返回`z`的正弦值。

### sqrt

```python
cmath.sqrt(z)
```

返回`z`的平方根。

## Constants

### cmath.e

自然对数的基础

### cmath.pi

圆周长与直径的比值


