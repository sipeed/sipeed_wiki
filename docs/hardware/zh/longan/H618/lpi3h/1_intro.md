---
title: 板卡介绍
keywords: Linux, Longan, H618, SBC, ARM
update:
  - date: 2023-12-08
    version: v1.0
    author: ztd
    content:
      - Release docs
---

## 简介
Longan Pi 3H 是基于 Longan Module 3H 核心板的 ARM Linux 开发板，以 H618 (Quad core ARM Cortex-A53@1.5Ghz , 64-bit) 为主控核心，板载最大 4GB 64bit LPDDR4，支持 HDMI 4K 显示输出。支持千兆网口，板载 wifi6/BT。

## 基础参数

<table>
<thead>
<tr>
  <th colspan=2>主控参数</th>
</tr>
</thead>
<tbody>
<tr>
  <td>主控芯片</td>
  <td>H618</td>
</tr>
<tr>
  <td>CPU 处理器</td>
  <td>ARM Cortex-A53@1.5Ghz <br>· 每核支持 32 KB L1 I-cache + 32 KB L1 D-cache <br>· 四核共享 1MB L2 Cache</td>
</tr>
<tr>
  <td>图形处理器</td>
  <td>Arm Mali-G31 <br>· OpenCL 2.0<br>· OpenGL ES 1.0/2.0/3.2<br>· Vulkan 1.1</td>
</tr>
<tr>
  <td>视频解码器</td>
  <td>· 支持 H.264 BP/MP/ HP@L4.2 解码，最大 4K 分辨率<br>· 支持 AVS2 JiZhun 10bit 解码，最大 4K 分辨率 <br>· 解码性能最大 4K@60fps </td>
</tr>
<tr>
  <td>视频编码器</td>
  <td>· 支持 H.264 BP/MP/HP 编码，最大 4K 分辨率<br>· 仅支持 I 帧和 P 帧<br>· 编码性能最大 4K@25fps </td>
</tr>
<tr>
  <th colspan=2>硬件特性</th>
</tr>
<tr>
  <td>RAM</td>
  <td>· 1/2/4 GB 64bits LPDDR4<br></td>
</tr>
<tr>
  <td>存储</td>
  <td>· eMMC: 可选空贴、32G<br>· 支持 TF 卡</td>
</tr>
<tr>
  <td>以太网</td>
  <td>· 千兆以太网接口</td>
</tr>
<tr>
  <td>USB</td>
  <td>· 2 x USBA Host <br>· 1 x USBC OTG</td>
</tr>
<tr>
  <td>显示接口</td>
  <td>· 1 x 标准 HDMI 接口 </td>
</tr>
<tr>
  <td>GPIO</td>
  <td>· UART<br>· IIC<br>· SPI</td>
</tr>
</tbody>
</table>

### 硬件资料下载

[LonganPi3H硬件资料](https://dl.sipeed.com/shareURL/LONGAN/LonganPi3H)

## 其他链接

[Github](https://github.com/sipeed/LonganPi-3H-SDK)  
[淘宝]()  

QQ群: 
Telegram: 

论坛：Maixhub.com/discussion  
联系邮箱：support@sipeed.com