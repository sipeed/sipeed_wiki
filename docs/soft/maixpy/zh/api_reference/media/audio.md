---
title: audio（音频）
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: audio（音频）
---


抽象的音频对象，该对象可以被当做参数传入也可以直接使用其方法来播放音频

## 模块函数

###  构造函数

构造 `Audio` 对象

```python
audio.Audio(array=None, path=None, points=1024)
```

####  参数

该接口能传入一个参数，每个参数会决定不同的音频类型

* `array`: `bytearray`类型的数据，可以将该数据转换为音频对象， 默认 `None`

* `path`: 打开的音频文件路径，目前仅支持 `wav` 格式， 默认 `None`, **注意**需要标明关键字`path`，`audio.Audio("/sd/1.wav")`这样是错的！！ `audio.Audio(path = "/sd/1.wav")` 才是正确的

* `points`: 开辟有 points 个采样点数的音频缓冲，一个采样点大小为 32bit。为0的情况下将不开辟缓冲, 默认 `1024`

####  返回值

返回一个 `Audio` 对象


### to_bytes: bytes转换函数

将音频对象中的音频数据转换为 `bytearray` 类型的对象

```
audio_data = test_audio.to_bytes()
```

####  参数

无

####  返回值

返回的音频数据 `bytearray` 对象


### play_process: 播放预处理函数

用于预处理音频对象，在播放之前需要对音频文件进行解析，所以需要预处理。这里需要传入一个播放用的 I2S 设备

```
wav_info = test_audio.play_process(i2s_dev)
```

####  参数

* `i2s_dev`: 用于播放的i2s设备


####  返回值

该 wav 文件的头部信息 ,`list`类型，分别是`numchannels`（声道数）, `samplerate`（采样率）, `byterate`（每秒数据字节数=samplerate * numchannels * bitspersample / 8）, `blockalign`（每个采样所需的字节数 = numchannels * bitspersample / 8）, `bitspersample`（每个采样存储的bit数，8：8bit，16：16bit，32：32bit）, `datasize`（音频数据长度）

### play: 播放函数

读取音频文件并且解析播放，一般配合循环来使用


####  参数

无


####  返回值

* `None`： 格式不支持播放
* `0`： 播放结束
* `1`： 正在播放

### finish： 音频后处理函数

完成音频播放，该函数必须在播放完毕后调用，回收底层分配的资源


####  参数

无

####  返回值

无

## 例程

播放 `wav` 音频

```python 
from fpioa_manager import *
from Maix import I2S, GPIO
import audio

# disable wifi
fm.register(8, fm.fpioa.GPIO0)
wifi_en=GPIO(GPIO.GPIO0,GPIO.OUT)
wifi_en.value(0)

# register i2s(i2s0) pin
fm.register(34,fm.fpioa.I2S0_OUT_D1)
fm.register(35,fm.fpioa.I2S0_SCLK)
fm.register(33,fm.fpioa.I2S0_WS)

# init i2s(i2s0)
wav_dev = I2S(I2S.DEVICE_0)

# init audio
player = audio.Audio(path = "/sd/6.wav")
player.volume(40)

# read audio info
wav_info = player.play_process(wav_dev)
print("wav file head information: ", wav_info)

# config i2s according to audio info
wav_dev.channel_config(wav_dev.CHANNEL_1, I2S.TRANSMITTER,resolution = I2S.RESOLUTION_16_BIT ,cycles = I2S.SCLK_CYCLES_32, align_mode = I2S.RIGHT_JUSTIFYING_MODE)
wav_dev.set_sample_rate(wav_info[1])

# loop to play audio
while True:
    ret = player.play()
    if ret == None:
        print("format error")
        break
    elif ret==0:
        print("end")
        break
player.finish()
```
