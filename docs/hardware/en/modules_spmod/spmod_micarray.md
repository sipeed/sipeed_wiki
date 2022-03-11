# SPMOD - MicArray


## 概述

<img src="../../assets/spmod/spmod_micarray/sp_micarray.png"  width="" height="300" />

SPMOD_MicArray(麦克风阵列模块)采用 RY3708(DC-DC)升压模块

## SPMOD - MicArray 介绍

- 采用 **Sipeed-SPMOD** 接口(2.54mm * 8PIN 排针)，统一 MaixPy 开发板接口
- 将SP-MOD转至FPC，利用FPC与麦克风阵列板相连。
- 板载3.3V至5V升压DC-DC (RY3708)，轻松驱动麦克风阵列。
- 利用Grove接口控制麦克风阵列板上的LED。
- 需要配合SIPEED MICARRAY一起使用。
- 模块尺寸：35.0\*10.0\*11.2mm


###  BOOST DC-DC RY3708 模块 介绍

| 功能特点： | 参数 |
| --- | -- |
| 输出电压 | 5.1V ±0.2V |
| 外部供电电压 |	3.3V ±0.2V |
| 外部供电电流 | 视麦克风阵列板的工作情况而定，通常小于500mA |
| 工作温度范围 | -40℃ ~ 85℃ |
> 1.2MHz固定开关频率,内部4A开关电流限制,高温自动切断,集成80mΩ内部功率MOSFET



###  SPMOD_MicArray 模块引脚定义：

| 引脚序号  | 引脚名称 | 类型  | 引脚说明    |
| -------- | -------- | ---- | ---------- |
| 1 | GND | G |模块电源地 |
| 2 | D2 | I | Mic_D0 |
| 3 | D3 | I | Mic_D2 |
| 4 | D0 | I | Mic_WS |
| 5 | 3V3 | V |模块电源输入正 |
| 6 | D4 | I | Mic_D1 |
| 7 | D5 | I | Mic_D3 |
| 8 | D1 | I | Mic_BCK |
| 9 | CK | I | LED控制串行时钟引脚 (相当于I2C SCL) |
| 10 | DA | I |  LED控制串行数据引脚 (相当于I2C SDA) |

<img src="" width="300" />

## 使用例程

```python
from Maix import MIC_ARRAY as mic
import lcd

lcd.init()
mic.init()
#mic.init(i2s_d0=23, i2s_d1=22, i2s_d2=21, i2s_d3=20, i2s_ws=19, i2s_sclk=18, sk9822_dat=24, sk9822_clk=25)

while True:
    imga = mic.get_map()
    b = mic.get_dir(imga)
    a = mic.set_led(b,(0,0,255))
    imgb = imga.resize(160,160)
    imgc = imgb.to_rainbow(1)
    a = lcd.display(imgc)
mic.deinit()
```

> 需要根据自己接板子上的管脚号来进行修改mic.init()中参数

## 参考设计

- SPMOD_MicArray 尺寸图：

<img src="../../assets/spmod/spmod_micarray/sipeed_spmod_micarray.png" height="250" />

-----

## 资源链接

| 资源 | --- |
| --- | --- |
| 官网 | www.sipeed.com |
| SIPEED 官方淘宝店 |[sipeed.taobao.com](sipeed.taobao.com) |
|Github | [https://github.com/sipeed](https://github.com/sipeed) |
|BBS | [http://bbs.sipeed.com](http://bbs.sipeed.com) |
|MaixPy 文档官网 | [http://maixpy.sipeed.com](http://wiki.sipeed.com/maixpy) |
|Sipeed 模型平台 | [https://maixhub.com](https://maixhub.com) |
|SDK 相关信息 | [https://dl.sipeed.com/MAIX/SDK](https://dl.sipeed.com/MAIX/SDK) |
|HDK 相关信息 | [https://dl.sipeed.com/MAIX/HDK](https://dl.sipeed.com/MAIX/HDK) |
|E-mail(技术支持和商业合作) | [Support@sipeed.com](mailto:support@sipeed.com) |
|telgram link | https://t.me/sipeed |
|MaixPy AI QQ 交流群 | 878189804 |
|MaixPy AI QQ 交流群(二群) | 1129095405 |
