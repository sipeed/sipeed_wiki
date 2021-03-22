---
title: NES 游戏模拟器
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: NES 游戏模拟器
---


经典的 FC 红白机 游戏模拟器， 带我们回到小时候吧～～

**警告，该模块只在标准固件（> 2m）中被编译包含，其他固件不带有，如有需求，请重新编译固件。**

## 函数

### init(rc_type=nes.KEYBOARD, cs, mosi, miso, clk, repeat=16, vol=5)

初始化 `NES` 模拟器

#### 参数

* `tc_type`： 遥控器类型， 键盘（`nes.KEYBOARD`）（注意是串口与电脑通信，而不是直接接USB键盘到开发板）或者手柄（`nes.JOYSTICK`）。 
> 建议使用`PS2`手柄，体验会更好， 键盘通过串口工具输入可能不能同时按多个按键，当然也可以通过自己在PC写一个脚本来转发键值就能解决（去[这里](https://github.com/sipeed/MaixPy_scripts/tree/master/multimedia/nes)找找？）

* `cs`： 如果使用 `SPI` 接口的 `PS2` 手柄， 传入 `cs` 外设编号（注意不是引脚号，需要先映射引脚）
* `mosi`： 如果使用 `SPI` 接口的 `PS2` 手柄， 传入 `mosi` 外设编号（注意不是引脚号，需要先映射引脚）
* `miso`： 如果使用 `SPI` 接口的 `PS2` 手柄， 传入 `miso` 外设编号（注意不是引脚号，需要先映射引脚）
* `clk`： 如果使用 `SPI` 接口的 `PS2` 手柄， 传入 `clk` 外设编号（注意不是引脚号，需要先映射引脚）
* `repeat`： 这个参数只对使用键盘（/串口）时， 指按键的重复率
* `vol`： 初始化时的音量， 后面可以通过按键调整

### 基础示例

运行 `NES` 游戏 `ROM`

#### 参数

* `nes`： 游戏 `ROM` 路径， 比如 `/sd/mario.nes`

```python
try:
  nes.init(nes.INPUT)
  nes.load("/sd/mario.nes")
  while True:
    nes.loop()
finally:
  nes.free()
```

## 快捷键


### 代码输入

* `nes.input` ： `(①号机手柄, ②号机手柄, 菜单功能)`

### 键盘（/串口）

* `移动` ： `W A S D`
* `A` ： `J`
* `B` ： `K`
* `start` ： `M` 或者 `Enter`
* `option`： `N` 或者 `\`
* `退出` ： `ESC`
* `音量 -` ： `-`
* `音量 +` ： `=`
* `运行速度 -` ： `R`
* `运行速度 +` ： `F`

### 手柄

* `移动` ： 方向键 `<-` `^` `V` `->`
* `A` ： `□`
* `B` ： `×`
* `start` ： `START`
* `select`： `SELECT`
* `退出` ： 暂无
* `音量 -` ： `R2`
* `音量 +` ： `R1`
* `运行速度 -` ： `L1`
* `运行速度 +` ： `L2`

## 例程

> "mario.nes" 游戏文件请自行搜索下载

## 例 0： 代码输入

> 2021年01月28日：现在建议使用 Maix handle （I2C 设备）进行游玩，如下代码注释 `nes.input(p1, p2, 0)` 表示输入两个手柄的数据。

```python
import nes, lcd
lcd.init(freq=15000000)
try:
  nes.init(nes.INPUT)
  nes.load("mario.nes")
  while True:
    # p1 = i2c.readfrom(66, 1) # handle i2c addr
    # p2 = i2c.readfrom(74, 1) # handle i2c addr
    # nes.input(p1, p2, 0)
    nes.loop()
finally:
  nes.free()

```

## 例 1： 键盘（串口）

```python
import nes, lcd

lcd.init(freq=15000000)
nes.init(nes.KEYBOARD)
nes.load("/sd/mario.nes")

while True:
    nes.loop()
    
```

## 例 2： PS2 手柄

```python
import nes, lcd
from fpioa_manager import fm

fm.register(19, fm.fpioa.GPIOHS19)
fm.register(18, fm.fpioa.GPIOHS18)
fm.register(23, fm.fpioa.GPIOHS23)
fm.register(21, fm.fpioa.GPIOHS21)

lcd.init(freq=15000000)
nes.init(nes.JOYSTICK, cs=fm.fpioa.GPIOHS19, clk=fm.fpioa.GPIOHS18, mosi=fm.fpioa.GPIOHS23, miso=fm.fpioa.GPIOHS21)
nes.load("/sd/mario.nes")

while True:
    nes.loop()

```





