---
title: Timer（定时器） 的使用
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: Timer（定时器） 的使用
---


关于 Timer 详细介绍请参考[Timer-API 文档](../../api_reference/machine/timer.md).

## 使用方法

* 从 machine 导入 Timer 模块

```python
from machine import Timer
```

* 创建 Timer 对象

```python
def on_timer(timer):
    print("time up:",timer)
    print("param:",timer.callback_arg())

tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PERIODIC, period=1, unit=Timer.UNIT_S, callback=on_timer, arg=on_timer, start=False, priority=1, div=0)
```

* 启动定时器, 此时定时器将定时执行回调函数

```python
tim.start()
```

* 停止定时器

```python
tim.stop()
```

## 示例

定时执行回调函数

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
