---
title: Sipeed 开源产品速览
keywords: Sipeed, Hardware, 矽速, 硬件资料, 文档, 资料下载, 深度学习, 人工智能, K210
desc: 矽速科技的开源软硬件 WIKI 资料站
---

## 总览

- [Maix-I & Zero](#maix-i--zero) 以 MCU 为主控的 AI 开发板
- [Maix II & III](#maix-ii--iii-系列)： 基于 Linux 系统的 AI 开发板
- [LicheePI](#licheepi-系列)： Linux 开发板
- [Tang](#tang-fpga-系列)：FPGA 开发板
- [MaixSense](#maixsense-系列)：3D TOF 模组
- [Longon](#longon-系列)：MCU 开发板
- [MaixFace](#maixface-模组)：商业项目板卡
- [其他外设](#外设模组)

## Maix-I & Zero 

| 项目     | M1/M1w                             | M1n                                | M1s                                                | M0                                          |
| :------- | :--------------------------------- | :--------------------------------- | :------------------------------------------------- | :------------------------------------------ |
| 主控     | K210                               | K210                               | BL808                                              | BL702                                       |
| 核心     | RV64@400MHz * 2                    | RV64@400MHz * 2                    | RV64GCV@480MHz<br>RV32GCP@320MHz<br>RV32EMC@160MHz | RV32@144MHz                                 |
| RAM      | 8MB                                | 8MB                                | 64MB                                               | 132KB                                       |
| 无线     | M1w 支持 Wifi                      |                                    | · Wifi<br>· 蓝牙<br>· Zigbee                       | 蓝牙                                        |
| 封装样式 | 邮票孔                             | 金手指                             | 邮票孔                                             |                                             |
| 模型平台 | [MaixHub](https://www.maixhub.com) | [MaixHub](https://www.maixhub.com) | [MaixHub](https://www.maixhub.com)                 | [MaixHub](https://www.maixhub.com)          |
| 尺寸     | 25.4(L)x25.4(W)mm                  | 25.0(L)x22.0(W)mm                  | 31.0(L)x18.0(W)mm                                  |                                             |
| 详情页   | [点我](./maix/core_module.md)      | [点我](./maix/M1n.md)              | [点我](./maix/m1s/m1s_module.md)                   | [点我](./maixzero/sense/maix_zero_sense.md) |

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
            <td><a href="./maix/maixpy_develop_kit_board/maix_go.html"><img
                        src="./../../soft/maixpy/assets/hardware/grove_ai_hat/grove_ai_hat1.png"  alt="Maix HAT"></a></td>
            <td><a href="./maix/maixpy_develop_kit_board/maix_go.html"
                    target="_blank"><img
                        src="./maix/assets/dk_board/maix_go/Go.jpg"  ></a></td>
        </tr>
    </tbody>
</table>

### Maix Zero

这是一款以博流 702 为主控所制作的极小开发板

<img src="./maixzero/sense/assets/m0sense_1.png" alt="m0sense" width=35%>

详情页 ：[点我](./maixzero/sense/maix_zero_sense.md)

### 产品支持

Maix 系列产品可以在多种场景实现客户不同方面的需要，在 AIoT 上已经广泛的使用，品质和性能在行业内已经有非常好的口碑，专业的技术团队为广大客户解决硬件设计和软件功能上的各种各样问题。商业合作可以联系 <support@sipeed.com>。

## Maix-II & III 系列

| 项目     | MaixII-Dock                                                                                                                                                            | MaixII-Sense                                                                                                                                                            | MaixII-S                                                                                                                                                            | MaixIII-axpi                                                                                                                                                            |
| :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 主控     | V831                                                                                                                                                                   | R329                                                                                                                                                                    | V833                                                                                                                                                                | Ax620a                                                                                                                                                                  |
| 核心     | Cortex A7@800MHz                                                                                                                                                       | Cortex A53\*2@1.5GHz                                                                                                                                                    | Cortex A7@1.2GHz                                                                                                                                                    | Cortex A7\*4@1.0GHz                                                                                                                                                     |
| RAM      | 64MB                                                                                                                                                                   | 256MB                                                                                                                                                                   | 默认128MB                                                                                                                                                           | 默认 1GB                                                                                                                                                                |
| 无线     | Wifi                                                                                                                                                                   | · Wifi<br>· 蓝牙                                                                                                                                                        | · Wifi                                                                                                                                                              | · Wifi<br>· 蓝牙                                                                                                                                                        |
| 模型平台 | [MaixHub](https://www.maixhub.com)                                                                                                                                     |                                                                                                                                                                         |                                                                                                                                                                     | [MaixHub](https://www.maixhub.com)                                                                                                                                      |
| 外观图   | <img src="https://gd3.alicdn.com/imgextra/i3/2200606237318/O1CN01dT63dq23vhAOtdtm7_!!2200606237318.png_400x400.jpg" style="transform:rotate(0deg);" alt="MaixII-Dock"> | <img src="https://gd3.alicdn.com/imgextra/i3/2200606237318/O1CN01AJdLYs23vh6b40oy2_!!2200606237318.png_400x400.jpg" style="transform:rotate(0deg);" alt="MaixII-Sense"> | <img src="https://gd2.alicdn.com/imgextra/i2/2200606237318/O1CN01C4iTYi23vh6muQApg_!!2200606237318.png_400x400.jpg" style="transform:rotate(0deg);" alt="MaixII-S"> | <img src="https://gd2.alicdn.com/imgextra/i2/2200606237318/O1CN01AY6Mu123vhBaHWr6H_!!2200606237318.jpg_400x400.jpg" style="transform:rotate(0deg);" alt="MaixIII-Axpi"> |
| 详情页   | [点我](http://wiki.sipeed.com/m2dock)                                                                                                                                       | [点我](./maixii/m2a/maixsense.md)                                                                                                                                       | [点我](./maixii/M2S/V833.md)                                                                                                                                        | [点我](./maixIII/ax-pi/axpi.md)                                                                                                                                         |
| 备注     |                                                                                                                                                                        |                                                                                                                                                                         | 仅支持商业                                                                                                                                                          |                                                                                                                                                                         |

### Maix-II

MAIX-II 系列包含多款硬件产品，目前有三款产品，分别如下：

<table>
<thead>
<tr>
  <th>产品名称</th>
  <th>板卡简述</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="white-space:nowrap"><strong>Maix-II Dock</strong></td>
  <td><strong>推荐产品</strong>，主控芯片为全志 V831, 高性价比能跑 Linux 的SOC，同时支持硬件 AI 加速（0.2Tops 算力），目前软件支持最容易入门，提供 C SDK 和 Python SDK， 以及在线模型训练服务(<a href="https://maixhub.com" target="_blank">MaixHub</a>)</td>
</tr>
<tr>
  <td style="white-space:nowrap"><strong>Maix-II Sense</strong></td>
  <td>芯片为全志R329，也有提供硬件 AI 加速，0.25Tops 算力。</td>
</tr>
<tr>
  <td style="white-space:nowrap"><strong>Maix-II-S</strong></td>
  <td>芯片为全志 V833，V831 升级版， 主要用于商业定制用途，个人用户慎重选择。</td>
</tr>
</tbody>
</table>

### MaixIII

目前 MaixIII axpi 是最新款的 AI 开发板，强烈推荐

![maix-iii-small](./../assets/maixIII/ax-pi/maix-iii-small.png)

详情页：[点我跳转](./maixIII/ax-pi/axpi.md)

## LicheePi 系列

| 类别     | Lichee RV    | Lichee Zero Plus                           | Lichee Zero                    | Lichee nano         |
| :------- | :----------- | :----------------------------------------- | :----------------------------- | :------------------ |
| SOC      | Allwinner D1 | Allwinner S3                               | Allwinner V3s                  | Allwinner F1c100s   |
| CPU架构  | 玄铁 C906    | Cortex™-A7                                 | Cortex™-A7                     | ARM 926EJS          |
| 运行频率 | 1GHz         | 1.2GHz                                     | 1.2GHz(max)                    | 600MHz(max)         |
| RAM      | 512MB DDR3   | 128Mbyte DDR3                              | 64MB DRAM                      | 32MB DDR            |
| FLASH    | 可选SD-nand  | 可选SD Nand、<br>SPI Nor Flash<br>或者eMMC | 预留<br>SOP8 SPI Flash<br>焊盘 | 板载 16MB NOR FLASH |
| TF连接器 | 有           | 有                                         | 有                             | 有                  |

- LicheePI 是为了能让用户获得优廉的 linux设备，实战linux底层相关的内容的产品。

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

## Tang FPGA 系列

| 项目            | <p style="white-space:nowrap">Tang Primer 20K</p> | <p style="white-space:nowrap">Tang Nano 9K</p> | <p style="white-space:nowrap">Tang Nano 4K</p> | <p style="white-space:nowrap">Tang Nano 1K</p> |
| :-------------- | :------------------------------------------------ | :--------------------------------------------- | :--------------------------------------------- | ---------------------------------------------- |
| 逻辑单元(LUT4)  | 20736                                             | 8640                                           | 4608                                           | 1152                                           |
| 寄存器（FF）    | 15552                                             | 6480                                           | 3456                                           | 864                                            |
| S-SRAM (bits)   | 41472                                             | 17280                                          |                                                |                                                |
| B-SRAM (bits)   | 828K x 46                                         | 468K x 26                                      | 180K x 10                                      | 72K x 4                                        |
| 用户闪存 (bits) |                                                   | 608K                                           | 256K                                           | 96K                                            |
| 锁相环 (PLL)    | 4                                                 | 2                                              | 2                                              | 1                                              |
| 板载 Flash      | 32Mbits NOR Flash                                 | 32Mbits NOR Flash                              | 32Mbits NOR Flash                              | 预留焊盘                                       |
| 硬核处理器      |                                                   |                                                | Cortex-M3                                      |

- Tang FPGA 系列开发板主要分为 Tang Nano 和 Tang Primer 两个系列。

<table>
<thead>
<tr>
<th style="text-align:center">Tang Primer 20K（核心板）</th>
<th style="text-align:center">Tang Nano 1K</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center"><a href="./tang/tang-primer-20k/primer-20k.html"><img src="./tang/../../assets/Tang/primer_20k/primer_20k.png" alt="Tang Primer 20K（核心板）"></a></td>
<td style="text-align:center"><a href="./tang/Tang-Nano-1K/Nano-1k.html"><img src="./tang/../../assets/Tang/Nano-1K/1K.png" alt="Tang Nano 1K"></a></td>
</tr>
</tbody>
<thead>
<tr>
<th style="text-align:center">Tang Nano 4K</th>
<th style="text-align:center">Tang Nano 9K</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center"><a href="./tang/Tang-Nano-4K/Nano-4K.html"><img src="./tang/../../assets/Tang/Nano_4K/Nano_4K.png" alt="Tang Nano 4K"></a></td>
<td style="text-align:center"><a href="./tang/Tang-Nano-9K/Nano-9K.html"><img src="./tang/../../assets/Tang/Nano-9K/9K.png" alt="Tang Nano 9K"></a></td>
</tr>
</tbody>
</table>


### 售罄产品

|                                       Tang Nano                                       |                                              Tang Primer                                               |
| :-----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: |
| [![Tang Nano](./tang/../../assets/Tang/Nano/Tang_Nano.jpg)](./tang/Tang-Nano/Nano.md) | [![Tang Primer](./tang/../../assets/Tang/permier/Tang_permier.jpg)](./tang/Tang-primer/Tang-primer.md) |


## MaixSense 系列

- 基于 TOF 技术的深度相机

|                                                | Maixsense-a010                               | MaixSense-a075V                             |
| ---------------------------------------------- | -------------------------------------------- | ------------------------------------------- |
| 图片                                           | ![me_small](./maixsense/assets/me_small.jpg) | ![me_big](./maixsense/assets/me_big.jpg)    |
| 接口                                           | 1.25mm 串口连接器 \*1<br>Type-C USB2.0 \*1   | 1.25mm 串口连接器 \*1 <br>Type-C USB2.0 \*1 |
| 分辨率                                         | TOF：100x100@30fps                           | RGB：1600x1200@30fps<br>TOF：320x240@60fps  |
| 视场角                                         | RGB：无<br>TOF：70°(H) * 60°(V)              | RGB：120°<br>TOF：55°(H)*72°(H)             |
| <p style="white-space:nowrap">TOF 像素尺寸</p> |                                              | 15um                                        |
| 激光发射器                                     | 40nm VCSEL                                   | 940nm,3W                                    |
| 测量范围                                       | 0.2-2.5m                                     | 0.15-1.5m                                   |
| 测量精度                                       | &lt;=1%/cm                                   | &lt;=1%/cm                                  |

## Longon 系列

MCU 开发板

<img src="./longan/Nano/assets/longan_nano.jpg" alt="longan_nano" width="40%">

详情页：[点我](./longan/Nano/assets/readme.md)

## MaixFace 模组

- 商业合作模组，无个人支持

前往首页商业方案板块查看对应设备

## 外设模组

前往首页外设模组板块查阅对应设备
