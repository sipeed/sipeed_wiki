数字 I/O
=====

Maixduino 支持基本的 Arduino 输入输出函数，你可以像使用其他 Arduino 开发板一样使用它们。

* Maixduino 可以自由操作不超过 32 个数字 IO 口，并可以将它们同时映射到 48 个 FPIO 上。

## digitalRead()

### 描述

    从选定的 IO 引脚读取电平, `HIGH`或者`LOW`.

### 用法

`digitalRead(pin)`

### 参数

`pin` : 你要读取的数字 IO 引脚。（0 - 47， Maixduino board 为 0 - 13*）

### 返回值

`HIGH` 或者 `LOW`

### 注意事项

* 只有在 `pinMode()` 初始化后的引脚才可以读取。
* \* Maixduino board 上的 SDA SCL 可作为普通数字引脚 14 15 号使用，BOOT key 作为 16 号引脚使用。

-----

## digitalWrite()

### 描述

将一个数字引脚设置为高电平或者低电平。

### 用法

`digitalWrite(pin, value)`

### 参数

`pin`: 引脚号

`value`: `HIGH` 或者 `LOW`

### 返回值

无

### 注意事项

* 只有在 `pinMode()` 初始化后的引脚才可以改变状态。

-----

## pinMode()

### 描述

设置一个引脚为输入或输出模式。

### 参数

`pin`: 需要设置的引脚

`mode`: `INPUT`, `OUTPUT`, `INPUT_PULLDOWN` 或者 `INPUT_PULLUP`. 

### 返回值

无

### 注意事项

在使用 `digitalRead()` 或者 `digitalWrite()` 前，必须使用此函数初始化对应引脚。

### 示例代码

```
void setup() {
  pinMode(13, OUTPUT);    // sets the digital pin 13 as output
}

void loop() {
  digitalWrite(13, HIGH); // sets the digital pin 13 on
  delay(1000);            // waits for a second
  digitalWrite(13, LOW);  // sets the digital pin 13 off
  delay(1000);            // waits for a second
}
```

将引脚13设置为与引脚16相同的值，声明为输入。

```
int ledPin = 13;  // LED connected to digital pin 13
int inPin = 16;    // pushbutton connected to digital pin 16
int val = 0;      // variable to store the read value

void setup() {
  pinMode(ledPin, OUTPUT);  // sets the digital pin 13 as output
  pinMode(inPin, INPUT);    // sets the digital pin 16 as input
}

void loop() {
  val = digitalRead(inPin);   // read the input pin
  digitalWrite(ledPin, val);  // sets the LED to the button's value
}
```

