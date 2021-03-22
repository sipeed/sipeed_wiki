---
title: Use of I2S (Integrated Circuit Audio Bus)
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: the use of I2S (integrated circuit built-in audio bus)
---


For a detailed introduction to the I2S audio bus, please refer to [I2S-API Document](./../../api_reference/Maix/i2s.md).

## Instructions

* Import I2S module from Maix

```python
from Maix import I2S
```

* Create I2S object

```python
i2s_dev = I2S(device_num)
```

* Configuration parameters

```python
i2s_dev.channel_config(rx.CHANNEL_0, rx.RECEIVER, align_mode = I2S.STANDARD_MODE)
i2s_dev.set_sample_rate(sample_rate)
```

* Read or play data

```python
i2s_dev.record(256)#sampling points number must be smaller than 256
```

## Routine

Collect data and play it directly

```python
from Maix import I2S
import time
from fpioa_manager import *

fm.register(20,fm.fpioa.I2S0_IN_D0)#GO
fm.register(19,fm.fpioa.I2S0_WS)
fm.register(18,fm.fpioa.I2S0_SCLK)
fm.register(34,fm.fpioa.I2S2_OUT_D1)
fm.register(35,fm.fpioa.I2S2_SCLK)
fm.register(33,fm.fpioa.I2S2_WS)
sample_rate = 44*1000
rx = I2S(I2S.DEVICE_0)
rx.channel_config(rx.CHANNEL_0, rx.RECEIVER, align_mode = I2S.STANDARD_MODE)
rx.set_sample_rate(sample_rate)
tx = I2S(I2S.DEVICE_2)
tx.channel_config(tx.CHANNEL_1, tx.TRANSMITTER, align_mode = I2S.RIGHT_JUSTIFYING_MODE)
tx.set_sample_rate(sample_rate)
while True:
    audio = rx.record(256)#sampling points number must be smaller than 256
    tx.play(audio)
```
