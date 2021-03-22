---
title: Hardware accelerated image processing
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: hardware accelerated image processing
---


Using hardware to replace certain software parts can make the calculation faster. The methods of acceleration optimization have been done as follows:

The following code respectively performs `edge search`, `sharpening`, and `embossing` on the image, and uses the convolution calculation to quickly obtain the result.

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
