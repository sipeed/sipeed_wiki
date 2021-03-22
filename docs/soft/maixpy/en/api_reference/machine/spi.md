---
title: machine.SPI
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: machine.SPI
---


SPI (Serial Peripheral Interface) is a synchronous serial protocol composed of a master and a slave.

The standard 4-wire mode consists of SCK (SCLK), CS (chip select), MOSI, MISO 4 wires connected to the master and slave

On K210, SPI has the following characteristics:

* There are 4 SPI devices. SPI0, SPI1, SPI3 can only work in master mode, and SPI2 can only work in slave mode. On MaixPy, SPI3 has been used to connect SPI Flash as a reserved hardware resource.
* Support 1/2/4/8 line full duplex mode. In MaixPy, currently only supports standard (Motorola) 4-wire full duplex mode (ie SCK, MOSI, MISO, CS four pins)
* The highest transmission rate 45M: 1/2 frequency, about 200Mbps
* Support DMA
* 4 hardware chip selects that can be configured with any pin



## Constructor

```python
spi = machine.SPI(id, mode=SPI.MODE_MASTER, baudrate=500000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck, mosi, miso, cs0, cs1, cs2, cs3)
```

Create a new SPI object with the specified parameters

### Parameters

* `id`: SPI ID, value range [0,4], currently only supports 0, 1, 4, and can only be in master mode, 2 can only be used as a slave, currently not implemented, 3 reserved, 4 uses soft Simulate SPI (.SPI_SOFT)
* `mode`: SPI mode, `MODE_MASTER` or `MODE_MASTER_2` or `MODE_MASTER_4` or `MODE_MASTER_8` or `MODE_SLAVE`, currently only supports `MODE_MASTER`
* `baudrate`: SPI baud rate (frequency)
* `polarity`: Polarity, the value is 0 or 1, which means the polarity of SPI when idle, 0 represents low level, 1 represents high level
* `phase`: phase, the value bit is 0 or 1, indicating that the data is collected on the first or second edge of the clock, 0 means the first one, 1 means the second
* `bits`: data width, the default value is 8, the value range is [4,32]
* `firstbit`: Specify whether the transmission is in MSB or LSB order, the default is `SPI.MSB`
* `sck`: SCK (clock) pin, the pin value can be passed directly, the value range: [0,47]. It is not necessary to set, but use [fm](../builtin_py/fm.md) to manage pin mapping in a unified manner.
* `mosi`: MOSI (host output) pin, the pin value can be directly passed, the value range: [0,47]. It is not necessary to set, but use [fm](../builtin_py/fm.md) to manage pin mapping in a unified manner.
* `miso`: MISO (host input) pin, the pin value can be directly passed, the value range: [0,47]. It is not necessary to set, but use [fm](../builtin_py/fm.md) to manage pin mapping in a unified manner.
* `cs0`: CS0 (chip select) pin, the pin value can be directly passed, the value range: [0,47]. It is not necessary to set, but use [fm](../builtin_py/fm.md) to manage pin mapping in a unified manner.
* `cs1`: CS1 (chip select) pin, the pin value can be directly passed, the value range: [0,47]. It is not necessary to set, but use [fm](../builtin_py/fm.md) to manage pin mapping in a unified manner.
* `cs2`: CS2 (chip select) pin, the pin value can be directly passed, the value range: [0,47]. It is not necessary to set, but use [fm](../builtin_py/fm.md) to manage pin mapping in a unified manner.
* `cs3`: CS3 (chip select) pin, the pin value can be directly passed, the value range: [0,47]. It is not necessary to set, but use [fm](../builtin_py/fm.md) to manage pin mapping in a unified manner.
* `d0~d7`: data pins, used in non-standard 4-wire mode, currently reserved. It is not necessary to set, but use [fm](../builtin_py/fm.md) to manage pin mapping in a unified manner.

## Method

### init

Similar constructor

```python
spi.init(id, mode=SPI.MODE_MASTER, baudrate=500000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck, mosi, miso, cs0)
```

#### Parameters

Same as constructor


#### return value

no


### read

Read data

```python
spi.read(nbytes, write=0x00, cs=SPI.CS0)
```

#### Parameters

* `nbytes`: the length to be read
* `cs`: select the chip select pin, the pins have been set for `cs0`~`cs3` during initialization, here only need to select `SPI.CS0`~`SPI.CS3`, the default is `SPI .CS0`
* `write`: Because it is full duplex, set the value of the `MOSI` pin when reading, the default is `0x00`, that is, it is always low


#### return value

`bytes` type data


### readinto

Read the data and put it in the specified variable

```python
spi.readinto(buf, write=0x00, cs=SPI.CS0)
```

#### Parameters


* `buf`: `bytearray` type, the length is defined, the data is saved here after reading
* `cs`: select the chip select pin, the pins have been set for `cs0`~`cs3` during initialization, here only need to select `SPI.CS0`~`SPI.CS3`, the default is `SPI .CS0`
* `write`: Because it is full duplex, set the value of the `MOSI` pin when reading, the default is `0x00`, that is, it is always low


#### return value

no

### write

send data

```python
spi.write(buf, cs=SPI.CS0)
```

#### Parameters

* `buf`: `bytearray` type, which defines the data and length
* `cs`: select the chip select pin, the pins have been set for `cs0`~`cs3` during initialization, here only need to select `SPI.CS0`~`SPI.CS3`, the default is `SPI .CS0`

#### return value

no

### write_readinto

Send data and read data to variables at the same time, that is, full duplex

```python
spi.write(write_buf, read_buf, cs=SPI.CS0)
```

#### Parameters

* `write_buf`: `bytearray` type, which defines the data and length to be sent
* `read_buf`: `bytearray` type, which defines the storage location of the received data
* `cs`: select the chip select pin, the pins have been set for `cs0`~`cs3` during initialization, here only need to select `SPI.CS0`~`SPI.CS3`, the default is `SPI .CS0`

#### return value

no

### deinit/\__del\__

Log off SPI, release hardware, turn off SPI clock

```python
spi.deinit()
```

#### Parameters

no

#### return value

no

#### Examples

```python
spi.deinit()
```
or
```
del spi
```

## Constant

* `SPI0`: SPI 0
* `SPI1`: SPI 1
* `SPI2`: SPI 2
* `MODE_MASTER`: as the master mode
* `MODE_MASTER_2`: as the master mode
* `MODE_MASTER_4`: as master mode
* `MODE_MASTER_8`: as the master mode
* `MODE_SLAVE`: as a slave mode
* `MSB`: MSB, that is, send the high or high byte first
* `LSB`: LSB, that is, send the low or low byte first
* `CS0`: Chip select 0
* `CS1`: Chip Select 1
* `CS2`: Chip Select 2
* `CS3`: Chip Select 3


## Routine

### Example 1: Basic read and write

```python
from machine import SPI

spi = SPI(SPI.SPI1, mode=SPI.MODE_MASTER, baudrate=10000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=28, mosi=29, miso=30, cs0= 27)
w = b'1234'
r = bytearray(4)
spi.write(w)
spi.write(w, cs=SPI.CS0)
spi.write_readinto(w, r)
spi.read(5, write=0x00)
spi.readinto(r, write=0x00)
```
