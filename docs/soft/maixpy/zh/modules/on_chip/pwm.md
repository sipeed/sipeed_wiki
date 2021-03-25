---
title: PWM 的使用
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: PWM 的使用
---


关于 PWM 详细介绍请参考[PWM-API 文档](../../api_reference/machine/pwm.md).

## 使用方法

* 从 machine 导入 PWM, Timer 模块

```python
from machine import Timer,PWM
```

* 创建 Timer 和 PWM

```python
tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
ch = PWM(tim, freq=500000, duty=50, pin=boad_info.LED_G)
```

* 改变占空比, 设置的 pin 脚将输出不同占空比的波形

```python
ch.duty(duty)
```

## 示例

控制 LED_G 灯亮度

> `board_info` 与板卡相关，不同板卡配置不同，使用前需要[手动配置](../../api_reference/builtin_py/board_info.md)。

```python
from machine import Timer,PWM
import time
from board import board_info
from fpioa_manager import fm

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
