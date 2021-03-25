时间

=====

## delay()

### 描述


使程序暂停一段时间（以毫秒为单位）。 （一秒钟内有1000毫秒）。

### 用法

`delay(ms)`

### 参数

`ms`: 要暂停的毫秒数。 数据类型：`unsigned long`

### 返回值

无

## delayMicroseconds()

### 描述

使程序暂停一段小时间（以微秒为单位）。 （一秒钟内有1000000毫秒）。

### 用法

`delayMicroseconds(us)`

### 参数

`us`: 要暂停的微秒数。 数据类型：`unsigned int`

### 返回值

无

-----

## micros()

返回自Maixduino开始运行当前程序以来的微秒数。

### 用法

`time = micros()`

### 参数

无

### 返回值

返回自Maixduino开始运行当前程序以来的微秒数。 数据类型 ： `unsigned long`

-----

## millis()

### 描述


返回自Maixduino开始运行当前程序以来经过的毫秒数。大约50天后，此数字将溢出（回到零）。

### 用法

`time = millis()`

### 参数

无

### 返回值

自程序启动以来经过的毫秒数。数据类型 ：`unsigned long`

