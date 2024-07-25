---
title: Tang FPGA Board
---

Tang FPGA Board contains Tang Nano and Tang Primer.

| Tang Nano                                                             | Tang Primer                                                               |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| - Tang Nano 1K<br>- Tang Nano 4K<br>- Tang Nano 9K<br>- Tang Nano 20K | - Tang Primer 20K<br>- Tang Primer 20K Dock<br>- Tang Primer 20K Lite<br> |

## Tang Nano

Tang Nano FPGA Boards are in a tiny size, containing onboard Jatg debugger, can be programmed and simulated via only one TypeC cable.
So many different Tang Nano FPGA Boards are listed, there must be one fits you.

### Spec.

| Item              | <p style="white-space:nowrap">Tang Nano 20K</p> | <p style="white-space:nowrap">Tang Nano 9K</p> | <p style="white-space:nowrap">Tang Nano 4K</p> | <p style="white-space:nowrap">Tang Nano 1K</p> |
| :---------------- | :---------------------------------------------- | :--------------------------------------------- | :--------------------------------------------- | ---------------------------------------------- |
| Logic units(LUT4) | 20736                                           | 8640                                           | 4608                                           | 1152                                           |
| Flip-flop（FF）   | 15552                                           | 6480                                           | 3456                                           | 864                                            |
| S-SRAM (bits)     | 41472                                           | 17280                                          |                                                |                                                |
| B-SRAM (bits)     | 828K                                            | 468K                                           | 180K                                           | 72K                                            |
| User Flash (bits) |                                                 | 608K                                           | 256K                                           | 96K                                            |
| PLL               | 4                                               | 2                                              | 2                                              | 1                                              |
| Onboard Flash     | 32Mbits NOR Flash                               | 32Mbits NOR Flash                              | 32Mbits NOR Flash                              | Pad reserved                                   |
| Hardcore          |                                                 |                                                | Cortex-M3                                      |                                                |

### Shape

<table>
<thead>
<tr>
<th style="text-align:center">Tang Nano 20K</th>
<th style="text-align:center">Tang Nano 9K</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center"><a href="/nano20k"><img src="/hardware/assets/Tang/nano_20k/tang_nano_20k_3920_top.png" alt="Tang Nano 20K"></a></td>
<td style="text-align:center"><a href="./Tang-Nano-9K/Nano-9K.html"><img src="./../../assets/Tang/Nano-9K/9K.png" alt="Tang Nano 9K"></a></td>
</tr>
</tbody>
<thead>
<tr>
<th style="text-align:center">Tang Nano 4K</th>
<th style="text-align:center">Tang Nano 1K</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center"><a href="./Tang-Nano-4K/Nano-4K.html"><img src="./../../assets/Tang/Nano_4K/Nano_4K.png" alt="Tang Nano 4K"></a></td>
<td style="text-align:center"><a href="./Tang-Nano-1K/Nano-1k.html"><img src="./../../assets/Tang/Nano-1K/1K.png" alt="Tang Nano 1K"></a></td>
</tr>
</tbody>
</table>

## Tang Primer

Tang Primer FPGA boards are for users secondary development

### Spec.

| Item              | <p style="white-space:nowrap">Tang Primer 20K</p> | <p style="white-space:nowrap">Tang Primer 20K Dock</p> | <p style="white-space:nowrap">Tang Primer 20K Lite</p> |
| :---------------- | :------------------------------------------------ | :----------------------------------------------------- | :----------------------------------------------------- |
| Logic units(LUT4) | 20736                                             | 20736                                                  | 20736                                                  |
| Flip-flop（FF）   | 15552                                             | 15552                                                  | 15552                                                  |
| S-SRAM (bits)     | 41472                                             | 41472                                                  | 41472                                                  |
| B-SRAM (bits)     | 828K                                              | 468K                                                   | 180K                                                   |
| PLL               | 2                                                 | 2                                                      | 2                                                      |
| Onboard Flash     | 32Mbits NOR Flash                                 | 32Mbits NOR Flash                                      | 32Mbits NOR Flash                                      |
| LEDs              |                                                   | 6                                                      |                                                        |

### Shape

| Tang Primer 20K                                                                              | Tang Primer 20K Dock                                             | Tang Primer 20K Lite                                                         |
| -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| <img src="/hardware/zh/tang/tang-primer-20k/assets/20k_core.png" alt="20k_core" width="85%"> | ![dock-up](/hardware/zh/tang/tang-primer-20k/assets/dock-up.png) | ![20k_lite_home](/hardware/zh/tang/tang-primer-20k/assets/20k_lite_home.png) |

## FPGA boards selection suggestion

For the beginner, [Tang Nano 1K](https://wiki.sipeed.com/tang1k) and [Tang Nano 9K](https://wiki.sipeed.com/tang9k) are the good choice to start FPGA.

For those who can design the PCB and want to know more about FPGA, [Tang Nano 4K](https://wiki.sipeed.com/tang4k) and [Tang Nano 20K](https://wiki.sipeed.com/nano20k) are good, because [Tang Nano 4K](https://wiki.sipeed.com/tang4k) can be used for driving DVP camera, and [Tang Nano 20K](https://wiki.sipeed.com/nano20k) is Retro Games friendly. Besides, [Tang Primer 20K](https://wiki.sipeed.com/primer20k) is a really good choice for secondary design, because it provides many pins.

If you don't know how to design the PCB, but you want to know more about FPGA, [Tang Primer 20K Dock](https://wiki.sipeed.com/primer20k) and [Tang Primer 20K Lite](https://wiki.sipeed.com/primer20k) are really good. [Tang Primer 20K Dock](https://wiki.sipeed.com/primer20k) provides enough connector, while [Tang Primer 20K Lite](https://wiki.sipeed.com/primer20k) provides many and many pins.

## Comparison

<table>
<thead>
<tr>
  <th style="text-align:left"></th>
  <th style="white-space:nowrap">Tang Primer 20K Dock</th>
  <th style="white-space:nowrap">Tang Nano 20K</th>
  <th style="white-space:nowrap">Tang Nano 9K</th>
  <th style="white-space:nowrap">Tang Nano 4K</th>
  <th style="white-space:nowrap">Tang Nano 1K</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="text-align:left">Chip series  </td>
  <td style="text-align:left">GW2A-18  </td>
  <td style="text-align:left">GW2AR-18 </td>
  <td style="text-align:left">GW1NR-9  </td>
  <td style="text-align:left">GW1NSR-4C</td>
  <td style="text-align:left">GW1NZ-1  </td>
</tr>
<tr>
  <td style="text-align:left">Chip version  </td>
  <td style="text-align:left">C        </td>
  <td style="text-align:left">C        </td>
  <td style="text-align:left">C        </td>
  <td style="text-align:left">         </td>
  <td style="text-align:left">         </td>
</tr>
<tr>
  <td style="text-align:left">Logic units(LUT4)</td>
  <td style="text-align:left">20736        </td>
  <td style="text-align:left">20736        </td>
  <td style="text-align:left">8640         </td>
  <td style="text-align:left">4608         </td>
  <td style="text-align:left">1152         </td>
</tr>
<tr>
  <td style="text-align:left">Flip-flop(FF)</td>
  <td style="text-align:left">15552    </td>
  <td style="text-align:left">15552    </td>
  <td style="text-align:left">6480     </td>
  <td style="text-align:left">3456     </td>
  <td style="text-align:left">864      </td>
</tr>
<tr>
  <td style="text-align:left">S-SRAM (bits)</td>
  <td style="text-align:left">41472</td>
  <td style="text-align:left">41472</td>
  <td style="text-align:left">17280</td>
  <td style="text-align:left"></td>
  <td style="text-align:left">4K</td>
</tr>
<tr>
  <td style="text-align:left">B-SRAM (bits)</td>
  <td style="text-align:left">828K</td>
  <td style="text-align:left">828K</td>
  <td style="text-align:left">468K</td>
  <td style="text-align:left">180K</td>
  <td style="text-align:left">72K </td>
</tr>
<tr>
  <td style="text-align:left">Users Flash</td>
  <td style="text-align:left"></td>
  <td style="text-align:left"></td>
  <td style="text-align:left">608K</td>
  <td style="text-align:left">256K</td>
  <td style="text-align:left">64K</td>
</tr>
<tr>
  <td style="text-align:left">DSP</td>
  <td style="text-align:left">48</td>
  <td style="text-align:left">48</td>
  <td style="text-align:left">20</td>
  <td style="text-align:left">16</td>
  <td style="text-align:left"> </td>
</tr>
<tr>
  <td style="text-align:left">Extra RAM</td>
  <td style="text-align:left">DDR SDRAM<br>1G bits Capacity<br>16 bits width</td>
  <td style="text-align:left">SDR SDRAM<br>64M bits Capacity<br>32 bits width</td>
  <td style="text-align:left">PSRAM<br>64M bits Capacity<br>32 bits width</td>
  <td style="text-align:left">HyperRAM<br>64M bits Capacity<br>8 bits width</td>
  <td style="text-align:left"></td>
</tr>
<tr>
  <td style="text-align:left">PLL</td>
  <td style="text-align:left">4</td>
  <td style="text-align:left">2</td>
  <td style="text-align:left">2</td>
  <td style="text-align:left">2</td>
  <td style="text-align:left">1</td>
</tr>
<tr>
  <td style="text-align:left">Onboard Flash</td>
  <td style="text-align:left">64Mbits Flash</td>
  <td style="text-align:left">32Mbits Flash</td>
  <td style="text-align:left">32Mbits Flash</td>
  <td style="text-align:left">32Mbits Flash</td>
  <td style="text-align:left"> </td>
</tr>
<tr>
  <td style="text-align:left">Hardcore</td>
  <td style="text-align:left"></td>
  <td style="text-align:left"></td>
  <td style="text-align:left"></td>
  <td style="text-align:left">Cortex-M3</td>
  <td style="text-align:left"></td>
</tr>
<tr>
  <td style="text-align:left">Camera</td>
  <td style="text-align:left">DVP</td>
  <td style="text-align:left"></td>
  <td style="text-align:left"></td>
  <td style="text-align:left">DVP</td>
  <td style="text-align:left"></td>
</tr>
<tr>
  <td style="text-align:left">HDMI</td>
  <td style="text-align:left">Y</td>
  <td style="text-align:left">Y</td>
  <td style="text-align:left">Y</td>
  <td style="text-align:left">Y</td>
  <td style="text-align:left"></td>
</tr>
<tr>
  <td style="text-align:left">RGB Screen</td>
  <td style="text-align:left">Y</td>
  <td style="text-align:left">Y</td>
  <td style="text-align:left">Y</td>
  <td style="text-align:left"></td>
  <td style="text-align:left">Y</td>
</tr>
<tr>
  <td style="text-align:left">SPI interface</td>
  <td style="text-align:left">Y</td>
  <td style="text-align:left"></td>
  <td style="text-align:left">Y</td>
  <td style="text-align:left"></td>
  <td style="text-align:left"></td>
</tr>
<tr>
  <td style="text-align:left">Ethernet</td>
  <td style="text-align:left">Y</td>
  <td style="text-align:left"></td>
  <td style="text-align:left"></td>
  <td style="text-align:left"></td>
  <td style="text-align:left"></td>
</tr>
<tr>
  <td style="text-align:left">USB 2.0</td>
  <td style="text-align:left">Y</td>
  <td style="text-align:left"></td>
  <td style="text-align:left"></td>
  <td style="text-align:left"></td>
  <td style="text-align:left"></td>
</tr>
<tr>
  <td style="text-align:left">WS2812</td>
  <td style="text-align:left">Y</td>
  <td style="text-align:left">Y</td>
  <td style="text-align:left"></td>
  <td style="text-align:left"></td>
  <td style="text-align:left"></td>
</tr>
<tr>
  <td style="text-align:left">MS5351</td>
  <td style="text-align:left"></td>
  <td style="text-align:left">Y</td>
  <td style="text-align:left"></td>
  <td style="text-align:left"></td>
  <td style="text-align:left"></td>
</tr>
<tr>
  <td style="text-align:left">Features</td>
  <td style="text-align:left">Many LUTs, many interfaces, easy to use.</td>
  <td style="text-align:left">Many LUTs, tiny size, multiple clocks</td>
  <td style="text-align:left">Good price, enough for softcore</td>
  <td style="text-align:left">FPGA SOC board，can drive DVP camera</td>
  <td style="text-align:left">Cheapest FPGA board</td>
</tr>
<tr>
  <td style="text-align:left">Detailed information</td>
  <td style="text-align:left"><a href="https://wiki.sipeed.com/primer20k">Click me</a></td>
  <td style="text-align:left"><a href="https://wiki.sipeed.com/nano20k">Click me</a></td>
  <td style="text-align:left"><a href="https://wiki.sipeed.com/tang9k">Click me</a></td>
  <td style="text-align:left"><a href="https://wiki.sipeed.com/tang4k">Click me</a></td>
  <td style="text-align:left"><a href="https://wiki.sipeed.com/tang1k">Click me</a></td>
</tr>
</tbody>
</table>