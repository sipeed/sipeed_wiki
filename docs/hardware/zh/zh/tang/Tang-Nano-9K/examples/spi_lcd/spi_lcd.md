---
title: Spi lcd 
keywords: Tang Nano 9K, spi, lcd
update:
  - date: 2022-10-25
    version: v0.1
    author: wonder
    content:
      - 内容编写
---

## 前言

Tang Nano 9K 板卡上有一个 8P 的 spi lcd 连接器，可以用来去驱动配套的 spi lcd 屏幕。

<img src="./../nano_9k/spi_lcd.jpg" alt="spi_lcd" width=48%>

配套 SPI 屏幕可以在淘宝店询问客服购买：[点我跳转到淘宝页面](https://sipeed.taobao.com/)

## 分析

SPI 屏幕的数据手册在这里：[点我跳转到下载页面](https://dl.sipeed.com/shareURL/TANG/Nano%209K/6_Chip_Manual/CN/LCD_Datasheet)

从数据手册中可以看到以下信息：

| NO. | Item              | Contents                   | Unit       |
| --- | ----------------- | -------------------------- | ---------- |
| 1   | LCD Size          | 1.14                       | inch       |
| 2   | Display Mode      | Normally black             | -          |
| 3   | Resolution        | 135(H)RGB x240(V)          | pixels     |
| 4   | Pixel pitch       | 0.1101(H) x 0.1038(V)      | mm         |
| 5   | Active area       | 14.864(H) x 24.912(V)      | mm         |
| 6   | Module size       | 17.6(H) x 31.0(V) x1.6 (D) | mm         |
| 7   | Pixel arrangement | RGB Vertical stripe        | -          |
| 8   | Interface         | 4 Line SPI                 | -          |
| 9   | Display Colors    | 262K                       | colors     |
| 10  | Drive IC          | ST7789V3                   | -          |
| 11  | Luminance(cd/m2)  | 400 (TYP)                  | Cd/m2      |
| 12  | Viewing Direction | All View                   | Best image |
| 13  | Backlight         | 1 White LED                | -          |
| 14  | Operating Temp.   | -20℃~ + 70℃              | ℃         |
| 15  | Storage Temp.     | -30℃~ + 80℃              | ℃         |
| 16  | Weight            | 1.8                        | g          |

在里面我们主要需要知道以下信息：
- 分辨率 (Resolution)：135(H)RGB x240(V)
- 接口 (Interface)：4 Line SPI 
- 驱动 (Drive IC)：ST7789V3 [点我下载相关数据手册](https://dl.sipeed.com/fileList/MAIX/HDK/Chip_DS/ST7789V3_SPEC_Preliminary_V0.0_200102.pdf)


感谢群友提供的代码，前往 https://github.com/sipeed/TangNano-9K-example/tree/main/spi_lcd 查看详情，相关说明会在整理之后展示。

![spi_lcd](./../nano_9k/spi_lcd.jpg)