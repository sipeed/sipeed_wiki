---
title: isolated_word (isolated word MFCC module)
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: isolated_word (isolated word MFCC module)
---


## Class (class)

### isolated_word

The isolated_word construction parameters are as follows:

-`dmac`: DMA channel used for recording. [Channel 2] is used by default.
-`i2s`: Recording device, I2S.DEVICE_0 is used by default.
-`size`: The capacity of vocabulary templates, which means the total number of templates that can be loaded. The default is 10.
-`shift`: Channel selection. Maix series hardware recording devices usually use mono input. Set 0 as the left channel, so 1 is the right channel.

```python
from speech_recognizer import isolated_word
sr = isolated_word(dmac=2, i2s=I2S.DEVICE_0, size=10, shift=0)
```

## Method (function)

### size

Returns the total number of current word templates.

```python
from speech_recognizer import isolated_word
sr = isolated_word()
sr.size()
```

### set_threshold

Set the working parameters of the isolated word module.

-Parameter①: Noise threshold, used for short-time zero-crossing rate calculation
-Parameter ②: Short-time zero-crossing rate threshold, exceeding this threshold is regarded as entering the transition section.
-Parameter ③: Short-term accumulation and threshold value. If the threshold is exceeded, it is regarded as entering the transition section.

```python
from speech_recognizer import isolated_word
sr = isolated_word()
sr.set_threshold(0, 0, 10000)
```

### record

Enter [Vocabulary Template].

-Parameter ①: Save the entered template to the specified index location.

```python
from speech_recognizer import isolated_word
sr = isolated_word()
while True:
  if sr.Done == sr.record(0):
    pass
```

### state

You can return to the following working status.


| Function | Description |
| --- | --- |
| Init | The module has been initialized. |
| Idle | The module is idling and is not working. |
| Ready | Module recording is processing. |
| MaybeNoise| The module determines whether it is a noise environment. |
| Speak | The module waits for voice recording. |
| Restrain| The data entered by the module is illegal, and the module returns to the Speak state. |
| Done | The module voice recognition is successful, and the result can be obtained through result. |

### recognize

Recognize [word template].

```python
from speech_recognizer import isolated_word
sr = isolated_word()
while True:
  if sr.Done == sr.recognize():
    print(sr.result())
```

### result

Get [Vocabulary Template] and return an array of (matched template number, matched dtw value, current frame length, matched frame length).

```python
from speech_recognizer import isolated_word
sr = isolated_word()
print(sr.result())
```

### get

Get 【Vocabulary Template】, and return (data frame length, data frame) array.

#### return value

* `frm_len`: data frame length
* `frm_data`: data frame

```python
from speech_recognizer import isolated_word
sr = isolated_word()
print(sr.get(0))
```

### set

Load [Vocabulary Template] into the module.

```python
from speech_recognizer import isolated_word
sr = isolated_word()
print(sr.set(1, sr.get(0)))
```

### run

Run the isolated word module (recording).

```python
from speech_recognizer import isolated_word
sr = isolated_word()
sr.run()
```

### reset

Reset the isolated word module.

```python
from speech_recognizer import isolated_word
sr = isolated_word()
sr.reset()
```

### dtw

Back to Dynamic Time Warping (DTW) algorithm Calculate the optimal matching value, the smaller the value, the better.

#### return value

* `dis`: Cumulative matching distance (int)

```python
from speech_recognizer import isolated_word
sr = isolated_word()
print(sr.dtw(sr.get(0)))
```

### __del__

To release the orphan word module, it can be called actively, or it can be automatically collected by gc.collect().

```python
from speech_recognizer import isolated_word
sr = isolated_word()
sr.__del__()
del sr
```
