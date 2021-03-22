---
title: Micropython Editor
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: Micropython Editor
---


MaixPy 固件中集成了文件编辑器 —— [`pye`](https://github.com/robert-hh/Micropython-Editor), 用户可以直接通过串口终端修改板子里面的文件

使用方法：

```python

from pye_mp import pye

pye("/sd/boot.py")

```
