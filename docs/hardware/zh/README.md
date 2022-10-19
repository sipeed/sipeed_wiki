---
title: Sipeed 开源产品速览
keywords: Sipeed, Hardware, 矽速, 硬件资料, 文档, 资料下载, 深度学习, 人工智能, K210
desc: 矽速科技的开源软硬件 WIKI 资料站
---

## Maix-I 系列

### Maix-I S

这是一款以博流 808 为主控所制作的模块与核心板

### Maix-I A

### Maix-I 系列

这是 2019 年以 K210 为核心所制作的一系列 AIOT 开发板。

<table role="table" class="center_table">
    <tbody>
        <tr>
            <th scope="col">型号</th>
            <th scope="col">图片</th>
            <th scope="col">型号</th>
            <th scope="col">图片</th>
        </tr>
        <tr>
             <td style="white-space:nowrap">Maix Bit</td>
            <td> <a href="./maix/maixpy_develop_kit_board/maix_bit.html"
                    target="_blank"><img
                        src="./maix/assets/dk_board/maix_bit/Bit.png" ></a> </td>
             <td style="white-space:nowrap">Maix Dock</td>
            <td><a href="./maix/maixpy_develop_kit_board/Maix_dock.html"
                    target="_blank"><img
                        src="./maix/assets/dk_board/maix_dock/Dan_Dock.png" ></a></td>
        </tr>
        <tr>
             <td style="white-space:nowrap">Maix Duino</td>
            <td><a href="./maix/maixpy_develop_kit_board/maix_duino.html"
                    target="_blank"><img
                        src="./maix/assets/dk_board/maix_duino/maixduino_0.png" ></a></td>
             <td style="white-space:nowrap">Maix nano</td>
            <td><a href="./maix/maixpy_develop_kit_board/maix_nano.html"><img
                        src="./maix/assets/dk_board/maix_nano/maix_nano.jpg"  alt="Maxi nano"></a></td>
        </tr>
        <tr>
             <td style="white-space:nowrap">Maix Cube</td>
            <td><a href="./maix/maixpy_develop_kit_board/maix_cube.html"
                    target="_blank"><img
                        src="./maix/assets/dk_board/maix_cube/maix_cube.png" ></a></td>
             <td style="white-space:nowrap">Maix Amigo</td>
            <td><a href="./maix/maixpy_develop_kit_board/maix_Amigo.html"
                    target="_blank"><img
                        src="./maix/assets/dk_board/maxi_amigo/maix_amigo_0.png" ></a></td>
        </tr>
        <tr>
             <td style="white-space:nowrap">Maix HAT</td>
            <td><a href="./maix/maixpy_develop_kit_board/maix_go.html"><img
                        src="./../../soft/maixpy/assets/hardware/grove_ai_hat/grove_ai_hat1.png"  alt="Maix HAT"></a></td>
             <td style="white-space:nowrap">Maix Go</td>
            <td><a href="./maix/maixpy_develop_kit_board/maix_go.html"
                    target="_blank"><img
                        src="./maix/assets/dk_board/maix_go/Go.jpg"  ></a></td>
        </tr>
    </tbody>
</table>

### 产品技术支持

Maix 系列产品可以在多种场景实现客户不同方面的需要，在 AIoT 上已经广泛的使用，品质和性能在行业内已经有非常好的口碑，专业的技术团队为广大客户解决硬件设计和软件功能上的各种各样问题。商业合作可以联系 <support@sipeed.com>。

## Maix-II & III 系列

### Maix-II 系列简介

继经典的 K210 Maix-I 系列 AIOT 板卡之后，Sipeed 继续推出多款可运行完整 Linux 系统的边缘计算板卡，将以 MAIX-II，MAIX-III 按照性能依次命名。

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

<!-- * **Maix-II Dock**： **本系列推荐产品**, 芯片为全志 V831, 高性价比能跑 Linux 的SOC，同时支持硬件 AI 加速（0.2Tops 算力），目前软件支持最容易入门，提供 C SDK 和 Python SDK， 以及在线模型训练服务([MaixHub](https://maixhub.com))
* **Maix-II Sense**： 芯片为全志R329，也有提供硬件 AI 加速，0.25Tops 算力。
* **Maix-II-S**：芯片为全志 V833，V831 升级版， 主要用于商业定制用途，个人用户慎重选择。 -->

### MaixII Dock

芯片为全志 V831, 单核 Cortex-A7 800MHz， 64MiB 片内 DDR2 内存， 高性价比能跑 Linux 的SOC，同时支持硬件 AI 加速（0.2Tops 算力），可以当成普通 Linux SOC 使用， 也可以用于边缘 AI 应用。

**本系列推荐产品**, 最具性价比， 目前软件支持最容易入门， 支持 C 语言开发，提供 C SDK([libmaix](http://github.com/sipeed/libmaix))； 同时提供 [MaixPy3](/maixpy3) 支持，使用 Python 语言即可开发，可以直接使用大量 Python 库，并且配套 jupyter IDE， 同时 [MaixHub](https://maixhub.com) 完全支持此设备

.. details:: 点开查看产品功能速览视频

    <p align="center">
        <iframe src="//player.bilibili.com/player.html?aid=298543445&bvid=BV1sF411u7xb&cid=586467021&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
    </p>

<table>
<tr>
  <td>产品实拍图片</td>
  <td></td>
</tr>
<tr>
  <td>
  <img src="./../assets/maixII/m2dock.jpg" alt="m2dock">
  </td>
  <td></td>
</tr>
</table>

* 购买链接: [sipeed.taobao.com](https://item.taobao.com/item.htm?ft=t&id=635874427363)
* 详情： [MaixII-Dock](./maixII/M2/resources.md)

### MaixII Sense

其主控芯片为全志 R329，双核 A53@1.5GHz，片内 256MiB DDR3 内存，双核 HiFi4@400MHz 也有提供硬件 AI 加速，0.25Tops 算力， 更加擅长音频领域， 支持 armbian 系统。

官方开放资料很多，目前比较适合动手能力比较强的开发者。

![MaixII-Sense](./maixII/M2A/assets/M2A-1.gif)

* 购买链接: [sipeed.taobao.com](https://sipeed.taobao.com)
* 详情： [MaixSense](./maixII/M2A/maixsense.md)
* [极数社区 R329 上手帖](https://aijishu.com/a/1060000000221780)
* [极数社区 R329 芯片FAQ](https://aijishu.com/a/1060000000291439)
* [极数社区矽速科技](https://aijishu.com/blog/xisukeji)（很多资料）

### MaixII S

可以理解成 V831 的性能升级版， V831 上的程序可以直接在 V833 上运行；
此开发板仅支持商业用户，个人用户应当选择 [Maix-II-Dock](./maixII/M2/resources.md) 开发板

<img style="max-height: 300px" src="./M2S/assets/M2s_Dock.jpg" alt=“M2s_Dock”/>

* 详情： [MaixII S](./M2S/V833.md)

## LicheePi 系列

Linux 开发板

[![](./../assets/lichee.jpg)](./lichee/readme.md)

- Lichee 是 [Sipeed](https://www.sipeed.com/) 推出的开源产品，是为了能让用户获得优廉的linux设备，实战linux底层相关的内容的产品。

目前LicheePi相关核心板部分参数对比表格如下：

| 类别 | Lichee RV |Lichee Zero Plus|Lichee Zero|Lichee nano|
| :--- | :--- | :--- | :--- | :--- |
| SOC | Allwinner D1 | Allwinner S3 | Allwinner V3s | Allwinner F1c100s |
| CPU架构 |玄铁 C906 | Cortex™-A7  | Cortex™-A7 |  ARM 926EJS  |
|运行频率|1GHz|1.2GHz|1.2GHz(max)|600MHz(max)|
| RAM | 512MB DDR3 | 128Mbyte DDR3 |  64MB DRAM | 32MB DDR |
|FLASH|可选SD-nand|可选SD Nand、<br>SPI Nor Flash<br>或者eMMC |预留<br>SOP8 SPI Flash<br>焊盘|板载 16MB NOR FLASH|
| TF连接器 | 有|有|有|有|

- 上述的款型都可以通过sd卡启动系统
- 其他参数过多，版面放不下，需要的话麻烦自行对比一下。

### Lichee 核心版照片(Linux)

#### Lichee Zero

<div align="center">
<a href="./Zero/Zero.html" ><img src="./assets/Zero/Zero_1.png" width=400></a>
</div>

#### Lichee Nano

<div align="center">

<a href="./Nano/Nano.html" ><img src="./assets/Nano/Nano_2.png" width=400></a>

</div>

#### Lichee Zero Plus

<div align="center">

<a href="./ZeroPlus/ZeroPlus.html"><img src="./assets/Zero-Plus/Plus_1.jpg" width=400></a>

</div>

#### Lichee RV

<div align="center">

<a href="./RV/RV.html"><img src="./assets/RV/D1-4.png" width=400></a>

</div>

## Tang FPGA 系列

Tang FPGA 系列开发板主要分为 Tang Nano 和 Tang Primer 两个系列。

### 外观总览
<table>
<thead>
<tr>
<th style="text-align:center">Tang Primer 20K（核心板）</th>
<th style="text-align:center">Tang Nano 1K</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center"><a href="./tang-primer-20k/primer-20k.html"><img src="./../../assets/Tang/primer_20k/primer_20k.png" alt="Tang Primer 20K（核心板）"></a></td>
<td style="text-align:center"><a href="./Tang-Nano-1K/Nano-1k.html"><img src="./../../assets/Tang/Nano-1K/1K.png" alt="Tang Nano 1K"></a></td>
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
<td style="text-align:center"><a href="./Tang-Nano-4K/Nano-4K.html"><img src="./../../assets/Tang/Nano_4K/Nano_4K.png" alt="Tang Nano 4K"></a></td>
<td style="text-align:center"><a href="./Tang-Nano-9K/Nano-9K.html"><img src="./../../assets/Tang/Nano-9K/9K.png" alt="Tang Nano 9K"></a></td>
</tr>
</tbody>
</table>

#### 主要参数对比

| 条目            |<p style="white-space:nowrap">Tang Primer 20K</p>| <p style="white-space:nowrap">Tang Nano 9K</p>|<p style="white-space:nowrap">Tang Nano 4K</p>|<p style="white-space:nowrap">Tang Nano 1K</p>|
| :-------------- | :---------------- | :---------------- | :---------------- | ------------ |
| 逻辑单元(LUT4)  | 20736             | 8640              | 4608              | 1152         |
| 寄存器（FF）    | 15552             | 6480              | 3456              | 864          |
| S-SRAM (bits)   | 41472             | 17280             |                   |              |
| B-SRAM (bits)   | 828K x 46         | 468K x 26         | 180K x 10         | 72K x 4      |
| 用户闪存 (bits) |                   | 608K              | 256K              | 96K          |
| 锁相环 (PLL)    | 4                 | 2                 | 2                 | 1            |
| 板载 Flash      | 32Mbits NOR Flash | 32Mbits NOR Flash | 32Mbits NOR Flash | 预留焊盘     |
| 硬核处理器      |                   |                   | Cortex-M3         |              | |

### 售罄产品

|                                  Tang Nano                                  |                                         Tang Primer                                          |
| :-------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------: |
| [![Tang Nano](./../../assets/Tang/Nano/Tang_Nano.jpg)](./Tang-Nano/Nano.md) | [![Tang Primer](./../../assets/Tang/permier/Tang_permier.jpg)](./Tang-primer/Tang-primer.md) |


## MaixSense 系列

3D TOF 模组

[![](./../assets/maixsense.jpg)](./maixsense/readme.md)

## Longon 系列

MCU 开发板

[![](./../assets/longan_nano.jpg)](./longan/readme.md)

## MaixFace 模组


## 外设模组

