---
title: video
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: video (video)
---



Supports playback and recording of `avi` video

## Global functions

### open(path, record=False, interval=100000, quality=50, width=320, height=240, audio=False, sample_rate=44100, channels=1)

Open a file to play or record

#### Parameters

* `path`: file path, such as `/sd/badapple.avi`
* `record`: Whether to record, if you select `Ture`, the video will be recorded, otherwise it will be played. Default `False`
* `interval`: The recording frame interval, the unit is microseconds, fps = 1000000/interval, the default is `100000`, that is, `10` frames per second
* `quality`: `jpeg` compression quality (`%`), default `50`
* `width`: recording screen width, default `320`
* `height`: Record screen height, default `240`
* `audio`: Whether to record audio, default is `False`
* `sample_rate`: Record audio sample rate, default `44100` (`44.1k`)
* `channels`: the number of recorded audio channels, the default is `1`, which is mono

#### return value

Return an object, the object returned is different according to different formats.

Currently only the `avi` format is supported, and objects created by the `avi` class are returned

## Class `avi`

Returned by the `video.open()` function

### play()

Play video, parse the data (audio or video) every time it is called

#### return value

* `0`: End of playback
* `1`: Now playing
* `2`: Pause (reserve)
* `3`: The currently decoded frame is a video frame
* `4`: The currently decoded frame is an audio frame

### capture(img)

Capture video frames (sequential capture)

#### Parameters

* `img`: image object, used to store the captured image

#### return value

* `0`: The end of the video has been reached
* `3`: The video frame is successfully captured

### volume(volume)

Set volume

#### Parameters

* `volume`: volume value, value range: [0,100]

#### return value

Set volume value, value range [0,100]


### record()

Record video and audio. Each time you call to record one frame, the function will limit the speed. If the recording interval is not reached, it will block before reaching the set interval.

#### return value

The length of the current frame of the recorded video




## Routine

### Example 1: Play `avi` video

First of all, make sure that the video is `320x240` size, the video compression format is `mjpeg`, and the audio compression format is `PCM`.

You can download the video that can be used for testing here: [badapple.avi](http://api.dl.sipeed.com/shareURL/MAIX/MaixPy/assets)

```python
import video,time
from Maix import GPIO

fm.register(34, fm.fpioa.I2S0_OUT_D1)
fm.register(35, fm.fpioa.I2S0_SCLK)
fm.register(33, fm.fpioa.I2S0_WS)
fm.register(8, fm.fpioa.GPIO0)
wifi_en=GPIO(GPIO.GPIO0,GPIO.OUT)
wifi_en.value(0)

v = video.open("/sd/badapple.avi")
print(v)
v.volume(50)
while True:
    if v.play() == 0:
        print("play end")
        break
v.__del__()

```

By default, `I2S0` is used to play audio, so you need to set the pin corresponding to `I2S0`. Turn off the WiFi because the WiFi of the `Dock` board interferes with the sound quality


### Example 2: Record `avi` video


```python

import sensor, image, lcd, time

lcd.init(freq=15000000)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)

sensor.set_hmirror(1)
sensor.set_vflip(1)

sensor.run(1)
sensor.skip_frames(30)

import video

v = video.open("/sd/capture.avi", audio = False, record=1, interval=200000, quality=50)

tim = time.ticks_ms()
for i in range(50):
    tim = time.ticks_ms()
    img = sensor.snapshot()
    lcd.display(img)
    img_len = v.record(img)
    # print("record",time.ticks_ms()-tim)

print("record_finish")
v.record_finish()
v.__del__()

# play your record
v = video.open("/sd/capture.avi")
print(v)
v.volume(50)
while True:
    if v.play() == 0:
        print("play end")
        break

print("play finish")
v.__del__()

lcd.clear()
```

You can cancel the print mask to see if the actual recording interval has reached the set frame interval (for example, the `200000us` set here), the actual printing should be `200ms`,
If the actual frame interval is greater than the set value, it means that the actual performance does not meet the set requirements. You need to increase the set frame interval to reduce the frame rate.
In addition, removing the display and printing can also increase the frame rate to a certain extent.

### Example 3: Sequence `avi` to capture video frames and display

```python
import lcd
import video
import image

lcd.init()
v = video.open("/sd/badapple_320_240_15fps.avi")
print(v)
img = image.Image()
while True:
    status = v.capture(img)
    if status != 0:
        lcd.display(img)
    else:
        print("end")
        break;
v.__del__()
```
