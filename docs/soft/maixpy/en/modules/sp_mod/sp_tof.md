---
title: Use of SP_TOF
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: use of SP_TOF
---


<img src="../../../assets/hardware/module_spmod/sp_tof.png"/>

The VL53L0X used by SP_TOF is a new generation of time-of-flight (ToF) laser ranging module, which can provide accurate distance measurement regardless of the reflectivity of the target, with a red laser sight to assist in observing the ranging point.

## Parameters

* Measuring distance: up to 2000mm (dark environment), 1000mm (bright environment)
* Working refresh rate: 50Hz
* Measuring angle: 27° (front)
* Communication interface: I2C
* Working voltage: 2.6V~3.5V
* Working temperature: -40°C~80°C

For detailed module information, please refer to [TOF Specification and Data Manual](http://api.dl.sipeed.com/shareURL/MAIX/HDK/sp_mod/sp_tof)

## Instructions

1. Preparation: The development board with the latest firmware, sp_tof module.

2. Run: Connect the module, modify the configuration surrounded by config in [Sample Code](https://github.com/sipeed/MaixPy_scripts/tree/master/modules/spmod/sp_tof), and aim the laser aiming head to measure after running Click to see the distance information printed by the terminal.

The procedure is as follows:

```python
# create obj and read distance
tof = VL53L0X(i2c)
while True:
    mm = tof.read()
    utime.sleep_ms(100)
    print(mm)

'''output
>>> [41]
536mm
538mm
533mm
535mm
529mm
532mm
'''
```

The main steps are:

* Create TOF object (parameter: I2C object).

* The reading distance, if the reading distance is 8190, it means that the range has been exceeded.
