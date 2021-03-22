---
title: uhashlib –哈希算法
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: uhashlib –哈希算法
---



该模块实现了相应[CPython](http://docs.micropython.org/en/latest/reference/glossary.html#term-cpython)模块的子集，如下所述。有关更多信息，请参阅原始CPython文档：[hashlib](https://docs.python.org/3.5/library/hashlib.html#module-hashlib)。

该模块实现二进制数据哈希算法。可用算法的确切清单取决于电路板。在可以实现的算法中：

SHA256-SHA2系列的最新现代哈希算法。它适用于密码安全的目的。除非它具有特定的代码大小限制，否则建议将其包含在MicroPython内核中，并建议任何开发板都提供此功能。

在 K210 中有硬件加速，不是软件计算

[例程](https://github.com/sipeed/MaixPy_scripts/blob/master/basic/demo_sha256.py)：
```python
a = bytes([0]*65)
b = hashlib.sha256(a)
c = b.digest()
print(c)
```

## 构造函数

## 类 uhashlib.sha256([data])

创建一个SHA256哈希对象，并有选择地向其中馈送数据。


## 方法

### hash.update(data)

将更多的二进制数据输入哈希。

### hash.digest()

返回通过哈希传递的所有数据的哈希，作为字节对象。调用此方法后，无法再将更多数据馈入哈希。

**注意**： 在`micropython`中， 使用此函数会完成最后的计算， 不是单纯的将结果显示出来， 所以只能调用一次， 如果你要多次使用这个值， 请保存到变量
```python
c = b.digest()
print(c)
```
多次调用会发现返回值不相同
```python
c = b.digest()
d = b.digest()
print(c == d) # False
```

### hash.hexdigest()

未实现此方法。使用 `ubinascii.hexlify(hash.digest())` 可获得类似的效果。


