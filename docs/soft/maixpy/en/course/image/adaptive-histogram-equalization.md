---
title:
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc:
---



```python
# Adaptive histogram equalization example
#
# This example shows how to use adaptive histogram equalization to improve the contrast in the image.
#Adaptive histogram equalization divides the image into regions, and then equalizes the histograms in these regions,
#To improve image contrast and global histogram equalization.
#In addition, you can specify clipping limits to prevent the contrast from becoming wild.

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()

while(True):
    clock.tick()

    # clip_limit <0 provides you with normal adaptive histogram equalization, which may cause a lot of contrast noise...

    # clip_limit=1 Do nothing. For best results, please slightly higher than 1, as shown below.
    # The higher the value, the closer it is to the standard adaptive histogram equalization, and will produce huge contrast fluctuations.

    img = sensor.snapshot().histeq(adaptive=True, clip_limit=3)

    print(clock.fps())
```
