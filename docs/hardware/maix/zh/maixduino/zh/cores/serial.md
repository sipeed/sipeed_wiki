Serial
=====

In Maixduino, there are two types of serial devices, `UARTHSClass` and `UARTClass`.
The `Serial` corresponds to the `UARTHSClass`, and the remaining `Serial1`, `Serial2`, and `Serial3` are `UARTClass`. `Serial` uses the default pin as **4** (RX), **5** (TX).
So you can use it in the serial monitor on your computer.The default pins for the other three global serial ports are **6**(RX), and **7**(TX) (they are connected to the WiFi module),To use them correctly, set different pins for them in `begin()`.

## Functions

The operation of the serial port is exactly the same as that of Arduino. You can find more information on the [Arduino website](https://www.arduino.cc/reference/en/language/functions/communication/serial/).

`if(Serial)`

`available()`

`availableForWrite()`

`begin()`

`end()`

`find()`

`findUntil()`

`flush()`

`parseFloat()`

`parseInt()`

`peek()`

`print()`

`println()`

`read()`

`readBytes()`

`readBytesUntil()`

`readString()`

`readStringUntil()`

`setTimeout()`

`write()`

`serialEvent()`

----
## Serial port settings

Serial.begin(BaudRate, RX , TX )

### Notes

For `platform.io` change the serial monitor baudrate in `platform.ini`.

```
; serial monitor baudrate
monitor_speed = 115200
```

----
## Serial.println()

### 描述

Prints data to the serial port as human-readable ASCII text followed by a carriage return character (ASCII 13, or '\r') and a newline character (ASCII 10, or '\n'). This command takes the same forms as `Serial.print()`.

### 用法

`Serial.println(val)`

`Serial.println(val, format)`

### 参数

`Serial`: serial port object.

`val`: the value to print. Allowed data types: any data type.

`format`: specifies the number base (for integral data types) or number of decimal places (for floating point types).

### 返回值

`println()` returns the number of bytes written, though reading that number is optional. Data type: `size_t`.

### 示例代码
```
#include <Arduino.h>

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  Serial.println("Hello world");
  delay(2000);
}
```
----

## Serial Monitor in `platform.io`
```
-- Available ports:
---  1: /dev/ttyUSB0         'USB Debugger'
---  2: /dev/ttyUSB1         'USB Debugger'
--- Enter port index or full name: 2
```
