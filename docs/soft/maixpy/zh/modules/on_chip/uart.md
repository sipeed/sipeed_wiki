---
title: UART 的使用
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: UART 的使用
---


关于 UART 详细介绍请参考[UART-API 文档](./../api_reference/machine/uart.md).

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
from machine import UART
from board import board_info
from fpioa_manager import fm

# maixduino board_info PIN10/PIN11/PIN12/PIN13 or other hardware IO 12/11/10/3
fm.register(board_info.PIN10, fm.fpioa.UART1_TX, force=True)
fm.register(board_info.PIN11, fm.fpioa.UART1_RX, force=True)
fm.register(board_info.PIN12, fm.fpioa.UART2_TX, force=True)
fm.register(board_info.PIN13, fm.fpioa.UART2_RX, force=True)

uart_A = UART(UART.UART1, 115200, 8, 0, 0, timeout=1000, read_buf_len=4096)
uart_B = UART(UART.UART2, 115200, 8, 0, 0, timeout=1000, read_buf_len=4096)

write_str = 'hello world'
for i in range(20):
    uart_A.write(write_str)
    if uart_A.any():
        read_data = uart_B.read()
        if read_data:
            read_str = read_data.decode('utf-8')
            print("string = ", read_str)
            if read_str == write_str:
                print("baudrate:115200 bits:8 parity:0 stop:0 ---check Successfully")

uart_A.deinit()
uart_B.deinit()
del uart_A
del uart_B

```
