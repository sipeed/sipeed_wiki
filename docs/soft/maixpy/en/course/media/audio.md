---
title: the use of audio
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: audio (audio) use
---


Detailed API reference: [audio API](./../../api_reference/media/audio.md)

## Instructions

> MaixAmigo, MaixCube needs [Initialize ES8374 audio decoder chip](https://github.com/sipeed/MaixPy_scripts/blob/master/modules/others/es8374/es8374.py) before using audio 

* Create audio object

```python
import audio

player = audio.Audio(path = "/sd/6.wav")
```

* Create I2S objects (used to process audio objects)

```python
from Maix import I2S

# init i2s(i2s0)
wav_dev = I2S(I2S.DEVICE_0)
# config i2s according to audio info
wav_dev.channel_config(wav_dev.CHANNEL_1, I2S.TRANSMITTER,resolution = I2S.RESOLUTION_16_BIT ,cycles = I2S.SCLK_CYCLES_32, align_mode = I2S.RIGHT_JUSTIFYING_MODE)
```

* Get audio object information and associate I2S object

```python
# read audio info
wav_info = player.play_process(wav_dev)
print("wav file head information: ", wav_info)
```

* Configure I2S objects according to audio information

```python
sample_rate = wav_info[1]
wav_dev.set_sample_rate(sample_rate)
```

* Use the associated I2S object to play audio

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

* End playback

```python
player.finish()
```

## Routine

> Test audio address: [6.wav](https://github.com/sipeed/MaixPy_scripts/blob/master/multimedia/audio/6.wav)

* Play wav files: [play_wav](https://github.com/sipeed/MaixPy_scripts/blob/master/multimedia/audio/play_wav.py)
* Record audio as a wav file and save: [record_wav](https://github.com/sipeed/MaixPy_scripts/blob/master/multimedia/audio/record_wav.py)
