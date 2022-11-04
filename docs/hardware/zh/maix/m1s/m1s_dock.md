---
title: M1s DOCK 开发板
keywords: M1s DOCK ,BL808, M1s
update:
  - date: 2022-11-04
    version: v0.1
    author: wonder
    content:
      - 初次编写
---

## 产品概述

Sipeed M1s Dock 是基于 [Sipeed M1s](./m1s_module.md) 模组来设计的一款核心板，引出了 MIPI CSI、SPI LCD 等 FPC 接口，免去接线难的烦恼。使用最精简的设计，用于客户对模组进行模组评估，或者爱好者直接上手游玩等用途。

购买链接：[淘宝](https://item.taobao.com/item.htm?id=691108452443)

<table>
  <tr>
  <td><img alt="m1s_dock_top" src="./assets/m1s_dock/m1s_dock_top.jpg"></td>
  <td><img alt="m1s_dock_bottom" src="./assets/m1s_dock/m1s_dock_bottom.jpg"></td>
  </tr>
</table>

<!-- 
<img width=40% alt="m1s_dock_top" src="./assets/m1s_dock/m1s_dock_top.jpg">
<img width=40% alt="m1s_dock_bottom" src="./assets/m1s_dock/m1s_dock_bottom.jpg">
 -->

## 板卡特点

-	主芯片 BL808 RISC-V 480Mhz + NPU BLAI-100
-	板载 USB 转 UART 调试器（可实现一键点击烧录，无需按实体按键）
-	板载显示屏座子（可选配 1.69 寸 240x280 电容触摸屏）
-	板载 MIPI 摄像头座子（可选配 200W 像素摄像头）
-	支持 2.4G WIFI / BT / BLE
-	板载 1 个模拟麦克风、1 个 LED、1 个 TF 卡座
-	引出一路 USB-OTG 到 USB Type-C 接口

### 硬件参数


<table>
    <thead>
        <tr>
            <th colspan = "2" > M1s 模组 </th>   
        </tr>
    </thead>
    <tbody>
    <tr>    
        <td rowspan="9" style="white-space:nowrap">主控 BL808 处理器</td>
    </tr>
    <tr>
        <td>多核 RISC-V (Max Freq 480MHz)</td>
    </tr>
    <tr>
        <td>AI NN 通用硬件加速器 —— BLAI-100 用于视频/音频检测/识别</td>
    </tr>
    <tr>
        <td>内嵌 64MB DRAM</td>
    </tr>
    <tr>
        <td>编解码：<br>- MJPEG and H264(Baseline/Main)<br>- 1920x1080@30fps + 640x480@30fps
        </td>
    </tr>
    <tr>
        <td>ISP（图像信号处理）：详情请查看<a href="https://dl.sipeed.com/shareURL/MAIX/M1s/M1s/6_Chip_Manual">芯片规格书</a></td>
    </tr>
    <tr>
        <td>接口：<br>- 摄像头接口 ：DVP 和 MIPI-CSI<br>- 显示接口：SPI、DBI、DPI(RGB)</td>
    </tr>
    <tr>
        <td>无线：<br>- 支持 Wi-Fi 802.11 b/g/n<br>- 支持 Bluetooth 5.x Dual-mode(BT+BLE)<br>- 支持 Wi-Fi / 蓝牙 共存</td>
    </tr>
    <tr>
      <td>USB 2.0 HS OTG （引出到 USB Type-C 接口）</td>
    </tr>
    <tr>    
        <td rowspan="5" style="white-space:nowrap"> 板载部件 </td>
    </tr>
    <tr>
        <td>板载 USB 转 UART 调试器（使用官方下载工具可实现一键点击烧录，无需按实体按键）</td>
    </tr>
    <tr>
        <td>板载 1 个显示屏座子（可选配 1.69 寸 240 x 280 电容触摸屏）</td>
    </tr>
    <tr>
        <td>板载 MIPI 摄像头座子（可选配 200W 像素摄像头）</td>
    </tr>
    <tr>
        <td>板载 1 个模拟麦克风、1 个 LED、1 个 TF 卡座 </td>
    </tr>
    </tbody>
    <tr>    
        <td rowspan="6" style="white-space:nowrap"> 其他说明 </td>
    </tr>
    <tr>
      <td>
        3D 模型文件下载：<a href="https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/5_3D_file">点击跳转</a>
      </td>
    </tr>
    <tr>
        <td>外部供电需求 TYPE-C 接口：5V±10% 0.5A</td>
    </tr>
    <tr>
        <td>温升: &lt;30K</td>
    </tr>
    <tr>
        <td>工作温度范围:-10℃ ~ 65℃</td>
    </tr>
    </tbody>    
</table>

### 功能框图

<table width=40%>
  <tr>
  <td><img alt="m1s_dock_function_block_top" src="./assets/m1s_dock/m1s_dock_function_block_top.jpg"></td>
  <td><img alt="m1s_dock_function_block_top" src="./assets/m1s_dock/m1s_dock_function_block_top.jpg"></td>
  </tr>
</table>

### 尺寸图

<img alt="m1s_dock_size" src="./assets/m1s_dock/m1s_dock_size.png" width=45%>

### 引脚图

<img alt="m1s_doc_pin_map" src="./assets/m1s_dock/m1s_doc_pin_map.png" width=45%>

## 对比

| 项目 | Maix Bit | ESP32 cam | M1s Dock |
|:---|:---|:---|:---|
| 处理器 | K210 | ESP32 | M1s(BL808) |
| 摄像头 | 0.3MP DVP GC0328 | 2MP DVP OV2640 with flash LED | 2MP MIPI OV2685(two-side) with flash LED |
| 显示屏 | 2.4 inch 320x240 || 1.68 inch 280x240 带电容触摸 |
| 音频 | I2S MEMS MIC |  | Analog MEMS MIC + LineOut |
| SD 卡槽 | SPI 模式 |  SPI 模式 |  SDHC 模式 <br> JTAG 模式 |
| 按键 | Reset <br> Boot | Reset | Reset <br> Boot <br> User x 2 |
| USB | USB to Serial x 1 || USB to Dual Serial  x 1 <br> USB OTG HS |
| 其他 ||| 4P 1.25mm 连接器（串口） |
| 引脚 | 2 x 18 pins,可用于面包板 | 2 x 8 pins | 2 x 16 pins,可用于面包板 |
| 尺寸 | 25 x 53 mm | 27 x 41 mm | 27 x 55 mm |


## 资料

- [规格书](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/1_Specification)
- [原理图](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/2_Schematic)
- [位号图](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/3_Bit_number_map)
- [尺寸图](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/4_Dimensional_drawing)
- [3D 模型文件](https://dl.sipeed.com/shareURL/MAIX/M1s_Dock/M1s/5_3D_file)
- [芯片数据手册](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/6_Chip_Manual)
- [触摸屏手册](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/6_Chip_Manual/touch_screen)

---

- [SDK]() (Github) 等待公开
- 交流 QQ 群：`592731168` 。[点我加群](点击链接加入群聊【荔枝开源 M1s AI交流群】：https://jq.qq.com/?_wv=1027&k=uyKNhTeu)
- 论坛：[bbs.sipeed.com](bbs.sipeed.com)

## 联系

M1s 模组可以在多种场景实现客户不同方面的需要，商业合作请联系使用邮箱商务 [support@sipeed.com](support@sipeed.com)
