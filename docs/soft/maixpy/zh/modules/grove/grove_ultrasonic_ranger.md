---
title: Grove - Ultrasonic Ranger(超声波测距)
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: Grove - Ultrasonic Ranger(超声波测距)
---


<div class="grove_pic">
<img src="../../../assets/hardware/module_grove/ultrasonic.jpg">
</div>

Grove-Ultrasonic Ranger 是一个非接触式测距模块，工作频率为 40KHz。Grove_Ultrasonic_Ranger 的触发和回波信号共享1个 SIG 引脚。  

## 参数

|项目       |值         |
|:--------|:-----------|   
|工作电压 	|3.2〜5.2V          | 
|工作电流 	|8ma               |    
|超声波频率 |	40kHz           |      
|测量范围 	|2-350cm           |    
|解析度 	 |   1cm            |     
|输出量 	 |   PWM           |     
|尺寸 	  |  50mm x 25mm x 16mm|
|重量 	  |  13g             |   
|测量角度 	|15°               |     
|工作温度 	|-10〜60°C           |    
|触发信号 	|10uS TTL          |      
|回声信号 	|TTL               |

## 使用方法

MaixPy 已经在 modules 模块中实现有 ultrasonic 驱动。

* 导入 ultrasonic 类并创建对象

```python
from modules import ultrasonic
device = ultrasonic(fm.fpioa.GPIOHS0)
```

* 获取当前测量距离(cm)

```python
distance = device.measure(unit = ultrasonic.UNIT_CM, timeout = 3000000)
```

## 例程

[Grove - Ultrasonic Ranger 例程](https://github.com/sipeed/MaixPy_scripts/tree/master/modules/grove/ultrasonic)

## 更多

* API 手册: [modules.ultrasonic](../../api_reference/extend/ultrasonic.md)

* 模块详情: [Seeed Grove-Ultrasonic_Ranger](https://wiki.seeedstudio.com/Grove-Ultrasonic_Ranger/)