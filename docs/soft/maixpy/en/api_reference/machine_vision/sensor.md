---
title: sensor (camera)
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: sensor (camera)
---


sensor sensor module (here specifically refers to the camera module), for camera configuration and image capture, etc., used to control the development board camera to complete the camera task.


## Method

### Initialize the monocular camera

Reset and initialize the monocular camera

```python
sensor.reset([, freq=24000000[, set_regs=True[, dual_buff=False]]])
```

#### Parameters

* `freq`: Set the camera clock frequency, the higher the frequency, the higher the frame rate, but the image quality may be worse. The default is `24MHz`, if the camera has colored spots (ov7740), you can adjust it appropriately, such as `20MHz`
* `set_regs`: Allow the program to write camera registers, the default is `True`. If you need to customize the reset sequence, you can set it to `False`, and then use the `sensor.__write_reg(addr, value)` function to customize the write register sequence
* `dual_buff`: The default is `False`. Double buffering is allowed, which will increase the frame rate, but the memory usage will also increase (about 384KiB)
* `choice`: Specify the type of camera to be searched, ov type (1), gc type (2), mt type (3), if this parameter is not passed, all types of cameras will be searched

#### return value

no

### Reset the binocular camera

Reset and initialize the binocular camera

> K210 has only one DVP interface and can only control one Sensor at a time. But we can use the `shudown` method to control the PWDN pin to select a specific Sensor. The remaining operations remain unchanged after the Sensor is specified. See

Routine 2

```python
sensor.binocular_reset()
```

#### Parameters

no

#### return value

no

### Set frame size

Used to set the output frame size of the camera, k210 supports the maximum VGA format, and the image cannot be obtained if it is larger than VGA

> The screen configured on the MaixPy development board is 320*240 resolution, and it is recommended to set it to QVGA format

```
sensor.set_framesize(framesize[, set_regs=True])
```

#### Parameters

* `framesize`: frame size
* `set_regs`: Allow the program to write camera registers, the default is `True`. If you need to customize the sequence of setting the frame size, you can set it to `False`, and then use the `sensor.__write_reg(addr, value)` function to customize the write register sequence

#### return value

* `True`: set successfully
* `False`: setting error

### Set frame format

Used to set the camera output format

> The screen configured on the MaixPy development board uses RGB565, and it is recommended to set it to RGB565 format

```
sensor.set_pixformat(format[, set_regs=True])
```
#### Parameters

* `format`: Frame format
* `set_regs`: Allow the program to write camera registers, the default is `True`. If you need to customize the sequence of setting the pixel format, you can set it to `False`, and then use the `sensor.__write_reg(addr, value)` function to customize the write register sequence

> Available frame formats are `GRAYSCALE`, `RGB565`, `YUV422`

#### return value

* `True`: set successfully
* `False`: setting error

### Image capture control

Image capture function control

```
sensor.run(enable)
```
#### Parameters

* `enable`: 1 means start capturing images 0 means stop capturing images

#### return value

* `True`: set successfully
* `False`: setting error


### Take an image

Take a picture with the camera

```
sensor.snapshot()
```
#### Parameters

no

#### return value

* `img`: The returned image object

### Camera control

Turn off the camera / switch camera

```
sensor.shutdown(enable/select)
```
#### Parameters

Monocular camera
* `enable`: True means to turn on the camera False means to turn off the camera

Binocular camera
* `select`: switch camera by writing 0 or 1

#### return value

no

### Frame skip

Skip the specified number of frames or skip the image within the specified time, so that the camera image is stable after changing the camera settings

```
sensor.skip_frames(n, [, time])
```
#### Parameters

* `n`: skip n frames of images

* `time`: skip the specified time, the unit is ms

> If n and time are not specified, the method skips 300 milliseconds of frames; if both are specified, the method skips n number of frames, but will return after time milliseconds

#### return value

no

### Resolution width

Get the camera resolution width

```
sensor.width()
```
#### Parameters

no

#### return value

* `int` type of camera resolution width



### Resolution height

Get the camera resolution height

```
sensor.height()
```
#### Parameters

no

#### return value

* `int` type of camera resolution height

### Get frame buffer

Get the current frame buffer

```
sensor.get_fb()
```
#### Parameters

no

#### return value

* Objects of type `image`

### Get ID

Get the current camera ID

```
sensor.get_id()
```
#### Parameters

no

#### return value

* ID of type `int`

### Set the color bar test mode

Set the camera to the color bar test mode

> After the color bar test mode is turned on, the camera will output a color bar image, which is often used to check whether the camera bus is connected correctly.
```
sensor.set_colorbar(enable)
```
#### Parameters

* `enable`: 1 means turn on the color bar test mode 0 means turn off the color bar test mode

#### return value

no

### Set contrast

Set camera contrast

```
sensor.set_contrast(contrast)
```
#### Parameters

* `constrast`: camera contrast, the range is [-2,+2]

#### return value

* `True`: set successfully
* `False`: setting error

### Set brightness

Set camera brightness

```
sensor.set_brightness(brightness)
```
#### Parameters

* `brightness`: Camera brightness, range [-2,+2]

####  return value

* `True`: set successfully
* `False`: setting error

### Set saturation

Set camera saturation

```
sensor.set_saturation(saturation)
```
#### Parameters

* `constrast`: camera saturation, the range is [-2,+2]

#### return value

* `True`: set successfully
* `False`: setting error

### Set automatic gain

Set camera auto gain mode

```
sensor.set_auto_gain(enable,gain_db)
```

#### Parameters

* `enable`: 1 means turn on auto gain 0 means turn off auto gain
* `gain_db`: When auto gain is turned off, the set camera fixed gain value, the unit is dB

> If you need to track the color, you need to turn off the automatic gain


#### return value

no

### Get the gain value

Get the camera gain value

```
sensor.get_gain_db()
```

#### Parameters

no

#### return value

* `float` type gain value

### Set horizontal mirroring

Set camera horizontal mirroring

```
sensor.set_hmirror(enable)
```

#### Parameters

* `enable`: 1 means enable horizontal mirroring 0 means turn off horizontal mirroring

#### return value

no
### Set the camera to flip vertically

Set the camera to flip vertically

```
sensor.set_vflip(enable)
```

#### Parameters

* `enable`: 1 means turn on vertical flip 0 means turn off vertical flip

#### return value

no

### Write register

Write the specified value to the camera register

```
sensor.__write_reg(address, value)
```

#### Parameters

* `address`: register address
* `value`: write value

#### return value

no

> Please refer to the camera data sheet for details

### Read register

Read camera register value

```
sensor.__read_reg(address)
```

#### Parameters

* `address`: register address

#### return value

* `int` type of register value

> Please refer to the camera data sheet for details

### set_jb_quality

Set the quality of the image transmitted to the IDE

```
sensor.set_jb_quality(quality)
```

#### Parameters

`quality`: `int` type, image quality percentage (0~100), the larger the number, the better the quality

## Routine


### Routine 1

```python
# Monocular camera

import sensor
import lcd

lcd.init()

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

while True:
    img = sensor.snapshot()
    lcd.display(img)
```

### Routine 2

```python
# Binocular camera

import sensor
import image
import lcd
import time

lcd.init()

sensor.binocular_reset()
sensor.shutdown(0) # Select sensor 0
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)

sensor.shutdown(1) # Select sensor 1
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

while True:
    sensor.shutdown(0) # Select sensor 0
    img = sensor.snapshot()
    lcd.display(img)
    time.sleep_ms(100)

    sensor.shutdown(1) # Select sensor 1
    img = sensor.snapshot()
    lcd.display(img)
    time.sleep_ms(100)
```
