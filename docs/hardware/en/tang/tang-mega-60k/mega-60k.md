---
title: Tang Mega 60K Dock
keywords: FPGA, Tang, Mega, 60K
update:
  - date: 06-26-2024
    version: v0.1
    author: Serika
    content:
      - Create document
---

## Overview

  Date to Release: July xx, 2024
  TBD

  aliexpress purchase link: [Click me](https://sipeed.aliexpress.com/store/1101739727)

## Board Features

  - Medium capacity LUT4
  - Medium capacity memory
  - PCIe 2.0 x 4
  - USB3.0 x 1
  - MIPI C-PHY & D-PHY RX/TX
  - TBD

## Product Appearance

TBD

## Block Diagram

TBD

## Hardware Parameters

### SOM Board Parameters

<table>
	<thead>
		<tr>
			<th style="text-align:center">Item</th>
			<th style="text-align:center">Parameter</th>
			<th style="text-align:center">Supplement</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align:left">FPGA Chip</td>
			<td style="text-align:left"><a href="https://www.gowinsemi.com.cn/prod_view.aspx?TypeId=74&FId=t3:10:3&Id=188#GW5AT">GW5AT-LV60PG484A</a>
			</td>
			<td style="text-align:left">
				<table>
					<tr>
						<td>Logic Unit (LUT4)</td>
						<td>59904</td>
					</tr>
					<tr>
						<td>Register (FF)</td>
						<td>59904</td>
					</tr>
					<tr>
						<td>Distributed SRAM<br>(S-SRAM) M(Kbits)</td>
						<td>468</td>
					</tr>
					<tr>
						<td>Block SRAM (B-SRAM) (Kbits)</td>
						<td>2124</td>
					</tr>
					<tr>
						<td>Number of Block SRAMs (B-SRAM) (pcs)</td>
						<td>118</td>
					</tr>
					<tr>
						<td>Multiplier (18x18 Multiplier)</td>
						<td>118</td>
					</tr>
					<tr>
						<td>Phase-Locked Loop (PLLs)</td>
						<td>8</td>
					</tr>
                    <tr>
                        <td>Global Clock</td>
                        <td>16</td>
                    </tr>
                    <tr>
                        <td>High-Speed Clock</td>
                        <td>20</td>
                    </tr>
                    <tr>
                        <td>Transceivers</td>
                        <td>4</td>
                    </tr>
                    <tr>
                        <td>Transceivers Rate</td>
                        <td>270Mbps-12.5Gbps</td>
                    </tr>
                    <tr>
                        <td>PCIe HardCore</td>
                        <td>x1<br>Speed optional x1, x2, x4, x8 PCIe 2.0</td>
                    </tr>
                    <tr>
                        <td>LVDS (Gbps)</td>
                        <td>1.25</td>
                    </tr>
                    <tr>
                        <td>DDR3 (Mbps)</td>
                        <td>1333</td>
                    </tr>
                    <tr>
                        <td>MIPI D-PHY HardCore</td>
                        <td>2.5Gbps（RX/TX），<br>4x data lane，<br>1x clock lane</td>
                    </tr>
                    <tr>
                        <td>MIPI C-PHY HardCore</td>
                        <td>2.5Gbps（RX/TX），<br>=5.75Gbps,RX/TX<br>3x 3bit data lane</td>
                    </tr>
                    <tr>
                        <td>ADC</td>
                        <td>2</td>
                    </tr>
					<tr>
						<td>Total I/O Bank</td>
						<td>11</td>
					</tr>
				</table>
			</td>
		</tr>
		<tr>
			<td style="text-align:left">Memory</td>
			<td style="text-align:left">4Gb DDR3</td>
			<td style="text-align:left">512MB x 1</td>
		</tr>
		<tr>
			<td style="text-align:left">Flash</td>
			<td style="text-align:left">128Mbits Flash x 1</td>
			<td style="text-align:left">See <a href="#burn_flash">How to Burn to Flash</a></td>
		</tr>
		<tr>
			<td style="text-align:left">Debug Interface</td>
			<td style="text-align:left">Jtag + Uart</td>
			<td style="text-align:left">JST SH1.0 8Pins CONN.</td>
		</tr>
		<tr>
			<td style="text-align:left">Overall Package</td>
			<td style="text-align:left">35mm x 45mm Size</td>
			<td style="text-align:left">BTB CONN. Connects the SOM and the Dock Board</td>
		</tr>
	</tbody>
</table>

### Dock board Parameters

TBD

## Hardware Resources

- [Specification](https://dl.sipeed.com/shareURL/TANG/Mega_60K/01_Specification)
- [Schematics](https://dl.sipeed.com/shareURL/TANG/Mega_60K/02_Schematic)
- [PCB BOM](https://dl.sipeed.com/shareURL/TANG/Mega_60K/03_Designator_drawing)
- [Dimension Diagram](https://dl.sipeed.com/shareURL/TANG/Mega_60K/04_Mechanical_drawing)
- [3D Model](https://dl.sipeed.com/shareURL/TANG/Mega_60K/05_3D_file)
- [Some Chip Manuals](https://dl.sipeed.com/shareURL/TANG/Mega_60K/07_Datasheet)

## Getting Started

Note that 138K is currently not supported by the education version, and you need to download V1.9.9 or a newer version of the commercial IDE for use.  
Lic can be applied on the Gowin official website, or you can use the online Lic service provided by Sipeed. In the IDE, select Float Lic and fill in the following information:

~~~
ip: 106.55.34.119
port: 10559
~~~

if the ip not work, try use "gowinlic.sipeed.com" domain's IP.

Install IDE [Click me](https://wiki.sipeed.com/hardware/zh/tang/Tang-Nano-Doc/get_started/install-the-ide.html)


Example code [github](https://github.com/sipeed/TangMega-60K-example)

- Other Learning Resources

  - Free online tutorial: [Verilog Tutorial](https://www.runoob.com/w3cnote/verilog-tutorial.html) (Learn Verilog)
  - Free online FPGA tutorial: [Verilog](https://www.asic-world.com/verilog/index.html) (English website)
  - Verilog practice website: [HDLBits](https://hdlbits.01xz.net/wiki/Main_Page) (English website)
  - Online Gowin Semiconductor reference video tutorials: [Click here](http://www.gowinsemi.com.cn/video_complex.aspx?FId=n15:15:26)

  ## Communication Methods

  - **Reddit** : [reddit.com/r/GowinFPGA/](reddit.com/r/GowinFPGA/)
  - **Telegram** : [t.me/sipeed](t.me/sipeed)
  - Discussion forum: [maixhub.com/discussion](https://maixhub.com/discussion)
  - QQ discussion group: [834585530](https://jq.qq.com/?_wv=1027&k=wBb8XUan)
  - Leave a message directly below this page
  - Goto**[GitHub project page](https://github.com/sipeed/TangMega-60K-example)**and submit issues
  - Business email : [support@sipeed.com](support@sipeed.com)

## Precautions

<table>
    <tr>
        <th>Item</th>
        <th>Precautions</th>
    </tr>
    <tr>
        <td>芯片型号</td>
        <td>The specific model of the FPGA chip used by Tang Mega 138K is<b>GW5AT-LV60PG484A</b> <br> <br>Please select the package model <b>PBG484A</b> in the IDE.</td>
    </tr>
    <tr>
        <td>Static Electricity</td>
        <td>Please avoid static electricity hitting the PCBA; release the static electricity from your hands before touching the PCBA.</td>
    </tr>
    <tr>
        <td>Tolerance Voltage</td>
        <td>When using GPIO pin headers for external communication, ensure that the IO voltage is <b>3.3V</b>. Excessive voltage will permanently damage the PCBA.</td>
    </tr>
    <tr>
        <td>FPC Socket</td>
        <td>When connecting the FPC soft cable, please ensure that the cable is completely and correctly inserted into the socket without any deviation.</td>
    </tr>
    <tr>
        <td>PCIE Gold Finger</td>
        <td>When testing the PCIE gold finger, ensure that both the host and the board are in the off or unpowered state to avoid short-circuiting the gold finger due to displacement during the insertion process.</td>
    </tr>
    <tr>
        <td>Plug and Unplug</td>
        <td>Please completely power off before plugging and unplugging.</td>
    </tr>
    <tr>
        <td>Avoid Short Circuit</td>
        <td>Please avoid any liquid or metal touching the solder pads of the components on the PCBA during the power-on process, otherwise it may cause a short circuit and burn the PCBA.</td>
    </tr>
</table>


## Contact

Tang Mega 60K can meet different needs of customers in various scenarios. For technical support and business cooperation, please contact [support@sipeed.com](support@sipeed.com)


## Frequently Asked Questions (FAQs)

TBD
