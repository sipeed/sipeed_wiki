---
title: MaixPy 查找二维码
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: MaixPy 查找二维码
---


从图片中识别二维码，常见的二维码为 QR Code，QR 全称 Quick Response，它比传统的条形码(Bar Code)能存更多的信息，也能表示更多的数据类型.

## 使用方法

image 模块中已经实现有查找二维码方法，需要使用非 minimum 固件版本，需要准备一个二维码，可以用[草料二维码](https://cli.im/)生成你想要的内容.

* 从摄像头获取图片，将摄像头对准二维码

```python
import image, sensor
img=sensor.snapshot()
```

* 从图片中查找所有二维码对象(image.qrcode)列表

```python
res = img.find_qrcodes()
```

* 操作二维码对象

例如打印信息

```python
print(res[0].payload())
```

详细 API 介绍请查看[API-Image](../../api_reference/machine_vision/image/image.md).

## 例程

识别二维码，如果识别不到二维码，请尝试更改 `sensor.vflip()` 函数参数。

```python
import sensor
import image
import lcd
import time

clock = time.clock()
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(1)
sensor.run(1)
sensor.skip_frames(30)
while True:
    clock.tick()
    img = sensor.snapshot()
    res = img.find_qrcodes()
    fps =clock.fps()
    if len(res) > 0:
        img.draw_string(2, 2, res[0].payload(), color=(0,128,0), scale=2)
        print(res[0].payload())
    lcd.display(img)
```
