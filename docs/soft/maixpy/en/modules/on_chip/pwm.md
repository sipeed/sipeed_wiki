---
title: Use of PWM
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: Use of PWM
---


For details on PWM, please refer to [PWM-API Document](../../api_reference/machine/pwm.md).

## Instructions

* Import PWM and Timer modules from machine

```python
from machine import Timer,PWM
```

* Create Timer and PWM

```python
tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
ch = PWM(tim, freq=500000, duty=50, pin=boad_info.LED_G)
```

* Change the duty cycle, the set pin will output waveforms with different duty cycles

```python
ch.duty(duty)
```

## Example

Control the brightness of LED_G

> `board_info` is related to the board, and different board configurations are different. [Manual configuration](../../api_reference/builtin_py/board_info.md) is required before use.

```python
from machine import Timer,PWM
import time
from board import board_info
from fpioa_manager import fm

tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
ch = PWM(tim, freq=500000, duty=50, pin=boad_info.LED_G)
duty=0
dir = True
while True:
    if dir:
        duty += 10
    else:
        duty -= 10
    if duty>100:
        duty = 100
        dir = False
    elif duty<0:
        duty = 0
        dir = True
    time.sleep(0.05)
    ch.duty(duty)
```
