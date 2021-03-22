---
title: GPIO 的使用
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: GPIO 的使用
---

关于 GPIO 详细介绍请参考[GPIO-API 文档](../../api_reference//Maix/gpio.md).

## 使用方法

* 将某 IO 注册为 GPIO 功能

```python
from Maix import GPIO
from fpioa_manager import fm

fm.register(io_number,fm.fpioa.GPIO0)
```

* 设置 GPIO 为输入或输出模式

```python
gpio=GPIO(GPIO.GPIO0,GPIO.OUT)
```

* 读取或设置 GPIO 电平

```python
gpio.value()
```

## 示例

> `board_info` 与板卡相关，不同板卡配置不同，使用前需要[手动配置](../../api_reference/builtin_py/board_info.md)。

点亮 LED

```python
import utime
from Maix import GPIO
from board import board_info
from fpioa_manager import fm

fm.register(board_info.LED_R,fm.fpioa.GPIO0)
led_r=GPIO(GPIO.GPIO0,GPIO.OUT)
utime.sleep_ms(500)
led_r.value(0)
fm.unregister(board_info.LED_R)
```