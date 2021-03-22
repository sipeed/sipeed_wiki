---
title: I2S
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: I2S
---

I2S模块主要用于驱动I2S设备，k210一共有3个I2S设备，每个设备一共有4个通道，在使用前需要对引脚进行映射管理

## 模块函数

### 构造函数

新建一个 I2S 对象

```
from Maix import I2S
i2s_dev = I2S(device_num)
```

#### 参数

`device_num` I2S号，使用指定的 I2S，可以通过 `I2S.` 按tab键来补全

#### 返回值

返回一个`I2S` 对象

### 通道配置函数

用于配置 I2S 通道，在此之前需要对引脚进行映射

```
i2s_dev.channel_config(channel, mode, resolution, cycles, align_mode)
```
#### 参数

* `channel`:    I2S通道编号

* `mode`:       通道传输模式，一共有接收和发送模式，录音为接受，播放为发送

* `resolution`: 通道分辨率，即接收数据位数

* `cycles`:     单个数据时钟数

* `align_mode`: 通道对齐模式

#### 返回值

无

### 设置采样率

用于配置 I2S 采样率

```
i2s_dev.set_sample_rate(sample_rate)
```
#### 参数

`sample_rate`: int 类型，采样率

#### 返回值

无

### 接收音频

使用I2S接收音频数据

```
audio = i2s_dev.record(points)
```
#### 参数

* `points`: 一次采集的音频点数

#### 返回值

`audio`: 一个`audio`音频对象

### 发送音频

使用I2S发送音频数据

```
i2s_dev.play(audio)
```
#### 参数

* `audio`: 发送的音频对象

#### 返回值
无

## 例程

### 例程1

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

### 例程2

采集数据转化为 Audio 并播放

```python
from Maix import I2S
from Maix import Audio
from Maix import FFT
import time
from fpioa_manager import *

fm.register(20,fm.fpioa.I2S0_IN_D0)
fm.register(19,fm.fpioa.I2S0_WS)
fm.register(18,fm.fpioa.I2S0_SCLK)
fm.register(34,fm.fpioa.I2S2_OUT_D1)
fm.register(35,fm.fpioa.I2S2_SCLK)
fm.register(33,fm.fpioa.I2S2_WS)

rx = I2S(I2S.DEVICE_0)
rx.channel_config(rx.CHANNEL_0, rx.RECEIVER, align_mode = I2S.STANDARD_MODE)
rx.set_sample_rate(16000)
tx = I2S(I2S.DEVICE_2)
tx.channel_config(tx.CHANNEL_1, tx.TRANSMITTER, align_mode = I2S.RIGHT_JUSTIFYING_MODE)
tx.set_sample_rate(16000)

while True:
    audio = rx.record(256)
    audio_data = audio.to_bytes()
    play_audio = Audio(audio_data)
    tx.play(play_audio)
```