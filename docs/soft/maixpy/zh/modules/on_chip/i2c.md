---
title: I2C 的使用
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: I2C 的使用
---


关于 I2C 详细介绍请参考[I2C-API 文档](../../api_reference/machine/i2c.md).

## 使用方法

### 主机模式

* 创建 I2C(软件模拟或硬件) 对象

```python
from machine import I2C
from fpioa_manager import fm
# i2c = I2C(I2C.I2C0, freq=100000, scl=28, sda=29) # hardware i2c
i2c = I2C(I2C.I2C4, freq=100000, scl=28, sda=29,gscl=fm.fpioa.GPIOHS3,gsda=fm.fpioa.GPIOHS2) # software i2c
```

* 扫描从机, 返回所有从机地址

```python
devices = i2c.scan()
```

* 对从机读写数据

```python
for device in devices:
    i2c.writeto(device, b'123')
    i2c.readfrom(device, 3)
```

### 从机模式

* 创建从机回调函数

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

* 创建 I2C 对象

```python
from machine import I2C
i2c = I2C(I2C.I2C0, mode=I2C.MODE_SLAVE, scl=28, sda=29, addr=0x24, addr_size=7, on_receive=on_receive, on_transmit=on_transmit, on_event=on_event)
```

## 示例

* 读取所有从机地址并分别收发数据

```python
from machine import I2C

i2c = I2C(I2C.I2C0, freq=100000, scl=28, sda=29) # software i2c

devices = i2c.scan()
print(devices)

for device in devices:
    i2c.writeto(device, b'123')
    i2c.readfrom(device, 3)
```

* 从机模式示例

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