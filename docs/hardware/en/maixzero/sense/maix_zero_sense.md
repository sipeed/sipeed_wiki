---
title: M0sense Board
keywords: BL702 ,M0sense
update:
  - date: 2022-11-16
    version: v0.1
    author: wonder
    content:
      - Creat file
---

## Summary

Sipeed M0sense is an AIOT development board based on BL702 of [Bouffalo Lab](https://en.bouffalolab.com/), it's RISC-V architecture, supports low-energy bluetooth. There is a 8Pins FPC connector for connecting LCD screen, and 1 microphone, 1 RGB LED and a six-axis sensor chip are on this board. One USB 2.0 FS routes to Type-C interface.

Buy one: [Aliexpress]()

Render picture:

<img src="./../../../../hardware/zh/maixzero/sense/assets/m0sense_1.png" alt="m0sense_1.png" width=30%>

Real picture:

<div>
  <img src="./../../../../hardware/zh/maixzero/sense/assets/m0sense_outlook_top.png" alt="m0sense_outlook_top.png" width=40%>
  <img src="./../../../../hardware/zh/maixzero/sense/assets/m0sense_outlook_bot.png" alt="m0sense_outlook_bot.png" width=40%>
</div>

## Feature

- Mainchip BL702 RISC-V 144MHz
- BlueTooth 5.0/ BLE
- Onboard screen interface (Optional 0.68 inch 80x160 solution screen)
- Onboard 1 analog microphone、1 LED、1 IMU
- Route USB 2.0 FS to USB Type-C port

## Parameter

<table>
    <thead>
        <tr>
            <th colspan = "2" > M0sense </th>
        </tr>
    </thead>
    <tbody>
    <tr>    
        <td rowspan="6" style="white-space:nowrap">Mainchip BL702</td>
    </tr>
    <tr>
        <td>32 bits RISC-V with FPU (Max Freq 144MHz)</td>
    </tr>
    <tr>
        <td>132KB RAM，192KB ROM, 512KB Flash</td>
    </tr>
    <tr>
        <td>
        · Two 32-bit timer       <br>
        · Eight DMA channels     <br>
        · One SPI                <br>
        · Two UART               <br>
        · One I2C interface      <br>
        · One I2S                <br>
        · Five PWM               <br>
        · One 12-bit ADC         <br>
        · One 10-bit DAC         <br>
        </td>
    </tr>
    <tr>
        <td>Wireless：<br>
            · 2.4Ghz BlueTooth V5.0<br>
            · 1Mbps and 2Mbps BLE
        </td>
    </tr>
    <tr>
        <td>
            USB 2.0 FS route to USB Type-C to burn firmware
        </td>
    </tr>
    <tr>    
        <td rowspan="6" style="white-space:nowrap"> Onboard components </td>
    </tr>
    <tr>
        <td>Screen interface (Optional 0.68 inch 80x160 solution screen)</td>
    </tr>
    <tr>
        <td> One analog microphone </td>
    </tr>
    <tr>
        <td> One RGB LED</td>
    </tr>
    <tr>
        <td> One six-axis IMU（QMI8658A）</td>
    </tr>
    <tr>
        <td>Ceramic antenna</td>
    </tr>
    <tr>    
        <td rowspan="5" style="white-space:nowrap"> Others </td>
    </tr>
    <tr>
      <td>
        3D file model：<a href="https://dl.sipeed.com/shareURL/Maix-Zero/Maix-Zero/5_3D_file">Click me</a>
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

<img src="./../../../../hardware/zh/maixzero/sense/assets/m0sense_size.png" alt="m0sense_size" width=55%>

## 引脚

<img src="./../../../../hardware/zh/maixzero/sense/assets/m0sense_pinmap.png" alt="m0sense_pinmap" width=75%>

## 对比

<table>
  <thead>
    <tr>
      <th>Item</th>
      <th>Arduino Nano 33 BLE SENSE</th>
      <th>Sipeed M0sense</th>
    </tr>
  </thead>
  <body>
    <tr>
      <td> MCU </td>
      <td>nRF52840 (Cortex M4)</td>
      <td>BL702 (RV32)</td>
    </tr>
    <tr>
      <td>Freq</td>
      <td>64MHz</td>
      <td>144MHz</td>
    </tr>
    <tr>
      <td>SRAM</td>
      <td>256KB</td>
      <td>132KB</td>
    </tr>
    <tr>
      <td>Bluetooth</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>IIC/UART/SPI</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>LED</td>
      <td>Single</td>
      <td>RGB Three color</td>
    </tr>
    <tr>
      <td>MIC</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>IMU</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Other sensors</td>
      <td>APDS9960，LPS22HB，HTS221</td>
      <td></td>
    </tr>
    <tr>
      <td>LCD</td>
      <td></td>
      <td>Optional 0.68 inch 80x160 solution screen</td>
    </tr>
    <tr>
      <td>USB</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Dimenssion</td>
      <td>45mm x 18mm</td>
      <td>23mm x 18mm</td>
    </tr>
    <tr>
      <td>Model platform</td>
      <td>TFLite-Micro + edge impulse</td>
      <td>TinyMaix + MaixHub</td>
    </tr>
    <tr>
      <td>Price</td>
      <td>$40</td>
      <td>$4</td>
    </tr>
  </body>
</table>

## Software

<table>
    <thead>
        <tr>
            <th colspan = "2" > M0sense </th>   
        </tr>
    </thead>
    <tbody>
        <tr>
          <td>OS</td>
          <td>FreeRTOS</td>
        </tr>
        <tr>
          <td>Development</td>
          <td>· C SDK<br>· MaixHAL C <br>· pikascript</td>
        </tr>
        <tr>
          <td>Burn Firmware </td>
          <td>·  USB virtual uart<br>· USB virtual disk burn</td>
        </tr>
        <tr>
          <td>AI Framework</td>
          <td>TinyMaix Framework</td>
        </tr>
        <tr>
          <td>AI model</td>
          <td>· Download from <a herf="https://maixhub.com/">MaixHub</a>. Support voice response, gesture detection and other models</td>
        </tr>
        <tr>
          <td>Sipeed examples</td>
          <td>· https://github.com/sipeed</td>
        </tr>
    </tbody>
</table>

## Links

- [Datasheet](https://dl.sipeed.com/shareURL/Maix-Zero/Maix-Zero/1_Specification)
- [Schematic](https://dl.sipeed.com/shareURL/Maix-Zero/Maix-Zero/2_Schematic)
- [Bit map](https://dl.sipeed.com/shareURL/Maix-Zero/Maix-Zero/3_Bit_number_map)
- [Dimension](https://dl.sipeed.com/shareURL/Maix-Zero/Maix-Zero/4_Dimensional_drawing)
- [3D model file](https://dl.sipeed.com/shareURL/Maix-Zero/Maix-Zero/5_3D_file)
- [Bouffalolab official site](https://dev.bouffalolab.com/home/)

---

- [SDK](https://github.com/bouffalolab/bl_mcu_sdk) (Github) 
- [Telegram](https://t.me/sipeed)
- [Twitter](https://twitter.com/SipeedIO)
- [Reddit](https://www.reddit.com/r/Sipeed/)
- [Online model platform](https://maixhub.com/)

## 注意事项

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

## 联系

M0sense eets different needs of customers in various scenarios. Please contact email [support@sipeed.com](support@sipeed.com) for technical support and business cooperation.
