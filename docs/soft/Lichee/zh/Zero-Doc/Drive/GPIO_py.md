---
title: Python 操作GPIO
---
需要python3.8及以上版本
首先需要安装gpiod
下载gpiod的源码，解压到zero中。

` wget https://files.pythonhosted.org/packages/09/4f/9c246b2133414f2566d848e89b20dbd8f22dd323f05954ecbb105191ab2a/gpiod-1.5.0.tar.gz`


解压后，使用

```bash
python setup.py build
python setup.py install
```
安装

如果出现 ` ValueError: ZIP does not support timestamps before 1980` ,则需要修改下系统时间。

` date -s 2022-2-22`

gpiod依赖于libgpiod，还需要在buildroot中开启。需要注意的是，编译器内核要大于4.8，因此6.x的交叉编译工具不能使用（内核4.6）

升级编译链版本后，需要make clean后重新编译。

如果使用的设备树是with-dock的话，还需要注释掉mmc1，不然无法控制PG0-PG5。
然后运行led.py即可。

如果出现** ` module 'gpiod' has no attribute 'chip` , 则需要打开 `/usr/bin/python` , 删除掉gpiod.so

led.py

```python
import time
import gpiod as gpio
PG_BASE = (7-1)*32 # "PG"
gpiochip0 = gpio.chip("gpiochip0")
led = gpiochip0.get_line((PG_BASE + 1)) # "PG1"
config = gpio.line_request()
config.request_type = gpio.line_request.DIRECTION_OUTPUT
led.request(config)
 
while led:
    led.set_value(0)
    time.sleep(1)
    print(hello sipeed!)
    led.set_value(1)
    time.sleep(1)
    print(hello sipeed!)
```
运行结果
```bash
licheepi# python led.py
[ 3634.510245] sun8i-v3s-pinctrl 1c20800.pinctrl: 1c20800.pinctrl supply vcc-pg not found, using dummy regulator
hello sipeed!
hello sipeed!
```
