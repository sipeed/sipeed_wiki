---
title: First program: Use screen and camera
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: first program: use screen and camera
---


The development board has a matching camera and screen, please check whether the hardware connection is correct before powering on(**Align according to the No. 1 pin marked on the cable**)

Then power on, open the serial terminal, press the keyboard `Ctrl+E`, and paste the following code:

```python
import sensor, lcd

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
sensor.skip_frames()

lcd.init(freq=15000000)

while(True):
    lcd.display(sensor.snapshot())

```
Press the keyboard `Ctrl+D` to start running the code

You will find that the screen is lit, and the picture taken by the camera is displayed

If it displays `reset fail`, the camera is not connected well, or the camera is damaged, or check whether an unsupported camera is used

The meaning of the above programs can be found in the API manual, which can be found in the directory on the left, or you can use the search box in the upper left corner to search.
Now explain the above program:

* `import sensor, lcd`: first import the built-in `sensor` (camera) library and `lcd` (screen) library
* `sensor.reset()`: Initialize the camera. If it fails, check the hardware
* `sensor.set_pixformat(sensor.RGB565)`: Set the camera to `RGB565` format, the default is to use `RGB565`
* `sensor.set_framesize(sensor.QVGA)`: The resolution is `QVGA`, that is, `320x240`
* `sensor.run(1)`: start to run, it is not necessary to call it in the current version, the camera will automatically start to run after the above settings are completed
* `sensor.skip_frames()`: The image quality is not stable when the camera is just started, so some images are skipped
* `lcd.init(freq=15000000)`: Initialize the LCD, here is a parameter called `freq`, frequency, which specifies the clock frequency for driving the LCD, here is `15MHz`, which can be adjusted according to the hardware performance
* `while(True)`: This is a loop, the code inside the loop will be run continuously
* `sensor.snapshot()`: fetch a frame of image data from the camera, the return value is an image object
* `lcd.display()`: display image to LCD
* `lcd.display(sensor.snapshot())`: here is to execute the image acquisition in brackets first, and the return value is directly displayed as a parameter to the LCD
