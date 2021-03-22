---
title: get image
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: get image
---


You can get images from the camera, you can read picture files from the file system, or you can get pictures from the network

## Get from camera


This part has been mentioned in the previous tutorial

```
import sensor, lcd

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
sensor.skip_frames()

img = sensor.snapshot()
print(img)
```

* `import sensor`: first import the built-in `sensor` (camera) library
* `sensor.reset()`: Initialize the camera. If it fails, check the hardware
* `sensor.set_pixformat(sensor.RGB565)`: Set the camera to `RGB565` format, the default is to use `RGB565`
* `sensor.set_framesize(sensor.QVGA)`: The resolution is `QVGA`, that is, `320x240`
* `sensor.run(1)`: start to run, it is not necessary to call it in the current version, the camera will automatically start to run after the above settings are completed
* `sensor.skip_frames()`: The image quality is not stable when the camera is just started, so some images are skipped
* `sensor.snapshot()`: fetch a frame of image data from the camera, the return value is an image object

In addition to the above functions, you may also need to set the image to mirror (`hmirror`), such as the front camera; or flip up and down (`vflip`), and white balance, etc., see [sensor module API manual](/ api_reference/machine_vision/sensor.md)


## Read from file

```python
import image

img = image.Image("/sd/test.jpg")
print(img)
```

Of course you can also save the picture to the file system`
```python
img.save("/sd/test2.jpg", quality=95)
```


## Read from memory (or read from network)

You can read the file to the memory first, depending on your application where you read it from, such as network, or serial port SPI, etc.
Construct a `bytes` object

```python
import image

jpeg_buff = b'\xFF' # jpeg buffer
img = image.Image(jpeg_buff, from_bytes = True)
print(img)
```

## Create a blank image directly

```python
import image

img = image.Image(size=(320, 240))
```

This picture is a black blank image
