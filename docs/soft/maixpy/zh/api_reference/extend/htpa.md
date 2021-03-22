---
title: modules.htpa（HTPA 热红外测温模组）
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: modules.htpa（HTPA 热红外测温模组）
---


海曼 HTPA 32x32 热红外测温模组

<img src="../../../assets/hardware/other/htpa32x32.png">

## 构造方法 htpa(i2c, scl_pin, sda_pin, i2c_freq)

创建一个实例

### 参数

* `i2c`: I2C编号， 比如`I2C.I2C0`，取值 [0, 2] (见`machine.I2C`)
* `scl_pin`: I2C SCL 引脚
* `sda_pin`: I2C SDA 引脚
* `i2c_freq`: I2C 时钟频率


### 返回值

htpa 对象


## 实例方法 temperature()

获取传感器温度值，只能被实例调用

### 返回值

数组，长度为传感器的宽度x高度，比如`32x32`

## 实例方法 width()

获取传感器分辨率宽度，只能被实例调用

### 返回值

整数，宽度

## 实例方法 height()

获取传感器分辨率宽度，只能被实例调用


## 例子

[heimann_HTPA_32x32](https://github.com/sipeed/MaixPy_scripts/tree/master/modules/others/heimann_HTPA_32x32)

