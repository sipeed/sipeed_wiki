---
title: isolated word
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: isolated word
---


> **This document has passed the MaixPy 0.5.1_128 minimum_speech_with_ide_support firmware test. Please make sure the hardware recording function is available before use.**

This is an algorithm module for isolated word recognition. The user generates a vocabulary template through recording and loads it into the module, and then recognizes the vocabulary template loaded by the user through it, and returns the possibility of matching. Please refer to [STM32-based isolated word speech recognition ](https://gk969.com/stm32-speech-recognition/).

- Isolated word recognition

    According to the way of pronunciation, there are three types: isolated word recognition, connected word recognition, and continuous speech recognition; the so-called isolated word recognition (Isolated Word Recognition) means that when the sound to be recognized is issued, only one word in the vocabulary is included at a time Article.

- Vocabulary template

    We record a vocabulary spoken by the human voice and use algorithms to make it into a recognizable template, which is called a vocabulary template.

- Template matching

    Assuming that the algorithm module is loaded with a vocabulary template, after we input data to the algorithm module through recording, it will perform internal matching to obtain the most likely recognition result.

> The specific identification process of this module is: pre-filtering, ADC, framing, endpoint detection, pre-emphasis, windowing, feature extraction, feature matching. Endpoint detection (VAD) uses a combination of short-term amplitude and short-term zero-crossing rate. After detecting the effective speech, according to the human hearing perception characteristics, the Mel frequency cepstral coefficient (MFCC) of each frame of speech is calculated. Then the dynamic time warping (DTW) algorithm is used to match the feature template, and the recognition result is finally output.

## how to use?

Current hardware support level: Maix BIT / DOCK / DUINO / GO.

> As of 20201123, after the Cube & Amigo has passed ES8374, the microphone's noise floor is too high and it will be judged as a noisy environment, which needs to be repaired.

### Sample code out of the box

-Use the test case of maixduino/maixbit [isolated_word.py](https://github.com/sipeed/MaixPy_scripts/blob/master/multimedia/speech_recognizer/isolated_word.py), please read the code for the usage method, please pay attention to the microphone of the hardware Configuration and channel configuration.
-Maix DOCK can directly use the sample code [demo_isolated_word_on_maixdock.py](https://github.com/sipeed/MaixPy_scripts/blob/master/multimedia/speech_recognizer/demo_isolated_word_on_maixdock.py), just follow the on-screen instructions to speak, see [ Test video](https://www.bilibili.com/video/BV1oz4y1C7yE?from=search&seid=17464946072274851468).

### Module call flow

In order to better use this module, please understand the usage process.

#### Prepare I2S recording module

Configure an I2S.DEVICE_0 device and set the CHANNEL_0 channel to the recording input.

```python
from Maix import GPIO, I2S
from fpioa_manager import fm

fm.register(20,fm.fpioa.I2S0_IN_D0, force=True)
fm.register(18,fm.fpioa.I2S0_SCLK, force=True) # dock 32
fm.register(19,fm.fpioa.I2S0_WS, force=True) # dock 30

rx = I2S(I2S.DEVICE_0)
rx.channel_config(rx.CHANNEL_0, rx.RECEIVER, align_mode=I2S.STANDARD_MODE)
rx.set_sample_rate(16000)
print(rx)
```

operation result:

```shell
[MAIXPY]i2s0:(sampling rate=16003, sampling points=1024)
[MAIXPY]channle0:(resolution=2, cycles=2, align_mode=1, mode=1)
[MAIXPY]channle1:(resolution=0, cycles=0, align_mode=0, mode=0)
[MAIXPY]channle2:(resolution=0, cycles=0, align_mode=0, mode=0)
[MAIXPY]channle3:(resolution=0, cycles=0, align_mode=0, mode=0)
```

#### Create an isolated word module

The parameters initialized by isolated_word are as follows:

- [dmac] The DMA channel used for recording. [Channel 2] is used by default.
- [i2s] Recording device, I2S.DEVICE_0 is used by default.
- [size] The capacity of vocabulary templates, which means the total number of templates that can be loaded. The default is 10.
- [shift] Channel selection. Maix series hardware recording devices usually use mono input. Set 0 as the left channel, so 1 is the right channel.

```python
from speech_recognizer import isolated_word

# default: maix dock / maix duino set shift=0
sr = isolated_word(dmac=2, i2s=I2S.DEVICE_0, size=10, shift=0) # maix bit set shift=1
print(sr.size())
print(sr)

## threshold
sr.set_threshold(0, 0, 10000)
```

The results are as follows:

```shell
10
[MAIXPY] isolated_word:(80212a60)
 mfcc_dats=8023a060

 size=10

 i2s_device_number_t=0

 dmac_channel_number_t=2
```

#### Entry vocabulary template

Call the following code:

- If the surrounding environment is very noisy, it will output 2 (isolated_word.Ready) to 3 (isolated_word.MaybeNoise) repeatedly, and you need to be in a quiet environment to enter the vocabulary template
- If the status is isolated_word.Speak, it means you can speak
- If you run sr.record(0) and its status changes to isolated_word.Done, it means the recording is complete and it will be saved to the template number 0.
- You can check the current module status through sr.state()

```python
## record and get & set
while True:
  time.sleep_ms(100)
  print(sr.state())
  if sr.Done == sr.record(0):
    data = sr.get(0)
    print(data)
    break
  if sr.Speak == sr.state():
    print('speak A')
#sr.set(1, data)
```

In the same way, if you want to enter the second [Vocabulary Template], you only need to change the entry position, such as to sr.record(1) (the computer storage array starts counting from 0).

#### Identify vocabulary templates

Assuming that you have entered [Vocabulary Template], call the following code, it will continue to recognize the current voice and start matching the entered [Vocabulary Template], which is the so-called isolated word speech recognition.

```python
print('recognizer')
while True:
  time.sleep_ms(200)
  #print(sr.state())
  #print(sr.dtw(data))
  if sr.Done == sr.recognize():
    res = sr.result()
    print(res)
```

The final effect is to print out the best matching [word template] number and related data. For details, please check the result function usage. You can judge whether the recognition is reasonable according to the actual situation, such as whether the matching frame length/matching degree meets expectations , Too large or too small are unreasonable.
