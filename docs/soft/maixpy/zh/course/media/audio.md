---
title: audio（音频） 的使用
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: audio（音频） 的使用
---


详细 API 参考：[audio API](./../../api_reference/media/audio.md)

## 使用方法

> MaixAmigo, MaixCube 在使用音频前需要[初始化 ES8374 音频解码芯片](https://github.com/sipeed/MaixPy_scripts/blob/master/modules/others/es8374/es8374.py)

* 创建 audio 对象

```python 
import audio

player = audio.Audio(path = "/sd/6.wav")
```

* 创建 I2S 对象（用于处理音频对象）

```python
from Maix import I2S

# init i2s(i2s0)
wav_dev = I2S(I2S.DEVICE_0)
# config i2s according to audio info
wav_dev.channel_config(wav_dev.CHANNEL_1, I2S.TRANSMITTER,resolution = I2S.RESOLUTION_16_BIT ,cycles = I2S.SCLK_CYCLES_32, align_mode = I2S.RIGHT_JUSTIFYING_MODE)
```

* 获取 audio 对象信息并关联 I2S 对象

```python
# read audio info
wav_info = player.play_process(wav_dev)
print("wav file head information: ", wav_info)
```

* 根据 audio 信息配置 I2S 对象

```python
sample_rate = wav_info[1]
wav_dev.set_sample_rate(sample_rate)
```

* 使用已关联的 I2S 对象播放音频

```python
# loop to play audio
while True:
    ret = player.play()
    if ret == None:
        print("format error")
        break
    elif ret==0:
        print("end")
        break
```

* 结束播放

```python
player.finish()
```

## 例程

> 测试音频地址：[6.wav](https://github.com/sipeed/MaixPy_scripts/blob/master/multimedia/audio/6.wav)

* 播放 wav 文件：[play_wav](https://github.com/sipeed/MaixPy_scripts/blob/master/multimedia/audio/play_wav.py)
* 录制音频为 wav 文件并保存：[record_wav](https://github.com/sipeed/MaixPy_scripts/blob/master/multimedia/audio/record_wav.py)
