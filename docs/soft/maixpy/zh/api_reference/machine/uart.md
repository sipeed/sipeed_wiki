---
title: machine.UART
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy  machine.UART
---


uart 模块主要用于驱动开发板上的异步串口，可以自由对 uart 进行配置。k210 一共有3个 uart，每个 uart 可以进行自由的引脚映射。

## 构造

### 引脚映射

在使用 uart 前，我们需要使用 fm 来对芯片引脚进行映射和管理。如下所示，将 PIN10 设置为 uart2 的发送引脚，PIN11 设置为 uart2 的接收引脚
```
fm.register(board_info.PIN10,fm.fpioa.UART2_TX)
fm.register(board_info.PIN11,fm.fpioa.UART2_RX)
```

### 构造函数

```
uart = machine.UART(uart,baudrate,bits,parity,stop,timeout, read_buf_len)
```

通过指定的参数新建一个 UART 对象

#### 参数

* `uart` UART 号，使用指定的 UART，可以通过 `machine.UART.` 按tab键来补全
* `baudrate`: UART 波特率
* `bits`: UART 数据宽度，支持 `5/6/7/8` (默认的 REPL 使用的串口（UARTHS）只支持 8 位模式)， 默认 `8`
* `parity`: 奇偶校验位，支持 `None`, `machine.UART.PARITY_ODD`,  `machine.UART.PARITY_EVEN` （默认的 REPL 使用的串口（UARTHS）只支持 None）， 默认 `None`
* `stop`: 停止位， 支持 `1`， `1.5`, `2`， 默认 `1`
* `timeout`: 串口接收超时时间
* `read_buf_len`： 串口接收缓冲，串口通过中断来接收数据，如果缓冲满了，将自动停止数据接收

#### 返回值

* UART对象

## 方法

### init

用于初始化 uart，一般在构造对象时已经初始化，这里用在重新初始化 uart
```
uart.init(baudrate,bits,parity,stop,timeout, read_buf_len)
```

#### 参数

同构造函数，但不需要第一个UART号

#### 返回值

无

### read

用于读取串口缓冲中的数据

```
uart.read(num)
```
#### 参数

* `num`: 读取字节的数量，一般填入缓冲大小，如果缓冲中数据的数量没有 `num` 大，那么将只返回缓冲中剩余的数据

#### 返回值

* `bytes`类型的数据

### readline

用于读取串口缓冲数据的一行

```
uart.readline(num)
```
* `num`: 读取行的数量

#### 返回值

*`bytes`类型的数据


### write

用于使用串口发送数据

```
uart.write(buf)
```
#### 参数

* `buf`: 需要发送到数据

#### 返回值

* 写入的数据量

### deinit

注销 UART 硬件，释放占用的资源

```
uart.deinit()
```

#### 参数

无

#### 返回值

无

### repl_uart()

获取用于 REPL 的串口对象

#### 返回值

用于 REPL 的串口对象， 默认初始化位 `115200 8 N 1`


## 例程


### 例程 1

在运行里程之前，请确认 `PIN4` 已经连接到 `PIN10`， `PIN3` 已经连接到 `PIN11`

运行程序后，可以在终端看到 `baudrate:115200 bits:8 parity:0 stop:0 ---check Successfully` 的打印信息

> 以下例程对于Bit开发是不能直接进行使用，需要修改对应可用的PIN脚，可自行尝试

```python
from machine import UART
from board import board_info
from fpioa_manager import fm

# maixduino board_info PIN10/PIN11/PIN12/PIN13 or other hardware IO 10/11/4/3
fm.register(board_info.PIN10, fm.fpioa.UART1_TX, force=True)
fm.register(board_info.PIN11, fm.fpioa.UART1_RX, force=True)
fm.register(board_info.PIN3, fm.fpioa.UART2_TX, force=True)
fm.register(board_info.PIN4, fm.fpioa.UART2_RX, force=True)

uart_A = UART(UART.UART1, 115200, 8, 0, 0, timeout=1000, read_buf_len=4096)
uart_B = UART(UART.UART2, 115200, 8, 0, 0, timeout=1000, read_buf_len=4096)

write_str = 'hello world'
for i in range(20):
    uart_A.write(write_str)

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

### 例程 2

AT模块串口
> 以下例程对于Bit开发是不能直接进行使用，需要修改对应可用的PIN脚，可自行尝试


```python
fm.register(board_info.WIFI_RX,fm.fpioa.UART2_TX)
fm.register(board_info.WIFI_TX,fm.fpioa.UART2_RX)
uart = machine.UART(machine.UART.UART2,115200,timeout=1000, read_buf_len=4096)
```
### 例程 3

修改 REPL 串口波特率
> 以下例程对于Bit开发是不能直接进行使用，需要修改对应可用的PIN脚，可自行尝试


```python
from machine import UART
repl = UART.repl_uart()
repl.init(1500000, 8, None, 1, read_buf_len=2048)
```

### 例程 3

修改 REPL 串口
> 以下例程对于Bit开发是不能直接进行使用，需要修改对应可用的PIN脚，可自行尝试


```python
from machine import UART

fm.register(board_info.PIN15,fm.fpioa.UART1_TX)
fm.register(board_info.PIN17,fm.fpioa.UART1_RX)
uart = machine.UART(UART.UART1, 115200)
UART.set_repl_uart(uart)
```
