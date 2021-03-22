---
title: machine.Timer
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: machine.Timer
---


硬件定时器，可以用来定时触发任务或者处理任务，设定时间到了后可以触发中断（调用回调函数），精度比软件定时器高。
需要注意的是，定时器在不同的硬件中可能会有不同的表现。MicroPython 的 Timer 类定义了在给定时间段内（或在一段延迟后执行一次回调）执行回调的基本操作，并允许特定的硬件上定义更多的非标准行为（因此不能移植到其他板）。

共有 3 个定时器， 每个定时器有 4 个通道可以使用

## 构造函数

```python
tim = machine.Timer(id, channel, mode=Timer.MODE_ONE_SHOT, period=1000, unit=Timer.UNIT_MS, callback=None, arg=None, start=True, priority=1, div=0)
```

通过指定的参数新建一个 Timer 对象

### 参数

* `id`: Timer ID, [0~2] \(Timer.TIMER0~TIMER2\)
* `channel`: Timer 通道, [Timer.CHANNEL0~Timer.CHANNEL3]
* `mode`: Timer 模式, `MODE_ONE_SHOT` 或者 `MODE_PERIODIC` 或者 `MODE_PWM`
* `period`: Timer 周期, 在启动定时器后 `period` 时间， 回调函数将会被调用，(0,~)
* `unit`: 设置周期的单位，默认位毫秒（`ms`），`Timer.UNIT_S` 或者 `Timer.UNIT_MS` 或者 `Timer.UNIT_US` 或者`Timer.UNIT_NS`
* `callback`: 定时器回调函数， 定义了两个参数， 一个是定时器对象`Timer`， 第二个是在定义对象是希望传的参数`arg`，更多请看`arg`参数解释
> 注意：回调函数是在中断中调用的，所以在回调函数中请不要占用太长时间以及做动态分配开关中断等动作
* `arg`: 希望传给回调函数的参数，作为回调函数的第二个参数
* `start`: 是否在对象构建成功后立即开始定时器， `True`：立即开始， `False`:不立即开启，需要调用`start()`函数来启动定时器
* `priority`: 硬件定时器中断优先级， 与特定的CPU相关， 在K210中，取值范围是[1,7]， 值越小优先级越高
* `div`: 硬件定时器分频器，取值范围[0,255]， 默认为0， clk_timer（定时器时钟频率） = clk_pll0（锁相环0频率）/2^(div+1)
> clk_timer*period(unit:s) 应该 < 2^32 并且 >=1


## 方法

### init

类似构造函数

```python
tim.init(id, channel, mode=Timer.MODE_ONE_SHOT, period=1000, unit=Timer.UNIT_MS, callback=None, arg=None, start=True, priority=1, div=0)
```

#### 参数

类似构造函数

#### 返回值

无


### callback_arg

获取设置的传给回调函数的参数，只能是 `Timer` 对象调用， 类 `Timer` 不能调用


### callback

获取或者设置回调函数

```python
tim.callback(callback)
```

#### 参数

* `callback`： 设置的回调函数，可选参数， 如果不传参数，则只返回先有的回调函数

#### 返回值

当前的回调函数

#### 例子

```python
def on_timer(timer):
    print("time up:",timer)
    print("param:",timer.callback_arg())

tim.callback(on_timer)
print(on_timer, tim.callback())
```

### period

获取或者设置定时周期

```python
tim.period(period)
```

#### 参数

* `period`： 可选参数，配置周期， 如果不传参数， 则只返回当前周期值

#### 返回值

当前周期值

#### 例子

```python
tim.period(2000)
print( tim.period() )
```

### start

启动定时器

```python
tim.start()
```

#### 参数

无

#### 返回值

无

#### 例子

```python
tim.start()
```

### stop

停止定时器

```python
tim.stop()
```

#### 参数

无

#### 返回值

无

### restart

重新开启定时器

```python
tim.restart()
```

#### 参数

无

#### 返回值

无

### deinit/\__del\__

注销定时器，并且注销硬件的占用，关闭硬件的时钟

```python
tim.deinit()
```

#### 参数

无

#### 返回值

无

#### 例子

```python
tim.deinit()
```
或者
```python
del tim
```

## 常量

* `TIMER0`: Timer0 id
* `TIMER1`: Timer1 id
* `TIMER2`: Timer2 id
* `CHANNEL0`: Timer 通道 0
* `CHANNEL1`: Timer 通道 1
* `CHANNEL2`: Timer 通道 2
* `CHANNEL3`: Timer 通道 3
* `MODE_ONE_SHOT`: Timer 只运行一次（回调一次）
* `MODE_PERIODIC`: Timer 始终运行（连续回调）
* `MODE_PWM`: 定时器不用来回调函数，用以产生PWM
* `UNIT_S`:  单位秒 (s)
* `UNIT_MS`: 单位毫秒 (ms)
* `UNIT_US`: 单位微秒 (us)
* `UNIT_NS`: 单位纳秒 (ns)


## 例程

### 例程 1

定时3秒后打印信息

```python
from machine import Timer

def on_timer(timer):
    print("time up:",timer)
    print("param:",timer.callback_arg())

tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_ONE_SHOT, period=3000, callback=on_timer, arg=on_timer)
print("period:",tim.period())
```

### 例程 2

每隔 1 秒打印消息， 停止 5 秒后再重启， 5 秒后关闭并注销定时器

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



