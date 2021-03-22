---
title: 内置类（builtin_py）
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 内置类（builtin_py）
---


`内置类` 库（builtin_py）是对 MaixPy 底层的类进行封装的用户层接口，方便用户使用 MaixPy 它包括以下：

* [fpioa_manager](fm.md)
* [board_info](board_info.md)
* [pye](pye.md)

> `board_info` 与板卡相关，不同板卡配置不同，使用前需要[手动配置](../builtin_py/board_info.md)。

```python
from board import board_info
from fpioa_manager import fm
```
