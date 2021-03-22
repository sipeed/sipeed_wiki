---
title: Use of I2C
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: the use of I2C
---


For detailed introduction of I2C, please refer to [I2C-API Document](../../api_reference/machine/i2c.md).

## Instructions

### Host Mode

* Create I2C (software simulation or hardware) objects

```python
from machine import I2C
from fpioa_manager import fm
# i2c = I2C(I2C.I2C0, freq=100000, scl=28, sda=29) # hardware i2c
i2c = I2C(I2C.I2C4, freq=100000, scl=28, sda=29,gscl=fm.fpioa.GPIOHS3,gsda=fm.fpioa.GPIOHS2) # software i2c
```

* Scan slaves, return all slave addresses

```python
devices = i2c.scan()
```

* Read and write data to the slave

```python
for device in devices:
    i2c.writeto(device, b'123')
    i2c.readfrom(device, 3)
```

### Slave mode

* Create slave callback function

```python
count = 0
def on_receive(data):
    print("on_receive:",data)

def on_transmit():
    count = count+1
    print("on_transmit, send:",count)
    return count

def on_event(event):
    print("on_event:",event)
```

* Create I2C object

```python
from machine import I2C
i2c = I2C(I2C.I2C0, mode=I2C.MODE_SLAVE, scl=28, sda=29, addr=0x24, addr_size=7, on_receive=on_receive, on_transmit=on_transmit, on_event=on_event)
```

## Example

* Read all slave addresses and send and receive data respectively

```python
from machine import I2C

i2c = I2C(I2C.I2C0, freq=100000, scl=28, sda=29) # software i2c

devices = i2c.scan()
print(devices)

for device in devices:
    i2c.writeto(device, b'123')
    i2c.readfrom(device, 3)
```

* Slave mode example

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
