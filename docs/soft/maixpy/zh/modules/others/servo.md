---
title: 舵机
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 舵机
---


## 警告！请外接电源，不要用电脑供电给舵机，烧了自理。

## 使用方法

舵机需要使用 PWM 输出不同占空比来控制其旋转角度, 首先需要准备舵机

* 导入 PWM 模块，创建 PWM 对象，PWM 输出引脚接到舵机信号输入

```python
from machine import Timer,PWM
tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
S1 = PWM(tim, freq=50, duty=0, pin=17)
```

* 输出不同占空比波形来控制舵机

```python
S1.duty((angle+90)/180*10+2.5)
```

PWM 控制 API 参考: [PWM API](../../api_reference/machine/pwm.md)

## 例程

* 控制舵机旋转不同角度: [Servo](https://github.com/sipeed/MaixPy_scripts/blob/79a5485ec983e67bb8861305a52418b29e0dc205/modules/others/Servo/Servo.py)

* 舵机云台: [gimbal](https://github.com/sipeed/MaixPy_scripts/tree/master/application/gimbal)
