---
title: Use of onewire (single bus)
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy doc: Use of onewire (single bus)
---

## Instructions

* Import onewire module from modules

```python
from modules import onewire
```

* Create onewire object

```python
fm.register(14, fm.fpioa.GPIOHS2, force=True)
bus = onewire(fm.fpioa.GPIOHS2)
```

* Search, read and write data and other operations

## Routine

ds18b20 temperature reading: [onwire_ds18b20](https://github.com/sipeed/MaixPy_scripts/blob/80f4eb71d3481b6f119f25f39f7c9b37404b99ce/hardware/demo_onewire_ds18x20.py)
