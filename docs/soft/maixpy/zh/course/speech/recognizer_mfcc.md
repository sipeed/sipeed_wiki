---
title: isolated word
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: isolated word
---


> **本文档在 MaixPy 0.5.1_128 minimum_speech_with_ide_support 固件测试通过，使用前请确保硬件录音功能可用。**

这是一个孤立词识别的算法模块,用户通过录音生成词汇模板加载到模块中，再通过它识别到用户加载的词汇模板，并返回匹配的可能性，实现请参考[基于STM32的孤立词语音识别](https://gk969.com/stm32-speech-recognition/)。

- 孤立词识别

    按照语音发音方式来分，有孤立词识别、连接词识别、连续语音识别 3 种；所谓孤立词识别（Isolated Word Recognition）是指在发待识别音时，每次只含词汇表中的一个词条。

- 词汇模板

    我们将一段用人声说出的词汇录音下来，通过算法制作成可识别的模板，称为词汇模板。

- 模板匹配

    假设算法模块加载了词汇模板，我们通过录音输入数据给算法模块后，它会进行内部匹配得到最有可能的识别结果。

> 本模块具体识别流程是：预滤波、ADC、分帧、端点检测、预加重、加窗、特征提取、特征匹配。端点检测(VAD)采用短时幅度和短时过零率相结合。检测出有效语音后，根据人耳听觉感知特性，计算每帧语音的Mel频率倒谱系数(MFCC)。然后采用动态时间弯折(DTW)算法与特征模板相匹配，最终输出识别结果。

## 如何使用？

目前硬件支持程度：Maix BIT / DOCK / DUINO / GO 。

> 截至 20201123 由于 Cube & Amigo 经过 ES8374 后，麦克风底噪过大会被判断为噪音环境，还需要修复。

### 开箱即用示例代码

- 使用 maixduino / maixbit 的测试用例 [isolated_word.py](https://github.com/sipeed/MaixPy_scripts/blob/master/multimedia/speech_recognizer/isolated_word.py)，使用方法请阅读代码，请注意硬件的 麦克风 配置 和 声道 配置。
- Maix DOCK 可直接使用的示例代码[demo_isolated_word_on_maixdock.py](https://github.com/sipeed/MaixPy_scripts/blob/master/multimedia/speech_recognizer/demo_isolated_word_on_maixdock.py)，按屏幕提示说话即可，具体看[测试录像](https://www.bilibili.com/video/BV1oz4y1C7yE?from=search&seid=17464946072274851468)。

### 模块调用流程

为了能够更好地使用本模块，请了解使用流程。

#### 准备 I2S 录音模块

配置一个 I2S.DEVICE_0 设备，并设置 CHANNEL_0 通道到录音输入。

```python
from Maix import GPIO, I2S
from fpioa_manager import fm

fm.register(20,fm.fpioa.I2S0_IN_D0, force=True)
fm.register(18,fm.fpioa.I2S0_SCLK, force=True) # dock 32
fm.register(19,fm.fpioa.I2S0_WS, force=True)   # dock 30

rx = I2S(I2S.DEVICE_0)
rx.channel_config(rx.CHANNEL_0, rx.RECEIVER, align_mode=I2S.STANDARD_MODE)
rx.set_sample_rate(16000)
print(rx)
```

运行结果：

```shell
[MAIXPY]i2s0:(sampling rate=16003, sampling points=1024)
[MAIXPY]channle0:(resolution=2, cycles=2, align_mode=1, mode=1)
[MAIXPY]channle1:(resolution=0, cycles=0, align_mode=0, mode=0)
[MAIXPY]channle2:(resolution=0, cycles=0, align_mode=0, mode=0)
[MAIXPY]channle3:(resolution=0, cycles=0, align_mode=0, mode=0)
```

#### 创建 孤立词 模块

isolated_word 初始化的参数如下：

- [dmac] 录音所使用的 DMA 通道，默认使用【通道 2】。
- [i2s] 录音设备，默认使用 I2S.DEVICE_0 。
- [size] 词汇模板容量，表示可以加载的模板总数，默认为 10 个。
- [shift] 声道选择，Maix 系列的硬件录音设备通常为单声道输入，设置 0 为左声道，所以 1 为右声道。

```python
from speech_recognizer import isolated_word

# default: maix dock / maix duino set shift=0
sr = isolated_word(dmac=2, i2s=I2S.DEVICE_0, size=10, shift=0) # maix bit set shift=1
print(sr.size())
print(sr)

## threshold
sr.set_threshold(0, 0, 10000)
```

运行结果如下：

```shell
10
[MAIXPY] isolated_word:(80212a60)
 mfcc_dats=8023a060

 size=10

 i2s_device_number_t=0

 dmac_channel_number_t=2
```

#### 录入词汇模板

调用如下代码：

- 如果周围环境很嘈杂，它就会反复输出 2 (isolated_word.Ready) 到 3 (isolated_word.MaybeNoise) ，需要处于安静环境下才能录入词汇模板
- 如果状态为 isolated_word.Speak 则表示你可以说话了
- 如果运行 sr.record(0) 它状态变成了 isolated_word.Done 则表示录入完成，并保存到编号 0 的模板。
- 你可以通过 sr.state() 可以查看当前模块的状态

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

同理，如果你要录入第二个【词汇模板】，只需要改变录入的位置，如改成 sr.record(1)（计算机存储数组从 0 开始计数）。

#### 识别词汇模板

假设你已经录入了【词汇模板】则调用如下代码，它会持续识别当前的声音开始匹配录入的【词汇模板】，也就是所谓的孤立词语音识别。

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

最终呈现的效果就是打印出最优匹配的【词汇模板】编号以及相关数据，具体请查看 result 函数用法，可以根据实际情况来判断本次识别是否合理，如匹配的帧长/匹配度是否符合预期，过大或过小都是不合理的。
