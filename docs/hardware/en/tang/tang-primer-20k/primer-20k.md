# Tang Primer 20K

## Preface

Tang Primer 20K is a core board with DDR3 sodimm shape based on [GW2A-V18PG256C8IC8I7](https://www.gowinsemi.com/en/product/detail/38/) as the main chip, with 2 ext-boards are prepared, the Dock and the Lite.

## Core board

### Peripherals block

<div>
    <img src="./assets/20k_front.png" width=45%>
    <img src="./assets/20k_back.png" width=45%>
</div>

### Parameters

<table>
	<thead>
		<tr>
			<th style="text-align:center">Item</th>
			<th style="text-align:center">Parameter</th>
			<th style="text-align:center">Addition</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align:left">Chip</td>
			<td style="text-align:left"><a href="http://www.gowinsemi.com.cn/prod_view.aspx?TypeId=10&amp;FId=t3:10:3&amp;Id=167#GW2A">GW2A-LV18PG256C8IC8I7</a>
			</td>
			<td style="text-align:left">
				<table>
					<tr>
						<td>Logic units(LUT4)</td>
						<td>20736</td>
					</tr>
					<tr>
						<td>Flip-Flop(FF)</td>
						<td>15552</td>
					</tr>
					<tr>
						<td>Shadow SRAM S-SRAM(bits)</td>
						<td>41472</td>
					</tr>
					<tr>
						<td>Block SRAM B-SRAM(bits)</td>
						<td>828K</td>
					</tr>
					<tr>
						<td>Number of B-SRAM</td>
						<td>46</td>
					</tr>
					<tr>
						<td>18x18 Multiplier</td>
						<td>48</td>
					</tr>
					<tr>
						<td>PLLs</td>
						<td>4</td>
					</tr>
					<tr>
						<td>I/O Bank</td>
						<td>8</td>
					</tr>
				</table>
			</td>
		</tr>
		<tr>
			<td style="text-align:left">Memory</td>
			<td style="text-align:left">128M DDR3</td>
			<td style="text-align:left">13Row x 10Col x 8banks x 16bits</td>
		</tr>
		<tr>
			<td style="text-align:left">Flash</td>
			<td style="text-align:left">32Mbits NOR Flash</td>
			<td style="text-align:left">W25Q32JVS</td>
		</tr>
		<tr>
			<td style="text-align:left">Debugger</td>
			<td style="text-align:left">Jtag + Uart</td>
			<td style="text-align:left">JST SH1.0 8Pins connector</td>
		</tr>
		<tr>
			<td style="text-align:left">SD card slot</td>
			<td style="text-align:left">1</td>
			<td style="text-align:left">Push-pull type</td>
		</tr>
		<tr>
			<td style="text-align:left">Display</td>
			<td style="text-align:left">8Pins spi lcd connector</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left">Package</td>
			<td style="text-align:left">204P DDR3</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left">Avaliable IO</td>
			<td style="text-align:left">117</td>
			<td style="text-align:left"></td>
		</tr>
	</tbody>
</table>

## Comparison between ext-board

### Dock ext-board appearance

The corresponding pins numbering of LED2 and LED3 is N16 and N14. See the mark on left of the right picture.

<div>
<img src="./../../../zh/tang/tang-primer-20k/assets/dock-up.png" alt="dock-up" width=45%>
<img src="./../../../zh/tang/tang-primer-20k/assets/dock-back.png" alt="dock-back" width=45%>
</div>

### Lite ext-board appearance

The corresponding pin numbering between R8 and P9 is P8. See the mark on the top left of the right picture.

<div>
<img src="./../../../zh/tang/tang-primer-20k/assets/lite-up.png" alt="lite-up" width=45%>
<img src="./../../../zh/tang/tang-primer-20k/assets/lite-back.png" alt="lite-back" width=45%>
</div>

### Comparison between peripherals of ext-board

<table>
	<thead>
		<tr>
			<th rowspan="2" colspan="2">Item</th>
			<th colspan="2">Dock</th>
			<th colspan="1">Lite</th>
		</tr>
		<tr>
			<th>Number</th>
			<th>Addition</th>
			<th>Number</th>
		</tr>
	</thead>
	<body>
		<tr>
			<td colspan="2">RGB Interface</td>
			<td>1</td>
			<td>RGB565 40P FPC Connector</td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">DVP Interface</td>
			<td>1</td>
			<td>24P FPC Connector</td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">Mic array Interface</td>
			<td>1</td>
			<td>10P FPC Connector</td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">Touch Interface</td>
			<td>1</td>
			<td>4P FPC Connector</td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">PMOD Interface</td>
			<td>4</td>
			<td></td>
			<td>4</td>
		</tr>
		<tr>
			<td colspan="2">3.5mm headphone Jack</td>
			<td>1</td>
			<td>LPA4809MSF driver</td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">DIP switch</td>
			<td>1</td>
			<td>5P DIP switch</td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">Slide switch</td>
			<td>1</td>
			<td>Switch USB function</td>
			<td>2</td>
		</tr>
		<tr>
			<td style="white-space:nowrap" rowspan="2">Type-C</td>
			<td style="white-space:nowrap">USB-JTAG&UART</td>
			<td>1</td>
			<td>Onboard BL702 used to download bitstream file and provide serial communication</td>
			<td></td>
		</tr>
		<tr>
			<td style="white-space:nowrap">User-defined USB</td>
			<td>1</td>
			<td>USB3317 with Slide switch to change USB Interface function</td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">Wireless antenna</td>
			<td>1</td>
			<td>BL702 wireless function</td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">Key</td>
			<td>6</td>
			<td>One used for burning BL702,<br>five for Users</td>
			<td>2</td>
		</tr>
		<tr>
			<td colspan="2">LED</td>
			<td>6</td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">HDMI Interface</td>
			<td>1</td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">Ethernet Interface</td>
			<td>1</td>
			<td>TL8201F</td>
			<td></td>
		</tr>
		<!-- <tr>
			<td colspan="2">RGB LED</td>
			<td>1</td>
			<td>WS2812</td>
			<td></td>
		</tr> -->
	</body>
</table>

## Hardware information

Datasheet, Schematic and dimensional drawing about hardware design can be found [here](https://dl.sipeed.com/shareURL/TANG/Primer_20K)

## User guide

1. Install IDE: [Click me](./../Tang-Nano-Doc/install-the-ide.md).

2. Visit [Start to use](./start.md) to avoid some problems, and we can start coding for FPGA there.

3. After coding for FPGA, if you think it difficult, here we collect some useful learning resource.
   + Online FPGA tutorial: [Verilog](https://www.asic-world.com/verilog/index.html)
   + Online Verilog exercise：[HDLBits](https://hdlbits.01xz.net/wiki/Main_Page)

	If you have trouble using IDE, we have packed all documents about IDE, visit [Download station](https://dl.sipeed.com/shareURL/TANG/Primer_20K/07_Chip_manual/EN/General%20Guide) and download what you need.

## Reference examples summary

### Open codes

github ：https://github.com/sipeed/TangPrimer-20K-example

### Tutorial

- Lite ext-board blink ：[Click me](./examples/lite/blink.md)
- Dock ext-board examples summary : [Click me](./example.md)








































## Attention

1. If you have trouble with this board, you can join our telegram (t.me/sipeed) or contact us on twitter (https://twitter.com/SipeedIO).

2. For fpga burning we require using [this](https://dl.sipeed.com/shareURL/TANG/programmer) Programmer application. Because other version Programmer application may fail burning this board.

3. If you meet problems, please visit [problems](./../Tang-Nano-Doc/questions.md) first, normally most problems will be solved after using this programmer [Click me](https://dl.sipeed.com/shareURL/TANG/programmer).
   
4. Avoid using JTAG, MODE0/1 and DONE pins. If you really need to use these pins, please refer to [SUG100-2.6E_Gowin Software User Guide.pdf](https://dl.sipeed.com/fileList/TANG/Nano%209K/6_Chip_Manual/EN/General%20Guide/SUG100-2.6E_Gowin%20Software%20User%20Guide.pdf).

5. Please avoid static electricity hitting PCBA; Please release the static electricity from the hand before contacting PCBA.

6. The working voltage of each GPIO has been marked in the schematic . Please do not let the actual working voltage of GPIO exceed the rated value, because it will cause permanent damage to PCBA.

7. When connecting FPC flexible cable, make sure the cable is completely inserted into the base with on offset.

8. Avoid any liquid or metal touching the pads of components on PCBA during working, because this will cause short circuit and damage PCBA.