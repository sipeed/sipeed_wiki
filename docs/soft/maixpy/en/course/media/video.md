---
title: Use of video
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: video (video) use
---


Detailed API reference: [video API](./../../api_reference/media/video.md)

## Instructions

> MaixAmigo, MaixCube needs [Initialize ES8374 audio decoder chip](https://github.com/sipeed/MaixPy_scripts/blob/master/modules/others/es8374/es8374.py) before using audio 

* Create a video object, set the volume

```python
import video

v = video.open("/sd/badapple.avi")
v.volume(50)
```

* Initialize lcd, used to play the screen

```python
import lcd

lcd.init()
```

* Create I2S to process audio objects

```python
from Maix import GPIO, I2S

i2s = I2S(I2S.DEVICE_0)
i2s.channel_config(i2s.CHANNEL_1, I2S.TRANSMITTER, resolution=I2S.RESOLUTION_16_BIT,
                       cycles=I2S.SCLK_CYCLES_32, align_mode=I2S.RIGHT_JUSTIFYING_MODE)
fm.register(34, fm.fpioa.I2S0_OUT_D1, force=True)
fm.register(35, fm.fpioa.I2S0_SCLK, force=True)
fm.register(33, fm.fpioa.I2S0_WS, force=True)

```

* Play video

```python
while True:
    if v.play() == 0:
        print("play end")
        break
```

* Recycling objects

```python
v.__del__()
```

## Routine

> The avi file address in the test case: [badapple.avi](https://api.dl.sipeed.com/shareURL/MAIX/MaixPy/assets)

* Play avi files: [video_play](https://github.com/sipeed/MaixPy_scripts/blob/master/multimedia/video/demo_video_play.py)
* Use the camera to record the video as an avi file and save it: [record_video](https://github.com/sipeed/MaixPy_scripts/blob/master/multimedia/video/demo_video_record.py)
* Sequentially capture and display each frame of avi video: [video_capture](https://github.com/sipeed/MaixPy_scripts/blob/master/multimedia/video/demo_video_capture.py)
* Amigo play avi files: [amigo_play_video](https://github.com/sipeed/MaixPy_scripts/blob/master/multimedia/video/amigo_play_video.py)
