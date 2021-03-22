---
title: Use of UART
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: use of UART
---


For details on UART, please refer to [UART-API Document](../../api_reference/machine/uart.md).

## Instructions

* Import UART module from machine

```python
from machine import UART
```

* The pin used for configuration is UART function

```python
fm.register(10, fm.fpioa.UART1_TX, force=True)
fm.register(11, fm.fpioa.UART1_RX, force=True)
```

* Create UART object

```python
uart = UART(UART.UART1, 115200, 8, 1, 0, timeout=1000, read_buf_len=4096)
```

* Read and write data

```python
uart.write(b'hello world')
read_data = uart.read()
```

## Example

Send back the data received by the serial port

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
        uart.write(read_data) # send data back
        print("wait data: ")

uart.deinit()
del uart
```
