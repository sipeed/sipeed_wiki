---
title: Grove-Chainable RGB LED (Linkable LED lights)
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: Grove-Chainable RGB LED (linkable LED lights)
---


<div class="grove_pic">
<img src="../../../assets/hardware/module_grove/grove_rgb_led.jpg">
</div>

Grove-Chainable RGB LED uses 2-wire transmission (data and clock) to communicate with the MCU. This 2-wire transmission can be used to cascade multiple modules. Built-in clock regeneration can extend the transmission distance. The Grove module is suitable for any project based on colored LEDs.

## Parameters

|Item|Value|
|----|----|
|Working voltage|5V |
|Electric current|20mA|
|Communication protocol|serial communication|


## Instructions

* Import the RGB_LED class in the routine warehouse and create an RGB_LED object

```python
from RGB_LED import RGB_LED
led = RGB_LED(clk_pin, data_pin, led_num, clk_gpiohs_num, data_gpiohs_num, True)
```

* Set the color of a light, the color value is rgb format

```python
for i in range(led_num):
    led.set_RGB(i, r, g, b)
```

## Routine

[Grove-Chainable RGB LED example](https://github.com/sipeed/MaixPy_scripts/tree/master/modules/grove/chainable_RGB_LED)

## More

Module details: [Seeed Grove-Chainable RGB LED](https://wiki.seeedstudio.com/Grove-Chainable_RGB_LED/)
