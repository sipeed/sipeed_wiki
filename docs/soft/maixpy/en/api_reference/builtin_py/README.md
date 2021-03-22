---
title: built-in class (builtin_py)
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy doc: built-in class (builtin_py)
---


The `builtin_py` library (builtin_py) is a user-level interface that encapsulates the underlying classes of MaixPy, which is convenient for users to use MaixPy. It includes the following:

* [fpioa_manager](fm.md)
* [board_info](board_info.md)
* [pye](pye.md)

> `board_info` is related to the board, and different board configurations are different. [Manual configuration](board_info.md) is required before use.

```python
from board import board_info
from fpioa_manager import fm
```
