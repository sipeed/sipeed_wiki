---
title: Sipeed 开源产品速览
keywords: Sipeed, Hardware, 矽速, 硬件资料, 文档, 资料下载, 深度学习, 人工智能, K210
desc: 矽速科技的开源软硬件 WIKI 资料站
---

## 总览

- [Maix Zero](https://wiki.sipeed.com/hardware/zh/index.html#Maix-Zero) 以 MCU 为主控的 AIOT 开发板
- [Maix-I](https://wiki.sipeed.com/hardware/zh/index.html#Maix-I) 以 MCU 为主控的 AI 开发板
- [Maix-II](https://wiki.sipeed.com/hardware/zh/index.html#Maix-II-系列)：Linux AI 开发板，小巧便携且实用
- [Maix-III](https://wiki.sipeed.com/hardware/zh/index.html#Maix-III)： Linux AI 开发板，超强算力超大内存多种玩法
- [LicheePI](https://wiki.sipeed.com/hardware/zh/index.html#LicheePi-系列)： Linux 开发板
- [Tang](https://wiki.sipeed.com/hardware/zh/index.html#Tang-FPGA-系列)：FPGA 开发板
- [MaixSense](https://wiki.sipeed.com/hardware/zh/index.html#Maixsense-系列)：3D TOF 模组
- [SLogic](https://wiki.sipeed.com/hardware/zh/index.html#SLogic-系列): 多功能逻辑分析仪
- [Longon](https://wiki.sipeed.com/hardware/zh/index.html#Longon-系列)：MCU 开发板
- [MaixFace](https://wiki.sipeed.com/hardware/zh/index.html#Maixface-模组)：商业项目板卡
- [其他外设](https://wiki.sipeed.com/hardware/zh/index.html#外设模组)

## Maix Zero

| 项目     | M0S                                                                             | M0P                                                                                               | M0sense                                                                     |
| :------- | :------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------- |
| 主控     | BL616                                                                           | BL618                                                                                             | BL702                                                                       |
| 核心     | RV32GCP@320MHz                                                                  | RV32@320MHz                                                                                       | RV32@144MHz                                                                 |
| RAM      | 480KB                                                                           | 480KB                                                                                             | 132KB                                                                       |
| 储存     | 内置 4MB Flash                                                                  | 内置 8MB Flash                                                                                    | 内置 192KB ROM, 512KB Flash                                                 |
| 无线     | · Wifi<br>· 蓝牙<br>· Zigbee                                                    | · Wifi<br>· 蓝牙<br>· Zigbee                                                                      | 蓝牙                                                                        |
| 模型平台 | [MaixHub](https://www.maixhub.com)                                              | [MaixHub](https://www.maixhub.com)                                                                | [MaixHub](https://www.maixhub.com)                                          |
| 尺寸     | 11(L)x10(W)mm                                                                   | 25.5(L) x 18(W) mm                                                                                |                                                                             |
| 详情页   | [点我](./maixzero/m0s/m0s.md)                                                   | [点我](./maixzero/m0p/m0p.md)                                                                     | [点我](./maixzero/sense/maix_zero_sense.md)                                 |
| 外观图   | <img src="./maixzero/m0s/assets/m0s/m0s_pin_map.png" alt="m0sense" width="230"> | <img src="./maixzero/m0p/assets/m0p/m0p_module_outlook.png" alt="m0p_module_outlook" width="230"> | <img src="./maixzero/sense/assets/m0sense_1.png" alt="m0sense" width="230"> |

## Maix-I

| 项目     | M1/M1w                             | M1n                                | M1s                                                |
| :------- | :--------------------------------- | :--------------------------------- | :------------------------------------------------- |
| 主控     | K210                               | K210                               | BL808                                              |
| 核心     | RV64@400MHz \* 2                   | RV64@400MHz \* 2                   | RV64GCV@480MHz<br>RV32GCP@320MHz<br>RV32EMC@160MHz |
| RAM      | 8MB                                | 8MB                                | 64MB                                               |
| 无线     | M1w 支持 Wifi                      |                                    | · Wifi<br>· 蓝牙<br>· Zigbee                       |
| 封装样式 | 邮票孔                             | 金手指                             | 邮票孔                                             |
| 模型平台 | [MaixHub](https://www.maixhub.com) | [MaixHub](https://www.maixhub.com) | [MaixHub](https://www.maixhub.com)                 |
| 尺寸     | 25.4(L)x25.4(W)mm                  | 25.0(L)x22.0(W)mm                  | 31.0(L)x18.0(W)mm                                  |
| 详情页   | [点我](./maix/core_module.md)      | [点我](./maix/M1n.md)              | [点我](./maix/m1s/m1s_module.md)                   |

### Maix-I S

这是一款以博流 808 为主控所制作的 AIOT 模组与核心板

|      | [M1s](./maix/m1s/m1s_module.md)                                                                                                                                                                                   | [M1s Dock](./maix/m1s/m1s_dock.md)                                                                                                                                                                                   |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 图片 | <a href="https://wiki.sipeed.com/m1s"><img src="https://gd4.alicdn.com/imgextra/i4/2200606237318/O1CN011g9yY323vhCXEyiKU_!!2200606237318.jpg" style="transform:rotate(270deg);" alt="M1s_module" width="80%"></a> | <a href="https://wiki.sipeed.com/m1s#dock"><img src="https://gd1.alicdn.com/imgextra/i1/2200606237318/O1CN01gE4a1E23vhCV77ggE_!!2200606237318.jpg" style="transform:rotate(270deg);" alt="M1s_Dock" width="80%"></a> |

### Maix-I

这是 2019 年以 K210 为核心所制作的一系列 AIOT 开发板。

<table role="table" class="center_table">
    <tbody>
        <tr>
            <th scope="col"></th>
            <th scope="col">Maix Bit</th>
            <th scope="col">Maix Dock</th>
            <th scope="col">Maix Duino</th>
            <th scope="col">Maix nano</th>
        </tr>
        <tr>
             <td style="white-space:nowrap">图片</td>
            <td> <a href="./maix/maixpy_develop_kit_board/maix_bit.html"
                    target="_blank"><img
                        src="./maix/assets/dk_board/maix_bit/Bit.png" ></a> </td>
            <td><a href="./maix/maixpy_develop_kit_board/Maix_dock.html"
                    target="_blank"><img
                        src="./maix/assets/dk_board/maix_dock/Dan_Dock.png" ></a></td>
            <td><a href="./maix/maixpy_develop_kit_board/maix_duino.html"
                    target="_blank"><img
                        src="./maix/assets/dk_board/maix_duino/maixduino_0.png" ></a></td>
            <td><a href="./maix/maixpy_develop_kit_board/maix_nano.html"><img
                        src="./maix/assets/dk_board/maix_nano/maix_nano.jpg"  alt="Maxi nano"></a></td>
        </tr>
        <tr>
            <th scope="col"></th>
            <th scope="col">Maix Cube</th>
            <th scope="col">Maix Amigo</th>
            <th scope="col">Maix HAT</th>
            <th scope="col">Maix Go</th>
        </tr>
        <tr>
             <td style="white-space:nowrap">图片</td>
            <td><a href="./maix/maixpy_develop_kit_board/maix_cube.html"
                    target="_blank"><img
                        src="./maix/assets/dk_board/maix_cube/maix_cube.png" ></a></td>
            <td><a href="./maix/maixpy_develop_kit_board/maix_Amigo.html"
                    target="_blank"><img
                        src="./maix/assets/dk_board/maxi_amigo/maix_amigo_0.png" ></a></td>
            <td><a href="./maix/maixpy_develop_kit_board/maix_hat.html"><img
                        src="./../../soft/maixpy/assets/hardware/grove_ai_hat/grove_ai_hat1.png"  alt="Maix HAT"></a></td>
            <td><a href="./maix/maixpy_develop_kit_board/maix_go.html"
                    target="_blank"><img
                        src="./maix/assets/dk_board/maix_go/Go.jpg"  ></a></td>
        </tr>
    </tbody>
</table>

### 产品支持

Maix 系列产品可以在多种场景实现客户不同方面的需要，在 AIoT 上已经广泛的使用，品质和性能在行业内已经有非常好的口碑，专业的技术团队为广大客户解决硬件设计和软件功能上的各种各样问题。商业合作可以联系 <support@sipeed.com>。

## Maix-II

| 项目     | MaixII-Dock                                                                                                                                                                                                                    | MaixII-Sense                                                                                                                                                            | MaixII-S                                                                                                                                                            |
| :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 主控     | V831                                                                                                                                                                                                                           | R329                                                                                                                                                                    | V833                                                                                                                                                                |
| 核心     | Cortex A7@800MHz                                                                                                                                                                                                               | Cortex A53\*2@1.5GHz                                                                                                                                                    | Cortex A7@1.2GHz                                                                                                                                                    |
| RAM      | 64MB                                                                                                                                                                                                                           | 256MB                                                                                                                                                                   | 默认 128MB                                                                                                                                                          |
| 无线     | Wifi                                                                                                                                                                                                                           | · Wifi<br>· 蓝牙                                                                                                                                                        | · Wifi                                                                                                                                                              |
| 外观图   | <img src="https://gd3.alicdn.com/imgextra/i3/2200606237318/O1CN01dT63dq23vhAOtdtm7_!!2200606237318.png_400x400.jpg" style="transform:rotate(0deg);" alt="MaixII-Dock">                                                         | <img src="https://gd3.alicdn.com/imgextra/i3/2200606237318/O1CN01AJdLYs23vh6b40oy2_!!2200606237318.png_400x400.jpg" style="transform:rotate(0deg);" alt="MaixII-Sense"> | <img src="https://gd2.alicdn.com/imgextra/i2/2200606237318/O1CN01C4iTYi23vh6muQApg_!!2200606237318.png_400x400.jpg" style="transform:rotate(0deg);" alt="MaixII-S"> |
| 模型平台 | [MaixHub](https://www.maixhub.com)                                                                                                                                                                                             |                                                                                                                                                                         |                                                                                                                                                                     |
| 详情页   | [点我](http://wiki.sipeed.com/m2dock)                                                                                                                                                                                          | [点我](./maixii/m2a/maixsense.md)                                                                                                                                       | [点我](./maixii/M2S/V833.md)                                                                                                                                        |
| 备注     | <strong>推荐产品</strong>，高性价比能跑 Linux 的 SOC，同时支持硬件 AI 加速（0.2Tops 算力），目前软件支持最容易入门，提供 C SDK 和 Python SDK， 以及在线模型训练服务(<a href="https://maixhub.com" target="_blank">MaixHub</a>) | 有提供硬件 AI 加速，0.25Tops 算力。                                                                                                                                     | 仅支持商业                                                                                                                                                          |

## Maix-III

目前 Maix-III axpi 是最新款的 AI 开发板，拥有高算力、大内存、多种接口，支持超多算子。强烈推荐。

| 项目       | MaixIII-axpi                                                                                                                                                                        |
| :--------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 主控       | Ax620a                                                                                                                                                                              |
| 核心       | Cortex A7\*4@1.0GHz                                                                                                                                                                 |
| NPU        | 14.4Tops@int4，3.6Tops@int8                                                                                                                                                         |
| ISP        | 4K@30fps                                                                                                                                                                            |
| RAM        | 2GB LPDDR4X 3733Mhz                                                                                                                                                                 |
| 摄像头输入 | 默认单摄, 最高支持 3 摄:<br>1 个 MIPI4-LANE+2 个 MIPI2-LANE                                                                                                                         |
| 屏幕输出   | 支持最高 4-LANE MIPI DSI 屏幕                                                                                                                                                       |
| 网络接口   | 支持 千兆以太网（ETH） 和 2.4GHZ WI-FI 板载天线                                                                                                                                     |
| USB 接口   | 1xUSB2.0HS 支持 OTG 或 HOST 功能，<br>1xUSB-UART 系统串口                                                                                                                           |
| 外观图     | <img src="https://gd2.alicdn.com/imgextra/i2/2200606237318/O1CN01AY6Mu123vhBaHWr6H_!!2200606237318.jpg_400x400.jpg" style="transform:rotate(0deg);" alt="MaixIII-Axpi" width="40%"> |
| 模型平台   | [MaixHub](https://www.maixhub.com)                                                                                                                                                  |

更多内容请前往[详情页](./maixIII/ax-pi/axpi.md)查看

## Lichee

### Lichee 4A

- 使用 TH1520 SOC 的设备

|      | Lichee Pi 4A                                  |
| :--- | :-------------------------------------------- |
| 外观 | ![](./../assets/lichee/th1520/licheepi4a.png) |

### Lichee Linux

- Lichee Linux 开发板使用了全志科技的 SOC 芯片，是为了实战 linux 底层相关的内容的产品。

| 类别      | Lichee RV    | Lichee Zero Plus                             | Lichee Zero                    | Lichee nano         |
| :-------- | :----------- | :------------------------------------------- | :----------------------------- | :------------------ |
| SOC       | Allwinner D1 | Allwinner S3                                 | Allwinner V3s                  | Allwinner F1c100s   |
| CPU 架构  | 玄铁 C906    | Cortex™-A7                                   | Cortex™-A7                     | ARM 926EJS          |
| 运行频率  | 1GHz         | 1.2GHz                                       | 1.2GHz(max)                    | 600MHz(max)         |
| RAM       | 512MB DDR3   | 128Mbyte DDR3                                | 64MB DRAM                      | 32MB DDR            |
| FLASH     | 可选 SD-nand | 可选 SD Nand、<br>SPI Nor Flash<br>或者 eMMC | 预留<br>SOP8 SPI Flash<br>焊盘 | 板载 16MB NOR FLASH |
| TF 连接器 | 有           | 有                                           | 有                             | 有                  |

<table>
<thead>
<tr>
<th style="text-align:center">Lichee Zero</th>
<th style="text-align:center">Lichee Nano</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center"><a href="./lichee/Zero/Zero.html"><img src="./lichee/assets/Zero/Zero_1.png" alt="Lichee Zero"></a></td>
<td style="text-align:center"><a href="./lichee/Nano/Nano.html" ><img src="./lichee/assets/Nano/Nano_2.png" alt="Lichee Nano"></a></td>
</tr>
</tbody>
<thead>
<tr>
<th style="text-align:center">Lichee Zero Plus</th>
<th style="text-align:center">Lichee RV</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center"><a href="./lichee/ZeroPlus/ZeroPlus.html"><img src="./lichee/assets/Zero-Plus/Plus_1.jpg" alt="Tang Nano 4K"></a></td>
<td style="text-align:center"><a href="./lichee/RV/RV.html"><img src="./lichee/assets/RV/D1-4.png" alt="Lichee RV"></a></td>
</tr>
</tbody>
</table>


### Lichee 4A

Lichee 4A 是使用了 TH1520 芯片的一系列设备，目前有 Lichee Module 4A 和 Lichee Pi 4A 两款产品

Lichee Module 4A 介绍：[点我](https://wiki.sipeed.com/licheem4a)
Lichee Pi 4A 介绍：[点我](https://wiki.sipeed.com/licheepi4a)

| 条目 | 说明 |
|:---|:---|
|主控芯片|	TH1520|
|CPU处理器|	RISC-V 64GCV C910*4@1.85GHz <br>· 每核支持 64KB I cache 和 64KB D Cache<br>· 四核共享 1MB L2 Cache<br>· 支持 TEE 和 REE，TEE/REE 支持核数启动时可配置<br>· 支持自定义且接口兼容 RISC-V 的多核调试框架<br>· 独立电源域，支持 DVFS|
|图形处理器|	· OpenCL 1.1/1.2/2.0<br>· OpenGL ES 3.0/3.1/3.2<br>· Vulkan 1.1/1.2<br>· Android NN HAL<br>|
|NPU处理器|	支持 4TOPS@INT8 通用 NNA 算力，主频 1GHz<br>· 支持 TensorFlow、ONNX、Caffe<br>· 支持 CNN、RNN、DNN 等<br>|
|视频解码器|	实时解码器，支持 H.265/H.264/VP9/8/7/6/AVS/AVS+/AVS2.0/VC1/MPEG4<br>· 支持 H.264 BP/MP/HP@level 5.1 解码，最大 4K 分辨率<br>· 支持 H.265/HEVC Main Profile@level 5.1 解码，最大 4K 分辨率<br>· 支持 VP9 Profile-2 解码，最大 4K 分辨率<br>· 支持 AVS2.0 解码，最大 4K 分辨率<br>· 支持 VP6/7/8/AVS/AVS+/VC1/MPEG4 解码，最大 1920x1080 分辨率<br>· 解码性能最大 4K@75fps|
|视频编码器|	· 支持 H.264 BP/MP/HP@level4.2 编码，最大 4K 分辨率<br>· 支持 H.265/HEVC Main Profile 编码，最大 4K 分辨率<br>· 仅支持 I 帧和 P 帧<br>· 编码性能最大 4K@40fps|

## Tang FPGA 系列

Tang FPGA 目前分为 Tang Nano 和 Tang Primer 两个系列。
- Tang Nano 是尽可能小体积的核心板
- Tang Primer 是多引脚多拓展性的开发板。

### Tang Nano

| 项目            | <p style="white-space:nowrap">Tang Nano 20K</p> | <p style="white-space:nowrap">Tang Nano 9K</p> | <p style="white-space:nowrap">Tang Nano 4K</p> | <p style="white-space:nowrap">Tang Nano 1K</p> |
| :-------------- | :---------------------------------------------- | :--------------------------------------------- | :--------------------------------------------- | ---------------------------------------------- |
| 逻辑单元(LUT4)  | 20736                                           | 8640                                           | 4608                                           | 1152                                           |
| 寄存器（FF）    | 15552                                           | 6480                                           | 3456                                           | 864                                            |
| S-SRAM (bits)   | 41472                                           | 17280                                          |                                                |                                                |
| B-SRAM (bits)   | 828K                                            | 468K                                           | 180K                                           | 72K                                            |
| 用户闪存 (bits) |                                                 | 608K                                           | 256K                                           | 96K                                            |
| 锁相环 (PLL)    | 2                                               | 2                                              | 2                                              | 1                                              |
| RAM             | 32bits SDR SDRAM                                | 16 bits PSRAM                                  | 8bits HyperRam                                 |                                                |
| RAM 容量        | 64Mb                                            | 64M                                            | 64Mb                                           |                                                |
| 板载 Flash      | 64Mbits NOR Flash                               | 32Mbits NOR Flash                              | 32Mbits NOR Flash                              | 预留焊盘                                       |
| 硬核处理器      |                                                 |                                                | Cortex-M3                                      |                                                |

<table>
<thead>
<tr>
<th style="text-align:center">Tang Nano 20K</th>
<th style="text-align:center">Tang Nano 9K</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center"><a href="./tang/tang-nano-20k/nano-20k.html"><img src="./../assets/Tang/nano_20k/tang_nano_20k_3920_top.png" alt="Tang Nano 20K"></a></td>
<td style="text-align:center"><a href="./tang/Tang-Nano-9K/Nano-9K.html"><img src="./../assets/Tang/Nano-9K/9K.png" alt="Tang Nano 9K"></a></td>
</tr>
</tbody>
<thead>
<tr>
<th style="text-align:center">Tang Nano 4K</th>
<th style="text-align:center">Tang Nano 1K</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center"><a href="./tang/Tang-Nano-4K/Nano-4K.html"><img src="./../assets/Tang/Nano_4K/Nano_4K.png" alt="Tang Nano 4K"></a></td>
<td style="text-align:center"><a href="./tang/Tang-Nano-1K/Nano-1k.html"><img src="./../assets/Tang/Nano-1K/1K.png" alt="Tang Nano 1K"></a></td>
</tr>
</tbody>
</table>

### Tang Primer

| 项目           | <p style="white-space:nowrap">Tang Primer 20K</p>                                                | <p style="white-space:nowrap">Tang Primer 25K</p> |
| :------------- | :----------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| 逻辑单元(LUT4) | 20736                                                                                            | 23040                                             |
| 寄存器（FF）   | 15552                                                                                            | 23040                                             |
| S-SRAM (bits)  | 41472                                                                                            | 180K                                              |
| B-SRAM (bits)  | 828K                                                                                             | 1008K                                             |
| 锁相环 (PLL)   | 4                                                                                                |                                                   |
| 板载内存       | 16bits DDR3 RAM                                                                                  |                                                   |
| 板载内存容量   | 128MB                                                                                            |                                                   |
| 板载 Flash     | 32Mbits NOR Flash                                                                                |                                                   |
| 核心板照片     | <img src="./../assets/Tang/primer_20k/primer_20k.png" alt="Tang Primer 20K（核心板）" width=45%> |                                                   |
| 底板数量       | 2                                                                                                |                                                   |
| 详情页         | <a href="./tang/tang-primer-20k/primer-20k.html"> 点我 </a>                                      |                                                   |

### 售罄产品

|                                   Tang Nano                                   |                                          Tang Primer                                           |
| :---------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------: |
| [![Tang Nano](./../assets/Tang/Nano/Tang_Nano.jpg)](./tang/Tang-Nano/Nano.md) | [![Tang Primer](./../assets/Tang/permier/Tang_permier.jpg)](./tang/Tang-primer/Tang-primer.md) |

## MaixSense 系列

- 基于 TOF 技术的深度相机

|                                                | Maixsense-a010                               | MaixSense-a075V                             |
| ---------------------------------------------- | -------------------------------------------- | ------------------------------------------- |
| 图片                                           | ![me_small](./maixsense/assets/me_small.jpg) | ![me_big](./maixsense/assets/me_big.jpg)    |
| 接口                                           | 1.25mm 串口连接器 \*1<br>Type-C USB2.0 \*1   | 1.25mm 串口连接器 \*1 <br>Type-C USB2.0 \*1 |
| 分辨率                                         | TOF：100x100@30fps                           | RGB：1600x1200@30fps<br>TOF：320x240@60fps  |
| 视场角                                         | RGB：无<br>TOF：70°(H) \* 60°(V)             | RGB：120°<br>TOF：55°(H)\*72°(H)            |
| <p style="white-space:nowrap">TOF 像素尺寸</p> |                                              | 15um                                        |
| 激光发射器                                     | 40nm VCSEL                                   | 940nm,3W                                    |
| 测量范围                                       | 0.2-2.5m                                     | 0.15-1.5m                                   |
| 测量精度                                       | &lt;=1%/cm                                   | &lt;=1%/cm                                  |

## SLogic 系列

SLogic 全称为 Sipeed Logic Analyzer，是逻辑分析仪。

<!-- |                  | Lite8                                         | Combo8                                        |
| ---------------- | --------------------------------------------- | --------------------------------------------- |
| 采样芯片         | BL616                                         | BL616                                         |
| 通讯方式         | USB2.0   HS                                   | USB2.0   HS                                   |
| 采样率@通道数    | 160M@2Channel<br>80M@4Channel<br>40M@8Channel | 160M@2Channel<br>80M@4Channel<br>40M@8Channel |
| 信号输入范围     | 0～3.6V                                       | 0～3.6V                                       |
| 高低电平识别范围 | VIH: >2V<br>VIL: <0.8V                        | VIH: >2V<br>VIL: <0.8V                        |
| CKLink 功能      |                                               | 支持                                          |
| DapLink 功能     |                                               | 支持                                          |
| 串口功能         |                                               | 支持四串口功能，每个串口最大20MBps            |

SLogic Combo8 功能指示

| LED 状态 | 功能 |
| --- | --- |

| 111 | SLogic | 110 | UARTx4 | 101 | DAPLink | 100 | CKLink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CH7 | CH6 | RX1 | RX3 | RTS | TMS/SWDIO | RTS | TMS |
| CH5 | CH4 | TX1 | TX3 | DTR | TDO | DTR | TDO |
| CH3 | CH2 | RX0 | RX2 | RXD | TDI | RXD | TDI |
| CH1 | CH0 | TX0 | TX2 | TXD | TCK/SWCLK | TXD | TCK |
| 3V3 | 5V | 3V3 | 5V | 3V3 | 5V | 3V3 | 5V  |
| GND | GND | GND | GND | GND | GND | GND | GND | -->

## Longon 系列

MCU 开发板

<img src="./longan/Nano/assets/longan_nano.jpg" alt="longan_nano" width="40%">

详情页：[点我](./longan/Nano/assets/readme.md)

## MaixFace 模组

- 商业合作模组，无个人支持

前往首页商业方案板块查看对应设备

## 外设模组

前往首页外设模组板块查阅对应设备
