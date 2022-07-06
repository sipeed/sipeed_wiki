---
title: Sipeed M1/M1W
keywords: maixpy, k210, AIOT, 边缘计算, M1/M1W
desc: maixpy doc: Sipeed M1/M1W 
---

## M1/M1W

M1/M1W模块是基于嘉楠堪智科技的边缘智能计算芯片 K210 (RISC-V架构) 设计的一款AIOT模块。主控芯片内置64位双核高性能低功耗处理器，每个核都有浮点运算单元(FPU) ,具备卷积人工神经网络硬件加速器(KPU)和快速傅里叶变换加速器(FFT)、搭载现场可编程IO阵列(FPIOA)，支持多种主流Al编程框架。M1W模块内置标准802.11 b/g/n协议的ESP8285 WiFi芯片，可让模块轻松联网。

![M1/M1W](./assets/m1_m1w/M1_Dan.png)

## 应用
智能家居，机器人清洁器，智能扬声器，电子门锁，家庭监控等;
医学行业应用，如辅助诊断，医学图像识别;
智能工业应用，如工业机械，智能分拣，电气设备监控等;
教育机器人，智能互动平台，教育效率检查等教育应用;
农业应用，如农业监测，病虫害监测，自动控制等


## M1/M1W 参数
M1/M1W Al模块系统主要由电源(3 Channel DC-DC)、Flash芯片(16M)电路、K210芯片和WiFi芯片四部分组成。K210作为核心单元，功能非常很强大，芯片内置64位双核处理器，拥有8M的片上SRAM。模块在Al机器视觉、听觉性能方便表现突出，芯片总算力可达1TOPS，芯片内置多种硬件加速单元(KPU、FPU，FFT等)，可以方便地实现各类应用场景的机器视觉/听觉算法,也可以进行语音方向扫描和语音数据输出的前置处理工作。M1W模块嵌入无线WiFi功能，可轻松实现联网控制。


<p><img loading="M1/M1W" src="./assets/m1_m1w/M1_vs_M1W.png" width = 500 ></p>
<p><img loading="M1/M1W" src="./assets/m1_m1w/M1_pin.png" width = 500 ></p>
<p><img loading="M1/M1W" src="./assets/m1_m1w/M1W_2.png" width=500 ></p>

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
        <td>神经网络模型</td>
        <td><li>支持YOLOv3<li>Mobilenetv2<li>TinyYOLOv2</td>
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
            <th colspan="2">模块软件</th>
        </tr>
    </thead>
    <tr>
    <td>操作系统</td><td>FreeRtos and Standrad development ki</td>
    </tr>
    <tr>
        <td>编程语言</td><td>MicroPython</td>
    </tr>
    <tr>
        <td>机器视觉</td><td>支持卷积神经网络</td>
    </tr>
    <tr>
        <td>机器听觉</td><td>高性能音频处理器(APU)</td>
    </tr>
    <tr>
        <td>开发环境</td><td>串口终端、MaixPy IDE</td>
    </tr>
</table>

<table role="table" class="center_table">
    <thead>
        <tr>
            <th colspan="2">模块硬件</th>
        </tr>
    </thead>
    <tr>
    <td>尺寸</td><td>25.4*25.4*3.3mm</td>
    </tr>
    <tr>
        <td>引脚</td><td>72 PIN全引脚引出</td>
    </tr>
    <tr>
        <td>供电电压</td><td>5.0V @ 300mA（供电电流需大于300mA)</td>
    </tr>
    <tr>
        <td>工作温度</td><td>-30°C ~85°C</td>
    </tr>
</table>

<table role="table" class="center_table">
    <thead>
        <tr>
            <th colspan = "2">Wi-Fi功能参数</th>
        </tr>
    </thead>
    <tr>
        <td>主控</td>
        <td>ESP8285</td>
    </tr>
    <tr>
    <td>无线标准</td><td>802.11 b/g/n</td>
    </tr>
    <tr>
    <td>频率范围</td><td>2400Mhz - 2483.5Mhz</td>
    </tr>
    <tr>
    <td>天线</td><td>标准IPEX接口天线</td>
    </tr>
    <tr>
    <td>Wi-Fi模式</td><td>支持Station / SoftAP /SoftAP+Station</td>
    </tr>
</table>

> 为了让Al模块能应用于更多场合，Sipeed团队还推出了无WiFi功能版本的M1模块，如果用户无需使用无线联网的功能，可以选择我们的M1模块。M1模块和M1W模块的AI功能一致，使用方法基本相同，主要区别就是M1W模块比M1模块多了WiFi功能。

## 资料下载

芯片 K210 Datasheet: [Kendryte 官网](https://canaan-creative.com/)
M1W 资料下载: [dl.sipeed.com](https://dl.sipeed.com/shareURL/MAIX/HDK/Sipeed-M1&M1W)


## 产品技术支持
Maix系列产品可以在多种场景实现客户不同方面的需要，在AIoT上已经广泛的使用，品质和性能在行业内已经有非常好的口碑，专业的技术团队为广大客户解决硬件设计和软件功能上的各种各样问题。专业技术支持和更详细资料请联系商务<support@sipeed.com>。