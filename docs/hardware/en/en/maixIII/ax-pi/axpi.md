---
title: MAIX-III AXera-Pi
keywords: MAIX-III, AXera-Pi, Maix3, Sipeed, ax620a, axera, sipeed, AI, model, maixhub
update:
  - date: 2022-12-08
    version: v0.1
    author: wonder
    content:
      - Initialize Doc
---

If you think this AI development board are excellent enough and your friends may be interested with this, just share with them this link [http://wiki.sipeed.com/en/m3axpi](http://wiki.sipeed.com/en/m3axpi)

![maixiii_axpi](./../../../../../static/home/maixiii_axpi_en.jpg)

> [Official Online Store](https://www.aliexpress.com/item/1005005016931077.html)

In the past few years, many Linux AI chips come out.

Raspberry Pi and Jetson Nano these boards are really popular by their good performance, but now MAIX-III AXera-Pi comes out, equipped with the high-performance 3.6TOPs@INT8 chip ax620a, which will be your good choice and provice you a really good experience.

<p align="center">
<img src="https://axera-tech.com/upload/8f/091a2540e7cdc5c7f62df022f80220.jpg" alt="img" style="zoom: 50%;" />
</p>

We design a core module for this chip, which is convenient if you want to design the ext-board for yourself.

<table>
<thead>
<tr>
  <th colspan=2>MaixIII Core module</th>
</tr>
</thead>
<tbody>
<tr>
  <td>CPU</td>
  <td>4 * Cortex-A7, with NEON and FPU</td>
</tr>
<tr>
  <td>NPU</td>
  <td>14.4Tops@int4，3.6Tops@int8</td>
</tr>
<tr>
  <td>ISP</td>
  <td>4K@30fps</td>
</tr>
<tr>
  <td>Codec format</td>
  <td>H.264, H.265</td>
</tr>
<tr>
  <td>Video encode</td>
  <td>4K@30fps</td>
</tr>
<tr>
  <td>Video decode</td>
  <td>1080P@60fps</td>
</tr>
<tr>
  <td>Ethernet</td>
  <td>Support RGMII / RMII Ethernet</td>
</tr>
<tr>
  <td>Display</td>
  <td>MIPI DSI 4 Lane，up to 4K@30FPS</td>
</tr>
<tr>
  <td>DRAM</td>
  <td>2GB LPDDR4X 3733Mhz</td>
</tr>
<tr>
  <td>Storge</td>
  <td>Optional 16GB EMMC (Boot from TF card by default)</td>
</tr>
<tr>
  <td>IO pins</td>
  <td>DDR4 SODIMM 260P route all IO</td>
</tr>
</tbody>
</table>

## Introduction

In WORLD ARTIFICIAL INTELLIGENCE CONFERENCE 2022, this AI board is shown the first tima, like what's in the following picture.

<p align="center">
  <img src="./../../../zh/maixIII/assets/waic-axpi.jpg" style="zoom: 70%;" />
</p>

And finally we launched this AI development board equipped with AX620A in 20221001. Its official name is **MAIX-III AXera-Pi**, while we like to call it **M3AXPI** in the following content.

<p align="center">
  <video src="../../../zh/maixIII/assets/axpi_boom.mp4"
    width="100%" controls="controls" autoplay="autoplay"
    x5-playsinline=""
 		playsinline
 		webkit-playsinline="true"
 		poster="../../../zh/maixIII/assets/maix-iii-small.jpg"
 		preload="auto"
  >
  </video>
</p>

So, why is this AI development board good?

- Need documents? Follow our guides, to start journey from embedded Linux development to AI model deployment.
- High power consumption? Just use one usb cable connecting with USB3.0 port to boot this device, no need of other power supply.
- Difficult to develop? Compile your own application on this board, or train your own AI model online and deploy it on board.
- Awful camera image? This chip is aimed for AI ISP night vision enhancement, we have adjust the camera to best state.
- Too expensive? This board sold about 100$, chiper than any other similar board.

## Special column Documents

These documents are from Chinese club, read these via browser translator is a good idea.

Official Documents:

- [MAIX-III AXera-Pi：New generation of 3.6T visual AI board comes out](https://aijishu.com/a/1060000000374898)
- [MAIX-III AXera-Pi: Many kinds of AI usage](https://aijishu.com/a/1060000000374900)
- [MAIX-III AXera-Pi: Plenty of demos on this board](https://aijishu.com/a/1060000000374902)
- [MAIX-III AXera-Pi: Unbox this board](https://aijishu.com/a/1060000000378968)
- [MAIX-III AXera-Pi: Start this board ①](https://aijishu.com/a/1060000000380513)
- [MAIX-III AXera-Pi: Start this board ②](https://aijishu.com/a/1060000000383970)

- [YOLOv8 object detection：Train and deploy model on Axera-Pi ①](https://aijishu.com/a/1060000000395215)
- [YOLOv8 object detection：Train and deploy model on Axera-Pi ②](https://aijishu.com/a/1060000000395812)
- [MMPose：Human Keypoints Detection on AXera-Pi](https://aijishu.com/a/1060000000396746)
- [MOT：Mutiple Object Tracking on AXera-Pi](https://aijishu.com/a/1060000000399566)
- [MMPose (Extra section) ：Fall Detection and alert on AXera-Pi](https://aijishu.com/a/1060000000401084)
- [OCR：Optical Character Recognition on AXera-Pi](https://aijishu.com/a/1060000000403913)

Community Documents:

- [Axera-Pi unbox experience](https://zhuanlan.zhihu.com/p/571233089)
- [HonestQiao —— unbox Axera-Pi](https://bbs.elecfans.com/m/jishu_2314161_1_1.html)
- [Axera-Pi NPU experience](https://neucrack.com/p/440)
- [MMYOLO object detection algorithm on AX620A](https://zhuanlan.zhihu.com/p/614698969)
- [Deploy yolov8 on Axera-Pi](https://www.yuque.com/prophetmu/chenmumu/pd3sdkb8z4vvvgai)
- [[m3axpi] YOLOv5 Train and deploy model](https://github.com/Abandon-ht/m3axpi_model/blob/main/yolov5/README_zh-CN.md)
- [[m3axpi] YOLOv8 Train and deploy model](https://github.com/Abandon-ht/m3axpi_model/blob/main/yolov8/README_zh-CN.md)
- [Prepare AX620A development enviroment on ubuntu22.04](https://blog.csdn.net/flamebox/article/details/127103964)
- [Train and deploy yolo5s on Axera-Pi](https://blog.csdn.net/flamebox/article/details/127249243)
- [[AXPI] Use RNDIS on m1/m2 MAC](https://zhuanlan.zhihu.com/p/593627641)
- [Kaldi - Real-time speech recognition on embedded device](https://mp.weixin.qq.com/s/r4nGu04o1sjdFZt_vYbUAA)

Video reference:

- [MAIX-III AXera-Pi unbox and start](https://www.bilibili.com/video/BV1LP4y1274d)
- [MAIX-III AXera-Pi development deployment](https://www.bilibili.com/video/BV1Ne4y117U9)
- [MAIX-III AXera-Pi model transformer and deploy](https://www.bilibili.com/video/BV1jg411z7C8)
- [MAIX-III AXera-Pi video inference and push](https://www.bilibili.com/video/BV14D4y147Ed)

## Camera effect

### Night vision enhancement

<table>
    <tr>
        <th colspan="2">Left picture is original, right picture is enhanced</th>
    </tr>
    <tr>
        <td><img src="./assets/axpi/night_vision_enhancement_1.jpg"></td>
        <td><img src="./assets/axpi/night_vision_enhancement_2.jpg"></td>
    </tr>
    <tr>
        <td><img src="./assets/axpi/night_vision_enhancement_3.jpg"></td>
        <td><img src="./assets/axpi/night_vision_enhancement_4.jpg"></td>
    </tr>
</table>

<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=561523949&bvid=BV1Ee4y1v7iF&cid=860676576&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="max-width:640px; max-height:480px;"> </iframe>
</p>

### Exhibition darkroom

- The left screen shows the enhanced picture and the righr screen is the original one.

<div align="center"><img src="./assets/axpi/exhibition_darkroom.jpg" alt="exhibition_darkroom" ></div>

<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=430541632&bvid=BV1iG41137tx&cid=831645988&page=1&t=83.6" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="max-width:640px; max-height:480px;"> </iframe>
</p>

### Actual AI effect

<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=773227207&bvid=BV1B14y1Y7A4&cid=837154353&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="max-width:640px; max-height:480px;"> </iframe>
</p>

## AI Ecology

### Support many Operators

![many_operator](./assets/axpi/many_operator.jpg)

Screenshots of part operators. [Click me to see whole operator support list](https://pulsar-docs.readthedocs.io/en/latest/appendix/op_support_list.html)

### Many archived models

Before receiving this board, visit [MaixHub](https://maixhub.com/model/zoo) to see your interested model, choose Platform `axera-pi` at the Lower left corner to find model can be deployed on `AX-PI`

![maixhub_zoo.jpg](./assets/axpi/maixhub_zoo.jpg)

Apart from these, many models are uploaded to [github AXERA-TECH/ax-samples](https://github.com/AXERA-TECH/ax-samples), and we also put sme models in sustem image, just burn the system image into SD card and boot it on board to experience these models. Up to now the supported models are as follows:

- Objects Classification
  - MobileNetv1
  - [MobileNetv2](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax620/README.md#MobileNetv2)
  - MobileOne-s0
  - ResNet18
  - ResNet50
  - Others......
- Objects Detection
  - [PP-YOLOv3](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax620/README.md#yolov3paddle)
  - YOLOv3
  - YOLOv3-Tiny
  - YOLOv4
  - YOLOv4-Tiny
  - YOLOv4-Tiny-3l
  - [YOLOv5s](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax620/README.md#YOLOv5s)
  - [YOLOv5-Lite](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax620/README.md#YOLOv5-Lite)([original model](https://github.com/ppogg/YOLOv5-Lite))
  - [YOLOv7-Tiny](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax620/README.md#YOLOv7-Tiny)  
  - [YOLOv8s](https://github.com/AXERA-TECH/ax-samples/tree/main/examples#YOLOv8s)
  - [YOLOX-S](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax620/README.md#YOLOX-S)
  - YOLO-Fastest-XL
  - NanoDet
- Human Body Detection
  - YOLO-Fastest-Body
- Human Face Detection
  - [scrfd](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax620/README.md#Scrfd)
  - [YOLOv5-Face](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax620/README.md#YOLOv5-Face)([original model](https://github.com/deepcam-cn/yolov5-face))
- Human Face Segmentation
  - Face_Parsing
- Obstacles Detection
  - Robot-Obstacle-Detect
- Object detection of Uav view
  - [YOLOv5s_visdrone](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax620/README.md#YOLOv5s_visdrone)
- Monocular 3D Vehicle Detection
  - [Monodlex](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax620/README.md#Monodlex)
- Human body Key points
  - [HRNet](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax620/README.md#HRNet)
  - [AX-POSE-PPL](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax620/README.md#AX-POSE-PPL)
  - [HandPose](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax620/README.md#HandPose)
- Human body Segmentation
  - [PP-HumanSeg](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax620/README.md#PP-HumanSeg)
- Semantics Segmentation
  - [PP-Seg](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax620/README.md#MobileSeg)
- Classic CV
  - CropResize
- Pipeline example
  - NV12 -> CropResize -> NN(Classification)

Visit [Deploy models to AX-Pi (Maix-III(M3) series) board](/ai/en/deploy/ax-pi.html) to deploy models to AX-Pi.

<!-- <p align="center">
  <img src="./../../../en/maixIII/assets/ai_guide.jpg" style="zoom: 75%;" />
</p> -->

### Tranning your models

- [[m3axpi] YOLOv5 train and convert model guide](https://github.com/Abandon-ht/m3axpi_model/blob/main/yolov5/README.md)
- [[m3axpi] YOLOv8 train and convert model guide](https://github.com/Abandon-ht/m3axpi_model/blob/main/yolov8/README.md)

### Tranning model online

Now [MaixHub](https://maixhub.com/welcome) has been upgraded, with more friendly interface and more functions, here are steps to tranning model online.

<p align="center">
  <img src="./assets/axpi/test_maixhub.jpg" style="zoom: 100%;" />
</p>

### Share your model

There is a model and codes or programs to load your model after you finish training, you can share these on [Maixhub](https://maixhub.com/model/zoo) to others. Let's have fun and build the model Community together.

<p align="center">
  <img src="./assets/axpi/share_model.jpg" style="zoom: 75%;" >
</p>

## Cases

> Updated in 20221205

<p align="center">
  <img src="./assets/axpi/demo_one.jpg" style="zoom: 100%;">
  <img src="./assets/axpi/demo_two.jpg" style="zoom: 100%;">
</p>

## Linux development

### Run debian

We provide a linux image based on debian11, and you can boot this board from SD card after you burn the system image into SD card. We aim to make it easiler for user to use. Besides, it's really conveient to program AI development with Python API.

1. Burning image: [WIKI AXera-Pi Burn image](https://wiki.sipeed.com/hardware/en/maixIII/ax-pi/flash_system.html#Burn-system-image)

2. Basic usage：[WIKI AXera-Pi guide](https://wiki.sipeed.com/hardware/en/maixIII/ax-pi/flash_system.html)

3. Program with Python：[ax_pipeline_api](https://github.com/junhuanchen/ax_pipeline_api)

4. Development Note：[[maixpy3 axpi] How to port debian11 to ax620a](https://www.cnblogs.com/juwan/p/16751348.html) (中文)

5. Development Note：[[maixpy3 axpi] Edit and pack the compiled debian image](https://www.cnblogs.com/juwan/p/16769237.html) (中文)

### BSP SDK

We provide source code, api documents, sdk usages, visit [sdk usage](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/sdk_usage.html) to get more.

#### [ax-sample](https://github.com/AXERA-TECH/ax-samples)

Here are typical AI models provided by Axera for development, evaluation and verification, those who are good at AI development or want to test these models can have a try, and these are not involved with peripherals.

1. [examples](https://github.com/AXERA-TECH/ax-samples/tree/main/examples)
2. [PP-YOLOv3](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax620/README.md#yolov3paddle)
3. [PP-HumanSeg](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax620/README.md#MobileSeg)
4. [PP-Seg](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax620/README.md#PP-HumanSeg)

#### [libmaix](https://github.com/sipeed/libmaix)

A unified embedded development environment come by SIPEED, includes camera, screen, vision, image processing and pipelines-related deployment examples, is suitable for those who want to learn embedded Linux.

1. [Test screen display](https://github.com/sipeed/libmaix/tree/release/examples/display)
2. [Screen displays camera content](https://github.com/sipeed/libmaix/tree/release/examples/axpi)
3. [camera + screen + yolov5 model](https://github.com/sipeed/libmaix/tree/release/examples/axpi_yolov5_cam)

#### [axpi_bsp_sdk](https://github.com/sipeed/axpi_bsp_sdk)

BSP development package for business, provided by Axera. It's the original development package for this chip, containing components like uboot、linux、msp 、sample、rtsp、ipcdemo, and this is progressively open source, you can get these codes for commercial evaluation, such as ipcdemo, but normally these codes are complex and highly coupled, those who are experienced enough and want to use this board for business cooperation can try this.

1. Development documents [docs](https://github.com/sipeed/axpi_bsp_sdk/tree/main/msp/sample/vo_fb)
2. Platform application [ipcdmeo](https://github.com/sipeed/axpi_bsp_sdk/tree/main/app/IPCDemo)
3. Peripheral Verification[sample](https://github.com/sipeed/axpi_bsp_sdk/tree/main/msp/sample)

#### [ax-pipeline](https://github.com/AXERA-TECH/ax-pipeline)

AX-Pipeline is provided by Axera. With M3AXPI, this project is used for pepole to know the usages of ISP, image processing, NPU, codec and display, which is convenient for developers to quickly evaluate and develop their own multimedia applications.

1. [Quick compilation](https://github.com/AXERA-TECH/ax-pipeline/blob/main/docs/compile.md) Simple cross-platform compilation via cmake.
2. [How to replace into my own trained yolov5 model](https://github.com/AXERA-TECH/ax-pipeline/blob/main/docs/how_to_deploy_custom_yolov5_model.md)
3. [How to deploy my other models](https://github.com/AXERA-TECH/ax-pipeline/blob/main/docs/how_to_deploy_custom_model.md)
4. [How to adjust the image orientation](https://github.com/AXERA-TECH/ax-pipeline/blob/main/docs/how_to_adjust_image_orientation.md)
5. [ModelZoo](https://github.com/AXERA-TECH/ax-pipeline/blob/main/docs/modelzoo.md) descriptions for models which are supported or to be supported

## Hardware

<p align="center">
  <img src="./../../../zh/maixIII/assets/waiguan1.jpg" style="zoom: 51%;" />
  <img src="./../../../zh/maixIII/assets/maix-iii-small.jpg" style="zoom: 80%;" />
  <img src="./../../../zh/maixIII/assets/waiguan2.jpg" style="zoom: 45%;" />
</p>

### Hardware function diagram

<p align="center">
  <img src="./../../../zh/maixIII/assets/layout_axpi_2.png" alt="layout_axpi_2" width="45%">
  <img src="./../../../zh/maixIII/assets/layout_axpi_1.png" alt="layout_axpi_1" width="45%">
</p>

### Core module parameters

<table>
<thead>
<tr>
  <th colspan=2>MaixIII Core module</th>
</tr>
</thead>
<tbody>
<tr>
  <td>CPU</td>
  <td>4 * Cortex-A7, with NEON and FPU</td>
</tr>
<tr>
  <td>NPU</td>
  <td>14.4Tops@int4，3.6Tops@int8</td>
</tr>
<tr>
  <td>ISP</td>
  <td>4K@30fps</td>
</tr>
<tr>
  <td>Codec format</td>
  <td>H.264, H.265</td>
</tr>
<tr>
  <td>Video encode</td>
  <td>4K@30fps</td>
</tr>
<tr>
  <td>Video decode</td>
  <td>1080P@60fps</td>
</tr>
<tr>
  <td>Ethernet</td>
  <td>Support RGMII / RMII Ethernet</td>
</tr>
<tr>
  <td>Display</td>
  <td>MIPI DSI 4 Lane</td>
</tr>
<tr>
  <td>RAM</td>
  <td>2GB LPDDR4X 3733Mhz</td>
</tr>
<tr>
  <td>Storge</td>
  <td>Optional 16GB EMMC (Boot from TF card by default)</td>
</tr>
<tr>
  <td>IO pins</td>
  <td>DDR4 SODIMM 260P route all IO</td>
</tr>
</tbody>
</table>

### Ext-board parameters

<table>
<thead>
<tr>
  <th colspan=2> Ext-board </th>
</tr>
</thead>
<tbody>
<tr>
  <td>Camera</td>
  <td> Maixmum supported 3 cameras (Default connecting one camera):<br> 1 MIPI 4-LANE + 2 MIPI 2-LANE</td>
</tr>
<tr>
  <td>Display</td>
  <td>Maixmum supported 4-LANE MIPI DSI</td>
</tr>
<tr>
  <td>SD card slot</td>
  <td>Default boot from SD card</td>
</tr>
<tr>
  <td>Recording</td>
  <td>2 onboard MEMS MIC support dual MIC noise reduction</td>
</tr>
<tr>
  <td>Audio output</td>
  <td>Support 3.5MM interface, used for stereo output or MIC input</td>
</tr>
<tr>
  <td>Network</td>
  <td>Support Gigabit Ethernet (ETH) and 2.4GHZ WI-FI</td>
</tr>
<tr>
  <td>USB </td>
  <td>1 x USB2.0HS used for OTG or HOST<br>1 x USB-UART</td>
</tr>
<tr>
  <td>Others</td>
  <td>1 User key，<br>3 x System keys，<br>1 x RTC，<br>2 x LEDs</td>
</tr>
<tr>
  <td>Interface</td>
  <td>Reserved CJTAG，used for connecting corresponding debugger，<br> 2 x 12 pin headers，<br>4 x M2.5 screw positioning holes</td>
</tr>
</tbody>
</table>

[Hardware summary informations](https://dl.sipeed.com/shareURL/MaixIII/AXera)

- [Datasheet](https://dl.sipeed.com/shareURL/MaixIII/AXera/01_Specification)
- [Schematic](https://dl.sipeed.com/shareURL/MaixIII/AXera/02_Schematic)
- [Bit map](https://dl.sipeed.com/shareURL/MaixIII/AXera/03_Bit_number_map)
- [3D file](https://dl.sipeed.com/shareURL/MaixIII/AXera/05_3D_file)
- [Dimension](https://dl.sipeed.com/shareURL/MaixIII/AXera/04_Dimensional_drawing)
- [GC4653 Camera DS](https://dl.sipeed.com/shareURL/MaixIII/AXera/07_Chip_manual)

### Camera comparison

- Low-end camera gc4653 400w basic experience

<p align="center">
  <img src="./../../../zh/maixIII/assets/ax620a_gc.jpg" style="zoom: 100%;" />
</p>

- High-end camera os04a10 400w enhanced night vision edition

<p align="center">
  <img src="./../../../zh/maixIII/assets/ax620a_os.jpg" style="zoom: 100%;" />
</p>

> [How to change camera](https://wiki.sipeed.com/hardware/en/maixIII/ax-pi/faq_axpi.html)

## Others

- Online AI: https://maixhub.com
- Documents: https://wiki.sipeed.com
- Telegram: https://t.me/sipeed
- Github: https://github.com/sipeed

> Visit [Maix-III AXera-Pi (FAQ)](https://wiki.sipeed.com/hardware/en/maixIII/ax-pi/faq_axpi.html) if you have trobule.
