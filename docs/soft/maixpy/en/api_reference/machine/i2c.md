---
title: machine.I2C
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: machine.I2C
---



I2C bus protocol, simply use two lines (SCL, SDA) to control multiple slaves (master mode).

* Support master mode and slave mode
* 7-bit/10-bit addressing mode
* Standard mode <=100Kb/s
* Fast mode <=400Kb/s
* Super fast mode <=1000Kb/s
* High-speed mode 3.4Mb/s

## Constructor

```python
class machine.I2C(id, mode=I2C.MODE_MASTER, scl=None, sda=None, gscl=None, gsda=None, freq=400000, timeout=1000, addr=0, addr_size=7, on_recieve=None, on_transmit =None, on_event=None)
```

Create a new I2C object with the specified parameters

### Parameters

* `id`: I2C ID, [0~2] \(I2C.I2C0~I2C.I2C2\) [3~5] \(I2C.I2C3~I2C.I2C5, I2C_SOFT\) is the number of soft analog I2C
* `mode`: Mode, master (`I2C.MODE_MASTER`) and slave (`I2C.MODE_SLAVE`) modes
* `scl`: SCL pin, just pass the pin number directly, the value range: [0,47]. It is not necessary to set, but use [fm](../builtin_py/fm.md) to manage pin mapping in a unified manner.
* `sda`: SDA pin, just pass the pin number directly, the value range: [0,47]. It is not necessary to set, but use [fm](../builtin_py/fm.md) to manage pin mapping in a unified manner.
* `gscl`: GPIOHS corresponding to SCL, only need to be passed when using software to simulate I2C, the default is the same as `scl`.
* `gsda`: GPIOHS corresponding to SDA, only need to be passed when using software to simulate I2C, the default is the same as `sda`.
* `freq`: I2C communication frequency, supports standard 100Kb/s, fast 400Kb/s, and higher rates (hardware supports ultra-fast mode 1000Kb/s, and high-speed mode 3.4Mb/s)
* `timeout`: timeout time, currently this parameter is reserved, the setting is invalid
* `addr`: slave address, if it is in master mode, don’t need to set, slave mode means slave (local) address
* `addr_size`: address length, supports 7-bit addressing and 10-bit addressing, the value is `7` or `10`
* `on_recieve`: Receive callback function in slave mode
* `on_transmit`: send callback function in slave mode
* `on_event`: event function in slave mode (start event and end event)

## Method

### init

Similar constructor

```python
i2c = I2C.init(id, mode=Timer.MODE_MASTER, scl, sda, gscl, gsda, freq=400000, timeout=1000, addr=0, addr_size=7, on_recieve=None, on_transmit=None, on_event=None)
```

#### Parameters

Same as constructor



#### return value

no


### scan

Scan the slave on the I2C bus

```python
i2c.scan()
```

#### Parameters

no

#### return value

list object, contains all scanned slave addresses


### readfrom

Read data from the bus

```python
i2c.readfrom(addr, len, stop=True)
```

#### Parameters

* `addr`: slave address
* `len`: data length
* `stop`: Whether to generate a stop signal, keep it, currently only the default value Ture can be used

#### return value

The read data, `bytes` type

### readfrom_into

Read the data and put it in the specified variable

```python
i2c.readfrom_into(addr, buf, stop=True)
```

#### Parameters

* `addr`: slave address
* `buf`: `bytearray` type, the length is defined, the data read is stored here
* `stop`: Whether to generate a stop signal, keep it, currently only the default value Ture can be used

#### return value

no

### writeto

Send data to slave

```python
i2c.writeto(addr, buf, stop=True)
```

#### Parameters


* `addr`: slave address
* `buf`: The data to be sent
* `stop`: Whether to generate a stop signal, keep it, currently only the default value Ture can be used

#### return value

Number of bytes sent successfully

### readfrom_mem

Read slave register

```python
i2c.readfrom_mem(addr, memaddr, nbytes, mem_size=8)
```

#### Parameters

* `addr`: slave address
* `memaddr`: slave register address
* `nbytes`: the length to be read
* `mem_size`: register width, the default is 8 bits

#### return value

Returns the read data of `bytes` type


### readfrom_mem_into

Read the slave register value into the specified variable

```python
i2c.readfrom_mem_into(addr, memaddr, buf, mem_size=8)
```

#### Parameters

* `addr`: slave address
* `memaddr`: slave register address
* `buf`: `bytearray` type, the length is defined, the data read is stored here
* `mem_size`: register width, the default is 8 bits

#### return value

no


### writeto_mem

Write data to slave register

```python
i2c.writeto_mem(addr, memaddr, buf, mem_size=8)
```

#### Parameters


* `addr`: slave address
* `memaddr`: slave register address
* `buf`: the data to be written
* `mem_size`: register width, the default is 8 bits

#### return value

no

### deinit/\__del\__

Log off the I2C hardware, release the occupied resources, and turn off the I2C clock

```python
i2c.deinit()
```

#### Parameters

no

#### return value

no

#### Examples

```python
i2c.deinit()
```
or
```python
del i2c
```


## Constant

* `I2C0`: I2C 0
* `I2C1`: I2C 1
* `I2C2`: I2C 2
* `MODE_MASTER`: as the master mode
* `MODE_SLAVE`: as a slave mode
* `I2C_EV_START`: Event type, start signal
* `I2C_EV_RESTART`: Event type, restart signal
* `I2C_EV_STOP`: Event type, end signal


## Routine

### Example 1: Scan the slave device

```python
from machine import I2C

i2c = I2C(I2C.I2C0, freq=100000, scl=28, sda=29)
devices = i2c.scan()
print(devices)
```

### Example 2: Read and write

```python
import time
from machine import I2C

i2c = I2C(I2C.I2C0, freq=100000, scl=28, sda=29)
i2c.writeto(0x24,b'123')
i2c.readfrom(0x24,5)
```

### Example 3: Slave mode

```python
from machine import I2C

count = 0

def on_receive(data):
    print("on_receive:",data)

def on_transmit():
    count = count+1
    print("on_transmit, send:",count)
    return count

def on_event(event):
    print("on_event:",event)

i2c = I2C(I2C.I2C0, mode=I2C.MODE_SLAVE, scl=28, sda=29, addr=0x24, addr_size=7, on_receive=on_receive, on_transmit=on_transmit, on_event=on_event)
```

### Example 4: OLED(ssd1306 128x64)
```python
import time
from machine import I2C

SSD1306_CMD = 0
SSD1306_DATA = 1
SSD1306_ADDR = 0x3c

def oled_init(i2c):
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0xAE, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0x20, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0x10, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0xb0, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0xc8, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0x00, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0x10, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0x40, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0x81, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0xff, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0xa1, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0xa6, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0xa8, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0x3F, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0xa4, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0xd3, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0x00, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0xd5, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0xf0, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0xd9, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0x22, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0xda, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0x12, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0xdb, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0x20, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0x8d, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0x14, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0xaf, mem_size=8)



def oled_on(i2c):
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0X8D, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0X14, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0XAF, mem_size=8)

def oled_off(i2c):
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0X8D, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0X10, mem_size=8)
    i2c.writeto_mem(SSD1306_ADDR, 0x00, 0XAE, mem_size=8)

def oled_fill(i2c, data):
    for i in range(0,8):
        i2c.writeto_mem(SSD1306_ADDR, 0x00, 0xb0+i, mem_size=8)
        i2c.writeto_mem(SSD1306_ADDR, 0x00, 0x10, mem_size=8)
        i2c.writeto_mem(SSD1306_ADDR, 0x00, 0x01, mem_size=8)
        for j in range(0,128):
            i2c.writeto_mem(SSD1306_ADDR, 0x40, data, mem_size=8)

i2c = I2C(I2C.I2C0, mode=I2C.MODE_MASTER, freq=400000, scl=28, sda=29, addr_size=7)

time.sleep(1)
oled_init(i2c)
oled_fill(i2c, 0xff)

```
