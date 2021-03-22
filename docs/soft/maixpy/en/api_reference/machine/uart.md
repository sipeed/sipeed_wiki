---
title: machine.UART
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: machine.UART
---


The uart module is mainly used to drive the asynchronous serial port on the development board, and uart can be configured freely. There are 3 uarts in k210, and each uart can be freely mapped.

## Construction

### Pin mapping

Before using uart, we need to use fm to map and manage the chip pins. As shown below, set PIN10 as the sending pin of uart2 and PIN11 as the receiving pin of uart2
```
fm.register(board_info.PIN10,fm.fpioa.UART2_TX)
fm.register(board_info.PIN11,fm.fpioa.UART2_RX)
```

### Constructor

```
uart = machine.UART(uart,baudrate,bits,parity,stop,timeout, read_buf_len)
```

Create a new UART object with the specified parameters

#### Parameters

* `uart` UART number, use the specified UART, which can be completed by pressing the tab key in `machine.UART.`
* `baudrate`: UART baud rate
* `bits`: UART data width, support `5/6/7/8` (the default serial port used by REPL (UARTHS) only supports 8-bit mode), default `8`
* `parity`: Parity bit, support `None`, `machine.UART.PARITY_ODD`, `machine.UART.PARITY_EVEN` (the default serial port (UARTHS) used by REPL only supports None), the default is `None`
* `stop`: stop bit, support `1`, `1.5`, `2`, default `1`
* `timeout`: Serial port receiving timeout time
* `read_buf_len`: serial port receive buffer, serial port receives data through interrupt, if the buffer is full, it will automatically stop data receiving

#### return value

* UART object

## Method

### init

It is used to initialize uart, which is generally initialized when constructing the object, here is used to reinitialize uart
```
uart.init(baudrate,bits,parity,stop,timeout, read_buf_len)
```

#### Parameters

Same as constructor, but does not require the first UART number

#### return value

no

### read

Used to read the data in the serial buffer

```
uart.read(num)
```
#### Parameters

* `num`: The number of bytes read, generally fill in the buffer size, if the number of data in the buffer is not as large as `num`, then only the remaining data in the buffer will be returned

#### return value

* `bytes` type of data

### readline

Used to read one line of serial buffer data

```
uart.readline(num)
```
* `num`: the number of rows read

#### return value

*`bytes` type of data


### write

Used to send data using serial port

```
uart.write(buf)
```
#### Parameters

* `buf`: Need to send to data

#### return value

* The amount of data written

### deinit

Log off the UART hardware and release the occupied resources

```
uart.deinit()
```

#### Parameters

no

#### return value

no

### repl_uart()

Get the serial port object used for REPL

#### return value

The serial port object used for REPL, the default initialization bit is `115200 8 N 1`


## Routine


### Routine 1

Before running mileage, please make sure that `PIN15` has been connected to `PIN10`, and `PIN17` has been connected to `PIN9`

After running the program, you can see the printed information of `baudrate:115200 bits:8 parity:0 stop:0 ---check Successfully` in the terminal

```python
from fpioa_manager import fm
from machine import UART
fm.register(board_info.PIN15,fm.fpioa.UART1_TX)
fm.register(board_info.PIN17,fm.fpioa.UART1_RX)
fm.register(board_info.PIN9,fm.fpioa.UART2_TX)
fm.register(board_info.PIN10,fm.fpioa.UART2_RX)
uart_A = UART(UART.UART1, 115200, 8, None, 1, timeout=1000, read_buf_len=4096)
uart_B = UART(UART.UART2, 115200, 8, None, 1, timeout=1000, read_buf_len=4096)
write_str ='hello world'
for i in range(20):
    uart_A.write(write_str)
    read_data = uart_B.read()
    read_str = read_data.decode('utf-8')
    print("string = ",read_str)
    if read_str == write_str:
        print("baudrate:115200 bits:8 parity:None stop:1 ---check Successfully")
uart_A.deinit()
uart_B.deinit()
del uart_A
del uart_B
```

### Routine 2

AT module serial port

```python
fm.register(board_info.WIFI_RX,fm.fpioa.UART2_TX)
fm.register(board_info.WIFI_TX,fm.fpioa.UART2_RX)
uart = machine.UART(machine.UART.UART2,115200,timeout=1000, read_buf_len=4096)
```
### Routine 3

Modify the baud rate of the REPL serial port

```python
from machine import UART
repl = UART.repl_uart()
repl.init(1500000, 8, None, 1, read_buf_len=2048)
```

### Routine 3

Modify the REPL serial port

```python
from machine import UART

fm.register(board_info.PIN15,fm.fpioa.UART1_TX)
fm.register(board_info.PIN17,fm.fpioa.UART1_RX)
uart = machine.UART(UART.UART1, 115200)
UART.set_repl_uart(uart)
```
