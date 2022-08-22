Maix-II series hardware products
===

## Maix-II brief

Following the classic K210 Maix-I series AIOT boards, Sipeed continues to launch a number of edge computing boards that can run a complete Linux system, which will be named MAIX-II and MAIX-III in order of performance.

The MAIX-II series includes a variety of hardware products, currently:
* **Maix-II Dock**: **Recommended products in this series**, the chip is Allwinner V831, a cost-effective SOC that can run Linux, and supports hardware AI acceleration (0.2Tops computing power), currently have the best software support in this Maix-II series, provide CSDK and Python SDK, and online model training service ([MaixHub](https://maixhub.com))
* **MaixSense**: The chip is Allwinner R329, which also provides hardware AI acceleration, 0.25Tops computing power.
* **Maix-II-S**: The chip is Allwinner V833, an upgraded version of V831, which is mainly used for commercial customization, and individual users should choose carefully.

## MaixII Dock

The chip is Allwinner V831, single-core Cortex-A7 800MHz, 64MiB on-chip DDR2 memory, cost-effective SOC that can run Linux, and supports hardware AI acceleration (0.2Tops computing power), which can be used as a common Linux SOC or used for Edge AI applications.

**This series of recommended products**, the most cost-effective, the current software support is the easiest to get started, supports C language development, provides C SDK ([libmaix](http://github.com/sipeed/libmaix)); also provides [ MaixPy3](/maixpy3) support, you can use Python language to develop, you can directly use a large number of Python libraries, and supporting jupyter IDE, and [MaixHub](https://maixhub.com) fully supports this device

* Quick overview of product features

<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=298543445&bvid=BV1sF411u7xb&cid=586467021&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen=" true"> </iframe>
</p>

* Real pictures:
![m2dock](../../assets/maixII/m2dock.jpg)
* Purchase link: [sipeed.aliexpress.com](https://www.aliexpress.com/item/1005002538932487.html)
* Details: [MaixII-Dock](./M2/resources.md)

## MaixSense

The chip is Allwinner R329, dual-core A53@1.5GHz, on-chip 256MiB DDR3 memory, dual-core HiFi4@400MHz also provides hardware AI acceleration, 0.25Tops computing power, more good at audio field, support armbian system.

There are many official open materials, and it is more suitable for developers with strong hands-on ability at present.

![](./M2A/assets/M2A-1.gif)

* Purchase link: [sipeed.aliexpress.com](https://www.aliexpress.com/item/1005003152376519.html)
* Details: [MaixSense](./M2A/maixsense.md)


## MaixII S

It can be understood as a performance upgrade version of V831. Programs on V831 can be directly run on V833. This development board only supports commercial users. Personal users are recommended to choose Maix-II-Dock development board.

<img style="max-height: 300px" src="./M2S/assets/M2s_Dock.jpg" alt="M2s_Dock"/>

* Details: [MaixII S](./M2S/V833.md)
