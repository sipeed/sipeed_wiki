---
title: I2S
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: I2S
---

The I2S module is mainly used to drive I2S devices. There are 3 I2S devices in k210, and each device has 4 channels. The pins need to be mapped and managed before use.

## Module function

### Constructor

Create a new I2S object

```
from Maix import I2S
i2s_dev = I2S(device_num)
```

#### Parameters

`device_num` I2S number, use the specified I2S, you can use `I2S.` to press the tab key to complete

#### return value

Returns an `I2S` object

### Channel configuration function

Used to configure the I2S channel, the pins need to be mapped before

```
i2s_dev.channel_config(channel, mode, resolution, cycles, align_mode)
```
#### Parameters

* `channel`: I2S channel number

* `mode`: Channel transmission mode, there are a total of receiving and sending modes, recording is receiving, playing is sending

* `resolution`: Channel resolution, that is, the number of received data bits

* `cycles`: the number of single data clocks

* `align_mode`: channel alignment mode

#### return value

no

### Set the sampling rate

Used to configure I2S sampling rate

```
i2s_dev.set_sample_rate(sample_rate)
```
#### Parameters

`sample_rate`: int type, sampling rate

#### return value

no

### Receive audio

Use I2S to receive audio data

```
audio = i2s_dev.record(points)
```
#### Parameters

* `points`: The number of audio points collected at one time

#### return value

`audio`: an `audio` audio object

### Send audio

Use I2S to send audio data

```
i2s_dev.play(audio)
```
#### Parameters

* `audio`: The audio object sent

#### return value
no

## Routine

### Routine 1

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

### Routine 2

The collected data is converted into Audio and played

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
