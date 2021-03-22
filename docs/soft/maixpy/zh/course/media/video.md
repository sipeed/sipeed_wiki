---
title: video（视频） 的使用
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: video（视频） 的使用
---


详细 API 参考：[video API](./../../api_reference/media/video.md)

## 使用方法

> MaixAmigo, MaixCube在使用音频前需要[初始化 ES8374 音频解码芯片](https://github.com/sipeed/MaixPy_scripts/blob/master/modules/others/es8374/es8374.py)

* 创建 video 对象，设置音量

```python 
import video

v = video.open("/sd/badapple.avi")
v.volume(50)
```

* 初始化 lcd，用于播放画面

```python
import lcd

lcd.init()
```

* 创建 I2S，用于处理音频对象

```python
from Maix import GPIO, I2S

i2s = I2S(I2S.DEVICE_0)
i2s.channel_config(i2s.CHANNEL_1, I2S.TRANSMITTER, resolution=I2S.RESOLUTION_16_BIT,
                       cycles=I2S.SCLK_CYCLES_32, align_mode=I2S.RIGHT_JUSTIFYING_MODE)
fm.register(34,  fm.fpioa.I2S0_OUT_D1, force=True)
fm.register(35,  fm.fpioa.I2S0_SCLK, force=True)
fm.register(33,  fm.fpioa.I2S0_WS, force=True)

```

* 播放视频

```python
while True:
    if v.play() == 0:
        print("play end")
        break
```

* 回收对象

```python
v.__del__()
```

## 例程

> 测试用例中 avi 文件地址：[badapple.avi](https://api.dl.sipeed.com/shareURL/MAIX/MaixPy/assets)

* 播放 avi 文件：[video_play](https://github.com/sipeed/MaixPy_scripts/blob/master/multimedia/video/demo_video_play.py)
* 使用摄像头录制视频为 avi 文件并保存：[record_video](https://github.com/sipeed/MaixPy_scripts/blob/master/multimedia/video/demo_video_record.py)
* 顺序捕获 avi 视频每个画面并显示：[video_capture](https://github.com/sipeed/MaixPy_scripts/blob/master/multimedia/video/demo_video_capture.py)
* amigo 播放 avi 文件：[amigo_play_video](https://github.com/sipeed/MaixPy_scripts/blob/master/multimedia/video/amigo_play_video.py)
