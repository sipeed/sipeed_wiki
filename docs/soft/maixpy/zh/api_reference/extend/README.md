---
title: 外设模块
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 外设模块
---


这里的外设模块主要指片外外设（相对于片上外设，比如GPIO、I2C等），比如 `LCD`、 摄像头、 触摸屏等等

关于图像相关的暂时放在了 [机器视觉](../machine_vision/README.md) 分类， 包括以下外设模块

* [lcd](../machine_vision/lcd.md)： 显示图像
* [sensor](../machine_vision/sensor.md)： 获取摄像头数据， 取名叫 `sensor` 是兼容 `openmv`， 当然也不完全一样，请阅读文档

其它外设模块包括：

* [touchscreen](./touchscreen.md)： 触摸屏相关操作，读取触摸屏点击状态以及获取点击的坐标等
* [ws2812](./ws2812.md): WS2812单总线灯带
* [热红外温度传感器](./htpa.md)
* [超声波](./ultrasonic.md)



