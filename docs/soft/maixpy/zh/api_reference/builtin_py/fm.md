---
title: fpioa_manager
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: fpioa_manager
---


> **本文档在 MaixPy 0.5.1-128 版本测试通过。**

fpioa_manager：简称`fm`，该模块用于注册芯片内部功能和引脚，帮助用户管理内部功能和引脚映射关系的功能模块。

## 如何理解【引脚]映射[内部功能]？

K210 芯片上的 外部引脚 和 内部功能 是彼此独立的，引脚是指从芯片上引出的许多金属触点，也就是我们俗称的功能引脚，它可以是 GPIO / PWM / ADC / I2C 等内部功能引脚，传统的认知是引脚对应的内部功能是不可改变的，但可以复用的，而 K210 是可以通过映射来改变引脚功能的，看如下示意图理解具体的映射功能。

首先可以将 I2C 的 SCL/SDA 映射（MAP）到 IO6/IO7 引脚，从而在此引脚上进行 I2C 的读写操作。

```
    +------------------------------+
    |                              |
    |           +---+              |
<-----+ <-----+ |I2C|              |
 IO6|           +---+              |
    |           |                  |
    |           |   +----+         |
<-----+ <-------+   |UART|         |
 IO7|               +----+         |
    |                              |
    |           +---+              |
<-----+         |SPI|              |
 IO8|           +---+              |
    |                              |
    |             +---+            |
<-----+           |I2S|            |
 IO9|             +---+            |
    |                              |
    |                              |
    +------------------------------+
```

接着还可以将 SPI 的 SCLK/MOSI/MISO/CS 映射（MAP）到 IO6/IO7/IO8/IO9 引脚，也就可以在此引脚上进行 SPI 的读写操作。

```
    +------------------------------+
    |                              |
    |               +---+          |
<------<-------<--  |I2C|          |
 IO6|            |  +---+          |
    |            |                 |
    |            |       +----+    |
<------<------+  |       |UART|    |
 IO7|         |  |       +----+    |
    |         +--+-+               |
    |          |SPI|               |
<------<--------+--+               |
 IO8|           |                  |
    |           |                  |
    |           |    +---+         |
<------<--------+    |I2S|         |
 IO9|                +---+         |
    |                              |
    |                              |
    +------------------------------+
```

## 使用方法

调用 register 函数将 pin 引脚与具体的硬件功能(GPIO/I2C/UART/I2S/SPI)绑定起来，在不使用的时候调用 unregister 释放引脚所绑定的硬件功能（或称 **function** ），这不同于传统单片机的理解， K210 可以将一定范围内的引脚映射到具体的硬件功能。

如下代码所示：

```python
from fpioa_manager import fm

fm.register(11, fm.fpioa.GPIO0, force=True)
fm.register(12, fm.fpioa.GPIOHS0, force=True)
fm.register(13, fm.fpioa.UART2_TX)
fm.register(14, fm.fpioa.UART2_RX)

# other code

fm.unregister(11)
fm.unregister(12)
fm.unregister(13)
fm.unregister(14)
```

**注意事项**:

以下 GPIOHS 已经在 MaixPy 中默认使用，程序中如非必要请不要使用。

| GPIOHS | 功能| 描述 |
| ------ | --- | --- |
| GPIOHS31 | LCD_DC      | LCD 控制信号引脚 |
| GPIOHS30 | LCD_RST     | LCD 复位芯片脚 |
| GPIOHS29 | SD_CS       | SD 卡 SPI 片选 |
| GPIOHS28 | MIC_LED_CLK | SK9822_DAT |
| GPIOHS27 | MIC_LED_DATA | SK9822_CLK |

另外以下引脚已经在 MaxiPy 开机启动时注册，请注意。

### SD卡
* `功能`：SPI1_SCLK/SPI1_D0/SPI1_D1/GPIOHS29/SPI0_SS1
* `引脚`：PIN25/PIN26/PIN27/PIN28/PIN29

### LCD
* `功能`：SPI0_SS3/SPI0_SCLK/GPIOHS30/GPIOHS31
* `引脚`：PIN36/PIN37/PIN38/PIN39

### sensor
* `功能`：SCCB_SDA/SCCB_SCLK/CMOS_RST/CMOS_VSYNC/CMOS_PWDN/CMOS_HREF/CMOS_XCLK/CMOS_PCLK
* `引脚`：PIN40/PIN41/PIN42/PIN43/PIN44/PIN45/PIN46/PIN47

### REPL
* `功能`：UARTHS_RX/UARTHS_TX
* `引脚`：PIN4/PIN5

## class `fm`

### register(pin, func, force=True)

* `pin`: 功能映射引脚
* `function` : 芯片功能
* `force`: 强制分配，如果为`True`，则可以多次对同一个引脚注册;`False`则不允许同一引脚多次注册。默认为`True`是为了方便`IDE`多次运行程序使用

设置引脚（pin）对应的外设功能（func），默认启用强制绑定参数（force=True），它将强制更换指定的引脚功能，如果发现存在上一个绑定的引脚，则会发出一个警告，但不影响代码继续执行。 

如果设置 force=False ，则会在 register 发现硬件功能已经被使用了，此时就会弹出异常，方便深度开发的时候不清楚 GPIO/HS 的分配情况，常见于运行某个代码的按键在访问某些功能的时候不能使用了的场合。

#### 使用方法

```python
from fpioa_manager import fm
fm.register(16, fm.fpioa.GPIO2)
fm.register(13, fm.fpioa.GPIO2)
fm.register(12, fm.fpioa.GPIO2, force=False)
```

可见提示了 fm.fpioa.GPIO2(pin:16) 和 fm.fpioa.GPIO2(pin:13) 的占用情况。

```shell
[Warning] function is used by fm.fpioa.GPIO2(pin:16)
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
  File "fpioa_manager.py", line 20, in register
Exception: [Warning] function is used by fm.fpioa.GPIO2(pin:13)
```

### unregister(pin)

释放引脚（pin）上的硬件功能（GPIO/I2C/SPI/I2S/UART）。

### get_pin_by_function(pin)

获取引脚（pin）上绑定的硬件功能。

### get_gpio_used()

获取所有 gpio 的使用情况，它只查询 GPIOHS / GPIO 的引脚分配情况, None 表示该硬件功能未被使用。

#### 使用方法

```python
from fpioa_manager import fm
for item in fm.get_gpio_used():
    print(item)
```

> 注意：每个引脚都会有默认状态

```shell
('fm.fpioa.GPIOHS0', 16)
('fm.fpioa.GPIOHS1', 17)
('fm.fpioa.GPIOHS2', 18)
('fm.fpioa.GPIOHS3', 19)
('fm.fpioa.GPIOHS4', 37)
('fm.fpioa.GPIOHS5', 38)
('fm.fpioa.GPIOHS6', 22)
('fm.fpioa.GPIOHS7', 23)
('fm.fpioa.GPIOHS8', 24)
('fm.fpioa.GPIOHS9', 25)
('fm.fpioa.GPIOHS10', None)
('fm.fpioa.GPIOHS11', 27)
('fm.fpioa.GPIOHS12', 28)
('fm.fpioa.GPIOHS13', 29)
('fm.fpioa.GPIOHS14', 30)
('fm.fpioa.GPIOHS15', 31)
('fm.fpioa.GPIOHS16', 32)
('fm.fpioa.GPIOHS17', 33)
('fm.fpioa.GPIOHS18', 34)
('fm.fpioa.GPIOHS19', 35)
('fm.fpioa.GPIOHS20', None)
('fm.fpioa.GPIOHS21', None)
('fm.fpioa.GPIOHS22', None)
('fm.fpioa.GPIOHS23', None)
('fm.fpioa.GPIOHS24', 40)
('fm.fpioa.GPIOHS25', 41)
('fm.fpioa.GPIOHS26', 42)
('fm.fpioa.GPIOHS27', 43)
('fm.fpioa.GPIOHS28', 44)
('fm.fpioa.GPIOHS29', 26)
('fm.fpioa.GPIOHS30', 46)
('fm.fpioa.GPIOHS31', 47)
('fm.fpioa.GPIO0', 8)
('fm.fpioa.GPIO1', 9)
('fm.fpioa.GPIO2', None)
('fm.fpioa.GPIO3', None)
('fm.fpioa.GPIO4', 12)
('fm.fpioa.GPIO5', 13)
('fm.fpioa.GPIO6', 14)
('fm.fpioa.GPIO7', 15)
```

### help()

调用它会打印出如下『附录： 外设表』帮助说明。

详细看 [FPIOA](../Maix/fpioa.md) 。
