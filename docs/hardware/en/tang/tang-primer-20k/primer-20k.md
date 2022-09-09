# Tang Primer 20K

## Preface

Tang Primer 20K is a core board with DDR3 sodimm shape using [GW2A-V18PG256C8IC8I7](https://www.gowinsemi.com/en/product/detail/38/) as the main chip, 2 ext-boards are prepared, the Dock and the Lite. Being as the 6th FPGA board sold by Sipeed, Tang Primer 20K has always been expected.

**Notice: Dock ext-board will be ready in October**

Dock ext-board and Lite ext-board contains different resources. The Dock ext-board can be used to drive peripherals like dvp camera, rgb screen, Gigabit Ethernet and other peripherals direclty and quickly, which save user's time to verify codes. Besides, there is a [USB-softcore](http://www.gowinsemi.com.cn/enrollment_view.aspx?TypeId=67&Id=858&FId=t27:67:27#IP) provided by GOWIN, you can try it by yourself if you are instarected enough. The Lite ext-board routes out almost all IO, and there are some Differential pins routed to pin headers, users can design instresting ext-module to use this kit, line length and impedance data are [here](https://dl.sipeed.com/shareURL/TANG/Primer_20K/04_Net_Length).

## Core board

### Peripherals block

<div>
    <img src="./assets/20k_front.png" width=45%>
    <img src="./assets/20k_back.png" width=45%>
</div>

### Specs

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
		<tr>
			<td colspan="2">RGB LED</td>
			<td>1</td>
			<td>WS2812</td>
			<td></td>
		</tr>
	</body>
</table>

## Target user

| Usage     | FPGA                             | MCU                                | FPGA+MCU                     |
| :---- | :---------- | :------------- | :----------------- |
| Language     | Verilog HDL/Verilog         | C/C++               | Verilog HDL/Verilog ，  C/C++                |
| Introduction     | Verify HDL on FPGA | Burn softcore bitstream into chip then <br>use Primer 20K as normal MCU| After flashing the softcore bitstream,
it can be used as two chips |
| User |  Beginner，FPGA developer  | RISC-V developers，Cortex-M developers | Senior engineer |

## User guide

1. Check the board whether it works.

1. Download our packaged user guide document : [Click me](https://dl.sipeed.com/shareURL/TANG/Nano%209K/6_Chip_Manual/EN/General%20Guide) (All PDFs mentioned below are here)
   
2. Install IDE and configure license : <a href="https://wiki.sipeed.com/hardware/en/tang/Tang-Nano-Doc/install-the-ide.html" target="blank">Click me</a>
   
3. Read this file : [SUG100-2.6E_Gowin Software User Guide.pdf](https://dl.sipeed.com/fileList/TANG/Nano%209K/6_Chip_Manual/EN/General%20Guide/SUG100-2.6E_Gowin%20Software%20User%20Guide.pdf)

4. Read this [tutorial] (On building) (LEDs Blink experiment).
   We suggest you recreate a project ang light the led by yourself, this can help you know more about the steps about fpga.
   We recommended you read the following tips during this process:
   - Verilog code specifications (please search by yourself. It is very necessary to obey good code specifications from beginning)
   
	The following documents are very useful for learning FPGA, so we should read them.
	   - SUG949-1.1E_Gowin HDL Coding User Guide.pdf
	   - UG286-1.9.1E_Gowin Clock User Guide.pdf
	The documents mentioned above can be downloaded from our [Download station](https://dl.sipeed.com/shareURL/TANG/Nano%209K/6_Chip_Manual/EN/General%20Guide)
   	And there has been a compressed package contains all documents

   Online tutorial:  
   We suggest two excellent learning sites about verilog : [HDLBITs](https://hdlbits.01xz.net/wiki/Main_Page) and [Verilog Page](https://www.asic-world.com/verilog/index.html)

## Reference examples summary

https://github.com/sipeed/TangPrimer-20K-example

Examples update time:

- LED drive ：Update on 2022.08.22

## Hardware files

[All hardware files](https://dl.sipeed.com/shareURL/TANG/Primer_20K)

## Attention

1. If you have trouble with this board, you can join our telegram (t.me/sipeed) or contact us on twitter (https://twitter.com/SipeedIO).

2. For fpga burning we require using [this](https://dl.sipeed.com/shareURL/TANG/programmer) Programmer application. Because other version Programmer application may fail burning this board.

3. If you meet problems, please visit [problems](./../Tang-Nano-Doc/questions.md) first, normally most problems will be solved after using this programmer [Click me](https://dl.sipeed.com/shareURL/TANG/programmer).
   
4. Avoid using JTAG, MODE0/1 and DONE pins. If you really need to use these pins, please refer to [SUG100-2.6E_Gowin Software User Guide.pdf](https://dl.sipeed.com/fileList/TANG/Nano%209K/6_Chip_Manual/EN/General%20Guide/SUG100-2.6E_Gowin%20Software%20User%20Guide.pdf).

5. Please avoid static electricity hitting PCBA; Please release the static electricity from the hand before contacting PCBA.

6. The working voltage of each GPIO has been marked in the schematic . Please do not let the actual working voltage of GPIO exceed the rated value, because it will cause permanent damage to PCBA.

7. When connecting FPC flexible cable, make sure the cable is completely inserted into the base with on offset.

8. Avoid any liquid or metal touching the pads of components on PCBA during working, because this will cause short circuit and damage PCBA.