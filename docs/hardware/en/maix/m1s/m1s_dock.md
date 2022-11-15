---
title: M1s DOCK 开发板
keywords: M1s DOCK ,BL808, M1s
update:
  - date: 2022-11-15
    version: v0.1
    author: wonder
    content:
      - Initialize Doc
---

## Summary

Sipeed M1s Dock is a development board designed based on [Sipeed M1s module](./m1s_module.md)，routes interface like MIPI CSI、SPI LCD and FPC connector, to get rid of worries of connecting cable. Designed with the most minimal design, for customers to evaluate the module, or hobbyists to play directly, etc.

Buy one: [Aliexpress]()

<table>
  <tr>
  <td><img alt="m1s_dock_top" src="./../../../zh/maix/m1s/assets/m1s_dock/m1s_dock_top.jpg"></td>
  <td><img alt="m1s_dock_bottom" src="./../../../zh/maix/m1s/assets/m1s_dock/m1s_dock_bottom.jpg"></td>
  </tr>
</table>

<!-- 
<img width=40% alt="m1s_dock_top" src="./../../../zh/maix/m1s/assets/m1s_dock/m1s_dock_top.jpg">
<img width=40% alt="m1s_dock_bottom" src="./../../../zh/maix/m1s/assets/m1s_dock/m1s_dock_bottom.jpg">
 -->

## Feature

-	MainChip BL808 RISC-V 480Mhz + NPU BLAI-100
-	Onboard USB to UART debugger
-	Onboard screen interface (Optional 1.69-inch 240x280 capacitor touch screen)
-	Onboard MIPI camera interface (Optional 2M solution camera)
-	Support 2.4G WIFI / BT / BLE
-	Onboard 1 analog microphone、1  LED、1 TF card slot
-	Route USB-OTG to USB Type-C port

### Parameter

<table>
    <thead>
        <tr>
            <th colspan = "2" > M1s Dock </th>   
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
        <td rowspan="5" style="white-space:nowrap">Onboard components</td>
    </tr>
    <tr>
        <td>Onboard USB to UART debugger (Used for uart communication and burn firmware)</td>
    </tr>
    <tr>
        <td>Onboard screen interface (Optional 1.69-inch 240x280 capacitor touch screen)</td>
    </tr>
    <tr>
        <td>Onboard MIPI camera interface (Optional 2M solution camera</td>
    </tr>
    <tr>
        <td>Onboard 1 analog microphone、1  LED、1 TF card slot</td>
    </tr>
    <tr>    
        <td rowspan="5" style="white-space:nowrap"> Others </td>
    </tr>
    <tr>
      <td>
        3D model file：<a href="https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/5_3D_file">Click me</a>
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

### Function block

<table width=40%>
  <tr>
  <td><img alt="m1s_dock_function_block_top" src="./../../../zh/maix/m1s/assets/m1s_dock/m1s_dock_function_block_top.jpg"></td>
  <td><img alt="m1s_dock_function_block_top" src="./../../../zh/maix/m1s/assets/m1s_dock/m1s_dock_function_block_top.jpg"></td>
  </tr>
</table>

### Dimenssion

<img alt="m1s_dock_size" src="./../../../zh/maix/m1s/assets/m1s_dock/m1s_dock_size.png" width=45%>

### Pin map

<img alt="m1s_doc_pin_map" src="./../../../zh/maix/m1s/assets/m1s_dock/m1s_doc_pin_map.png" width=45%>

## Comparison

| Item    | Maix Bit                 | ESP32 cam                     | M1s Dock                                   |
| :------ | :----------------------- | :---------------------------- | :----------------------------------------- |
| MainChip  | K210                     | ESP32                         | M1s(BL808)                                 |
| Camera  | 0.3MP DVP GC0328         | 2MP DVP OV2640 with flash LED | 2MP MIPI OV2685(two-side) with flash LED   |
| Screen  | 2.4 inch 320x240         |                               | 1.68 inch 280x240 capacitive touch screen               |
| Audio    | I2S MEMS MIC             |                               | Analog MEMS MIC + LineOut                  |
| SD Card Slot | SPI mode                 | SPI mode                      | · SDHC mode <br>· JTAG mode                |
| Key    | Reset <br> Boot          | Reset                         | · Reset <br>· Boot <br>· User x 2          |
| USB     | USB to Serial x 1        |                               | · USB to Dual Serial  x 1 <br>· USB OTG HS |
| Other    |                          |                               | 4P x 1.25mm connector（UART port）                 |
| Pin    |·  2 x 18 pins <br>· bread board friendly| 2 x 8 pins                    |· 2 x 16 pins<br>·  bread board friendly                   |
| JTAG    |                          |                               | Optional TF2JTAG                               |
| SHell    |                          |                               | Optional                                       |
| 尺寸    | 25 x 53 mm               | 27 x 41 mm                    | 27 x 55 mm                                 |

## Software

<table>
    <thead>
        <tr>
            <th colspan = "2" > M1s Dock </th>   
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

- [Datasheet](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/1_Specification)
- [Schematic](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/2_Schematic)
- [Bit map](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/3_Bit_number_map)
- [Dimensions](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/4_Dimensional_drawing)
- [3D model file](https://dl.sipeed.com/shareURL/MAIX/M1s_Dock/M1s/5_3D_file)
- [Chip manual](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/6_Chip_Manual)
- [Capacitive touch screen manual](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/6_Chip_Manual/touch_screen)
- [Bouffalolab official site](https://dev.bouffalolab.com/home/)

---

- [SDK](https://github.com/sipeed/M1s_BL808_SDK) (Github) 
- [Examples](https://github.com/sipeed/M1s_BL808_example)（Github）
- [Telegram](https://t.me/sipeed)
- [Twitter](https://twitter.com/SipeedIO)
- [Reddit](https://www.reddit.com/r/Sipeed/)
- [Online model platform](https://maixhub.com/)


<!-- ## 注意事项

<table>
    <tr>
        <th>项目</th>
        <th>注意事项</th>
    </tr>
    <tr>
        <td>静电防护</td>
        <td>请避免静电打到 PCBA 上；接触 PCBA 之前请把手的静电释放掉</td>
    </tr>
    <tr>
        <td>容忍电压</td>
        <td> 每个 GPIO 的工作电压已经在原理图中标注出来，请不要让 GPIO 的实际工作的电压超过额定值，否则会引起 PCBA 的永久性损坏 </td>
    </tr>
    <tr>
        <td>FPC 座子</td>
        <td>在连接 FPC 软排线的时候，谲确保排线无偏侈地完整地插入到排线中</td>
    </tr>
    <tr>
        <td>插拔</td>
        <td>请完全断电后才进行插拔操作</td>
    </tr>
    <tr>
        <td>避免短路</td>
        <td>请在上电过程中，避免任何液体和金属触碰到 PCBA 上的元件的焊盘，否则会导致路，烧毁 PCBA</td>
    </tr>
</table> -->

## Contact

M1s Dock meets different needs of customers in various scenarios. Please contact email [support@sipeed.com](support@sipeed.com) for technical support and business cooperation
