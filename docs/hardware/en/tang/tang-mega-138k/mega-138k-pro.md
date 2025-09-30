---
title: Tang Mega 138K Pro Dock
keywords: FPGA, Tang, Mega, 138K
update:
  - date: 2023-08-29
    version: v
    author: wonder
    content:
      - Creat document
  - date: 2024-09-26
    version: v0.2
    author: Serika
    content:
      - Update FAQs
  - date: 2025-01-24
    version: v0.3
    author: Serika
    content:
      - Add Secondary lic server ip addr.
---

- Product Overview

  Tang Mega 138K uses a 22nm process GW5AST-LV138FPG676A FPGA chip, which has 138,240 lookup table units and nearly 300 DSP units. It contains eight high-speed transceivers with a speed range of 270Mbps ~ 12.5Gbps, suitable for transmitting data through high-speed ports such as fiber optics or PCIE. In addition, the chip contains a hard-core PCIE, which consumes better resources when using PCIE and achieves better performance. It is suitable for high-speed communication, protocol conversion, high-performance computing, and other occasions.

  aliexpress purchase link: [Click me](https://www.aliexpress.us/item/3256805893801730.html)

  ## Board Features

  - Large capacity LUT
  - Large capacity memory
  - PCIe 3.0 x 4
  - SFP+ x 2
  - RISCV hard core

## Product Appearance

<img src="./assets/mega_138k_pro_top.png" width="45%">

## Hardware Parameters

### SOM Board Parameters

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
			<td style="text-align:left">FPGA Chip</td>
			<td style="text-align:left"><a href="https://www.gowinsemi.com/en/product/detail/60/">GW5AST-LV138FPG676A</a>
			</td>
			<td style="text-align:left">
				<table>
					<tr>
						<td>Logic Unit (LUT4)</td>
						<td>138240</td>
					</tr>
					<tr>
						<td>Register (FF)</td>
						<td>138240</td>
					</tr>
					<tr>
						<td>Distributed SRAM (S-SRAM) (Kbits)</td>
						<td>1080</td>
					</tr>
					<tr>
						<td>Block SRAM (B-SRAM) (Kbits)</td>
						<td>6120</td>
					</tr>
					<tr>
						<td>Number of Block SRAMs (B-SRAM) (pcs)</td>
						<td>340</td>
					</tr>
					<tr>
						<td>Multiplier (18x18 Multiplier)</td>
						<td>298</td>
					</tr>
					<tr>
						<td>Phase-Locked Loop (PLLs)</td>
						<td>12</td>
					</tr>
                    <tr>
                        <td>Global Clock</td>
                        <td>16</td>
                    </tr>
                    <tr>
                        <td>High-Speed Clock</td>
                        <td>24</td>
                    </tr>
                    <tr>
                        <td>Transceivers</td>
                        <td>8</td>
                    </tr>
                    <tr>
                        <td>Transceivers Rate</td>
                        <td>270Mbps-12.5Gbps</td>
                    </tr>
                    <tr>
                        <td>PCIE Hard Core</td>
                        <td>1<br>Speed optional x1, x2, x4, x8 PCIe 3.0</td>
                    </tr>
                    <tr>
                        <td>LVDS (Gbps)</td>
                        <td>1.25</td>
                    </tr>
                    <tr>
                        <td>DDR3 (Mbps)</td>
                        <td>1,333</td>
                    </tr>
                    <tr>
                        <td>MIPI D-PHY Hard Core</td>
                        <td>2.5Gbps (RX),<br>8 data channels,<br>2 clock channels</td>
                    </tr>
                    <tr>
                        <td>Hard Core SoC</td>
                        <td>RiscV AE350_SOC</td>
                    </tr>
                    <tr>
                        <td>ADC</td>
                        <td>2</td>
                    </tr>
					<tr>
						<td>Total I/O Bank</td>
						<td>10</td>
					</tr>
				</table>
			</td>
		</tr>
		<tr>
			<td style="text-align:left">Memory</td>
			<td style="text-align:left">1GB DDR3</td>
			<td style="text-align:left">512MB x 2</td>
		</tr>
		<tr>
			<td style="text-align:left">Flash</td>
			<td style="text-align:left">128Mbits Flash x 2</td>
			<td style="text-align:left">See <a href="#burn_flash">How to Burn to Flash</a></td>
		</tr>
		<tr>
			<td style="text-align:left">Debug Interface</td>
			<td style="text-align:left">Jtag + Uart</td>
			<td style="text-align:left">JST SH1.0 8Pins Connector</td>
		</tr>
		<tr>
			<td style="text-align:left">Overall Package</td>
			<td style="text-align:left">50mm x 70mm Size</td>
			<td style="text-align:left">BTB CONN. Connects the SOM and the Dock Board</td>
		</tr>
	</tbody>
</table>

### Dock board Parameters

| Item                | Quantity | Remarks                                           |
| :------------------ | -------- | ------------------------------------------------- |
| LED                 | 6        |                                                   |
| WS2812              | 1        | The WS2812 & aRGB strip CONN. share the same pin  |
| Button              | 4        |                                                   |
| PCIE                | 1        |                                                   |
| SFP+                | 2        |                                                   |
| Gigabit Ethernet    | 1        |                                                   |
| DVI RX              | 2        | Mutually occupied with DVI TX                    |
| DVI TX              | 2        | Mutually occupied with DVI RX                    |
| PMOD                | 3        |                                                   |
| ADC                 | 2        |                                                   |
| MIPI CSI            | 2        | 3 LANE MIPI CSI                                   |
| WS2812              | 1        | The aRGB strip CONN. & WS2812 share the same pin  |
| DVP Interface       | 1        |                                                   |
| RGB Interface       | 1        | Supports RGB888 screen                            |
| MIC ARRAY Interface | 1        | Supports connecting Sipeed 6+1 microphone array   |
| SD Card Slot        | 1        |                                                   |
| EEPROM              | 1        | Can store necessary information                  |
| M.2 Socket          | 1        | Reserved, can write peripheral driver yourself    |
| PWM Fan Interface   | 1        |                                                   |
| Speaker Interface   | 1        |                                                   |
| 3.5mm Headphone Jack| 1        |                                                   |
| Custom USB          | 1        | Cannot power the board                            |
| MS5351              | 2        | Provides RefClk for Serdes; control output via onboard UART |
| USB JTAG&UART       | 1        | Supports FPGA programming and provides UART function |
| 40P Pin Header      | 1        |                                                   |
| Power Switch        | 1        |                                                   |
| 12V DC              | 1        |                                                   |

## Hardware Resources

~~[Board Specification](https://dl.sipeed.com/shareURL/TANG/Mega_138K_Pro/01_Specification)~~
[Board Schematic](https://dl.sipeed.com/shareURL/TANG/Mega_138K_Pro/02_Schematic)
[PCB BOM](https://dl.sipeed.com/shareURL/TANG/Mega_138K_Pro/03_Designator_drawing)
[Board Dimension Diagram](https://dl.sipeed.com/shareURL/TANG/Mega_138K_Pro/04_Mechanical_drawing)
[Board 3D Model](https://dl.sipeed.com/shareURL/TANG/Mega_138K_Pro/05_3D_file)
[Some Chip Manuals](https://dl.sipeed.com/shareURL/TANG/Mega_138K_Pro/07_Datasheet)

## Getting Started

Note that 138K Pro is currently not supported by the education version, and you need to download V1.9.9 or a newer version of the commercial IDE for use.  
Lic can be applied on the Gowin official website, or you can use the online Lic service provided by Sipeed. In the IDE, select Float Lic and fill in the following information:

~~~
---Server 01---
ip: 45.33.107.56
port: 10559

---Server 02---
ip: 106.55.34.119
port: 10559
~~~

if the ip not work, try use "gowinlic.sipeed.com" domain's IP.

Install IDE [Click me](https://wiki.sipeed.com/hardware/zh/tang/common-doc/get_started/install-the-ide.html)


Example code [github](https://github.com/sipeed/TangMega-138KPro-example)

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
  - Business email : [support@sipeed.com](support@sipeed.com)

## Precautions

<table>
    <tr>
        <th>Item</th>
        <th>Precautions</th>
    </tr>
    <tr>
        <td>Chip Model</td>
        <td>The specific model of the FPGA chip used by Tang Mega 138K Pro is GW5AST-LV138FPG676A. Please select the package model <span><b>FCPBG676A</b></span> & <span><b>Device Version: B</b></span> in the IDE.
        <a href="../common-doc/questions#How-to-Identify-Device-Version">How to identify the device version</a></td>
    </tr>
    </tr>
    <tr>
        <td>Static Electricity</td>
        <td>Please avoid static electricity hitting the PCBA; release the static electricity from your hands before touching the PCBA.</td>
    </tr>
    <tr>
        <td>Tolerance Voltage</td>
        <td>When using GPIO pin headers for external communication, ensure that the IO voltage is 3.3V. Excessive voltage will permanently damage the PCBA.</td>
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
    <tr>
        <td>Protecting the die</td>
        <td>Please avoid any impact on the exposed chip die during the process of removing and installing the heat sink. Do not press the heat sink hard after installing it. Otherwise, the chip die will be damaged.</td>
    </tr>
</table>


## Contact

Tang Mega 138K can meet different needs of customers in various scenarios. For technical support and business cooperation, please contact [support@sipeed.com](support@sipeed.com)

## Frequently Asked Questions (FAQs)

### The system does not recognize the onboard debugger

- Try connecting directly to the computer instead of through a USB HUB.
- Try using a better quality USB cable.
- Try another computer to rule out the computer being the problem. 
- Try [update to the latest firmware](#How-to-update-the-firmware-for-the-onboard-debugger) and try again.

### The UART of the onboard debugger cannot be used

- Try reinstall FTDI drivers.
- IF the actual baudrate is always four times the set baudrate or the UART continuously outputs garbled characters. try [update to the latest firmware](#How-to-update-the-firmware-for-the-onboard-debugger) and try again.

### OpenFPGAloader not work

- Try [update to the latest firmware](#How-to-update-the-firmware-for-the-onboard-debugger) and try again.


### How to update the firmware for the onboard debugger

- See [Update the debugger](./../common/update_debugger) for details.

### The power light is not on after the board is powered on

1. Please check if the power switch of the board is turned on.
2. Check your power supply method.

### How to burn the bitstream to FLASH {#burn_flash}

1. Setting the **Programmer** as shown in the figure below:

<img src="./assets/flash_mode.png" alt="flash_mode" width=35%>

### No Response or Undesirable Pin Phenomenon After Burning

1. First, ensure that the IDE has selected the correct model **GW5AST-LV138FPG676AC1/10**; every parameter in the figure below **MUST** be consistent.

<img src="./assets/partno_138K_Pro.png" alt="device_choose" width=35%>

2. Then, check your code and the corresponding simulation waveforms to meet the requirements. The GAO tools in GOWIN IDE maybe helpful. For more information, please refer to the GOWIN document [SUG100](https://www.gowinsemi.com/upload/database_doc/1885/document/660bb2366d0b3.pdf)(require login).


### For more questions and solutions, go to [Related Questions](./../common-doc/questions) to view