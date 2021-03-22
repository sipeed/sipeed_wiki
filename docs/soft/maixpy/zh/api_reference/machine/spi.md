---
title: machine.SPI
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: machine.SPI
---


SPI（Serial Peripheral Interface） 是一个同步串行协议，由主机和从机组成。

标准4线模式由 SCK（SCLK）， CS（片选）， MOSI， MISO 4条线连接主从机

在 K210 上， SPI 有一下特征：

* 共有 4 个 SPI 设备， 其中 SPI0 、SPI1、 SPI3 只能工作在主机模式下， SPI2 只能工作在从机模式时下， 在 MaixPy 上， SPI3 已经用来连接了 SPI Flash 作为保留硬件资源。
* 支持 1/2/4/8 线全双工模式， 在 MaixPy 中， 目前只支持标准（摩托罗拉）4线全双工模式（即 SCK， MOSI， MISO， CS 四个引脚）
* 最高传输速率 45M：1/2主频，约 200Mbps
* 支持 DMA
* 4个可配置任意引脚的硬件片选



## 构造函数

```python
spi = machine.SPI(id, mode=SPI.MODE_MASTER, baudrate=500000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck, mosi, miso, cs0, cs1, cs2, cs3)
```

通过指定的参数新建一个 SPI 对象

### 参数

* `id`： SPI ID， 取值范围[0,4]， 目前只支持 0 和 1 、4 ， 并且只能是主机模式， 2 只能作为从机，目前未实现， 3 保留, 4 使用软模拟 SPI（.SPI_SOFT）
* `mode`： SPI  模式， `MODE_MASTER` 或者`MODE_MASTER_2`或者`MODE_MASTER_4`或者`MODE_MASTER_8`或者`MODE_SLAVE`， 目前只支持`MODE_MASTER`
* `baudrate`： SPI 波特率（频率）
* `polarity`： 极性， 取值为 0 或 1， 表示 SPI 在空闲时的极性， 0 代表低电平， 1 代表高电平
* `phase`： 相， 取值位 0 或 1， 表示在时钟的第一个还是第二个跳变沿采集数据， 0 表示第一个， 1 表示第二个
* `bits`： 数据宽度， 默认值为8， 取值范围[4,32]
* `firstbit`： 指定传输采用 MSB 还是 LSB 顺序传输， 默认 `SPI.MSB`
* `sck`: SCK（时钟）引脚， 可直接传引脚数值，取值范围：[0,47]。 可以不设置，而是使用 [fm](../builtin_py/fm.md) 统一管理引脚映射。
* `mosi`: MOSI（主机输出） 引脚， 可直接传引脚数值，取值范围：[0,47]。 可以不设置，而是使用 [fm](../builtin_py/fm.md) 统一管理引脚映射。
* `miso`: MISO（主机输入） 引脚， 可直接传引脚数值，取值范围：[0,47]。 可以不设置，而是使用 [fm](../builtin_py/fm.md) 统一管理引脚映射。
* `cs0`: CS0（片选） 引脚， 可直接传引脚数值，取值范围：[0,47]。 可以不设置，而是使用 [fm](../builtin_py/fm.md) 统一管理引脚映射。
* `cs1`: CS1（片选） 引脚， 可直接传引脚数值，取值范围：[0,47]。 可以不设置，而是使用 [fm](../builtin_py/fm.md) 统一管理引脚映射。
* `cs2`: CS2（片选） 引脚， 可直接传引脚数值，取值范围：[0,47]。 可以不设置，而是使用 [fm](../builtin_py/fm.md) 统一管理引脚映射。
* `cs3`: CS3（片选） 引脚， 可直接传引脚数值，取值范围：[0,47]。 可以不设置，而是使用 [fm](../builtin_py/fm.md) 统一管理引脚映射。
* `d0~d7`： 数据引脚， 在非标准4线模式中使用，目前保留。 可以不设置，而是使用 [fm](../builtin_py/fm.md) 统一管理引脚映射。

## 方法

### init

类似构造函数

```python
spi.init(id, mode=SPI.MODE_MASTER, baudrate=500000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck, mosi, miso, cs0)
```

#### 参数

与构造函数相同


#### 返回值

无


### read

读取数据

```python
spi.read(nbytes, write=0x00, cs=SPI.CS0)
```

#### 参数

* `nbytes`： 需要读取的长度
* `cs`： 选择片选引脚， 在初始化时已经为`cs0`~`cs3`设置了引脚，这里只需要选择`SPI.CS0`~`SPI.CS3`即可，默认为`SPI.CS0`
* `write`： 因为是全双工，设置在读取时`MOSI`引脚的值，默认为`0x00`，即始终为低电平


#### 返回值

`bytes`类型的数据


### readinto

读取数据，并放到指定变量中

```python
spi.readinto(buf, write=0x00, cs=SPI.CS0)
```

#### 参数


* `buf`： `bytearray` 类型， 定义了长度，读取完成后数据保存在此
* `cs`： 选择片选引脚， 在初始化时已经为`cs0`~`cs3`设置了引脚，这里只需要选择`SPI.CS0`~`SPI.CS3`即可，默认为`SPI.CS0`
* `write`： 因为是全双工，设置在读取时`MOSI`引脚的值，默认为`0x00`，即始终为低电平


#### 返回值

无

### write

发送数据

```python
spi.write(buf, cs=SPI.CS0)
```

#### 参数

* `buf`： `bytearray` 类型， 定义了数据及长度
* `cs`： 选择片选引脚， 在初始化时已经为`cs0`~`cs3`设置了引脚，这里只需要选择`SPI.CS0`~`SPI.CS3`即可，默认为`SPI.CS0`

#### 返回值

无

### write_readinto

发送数据，同时读取数据到变量，即全双工

```python
spi.write(write_buf, read_buf, cs=SPI.CS0)
```

#### 参数

* `write_buf`： `bytearray` 类型， 定义了需要发送的数据及长度
* `read_buf`： `bytearray` 类型， 定义了接收数据存放的位置
* `cs`： 选择片选引脚， 在初始化时已经为`cs0`~`cs3`设置了引脚，这里只需要选择`SPI.CS0`~`SPI.CS3`即可，默认为`SPI.CS0`

#### 返回值

无

### deinit/\__del\__

注销 SPI，释放硬件，关闭 SPI 时钟

```python
spi.deinit()
```

#### 参数

无

#### 返回值

无

#### 例子

```python
spi.deinit()
```
或者
```
del spi
```

## 常量

* `SPI0`: SPI 0
* `SPI1`: SPI 1
* `SPI2`: SPI 2
* `MODE_MASTER`: 作为主机模式
* `MODE_MASTER_2`: 作为主机模式
* `MODE_MASTER_4`: 作为主机模式
* `MODE_MASTER_8`: 作为主机模式
* `MODE_SLAVE`: 作为从机模式
* `MSB`： MSB， 即先发送高位或高字节
* `LSB`： LSB， 即先发送低位或者低字节
* `CS0`： 片选0
* `CS1`： 片选1
* `CS2`： 片选2
* `CS3`： 片选3


## 例程

### 例程 1： 基本读写

```python
from machine import SPI

spi = SPI(SPI.SPI1, mode=SPI.MODE_MASTER, baudrate=10000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=28, mosi=29, miso=30, cs0=27)
w = b'1234'
r = bytearray(4)
spi.write(w)
spi.write(w, cs=SPI.CS0)
spi.write_readinto(w, r)
spi.read(5, write=0x00)
spi.readinto(r, write=0x00)
```
