---
title: MaixPy 查找色块
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: MaixPy 查找色块
---


找出图片中指定颜色所有色块

## 使用方法

MaixPy 已经在 image 模块中实现有查找色块方法，需要使用非 minimum 固件版本。

* 从摄像头获取图片

```python
import image, sensor
img=sensor.snapshot()
```

* 从图片中查找所有色块对象(image.blob)列表, 传入的颜色阈值参数按照 LAB 格式(l_lo，l_hi，a_lo，a_hi，b_lo，b_hi)

```python
green_threshold   = (0,   80,  -70,   -10,   -0,   30)
blobs = img.find_blobs([green_threshold])
```

* 操作色块对象
  
根据自己的需求操作色块对象, 例如将色块对象在图像中用矩形框标识出来

```python
tmp=img.draw_rectangle(b[0:4])
```

详细 API 介绍请查看[API-Image](../../api_reference/machine_vision/image/image.md).

## 例程

找绿色色块

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
green_threshold   = (0,   80,  -70,   -10,   -0,   30)
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
