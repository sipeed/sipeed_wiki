---
title: steering gear
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy doc: steering gear
---


## caveat!Please use an external power supply, do not use a computer to supply power to the steering gear.

## Instructions

The steering gear needs to use PWM output with different duty ratios to control its rotation angle. First, you need to prepare the steering gear

* Import the PWM module, create a PWM object, and connect the PWM output pin to the servo signal input

```python
from machine import Timer,PWM
tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
S1 = PWM(tim, freq=50, duty=0, pin=17)
```

* Output different duty cycle waveforms to control the servo

```python
S1.duty((angle+90)/180*10+2.5)
```

PWM control API reference: [PWM API](../../api_reference/machine/pwm.md)

## Routine

* Control the servo to rotate at different angles: [Servo](https://github.com/sipeed/MaixPy_scripts/blob/79a5485ec983e67bb8861305a52418b29e0dc205/modules/others/Servo/Servo.py)

* Servo pan/tilt: [gimbal](https://github.com/sipeed/MaixPy_scripts/tree/master/application/gimbal)
