---
title: Micropython Editor
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy doc: Micropython Editor
---


MaixPy firmware integrates a file editor-[`pye`](https://github.com/robert-hh/Micropython-Editor), users can directly modify the files in the board through the serial terminal

Instructions:

```python

from pye_mp import pye

pye("/sd/boot.py")

```
