---
title: MaixPy Find QR code
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: MaixPy find QR code
---


Recognize the two-dimensional code from the picture. The common two-dimensional code is QR Code. The full name of QR is Quick Response. It can store more information and represent more data types than the traditional bar code (Bar Code).

## Instructions

The image module has implemented a method to find the QR code, you need to use a non-minimum firmware version, you need to prepare a QR code, you can use [caoliao QR code](https://cli.im/) to generate the content you want .

* Get pictures from the camera, and point the camera at the QR code

```python
import image, sensor
img=sensor.snapshot()
```

* Find a list of all QR code objects (image.qrcode) from the picture

```python
res = img.find_qrcodes()
```

* Manipulate QR code objects

E.g. print information

```python
print(res[0].payload())
```

For detailed API introduction, please refer to [API-Image](../../api_reference/machine_vision/image/image.md).

## Routine

Recognize the QR code. If the QR code cannot be recognized, please try to change the `sensor.vflip()` function parameter.

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
    if len(res)> 0:
        img.draw_string(2, 2, res[0].payload(), color=(0,128,0), scale=2)
        print(res[0].payload())
    lcd.display(img)
```
