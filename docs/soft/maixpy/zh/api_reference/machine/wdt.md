---
title: machine.WDT
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: machine.WDT
---


MaixPy 的 WDT 看门狗模块，用于在应用程序崩溃且最终进入不可恢复状态时重启系统。一旦开始，当硬件运行期间没有定期进行喂狗（feed）就会在超时后自动复位。

## 构造函数

```python
from machine import WDT
wdt0 = WDT(id=1, timeout=4000, callback=on_wdt, context={})
```

通过指定的参数新建一个 WDT 对象

### 参数

* `id`: 这个看门狗对象必须初始化时必须指定 ID （0 ~ 2） 用于区分使用的看门狗。
* `timeout`： 看门狗超时时间，单位为毫秒（ms）。
* `callback`: （可选）可以在超时后执行的回调函数。
* `context`： （可选）为回调函数传递的参数。

## 方法

### feed

“喂养”看门狗，以防止其重置系统。该应用应将该调用用于合适位置，并确保只在验证一切正常运行后才“喂养”看门狗。

```python
wdt0.feed()
```

#### 参数

无

#### 返回值

无

### stop

停止当前看门狗对象

```python
wdt0.stop()
```

#### 参数

无

#### 返回值

无

## 例程


### 例程 1 （基础使用）

喂一次狗后便不再喂狗使得系统复位

```python
import time
from machine import WDT

# '''
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

### 例程 2 （进阶使用）

在回调函数中喂狗，系统正常运行

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

