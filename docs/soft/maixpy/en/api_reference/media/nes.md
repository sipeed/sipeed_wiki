---
title: NES game emulator
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: NES game emulator
---


The classic FC red and white game simulator, take us back to our childhood~~

**Warning, this module is only compiled and included in the standard firmware (> 2m), and not included in other firmware. If necessary, please recompile the firmware. **

## Function

### init(rc_type=nes.KEYBOARD, cs, mosi, miso, clk, repeat=16, vol=5)

Initialize the `NES` emulator

#### Parameters

* `tc_type`: remote control type, keyboard (`nes.KEYBOARD`) (note that the serial port communicates with the computer, not directly connecting the USB keyboard to the development board) or handle (`nes.JOYSTICK`).
> It is recommended to use the `PS2` handle, the experience will be better, the keyboard may not be able to press multiple keys at the same time when inputting through the serial tool, of course, you can also write a script on the PC to forward the key value to solve the problem (go [here] (https ://github.com/sipeed/MaixPy_scripts/tree/master/multimedia/nes) Looking for it?)

* `cs`: If you use the `PS2` handle of the `SPI` interface, pass in the `cs` peripheral number (note that it is not a pin number, you need to map the pin first)
* `mosi`: If you use the `PS2` handle of the `SPI` interface, pass in the `mosi` peripheral number (note that it is not a pin number, you need to map the pin first)
* `miso`: If you use the `PS2` handle of the `SPI` interface, pass in the `miso` peripheral number (note that it is not a pin number, you need to map the pin first)
* `clk`: If you use the `PS2` handle of the `SPI` interface, pass in the `clk` peripheral number (note that it is not a pin number, you need to map the pin first)
* `repeat`: This parameter is only used when using the keyboard (/serial port), it refers to the repeat rate of the keys
* `vol`: The volume during initialization, which can be adjusted by pressing the buttons later

### Basic example

Run `NES` game `ROM`

#### Parameters

* `nes`: the path of the game `ROM`, such as `/sd/mario.nes`

```python
try:
  nes.init(nes.INPUT)
  nes.load("/sd/mario.nes")
  while True:
    nes.loop()
finally:
  nes.free()
```

## hot key


### Code input

* `nes.input`: `(①No. handset handle, ②No. handset handle, menu function)`

### Keyboard (/serial port)

* `Move`: `W A S D`
* `A`: `J`
* `B`: `K`
* `start`: `M` or `Enter`
* `option`: `N` or `\`
* `Exit`: `ESC`
* `Volume -`: `-`
* `Volume +`: `=`
* `Running Speed ​​-`: `R`
* `Run speed +`: `F`

### Handle

* `Move`: Arrow keys `<-` `^` `V` `->`
* `A`: `□`
* `B`: `×`
* `start`: `START`
* `select`: `SELECT`
* `Exit`: None
* `Volume -`: `R2`
* `Volume +`: `R1`
* `Run speed -`: `L1`
* `Run speed +`: `L2`

## Routine

> "mario.nes" game file please search and download by yourself

## Example 0: Code input

> January 28, 2021: It is now recommended to use Maix handle (I2C device) to play. The following code comment `nes.input(p1, p2, 0)` means to input the data of two handles.

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

## Example 1: Keyboard (serial port)

```python
import nes, lcd

lcd.init(freq=15000000)
nes.init(nes.KEYBOARD)
nes.load("/sd/mario.nes")

while True:
    nes.loop()
    
```

## Example 2: PS2 handle

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
