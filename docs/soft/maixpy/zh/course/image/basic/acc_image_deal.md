---
title: 硬件加速的图像处理
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 硬件加速的图像处理
---


使用硬件替换某些软件部分， 可以让计算更加快速，已经做了加速优化的方法如下：

如下代码， 分别对图像进行了`边缘查找`，`锐化`，`浮雕化`， 利用了卷积计算快速得到结果。

```python
import sensor
import image
import lcd
import time

lcd.init(freq=15000000)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
origin = (0,0,0, 0,1,0, 0,0,0)
edge = (-1,-1,-1,-1,8,-1,-1,-1,-1)
sharp = (-1,-1,-1,-1,9,-1,-1,-1,-1)
relievo = (2,0,0,0,-1,0,0,0,-1)

tim = time.time()
while True:
    img=sensor.snapshot()
    img.conv3(edge)
    lcd.display(img)
    if time.time() -tim >10:
        break
tim = time.time()
while True:
    img=sensor.snapshot()
    img.conv3(sharp)
    lcd.display(img)
    if time.time() -tim >10:
        break
tim = time.time()
while True:
    img=sensor.snapshot()
    img.conv3(relievo)
    lcd.display(img)
    if time.time() -tim >10:
        break

lcd.clear()
```
