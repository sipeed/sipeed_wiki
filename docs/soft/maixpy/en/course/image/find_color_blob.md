---
title: MaixPy Find color blocks
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: MaixPy find color blocks
---


Find all color blocks of the specified color in the picture

## Instructions

MaixPy has implemented a method to find color patches in the image module, and a non-minimum firmware version is required.

* Get pictures from the camera

```python
import image, sensor
img=sensor.snapshot()
```

* Find a list of all color block objects (image.blob) from the picture, and the incoming color threshold parameters follow the LAB format (l_lo, l_hi, a_lo, a_hi, b_lo, b_hi)

```python
green_threshold = (0, 80, -70, -10, -0, 30)
blobs = img.find_blobs([green_threshold])
```

* Manipulate color block objects
  
Operate the color block object according to your own needs, for example, mark the color block object with a rectangular frame in the image

```python
tmp=img.draw_rectangle(b[0:4])
```

For detailed API introduction, please refer to [API-Image](../../api_reference/machine_vision/image/image.md).

## Routine

Find the green patch

```python
import sensor
import image
import lcd
import time
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
green_threshold = (0, 80, -70, -10, -0, 30)
while True:
    img=sensor.snapshot()
    blobs = img.find_blobs([green_threshold])
    if blobs:
        for b in blobs:
            tmp=img.draw_rectangle(b[0:4])
            tmp=img.draw_cross(b[5], b[6])
            c=img.get_pixel(b[5], b[6])
    lcd.display(img)
```
