---
title: onewire（单总线）的使用
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: onewire（单总线）的使用
---


# 使用方法

* 从 modules 导入 onewire 模块

```python
from modules import onewire
```

* 创建 onewire 对象

```python
fm.register(14, fm.fpioa.GPIOHS2, force=True)
bus = onewire(fm.fpioa.GPIOHS2)
```

* 搜索，读写数据等操作

## 例程：

ds18b20 温度读取：[onwire_ds18b20](https://github.com/sipeed/MaixPy_scripts/blob/80f4eb71d3481b6f119f25f39f7c9b37404b99ce/hardware/demo_onewire_ds18x20.py)