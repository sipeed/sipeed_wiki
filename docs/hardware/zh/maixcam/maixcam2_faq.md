---
title: MaixCAM2 FAQ (常见问题)
---


下面找不到的问题，也可以参考[MaixPy FAQ](https://wiki.sipeed.com/maixpy/doc/zh/faq.html)。


## 产品是带外壳形态，我不需要外壳，屏幕或者摄像头，能去掉量产吗

可以。
自带外壳、屏幕和摄像头是方便快速验证产品和想法，实际量产可以联系 Sipeed(support@sipeed.com 或者网店) 定制去掉部分器件，量大更优。
另外也提供核心板版本，有 PCB 设计能力可以自行直接购买核心板设计底板。


## 购买的 4GB 内存版本的，怎么系统内显示只有 2GB / 1GB 内存

硬件是 `4GB` 内存，内存被分为了用户层内存和系统使用内存，在 `Linux`系统下用`free`命令看到的内存就是用户层内存，
系统使用的内存有一大部分被用来作为硬件专用内存了，比如`模型运行`、`摄像头`、`显示`等等。
我们可以修改`/boot/configs`文件里面的`maix_memory_cmm=-1` 值来修改分配比例，`-1`是默认值，
比如我们可以修改为`3072`（不写单位，默认单位是`MiB`），那么将预留`3072MiB`给模型等硬件使用，剩下的给`Linux`系统。
**需要重启才能生效。**
更详细的请看[MaixPy 内存使用说明](https://wiki.sipeed.com/maixpy/doc/zh/pro/memory.html)。



