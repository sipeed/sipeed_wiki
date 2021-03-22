---
title: Use of WDT (Watchdog)
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: the use of WDT (watchdog)
---


For detailed introduction of WDT, please refer to [WDT API Document](../../api_reference/machine/wdt.md).

## Instructions

The watchdog is mainly used to protect the normal operation of the system. The principle of action is that after the watchdog is started, a dog feeding operation must be executed regularly in the program. When the system is disturbed and cannot operate normally, the dog feeding operation cannot be executed regularly. At this time, the watchdog will generate an internal reset, allowing the system to restart.

* Import WDT module from machine

```python
from machine import WDT
```

* Define the callback function and create the WDT object

```python
def on_wdt(self):
    print(self.context(), self)
    #self.feed()
    ## release WDT
    #self.stop()

# test callback wdt
wdt1 = WDT(id=1, timeout=4000, callback=on_wdt, context={})
```

* Feed the dog

```python
wdt1.feed()
```

*Dog feeding operation can be performed in the callback function*

* Turn off watchdog

```python
wdt1.stop()
```

## Example

1. Close after feeding the dog once
2. Do not feed the dog to reset the system

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
wdt0.stop()
print('stop', wdt0)
# 3.wait wdt work
#while True:
    #print('idle', time.ticks_ms())
    #time.sleep(1)
#'''

#'''
def on_wdt(self):
    print(self.context(), self)
    #self.feed()
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
wdt1.stop()
print('stop', wdt1)
# 3.wait wdt work
#while True:
    #print('idle', time.ticks_ms())
    #time.sleep(1)
#'''

#'''
## test default and callback wdt
def on_wdt(self):
    print(self.context(), self)
    #self.feed()
    ## release WDT
    #self.stop()

wdt0 = WDT(id=0, timeout=3000, callback=on_wdt, context=[])
wdt1 = WDT(id=1, timeout=4000, callback=on_wdt, context={})
## 3.wait wdt work
while True:
    #wdt0.feed()
    print('idle', time.ticks_ms())
    time.sleep(1)
#'''

'''output
into [MAIXPY]WDT:(800cc560; id=0, timeout=3000, callback=800abcf8, context=800abcf8)
550247
552247
stop [MAIXPY]WDT:(800cc560; id=0, timeout=3000, callback=800abcf8, context=800abcf8)
into [MAIXPY]WDT:(800cc5e0; id=1, timeout=4000, callback=800cc5a0, context=800cc5c0)
554261
556261
stop [MAIXPY]WDT:(800cc5e0; id=1, timeout=4000, callback=800cc5a0, context=800cc5c0)
idle 556268
idle 557269
idle 558269
[] [MAIXPY]WDT:(800cc680; id=0, timeout=3000, callback=800cc620, context=800cc640)
idle 559275
{} [MAIXPY]WDT:(800cce40; id=1, timeout=4000, callback=800cc620, context=800cc6c0)
idle 560282
idle 561283

[MAIXPY] Pll0:freq:806000000
[MAIXPY] Pll1:freq:398666666
[MAIXPY] Pll2:freq:45066666
[MAIXPY] cpu:freq:403000000
[MAIXPY] kpu:freq:398666666
[MAIXPY] Flash:0xef:0x17
[MaixPy] gc heap=0x800c9850-0x80149850(524288)
[MaixPy] init end

 __ __ _____ __ __ _____ __ __
| \/ | /\ |_ _| \ \ / / | __ \ \ \ / /
| \ / | / \ | | \ V / | |__) | \ \_/ /
| |\/| | / /\ \ | |> <| ___/ \ /
| | | | / ____ \ _| |_ /. \ | | | |
|_| |_| /_/ \_\ |_____| /_/ \_\ |_| |_|

Official Site: https://www.sipeed.com
Wiki: https://maixpy.sipeed.com

MicroPython v0.5.1-174-gf18990aa3-dirty on 2021-01-11; Sipeed_M1 with kendryte-k210
Type "help()" for more information.
'''
```
