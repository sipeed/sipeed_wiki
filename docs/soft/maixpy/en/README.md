---
title: Introduction to MaixPy documentation
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: Introduction to MaixPy documentation
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
    <br/>
</div>


<table role="table" class="center_table">
    <thead>
        <tr>
            <th>Site navigation</th>
            <th>Address</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>MaixPy</strong> The only official document official website</td>
            <td><span class="limit_width">Official website:</span> <span class=""><a href="https://maixpy.sipeed.com" rel="nofollow"><strong>maixpy. sipeed.com</strong></a></span><br><span class="limit_width">Chinese site: </span><span class=""><a href="https://cn.maixpy.sipeed.com" rel="nofollow"><strong>cn.maixpy.sipeed.com</strong></a></span>
            <br><span class="limit_width">Site on github: </span><span class=""><a href="https://en.maixpy.sipeed.com" rel="nofollow"><strong>en.maixpy.sipeed.com</strong></a></span>
            </td>
        </tr>
        <tr>
            <td><strong>MaixPy</strong> demo repository</td>
            <td><span class="limit_width">github:</span> <span class=""><a href="https://github.com/sipeed/MaixPy_scripts"><strong>github/maixpy_script </strong></a></span> <br><span class="limit_width">Domestic:</span><span class=""><a href="https://gitee.com/Sipeed/maixpy_scripts "rel="nofollow"><strong>gitee/maixpy_scripts</strong></a></span></td>
        </tr>
        <tr>
            <td>MaixPy source code</td>
            <td><span class="limit_width"></span><span class=""><a href="https://github.com/sipeed/MaixPy"><strong>github: MaixPy</strong> </a></span></td>
        </tr>
        <tr>
            <td>Hardware data download</td>
            <td><span class="limit_width"></span><span class=""><a href="http://dl.sipeed.com/MAIX/HDK" rel="nofollow"><strong> dl.sipeed.com</strong></a></span></td>
        </tr>
        <tr>
            <td>Sipeed WIKI</td>
            <td><span class="limit_width"></span><span class=""><a href="https://wiki.sipeed.com" rel="nofollow"><strong>wiki.sipeed. com</strong></a></span></td>
        </tr>
    </tbody>
</table>





## About MaixPy


[**MaixPy**](https://maixpy.sipeed.com/zh/maixpy.sipeed.com) is to port [Micropython](http://micropython.org/) to [K210](https:/ /canaan-creative.com/product/kendryteai) (a 64-bit dual-core RISC-V CPU with hardware FPU, convolution accelerator, FFT, Sha256) is a project that supports the normal operation of the MCU and integrates hardware acceleration. `AI` machine vision and microphone array, `1TOPS` computing power core module is less than `￥50`, in order to quickly develop intelligent applications in the field of `AIOT` with extremely low cost and practical size.

> MicroPython is a parser based on the grammar of Python3. It contains most of the basic grammar of Python3. It mainly runs on embedded chips with limited performance and memory. (Note that Micropython does not include all the syntax of Python3)



**MaixPy** makes programming on K210 easier and faster. We also open source the source code on [**github**](https://github.com/sipeed/MaixPy)

There are many interesting things you can do with MaixPy. Specifically, you can <a href= "what_maix_do.html" target="_blank">look here</a>

## Concise code example

For example, if we need to scan the devices on the **I2C** bus, there is no need for complicated development environment and engineering, just send the following code through the serial port to achieve:

```python
from machine import I2C # Import built-in library

i2c = I2C(I2C.I2C0, freq=100000, scl=28, sda=29) # Define an I2C object, use I2C0, frequency 100kHz, SCL pin is IO28, SDA pin is IO29
devices = i2c.scan() # call function to scan device
print(devices) # print device
```

Similarly, we need to implement a **breathing light**, just the following code:

> `board_info` is related to the board, and different board configurations are different. [Manual configuration](api_reference/builtin_py/board_info.md) is required before use.

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

**Real-time photos**:

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

**AI Object Detection**:

```python
import KPU as kpu
import sensor

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))

model = kpu.load("/sd/mobilenet.kmodel") # load model
while(True):
    img = sensor.snapshot() # take picture by camera
    out = kpu.forward(task, img)[:] # inference, get one-hot output
    print(max(out)) # print max probability object ID
```
please read doc before run it!

## The content of this document

All about MaixPy, including:
* How to choose and get a suitable module or development board
* How to get started
* Library and interface (API) document query
* Detailed step-by-step tutorial
* Sharing from the community (tutorial or open source project)

**In order to avoid encountering difficult problems during the learning process, please read from top to bottom according to the directory structure on the left, especially the chapters written in the front, do not skip**


## Can run MaixPy development board

First of all, we need to choose a development board that suits us. For the MaixPy model of each model, please click: [Development board and accessories purchase guide](./develop_kit_board/get_hardware.md), and there are also hardware parameters and corresponding development boards in the catalog. data

To get these boards, you can visit the official website of Sipeed [www.sipeed.com](https://www.sipeed.com/), or [official Taobao shop](https://sipeed.taobao.com/ )
## MaixPy source code

`MaixPy` source code refers to the `Micropython` parser running on `K210`, written in `C language`, source code is hosted on [github](https://github.com/sipeed/MaixPy), if you just want to use MaixPy, you don't need to know the source code, but you can also give MaixPy project a star [here](https://github.com/sipeed/MaixPy);

If you want to participate in the development of MaixPy’s built-in functions, you can download for development, and welcome everyone to submit a PR


This project is mainly maintained by &copy;<a href="https://www.sipeed.com" style="color: #f14c42">Sipeed</a> Co.,Ltd., and accepts contributions from the open source community, For specific contributions, see [Contributor List](https://github.com/sipeed/MaixPy/graphs/contributors)

## MaixPy document source code


The source code of the document is hosted at [github](https://github.com/sipeed/MaixPy_DOC), if the document has typos or improvements, you can submit a PR, and the document will be updated after the PR is passed

Note: Before editing the document, **must** look at the [document writing specification](contribute/doc_convention.md), only the modifications that conform to the document specification will be approved



## Feedback

For questions about this document or function or source code, you are also welcome to submit an issue:

* [Feedback](https://github.com/sipeed/MaixPy/issues)


## communicate with

If you have any questions, try to submit `issue` to the feedback address above, so that you can leave a record. Others can also check it. Before submitting, search to see if anyone has raised the same issue.

The following communication methods provide assistance:

<table role="table">
    <thead>
        <tr>
            <th>Communication method</th>
            <th>Address</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>issue(recommend)</td>
            <td><a href="https://github.com/sipeed/MaixPy/issues">https://github.com/sipeed/MaixPy/issues</a></td>
        </tr>
        <tr>
            <td>BBS</td>
            <td><a href="https://bbs.sipeed.com" rel="nofollow">https://bbs.sipeed.com</a></td>
        </tr>
        <tr>
            <td>MaixPy AI QQ group</td>
            <td>878189804</td>
        </tr>
        <tr>
            <td>MaixPy AI QQ Group (Second Group)</td>
            <td>1129095405</td>
        </tr>
        <tr>
            <td>telgram</td>
            <td><a href="https://t.me/sipeed" rel="nofollow">https://t.me/sipeed</a></td>
        </tr>
        <tr>
            <td>E-mail (commercial cooperation)</td>
            <td><a target="_blank" rel="noopener noreferrer" href="../assets/sipeed/support_email.jpg"><img src="../assets/sipeed/support_email.jpg" alt=" email" style="max-width:100%;"></a></td>
        </tr>
    </tbody>
</table>



------------
