---
title: Sensor
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: Sensor
---


The sensor module is used to set the parameters of the photosensitive element.

Use routine:

-Real-time preview camera

    ```python
    import sensor #Introduction of the photosensitive element module
    sensor.reset()#Initialize the photosensitive element
    sensor.set_pixformat(sensor.RGB565)#Set to color
    sensor.set_framesize(sensor.QVGA)#Set the size of the image
    sensor.skip_frames()#Skip n photos, after changing the settings, skip some frames and wait for the photosensitive element to stabilize.

    while(True):
        img = sensor.snapshot()#take a photo, img is an image object
    ```

-Initialization

    ```python
    sensor.reset()# Initialize the photosensitive element
    #Set color/black and white
    sensor.set_pixformat()# Set the pixel mode.
    sensor.GRAYSCALE# Grayscale, 8bit per pixel.
    sensor.RGB565# Color, 16bit per pixel.
    ```

-Set image size


    sensor.QQCIF# 88x72
    sensor.QCIF# 176x144
    sensor.CIF# 352x288
    sensor.QQSIF# 88x60
    sensor.QSIF# 176x120
    sensor.SIF# 352x240
    sensor.QQQQVGA# 40x30
    sensor.QQQVGA# 80x60
    sensor.QQVGA# 160x120
    sensor.QVGA# 320x240
    sensor.VGA# 640x480

    ```python
    sensor.set_framesize()# Set the size of the image
    ```

-Skip some frames

sensor.skip_frames(n=10) Skip n photos, after changing the settings, skip some frames and wait for the sensor to stabilize.

-Get an image

sensor.snapshot() takes a picture and returns an image object.

-Auto gain / white balance / exposure

sensor.set_auto_gain() Automatic gain is turned on (True) or turned off (False).

When using color tracking, you need to turn off automatic gain.

sensor.set_auto_whitebal() Automatic white balance is turned on (True) or turned off (False).

When using color tracking, you need to turn off the automatic white balance.

sensor.set_auto_exposure(enable[\, exposure_us])

enable Turn on (True) or turn off (False) automatic exposure. Open by default.

If enable is False, you can use exposure_us to set a fixed exposure time (in microseconds).

-Set window ROI

```python
sensor.set_windowing(roi)
```

ROI: Region Of Interest, the term "region of interest" in image processing. It is the area to be processed extracted from the image to be processed.

```python
sensor.set_framesize(sensor.VGA) # high resolution
sensor.set_windowing((240, 240)) #Take the 240*240 area in the middle
```

The format of roi is (x, y, w, h).


-Set flip

```python
#Horizontal flip
sensor.set_hmirror(True)
# Flip vertically
sensor.set_vflip(True)
```
