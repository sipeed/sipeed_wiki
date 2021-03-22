---
title: lcd (screen display)
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: lcd (screen display)
---




## Function

### lcd.init(type=1, freq=15000000, color=lcd.BLACK, invert = 0, lcd_type = 0)

Initialize the `LCD` screen display

#### Parameters

* `type`: Type of device (reserved for future use):
  * `0`: None
  * `1`: lcd shield (default value)
  * `2`: Maix Cube
  * `5`: sipeed rgb screen adapter board
> type is a key-value parameter, which must be explicitly called by writing type= in the function call

* `freq`: the frequency of `LCD` (actually refers to the communication rate of `SPI`)

* `color`: The color initialized by `LCD`, which can be a 16-bit `RGB565` color value, such as `0xFFFF`; or a `RGB888` tuple, such as `(236, 36, 36)`, which defaults to `lcd. BLACK`

* `invert`: `LCD` inverted color display

* `lcd_type`: lcd type:
  * `0`: default type
  * `1`: LCD_TYPE_ILI9486
  * `2`: LCD_TYPE_ILI9481
  * `3`: LCD_TYPE_5P0_7P0, a 5-inch or 7-inch LCD with a resolution of 800 * 480 (requires a sipeed adapter board)
  * `4`: LCD_TYPE_5P0_IPS, 5-inch IPS LCD with a resolution of 854*489 (requires sipeed adapter board)
  * `5`: LCD_TYPE_480_272_4P3, 4.3-inch LCD with a resolution of 480*272 (sipeed adapter board required)

> MaixCube and MaixAmigo need to configure the power chip before using the LCD, otherwise the screen will be blurred. In this step, the MaixPy firmware will be configured automatically, no manual operation is required, the user only needs to understand.

### lcd.deinit()

Log off the `LCD` driver and release the I/O pins

### lcd.width()

Returns the width of `LCD` (horizontal resolution)


### lcd.height()

Returns the height (vertical resolution) of `LCD`.


### lcd.type()

Return the type of `LCD` (reserved for future use):

0: None
1: lcd Shield

### lcd.freq(freq)

Set or get the frequency of `LCD` (SPI)

#### Paremeters

* `freq`: LCD (SPI) frequency

#### Return

LCD frequency


### lcd.set_backlight(state)

Set the backlight status of `LCD`, turning off the backlight will greatly reduce the power consumption of the LCD expansion board

> Not implemented

#### Parameters

* `state`: backlight brightness, value [0,100]

### lcd.get_backlight()

Back to backlight state

#### return value

Backlight brightness, value [0,100]

### lcd.display(image, roi=Auto)

Display an image (GRAYSCALE or RGB565) on the LCD screen.

roi is a rectangular tuple (x, y, w, h) of a region of interest. If not specified, it is the image rectangle

If the roi width is smaller than the lcd width, use a vertical black border to center the roi in the center of the screen (that is, fill the unoccupied area with black).

If the width of roi is greater than the width of lcd, the roi is at the center of the screen, and the mismatched pixels will not be displayed (that is, the LCD screen displays the center of roi in the form of a window).

If the height of roi is less than the height of lcd, use a vertical black border to make roi in the center of the screen (that is, fill the unoccupied area with black).

If the height of roi is greater than the height of lcd, the roi is at the center of the screen, and the mismatched pixels will not be displayed (that is, the LCD screen displays the center of roi in the form of a window).

> roi is a key-value parameter, which must be explicitly called by writing roi= in the function call.

* `oft`: Set the offset coordinate, after setting this coordinate, the surrounding will not be automatically filled


### lcd.clear()

Clear the LCD screen to black or the specified color.

#### Parameters

* `color`: The color initialized by `LCD`, which can be a 16-bit `RGB565` color value, such as `0xFFFF`; or a tuple of `RGB888`, such as `(236, 36, 36)`


### lcd.direction(dir)

It has been abandoned after `v0.3.1`, please use `lcd.rotation` and `lcd.invert` instead, do not use it unless necessary, the interface will still be reserved for debugging

Set the screen orientation, and whether to mirror, etc.

#### Parameters

* `dir`: Under normal circumstances, `lcd.YX_LRUD` and `lcd.YX_RLDU` are recommended, and there are other values, just exchange `XY` or `LR` or `DU`

### lcd.rotation(dir)

Set `LCD` screen orientation

#### Parameters

* `dir`: value range [0,3], rotate clockwise from `0` to `3`

#### return value

Current direction, value [0,3]

### lcd.mirror(invert)

Set whether `LCD` is displayed on mirror

#### Parameters

* `invert`: Whether to display in mirror, `True` or `False`

#### return value

The current setting, whether to display in a mirror, return to `True` or `False`

### lcd.bgr_to_rgb(enable)

Set whether to enable bgr color display

#### Parameters

* `enable`: Whether to enable bgr display, `True` or `False`

### lcd.fill_rectangle(x, y, w, h, color)

Fill a rectangle area on `LCD`

#### Parameters

* `x`: start coordinate `x`
* `x`: starting coordinate `y`
* `w`: padding width
* `h`: Fill height
* `color`: Fill color, which can be a tuple, such as `(255, 255, 255)`, or `RGB565``uint16` value, such as red `0x00F8`

## Routine

### Example 1: Display English

```python
import lcd

lcd.init()
lcd.draw_string(100, 100, "hello maixpy", lcd.RED, lcd.BLACK)

```

### Example 2: Display picture

```python
import lcd
import image

img = image.Image("/sd/pic.bmp")
lcd.display(img)
```

### Example 3: Display English by displaying pictures

```python
import lcd
import image

img = image.Image()
img.draw_string(60, 100, "hello maixpy", scale=2)
lcd.display(img)
```

### Example 4: Display the image captured by the camera in real time

```python
import sensor, lcd

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
sensor.skip_frames()
lcd.init()

while(True):
    lcd.display(sensor.snapshot())
```
