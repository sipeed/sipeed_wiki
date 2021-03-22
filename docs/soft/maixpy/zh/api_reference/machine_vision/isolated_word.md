---
title: isolated_word（孤立词 MFCC 模块）
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: isolated_word（孤立词 MFCC 模块）
---


## 类 （class）

### isolated_word

isolated_word 构造参数如下：

- `dmac`: 录音所使用的 DMA 通道，默认使用【通道 2】。
- `i2s`: 录音设备，默认使用 I2S.DEVICE_0 。
- `size`: 词汇模板容量，表示可以加载的模板总数，默认为 10 个。
- `shift`: 声道选择，Maix 系列的硬件录音设备通常为单声道输入，设置 0 为左声道，所以 1 为右声道。

```python
from speech_recognizer import isolated_word
sr = isolated_word(dmac=2, i2s=I2S.DEVICE_0, size=10, shift=0)
```

## 方法 （function）

### size

返回当前词汇模板总量。

```python
from speech_recognizer import isolated_word
sr = isolated_word()
sr.size()
```

### set_threshold

设置孤立词模块的工作参数。

- 参数①： 噪声阈值，用于短时过零率计算
- 参数②： 短时过零率阈值，超过此阈值，视为进入过渡段。
- 参数③： 短时累加和阈值，超过此阈值，视为进入过渡段。

```python
from speech_recognizer import isolated_word
sr = isolated_word()
sr.set_threshold(0, 0, 10000)
```

### record

录入【词汇模板】。

- 参数①： 将录入的模板保存到指定的索引位置。

```python
from speech_recognizer import isolated_word
sr = isolated_word()
while True：
  if sr.Done == sr.record(0):
    pass
```

### state

可以返回如下工作状态。


| 功能  | 描述      |
| ---   | ---        |
| Init  | 模块已经初始化。       |
| Idle  | 模块正在空转，没有工作。|
| Ready   | 模块录音处理中。       |
| MaybeNoise| 模块判断是否为噪音环境。|
| Speak   | 模块等待人声录入。   |
| Restrain| 模块录入数据不合法，退回 Speak 状态。  |
| Done  | 模块语音识别成功，可通过 result 获取结果。|

### recognize

识别【词汇模板】。

```python
from speech_recognizer import isolated_word
sr = isolated_word()
while True：
  if sr.Done == sr.recognize():
    print(sr.result())
```

### result

获取【词汇模板】,返回 （匹配的模板编号、匹配的dtw值、当前的帧长、匹配的帧长） 数组。

```python
from speech_recognizer import isolated_word
sr = isolated_word()
print(sr.result())
```

### get

获取【词汇模板】,返回 （数据帧长， 数据帧） 数组。

#### 返回值

* `frm_len`:数据帧长
* `frm_data`:数据帧

```python
from speech_recognizer import isolated_word
sr = isolated_word()
print(sr.get(0))
```

### set

加载【词汇模板】到模块中。

```python
from speech_recognizer import isolated_word
sr = isolated_word()
print(sr.set(1, sr.get(0)))
```

### run

运行孤立词模块（录音）。

```python
from speech_recognizer import isolated_word
sr = isolated_word()
sr.run()
```

### reset

重置孤立词模块。

```python
from speech_recognizer import isolated_word
sr = isolated_word()
sr.reset()
```

### dtw

返回 动态时间弯折(DTW)算法 计算最优匹配值，该值越小就越好。

#### 返回值

* `dis`:累计匹配距离（int） 

```python
from speech_recognizer import isolated_word
sr = isolated_word()
print(sr.dtw(sr.get(0)))
```

### __del__

释放孤立词模块，可以主动调用，也可以被 gc.collect() 自动回收。

```python
from speech_recognizer import isolated_word
sr = isolated_word()
sr.__del__()
del sr
```
