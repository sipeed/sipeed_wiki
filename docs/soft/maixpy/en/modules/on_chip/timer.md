---
title: Use of Timer
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: the use of Timer (timer)
---


For detailed introduction of Timer, please refer to [Timer-API Document](../../api_reference/machine/timer.md).

## Instructions

* Import Timer module from machine

```python
from machine import Timer
```

* Create a Timer object

```python
def on_timer(timer):
    print("time up:",timer)
    print("param:",timer.callback_arg())

tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PERIODIC, period=1, unit=Timer.UNIT_S, callback=on_timer, arg=on_timer, start=False, priority=1, div=0)
```

* Start the timer, at this time the timer will execute the callback function regularly

```python
tim.start()
```

* Stop the timer

```python
tim.stop()
```

## Example

Execute callback function regularly

```python
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
