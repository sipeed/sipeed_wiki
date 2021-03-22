---
title: fpioa_manager
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: fpioa_manager
---


> **This document has passed the test of MaixPy 0.5.1-128. **

fpioa_manager: abbreviated as `fm`, this module is used to register the internal functions and pins of the chip, and help users to manage the internal functions and pin mapping relationships.

## How to understand [pin] mapping [internal function]?

The external pins and internal functions on the K210 chip are independent of each other. The pins refer to many metal contacts drawn from the chip, which are also commonly known as function pins. It can be GPIO / PWM / ADC / I2C, etc. Function pins, the traditional cognition is that the internal functions corresponding to the pins cannot be changed, but they can be reused. The K210 can change the pin functions through mapping. See the diagram below to understand the specific mapping functions.

First, you can map (MAP) the I2C SCL/SDA to the IO6/IO7 pin, so that I2C read and write operations can be performed on this pin.

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

Then you can map (MAP) the SCLK/MOSI/MISO/CS of SPI to the IO6/IO7/IO8/IO9 pin, and you can read and write SPI on this pin.

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

## Instructions

Call the register function to bind the pin to the specific hardware function (GPIO/I2C/UART/I2S/SPI), and call unregister when not in use to release the hardware function bound to the pin (or **function* *) This is different from the understanding of traditional single-chip microcomputers. K210 can map pins within a certain range to specific hardware functions.

As shown in the following code:

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

**Precautions**:

The following GPIOHS has been used by default in MaixPy, please don't use it unless necessary in the program.

| GPIOHS | Function | Description |
| --- | --- | --- |
| GPIOHS31 | LCD_DC | LCD control signal pin |
| GPIOHS30 | LCD_RST | LCD reset chip pin |
| GPIOHS29 | SD_CS | SD card SPI chip select |
| GPIOHS28 | MIC_LED_CLK | SK9822_DAT |
| GPIOHS27 | MIC_LED_DATA | SK9822_CLK |

In addition, the following pins have been registered when MaxiPy starts up, please pay attention.

### SD card
* `Function`: SPI1_SCLK/SPI1_D0/SPI1_D1/GPIOHS29/SPI0_SS1
* `Pin`: PIN25/PIN26/PIN27/PIN28/PIN29

### LCD
* `Function`: SPI0_SS3/SPI0_SCLK/GPIOHS30/GPIOHS31
* `Pin`: PIN36/PIN37/PIN38/PIN39

### sensor
* `Function`: SCCB_SDA/SCCB_SCLK/CMOS_RST/CMOS_VSYNC/CMOS_PWDN/CMOS_HREF/CMOS_XCLK/CMOS_PCLK
* `Pin`: PIN40/PIN41/PIN42/PIN43/PIN44/PIN45/PIN46/PIN47

### REPL
* `Function`: UARTHS_RX/UARTHS_TX
* `Pin`: PIN4/PIN5

## class `fm`

### register(pin, func, force=True)

* `pin`: Function mapping pin
* `function`: Chip function
* `force`: Forced allocation, if it is `True`, the same pin can be registered multiple times; `False` does not allow multiple registration of the same pin. The default is `True` to facilitate the use of `IDE` to run the program multiple times

Set the peripheral function (func) corresponding to the pin (pin). The forced binding parameter (force=True) is enabled by default. It will force the specified pin function to be replaced. If it finds the last bound pin, it will A warning is issued, but it does not affect the continued execution of the code.

If force=False is set, it will be found in the register that the hardware function has been used, and an exception will pop up at this time, which is convenient for in-depth development. When some functions cannot be used.

#### Instructions

```python
from fpioa_manager import fm
fm.register(16, fm.fpioa.GPIO2)
fm.register(13, fm.fpioa.GPIO2)
fm.register(12, fm.fpioa.GPIO2, force=False)
```

It can be seen that the occupancy status of fm.fpioa.GPIO2(pin:16) and fm.fpioa.GPIO2(pin:13) are prompted.

```shell
[Warning] function is used by fm.fpioa.GPIO2(pin:16)
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
  File "fpioa_manager.py", line 20, in register
Exception: [Warning] function is used by fm.fpioa.GPIO2(pin:13)
```

### unregister(pin)

Release the hardware function (GPIO/I2C/SPI/I2S/UART) on the pin.

### get_pin_by_function(pin)

Get the hardware function bound on the pin.

### get_gpio_used()

Get the usage status of all gpio, it only queries the GPIOHS / GPIO pin assignment, None means that the hardware function is not used.

#### Instructions

```python
from fpioa_manager import fm
for item in fm.get_gpio_used():
    print(item)
```

> Note: Each pin will have a default state
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

Calling it will print out the following help description of "Appendix: Peripheral Table".

See [FPIOA](../Maix/fpioa.md) for details.
