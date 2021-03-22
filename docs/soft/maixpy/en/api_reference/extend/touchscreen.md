---
title: touchscreen (touch screen)
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: touchscreen (touch screen)
---


The `touchscreen` module contains basic reading touch screen operations

Currently supported touch screens:

* ns2009 (default)

If you need to modify the driver model, you need to recompile the `MaixPy` source code to modify the pre-compiled supported model



## Global functions

### init(i2c=None, cal=None)

Initialize the touch screen

> API may be changed later (mainly for changes to parameters of multiple drivers)

#### Parameters

* `i2c`: Currently supports the touch screen of `I2C` communication. Pass in the `I2C` instance object, this parameter may be renamed or cancelled later
* `cal`: Calibration data, a tuple of `7` integer values, which can be obtained by the `touchscreen.calibrate()` function

### calibrate()

Calibrate the screen so that the screen display and touch screen pixels can correspond

#### return value

Return a tuple of `7` integer values, which can be saved to the file system or `flash` and passed in during initialization, so that there is no need to calibrate every time

### read()

Read the current screen state and the coordinate value of the pressed point

#### return value

A tuple `(status, x, y)` composed of `3` integer values, note that this value will always keep the previous state

* `status`: status, the values ​​are `touchscreen.STATUS_PRESS`, `touchscreen.STATUS_MOVE`, `touchscreen.STATUS_RELEASE`
* `x`: `x` axis coordinate
* `y`: `y` axis coordinate


## Constant

### touchscreen.STATUS_PRESS

The screen is pressed, the first value of the tuple returned by the `read()` function

### touchscreen.STATUS_MOVE

The screen is pressed and moved, that is, press to move, the first value of the tuple returned by the `read()` function

### touchscreen.STATUS_RELEASE

The screen is no longer held down, that is, there is no click, the first value of the tuple returned by the `read()` function



## Routine

## Routine 1: Drawing board

Black background and white pen drawing board, use the `boot` button to clear the content

> Cancel the comment of `ts.calibrate()` to start the touch screen calibration program

> `board_info` is related to the board, and different board configurations are different. [Manual configuration](../builtin_py/board_info.md) is required before use.

```python
import touchscreen as ts
from machine import I2C
import lcd, image
from board import board_info
from fpioa_manager import *

board_info=board_info()

fm.register(board_info.BOOT_KEY, fm.fpioa.GPIO1)
btn_clear = GPIO(GPIO.GPIO1, GPIO.IN)

lcd.init()
i2c = I2C(I2C.I2C0, freq=400000, scl=30, sda=31)
ts.init(i2c)
#ts.calibrate()
lcd.clear()
img = image.Image()
status_last = ts.STATUS_IDLE
x_last = 0
y_last = 0
draw = False
while True:
    (status,x,y) = ts.read()
    print(status, x, y)
    if draw:
        img.draw_line((x_last, y_last, x, y))
    if status_last!=status:
        if (status==ts.STATUS_PRESS or status == ts.STATUS_MOVE):
            draw = True
        else:
            draw = False
        status_last = status
    lcd.display(img)
    x_last = x
    y_last = y
    if btn_clear.value() == 0:
        img.clear()
ts.__del__()
```
