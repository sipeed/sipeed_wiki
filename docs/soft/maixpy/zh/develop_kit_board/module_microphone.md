---
title: Sipeed Microphone
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: Sipeed Microphone
---


<table border="2">
    <tr>
        <th colspan=3>Sipeed 麦克风模块</th>
    </tr>
    <tr>
        <td>描述</td>
        <td>实物图</td>
        <td>说明</td>
    </tr>
        <td>
            单麦克风模块
        </td>
        <td>
            <img src="../../assets/hardware/module/microphone_taobao_400x400.jpg" height="200">
            </p>
            <a href="https://sipeed.taobao.com/">点击购买 麦克风模块</a>
        </td>
        <td>
        1.麦克风 IC: MSM261S4030H0</p>
        2.接口：6P 2.54mm 排线接口</p>
        3.供电电压：3.3V@5mA</p>
        4.模块尺寸：15.2mm*9.1mm</p>
        4.工作温度: -30℃~80℃</p>
    <tr>
    <tr>
        <td>
            单麦克风模块
        </td>
        <td>
            <img src="../../assets/hardware/module/mic_array_taobao.jpg" height="200">
            </p>
            <a href="https://sipeed.taobao.com/">点击购买 麦克风模块</a>
        </td>
        <td>
        1.麦克风 IC: 6 个 MSM261S4030H0</p>
        2.接口：10Pfpc / 10 pin 2.54mm 排线接口</p>
        3.供电电压：5V@mA</p>
        4.模块尺寸：15.2mm*9.1mm</p>
        4.工作温度: -30℃~80℃</p>
    </tr>
</table>


## Sipeed Mic-Array

Mic-Array 麦克风阵列，截止 MaixPy 版本 `MicroPython v0.5.0-218-g8053a70`, 麦克风阵列硬件上的 pin io 支持自定义配置


| No. | MaixGo(默认配置 IO) | 说明 |
| --- | --- | --- |
| MIC_D0 | 23 | --- |
| MIC_D1 | 22 | --- |
| MIC_D2 | 21 | --- |
| MIC_D3 | 20 | --- |
| MIC_WS | 19 | --- |
| MIC_SCLK | 18 | --- |
| --- | --- | --- |
| LED_DAT | 24 | SK9822 DAT |
| LED_CLK | 25 | SK9822 CLK |

### 例程

声源定位

```python
from Maix import MIC_ARRAY as mic
import lcd

lcd.init()
mic.init()#默认配置
# mic.init(i2s_d0=23, i2s_d1=22, i2s_d2=21, i2s_d3=20, i2s_ws=19, i2s_sclk=18, sk9822_dat=24, sk9822_clk=25)#可自定义配置 IO

while True:
    imga = mic.get_map()    # 获取声音源分布图像
    b = mic.get_dir(imga)   # 计算、获取声源方向
    a = mic.set_led(b,(0,0,255))# 配置 RGB LED 颜色值
    imgb = imga.resize(160,160)
    imgc = imgb.to_rainbow(1) # 将图像转换为彩虹图像
    a = lcd.display(imgc)
mic.deinit()
```

效果：

<iframe width="600" height="350"  src="//player.bilibili.com/player.html?aid=37058760&cid=65120313&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>