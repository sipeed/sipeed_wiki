# MaixAmigo

## 使用教程
<a href="/soft/maixpy/zh/" target="_blank"> MaixPy </a>

## 概述

  SIPEED MaixAmigo 是基于我们 M1n 模块(主控:Kendryte K210)开发的一款集学习开发和商用一体的人脸识别产品.
  <br/>MaixAmigo 集成前后摄像头、TF卡槽、用户按键、TFT显示屏、锂电池、扬声器麦克风、扩展接口等, 用户可使用 MaixAmigo 轻松搭建一款人脸识别门禁系统, 同时还预留开发调试接口, 也能将其作为一款功能强大的 AI 学习开发板.

## MaixAmigo 外观及功能介绍

### 外观一览

![MaixAmigo](./../assets/dk_board/maxi_amigo/image-20200730120223557.png)

### 板载硬件功能介绍

- 3.5 寸 **TFT** 屏幕: 分辨率 **320x480***
- 3.5 寸电阻触摸屏： FT6X36
- 芯片复位按键
- 电源按键: 短按开机, 长按 *8S* 关机
- 三个功能按键
- Grove 接口: 板载 3 个**Grove** 数字接口, 传感器,控制器扩展无限可能~
- SP-MOD 接口: 板载 3 个更加强大,更高扩展性的 **SP-MOD** 数字接口, I2C,SPI(标准,双线,四线模式)等接口均可以使用
  - 后续支持乐高手柄功能
- TF 卡槽: 多媒体资源扩展,支持大容量储存
- 摄像头: 搭载 **OV7740** **30W** 像素 与 **GC0328 30W 像素** **Sensor**
- Type-C 接口: USB-TypeC 电源、调试接口,正反盲插


- 电源管理控制单元: AXP173
  - 板载 600mAh 锂电池,支持用户充放电控制
- 音频驱动 IC: ES8374
  - 支持音频录制,播放
- 三轴加速度传感器: MSA301

### 板载扩展接口

MaixAmigo 对用户开放了两个高度扩展的接口: SP-MOD 与 Grove 接口,
用户可以很方便的进行 DIY

#### SP-MOD 接口

SP-MOD 即为 sipeed module, simplify PMOD, super module

| 接口 | 接口描述 |
|---|---|
|SP-MODE 接口描述|![spmod_interface_1](./../../../assets/spmod/spmod_interface_1.png)|
|硬件接口|![spmod_interface_2](./../../../assets/spmod/spmod_interface_2.png)|

#### Grove 接口

Grove 接口的线缆有 4 种颜色, 用户可以根据颜色快速区别
![grove_interface](./../assets/interface_grove/grove_interface.jpg)

| pin | 颜色 | 描述 |
| --- | --- | --- |
| pin 1 | 黄色 | (例如, I2C Grove Connectors上的SCL) |
| pin 2 | 白色 | (例如, I2C Grove Connectors上的SDA) |
| pin 3 | 红色 |   VCC (所有的Grove接口红色都是VCC) |
| pin 4 | 黑色 |   GND (所有的Grove接口红色都是GND) |

Grove模块主要有 4 种接口:

- Grove Digital 数字接口:

    Grove 数字接口由 Grove 插头的四条标准线组成.
    两条信号线通常称为 D0 和 D1 .
    大多数模块只使用 D0, 但有些(像LED Bar Grove显示屏)使用两者.通常核心板会将板卡上的第一个Grove连接头称为 D0, 第二个称为 D1.第一个接头会连接到主控芯片的 DO/D1 管脚, 第二个连接头会连接到主控芯片的D1/D2引脚, 后面的连接头以此类推.

|pin  |Function | Note |
| ---|---|---|
| pin1 | Dn | 第一个数字输入 | 
| pin2 | Dn+1 | 第二个数字输入 |
| pin3 | VCC | 供电引脚 5V/3.3V |
| pin4 | GND | 地 |

- Grove Analog 模拟接口
    Grove模拟接口由Grove插头的四条标准线组成.
    两条信号线通常称为A0和A1.
    大多数模块只使用A0，但有些（像LED Bar Grove显示屏）使用两者.
    通常核心板会将板卡上的第一个Grove连接头称为A0，第二个称为A1。第一个接头会连接到主控芯片的AO/A1管脚，第二个连接头会连接到主控芯片的A1/A2引脚，后面的连接头以此类推.

| pin  | Function | Note |
| ---|---|---|
| pin1 | An | 第一个模拟输入 | 
| pin2 | An+1 | 第二个模拟输入 |
| pin3 | VCC | 供电引脚 5V/3.3V |
| pin4 | GND | 地 |


- Grove UART :
    The Grove UART 是特殊的一种数字输入输出接口
    它使用引脚 1 和引脚 2 进行串行输入和发送
    引脚1是 RX 线(用于接收数据, 因此是输入)
    其中引脚 2 是 TX 线(用于向 Grove 模块传输数据)

| pin  | Function | Note |
| --- | --- | --- |
| pin1 | RX | 串行接收 |
| pin2 | TX | 串行发送 |
| pin3 | VCC | 供电引脚 5V/3.3V |
| pin4 | GND | 地 |

- Grove I2C:
    有许多类型的 I2C Grove 传感器可用.MaixAmigo 上的 Grove 只支持 3.3V 传感器

  Grove I2C 连接器具有标准布局.引脚 1 是SCL信号, 引脚 2 是SDA信号

| pin  | Function | Note |
| --- | --- | --- |
| pin1 | SCL | I2C 时钟 |
| pin2 | SDA | I2C 数据 |
| pin3 | VCC | 供电引脚, 5V/3.3V |
| pin4 | GND | 地 |

### 板载 I2C 设备

MaixAmigo 板载 I2C 传感器/IC

| IC | 设备 id | I2C 地址(7位地址) |
| --- | --- | --- |
| ES8374 | 0x08 | 0x10 |
| MSA301 | 0x13 | 0x26 |
| AXP173 | 0x68 | 0x34 |

## 参数
Maix Amigo内置64位400Mhz双核高性能处理器,拥有8M的片上SRAM，16MiB FLASH大容量存储,轻松处理多媒体应用,在AI机器视觉、听觉性能方便表现突出，内置多种硬件加速单元（KPU、FPU，FFT等)，总算力最高可达1TOPS,可以方便地实现各类应用场景的机器视觉/听觉算法,也可以进行语音扫描和语音数据输出的前置处理工作

<table role="table" class="center_table">
    <thead>
        <tr>
            <th colspan = "2">K210 芯片基本参数</th>   
        </tr>
    </thead>
    <tbody>
    <tr>    
        <td>内核</td>
        <td>RISC-V Dual Core 64bit, with FPU</td>
    </tr>
    <tr>
        <td>主频</td>
        <td>400MHz （可超频至600MHz）</td>
    </tr>
    <tr>
        <td>SRAM</td>
        <td>内置8M Byte</td>
    </tr>
    <tr>
        <td>摄像头帧率</td>
        <td>OV7740/QVGA@60fps/VGA@30fps</td>
    </tr>
    <tr>
        <td>语音识别</td>
        <td>离线语音识别，声场</td>
    </tr>
    <tr>
        <td>网络模型</td>
        <td><li>支持MobileNetV1/V2<li>人脸识别<li>ASR</td>
    </tr>
    <tr>
        <td>深度学习框架</td>
        <td>支持TensorFlow \ Keras \ Darknet \ Caffe 等主流框架</td>
    </tr>
    <tr>
        <td>外设</td>
        <td>FPIOA、 UART、 GPIO、 SPI、 I2C、I2S、 TIMER</td>
    </tr>
    <tr>
        <td>硬件加速单元</td>
        <td><li>KPU卷积运算加速器<li>FPU浮点运算加速器<li>APU音频处理器<li>FFT傅里叶变换加速器</td>
    </tr>
    </tbody>
</table>

<table role="table" class="center_table">
    <thead>
        <tr>
            <th colspan = "2" >开发板参数</th>   
        </tr>
    </thead>
        <td> 板载资源</td>
        <td><li>3.5寸TFT屏幕<li>复位按键*1<li>功能按键*3<li>前后摄像头*2<li>LED*3<li>加速度传感器*1</td>
    </tr>
    <tr>
        <td>板载接口</td>
        <td><li>USB Type-C接口<li>音频接口(支持外接扬声器)<li>TF卡槽<li>Grove标准接口<li>SP-MOD接口(支持SP-MOD接口模块)</td>
    </tr>
    <tr>
        <td>尺寸</td>
        <td>104.3*63.3*16.5mm</td>
    </tr>
    <tr>
        <td>供电电压</td>
        <td>USB-type或内部锂电池（520mAh）</td>
    </tr>
</table>
    
<table role="table" class="center_table">
    <thead>
        <tr>
        <th colspan = "2">软件开发</th>
        <tr>
    </thead>
    <tr>
    <td>软件环境</td>
    <td>MaixPy（microPython）</td>
    </tr>
    <tr>
    <td>开发环境</td>
    <td>MaixPy IDE、PlatformlO IDE、Arduino IDE等</td>
    </tr>
    <tr>
    <td>编程语言</td>
    <td>C，MicroPython</td>
    </tr>
</table>

## 相关资料下载

Maix-Amigo 资料下载：[Sipeed-Amigo](https://dl.sipeed.com/shareURL/MAIX/HDK/Sipeed-Amigo)

Maix-Amigo 规格书下载：[Sipeed-Amigo](https://dl.sipeed.com/shareURL/MAIX/HDK/Sipeed-Amigo/ProductSpecification)

Maix-Amigo IPS 版本 原理图下载：[Maix_Amigo_2970(Schematic).pdf](https://dl.sipeed.com/fileList/MAIX/HDK/Sipeed-Amigo/2970/Maix_Amigo_2970(Schematic).pdf)

Maix-Amigo TFT 版本 原理图下载：[Maix_Amigo_2960(Schematic).pdf](https://dl.sipeed.com/fileList/MAIX/HDK/Sipeed-Amigo/2960/Maix_Amigo_2960(Schematic).pdf)

## 产品技术支持
Maix系列产品可以在多种场景实现客户不同方面的需要，在AIoT上已经广泛的使用，品质和性能在行业内已经有非常好的口碑，专业的技术团队为广大客户解决硬件设计和软件功能上的各种各样问题。专业技术支持和更详细资料请联系商务<support@sipeed.com>。