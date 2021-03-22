---
title: Grove - Chainable RGB LED(可链接 LED 灯)
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: Grove - Chainable RGB LED(可链接 LED 灯)
---


<div class="grove_pic">
<img src="../../../assets/hardware/module_grove/grove_rgb_led.jpg">
</div>

Grove - Chainable RGB LED 使用2线传输（数据和时钟）与 MCU 通信。 这种2线传输可用于级联多个模块。 内置 clock regeneration 可延长传输距离。 该Grove模块适用于任何基于彩色LED的项目。 

## 参数

|项目|值|
|:----|:----|
|工作电压|5V |
|工作电流|20mA|
|通信协议|串行|

## 使用方法

* 导入例程仓库中的 RGB_LED 类并创建一个 RGB_LED 对象

```python
from RGB_LED import RGB_LED
led = RGB_LED(clk_pin, data_pin, led_num, clk_gpiohs_num, data_gpiohs_num, True)
```

* 设置某个灯的颜色， 颜色值为 rgb 格式

```python
for i in range(led_num):
    led.set_RGB(i, r, g, b)
```

## 例程

[Grove - Chainable RGB LED 例程](https://github.com/sipeed/MaixPy_scripts/tree/master/modules/grove/chainable_RGB_LED)

## 更多

模块详情: [Seeed Grove - Chainable RGB LED](https://wiki.seeedstudio.com/Grove-Chainable_RGB_LED/)