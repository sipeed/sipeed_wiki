---
title: M1s Module
keywords: M1s ,Module, bl808, BL808
update:
  - date: 2022-11-14
    version: v0.1
    author: wonder
    content:
      - Initialize Doc
---

## Summary

Sipeed M1s module is an AIOT module based on BL808 of [Bouffalo Lab](https://en.bouffalolab.com/), it contains 3 cores inside, with WiFi/BT/BLE/Zigbee wireless units, including multiple cpus, audio encoder and decoder, video encoder and decoder and AI hardware accelerator (BLAI-100), suitable for a variety of high performance and low power applications. 

Buy one: [Aliexpress](https://www.aliexpress.com/item/1005004970779483.html)

<img src="./../../../zh/maix/m1s/assets/m1s_module/m1s_module_outlook.png" alt="m1s_module_outlook" width=35%>

## Feature

- MainChip BL808 RV64 480MHz + RV32 320MHz + NPU BLAI 100GOPS
- Onboard SPI FLASH  (16MByte default)
- Support 2.4G WIFI / BT / BLE
- Support IPEX-I antenna and onboard PCB antenna
- Stamp package route all IO

## Parameter

<table>
    <thead>
        <tr>
            <th colspan = "2" > M1s Module </th>   
        </tr>
    </thead>
    <tbody>
    <tr>    
        <td rowspan="8" style="white-space:nowrap">Main Chip BL808</td>
    </tr>
    <tr>
        <td>Three RISC-V CPUs：<br>· RV64GCV 480MHz <br>· RV32GCP 320MHz <br>· RV32EMC 160MHz</td>
    </tr>
    <tr>
        <td>AI NN general purpose hardware accelerator：<br>· BLAI-100, used for video/audio detection/identification，100GOPS hashrate</td>
    </tr>
    <tr>
        <td>768KB SRAM + 64MB UHS PSRAM</td>
    </tr>
    <tr>
        <td>Encode and Decode<br>- MJPEG and H264(Baseline/Main)<br>- 1920x1080@30fps + 640x480@30fps
        </td>
    </tr>
    <tr>
        <td>Interface：<br>- Camera interface ：DVP and MIPI-CSI<br>- Display interface：SPI、DBI、DPI(RGB)</td>
    </tr>
    <tr>
        <td>Wireless：<br>- Support Wi-Fi 802.11 b/g/n<br>- Support Bluetooth 5.x Dual-mode(BT+BLE)<br>- Support Wi-Fi / BT co-existence</td>
    </tr>
    <tr>
      <td>USB 2.0 HS OTG</td>
    </tr>
    <tr>    
        <td rowspan="3" style="white-space:nowrap">Onboard components</td>
    </tr>
    <tr>
        <td>Onboard SPI FLASH（Optional Capacity）</td>
    </tr>
    <tr>
        <td>Support IPEX-I antenna and onboard PCB antenna</td>
    </tr>
    </tbody>
    <tr>    
        <td rowspan="6" style="white-space:nowrap"> Others </td>
    </tr>
    <tr>
        <td>
        Dimension ：31mm (L) x 18mm (W)
        </td>
    </tr>
    <tr>
      <td>
        3D model file：<a href="https://dl.sipeed.com/shareURL/MAIX/M1s/M1s/5_3D_file">Click me</a>
      </td>
    </tr>
    <tr>
        <td>External power supply requirements：<br>VDDIO4/VDDIO3/VDDIO1/ and 3V3 these power supplys are required</td>
    </tr>
    <tr>
        <td>Temperature rise: &lt;30K</td>
    </tr>
    <tr>
        <td>Operating temperature:-10℃ ~ 65℃</td>
    </tr>
    </tbody>    
</table>

<img src="./../../../zh/maix/m1s/assets/m1s_module/m1s_module_size.png" alt="m1s_module_size" width=35%>

## Pin map

Visit Schematic for details：[Click me](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s/2_Schematic)

<img src="./../../../zh/maix/m1s/assets/m1s_module/m1s_pins.png" alt="m1s_pins" width=55%>

## Comparison

<table>
<thead>
<tr>
  <th style="text-align:left">Item</th>
  <th style="text-align:left">M1(K210)</th>
  <th style="text-align:left">M1s(BL808)</th>
  <th style="text-align:left">ESP32-S3-WROOM-N16R8</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="text-align:left">CPU</td>
  <td style="text-align:left">RV64@400MHz x2</td>
  <td style="text-align:left">· RV64GCV@480MHz<br>· RV32GCP@320MHz<br>· RV32EMC@160MHz</td>
  <td style="text-align:left;white-space:nowrap">Xtensa LX7@240MHz x2</td>
</tr>
<tr>
  <td style="text-align:left">RAM</td>
  <td style="text-align:left">8MB SRAM</td>
  <td style="text-align:left;white-space:nowrap">· 768KB SRAM <br>·  64MB UHS PSRAM(2000MHz)</td>
  <td style="text-align:left">· 512KB SRAM<br>· 8MB PSRAM</td>
</tr>
<tr>
  <td style="text-align:left">Flash</td>
  <td style="text-align:left">16MB</td>
  <td style="text-align:left">16MB</td>
  <td style="text-align:left">16MB</td>
</tr>
<tr>
  <td style="text-align:left">OS</td>
  <td style="text-align:left">· FreeRTOS<br>· No-mmu Linux</td>
  <td style="text-align:left">· FreeRTOS<br>· Linux</td>
  <td style="text-align:left">RTOS</td>
</tr>
<tr>
  <td style="text-align:left">NPU</td>
  <td style="text-align:left;white-space:nowrap">230GOPS with limited OPS</td>
  <td style="text-align:left;white-space:nowrap">100GOPS with rich OPS</td>
  <td style="text-align:left"></td>
</tr>
<tr>
  <td style="text-align:left">Camera</td>
  <td style="text-align:left">DVP, up to VGA</td>
  <td style="text-align:left">MIPI + DVP, up to 1080P h264</td>
  <td style="text-align:left">DVP</td>
</tr>
<tr>
  <td style="text-align:left">Display</td>
  <td style="text-align:left">· SPI<br>· 8bits MCU LCD</td>
  <td style="text-align:left">· SPI<br>· 8bits MCU LCD<br>· RGB LCD</td>
  <td style="text-align:left">· SPI<br>· 8bits MCU LCD</td>
</tr>
<tr>
  <td style="text-align:left">Audio</td>
  <td style="text-align:left">I2S</td>
  <td style="text-align:left">· I2S<br>· Analog Audio Input/Output</td>
  <td style="text-align:left">I2S</td>
</tr>
<tr>
  <td style="text-align:left">Wireless</td>
  <td style="text-align:left"></td>
  <td style="text-align:left">WIFI+BLE+Zigbee</td>
  <td style="text-align:left">WIFI + BLE</td>
</tr>
<tr>
  <td style="text-align:left">USB</td>
  <td style="text-align:left"></td>
  <td style="text-align:left">USB2.0 OTG HS</td>
  <td style="text-align:left">USB1.1 OTG</td>
</tr>
<tr>
  <td style="text-align:left">Accelerator</td>
  <td style="text-align:left">FFT</td>
  <td style="text-align:left">· Scaler<br>·  OSD<br>·  MJPED<br>·  G2D<br>·  H264</td>
  <td style="text-align:left"></td>
</tr>
<tr>
  <td style="text-align:left">Perpheral</td>
  <td style="text-align:left">UART, SPI, IIC</td>
  <td style="text-align:left">UART, SPI, IIC, SDIO ETH(RMII), ADC/DAC</td>
  <td style="text-align:left">UART, SPI, IIC, SDIO, ADC</td>
</tr>
<tr>
  <td style="text-align:left">Size</td>
  <td style="text-align:left">25.4 x 25.4 mm</td>
  <td style="text-align:left">31 x 18 mm</td>
  <td style="text-align:left">25.5 x 18 mm</td>
</tr>
<tr>
  <td style="text-align:left">Price</td>
  <td style="text-align:left">$6</td>
  <td style="text-align:left">$6</td>
  <td style="text-align:left">$4.3(digikey)</td>
</tr>
</tbody>
</table>

## Software

<table>
    <thead>
        <tr>
            <th colspan = "2" > M1s Module </th>   
        </tr>
    </thead>
    <tbody>
        <tr>
          <td>OS</td>
          <td>· Full support for FreeRTOS<br>· Basic support for Linux</td>
        </tr>
        <tr>
          <td>Developments</td>
          <td>· C SDK<br>· MaixHAL C <br>· pikascript python </td>
        </tr>
        <tr>
          <td>Burn Firmware</td>
          <td>· Burn from uart<br>· Virtual disk drag-and-drop burn</td>
        </tr>
        <tr>
          <td>AI Framework</td>
          <td>
          · Support BLAI accelerated inference engine with native SDK<br>
          · Suppory universal TinyMaix inference</td>
        </tr>
        <tr>
          <td>AI model store</td>
          <td>· Download from <a herf="https://maixhub.com/">MaixHub</a>. Support Face detection and recognition, posture detection and gesture detection, etc.</td>
        </tr>
        <tr>
          <td>Sipeed examples</td>
          <td>· https://github.com/sipeed/M1s_BL808_example</td>
        </tr>
    </tbody>
</table>

## Links

- [Datasheet](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s/1_Specification)
- [Schematic](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s/2_Schematic)
- [Bit map](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s/3_Bit_number_map)
- [Dimension](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s/4_Dimensional_drawing)
- [3D model file](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s/5_3D_file)
- [Chip manual](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s/6_Chip_Manual)
- [Bouffalolab official site](https://dev.bouffalolab.com/home/)

---

- [SDK](https://github.com/sipeed/M1s_BL808_SDK) (Github) 
- [Examples](https://github.com/sipeed/M1s_BL808_example)（Github）
- [Linux](https://github.com/sipeed/M1s_BL808_Linux_SDK)（Github）
- [Telegram](https://t.me/sipeed)
- [Twitter](https://twitter.com/SipeedIO)
- [Reddit](https://www.reddit.com/r/Sipeed/)
- [Online model platform](https://maixhub.com/)

## Attention

<table>
    <tr>
        <th>Item</th>
        <th>Attention</th>
    </tr>
    <tr>
        <td>Electrostatic protection</td>
        <td>Avoid static electricity hitting the PCBA. Release the static electricity of hand before touching the PCBA</td>
    </tr>
    <tr>
        <td>Operating voltage</td>
        <td>The operating voltage of each GPIO has been marked in the schematic. Please do not allow the actual operating voltage of the GPIO to exceed the rated value, otherwise the PCBA will be permanently damaged</td>
    </tr>
    <tr>
        <td>FPC Connector</td>
        <td>When connecting FPC cable，make sure that the row is completely inserted into the row without bias</td>
    </tr>
    <tr>
        <td>Plug and Remove</td>
        <td>Power off completely before plugging or removing it</td>
    </tr>
    <tr>
        <td>Avoid short circuit</td>
        <td>During the power-on, avoid any liquid or metal touching PCBA components，otherwise the PCBA will be damaged even burn</td>
    </tr>
    <tr>
        <td>Suggestion for Design</td>
        <td>Before hadrware design, see this post <a href="https://bbs.sipeed.com/thread/1721">https://bbs.sipeed.com/thread/1721</a> (Use Web Translation)</td>
    </tr>
    <tr>
        <td>BANK</td>
        <td>
            VDDIO1：GPIO 0-8，1.8V/3.3V<br>
            VDDIO2：GPIO 11-15，GPIO 40-41, 3.3V only<br>
            VDDIO3：GPIO 16-23，1.8V/3.3V<br>
            VDDIO4：GPIO 24-39，1.8V/3.3V<br>        
        </td>
    </tr>    
    <tr>
        <td>BOOT Mode</td>
        <td>
        When power on, the chip starts depend on the the voltage level of the BOOT pin: <br>
        · BOOT is 1 ：Start from flash<br>
        · BOOT is 0 ：Download from uart
        </td>
    </tr>
</table>

## Contact

M1s Dock meets different needs of customers in various scenarios. Please contact email [support@sipeed.com](support@sipeed.com) for technical support and business cooperation.