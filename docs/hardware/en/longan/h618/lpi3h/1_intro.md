---
title: Board Introduction
keywords: Linux, Longan, H618, SBC, ARM
update:
  - date: 2023-12-08
    version: v1.0
    author: ztd
    content:
      - Release docs
---

## Board Introduction
Longan Pi 3H is an ARM Linux development board based on the Longan Module 3H core board. It is powered by the H618 (Quad-core ARM Cortex-A53 @ 1.5GHz, 64-bit) as the main control core and has a maximum onboard 4GB 64-bit LPDDR4 memory. It supports HDMI 4K display output and features a Gigabit Ethernet port. Additionally, it comes with onboard Wi-Fi 6 and Bluetooth capabilities.

## Basic Specifications

<table>
<thead>
<tr>
  <th colspan=2>Specifications</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Main Chip</td>
  <td>H618</td>
</tr>
<tr>
  <td>CPU </td>
  <td>ARM Cortex-A53@1.5Ghz <br>· Each core supports a 32 KB L1 I-cache and a 32 KB L1 D-cache. <br>· The quad-core configuration shares a 1MB L2 cache.</td>
</tr>
<tr>
  <td>GPU</td>
  <td>Arm Mali-G31 <br>· OpenCL 2.0<br>· OpenGL ES 1.0/2.0/3.2<br>· Vulkan 1.1</td>
</tr>
<tr>
  <td>Video Decoder</td>
  <td>· Supports H.264 BP/MP/HP@L4.2 decoding, with a maximum resolution of 4K<br>· Supports AVS2 JiZhun 10-bit decoding, with a maximum resolution of 4K <br>· The maximum decoding performance is 4K@60fps </td>
</tr>
<tr>
  <td>Video Encoder</td>
  <td>· Supports H.264 BP/MP/HP encoding, with a maximum resolution of 4K<br>· Only supports I-frames and P-frames for video encoding<br>· The maximum encoding performance is 4K@25fps </td>
</tr>
<tr>
  <th colspan=2>Hardware Specifications</th>
</tr>
<tr>
  <td>RAM</td>
  <td>· 1/2/4 GB 64bits LPDDR4<br></td>
</tr>
<tr>
  <td>Storage</td>
  <td>· eMMC: empty/32G<br>· Supports TF (microSD) card</td>
</tr>
<tr>
  <td>Ethernet</td>
  <td>· Gigabit Ethernet interface</td>
</tr>
<tr>
  <td>USB</td>
  <td>· 2 x USBA Host <br>· 1 x USBC OTG</td>
</tr>
<tr>
  <td>Display Interface</td>
  <td>· 1 x Standard HDMI interface </td>
</tr>
<tr>
  <td>GPIO</td>
  <td>· UART<br>· IIC<br>· SPI</td>
</tr>
</tbody>
</table>

### Hardware Documentation Download

[LonganPi3H Hardware Documentation](https://dl.sipeed.com/shareURL/LONGAN/LonganPi3H)

## Other links

[Github](https://github.com/sipeed/LonganPi-3H-SDK)  
[Aliexpress](https://www.aliexpress.us/item/3256806204597847.html)  

Forum：Maixhub.com/discussion  
Email：support@sipeed.com