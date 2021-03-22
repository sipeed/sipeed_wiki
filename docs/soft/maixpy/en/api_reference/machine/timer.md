---
title: machine.Timer
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: machine.Timer
---


The hardware timer can be used to trigger tasks or process tasks regularly. After the set time is up, an interrupt can be triggered (call the callback function), and the accuracy is higher than the software timer.
It should be noted that timers may behave differently in different hardware. MicroPython's Timer class defines the basic operation of executing a callback within a given time period (or executing a callback after a delay), and allows more non-standard behaviors to be defined on specific hardware (so it cannot be ported to other boards).

There are 3 timers, each timer has 4 channels available

## Constructor

```python
tim = machine.Timer(id, channel, mode=Timer.MODE_ONE_SHOT, period=1000, unit=Timer.UNIT_MS, callback=None, arg=None, start=True, priority=1, div=0)
```

Create a new Timer object with the specified parameters

### Parameters

* `id`: Timer ID, [0~2] \(Timer.TIMER0~TIMER2\)
* `channel`: Timer channel, [Timer.CHANNEL0~Timer.CHANNEL3]
* `mode`: Timer mode, `MODE_ONE_SHOT` or `MODE_PERIODIC` or `MODE_PWM`
* `period`: Timer period, after starting the timer `period` time, the callback function will be called, (0,~)
* `unit`: Set the unit of the period, the default bit is milliseconds (`ms`), `Timer.UNIT_S` or `Timer.UNIT_MS` or `Timer.UNIT_US` or `Timer.UNIT_NS`
* `callback`: Timer callback function, defines two parameters, one is the timer object `Timer`, the second is the parameter `arg` that you want to pass in the definition object, please see the explanation of `arg` parameters for more
> Note: The callback function is called in the interrupt, so please don't take too long in the callback function and do dynamic allocation switch interrupt etc.
* `arg`: The parameter that you want to pass to the callback function as the second parameter of the callback function
* `start`: Whether to start the timer immediately after the object is successfully constructed, `True`: start immediately, `False`: not start immediately, you need to call the `start()` function to start the timer
* `priority`: hardware timer interrupt priority, related to a specific CPU, in K210, the value range is [1,7], the smaller the value, the higher the priority
* `div`: hardware timer divider, value range [0,255], default is 0, clk_timer (timer clock frequency) = clk_pll0 (phase-locked loop 0 frequency)/2^(div+1)
> clk_timer*period(unit:s) should be <2^32 and >=1


## Method

### init

Similar constructor

```python
tim.init(id, channel, mode=Timer.MODE_ONE_SHOT, period=1000, unit=Timer.UNIT_MS, callback=None, arg=None, start=True, priority=1, div=0)
```

#### Parameters

Similar constructor

#### return value

no


### callback_arg

Get the set parameters passed to the callback function, which can only be called by the `Timer` object, the class `Timer` cannot be called


### callback

Get or set callback function

```python
tim.callback(callback)
```

#### Parameters

* `callback`: the set callback function, optional parameters, if no parameters are passed, only the previous callback function will be returned

#### return value

Current callback function

#### Examples

```python
def on_timer(timer):
    print("time up:",timer)
    print("param:",timer.callback_arg())

tim.callback(on_timer)
print(on_timer, tim.callback())
```

### period

Get or set the timing period

```python
tim.period(period)
```

#### Parameters

* `period`: Optional parameter, configure the period, if no parameter is passed, only the current period value will be returned

#### return value

Current period value

#### Examples

```python
tim.period(2000)
print( tim.period())
```

### start

Start timer

```python
tim.start()
```

#### Parameters

no

#### return value

no

#### Examples

```python
tim.start()
```

### stop

Stop timer

```python
tim.stop()
```

#### Parameters

no

#### return value

no

### restart

Restart timer

```python
tim.restart()
```

#### Parameters

no

#### return value

no

### deinit/\__del\__

Log off the timer, log off the hardware occupation, turn off the hardware clock

```python
tim.deinit()
```

#### Parameters

no

#### return value

no

#### Examples

```python
tim.deinit()
```
or
```python
del tim
```

## Constant

* `TIMER0`: Timer0 id
* `TIMER1`: Timer1 id
* `TIMER2`: Timer2 id
* `CHANNEL0`: Timer channel 0
* `CHANNEL1`: Timer channel 1
* `CHANNEL2`: Timer channel 2
* `CHANNEL3`: Timer channel 3
* `MODE_ONE_SHOT`: Timer runs only once (callback once)
* `MODE_PERIODIC`: Timer always runs (continuous callback)
* `MODE_PWM`: The timer is not used as a callback function to generate PWM
* `UNIT_S`: unit of second (s)
* `UNIT_MS`: unit milliseconds (ms)
* `UNIT_US`: unit microsecond (us)
* `UNIT_NS`: unit nanosecond (ns)


## Routine

### Routine 1

Print information after 3 seconds

```python
from machine import Timer

def on_timer(timer):
    print("time up:",timer)
    print("param:",timer.callback_arg())

tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_ONE_SHOT, period=3000, callback=on_timer, arg=on_timer)
print("period:",tim.period())
```

### Routine 2

Print messages every 1 second, stop for 5 seconds and restart again, turn off and log off the timer after 5 seconds

```python
import time
from machine import Timer

def on_timer(timer):
    print("time up:",timer)
    print("param:",timer.callback_arg())

tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PERIODIC, period=1, unit=Timer.UNIT_S, callback=on_timer, arg=on_timer, start=False, priority=1, div=0)
print("period:",tim.period())
tim.start()
time.sleep(5)
tim.stop()
time.sleep(5)
tim.restart()
time.sleep(5)
tim.stop()
del tim
```
