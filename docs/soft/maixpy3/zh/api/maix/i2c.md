---
title: MaixII M2dock I2C 调试
keywords: MaixII, MaixPy3, Python, Python3, M2dock
desc: maixpy doc: MaixII M2dock I2C 调试
---

V831 镜像中默认包含 **i2c-tools**, i2c-tools 包含如下四条命令

## 1. i2cdetect

**查询 I2C 用法**

```shell
Usage: i2cdetect [-y] [-a] [-q|-r] I2CBUS [FIRST LAST]
       i2cdetect -F I2CBUS
       i2cdetect -l
  I2CBUS is an integer or an I2C bus name
```

**查询 I2C 总线**

```shell
i2cdetect -l
```



**查询 I2C 总线上挂载的设备**

| -y   | 取消交互过程，直接执行指令 |
| ---- | ------------- |
| twi2 | I2C 总线编号      |

```shell
i2cdetect -y 1
```



## 2. i2cdump

扫描寄存器内容：

```shell
i2cdump -y 1 0x68
```



## 3. i2cget

```shell
i2cget -y 1 0x68 0x00
```

| -y   | 取消交互过程，直接执行指令                 |
| ---- | ----------------------------- |
| 1    | I2C 总线编号                      |
| 0x68 | I2C 设备地址，此处表示 DS3231 RTC 时钟芯片 |
| 0x00 | 代表存储器地址                       |



## 4. i2cset

**寄存器内容写入：**

```shell
i2cset -y 1 0x68 0x00 0x13
```

| -y   | 取消交互过程，直接执行指令                 |
| ---- | ----------------------------- |
| 1    | I2C 总线编号                      |
| 0x68 | I2C 设备地址，此处表示 DS3231 RTC 时钟芯片 |
| 0x00 | 寄存器地址                         |
| 0x13 | 需要写入的寄存器值                     |

## python

```python
from maix import i2c
i2c = i2c.I2CDevice('/dev/i2c-2', 0x26)
print(i2c)
print(i2c.read(0x1, 1))
```
