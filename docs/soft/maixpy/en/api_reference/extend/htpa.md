---
title: modules.htpa (HTPA thermal infrared temperature measurement module)
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: modules.htpa (HTPA thermal infrared temperature measurement module)
---


Hyman HTPA 32x32 thermal infrared temperature measurement module

<img src="../../../assets/hardware/other/htpa32x32.png">

## Construction method htpa(i2c, scl_pin, sda_pin, i2c_freq)

Create an instance

### Parameters

* `i2c`: I2C number, such as `I2C.I2C0`, the value is [0, 2] (see `machine.I2C`)
* `scl_pin`: I2C SCL pin
* `sda_pin`: I2C SDA pin
* `i2c_freq`: I2C clock frequency


### return value

htpa object


## Instance method temperature()

Get the sensor temperature value, which can only be called by the instance

### return value

Array, length is the width x height of the sensor, such as `32x32`

## Instance method width()

Get the sensor resolution width, which can only be called by the instance

### return value

Integer, width

## Instance method height()

Get the sensor resolution width, which can only be called by the instance


## Examples

[heimann_HTPA_32x32](https://github.com/sipeed/MaixPy_scripts/tree/master/modules/others/heimann_HTPA_32x32)
