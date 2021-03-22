---
title: modules.onewire（单总线）
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: modules.onewire（单总线）
---


单总线即只有单根信号线，该线即传输数据也传输时钟，并且数据传输也为双向，节约 IO 口。

## 构造方法 onewire(gpio_num)

### 参数

* `gpio_num`：GPIO号。

### 返回值

* onewire 对象

## 实例方法 reset()

重置

### 返回值

* bool 类型，是否成功。

## 实例方法 readbit()

读取一位数据

### 返回值

* int 类型，读取到的数据。

## 实例方法 readbyte()

读取一个字节

### 返回值

* int 类型，读取到的数据。

## 实例方法 readbuffer(n)

读取指定长度的字节数

### 参数

* `n`：int 类型，需要读取的字节数

### 返回值

* bytearray 类型，读取到的字节数组

## 实例方法 writebit(bit)

写入一个位

### 参数

* `bit`：int 类型，需要写入的位数据

## 实例方法 writebyte(byte)

### 参数

* `byte`：int 类型，需要写入的字节数据

## 实例方法 writebuffer(buf)

### 参数

* `buf`：bytearray 类型，需要写入的数据

## 实例方法 select(rom_in)

让主机指定某一个从机。

### 参数

* `rom_in`：bytearray 类型，表示将指定从机的8byte的ROM数据。

## 实例方法 search(diff_in)

使用 F0H 标准搜索

### 参数

* `diff_in`：int 类型，第一次搜索优先选择的路径

### 返回值

* `list`：元素为(depth,roms)的列表，`depth` 为搜索深度,int 类型，`rom` 为器件 ROM 码，list 类型。

## 实例方法 skip()

跳过 ROM，适用于单节点

## 实例方法 depower()

重新使能IO

## 实例方法 crc8(data_in)

计算8位循环冗余校验码

### 参数

* `data_in`：需要校验的数据

### 返回值

* 返回校验码