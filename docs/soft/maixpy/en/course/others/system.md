---
title: System Control
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy doc: system control
---


## Reset (reset)

```python
import machine

machine.reset()
```


## Main frequency (cpu)

You can set the main frequency of CPU and KPU, please refer to [Maix.freq](/api_reference/Maix/freq.md) module

```python
from Maix import freq
freq.set(cpu = 400, kpu = 400)
```
