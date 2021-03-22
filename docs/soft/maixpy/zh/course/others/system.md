---
title: 系统控制
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 系统控制
---


## 复位（reset）

```python
import machine

machine.reset()
```


## 主频（cpu）

可以设置 CPU 和 KPU 的主频， 具体参考[Maix.freq](./../../api_reference/Maix/freq.md)模块

```python
from Maix import freq
freq.set(cpu = 400, kpu = 400)
```
