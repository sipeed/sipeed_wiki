# Maix Bit

## 教程&快速上手

相关的使用教程入口<a href="/soft/maixpy/zh/" target="_blank"> MaixPy </a>

## 描述
MAIX Bit开发板是SiPEED公司MAIX产品线的一员，基于嘉楠堪智科技的边缘智能计算芯片K210(RISC-V架构 64位双核)设计的一款AIOT开发板。开发板使用模块+底板方式设计，整洁小巧，板载Type-C接口和USB-UART电路，用户可以直接通过USB Type-C线连接电脑进行开发，配置128Mbit Flash、LCD、DVP、Micro SD卡等接口并把所有IO引出，方便用户扩展。

## 外观
<img src="./../assets/dk_board/maix_bit/Bit.png" alt="Maxi bit" >

## 特性

MaixBit开发板以K210作为核心单元，功能非常很强大，芯片内置64位双核处理器，拥有8M的片上SRAM，在Al机器视觉、听觉性能方便表现突出，内置多种硬件加速单元(KPU、FPU，FFT等)，总算力最高可达1TOPS，可以方便地实现各类应用场景的机器视觉/听觉算法,也可以进行语音方向扫描和语音数据输出的前置处理工作。


## 应用
智能家居，机器人清洁器，智能扬声器，电子门锁，家庭监控等;
医学行业应用，如辅助诊断，医学图像识别;
智能工业应用，如工业机械，智能分拣，电气设备监控等;
教育机器人，智能互动平台，教育效率检查等教育应用;
农业应用，如农业监测，病虫害监测，自动控制等

## 参数
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
            <th colspan = "2" >开发板参数</th>   
        </tr>
    </thead>
        <td> 板载资源</td>
        <td><li>按键*2 <li>RGB灯*1<li>MEMS Microphone*1<li>USB to UART<li>128Mbit Flash*1</td>
    </tr>
    <tr>
        <td>板载接口</td>
        <td><li>USB Type-C接口<li>24PIN DVP摄像头接口<li>24PIN LCD接口<li>MicroSD卡槽<li>所有IO排针引脚引出</td>
    </tr>
    <tr>
        <td>尺寸</td>
        <td>53.3*25.4mm</td>
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

## 资料下载
Sipeed-Maix-Bit 资料下载：[Sipeed-Maix-Bit](https://dl.sipeed.com/shareURL/MAIX/HDK/Sipeed-Maix-Bit)

Sipeed-Maix-Bit 规格书下载：[Sipeed-Maix-Bit](https://dl.sipeed.com/fileList/MAIX/HDK/Sipeed-Maix-Bit/Specifications/Sipeed%20Maix-Bit%20%E8%A7%84%E6%A0%BC%E4%B9%A6%20V2.0.pdf)

Sipeed-Maix-Bit 原理图下载：[Sipeed-Maix-Bit](https://dl.sipeed.com/fileList/MAIX/HDK/Sipeed-Maix-Bit/Maix-Bit%20V2.0(with%20MEMS%20microphone)/Maix-Bit%20V2.0(Schematic).pdf)

## 产品技术支持
Maix系列产品可以在多种场景实现客户不同方面的需要，在AIoT上已经广泛的使用，品质和性能在行业内已经有非常好的口碑，专业的技术团队为广大客户解决硬件设计和软件功能上的各种各样问题。专业技术支持和更详细资料请联系商务<support@sipeed.com>。