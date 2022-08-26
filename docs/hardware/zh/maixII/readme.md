Maix-II 系列硬件产品
===

## Maix-II 简介

继经典的 K210 Maix-I 系列 AIOT 板卡之后，Sipeed 继续推出多款可运行完整 Linux 系统的边缘计算板卡，将以 MAIX-II，MAIX-III 按照性能依次命名。

MAIX-II 系列包含多款硬件产品，目前有:
* **Maix-II Dock**： **本系列推荐产品**, 芯片为全志 V831, 高性价比能跑 Linux 的SOC，同时支持硬件 AI 加速（0.2Tops 算力），目前软件支持最容易入门，提供 C SDK 和 Python SDK， 以及在线模型训练服务([MaixHub](https://maixhub.com))
* **MaixSense**： 芯片为全志R329，也有提供硬件 AI 加速，0.25Tops 算力。
* **Maix-II-S**：芯片为全志 V833，V831 升级版， 主要用于商业定制用途，个人用户慎重选择。

## MaixII Dock

芯片为全志 V831, 单核 Cortex-A7 800MHz， 64MiB 片内 DDR2 内存， 高性价比能跑 Linux 的SOC，同时支持硬件 AI 加速（0.2Tops 算力），可以当成普通 Linux SOC 使用， 也可以用于边缘 AI 应用。

**本系列推荐产品**, 最具性价比， 目前软件支持最容易入门， 支持 C 语言开发，提供 C SDK([libmaix](http://github.com/sipeed/libmaix))； 同时提供 [MaixPy3](/maixpy3) 支持，使用 Python 语言即可开发，可以直接使用大量 Python 库，并且配套 jupyter IDE， 同时 [MaixHub](https://maixhub.com) 完全支持此设备

* 产品功能速览

<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=298543445&bvid=BV1sF411u7xb&cid=586467021&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
</p>

* 实拍图：
![m2dock](../../assets/maixII/m2dock.jpg)
* 购买链接: [sipeed.taobao.com](https://item.taobao.com/item.htm?ft=t&id=635874427363)
* 详情： [MaixII-Dock](./M2/resources.md)

## MaixSense

芯片为全志 R329，双核 A53@1.5GHz，片内 256MiB DDR3 内存，双核 HiFi4@400MHz 也有提供硬件 AI 加速，0.25Tops 算力， 更加擅长音频领域， 支持 armbian 系统。

官方开放资料很多，目前比较适合动手能力比较强的开发者。

![](./M2A/assets/M2A-1.gif)

* 购买链接: [sipeed.taobao.com](https://sipeed.taobao.com)
* 详情： [MaixSense](./M2A/maixsense.md)


## MaixII S

可以理解成 V831 的性能升级版， V831 上的程序可以直接在 V833 上运行，此开发板仅支持商业用户，个人用户建议选择 Maix-II-Dock 开发板

<img style="max-height: 300px" src="./M2S/assets/M2s_Dock.jpg" alt=“M2s_Dock”/>

* 详情： [MaixII S](./M2S/V833.md)


