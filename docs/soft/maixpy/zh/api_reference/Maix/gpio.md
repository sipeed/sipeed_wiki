---
title: GPIO
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: GPIO
---


General Purpose Input Output （通用输入/输出）简称为 GPIO，或总线扩展器。

K210上有高速 GPIO(GPIOHS) 和通用 GPIO
在 K210 上， GPIO 有一下特征：
* 高速 GPIO：

  高速 GPIO 为 GPIOHS，共 32 个。具有如下特点：
  * 可配置输入输出信号
  * 每个 IO 具有独立中断源
  * 中断支持边沿触发和电平触发
  * 每个 IO 可以分配到 FPIOA 上 48 个管脚之一
  * 可配置上下拉，或者高阻

* 通用 GPIO：

    通用 GPIO 共 8 个，具有如下特点:
    * 8 个 IO 使用一个中断源
    * 可配置输入输出信号
    * 可配置触发 IO 总中断，边沿触发和电平触发
    * 每个 IO 可以分配到 FPIOA 上 48 个管脚之一


**注意**:

一下 GPIOHS 默认已经被使用， 程序中如非必要尽量不要使用：

| GPIOHS | 功能|
| ------ | --- |
| GPIOHS31 | LCD_DC      |
| GPIOHS30 | LCD_RST     |
| GPIOHS29 | SD_CS       |
| GPIOHS28 | MIC_LED_CLK |
| GPIOHS27 | MIC_LED_DATA |



## 构造函数

```python
class GPIO(ID, MODE, PULL, VALUE)
```

通过指定的参数新建一个 SPI 对象

### 参数

* `ID`： 使用的 GPIO 引脚(一定要使用 GPIO 里带的常量来指定)

* `MODE`： GPIO模式

  • GPIO.IN就是输入模式

  • GPIO.OUT就是输出模式

* `PULL`： GPIO上下拉模式

  • GPIO.PULL_UP 上拉

  ​• GPIO.PULL_DOWN 下拉

  ​• GPIO.PULL_NONE  即不上拉也不下拉


## 方法


### value

修改/读取 GPIO 引脚状态

```python
GPIO.value([value])
```

#### 参数

* `[value]`： 可选参数，如果此参数不为空，则返回当前 GPIO 引脚状态


#### 返回值

如果 `[value]` 参数不为空，则返回当前 GPIO 引脚状态


### irq

配置一个中断处理程序，当 `pin` 的触发源处于活动状态时调用它。如果管脚模式为 pin.in，则触发源是管脚上的外部值。

```python
GPIO.irq(CALLBACK_FUNC,TRIGGER_CONDITION,GPIO.WAKEUP_NOT_SUPPORT,PRORITY)
```

#### 参数


* `CALLBACK_FUNC`：中断回调函数，当中断触发的时候被调用，一个入口函数 `pin_num`

  ​• PIN_NUM 返回的是触发中断的 GPIO 引脚号(只有GPIOHS支持中断，所以这里的引脚号也是GPIOHS的引脚号)

* `TRIGGER_CONDITION`：GPIO 引脚的中断触发模式

  ​• GPIO.IRQ_RISING 上升沿触发

  ​• GPIO.IRQ_FALLING 下降沿触发

  ​• GPIO.IRQ_BOTH  上升沿和下降沿都触发


#### 返回值

无

### disirq

关闭中断

```python
GPIO.disirq()
```

#### 参数

无

#### 返回值

无

### mode

设置 GPIO 输入输出模式

```python
GPIO.mode(MODE)
```

#### 参数

* MODE

  • `GPIO.IN` 输入模式

  • `GPIO.PULL_UP` 上拉输入模式
  
  • `GPIO.PULL_DOWN` 下拉输入模式

  • `GPIO.OUT` 输出模式

#### 返回值

无

## 常量

* `GPIO0`: GPIO0
* `GPIO1`: GPIO1
* `GPIO2`: GPIO2
* `GPIO3`: GPIO3
* `GPIO4`: GPIO4
* `GPIO5`: GPIO5
* `GPIO6`: GPIO6
* `GPIO7`: GPIO7
* `GPIOHS0`: GPIOHS0
* `GPIOHS1`: GPIOHS1
* `GPIOHS2`: GPIOHS2
* `GPIOHS3`: GPIOHS3
* `GPIOHS4`: GPIOHS4
* `GPIOHS5`: GPIOHS5
* `GPIOHS6`: GPIOHS6
* `GPIOHS7`: GPIOHS7
* `GPIOHS8`: GPIOHS8
* `GPIOHS9`: GPIOHS9
* `GPIOHS10`: GPIOHS10
* `GPIOHS11`: GPIOHS11
* `GPIOHS12`: GPIOHS12
* `GPIOHS13`: GPIOHS13
* `GPIOHS14`: GPIOHS14
* `GPIOHS15`: GPIOHS15
* `GPIOHS16`: GPIOHS16
* `GPIOHS17`: GPIOHS17
* `GPIOHS18`: GPIOHS18
* `GPIOHS19`: GPIOHS19
* `GPIOHS20`: GPIOHS20
* `GPIOHS21`: GPIOHS21
* `GPIOHS22`: GPIOHS22
* `GPIOHS23`: GPIOHS23
* `GPIOHS24`: GPIOHS24
* `GPIOHS25`: GPIOHS25
* `GPIOHS26`: GPIOHS26
* `GPIOHS27`: GPIOHS27
* `GPIOHS28`: GPIOHS28
* `GPIOHS29`: GPIOHS29
* `GPIOHS30`: GPIOHS30
* `GPIOHS31`: GPIOHS31
* `GPIO.IN`: 输入模式
* `GPIO.OUT`: 输出模式
* `GPIO.PULL_UP`: 上拉
* `GPIO.PULL_DOWN`: 下拉
* `GPIO.PULL_NONE`: 即不上拉也不下拉
* `GPIO.IRQ_RISING`: 上升沿触发
* `GPIO.IRQ_FALLING`:下降沿触发
* `GPIO.IRQ_BOTH`: 上升沿和下降沿都触发


### DEMO1: 点亮 LED

> `board_info` 与板卡相关，不同板卡配置不同，使用前需要[手动配置](../builtin_py/board_info.md)。

```python
import utime
from Maix import GPIO
from board import board_info
from fpioa_manager import fm

fm.register(board_info.LED_R,fm.fpioa.GPIO0)
led_r=GPIO(GPIO.GPIO0,GPIO.OUT)
utime.sleep_ms(500)
led_r.value()
fm.unregister(board_info.LED_R)
```

### DEMO2: 按键按下点亮 LED

> `board_info` 与板卡相关，不同板卡配置不同，使用前需要[手动配置](../builtin_py/board_info.md)。

```python
import utime
from Maix import GPIO
from board import board_info
from fpioa_manager import fm

fm.register(board_info.LED_R,fm.fpioa.GPIO0)
led_b = GPIO(GPIO.GPIO0,GPIO.OUT)
led_b.value(1)

fm.register(board_info.BOOT_KEY, fm.fpioa.GPIOHS1)
key = GPIO(GPIO.GPIOHS1, GPIO.IN)

utime.sleep_ms(100)
while True:
    if key.value() == 0: # 等待按键按下
        led_b.value(0)
        utime.sleep_ms(1000)
        break
    utime.sleep_ms(10)


led_b.value(1)

fm.unregister(board_info.LED_R)
fm.unregister(board_info.BOOT_KEY)
```

### DEMO3: 在 3 秒内等待按键触发中断

> `board_info` 与板卡相关，不同板卡配置不同，使用前需要[手动配置](../builtin_py/board_info.md)。

```python
import utime
from Maix import GPIO
from board import board_info
from fpioa_manager import fm

def test_irq(pin_num):
    print("key", pin_num, "\n")

fm.register(board_info.BOOT_KEY, fm.fpioa.GPIOHS0)
key = GPIO(GPIO.GPIOHS0, GPIO.IN, GPIO.PULL_NONE)

utime.sleep_ms(100)
key.irq(test_irq, GPIO.IRQ_BOTH, GPIO.WAKEUP_NOT_SUPPORT,7)
utime.sleep_ms(3000) # 在 3 秒内等待触发

key.disirq() # 禁用中断
fm.unregister(board_info.BOOT_KEY)
```
