---
title: HTPA thermal infrared temperature measurement module
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: HTPA thermal infrared temperature measurement module
---


<img src="./../../../assets/hardware/other/htpa32x32.png">
<img src="../../../assets/hardware/other/htpat_scale_240x240.png">

Can be used for non-contact temperature measurement.

## Parameters

* Power supply voltage (DC): 3.3V
* Current consumption: 5.5(±1.0)mA
* Clock frequency (sensor): 5(±3)MHz
* Ambient temperature range: -20 ~ 85℃
* Target temperature range: -20 ~ >1000°C
* Frame rate (full frame): 2 ~ 27hz
* Frame rate (quarter frame): 8 ~ 110hz
* Noise equivalent temperature difference (best optics): 140mK@1Hz
* Communication method: I2C

## Instructions

MaixPy has implemented htpa in modules (you need to enable the module when the firmware is compiled to be available).

* Import and create htpa

```python
from machine import I2C
from modules import htpa
dev = htpa(i2c=I2C.I2C0, scl_pin=7, sda_pin=6, i2c_freq=1000000)
```

* Get the temperature of all points in the detection range

```python
temperature = dev.temperature()
```

API details refer to [modules.htpa](../../api_reference/extend/htpa.md)

## Routine

* Draw temperature distribution graph on LCD: [htpa demo](https://github.com/sipeed/MaixPy_scripts/blob/79a5485ec983e67bb8861305a52418b29e0dc205/modules/others/heimann_HTPA_32x32/HTPA_32x32_demo.py)

## More

* Module information: [32x32 Thermopile Array](https://www.heimannsensor.com/32x32)
* Detailed tutorial: [thermal infrared heimann (Hyman) HTPA 32x32d](https://neucrack.com/p/199)
