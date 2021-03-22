---
title: nuclear filtering
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: nuclear filtering
---


![image-20200812191240724](kernel-filter.assets/image-20200812191240724.png)


Routine

```python
# Nuclear filtering
#
# This example demonstrates nuclear filtering.
import sensor, image, time

sensor.reset() # Initialize the sensor
#Set the image color format, there are RGB565 color map and GRAYSCALE grayscale
sensor.set_pixformat(sensor.GRAYSCALE) # or sensor.RGB565
#Set image pixel size
sensor.set_framesize(sensor.QVGA) # or sensor.QQVGA (or others)
sensor.skip_frames(time = 2000) # Let the new settings take effect
clock = time.clock() # Track FPS frame rate

kernel_size = 1 # 3x3==1, 5x5==2, 7x7==3, etc.

kernel = [-2, -1, 0, \
          -1, 1, 1, \
           0, 1, 2]

while(True):
    clock.tick() # Track the number of milliseconds that have passed between two snapshots().
    img = sensor.snapshot() # Take a picture and return the image

    # Run the kernel on every pixel of the image.
    # Run the kernel on each pixel of the image
    img.morph(kernel_size, kernel)

    print(clock.fps()) # Note: When connected to a computer, the frame rate will become half the speed. When the computer is not connected, the frame rate will increase.
```
