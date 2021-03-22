---
title: HTPA 热红外测温模组
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: HTPA 热红外测温模组
---


<img src="./../../../assets/hardware/other/htpa32x32.png">
<img src="../../../assets/hardware/other/htpat_scale_240x240.png">

可用于无接触测温。

## 参数

* 电源电压(DC)：3.3V
* 电流消耗：5.5(±1.0)mA
* 时钟频率(传感器)：5(±3)MHz
* 环境温度范围：-20 ~ 85℃
* 对象温度范围：-20 ~ >1000°C
* 帧率(全帧)：2 ~ 27hz
* 帧率(四分之一帧)：8 ~ 110hz
* 噪声等效温差(最佳光学)：140mK@1Hz
* 通信方式：I2C

## 使用方法

MaixPy 已经在 modules 中实现了 htpa（需要在固件编译时该模块使能才可用）。

* 导入并创建 htpa

```python
from machine import I2C
from modules import htpa
dev = htpa(i2c=I2C.I2C0, scl_pin=7, sda_pin=6, i2c_freq=1000000)
```

* 获取检测范围内所有点的温度

```python
temperature = dev.temperature()
```

API 详情参考[modules.htpa](../../api_reference/extend/htpa.md)

## 例程

* 在 LCD 绘制温度分布图：[htpa demo](https://github.com/sipeed/MaixPy_scripts/blob/79a5485ec983e67bb8861305a52418b29e0dc205/modules/others/heimann_HTPA_32x32/HTPA_32x32_demo.py)

## 更多

* 模块资料：[32x32 Thermopile Array](https://www.heimannsensor.com/32x32)
* 详细教程: [热红外 heimann (海曼) HTPA 32x32d](https://neucrack.com/p/199)