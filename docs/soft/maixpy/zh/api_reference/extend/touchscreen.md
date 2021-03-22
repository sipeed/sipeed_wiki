---
title: touchscreen（触摸屏幕）
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: touchscreen（触摸屏幕）
---


`touchscreen` 模块包含了基本的读取触摸屏幕操作

目前支持的触摸屏幕：

* ns2009（默认）

如果需要修改驱动型号，需要重新编译 `MaixPy` 源码修改预编译支持的型号



## 全局函数

### init(i2c=None, cal=None)

初始化触摸屏

> API 在后面可能会有所改动（主要是针对多种驱动对参数的改动）

#### 参数

* `i2c`： 目前支持的是 `I2C` 通信的触摸屏， 传入`I2C`实例对象， 后期这个参数可能会被重命名或者取消
* `cal`： 校准数据， 是一个 `7` 个整型值的元组， 可以通过 `touchscreen.calibrate()` 函数得到

### calibrate()

校准屏幕，使屏幕显示和触摸屏像素能够对应

#### 返回值

返回一个 `7` 个整型值的元组， 可以保存到文件系统或者`flash`，在初始化的时候传入，这样就不用每次都校准了

### read()

读取当前屏幕的状态以及按下的点的坐标值

#### 返回值

一个由 `3` 个整型值组成的元组 `(status, x, y)`， 注意这个值会一直保持上一个状态

* `status`： 状态， 取值有 `touchscreen.STATUS_PRESS`， `touchscreen.STATUS_MOVE`， `touchscreen.STATUS_RELEASE`
* `x`：  `x` 轴坐标
* `y`：  `y` 轴坐标


## 常量

### touchscreen.STATUS_PRESS

屏幕被按下， `read()` 函数返回的元组的第一个值

### touchscreen.STATUS_MOVE

屏幕被按住并移动，即按住移动， `read()` 函数返回的元组的第一个值

### touchscreen.STATUS_RELEASE

屏幕不再被按住，即没有点击， `read()` 函数返回的元组的第一个值



## 例程

## 例程 1 ： 图画板

黑底白画笔画图板， 使用`boot` 按键可以清除内容

> 取消 `ts.calibrate()` 的注释可以在开始运行触摸屏校准程序

> `board_info` 与板卡相关，不同板卡配置不同，使用前需要[手动配置](../builtin_py/board_info.md)。

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

