---
title: machine.PWM
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: machine.PWM
---


PWM： 脉宽调制模块， 硬件支持的PWM， 可以指定任意引脚（0到47引脚）

每个 PWM 依赖于一个定时器， 即当定时器与 PWM 功能绑定后， 不能作为普通定时器使用了。 因为有 3 个定时器， 每个定时器有 4 个通道， 即最大可以同时产生 12 路 PWM 波形

## 构造函数

```python
pwm = machine.PWM(tim, freq, duty, pin, enable=True)
```

通过指定的参数新建一个 PWM 对象

### 参数

* `tim`: 每个PWM依赖一个定时器来产生波形， 所以这里需要传一个定时器对象，这个定时器对象必须初始化时必须指定定时器 ID 和通道号
* `freq`： PWM 波形频率
* `duty`： PWM 占空比， 指高电平占整个周期的百分比，取值：[0,100]
* `[pin]`： PWM 输出引脚。 可以不设置，而是使用 [fm](../builtin_py/fm.md) 统一管理引脚映射。
* `enable`： 是否立即开始产生波形，默认位`True`，及对象生成后立即开始在指定的引脚上产生 PWM 波形

## 方法

### init

类似构造函数

```python
pwm.init(tim, freq, duty, pin, enable=True)
```

#### 参数

与构造函数相同

#### 返回值

无


### freq

获取或者设置 PWM 频率

```python
pwm.freq(freq)
```

#### 参数

* `freq`： PWM 频率， 可选参数， 如果不传参数则步设置只返回当前频率值

#### 返回值

当前设置的实际的 PWM 频率


### duty

获取或者设置 PWM 占空比

```python
pwm.duty(duty)
```

#### 参数

* `duty`： PWM 占空比 可选， 如果不传参数则步设置只返回当前占空比值

#### 返回值

当前设置的 PWM 占空比值


### enable

使能 PWM 输出， 使指定的引脚上立即产生波形

```python
pwm.enable()
```

#### 参数

无

#### 返回值

无

### disable

失能 PWM 输出， 指定的引脚不再产生波形

```python
pwm.disable()
```

#### 参数

无

#### 返回值

无

### deinit/\__del\__

注销 PWM 硬件，释放占用的资源，关闭 PWM 时钟

```python
pwm.deinit()
```

#### 参数

无

#### 返回值

无

#### 例子

```python
pwm.deinit()
```
或者
```python
del pwm
```

## 常量

无


## 例程


### 例程 1 （呼吸灯）

> `board_info` 与板卡相关，不同板卡配置不同，使用前需要[手动配置](../builtin_py/board_info.md)。

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

### 例程 2

> `board_info` 与板卡相关，不同板卡配置不同，使用前需要[手动配置](../builtin_py/board_info.md)。

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

