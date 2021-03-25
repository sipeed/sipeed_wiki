模拟 I/O
=====

Maixduino 使用 K210 芯片的 PWM 模块实现模拟输出 analogWrite() 功能。 不能使用模拟输入 analogRead() 功能

Maixduino 可以在 48 个自由引脚中最多选择 12 个设置模拟输出功能。(使用硬件定时器会减少可用引脚。)

## analogWrite()

### 描述 

设置一个模拟值（PWM波）到选定引脚。 可用于点亮不同亮度的LED或改变驱动电机的速度。

### 用法

`analogWrite(pin, value)`

### 参数

`pin`: 要设置的引脚。允许的数据类型: `int`。
`value`: 占空比，取值 0 - 255 . 允许的数据类型: `int`。

### 返回值

无

### 注意事项

使用 Ticker 库或者硬件定时器可能会和 PWM 产生冲突。

-----

## analogWriteResolution()

### 描述

`analogWriteResolution()` 是 Maixduino 的扩展 API 。

`analogWriteResolution()` 用于设置 `analogWrite()` 的精度. 默认为 8 位 (取值范围 0-255)。


通过将精度设置为 12 位,  `analogWrite()` 的取值范围可变为 0 - 4095 。

### 用法

`analogWriteResolution(bits)`

### 参数

`bits`: 确定analogWrite（）函数中使用的值的分辨率（以位为单位）。该值的范围为1到32。

### 返回值

无

### 注意事项


通过调整PWM占空比可能不会导致显着的精度变化。

### 示例代码

### 示例代码 Maix Bit, Maix Dock, Maix Go

```
int led1 = 12; // LED_BLUE
int led2 = 13; // LED_GREEN | LED_BUILTIN
int led3 = 14; // LED_RED

void setup()
{
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
}

void setColor(int red, int green, int blue)
{
  analogWrite(led1, 255-blue);
  analogWrite(led2, 255-green);
  analogWrite(led3, 255-red);
}

void loop()
{
  int i, j;
  for (i=0, j=255; i<256; i++)
  {
    setColor(i, j, 0);
    delay(4);
    j--;
  }
  delay(100);           
  for (i=0, j=255; i<256; i++)
  {
    setColor(j, 0, i);
    delay(4);
    j--;
  }
  delay(100);           
  for (i=0, j=255; i<256; i++)
  {
    setColor(0, i, j);
    delay(4);
    j--;
  }
  delay(100);        
}
```

### 示例代码 Maixduino

```
int led1 = 1; // LED_BUILTIN

void setup()
{
  pinMode(led1, OUTPUT);
}

void setColor(int value)
{
  analogWrite(led1, 255-value);
}

void loop()
{
  int i;
  for (i=0; i<256; i++)
  {
    setColor(i);
    delay(4);
  }
  delay(100);        
}
```
