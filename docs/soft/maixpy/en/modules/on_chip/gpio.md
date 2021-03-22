---
title: Use of GPIO
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy doc: use of GPIO
---

For detailed introduction of GPIO, please refer to [GPIO-API Document](../../api_reference//Maix/gpio.md).

## Instructions

* Register an IO as a GPIO function

```python
from Maix import GPIO
from fpioa_manager import fm

fm.register(io_number,fm.fpioa.GPIO0)
```

* Set GPIO as input or output mode

```python
gpio=GPIO(GPIO.GPIO0,GPIO.OUT)
```

* Read or set GPIO level

```python
gpio.value(1)
```

## Example

Turn on the LED

> `board_info` is related to the board, and different board configurations are different. [Manual configuration](../../api_reference/builtin_py/board_info.md) is required before use.

```python
import utime
from Maix import GPIO
from board import board_info
from fpioa_manager import fm

fm.register(board_info.LED_R,fm.fpioa.GPIO0)
led_r=GPIO(GPIO.GPIO0,GPIO.OUT)
utime.sleep_ms(500)
led_r.value(0)
fm.unregister(board_info.LED_R)
```
