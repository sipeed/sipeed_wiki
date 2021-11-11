---
title: MaixII M2dock I2C gpio 调试
keywords: MaixII, MaixPy3, Python, Python3, M2dock
desc: maixpy doc: MaixII M2dock gpio 调试
---

## PIN_CTL

- lichee/linux-4.9/drivers/pinctrl/sunxi/pinctrl-sun8iw19p1-r.c

- lichee/linux-4.9/drivers/pinctrl/sunxi/pinctrl-sun8iw19p1.c

![](./asserts/v831_pin_maps.png)

### V831 Dock PIN Maps

- PINCTRL_PIN(64 + (0), "P" "C" "0")
- PINCTRL_PIN(96 + (0), "P" "D" "0")
- PINCTRL_PIN(128 + (0), "P" "E" "0")
- PINCTRL_PIN(160 + (0), "P" "F" "0")
- PINCTRL_PIN(192 + (0), "P" "G" "0")
- PINCTRL_PIN(224 + (0), "P" "H" "0")
- PINCTRL_PIN(256 + (0), "P" "I" "0")

| PIN Number  | PIN      | function                                   | 设备树配置     | 功能        | 备注  |
| ----------- | -------- | ------------------------------------------ | --------- | --------- | --- |
| 238(224+14) | PH14     | SPI1_CS0TWI3_SDAPH_EINT14                  |           | State_LED |     |
| ---         | ---      |                                            |           | ---       | --- |
| 166(160+6)  | PF6      | PF_EINT6                                   |           |           |     |
|             | RST      |                                            |           |           |     |
| 199(192+7)  | PG7      | UART1_RXPG_EINT7                           |           |           |     |
| 198(192+6)  | PG6      | UART1_TXPG_EINT6                           |           |           |     |
| 236(224+12) | PH12     | JTAG_CKRMII_TXENSPI1_MOSITWI2_SDAPH_EINT12 | TWI2_SDA  |           |     |
| 235(224+11) | PH11     | JTAG_MSRMII_TXCKSPI1_CLKTWI2_SCKPH_EINT11  | TWI2_SCK  |           |     |
| 238(224+14) | PH14     | JTAG_DIMDIOSPI1_CS0TWI3_SDAPH_EINT14       |           |           |     |
| 237(224+13) | PH13     | JTAG_DOMDCSPI1_MISOTWI3_SCKPH_EINT13       |           |           |     |
| 234(224+10) | PH10     | RMII_TXD0TWI3_SDAUART0_RXPH_EINT10         |           |           |     |
|             | CPUX-RX  |                                            |           |           |     |
|             | UART0-TX | PWM_9RMII_TXD1TWI3_SCKUART0_TXPH_EINT9     |           |           |     |
| ---         | ---      |                                            |           | ---       | --- |
|             | GND      |                                            |           |           |     |
|             | 5V       |                                            |           |           |     |
| 230(224+6)  | PH6      | PWM_6RMII_RXD0TWI2_SDAUART2_RXPH_EINT6     |           |           |     |
| 231(224+7)  | PH7      | PWM_7RMII_CRS_DVUART0_TXUART2_RTSPH_EINT7  |           |           |     |
| 232(224+8)  | PH8      | PWM_8RMII_RXERUART0_RXUART2_CTSPH_EINT8    |           |           |     |
|             | GPADC0   |                                            |           |           |     |
| 224(224+0)  | PH0      | PWM_0I2S0_MCLKSPI1_CLKUART3_TXPH_EINT0     | SPI1_CLK  |           |     |
| 225(224+1)  | PH1      | PWM_1I2S0_BCLKSPI1_MOSIUART3_RXPH_EINT1    | SPI1_MOSI |           |     |
| 226(224+2)  | PH2      | PWM_2I2S0_LRCKSPI1_MISOUART3_CTSPH_EINT2   | SPI1_MISO |           |     |
| 227(224+3)  | PH3      | PWM_3I2S0_DOUTSPI1_CS0UART3_RTSPH_EINT3    | SPI1_CS0  |           |     |

## sysfs 操作 GPIO

```shell
root@sipeed:/# ls -l /sys/class/gpio
--w-------    1 root     root          4096 Dec  9 08:54 export
lrwxrwxrwx    1 root     root             0 Dec  9 08:54 gpiochip0 -> ../../devices/platform/soc/pio/gpio/gpiochip0
lrwxrwxrwx    1 root     root             0 Dec  9 08:54 gpiochip352 -> ../../devices/platform/soc/r_pio/gpio/gpiochip352
--w-------    1 root     root          4096 Dec  9 08:54 unexport
root@sipeed:/#
```

/sys/class/gpio 目录下的三种文件：

- export/unexport 文件:  `/sys/class/gpio/export`，只写，写入 GPIO 编号来向内核申请 GPIO 控制权（前提是没有内核代码申请这个 GPIO 端口）, 成功后会在目录下生成 gpioN 目录, `/sys/class/gpio/unexport` 和导出的效果相反。

- gpioN 指代具体的 gpio 引脚:  指代某个具体的 gpio 端口, 内有以下属性文件：

| Attribution | Read/Write | Value                          | Function     |
| ----------- | ---------- | ------------------------------ | ------------ |
| direction   | RW         | in,out;low,high                | 设置输入输出       |
| value       | RW         | 0,非零                           | 读取或者写入 IO 电平 |
| edge        | RW         | none , rising , falling , both | 配置中断触发方式     |
| active_low  | RW         | 0,非零                           | 设置低电平有效      |

- gpiochipN 指代 gpio 控制器:  gpiochipN 表示的就是一个 gpio_chip, 用来管理和控制一组 gpio 端口的控制器，该目录下存在以下属性文件：

| Attribution | Function                      |
| ----------- | ----------------------------- |
| base        | 和N相同，表示控制器管理的最小的端口编号。         |
| lable       | 诊断使用的标志，寄存器地址，1c20800.pinctrl |
| ngpio       | 表示控制器管理的 gpio 端口数量，A~G，224    |

### LED 测试

使用 sysfs 操作 GPIO 的例子：

```shell
ls -l /sys/class/gpio/ # show gpio
echo 238 > /sys/class/gpio/export  #export PH14(238), State_LED
ls -l /sys/class/gpio/ # show gpio
# output test
echo "out" > /sys/class/gpio/gpio238/direction # set gpio mode: direction
echo 0 > /sys/class/gpio/gpio238/value # set gpio output level: low
echo 1 > /sys/class/gpio/gpio238/value # set gpio output level: height
# input test
echo "in" > /sys/class/gpio/gpio238/direction #设置为输入
cat /sys/class/gpio/gpio192/value #读取电平

```

```bash
ll /sys/devices/platform/soc/r_pio/
```

## Python-gpiod

![](./asserts/v831_gpio.png)

```python
import gpiod
c = gpiod.chip("gpiochip1")
# pylint: disable=missing-docstring
import sys
import time
import pytest
from gpiod import chip, line, line_request

try:
    if len(sys.argv) > 2:
        LED_CHIP = sys.argv[1]
        LED_LINE_OFFSET = int(sys.argv[2])
    else:
        raise Exception()
# pylint: disable=broad-except
except Exception:
    print(
        """Usage:
    python3 -m gpiod.test.blink <chip> <line offset>"""
    )
    sys.exit()

c = chip(LED_CHIP)

print("chip name: ", c.name)
print("chip label: ", c.label)
print("number of lines: ", c.num_lines)

print()

led = c.get_line(LED_LINE_OFFSET)

print("line offset: ", led.offset)
print("line name: ", led.name)
print("line consumer: ", led.consumer)
print(
    "line direction: ",
    "input" if led.direction == line.DIRECTION_INPUT else "output",
)
print(
    "line active state: ",
    "active low" if led.active_state == line.ACTIVE_LOW else "active high",
)
print("is line used: ", led.is_used)
print("is line open drain: ", led.is_open_drain)
print("is_open_source: ", led.is_open_source)
print("is line requested: ", led.is_requested)

print("\nrequest line\n")

config = line_request()
config.consumer = "Blink"
config.request_type = line_request.DIRECTION_OUTPUT

led.request(config)

print("line consumer: ", led.consumer)
print(
    "line direction: ",
    "input" if led.direction == line.DIRECTION_INPUT else "output",
)
print(
    "line active state: ",
    "active low" if led.active_state == line.ACTIVE_LOW else "active high",
)
print("is line used: ", led.is_used)
print("is line open drain: ", led.is_open_drain)
print("is_open_source: ", led.is_open_source)
print("is line requested: ", led.is_requested)

while True:
    led.set_value(0)
    time.sleep(0.1)
    led.set_value(1)
    time.sleep(0.1)
```

```python
python test_blink.py gpiochip0 238
```
