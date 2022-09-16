---
title: MaixPy 文档简介
keywords: maixpy, k210, AIOT, 边缘计算, 人工智能, 深度学习
desc: maixpy  MaixPy 文档简介
---

<div class="title_pic">
    <div class="logo_maixpy">
    <img src="../assets/maixpy/maixpy.png" alt="maixpy ​​logo">
    </div>
    <span class="logo_sipeed">
    <img src="../assets/sipeed/sipeed_logo_4.svg" alt="sipeed logo">
    </span>
    <span class="logo_mpy">
    <img src="../assets/maixpy/micropython.png" alt="micropython logo">
    </span>
    </br>
</div>

## 关于 MaixPy

[**MaixPy**](https://wiki.sipeed.com/soft/maixpy/zh/index.html) 是将 [Micropython](http://micropython.org/) 移植到 [K210](https://canaan-creative.com/product/kendryteai)（一款 64 位双核带硬件 FPU、卷积加速器、FFT、Sha256 的 RISC-V CPU ） 的一个项目； [**MaixPy**](https://wiki.sipeed.com/soft/maixpy/zh/index.html) 不但支持 MCU 常规操作， 还集成了硬件加速的 `AI` 机器视觉和麦克风阵列相关的算法。相应的高达 `1TOPS` 算力核心模块却不到`￥50`， 凭借着快速开发和较低成本与其较小的体积很适合 `AIOT` 领域智能应用

> MicroPython 是基于 Python3 的语法做的一款解析器，包含了 Python3 的大多数基础语法， 主要运行在性能和内存有限的嵌入式芯片上。（注意 Micropython 不包含 Python3 的所有语法）

**MaixPy** 让我们在 K210 上编程更加简单快捷， 我们也将源代码开源在 github [点我跳转](https://github.com/sipeed/MaixPy) 上

使用 MaixPy 可以做很多有趣的事情， 具体可以 [看这里](./what_maix_do.md)

## 简洁的代码实例

比如我们需要扫描 **I2C** 总线上的设备，不需要复杂的开发环境和工程，只需要通过串口发送如下代码即可实现：

```python
from machine import I2C                          # 导入内置库

i2c = I2C(I2C.I2C0, freq=100000, scl=28, sda=29) # 定义一个I2C对象， 使用I2C0, 频率100kHz，SCL引脚是IO28, SDA 引脚是IO29
devices = i2c.scan()                             # 调用函数扫描设备
print(devices)                                   # 打印设备
```

同样，我们需要实现一个**呼吸灯**，只需要如下代码：

> `board_info` 与板卡相关，不同板卡配置不同，使用前需要[手动配置](./api_reference/builtin_py/board_info.md)。

```python
from machine import Timer,PWM
from board import board_info
import time

tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
ch = PWM(tim, freq=500000, duty=50, pin=board_info.LED_G)
duty=0
dir = True
while True:
    if dir:
        duty += 10
    else:
        duty -= 10
    if duty>100:
        duty = 100
        dir = False
    elif duty<0:
        duty = 0
        dir = True
    time.sleep(0.05)
    ch.duty(duty)
```

**实时拍照**：

```python
import sensor
import image
import lcd

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
while True:
    img=sensor.snapshot()
    lcd.display(img)
```

**AI 物体检测**:

```python
import KPU as kpu
import sensor

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))

model = kpu.load("/sd/mobilenet.kmodel")  # load model
while(True):
    img = sensor.snapshot()               # take picture by camera
    out = kpu.forward(task, img)[:]       # inference, get one-hot output
    print(max(out))                       # print max probability object ID
```
please read doc before run it!

## 这篇文档的内容

所有关于 MaixPy 的内容， 包括：
* 如何选择并得到一款合适自己的模块或者开发板
* 如何开始上手使用
* 库和接口（API）文档查询
* 详细的一步一步手把手教程
* 来自社区的分享（教程或开源项目）

**为了在学习过程中避免遇到难以解决的问题，请务必按照左边目录结构从上到下阅读，特别是写在前面的章节，不要跳过**


## 可以运行MaixPy的开发板

首先我们需要选择一款适合自己的开发板，各个型号的 MaixPy 型号请点击：[开发板与配件选购指南](./develop_kit_board/get_hardware.md)，同时目录下也有对应开发板的硬件参数和资料

要获得这些板子，可以访问Sipeed（矽速）官网[www.sipeed.com](https://www.sipeed.com/)，或者[官方淘宝店](https://sipeed.taobao.com/)

## MaixPy 源码

`MaixPy` 源码是指 运行在 `K210` 上的 `Micropython` 语法解析器， 使用 `C语言` 编写， 源码托管在 [github](https://github.com/sipeed/MaixPy), 如果只是想使用 MaixPy，不需要了解源码， 但是也欢迎给 `MaixPy` 项目一个 `star` ;

如果想参与开发 MaixPy 的内置功能，可以下载进行开发，欢迎大家提交 `PR`


本项目主要由 &copy;<a href="https://www.sipeed.com" style="color: #f14c42">Sipeed</a> Co.,Ltd. 维护， 并接受来自开源社区的贡献， 具体贡献这见[贡献者列表](https://github.com/sipeed/MaixPy/graphs/contributors)


## 反馈

关于本文档或者功能或者源码方面的问题，也欢迎提交issue:

* [反馈](https://github.com/sipeed/MaixPy/issues)


## 交流

有问题尽量到上面的反馈地址提交`issue`，方便留下记录，其他人也可以查阅，提交前搜索一下是否有人提过相同问题

也可以去[论坛](bbs.sipeed.com)发帖交流，方便按他人查询类似问题。

以下交流方式提供辅助：

<table role="table">
    <thead>
        <tr>
            <th>交流方式</th>
            <th>地址</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>issue</td>
            <td><a href="https://github.com/sipeed/MaixPy/issues">https://github.com/sipeed/MaixPy/issues</a></td>
        </tr>
        <tr>
            <td>BBS</td>
            <td><a href="https://bbs.sipeed.com" rel="nofollow">https://bbs.sipeed.com</a></td>
        </tr>
        <tr>
            <td>MaixPy AI QQ 交流群</td>
            <td>878189804</td>
        </tr>
        <tr>
            <td>MaixPy AI QQ 交流群(四群)</td>
            <td>256336487</td>
        </tr>
        <tr>
            <td>telgram</td>
            <td><a href="https://t.me/sipeed" rel="nofollow">https://t.me/sipeed</a></td>
        </tr>
        <tr>
            <td>E-mail(商业合作)</td>
            <td><a target="_blank" rel="noopener noreferrer" href="./../assets/sipeed/support_email.jpg"><img src="./../assets/sipeed/support_email.jpg" alt="email" style="max-width:100%;"></a></td>
        </tr>
    </tbody>
</table>

<table role="table" class="center_table">
    <thead>
        <tr>
            <th>网站导航</th>
            <th>地址</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>MaixPy</strong> 唯一官方文档官网</td>
            <td><span class="limit_width">中文站: </span><span class=""><a href="https://wiki.sipeed.com/soft/maixpy/zh/" rel="nofollow"><strong>wiki.sipeed.com</strong></a></span></td>
        </tr>
        <tr>
            <td><strong>MaixPy</strong> 例程仓库</td>
            <td><span class="limit_width">github：</span> <span class=""><a href="https://github.com/sipeed/MaixPy_scripts"><strong>github/maixpy_script</strong></a></span> <br><span class="limit_width">国内：</span><span class=""><a href="https://gitee.com/Sipeed/maixpy_scripts" rel="nofollow"><strong>gitee/maixpy_scripts</strong></a></span></td>
        </tr>
        <tr>
            <td>MaixPy 源码</td>
            <td><span class="limit_width"></span><span class=""><a href="https://github.com/sipeed/MaixPy"><strong>github: MaixPy</strong></a></span></td>
        </tr>
        <tr>
            <td>开发板资料下载</td>
            <td><span class="limit_width"></span><span class=""><a href="http://dl.sipeed.com/MAIX/HDK" rel="nofollow"><strong>dl.sipeed.com</strong></a></span></td>
        </tr>
        <tr>
            <td>Sipeed WIKI</td>
            <td><span class="limit_width"></span><span class=""><a href="https://wiki.sipeed.com" rel="nofollow"><strong>wiki.sipeed.com</strong></a></span></td>
        </tr>
    </tbody>
</table>

------------
