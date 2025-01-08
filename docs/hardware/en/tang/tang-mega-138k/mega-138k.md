---
title: Tang Mega 138K Dock
keywords: FPGA, Tang, Mega, 138K
update:
  - date: 2024-06-26
    version: v0.1
    author: Serika
    content:
      - Create document
  - date: 2024-09-26
    version: v0.2
    author: Serika
    content:
      - Corrected description of PCIe bus widths
---

## Overview

  Tang Mega 138K uses a 22nm process **GW5AST-LV138PG484A** FPGA chip, which has 138,240 lookup table units and nearly 300 DSP units. It contains eight high-speed transceivers with a speed range of 270Mbps ~ 8.0Gbps, suitable for transmitting data through high-speed ports such as PCIe. In addition, the chip contains a hard-core PCIe, which consumes better resources when using PCIe and achieves better performance. It is suitable for high-speed communication, protocol conversion, high-performance computing, and other occasions.
  
  Compared to the 138K Pro Dock, the 138K Dock has a smaller size and a lower price, and it replaces the SFP transceiver with USB3 SS(5Gbps). This not only effectively reduces the cost of high-speed communication but also brings better versatility.

  aliexpress purchase link: [Click me](https://www.aliexpress.com/item/3256807078990410.html)

## Board Features

  - Large capacity LUT4
  - Large capacity memory
  - PCIe 2.0 x 4
  - USB3.0 x 1(5Gbps)
  - RISC-V hard core (AE350 @800MHz)
  - HDMI TX/RX x 1
  - Gigabit Ethernet x 1
  - Onboard 3.7V li-on battery(1-Series) charge/discharge management

## Product Appearance

<img src="./assets/mega_138k_top.png" width="45%">

## Block Diagram

TBD

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
			<td style="text-align:left"><a href="https://www.gowinsemi.com/en/product/detail/60/">GW5AST-LV138PG484A</a>
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
						<td>Distributed SRAM<br>(S-SRAM) (Kbits)</td>
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
						<td>Multiplier (18x18 Multiplier)/td>
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
                        <td>4</td>
                    </tr>
                    <tr>
                        <td>Transceivers Rate</td>
                        <td>270Mbps-8.0Gbps</td>
                    </tr>
                    <tr>
                        <td>PCIe HardCore</td>
                        <td>x1<br>Speed optional x1, x2, x4 PCIe 3.0</td>
                    </tr>
                    <tr>
                        <td>LVDS (Gbps)</td>
                        <td>1.25</td>
                    </tr>
                    <tr>
                        <td>DDR3 (Mbps)</td>
                        <td>800</td>
                    </tr>
                        <td>Hard Core SoC</td>
                        <td>RiscV AE350_SOC</td>
                    </tr>
                    <tr>
                        <td>ADC</td>
                        <td>2</td>
                    </tr>
					<tr>
						<td>Total I/O Bank<</td>
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
			<td style="text-align:left">128Mbits Flash x 1</td>
			<td style="text-align:left">See <a href="#burn_flash">How to Burn to Flash</a></td>
		</tr>
		<tr>
			<td style="text-align:left">>Debug Interface</td>
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

| Item                 | Quantity | Remarks                                           |
| :------------------  | ----     | ------------------------------------------------- |
| LEDs                 | 4+8      | 4x Battery-Indicator+ 8x PMOD_LED                 |
| WS2812               | 1        | The WS2812 & aRGB strip CONN. share the same pin  |
| Buttons              | 3+1      | 3x User-KEY + 1x Reconfig-KEY                     |
| PCIe                 | 1        | 4-lane @ 5Gbps，CH569 16bit HSPI                  |
| USB3                 | 2        | SuperSpeed @ 5Gbps                                |
| GbE                  | 1        | 1000Mbps Ethernet                                 |
| DVI                  | 1        | DVI supports both RX and TX                       |
| PMOD                 | 2        | Multiplexed with the the DVP CONN. & 2x20P header at the top of the Dock board |
| ADC                  | 2        | 2x differential input channels                    |
| WS2812               | 1        | The aRGB strip CONN. & WS2812 share the same pin  |
| DVP Interface        | 1        | Multiplexed with the the PMOD & 2x20P header at the top of the Dock board |
| RGB Interface        | 1        | Supports RGB888 screen                           |
| MIC ARRAY Interface  | 1        | Supports Sipeed 6+1 microphone array             |
| SD Slot              | 1        | 1-bit SDIO/MMC or SPI mode                       |
| BATT CONN.           | 1        | Supports 3.7V li-on battery, with built-in charge management |
| PWM FAN CONN.        | 1        | Supports PWM fan with TACHO                       |
| Speaker CONN.        | 2        | Support stereo output, 2x 3W Speaker              |
| 3.5mm Headphone CONN.| 1        | Supports stereo output, without Mic               |
| MS5351               | 1        | Provides RefClk for Serdes; control output via onboard UART |
| USB JTAG & UART      | 1        | Supports FPGA programming and provides UART function  |
| 2x20P headers        | 2        | 2x20P header at the top of the Dock board multiplexed with the the PMOD & DVP CONN. |
| Power button         | 1        | **Press and hold for 2 seconds to toggle power state** |
| 12V DC               | 1        | DC5521                                       |

## Hardware Resources

- [Specification](https://dl.sipeed.com/shareURL/TANG/Mega_138K_60K/01_Specification)
- [Schematics](https://dl.sipeed.com/shareURL/TANG/Mega_138K_60K/02_Schematic)
- [PCB BOM](https://dl.sipeed.com/shareURL/TANG/Mega_138K_60K/03_Designator_drawing)
- [Dimension Diagram](https://dl.sipeed.com/shareURL/TANG/Mega_138K_60K/04_Mechanical_drawing)
- [3D Model](https://dl.sipeed.com/shareURL/TANG/Mega_138K_60K/05_3D_file)
- [Some Chip Manuals](https://dl.sipeed.com/shareURL/TANG/Mega_138K_60K/07_Datasheet)
- [All PIN Constraints](https://dl.sipeed.com/shareURL/TANG/Mega_138K_60K/08_Misc)

## Getting Started

Note that 138K is currently not supported by the education version, and you need to download V1.9.9 or a newer version of the commercial IDE for use.  
There are serious problems with the Programmer version V1.9.10.02, and this product cannot be programmed.
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

Install IDE [Click me](https://wiki.sipeed.com/hardware/zh/tang/Tang-Nano-Doc/get_started/install-the-ide.html)


Example code [github](https://github.com/sipeed/TangMega-138K-example)

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
  - Goto**[GitHub project page](https://github.com/sipeed/TangMega-138K-example)**and submit issues
  - Business email : [support@sipeed.com](support@sipeed.com)

## Precautions

<table>
    <tr>
        <th>Item</th>
        <th>Precautions</th>
    </tr>
    <tr>
        <td>Chip Model</td>
        <td>The specific model of the FPGA chip used by Tang Mega 138K is <b>GW5AST-LV138FPG676A</b>. <br>Please select the package model <b>PBG484A</b> in the IDE.</td>
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
</table>


## Contact

Tang Mega 138K can meet different needs of customers in various scenarios. For technical support and business cooperation, please contact [support@sipeed.com](support@sipeed.com)

## Frequently Asked Questions (FAQs)

### After powering on the board, only four indicator lights on the dockboard are on, the SOM indicator light is not on

1. Please check if the board’s power has been turned on, press and hold the PWR button (next to the HDMI port) for 2 seconds to turn on the power.

### After powering on the board, the Battery-Indicator light on the dcokboard is flashing

1. This is normal behavior, usually, the last LED (near the 12V DC connector) is flashing;
2. When the board is connected to a 3.7V lithium battery, these LEDs will serve as battery level indicators.

### After pressing and holding the PWR button for 2 seconds, all the indicator lights on the dockboard turn off and then light up in sequence

1. Check your power supply method, this situation means that the power supply is insufficient;
2. Solutions (choose one):
    a. Connect both the board’s **USB-3.0** and **USB-DEBUG** for power supply, i.e., dual 5V USB power supply; 
    b. Connect a 12V DC power supply to the board, if using the USB-C to 12V DC connector from the accessories, a PD power source with 12V output capability is required;
    c. Connect a 3.7V lithium battery to power the board, note that the battery voltage must be ≥3.6V and the continuous discharge capacity must be ≥600mA.

### IDE cannot find the model GW5AST-LV138PG484A

1. The educational version does not support 138K, please switch to the commercial version. The following image shows the educational version (which does not support 138K);
<img src="../assets/questions/no_model_in_IDE.png" width="35%">

2. IDE version is too low to use, update the IDE version ≥ **1.9.9**.

### How to burn the bitstream to FLASH {#burn_flash}

1. Setting the **Programmer** as shown in the figure below:

<img src="./../assets/flash_mode_GAO.png" alt="flash_mode" width=35%>

2. Check the position of the DIP switch; the correct position is shown in the figure below:

<img src="./assets/dip-key_defualt.png" alt="dip-key_defualt" width=35%>

### No Response or Undesirable Pin Phenomenon After Burning

1. First, ensure that the IDE has selected the correct model **GW5AST-LV138PG484AC1/10**; every parameter in the figure below **MUST** be consistent.

<img src="./assets/partno_138K.png" alt="device_choose" width=35%>

2. Then, check your code and the corresponding simulation waveforms to meet the requirements. The GAO tools in GOWIN IDE maybe helpful. For more information, please refer to the GOWIN document [SUG100](https://www.gowinsemi.com/upload/database_doc/1885/document/660bb2366d0b3.pdf)(require login).

### For more questions and solutions, go to [Related Questions](./../Tang-Nano-Doc/questions.md) to view