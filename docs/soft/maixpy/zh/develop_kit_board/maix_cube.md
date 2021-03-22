---
title: MaixCube
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: MaixCube
---


## 概述

  SIPEED **MaixCube** 可开发编程学习套件, MaixCube 在硬件上集成 30W 摄像头、可扩展 TF 卡槽、用户按键、IPS 1.3 寸显示屏、200mAh 锂电池、扬声器,麦克风、SPMOD,GROVE 扩展接口等。
  软件上 MaixCube 默认搭载 MaixPy, 用户可以非常轻松的使用 MicroPython 语法快速上手 AI IoT 开发，开发人脸识别，物体识别等 AI 应用，同时还预留开发调试接口，也能将其作为一款功能强大的 AI 学习开发板。

## 外观及功能介绍

### 外观一览

![Maix Cube](../../assets/hardware/maix_cube/maixcube_product_appearance.png)

### 板载功能

| 项目         | 说明                                                     |
| ------------ | -------------------------------------------------------- |
| CPU：        | 双核 64bit RISC-V / 400MHz (双精度FPU集成)               |
| 内存：       | 8MiB 64bit 片上 SRAM                                     |
| 存储：       | 16MiB Flash, 支持 micro SDXC 拓展存储 (最大128GB)        |
| 屏幕：       | 1.3 寸 **IPS** 屏幕：分辨率 **240*240**                  |
| 摄像头：     | 搭载 **0V7740** **30W** 像素 **Sensor**                  |
| 按键：       | 复位按键，电源按键（短按开机，长按 *8S* 关机），三向按键 |
| USB：        | Type-C 接口，正反盲插                                    |
| 音频：       | 支持音频录制，播放，驱动 IC（ES8374）                    |
| 板载传感器： | 三轴加速度传感器（MSA301）                               |
| 灯：         | 板载两颗 RGB LED，一颗闪光灯                            |
| TF 卡槽：    | 多媒体资源扩展，支持大容量储存                           |
| 电源管理：   | AXP173 控制单元，200mAh 锂电池，支持用户充放电控制       |

### 引脚资源

![Maix Cube](../../assets/hardware/maix_cube/maixcube_resources.png)

### 板载扩展接口

Maix Cube 对用户开放了两种高度扩展的接口：一个 [SP-MOD](../modules/sp_mod/README.md) 与 一个 [Grove](./../modules/grove/README.md) 接口，用户可以很方便的进行 DIY

### 板载 I2C 设备

MaixCube  板载 I2C 传感器/IC

| IC     | 设备 id     | I2C 地址(7位地址) | MaixPy 读取地址  | 示例代码 |
| ------ | ----------- | ----------------- | ---------------------------- |----|
| ES8374 | 0x08        | 0x10              | D(16)                        |[code](https://github.com/sipeed/MaixPy_scripts/blob/79a5485ec983e67bb8861305a52418b29e0dc205/modules/others/es8374/es8374.py)|
| MSA301 | 0x13        | 0x26              | D(38)                        |[code](https://github.com/sipeed/MaixPy_scripts/blob/7fea2359a7f0c05f586be915aa8e6112262e0caa/multimedia/gui/maixui/msa301.py)|
| AXP173 | 0x68        | 0x34              | D(52)                        |[code](https://github.com/sipeed/MaixPy_scripts/blob/7fea2359a7f0c05f586be915aa8e6112262e0caa/multimedia/gui/maixui/pmu_axp173.py)|


## 上手把玩

由于 MaixCube 出厂自带 GUI 演示界面和示例程序，所以在拿到板子时可以先上手把玩下预设程序，
在之后那么我们就开始以 MaixCube 上手，借助 MaixPy 入门 AIoT.

而在开发之前我们需要了解并准备相关工具，以减少我们后边因为准备不足而走的坑路

上手步骤:

1. 下载需要的驱动，软件
2. 开发板连接电脑，并安装 USB 驱动
3. 更新最新固件
4. 下载并打开最新的 MaixPy IDE
5. MaixPy IDE 连接开发板 运行 MaixPy 示例程序

### 软硬件准备

硬件准备:

  - **电脑**一台
  - **MaixCube** 开发板
  - **可靠**的 USB Type-C 数据线一条：注意一定要**可靠**的数据线

软件准备:

  - USB 驱动：**FT2232** ->[[下载链接点这里](https://dl.sipeed.com/MAIX/tools/ftdi_vcp_driver)](https://dl.sipeed.com/MAIX/tools/ftdi_vcp_driver)
  - Kflash_gui：[https://dl.sipeed.com/MAIX/tools/kflash_gui](https://dl.sipeed.com/MAIX/tools/kflash_gui)
  - MaixPy IDE ：[https://dl.sipeed.com/MAIX/MaixPy/ide/_/v0.2.5](https://dl.sipeed.com/MAIX/MaixPy/ide/_/v0.2.5)
  - 例程程序库：[https://github.com/sipeed/MaixPy_scripts](https://github.com/sipeed/MaixPy_scripts)

###  安装驱动

我们在拿到 Maix Cube 并连接到电脑的时候，可以打开设备管理器查看串口驱动是否已经安装，打开设备管理器的方法有:
- 此电脑(右键) -> 属性 -> 设备管理器
- 开始菜单(右键) -> 设备管理器
- 控制面板 -> (搜索)设备管理器

  <img src="../../assetcs/../assets/get_started/win_device_1.png" height="400">

1. 当我们的系统是 Win10 系统，系统则会帮我们自动安装驱动，而如果是旧版 Win7，win8 系统我们就需要自己手动安装:
    ![](../../assetcs/../assets/get_started/win_device_2.png)

1. 打开上一节的的链接下载驱动
    ![](../../assetcs/../assets/get_started/win_device_3.png)
1. 点击安装
    ![](../../assets/get_started/drives.gif)
1. 安装完成之后，可以在设备管理器看到已经识别到两个串口设备了
    ![](../../assetcs/../assets/get_started/win_device_4.png)


### 更新固件到最新版

  用户拿到开发板之后，板载的固件默认或许已经不是最新版的，那么在使用过程中会存在或多或少的 bug，
  我们这时候就需要更新固件版本到最新版本

  更新方法查看：[更新固件](../get_started/upgrade_maixpy_firmware.md)



###  运行第一个程序 `Hello World`


- LCD 实时预览 Camera（使用 MaixPy IDE 连接时型号选择 Maixduino 即可）

```python
import sensor, image, time, lcd

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_hmirror(1)
sensor.set_vflip(1)

clock = time.clock()

lcd.init(type=2)
lcd.rotation(2)

while(True):
    clock.tick()
    img = sensor.snapshot()
    print(clock.fps())
    img.draw_string(60, lcd.height()-120, "fps:"+str(clock.fps()), lcd.GREEN, scale=2)
    lcd.display(img)

```

## 资料下载

Sipeed-Maix-Cube 资料下载：[Sipeed-Maix-Cube](https://dl.sipeed.com/shareURL/MAIX/HDK/Sipeed-Maix-Cube)

Sipeed-Maix-Cube 规格书下载：[Sipeed-Maix-Cube](https://dl.sipeed.com/fileList/MAIX/HDK/Sipeed-Maix-Cube/ProductSpecification/Sipeed%20Maix%20Cube%20Datasheet%20V1.0.pdf)

Sipeed-Maix-Cube 原理图下载：[Sipeed-Maix-Cube][Sipeed-Maix-Cube]

[Sipeed-Maix-Cube]: https://dl.sipeed.com/fileList/MAIX/HDK/Sipeed-Maix-Cube/Maix-Cube-2757/Maix-Cube-2757(Schematic).pdf
