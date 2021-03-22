---
title: 双目摄像头
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 双目摄像头
---


![](../../../assets/hardware/module/camera_binocular.png)

## 使用方法

需要准备一个双目摄像头

* 导入并初始化双目摄像头

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

* 打开摄像头并捕捉图像

```python
sensor.shutdown(True)
img=sensor.snapshot()
```

API 详情请参考: [Sensor API](../../api_reference/machine_vision/sensor.md)

## 例程

捕捉图像并显示在 LCD 上

[demo_binocular](https://github.com/sipeed/MaixPy_scripts/blob/5a03ab549d06cd713f2c0d19f0c18fbd24c69025/hardware/demo_binocular.py)
