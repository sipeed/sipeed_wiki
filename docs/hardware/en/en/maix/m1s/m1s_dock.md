---
title: M1s DOCK
keywords: M1s DOCK ,BL808, M1s, bl808
update:
  - date: 2022-11-15
    version: v0.1
    author: wonder
    content:
      - Initialize Doc
---

## Summary

Sipeed M1s Dock is a development board designed based on [Sipeed M1s module](./m1s_module.md)，routes interface like MIPI CSI、SPI LCD and FPC connector, to get rid of worries about connecting cable. Designed with the most minimal design, for customers to evaluate the module, or hobbyists to play directly, etc.

Buy one: [Aliexpress](https://www.aliexpress.com/item/1005004970779483.html)

<td><img alt="m1s_dock.jpg" src="./../../../zh/maix/m1s/assets/m1s_dock/m1s_dock.jpg" width="45%"></td>

## Video

Video of M1s Dock and M0Sense：M1s Dock is before 3:15，and time after 3:15 is M0Sense.

<iframe width="560" height="315" src="https://www.youtube.com/embed/hkSAW42Evl4" title="M1s Dock" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Features

- MainChip BL808 RISC-V 480Mhz + NPU BLAI-100
- Onboard USB to UART debugger
- Onboard screen interface (Optional 1.69-inch 240x280 capacitor touch screen)
- Onboard MIPI camera interface (Optional 2M solution camera)
- Support 2.4G WIFI / BT / BLE
- Onboard 1 analog microphone、1 LED、1 TF card slot
- Route USB-OTG to USB Type-C port

### Parameters

<table>
    <thead>
        <tr>
            <th colspan = "2" > M1s Dock </th>   
        </tr>
    </thead>
    <tbody>
    <tr>    
        <td rowspan="8" style="white-space:nowrap">M1s Module</td>
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
        <td>Onboard MIPI camera interface (Optional 2M solution camera)</td>
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
        <td>External TYPE-C PORT power supply requirements：<br>5V±10% 0.5A</td>
    </tr>
    <tr>
        <td>Temperature rise: &lt;30K</td>
    </tr>
    <tr>
        <td>Operating temperature:-10℃ ~ 65℃</td>
    </tr>
    </tbody> 
</table>

### Chip Cores

Three cores in chip: M0，D0，LP。

| M0                                                                         | D0                                                                         | LP                                                                         |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| T-HEAD E907@320MHz | T-HEAD [C906](https://xrvm.com/cpu-details?id=4056751997003636736)@480MHz | T-HEAD [E902](https://xrvm.com/cpu-details?id=4056758197145440256)@160MHz |

### Function block

<img alt="m1s_dock_function_block_top" src="./../../../zh/maix/m1s/assets/m1s_dock/m1s_dock_function_block_top.jpg"  width=20%>
<img alt="m1s_dock_function_block_top" src="./../../../zh/maix/m1s/assets/m1s_dock/m1s_dock_function_block_top.jpg"  width=20%>

### Dimenssion

<img alt="m1s_dock_size" src="./../../../zh/maix/m1s/assets/m1s_dock/m1s_dock_size.png" width=45%>

### Pinmap

<img alt="m1s_doc_pin_map" src="./../../../zh/maix/m1s/assets/m1s_dock/m1s_doc_pin_map.png" width=45%>

## Comparison

| Item         | Maix Bit                                 | ESP32 cam                     | M1s Dock                                  |
| :----------- | :--------------------------------------- | :---------------------------- | :---------------------------------------- |
| MainChip     | K210                                     | ESP32                         | M1s(BL808)                                |
| Camera       | 0.3MP DVP GC0328                         | 2MP DVP OV2640 with flash LED | 2MP MIPI OV2685(two-side) with flash LED  |
| Screen       | 2.4 inch 320x240                         |                               | 1.68 inch 280x240 capacitive touch screen |
| Audio        | I2S MEMS MIC                             |                               | Analog MEMS MIC + LineOut                 |
| SD Card Slot | SPI mode                                 | SPI mode                      | · SDHC mode <br>· JTAG mode               |
| Key          | Reset <br> Boot                          | Reset                         | · Reset <br>· Boot <br>· User x 2         |
| USB          | USB to Serial x 1                        |                               | · USB to Dual Serial x 1 <br>· USB OTG HS |
| Other        |                                          |                               | 4P x 1.25mm connector（UART port）        |
| Pin          | · 2 x 18 pins <br>· bread board friendly | 2 x 8 pins                    | · 2 x 16 pins<br>· bread board friendly   |
| JTAG         |                                          |                               | Optional TF2JTAG                          |
| Shell        |                                          |                               | Optional                                  |
| Size         | 25 x 53 mm                               | 27 x 41 mm                    | 27 x 55 mm                                |

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
          <td>· C SDK<br>· MaixHAL C <br>· PikaPython </td>
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
          <td>· Download from <a href="https://maixhub.com/">MaixHub</a>. Support Face detection and recognition, posture detection and gesture detection, etc.</td>
        </tr>
        <tr>
          <td>Sipeed examples</td>
          <td>· https://github.com/sipeed/M1s_BL808_example</td>
        </tr>
    </tbody>
</table>

## Operators list

<table>
<thead>
<tr>
  <th>Type</th>
  <th>Operators</th>
  <th>Applicable Subset Spec.</th>
  <th>Processor</th>
</tr>
</thead>
<tbody>
<tr>
  <td rowspan="10">Convolution</td>
  <td rowspan="4">Conv </td>
  <td>Kernel: 1x1,3x3,5x5,7x7</td>
  <td rowspan="4">:strong:<code>NPU</code></td>
</tr>
<tr>
  <td>Stride: 1x1, 2x2</td>
</tr>
<tr>
  <td>Dilation: 1x1, 2x2</td>
</tr>
<tr>
  <td>Pad: same</td>
</tr>
<tr>
  <td rowspan="4">Depthwise Conv</td>
  <td>Kernel: 1x1,3x3 (5x5, 7x7 TBD)</td>
  <td rowspan="4">:strong:<code>NPU</code></td>
</tr>
<tr>
  <td>Stride: 1x1, 2x2</td>
</tr>
<tr>
  <td>Dilation: 1x1 (2x2 TBD)</td>
</tr>
<tr>
  <td>Pad: same</td>
</tr>
<tr>
  <td rowspan="2">Transpose Conv</td>
  <td>Kernel: 3x3</td>
  <td rowspan="2">strong:<code>NPU</code></td>
</tr>
<tr>
  <td>Stride: 2x2</td>
</tr>
<tr>
  <td rowspan="4">Pooling</td>
  <td rowspan="2">MaxPool (NPU TBD)</td>
  <td>Kerenl: 2x2</td>
  <td rowspan="2">DSP</td>
</tr>
<tr>
  <td>Stride: 2x2</td>
</tr>
<tr>
  <td rowspan="2">MaxPool</td>
  <td>Kerenl: 3x3</td>
  <td rowspan="2">:strong:<code>NPU</code></td>
</tr>
<tr>
  <td>Stride: 1x1, 2x2</td>
</tr>
<tr>
  <td rowspan="2">Activation</td>
  <td>Relu</td>
  <td></td>
  <td>:strong:<code>NPU</code></td>
</tr>
<tr>
  <td>Relu 6</td>
  <td></td>
  <td>:strong:<code>NPU</code></td>
</tr>
<tr>
  <td rowspan="5">Other processing</td>
  <td>BatchNormalization</td>
  <td>fused with conv</td>
  <td>:strong:<code>NPU</code></td>
</tr>
<tr>
  <td>Add (shortcut)</td>
  <td></td>
  <td>:strong:<code>NPU</code></td>
</tr>
<tr>
  <td>Concat (route)</td>
  <td>Channel wise (AXIS 3 in BHWC)</td>
  <td>:strong:<code>NPU</code></td>
</tr>
<tr>
  <td>Fully Connected</td>
  <td></td>
  <td>:strong:<code>NPU</code></td>
</tr>
<tr>
  <td>Upsample</td>
  <td>Nearest</td>
  <td>:strong:<code>NPU</code></td>
</tr>
</tbody>
</table>

## Links

- [Board Datasheet](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/1_Specification)
- [Board Schematic](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/2_Schematic)
- [Board Bit map](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/3_Bit_number_map)
- [Board Dimensions](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/4_Dimensional_drawing)
- [3D model file](https://dl.sipeed.com/shareURL/MAIX/M1s_Dock/M1s/5_3D_file)
- [Board Chip manual](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/6_Chip_Manual)
- [Capacitive touch screen manual](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/6_Chip_Manual/touch_screen)
- [Bouffalolab official documents](https://dev.bouffalolab.com/home/)
- [BL808 DataSheet](https://github.com/bouffalolab/bl_docs/tree/main/BL808_DS/en) (github)
- [BL808 Reference Manual](https://github.com/bouffalolab/bl_docs/tree/main/BL808_RM/en) (github)

---

- [Sipeed SDK](https://github.com/sipeed/M1s_BL808_SDK) (Github) 
- [Sipeed Examples](https://github.com/sipeed/M1s_BL808_example)（Github）
- [Bouffalolab SDK](https://github.com/bouffalolab/bouffalo_sdk)（Github）
- [Linux SDK](https://github.com/sipeed/M1s_BL808_Linux_SDK)（Github）
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
</table>

## Contact

M1s Dock meets different needs of customers in various scenarios. Please contact email [support@sipeed.com](support@sipeed.com) for technical support and business cooperation
