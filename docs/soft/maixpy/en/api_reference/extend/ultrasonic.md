---
title: modules.ultrasonic (ultrasonic ranging module)
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy doc: modules.ultrasonic (ultrasonic ranging module)
---


Grove-Ultrasonic Ranger (ultrasonic ranging module), only a single data cable is required

<div class="grove_pic">
<img src="./../../../assets/hardware/module_grove/ultrasonic.jpg">
</div>


## Construction method ultrasonic(gpiohs)

### Parameters

* `gpiohs`: gpiohs number, you need to use `fm` to register the pin first, for example

```python
from fpioa_manager import *
from modules import ultrasonic

fm.register(board_info.D[6], fm.fpioa.GPIOHS0, force = True)
device = ultrasonic(fm.fpioa.GPIOHS0)
```

### return value

Return object

## Method measure(unit, timeout)

### Parameters

* `unit`: unit, take the value in the following constant
* `timeout`: timeout time, in microseconds (us)

## Constant

### ultrasonic.UNIT_CM

The unit of the returned distance, cm

### ultrasonic.UNIT_INCH

The unit of the returned distance, feet
