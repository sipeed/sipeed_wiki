---
title: Binocular camera
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy doc: binocular camera
---


![](../../../assets/hardware/module/camera_binocular.png)

## Instructions

Need to prepare a binocular camera

* Import and initialize the binocular camera

```python
import sensor
sensor.binocular_reset()
sensor.shutdown(False)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.shutdown(True)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
```

* Turn on the camera and capture images

```python
sensor.shutdown(True)
img=sensor.snapshot()
```

For API details, please refer to: [Sensor API](../../api_reference/machine_vision/sensor.md)

## Routine

Capture image and display on LCD

[demo_binocular](https://github.com/sipeed/MaixPy_scripts/blob/5a03ab549d06cd713f2c0d19f0c18fbd24c69025/hardware/demo_binocular.py)
