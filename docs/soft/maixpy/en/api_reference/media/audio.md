---
title: audio
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: audio (audio)
---


Abstract audio object, which can be passed in as a parameter or directly use its method to play audio

## Module function

###  Constructor

Construct an `Audio` object

```python
audio.Audio(array=None, path=None, points=1024)
```

#### Parameters

The interface can pass in a parameter, each parameter will determine a different audio type

* `array`: `bytearray` type data, which can be converted into audio objects, the default is `None`

* `path`: Open audio file path, currently only supports `wav` format, default is `None`, **Note** The keyword `path`, `audio.Audio("/sd/1.wav" needs to be marked) )`This is wrong! ! `audio.Audio(path = "/sd/1.wav")` is correct

* `points`: Open up an audio buffer with points sampling points, one sampling point is 32bit. If it is 0, the buffer will not be opened, and the default is 1024.

####  return value

Returns an `Audio` object


### to_bytes: bytes conversion function

Convert the audio data in the audio object to an object of type `bytearray`

```
audio_data = test_audio.to_bytes()
```

#### Parameters

no

####  return value

The returned audio data `bytearray` object


### play_process: Play preprocessing function

It is used to preprocess audio objects. The audio file needs to be parsed before playing, so preprocessing is required. Here you need to pass in an I2S device for playback

```
wav_info = test_audio.play_process(i2s_dev)
```

#### Parameters

* `i2s_dev`: i2s device for playback


####  return value

The header information of the wav file, `list` type, are `numchannels` (number of channels), `samplerate` (sampling rate), `byterate` (number of data bytes per second = samplerate * numchannels * bitspersample / 8 ), `blockalign` (the number of bytes required for each sample = numchannels * bitspersample / 8), `bitspersample` (the number of bits stored in each sample, 8: 8bit, 16: 16bit, 32: 32bit), `datasize `(audio data length)

### play: play function

Read audio files and parse them for playback, generally used with loop


#### Parameters

no


####  return value

* `None`: The format does not support playback
* `0`: End of playback
* `1`: Now playing

### finish: Audio post-processing function

To complete the audio playback, this function must be called after the playback is completed to recover the resources allocated by the bottom layer


#### Parameters

no

####  return value

no

## Routine

Play `wav` audio

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
