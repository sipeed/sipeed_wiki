---
title: I2S（集成电路内置音频总线）的使用
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: I2S（集成电路内置音频总线）的使用
---


关于 I2S 音频总线详细介绍请参考[I2S-API 文档](./../../api_reference/Maix/i2s.md).

## 使用方法

* 从 Maix 导入 I2S 模块

```python
from Maix import I2S
```

* 创建 I2S 对象

```python
i2s_dev = I2S(device_num)
```

* 配置参数

```python
i2s_dev.channel_config(rx.CHANNEL_0, rx.RECEIVER, align_mode = I2S.STANDARD_MODE)
i2s_dev.set_sample_rate(sample_rate)
```

* 读取或播放数据

```python
i2s_dev.record(256)#sampling points number must be smaller than 256
```

## 例程

采集数据并直接播放

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
