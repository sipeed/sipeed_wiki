---
title: Grove - RGB LED Ring(LED 灯条)
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: Grove - RGB LED Ring(LED 灯条)
---


<div class="grove_pic">
<img src="../../../assets/hardware/module_grove/grove_led_ring.jpg">
</div>

Grove-RGB LED 环采用3535尺寸的 LED，LED 内嵌有嵌入式微控制器。每个 WS2813 驱动芯片均可寻址并且位于 LED 内部。每个 LED 都有恒定电流驱动，因此即使电压变化，颜色也将非常一致。

## 参数

|项目 |	值  |
|:---|:---|
|功率 | 3.3V/5V|
|静态电流 |0.7mA/LED|
|RGB通道恒流 |16mA/LED|
|刷新频率  |2Hz|
|重置时间  |>280μs|
|工作温度  |-25～85℃|
|贮存温度  |-40～105℃| 

## 使用方法

MaixPy 已经在 modules 模块中实现有 WS2812 驱动。

* 创建 ws2812 对象，只需要单根信号线即可

```python
from modules import ws2812
led_io, led_num = 24, 24
ws = ws2812(led_io, led_num)
```

* 设置某个灯的颜色并显示

```python
for i in range(led_num):
    ws.set_led(i, (0, 0, 0))
ws.display()
```

## 例程

[Grove - RGB LED Ring 例程](https://github.com/sipeed/MaixPy_scripts/blob/master/modules/grove/ws2812/ws2812.py)

## 更多

* API 手册: [modules.ws2812](../../api_reference/extend/ws2812.md)

* 模块详情: [Seeed Grove-LED_ring](https://wiki.seeedstudio.com/Grove-LED_ring/)