---
title: Sipeed Hardware
keywords: Sipeed, Hardware, Sipeed, Hardware specifications, Documentation, Downloaden, Deeplearning, Artificial Intelligence, K210
desc: Sipeed hardware documentation website
---

## Summary

- [Maix-I & Zero](#maix-i--zero) 以 MCU 为主控的 AI 开发板
- [Maix-II](#maix-ii-系列)：Linux AI 开发板，小巧便携且实用
- [Maix-III](#maix-iii)： Linux AI 开发板，超强算力超大内存多种玩法
- [LicheePI](#licheepi-系列)： Linux 开发板
- [Tang](#tang-fpga-系列)：FPGA 开发板
- [MaixSense](#maixsense-系列)：3D TOF 模组
- [Longon](#longon-系列)：MCU 开发板
- [MaixFace](#maixface-模组)：商业项目板卡
- [其他外设](#外设模组)

## Maix Zero

| Item           | M0S                                                                                   | M0                                                                                |
| :------------- | :------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------- |
| Chip           | BL616                                                                                 | BL702                                                                             |
| Core           | RV32GCP@320MHz                                                                        | RV32@144MHz                                                                       |
| RAM            | 480KB                                                                                 | 132KB                                                                             |
| Storage        | 4MB Flash Inside                                                                      | 192KB ROM, 512KB Flash Inside                                                     |
| Wireless       | · Wifi<br>· Bluetooth<br>· Zigbee                                                          | Bluetooth                                                                              |
| Model platform | [MaixHub](https://www.maixhub.com)                                                    | [MaixHub](https://www.maixhub.com)                                                |
| Size           | 11(L)x10(W)mm                                                                         |                                                                                   |
| Detail         | [Click me](./maixzero/m0s/m0s.md)                                                         | [Click me](./maixzero/sense/maix_zero_sense.md)                                       |
| Outlook        | <img src="./../zh/maixzero/m0s/assets/m0s/m0s_pin_map.png" alt="m0sense" width="360"> | <img src="./../zh/maixzero/sense/assets/m0sense_1.png" alt="m0sense" width="360"> |

## Maix-I

| Detail         | M1/M1w                             | M1n                                | M1s                                                | M0                                              |
| :------------- | :--------------------------------- | :--------------------------------- | :------------------------------------------------- | :---------------------------------------------- |
| MainChip       | K210                               | K210                               | BL808                                              | BL702                                           |
| Core           | RV64@400MHz \* 2                   | RV64@400MHz \* 2                   | RV64GCV@480MHz<br>RV32GCP@320MHz<br>RV32EMC@160MHz | RV32@144MHz                                     |
| RAM            | 8MB                                | 8MB                                | 64MB                                               | 132KB                                           |
| Wireless       | M1w supports Wifi                  |                                    | · Wifi<br>· Bluetooth<br>· Zigbee                  | Bluetooth                                       |
| Package        | Stamp hole                         | Golden finger                      | Stamp hole                                         |                                                 |
| Model platform | [MaixHub](https://www.maixhub.com) | [MaixHub](https://www.maixhub.com) | [MaixHub](https://www.maixhub.com)                 | [MaixHub](https://www.maixhub.com)              |
| Size           | 25.4(L)x25.4(W)mm                  | 25.0(L)x22.0(W)mm                  | 31.0(L)x18.0(W)mm                                  |                                                 |
| Details        | [Click me](./maix/core_module.md)  | [Click me](./maix/M1n.md)          | [Click me](./maix/m1s/m1s_module.md)               | [Click me](./maixzero/sense/maix_zero_sense.md) |

### Maix-I S

This is the AIOT module and develptment board based on BL808.

|            | [M1s](./maix/m1s/m1s_module.md)                                                                                                                                                                                      | [M1s Dock](./maix/m1s/m1s_dock.md)                                                                                                                                                                                      |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Appearance | <a href="https://wiki.sipeed.com/en/m1s"><img src="https://gd4.alicdn.com/imgextra/i4/2200606237318/O1CN011g9yY323vhCXEyiKU_!!2200606237318.jpg" style="transform:rotate(270deg);" alt="M1s_module" width="80%"></a> | <a href="https://wiki.sipeed.com/en/m1s#dock"><img src="https://gd1.alicdn.com/imgextra/i1/2200606237318/O1CN01gE4a1E23vhCV77ggE_!!2200606237318.jpg" style="transform:rotate(270deg);" alt="M1s_Dock" width="80%"></a> |

### Maix-I

This is a series of AIOT development boards based on K210 in 2019.

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
             <td style="white-space:nowrap">Appearance</td>
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
             <td style="white-space:nowrap">Appearance</td>
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

### Support

Maix series products have meet different needs of customers in a variety of situations. The quality and performance are good reputation in the industry. Professional technical team solves various problems in hardware design or software usages for our customers. For business cooperation, please contact <support@sipeed.com>.

## Maix-II

| Detail         | MaixII-Dock                                                                                                                                                                                                                           | MaixII-Sense                                                                                                                                                            | MaixII-S                                                                                                                                                            |
| :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| MainChip       | V831                                                                                                                                                                                                                                  | R329                                                                                                                                                                    | V833                                                                                                                                                                |
| Core           | Cortex A7@800MHz                                                                                                                                                                                                                      | Cortex A53\*2@1.5GHz                                                                                                                                                    | Cortex A7@1.2GHz                                                                                                                                                    |
| RAM            | 64MB                                                                                                                                                                                                                                  | 256MB                                                                                                                                                                   | 默认 128MB                                                                                                                                                          |
| Wireless       | Wifi                                                                                                                                                                                                                                  | · Wifi<br>· Bluetooth                                                                                                                                                   | · Wifi                                                                                                                                                              |
| Appearance     | <img src="https://gd3.alicdn.com/imgextra/i3/2200606237318/O1CN01dT63dq23vhAOtdtm7_!!2200606237318.png_400x400.jpg" style="transform:rotate(0deg);" alt="MaixII-Dock">                                                                | <img src="https://gd3.alicdn.com/imgextra/i3/2200606237318/O1CN01AJdLYs23vh6b40oy2_!!2200606237318.png_400x400.jpg" style="transform:rotate(0deg);" alt="MaixII-Sense"> | <img src="https://gd2.alicdn.com/imgextra/i2/2200606237318/O1CN01C4iTYi23vh6muQApg_!!2200606237318.png_400x400.jpg" style="transform:rotate(0deg);" alt="MaixII-S"> |
| Model platform | [MaixHub](https://www.maixhub.com)                                                                                                                                                                                                    |                                                                                                                                                                         |                                                                                                                                                                     |
| Details        | [Click me](http://wiki.sipeed.com/m2dock)                                                                                                                                                                                             | [Click me](./maixii/m2a/maixsense.md)                                                                                                                                   | [Click me](./maixii/M2S/V833.md)                                                                                                                                    |
| Notes          | <strong>Popular product</strong>，高性价比能跑 Linux 的 SOC，同时支持硬件 AI 加速（0.2Tops 算力），目前软件支持最容易入门，提供 C SDK 和 Python SDK， 以及在线模型训练服务(<a href="https://maixhub.com" target="_blank">MaixHub</a>) | 有提供硬件 AI 加速，0.25Tops 算力。                                                                                                                                     | 仅支持商业                                                                                                                                                          |

At the same time, it supports hardware AI acceleration (0.2Tops computing power). At present, the software support is the easiest to get started. C SDK and Python SDK are provided. And an online model training service (<a href="https://maixhub.com" target="_blank">MaixHub</a>)

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

## LicheePi 系列

| 类别      | Lichee RV    | Lichee Zero Plus                             | Lichee Zero                    | Lichee nano         |
| :-------- | :----------- | :------------------------------------------- | :----------------------------- | :------------------ |
| SOC       | Allwinner D1 | Allwinner S3                                 | Allwinner V3s                  | Allwinner F1c100s   |
| CPU 架构  | 玄铁 C906    | Cortex™-A7                                   | Cortex™-A7                     | ARM 926EJS          |
| 运行频率  | 1GHz         | 1.2GHz                                       | 1.2GHz(max)                    | 600MHz(max)         |
| RAM       | 512MB DDR3   | 128Mbyte DDR3                                | 64MB DRAM                      | 32MB DDR            |
| FLASH     | 可选 SD-nand | 可选 SD Nand、<br>SPI Nor Flash<br>或者 eMMC | 预留<br>SOP8 SPI Flash<br>焊盘 | 板载 16MB NOR FLASH |
| TF 连接器 | 有           | 有                                           | 有                             | 有                  |

- LicheePI 是为了能让用户获得优廉的 linux 设备，实战 linux 底层相关的内容的产品。

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
| 视场角                                         | RGB：无<br>TOF：70°(H) \* 60°(V)             | RGB：120°<br>TOF：55°(H)\*72°(H)            |
| <p style="white-space:nowrap">TOF 像素尺寸</p> |                                              | 15um                                        |
| 激光发射器                                     | 40nm VCSEL                                   | 940nm,3W                                    |
| 测量范围                                       | 0.2-2.5m                                     | 0.15-1.5m                                   |
| 测量精度                                       | &lt;=1%/cm                                   | &lt;=1%/cm                                  |

## Longon 系列

MCU 开发板

<img src="./longan/Nano/assets/longan_nano.jpg" alt="longan_nano" width="40%">

详情页：[Click me](./longan/Nano/assets/readme.md)

## MaixFace 模组

- 商业合作模组，无个人支持

前往首页商业方案板块查看对应设备

## 外设模组

前往首页外设模组板块查阅对应设备
