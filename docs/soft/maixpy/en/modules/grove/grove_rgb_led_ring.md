---
title: Grove-RGB LED Ring (LED strip)
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: Grove-RGB LED Ring (LED strip)
---


<div class="grove_pic">
<img src="../../../assets/hardware/module_grove/grove_led_ring.jpg">
</div>

The Grove-RGB LED ring uses 3535 size LEDs, and the LEDs are embedded with embedded microcontrollers. Each WS2813 driver chip can be addressed and located inside the LED. Each LED is driven by a constant current, so even if the voltage changes, the color will be very consistent.

## Parameters

|Item | Value |
| --- | --- |
|Working voltage| 3.3V/5V|
|Quiet current |0.7mA/LED|
|RGB channel constant current |16mA/LED|
|Refresh frequency |2Hz|
|Reset time |>280μs|
|Working temperature |-25～85℃|
|Storage temperature |-40～105℃|

## Instructions

MaixPy has implemented the WS2812 driver in the modules module.

* To create a ws2812 object, only a single signal line is needed

```python
from modules import ws2812
led_io, led_num = 24, 24
ws = ws2812(led_io, led_num)
```

* Set the color of a certain light and display it

```python
for i in range(led_num):
    ws.set_led(i, (0, 0, 0))
ws.display()
```

## Routine

[Grove-RGB LED Ring example](https://github.com/sipeed/MaixPy_scripts/blob/master/modules/grove/ws2812/ws2812.py)

## More

* API manual: [modules.ws2812](../../api_reference/extend/ws2812.md)

* Module details: [Seeed Grove-LED_ring](https://wiki.seeedstudio.com/Grove-LED_ring/)
