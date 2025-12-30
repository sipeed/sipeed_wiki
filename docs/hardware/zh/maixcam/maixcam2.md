---
title: MaixCAM2 -- 快速落地 AI 视觉、听觉应用
---


<style>
    #content_body .h1 {
        font-size: 2.2em;
        font-weight: 800;
    }
    .flex_center {
        display:flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .flex {
        display: flex;
    }
    .flex-row {
        flex-direction: row;
    }
    .items-center {
        align-items: center;
    }
    .justify-center {
        justify-content: center;
    }
    .justify-around {
        justify-content: space-around;
    }
    .w-full {
        width: 100%;
    }
    #content_body .card_item {
        color: #f0f5f9;
        background: linear-gradient(90deg, #26d0ce, #1a2980);
        border-radius: 1em;
        padding: 1em;
        margin: 1em 0.1em;
    }
    #content_body .card_item img {
        transition: transform 0.4s ease;
    }
    #content_body .card_item:visited {
        color: #f0f5f9;
    }
    #content_body .card_item:hover {
        border-radius: 1em;
        /* background: linear-gradient(70deg, #26d0ce, #1a2980); */
        padding: 1em;
        margin: 1em 0.1em;
    }
    #content_body .card_item:hover > img {
        transform: rotate(1deg) scale(1.05) ;
    }
    .mask_wrapper {
        position: relative;
    }
    .mask {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
    .item_name {
        font-size: larger;
        font-weight: 800;
    }
    #content_body .btn_blue {
        margin: 1em;
        color: white;
        font-size: 0.9em;
        border-radius: 0.3em;
        padding: 0.5em 2em;
        background-color: #0b4294;
    }
    #content_body .btn_blue:visited {
        color: white;
    }
    #content_body .btn_blue:hover {
        margin: 1em;
        color: white;
        font-size: 0.9em;
        border-radius: 0.3em;
        padding: 0.5em 2em;
        background-color: #082a5e;
    }
    #content_body .btn_red {
        margin: 1em;
        color: white;
        font-size: 0.9em;
        border-radius: 0.3em;
        padding: 0.5em 2em;
        background-color: #ad3838
    }
    #content_body .btn_red:visited {
        color: white;
    }
    #content_body .btn_red:hover {
        margin: 1em;
        color: white;
        font-size: 0.9em;
        border-radius: 0.3em;
        padding: 0.5em 2em;
        background-color: #630606;
    }

    .dark #content_body .card_item {
        color: #f0f5f9;
    }
    .dark #content_body a.card_item:visited {
        color: #f0f5f9;
    }
    .dark .card_item {
        background: #292929;
    }
</style>

<div style="width:100%; display:flex;justify-content: center;">

<!-- ![maixcam2](/static/image/maixcam2_front_back.png) -->

</div>

<div class="flex_center w-full">
    <div class="flex flex-row w-full">
        <div class="flex flex-row items-center justify-around w-full card_item mask_wrapper item1">
            <img src="/static/image/maixcam2_front_back.png" style="width: 80%">
        </div>
    </div>
</div>

<div style="padding: 1em 0 0 0; display: flex; justify-content: center">
    <a target="_blank" class="btn_red" href="https://sipeed.taobao.com">淘宝</a>
    <a target="_blank" class="btn_red" href="https://www.aliexpress.com/store/911876460">速卖通</a>
</div>

<div class="mb-10"></div>


## MaixCAM2 简介

`MaixCAM2` 是为更好地落地 AI 视觉、听觉和 AIOT 应用而设计的一款硬件产品，一个能快速验证产品原型且能快速量产的平台。

### **特点**：

1. **硬件性能突出**：双核`A53` + `12.8Tops@INT4 / 3.2Tops@INT8` + `4GB LPDDR4` + 多种硬件编解码器, `640x640` 分辨率下单独运行模型， `YOLO11n` 高达 `113FPS`, `YOLO11s` 高达 `62fps`。
    以下为常见芯片跑 `YOLO11n` 的横评：
    ![](../../assets/maixcam/maixcam2_benchmark.jpg)
2. **配套一体化硬件**：最高配套 `4K 1/1.8"` 摄像头、`640x480`高清触摸屏、双麦克风、`WiFi6`+`BLE5.4` 等，无需复杂硬件适配工作，上手即用。
3. **多种硬件形态**：提供带外壳的版本，不同配件配置，也提供`核心板`。
4. **离线 AI 大模型支持**： 除了支持`卷积模型`，也支持 `Transformer 模型`，上手即用的 `LLM / VLM / ASR / TTS`。
5. **完善和易用的软件生态**： 提供精心打磨的 [MaixPy](https://wiki.sipeed.com/maixpy)(`Python`) + [MaixCDK](https://wiki.sipeed.com/maixcdk)(`C++`) SDK, 丰富的文档和专业的配套 `IDE`、`云平台`。


### 基于 `MaixCAM2`，你可以创造出：

* **DIY 智能相机**：提供 `4K` 大底 `1/1.8"` 传感器，支持 `JPEG / RAW / H.264 / H.265` 编码，提供易用的软件支持，配合 `NPU` 加速的 `AI` 功能，轻松 DIY 你的智能相机。
* **机器人**：双麦 + 高清摄像头 + 高清触摸屏 + 硬件加速的 `AI` + 丰富外设，支持`卷积模型`、`Transformer模型`，上手即用的 `YOLO / LLM / VLM / ASR / TTS`，适用从玩具到各专业领域智能机器人。
* **产线质检助手**：传统算法 OpenMV / OpenCV + 硬件加速的 `AI` 识别，轻松满足产线机器人高精度和实时性和低成本需求。
* **竞赛杀器**：各种比赛好帮手，强大的性能、小巧的体积，易用的 Python SDK（MaixPy） 和 C++ SDK（MaixCDK），光速出有竞争力的作品。已有许多同学使用 MaixCAM 获得各种比赛的最高奖项。
* **教育帮手**：高校科研、教学， STEM 启蒙，传播最新知识，启发未来科技。
* **更多**： 等你发掘～

### 功能展示

**详细功能介绍请看：** <a target="_blank" class="btn_red" href="https://wiki.sipeed.com/maixpy/">MaixPy 主页</a>

## MaixCAM2 硬件参数

下表中加粗的是相比 MaixCAM / MaixCAM-Pro （一代）的升级点。

| 组件 | 描述 |
| --- | --- |
| CPU 大核 | **1.2GHz A53 x2, 运行 Linux(Ubuntu)** |
| CPU 小核 | RISC-V 32bit E907， 跑 RTT |
| NPU | **12.8Tops@INT4 / 3.2TOPS@INT8**， 支持卷积和**Transformer模型**，如 YOLO/**LLM/VLM** 等,  **YOLO11n 640x640 帧率高达 113FPS** |
| 内存 | **1GB / 4GB LPDDR4** 可选 |
| 存储 | **板载 32GB EMMC**， 板载 TF 卡槽 |
| 摄像头 | 最高支持 **8M(4K)@30fps** 摄像头，4 lane MIPI CSI 输入，22Pin 接口，支持拆分双路 CSI |
| 屏幕 | 2.4 寸高清 IPS 电容触摸屏，分辨率 640x480（4 lane MIPI DSI 输出，标准 31pin 接口，6pin 电容触摸屏），最大 1080p@60fps 输出 |
| 音频输出 | 板载PA功放 + **1W 喇叭** |
| 音频输入 | 板载**模拟硅麦 x2**，可直接收音 |
| 网络 | 板载 WiFi6 + BLE5.4 模组，**板载6pin FPC以太网接口(配合外接FPC 转 RJ45 模块使用)** |
| USB | Type-C USB2.0，支持Device和Host模式，支持 USB 摄像头 |
| IO 接口 | 2.54mm PMOD 接口， 引出 **20 个 IO** + Vsys/3.3v/GND 接口 + 1.25mm 6pin扩展接口，**核心板提供更多可用 IO**|
| 按键 | 1 x 电源开关 + 1 x Func（功能） 按键 |
| LED | 电源指示灯 + 用户 LED + **照明 LED** |
| 编解码 | H.264 / H.265 / MJPEG 硬解码， 支持 **4k@30fps 编码，1080p@60fps解码** |
| 外设 | I2C/SPI/UART/ADC/PWM/WDT 等常见外设 |
| 电源 | **支持锂电池充放电管理，并且提供带锂电池版本** |
| 外壳 | **外壳， 1/4 英寸标准螺纹固定孔** |
| IMU | **板载六轴 IMU 传感器（三轴加速度+三轴角速度）** |
| RTC | **板载 BM8563EMA RTC 芯片+纽扣充电电池，断电时间仍然正确** |
| 核心板 | **提供只包含芯片核心电路 + DDR 的金手指核心板**，方便自行硬件定制 |
<!-- | 尺寸 | **无电池版本外壳 67x51x12mm**  | -->


## MaixCAM2 软件生态

我们不只是做了硬件，更为 MaixCAM2 提供了一套完整的软件生态，包括：

| 名称 | 描述 | 图片/视频 |
| --- | --- | --- |
| **[MaixPy](https://wiki.sipeed.com/maixpy/)** | Python 开发包， 提供丰富且使用简单的 API，针对 MaixCAM 进行优化，支持硬件加速，提供丰富文档教程 | 1. [MaixPy 主页](https://wiki.sipeed.com/maixpy/)<br>2. [MaixPy 源码](https://github.com/sipeed/MaixPy) |
| [MaixVision](https://wiki.sipeed.com/maixvision) | AI 视觉 IDE，编程、代码运行、图像实时预览，甚至图形化编程等等，大大降低开发环境搭建难度和使用门槛 | ![MaixVision](../../assets/maixcam/maixvision.jpg)  <video playsinline controls muted preload style="width:100%" src="https://wiki.sipeed.com/maixpy/static/video/maixvision.mp4"></video> |
| [MaixHub](https://maixhub.com) | 在线 AI 模型训练平台，无需 AI 知识和昂贵的训练设备，一键训练模型，一键部署到 MaixCAM | ![MaixVision](../../assets/maixcam/maixhub.jpg) |
| [MaixCDK](https://github.com/sipeed/MaixCDK) | MaixPy 的 C++版本，熟悉 C/C++ 的开发者立刻上手 | 请看[MaixCDK 主页](https://github.com/sipeed/MaixCDK) |
| [应用商城](https://maixhub.com/app) | 提供各种应用和工具，无需开发直接下载使用，开发者也可以上传分享应用 | 请看 [MaixHub 应用商城](https://maixhub.com/app) |
| [分享广场](https://maixhub.com/share) | 开发者分享经验和项目 | 请看 [MaixHub 分享广场](https://maixhub.com/share) |


## 资料汇总

### MaixCAM 专属资料（Sipeed 提供）

* [MaixCAM2 官方文档](https://wiki.sipeed.com/maixcam2)（本文档）
* [MaixPy 官方文档](https://wiki.sipeed.com/maixpy/)（Python SDK）（[MaixPy 源码](https://github.com/sipeed/MaixPy)）
* [MaixCDK](https://github.com/sipeed/MaixCDK)（C/C++ SDK）（[MaixCDK 源码](https://github.com/sipeed/MaixCDK)）
* [系统源码](https://github.com/sipeed/maix_ax620e_sdk)
* [系统烧录](./maixcam2_os.md)
* [摄像头和镜头](./maixcam2_camera_lens.md)
* [硬件相关资料下载](https://dl.sipeed.com/shareURL/MaixCAM/MaixCAM2)
* [核心板资料](https://dl.sipeed.com/shareURL/MaixCAM/MaixCAM2)
* 外壳和支架：开源了 外壳、支架等 3D 模型文件，请到[makerworld.com](https://makerworld.com/)（推荐） 或[makerworld.com.cn](https://makerworld.com.cn) 搜索 `MaixCAM`/`MaixCAM2`。
* 引脚映射图：
> 注意: 为了防止插入PMOD等模块时插错位置导致模块烧毁, 默认将 `A2` 引脚堵住作为防呆设计
![maixcam2_pins](../../assets/maixcam/maixcam2_pins.jpg)


### 芯片资料

MaixCAM2 其基于爱芯的 AX630C 芯片，所以也可以参考它们的资料。

* [芯片原厂 资料下载](https://dl.sipeed.com/shareURL/MaixCAM/MaixCAM2)
* [芯片原厂 AI 模型](https://huggingface.co/AXERA-TECH)
* [芯片原厂 GitHub](https://github.com/AXERA-TECH)

### 配件

* [TOF测距和热成像模块](./tof_thermal.md)
* [显微套件](./microscope.md)


### 社区

* [MaixHub 应用商城](https://maixhub.com/app)
* [MaixHub 分享广场](https://maixhub.com/share)
* [GitHub](https://github.com) 搜索 `MaixCAM` 或者 `MaixPy`
* [Bilibili](https://bilibili.com) 搜索 `MaixCAM` 或者 `MaixPy`
* [makerworld.com](https://makerworld.com/)(推荐) 或者 [makerworld.com.cn](https://makerworld.com.cn) 搜索 `MaixCAM`
* QQ 群: 862340358
* Telegram: [MaixPy](https://t.me/maixpy)

## 购买

* [Sipeed 淘宝](https://sipeed.taobao.com/)
* [AliExpress](https://www.aliexpress.com/store/911876460)



