---
title: machine.WDT
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: machine.WDT
---


MaixPy's WDT watchdog module is used to restart the system when the application crashes and eventually enters an unrecoverable state. Once started, when the hardware is running without regular feeding (feed), it will automatically reset after a timeout.

## Constructor

```python
from machine import WDT
wdt0 = WDT(id=1, timeout=4000, callback=on_wdt, context={})
```

Create a new WDT object with specified parameters

### Parameters

* `id`: When this watchdog object must be initialized, an ID (0 ~ 2) must be specified to distinguish the watchdog used.
* `timeout`: Watchdog timeout time, in milliseconds (ms).
* `callback`: (Optional) A callback function that can be executed after timeout.
* `context`: (Optional) The parameters passed to the callback function.

## Method

### feed

"Feed" the watchdog to prevent it from resetting the system. The app should use the call in the right place and make sure to "feed" the watchdog only after verifying that everything is working properly.

```python
wdt0.feed()
```

#### Parameters

no

#### return value

no

### stop

Stop the current watchdog object

```python
wdt0.stop()
```

#### Parameters

no

#### return value

no

## Routine


### Routine 1 (Basic use)

Feed the dog once and stop feeding the dog to reset the system

```python
import time
from machine import WDT

#'''
# test default wdt
wdt0 = WDT(id=0, timeout=3000)
print('into', wdt0)
time.sleep(2)
print(time.ticks_ms())
# 1.test wdt feed
wdt0.feed()
time.sleep(2)
print(time.ticks_ms())
# 2.test wdt stop
# wdt0.stop()
```

### Routine 2 (advanced use)

Feed the dog in the callback function and the system runs normally

```python
import time
from machine import WDT
def on_wdt(self):
    print(self.context(), self)
    self.feed()
    ## release WDT
    #self.stop()

# test callback wdt
wdt1 = WDT(id=1, timeout=4000, callback=on_wdt, context={})
print('into', wdt1)
time.sleep(2)
print(time.ticks_ms())
# 1.test wdt feed
wdt1.feed()
time.sleep(2)
print(time.ticks_ms())
# 2.test wdt stop
# wdt1.stop()
# print('stop', wdt1)
# 3.wait wdt work
while True:
    print('idle', time.ticks_ms())
    time.sleep(1)
```
