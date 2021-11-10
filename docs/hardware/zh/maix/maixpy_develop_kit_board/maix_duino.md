# MaixDuino 开发板

## 概述

  SIPEED MaixDuino 是基于我们 M1 模块(主控:Kendryte K210)开发的一款外形兼容 Arduino 的开发板
  <br/>MaixDuino 集成摄像头、TF卡槽、用户按键、TFT显示屏、MaixDuino 扩展接口等, 用户可使用 MaixDuino 轻松搭建一款人脸识别门禁系统, 同时还预留开发调试接口, 也能将其作为一款功能强大的 AI 学习开发板.

## MaixDuino 外观及功能介绍

### 外观一览

![MaixDuino](./../assets/dk_board/maix_duino/maixduino_0.png)
![MaixDuino](./../assets/dk_board/maix_duino/maixduino_1.png)
![MaixDuino](./../assets/dk_board/maix_duino/maixduino_2.png)

### 板载功能介绍

- 电源输入 DC05: 6~12V 直流
- 电源输入 + 程序下载调试接口: USB Type-C 接口
- DVP 24PIN: 标准 Camera DVP 24PIN 接口
- TF 扩展槽:
- ESP32: ESP32 SPI 连接(ESP32 支持 WIFI 与 蓝牙)
- I2C DAC
- PA PAM8403A

![MaixDuino](./../assets/dk_board/maix_duino/maixduino_3.jpg)

## MaixDuino参数
Maixduino开发板以M1Al模块作为核心单元，功能非常很强大，模块内置64位双核处理器芯片，拥有8M的片上SRAM，在Al机器视觉、听觉性能方便表现突出，内置多种硬件加速单元(KPU、FPU，FFT等)，总算力最高可达1TOPS，可以方便地实现各类应用场景的机器视觉/听觉算法,也可以进行语音方向扫描和语音数据输出的前置处理工作。此外，开发板还配置了ESP32模块(WiFi+蓝牙一体)，简单的操作即可轻松联网。

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
        <td>图像识别</td>
        <td>QVGA@60fps/VGA@30fps</td>
    </tr>
    <tr>
        <td>语音识别</td>
        <td>麦克风阵列(8mics)</td>
    </tr>
    <tr>
        <td>网络模型</td>
        <td><li>支持YOLOv3<li>Mobilenetv2<li>TinyYOLOv2<li>人脸识别等</td>
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
        <td>视频处理</td>
        <td><li>神经网络处理器(KPU)<li>FPU满足IEEE754-2008标准<li>音频处理器(APU)<li>快速傅里叶变换加速器(FFT)</td>
    </tr>
    </tbody>
</table>
<table role="table" class="center_table">
  <thead>
    <tr>
      <th colspan = "2">ESP32模块</th>
    </tr>
  </thead>
  <tr>
    <td>主控</td>
    <td>ESP32-D0WDQ6(Xtensa 32-bit内核)</td>
  </tr>
  <tr>
    <td>无线标准</td>
    <td>802.11b/g/n</td>
  </tr>
  <tr>
    <td>无线频率</td>
    <td>2400MHz-2483.5MHz</td>
  </tr>
  <tr>
    <td>无线协议</td>
    <td>2.4G WiFi+双模蓝牙(BT&BLE4.2)</td>
  </tr>
  <tr>
    <td>天线</td>
    <td>PCB板载天线</td>
  </tr> 
</table>
<table role="table" class="center_table">
    <thead>
        <tr>
            <th colspan = "2" >开发板参数</th>   
        </tr>
    </thead>
        <td> 板载资源</td>
        <td><li>RGB灯*1<li>MEMS Microphone*1<li>USB转串口*1</td>
    </tr>
    <tr>
        <td>板载接口</td>
        <td><li>USB Type-C接口<li>24PIN DVP摄像头接口<li>24PIN LCD接口<li>MicroSD卡槽<li>音频接口（支持外接3扬声器）<li>部分IO排针引脚引出</td>
    </tr>
    <tr>
        <td>尺寸</td>
        <td>60*88mm</td>
    </tr>
    <tr>
        <td>供电电压</td>
        <td>5.0V @ 300mA（供电电流需大于300mA)</td>
    </tr>
    <tr>
        <td>工作温度</td>
        <td>-30℃ ~85C</td>
    </tr>
</table>
    
<table role="table" class="center_table">
    <thead>
        <tr>
        <th colspan = "2">软件开发</th>
        <tr>
    </thead>
    <tr>
    <td>芯片操作系统</td>
    <td>FreeRTOS、RT-Thread等</td>
    </tr>
    <tr>
    <td>开发环境</td>
    <td>MaixPy IDE、PlatformlO IDE、Arduino IDE等</td>
    </tr>
    <tr>
    <td>编程语言</td>
    <td>C，C++，MicroPython</td>
    </tr>
</table>


## 资料相关链接

- [MaixDuino 原理图](https://dl.sipeed.com/shareURL/MAIX/HDK/Sipeed-Maixduino)
<a href="/soft/maixpy/zh/" target="_blank"> MaixPy的使用教程入口 </a>
<a href="/soft/maixduino/zh/" target="_blank"> arduino的使用教程入口 </a>

## 产品技术支持
Maix系列产品可以在多种场景实现客户不同方面的需要，在AIoT上已经广泛的使用，品质和性能在行业内已经有非常好的口碑，专业的技术团队为广大客户解决硬件设计和软件功能上的各种各样问题。专业技术支持和更详细资料请联系商务<support@sipeed.com>。