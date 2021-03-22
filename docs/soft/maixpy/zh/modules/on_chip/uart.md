---
title: UART 的使用
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: UART 的使用
---


关于 UART 详细介绍请参考[UART-API 文档](../../api_reference/machine/uart.md).

## 使用方法

* 从 machine 导入 UART 模块

```python
from machine import UART
```

* 配置使用到的 pin 脚为 UART 功能

```python
fm.register(10, fm.fpioa.UART1_TX, force=True)
fm.register(11, fm.fpioa.UART1_RX, force=True)
```

* 创建 UART 对象

```python
uart = UART(UART.UART1, 115200, 8, 1, 0, timeout=1000, read_buf_len=4096)
```

* 读写数据

```python
uart.write(b'hello world')
read_data = uart.read()
```

## 示例

将串口接收到的数据发送回去

```python
from fpioa_manager import fm
from machine import UART
import time

# need your connect hardware IO 10/11 to loopback
fm.register(10, fm.fpioa.UART1_TX, force=True)
fm.register(11, fm.fpioa.UART1_RX, force=True)

uart = UART(UART.UART1, 115200, 8, 1, 0, timeout=1000, read_buf_len=4096)

uart.write(b'hello world')

while True:
    read_data = uart.read()
    if read_data:
        print("recv:", read_data)
        uart.write(read_data)  # send data back
        print("wait data: ")

uart.deinit()
del uart
```
