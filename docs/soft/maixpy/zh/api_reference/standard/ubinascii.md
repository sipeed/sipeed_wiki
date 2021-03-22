---
title: ubinascii – 二进制/ ASCII转换
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: ubinascii – 二进制/ ASCII转换
---



该模块实现了相应CPython模块的子集，如下所述。有关更多信息，请参阅原始CPython文档：[binascii](https://docs.python.org/3.5/library/binascii.html#module-binascii).

该模块以ASCII格式（两个方向）实现二进制数据与其各种编码之间的转换。

## 函数

### ubinascii.hexlify(data[, sep])

将二进制数据转换为十六进制表示。返回字节字符串。

#### 与CPython的区别

如果提供了附加参数sep，则它将用作十六进制值之间的分隔符。

### ubinascii.unhexlify(data)

将十六进制数据转换为二进制表示。返回字节字符串。 （即hexlify的倒数）

### ubinascii.a2b_base64(data)

解码base64编码的数据，忽略输入中的无效字符。符合 [RFC 2045 s.6.8.](https://tools.ietf.org/html/rfc2045#section-6.8) 返回一个bytes对象。

### ubinascii.b2a_base64(data)

以base64格式编码二进制数据，如 [RFC 3548](https://tools.ietf.org/html/rfc3548.html)所述。返回编码数据，后跟换行符，作为bytes对象。

