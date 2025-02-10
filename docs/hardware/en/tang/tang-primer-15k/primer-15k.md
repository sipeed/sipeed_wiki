---
title: Tang Primer 15K Dock
keywords: FPGA, Tang, Primer, 15K
update:
  - date: 06-26-2024
    version: v0.1
    author: Serika
    content:
      - Create document
---
## Overview

  Date to Release: Autumn 2024
  TBD

  aliexpress purchase link: [Click me](https://sipeed.aliexpress.com/store/1101739727)

## Board Features

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
			<td style="text-align:left"><a href="https://www.gowinsemi.com.cn/prod_view.aspx?TypeId=74&FId=t3:10:3&Id=188#G15K">GW5ART-15MG132P</a>
			</td>
			<td style="text-align:left">
				<table>
					<tr>
						<td>Logic Unit (LUT4)</td>
						<td>15120</td>
					</tr>
					<tr>
						<td>Register (FF)</td>
						<td>15120</td>
					</tr>
					<tr>
						<td>Distributed SRAM<br>(S-SRAM) (Kbits)</td>
						<td>118125</td>
					</tr>
					<tr>
						<td>Block SRAM (B-SRAM) (Kbits)</td>
						<td>630</td>
					</tr>
					<tr>
						<td>Number of Block SRAMs (B-SRAM) (pcs)</td>
						<td>35</td>
					</tr>
					<tr>
						<td>Multiplier (18x18 Multiplier)</td>
						<td>28+12</td>
					</tr>
					<tr>
						<td>Phase-Locked Loop (PLLs)</td>
						<td>2</td>
					</tr>
					    <td>Global Clock<</td>
                        <td>16</td>
                    </tr>
                    <tr>
                        <td>High-Speed Clock<</td>
                        <td>2</td>
                    </tr>
					                    <tr>
                        <td>Transceivers</td>
                        <td>8</td>
                    </tr>
                    <tr>
                        <td>Transceivers Rate</td>
                        <td>270Mbps-6.6Gbps</td>
                    </tr>
                    <tr>
                        <td>PCIe HardCore</td>
                        <td>1<br>Speed optional x1, x2, x4, x8 PCIe 2.0<</td>
                    </tr>
                    <tr>
                        <td>LVDS (Gbps)</td>
                        <td>1.25</td>
                    </tr>
					    <td>MIPI D-PHY HardCore</td>
                        <td>2.5Gbps（RX/TX），<br>4x data lane，<br>1x clock lane</td>
                    </tr>
                    <tr>
                        <td>MIPI C-PHY HardCore</td>
                        <td>2.5Gbps（RX/TX），<br>=5.75Gbps,RX/TX<br>3x 3bit data lane</td>
                    </tr>
					<tr>
                        <td>PSRAM</td>
                        <td>64Mb @ 667MHz</td>
                    </tr>
                    <tr>
                        <td>ADC</td>
                        <td>1</td>
                    </tr>
					<tr>
						<td>Total GPIO Bank</td>
						<td>4</td>
				</table>
			</td>
		</tr>
		<tr>
			<td style="text-align:left">Flash</td>
			<td style="text-align:left">64Mb</td>
			<td style="text-align:left">See <a href="#burn_flash">How to Burn to Flash</a></td>
		</tr>
		<tr>
			<td style="text-align:left">>Debug Interface</td>
			<td style="text-align:left">TBD</td>
			<td style="text-align:left">TBD</td>
		</tr>
		<tr>
			<td style="text-align:left">Overall Package</td>
			<td style="text-align:left">TBD</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left">GPIO</td>
			<td style="text-align:left"> 53</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left"> MIPI IO </td>
			<td style="text-align:left"> 10</td>
			<td style="text-align:left">Supports both C-PHY & D-PHY</td>
		</tr>
	</tbody>
</table>

## Dock board Parameters


<table>
	<thead>
		<tr>
			<th style="text-align:center">Item</th>
			<th style="text-align:center">Parameter</th>
			<th style="text-align:center">comment</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align:left">Debugger</td>
			<td style="text-align:left">TBD</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left">USB-A</td>
			<td style="text-align:left">TBD</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left"> IOs Headers </td>
			<td style="text-align:left"> TBD</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left"> PMOD </td>
			<td style="text-align:left"> TBD</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left">Buttons</td>
			<td style="text-align:left">TBD</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left">Size</td>
			<td style="text-align:left">TBD</td>
			<td style="text-align:left"></td>
		</tr>
	</tbody>
</table>

## Hardware Resources

- [Specification](https://dl.sipeed.com/shareURL/TANG/Primer_15K/01_Specification)
- [Schematics](https://dl.sipeed.com/shareURL/TANG/Primer_15K/02_Schematic)
- [PCB BOM](https://dl.sipeed.com/shareURL/TANG/Primer_15K/03_Designator_drawing)
- [Dimension Diagram](https://dl.sipeed.com/shareURL/TANG/Primer_15K/04_Mechanical_drawing)
- [3D Model](https://dl.sipeed.com/shareURL/TANG/Primer_15K/05_3D_file)
- [Some Chip Manuals](https://dl.sipeed.com/shareURL/TANG/Primer_15K/07_Datasheet)


## Getting Started

Note that 15K is currently not supported by the education version, and you need to download V1.9.9.04 or a newer version of the commercial IDE for use.  
Licence can be applied on the Gowin official website, or you can use the online Lic service provided by Sipeed. In the IDE, select Float Lic and fill in the following information:

~~~
ip: 106.55.34.119
port: 10559
~~~

if the ip not work, try use "gowinlic.sipeed.com" domain's IP.

if you don't want to apply for a license, you can  choose the education version IDE. The education version IDE can be used without a license, but it usually only contains a limited number of IPs.

Install IDE [Click me](https://wiki.sipeed.com/hardware/zh/tang/common-doc/get_started/install-the-ide.html)


Example code [github](https://github.com/sipeed/TangPrimer-15K-example)

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
  - Goto**[GitHub project page](https://github.com/sipeed/TangPrimer-15K-example)**and submit issues
  - Business email : [support@sipeed.com](support@sipeed.com)

### TFrequently Asked Questions (FAQs)

TBD


