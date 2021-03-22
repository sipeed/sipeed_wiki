---
title: machine.PWM
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: machine.PWM
---


PWM: Pulse width modulation module, PWM supported by hardware, you can specify any pin (0 to 47 pins)

Each PWM depends on a timer, that is, when the timer is bound with the PWM function, it cannot be used as a normal timer. Because there are 3 timers, each timer has 4 channels, that is, a maximum of 12 PWM waveforms can be generated simultaneously

## Constructor

```python
pwm = machine.PWM(tim, freq, duty, pin, enable=True)
```

Create a new PWM object with specified parameters

### Parameters

* `tim`: Each PWM relies on a timer to generate waveforms, so a timer object needs to be passed here. The timer ID and channel number must be specified when the timer object is initialized
* `freq`: PWM waveform frequency
* `duty`: PWM duty cycle, refers to the percentage of the high level in the entire cycle, value: [0,100]
* `[pin]`: PWM output pin. It is not necessary to set, but use [fm](../builtin_py/fm.md) to manage pin mapping in a unified manner.
* `enable`: Whether to start generating the waveform immediately, the default bit is `True`, and the PWM waveform will be generated on the specified pin immediately after the object is generated

## Method

### init

Similar constructor

```python
pwm.init(tim, freq, duty, pin, enable=True)
```

#### Parameters

Same as constructor

#### return value

no


### freq

Get or set PWM frequency

```python
pwm.freq(freq)
```

#### Parameters

* `freq`: PWM frequency, optional parameter, if no parameter is passed, the step setting will only return the current frequency value

#### return value

Actual PWM frequency currently set


### duty

Get or set the PWM duty cycle

```python
pwm.duty(duty)
```

#### Parameters

* `duty`: PWM duty cycle is optional, if no parameter is passed, the step setting will only return the current duty cycle value

#### return value

The currently set PWM duty cycle value


### enable

Enable PWM output to generate waveform on the specified pin immediately

```python
pwm.enable()
```

#### Parameters

no

#### return value

no

### disable

Disabled PWM output, the specified pin no longer generates waveform

```python
pwm.disable()
```

#### Parameters

no

#### return value

no

### deinit/\__del\__

Log off the PWM hardware, release the occupied resources, and turn off the PWM clock

```python
pwm.deinit()
```

#### Parameters

no

#### return value

no

#### Examples

```python
pwm.deinit()
```
or
```python
del pwm
```

## Constant

no


## Routine


### Routine 1 (breathing light)

> `board_info` is related to the board, and different board configurations are different. [Manual configuration](../builtin_py/board_info.md) is required before use.

```python
from machine import Timer,PWM
import time
from board import board_info

tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
ch = PWM(tim, freq=500000, duty=50, pin=board_info.LED_G)
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

### Routine 2

> `board_info` is related to the board, and different board configurations are different. [Manual configuration](../builtin_py/board_info.md) is required before use.

```python
import time
import machine
from board import board_info

tim = machine.Timer(machine.Timer.TIMER0, machine.Timer.CHANNEL0, mode=machine.Timer.MODE_PWM)
ch0 = machine.PWM(tim, freq=3000000, duty=20, pin=board_info.LED_G, enable=False)
ch0.enable()
time.sleep(3)
ch0.freq(2000000)
print("freq:",ch0.freq())
ch0.duty(60)
time.sleep(3)
ch0.disable()
```
