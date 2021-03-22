---
title: Grove-Ultrasonic Ranger (Ultrasonic Ranger)
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: Grove-Ultrasonic Ranger (Ultrasonic Ranger)
---


<div class="grove_pic">
<img src="../../../assets/hardware/module_grove/ultrasonic.jpg">
</div>

Grove-Ultrasonic Ranger is a non-contact ranging module with a working frequency of 40KHz. The trigger and echo signals of Grove_Ultrasonic_Ranger share a SIG pin.

## Parameters

| Item    |Value  |
| -------- | ----------- |
|Working voltage |3.2~5.2V |
|Working current |8ma |
|Ultrasonic frequency | 40kHz |
|Measuring range |2-350cm |
|Resolution | 1cm |
|Output | PWM |
|Size | 50mm x 25mm x 16mm|
|Weight | 13g |
|Measurement angle |15° |
|Working temperature |-10~60°C |
|Trigger signal |10uS TTL |
|Echo signal |TTL |

## Instructions

MaixPy has implemented ultrasonic driver in the modules module.

* Import ultrasonic class and create object

```python
from modules import ultrasonic
device = ultrasonic(fm.fpioa.GPIOHS0)
```

* Get the current measurement distance (cm)

```python
distance = device.measure(unit = ultrasonic.UNIT_CM, timeout = 3000000)
```

## Routine

[Grove-Ultrasonic Ranger example](https://github.com/sipeed/MaixPy_scripts/tree/master/modules/grove/ultrasonic)

## More

* API manual: [modules.ultrasonic](../../api_reference/extend/ultrasonic.md)

* Module details: [Seeed Grove-Ultrasonic_Ranger](https://wiki.seeedstudio.com/Grove-Ultrasonic_Ranger/)
