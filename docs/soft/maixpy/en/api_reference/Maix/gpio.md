---
title: GPIO
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: GPIO
---


General Purpose Input Output (General Purpose Input/Output) is abbreviated as GPIO, or bus extender.

There are high-speed GPIO (GPIOHS) and general-purpose GPIO on K210
On K210, GPIO has the following characteristics:
* High-speed GPIO:

  The high-speed GPIO is GPIOHS, 32 in total. It has the following characteristics:
  * Configurable input and output signals
  * Each IO has an independent interrupt source
  * Interrupt supports edge trigger and level trigger
  * Each IO can be assigned to one of the 48 pins on FPIOA
  * Configurable up and down

* General GPIO:

    There are 8 general-purpose GPIOs with the following characteristics:
    * 8 IOs use one interrupt source
    * Configurable input and output signals
    * Configurable trigger IO total interrupt, edge trigger and level trigger
    * Each IO can be assigned to one of the 48 pins on FPIOA


**note**:

The following GPIOHS has been used by default, try not to use it unless necessary in the program:

| GPIOHS | Function |
| --- | --- |
| GPIOHS31 | LCD_DC |
| GPIOHS30 | LCD_RST |
| GPIOHS29 | SD_CS |
| GPIOHS28 | MIC_LED_CLK |
| GPIOHS27 | MIC_LED_DATA |



## Constructor

```python
class GPIO(ID, MODE, PULL, VALUE)
```

Create a new SPI object with the specified parameters

### Parameters

* `ID`: the used GPIO pin (must use the constant in GPIO to specify)

* `MODE`: GPIO mode

  • GPIO.IN is the input mode

  • GPIO.OUT is the output mode

* `PULL`: GPIO pull-up mode

  • GPIO.PULL_UP pull up

  ​• GPIO.PULL_DOWN pull down

  ​• GPIO.PULL_NONE neither pull up nor pull down


## Method


### value

Modify/read GPIO pin status

```python
GPIO.value([value])
```

#### Parameters

* `[value]`: Optional parameter, if this parameter is not empty, it returns the current GPIO pin status


#### return value

If the `[value]` parameter is not empty, return the current GPIO pin status


### irq

Configure an interrupt handler to be called when the trigger source of `pin` is active. If the pin mode is pin.in, the trigger source is the external value on the pin.

```python
GPIO.irq(CALLBACK_FUNC,TRIGGER_CONDITION,GPIO.WAKEUP_NOT_SUPPORT,PRORITY)
```

#### Parameters


* `CALLBACK_FUNC`: Interrupt callback function, which is called when the interrupt is triggered, an entry function `pin_num`

  ​• PIN_NUM returns the GPIO pin number that triggered the interrupt (only GPIOHS supports interrupts, so the pin number here is also the pin number of GPIOHS)

* `TRIGGER_CONDITION`: Interrupt trigger mode of GPIO pin

  ​• GPIO.IRQ_RISING rising edge trigger

  ​• GPIO.IRQ_FALLING falling edge trigger

  ​• GPIO.IRQ_BOTH triggers on both rising and falling edges


#### return value

no

### disirq

Close interrupt

```python
GPIO.disirq()
```

#### Parameters

no

#### return value

no

### mode

Set GPIO input and output mode

```python
GPIO.mode(MODE)
```

#### Parameters

* MODE

  • `GPIO.IN` input mode

  • `GPIO.PULL_UP` pull-up input mode
  
  • `GPIO.PULL_DOWN` pull-down input mode

  • `GPIO.OUT` output mode

#### return value

no

## Constant

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
* `GPIO.IN`: input mode
* `GPIO.OUT`: output mode
* `GPIO.PULL_UP`: pull up
* `GPIO.PULL_DOWN`: pull down
* `GPIO.PULL_NONE`: neither pull up nor pull down
* `GPIO.IRQ_RISING`: rising edge trigger
* `GPIO.IRQ_FALLING`: falling edge trigger
* `GPIO.IRQ_BOTH`: trigger on both rising and falling edges


### DEMO1: Turn on the LED

> `board_info` is related to the board, and different board configurations are different. [Manual configuration](../builtin_py/board_info.md) is required before use.

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

### DEMO2: Press the button to light up the LED

> `board_info` is related to the board, and different board configurations are different. [Manual configuration](../builtin_py/board_info.md) is required before use.

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
    if key.value() == 0: # Wait for the button to be pressed
        led_b.value(0)
        utime.sleep_ms(1000)
        break
    utime.sleep_ms(10)


led_b.value(1)

fm.unregister(board_info.LED_R)
fm.unregister(board_info.BOOT_KEY)
```

### DEMO3: Wait for the key to trigger an interrupt within 3 seconds

> `board_info` is related to the board, and different board configurations are different. [Manual configuration](../builtin_py/board_info.md) is required before use.

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
utime.sleep_ms(3000) # Wait for the trigger within 3 seconds

key.disirq() # Disable interrupt
fm.unregister(board_info.BOOT_KEY)
```
