---
title: M0S module
keywords: M0S, module, BL616, wifi6
update:
  - date: 2023-01-14
    version: v0.1
    author: wonder
    content:
      - Create file
---

## Module summary

Sipeed M0S is a ultra-low power consumption tiny IOT module based on BL616 of [Bouffalo Lab](https://en.bouffalolab.com/), supports wireless protocol like Wifi6, BT 5.2 and zigbee, 320MHz default frequency, tiny size and ultra-low power mode and various wake sources of the chip meet different low power scenarios.

Buy one: [Aliexpress](https://www.aliexpress.com/item/1005005142466936.html)

<img src="./../../../zh/maixzero/m0s/assets/m0s/m0s_module_outlook.png" alt="m0s_module_outlook" width=35%>

## Module Feature

- Tri-Mode Wireless: WiFi6 / BT 5.2 / Zigbee
- High Frequency：320MHz default
- Ultra-low Power Consumption：Wifi6 low power consumption feature
- DSP Acceleration：Support RISC-V P Extended instruction set, double speeds up TinyMaix reasoning frame.
- High speed USB：Support USB2.0 HS OTG，up to 480Mbps
- Rich peripheral ports：Support RGB LCD，DVP Camera，Ethernet RMII and SDIO
- Tiny Size：Place ceramic antenna on 10x11 mm tiny size, and route all IO out

## Module Parameter

<table>
    <thead>
        <tr>
            <th colspan = "2" > M0S Module </th>
        </tr>
    </thead>
    <tbody>
    <tr>
        <td rowspan="5" style="white-space:nowrap"> Main Chip BL616 </td>
    </tr>
    <tr>
        <td>RISC-V CPU：RV32GCP@320MHz default </td>
    </tr>
    <tr>
        <td> 480KB SRAM + 4MB Flash inside</td>
    </tr>
    <tr>
        <td>Wireless：<br>- Support Wi-Fi6<br>- Support Bluetooth 5.2 Dual-mode(BT+BLE)<br>- Support Zigbee </td>
    </tr>
    <tr>
      <td>USB 2.0 HS OTG</td>
    </tr>
    <tr>
        <td rowspan="2" style="white-space:nowrap"> Onboard components </td>
    </tr>
    <tr>
        <td>Ceramic antenna</td>
    </tr>
    </tbody>
    <tr>
        <td rowspan="4" style="white-space:nowrap"> Others </td>
    </tr>
    <tr>
        <td>
        Size：10mm (W) x 11mm (H)
        </td>
    </tr>
    <tr>
      <td>
        Package file (KiCAD)：<a href="https://dl.sipeed.com/shareURL/Maix-Zero/M0S/M0S/4_Package">Click me</a>
      </td>
    </tr>
    <tr>
      <td>
        3D model file：<a href="https://dl.sipeed.com/shareURL/Maix-Zero/M0S/M0S/3_3D_file">Click me</a>
      </td>
    </tr>
    </tbody>
</table>

## Pinmap

![m0s_pin_map](./../../../zh/maixzero/m0s/assets/m0s/m0s_pin_map.png)

## Comparsion

| Model          |      M0S Module       |  ESP32-S3 N4 Module  |
| -------------- | :-------------------: | :------------------: |
| Chip           |    BL616(RV32GCP)     |    ESP32-S3 (LX7)    |
| Frequency      |        320MHz         |        240MHz        |
| SRAM           |         480KB         |        520KB         |
| Flash          |        4MByte         |        4MByte        |
| Wifi           |         WiFi6         |        WiFi4         |
| Bluetooth      |         BT5.2         |         BT5          |
| USB            | USB2.0 HS OTG 480Mbps | USB2.0 FS OTG 12Mbps |
| IIC/UART/SPI   |          Yes          |         Yes          |
| DVP Camera     |          Yes          |         Yes          |
| Size           |      10mm x 11mm      |    18mm x 25.5mm     |
| Model platform |  TinyMaix + MaixHub   |         ---          |

## M0S Dock

<table>
    <thead>
        <tr>
            <th colspan = "2" > M0S Dock </th>
        </tr>
    </thead>
    <tbody>
    <tr>
        <td> Module x 1 </td>
        <td> M0S Module </td>
    </tr>
    <tr>
        <td> Key x 1 </td>
        <td> Press this key then boot this device to burn this module </td>
    </tr>
    <tr>
        <td> LED x 3 </td>
        <td> One power LED，Two user LEDs </td>
    </tr>
    <tr>
        <td> TypeC Port x 1 </td>
        <td> To download firmware or other custom USB function </td>
    </tr>
    <tr>
        <td> IO connector x 10 </td>
        <td> 8 IO route to Pin headers<br> 2 IOs near TypeC Port </td>
    </tr>
    <tr>
        <td> Schematic </td>
        <td> <a href="https://dl.sipeed.com/shareURL/Maix-Zero/M0S/M0S_Dock/2_Schematic"> 点我 </a></td>
    </tr>
    </tbody>
</table>

## Software

<table>
    <thead>
        <tr>
            <th colspan = "2" > M0S Module </th>   
        </tr>
    </thead>
    <tbody>
        <tr>
          <td>OS</td>
          <td>FreeRTOS</td>
        </tr>
        <tr>
          <td>Development</td>
          <td>· C SDK<br>· MaixHAL C <br>· PikaPython</td>
        </tr>
        <tr>
          <td>Burn Firmware </td>
          <td>· USB uart burn<br>· · USB burn</td>
        </tr>
        <tr>
          <td>AI Framework</td>
          <td>TinyMaix Framework</td>
        </tr>
        <tr>
          <td>AI model</td>
          <td>· <a herf="https://maixhub.com/"> MaixHub </td>
        </tr>
        <tr>
          <td>Sipeed examples</td>
          <td>· https://github.com/sipeed/M0S_BL616_example</td>
        </tr>
    </tbody>
</table>


## Other Links

- [M0S Datasheet](https://dl.sipeed.com/shareURL/Maix-Zero/M0S/M0S/1_Specification)
- [M0S Schematic](https://dl.sipeed.com/shareURL/Maix-Zero/M0S/M0S/2_Schematic)
- [M0S Package](https://dl.sipeed.com/shareURL/Maix-Zero/M0S/M0S/4_Package)
- [3D Model File](https://dl.sipeed.com/shareURL/Maix-Zero/M0S/M0S/3_3D_file)
- [Bouffalolab official documents](https://dev.bouffalolab.com/home/)
- [BL616 DataSheet](https://github.com/bouffalolab/bl_docs/tree/main/BL616_DS/en) (github)
- [BL616 Reference Manual](https://github.com/bouffalolab/bl_docs/tree/main/BL616_RM/en) (github)

---

- [M0S Dock Datasheet](https://dl.sipeed.com/shareURL/Maix-Zero/M0S/M0S_Dock/1_Specification)
- [M0S Dock Schematic](https://dl.sipeed.com/shareURL/Maix-Zero/M0S/M0S_Dock/2_Schematic)

---

- [SDK](https://github.com/bouffalolab/bl_mcu_sdk) (Github)
- [Telegram](https://t.me/sipeed)
- [Twitter](https://twitter.com/SipeedIO)
- [Reddit](https://www.reddit.com/r/Sipeed/)
- [Online model platform](https://maixhub.com/)

## Attentions

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
        <td>Do not allow the actual operating voltage of the GPIO to exceed the rated value, otherwise the PCBA will be permanently damaged</td>
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

M0sense eets different needs of customers in various scenarios. Please contact email [support@sipeed.com](support@sipeed.com) for technical support and business cooperation.
