---
title: modules.onewire (single bus)
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: modules.onewire (single bus)
---


A single bus means that there is only a single signal line, which transmits data and clocks, and the data transmission is also bidirectional, saving IO ports.

## Construction method onewire(gpio_num)

### Parameters

* `gpio_num`: GPIO number.

### return value

* onewire object

## Instance method reset()

Reset

### return value

* bool type, whether it is successful.

## Instance method readbit()

Read one bit of data

### return value

* Int type, the data read.

## Instance method readbyte()

Read a byte

### return value

* Int type, the data read.

## Instance method readbuffer(n)

Read the number of bytes of the specified length

### Parameters

* `n`: int type, the number of bytes to be read

### return value

* bytearray type, the byte array read

## Example method writebit(bit)

Write a bit

### Parameters

* `bit`: int type, bit data to be written

## Example method writebyte(byte)

### Parameters

* `byte`: int type, byte data to be written

## Example method writebuffer(buf)

### Parameters

* `buf`: bytearray type, data to be written

## Example method select(rom_in)

Let the master specify a certain slave.

### Parameters

* `rom_in`: bytearray type, which means that the 8byte ROM data of the slave will be specified.

## Example method search(diff_in)

Search using F0H criteria

### Parameters

* `diff_in`: int type, the preferred path for the first search

### return value

* `list`: a list with elements (depth, roms), `depth` is the search depth, int type, `rom` is the device ROM code, list type.

## Example method skip()

Skip ROM, suitable for single node

## Example method depower()

Re-enable IO

## Example method crc8(data_in)

Calculate 8-bit cyclic redundancy check code

### Parameters

* `data_in`: data to be verified

### return value

* Return check code
