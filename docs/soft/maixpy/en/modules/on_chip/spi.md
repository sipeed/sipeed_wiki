---
title: Use of SPI
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: use of SPI
---


For details about SPI, please refer to [SPI-API Document](../../api_reference/machine/spi.md).

## Instructions

### Host Mode

* Import SPI module from machine

```python
from machine import SPI
```

* The pins used for configuration are chip select GPIO function and SPI function.

```python
fm.register(25,fm.fpioa.GPIOHS10, force=True)#cs
cs = GPIO(GPIO.GPIOHS10, GPIO.OUT)

fm.register(28,fm.fpioa.SPI1_D0, force=True)#mosi
fm.register(26,fm.fpioa.SPI1_D1, force=True)#miso
fm.register(27,fm.fpioa.SPI1_SCLK, force=True)#sclk
```

* Create SPI object

```python
spi1 = SPI(SPI.SPI1, mode=SPI.MODE_MASTER, baudrate=10000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB)
```

* Use chip select GPIO to select the slave, read and write data through SPI

```python
cs.value(0)
spi1.write_readinto(w, r)
cs.value(1)
```

### Slave mode

K210 SPI slave mode only supports three-wire communication, so this mode is not implemented in MaixPy. For slave mode, please refer to [SPI_SLAVE C SDK implementation](https://github.com/kendryte/kendryte-standalone-demo/tree/develop /spi_slave).

## Example

* Select the chip select GPIO corresponding to the slave and send and receive data

```python
from machine import SPI
from fpioa_manager import fm
from Maix import GPIO

m.register(25,fm.fpioa.GPIOHS10, force=True)#cs
cs = GPIO(GPIO.GPIOHS10, GPIO.OUT)

fm.register(28,fm.fpioa.SPI1_D0, force=True)#mosi
fm.register(26,fm.fpioa.SPI1_D1, force=True)#miso
fm.register(27,fm.fpioa.SPI1_SCLK, force=True)#sclk

spi1 = SPI(SPI.SPI1, mode=SPI.MODE_MASTER, baudrate=10000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB)

w = b'\xFF'
r = bytearray(1)

cs.value(0)
print(spi1.write_readinto(w, r))
cs.value(1)
```
