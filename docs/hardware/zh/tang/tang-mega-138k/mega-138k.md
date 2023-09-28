---
title: Tang Mega 138K Pro Dock
keywords: FPGA, Tang, Mega, 138K
update:
  - date: 2023-08-29
    version: v
    author: wonder
    content:
      - 新建文档
---

## 产品概述

Tang Mega 138K 使用 22nm 制程 GW5AST-LV138FPG676A FPGA 芯片，具有 138240 个查找表单元和近 300 个 DSP 单元。含有八个速度范围在 270Mbps ~ 12.5Gbps 高速收发器，适合用于光纤或者 PCIE 等高速口传递数据。此外，芯片含有硬核 PCIE，在使用 PCIE 的时候消耗更好的资源，并且得到更佳的性能。适用于高速通信、协议转换、高性能计算等场合。

淘宝购买链接：[点我](https://item.taobao.com/item.htm?id=740536508140)

## 板卡特点

- 大容量 LUT
- 大容量 内存
- PCIE3.0 x 4
- SFP+ x 2
- RISCV 硬核

## 产品外观

<img src="./assets/mega_138k_top.png" width="45%">

## 硬件参数

### 核心板参数

<table>
	<thead>
		<tr>
			<th style="text-align:center">项目</th>
			<th style="text-align:center">参数</th>
			<th style="text-align:center">补充</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align:left">FPGA 芯片</td>
			<td style="text-align:left"><a href="http://www.gowinsemi.com.cn/prod_view.aspx?TypeId=10&amp;FId=t3:10:3&amp;Id=167#GW2A">GW5AST-LV138FPG676A</a>
			</td>
			<td style="text-align:left">
				<table>
					<tr>
						<td>逻辑单元(LUT4)</td>
						<td>138240</td>
					</tr>
					<tr>
						<td>寄存器(FF)</td>
						<td>138240</td>
					</tr>
					<tr>
						<td>分布式静态随机存储器S-SRAM(Kbits)</td>
						<td>1080</td>
					</tr>
					<tr>
						<td>块状静态随机存储器B-SRAM(Kbits)</td>
						<td>6120</td>
					</tr>
					<tr>
						<td>块状静态随机存储器数目B-SRAM(个)</td>
						<td>340</td>
					</tr>
					<tr>
						<td>乘法器(18x18 Multiplier)</td>
						<td>298</td>
					</tr>
					<tr>
						<td>锁相环(PLLs)</td>
						<td>12</td>
					</tr>
                    <tr>
                        <td>全局时钟</td>
                        <td>16</td>
                    </tr>
                    <tr>
                        <td>高速时钟</td>
                        <td>24</td>
                    </tr>
                    <tr>
                        <td>Transceivers</td>
                        <td>8</td>
                    </tr>
                    <tr>
                        <td>Transceivers 速率</td>
                        <td>270Mbps-12.5Gbps</td>
                    </tr>
                    <tr>
                        <td>PCIE 硬核</td>
                        <td>1个<br>速度可选 x1, x2, x4, x8 PCIe 2.0</td>
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
                        <td>MIPI D-PHY硬核</td>
                        <td>2.5Gbps（RX），<br>8个数据通道，<br>2个时钟通道</td>
                    </tr>
                    <tr>
                        <td>硬核处理器</td>
                        <td>RiscV AE350_SOC</td>
                    </tr>
                    <tr>
                        <td>ADC</td>
                        <td>2</td>
                    </tr>
					<tr>
						<td>I/O Bank 总数</td>
						<td>10</td>
					</tr>
				</table>
			</td>
		</tr>
		<tr>
			<td style="text-align:left">内存</td>
			<td style="text-align:left">1GB DDR3</td>
			<td style="text-align:left">512MB x 2</td>
		</tr>
		<tr>
			<td style="text-align:left">Flash</td>
			<td style="text-align:left">128Mbits Flash x 2</td>
			<td style="text-align:left">查看 <a href="#burn_flash">烧录到Flash</a></td>
		</tr>
		<tr>
			<td style="text-align:left">调试接口</td>
			<td style="text-align:left">Jtag + Uart</td>
			<td style="text-align:left">JST SH1.0 8Pins 连接器</td>
		</tr>
		<tr>
			<td style="text-align:left">整体封装</td>
			<td style="text-align:left">50mm x 70mm 大小</td>
			<td style="text-align:left">BTB连接器连接核心板和底板</td>
		</tr>
	</tbody>
</table>

### 底板参数

| 项目                | 数量 | 备注                                              |
| :------------------ | ---- | ------------------------------------------------- |
| LED                 | 6    |                                                   |
| WS2812              | 1    |                                                   |
| 按键                | 4    |                                                   |
| PCIE                | 1    |                                                   |
| SFP+                | 2    |                                                   |
| 千兆以太网          | 1    |                                                   |
| DVI RX              | 2    | 与 DVI TX 互相占用                                |
| DVI TX              | 2    | 与 DVI RX 互相占用                                |
| PMOD                | 3    |                                                   |
| ADC                 | 2    |                                                   |
| MIPI CSI            | 2    | 3 LANE MIPI CSI                                   |
| ARGB                | 1    | 与 WS2812 同数据引脚                              |
| DVP Interface       | 1    |                                                   |
| RGB Interface       | 1    | 支持 RGB888 屏幕                                  |
| MIC ARRAY Interface | 1    | 支持连接 Sipeed 6+1 麦克风阵列                    |
| SD 卡槽             | 1    |                                                   |
| EEPROM              | 1    | 可存储必要信息                                    |
| M.2 座子            | 1    | 预留，可以自己写外设驱动                          |
| PWM 风扇接口        | 1    |                                                   |
| 扬声器接口          | 1    |                                                   |
| 3.5mm 耳机接口      | 1    |                                                   |
| 自定义 USB          | 1    | 无法给板子供电                                    |
| MS5351              | 2    | 为 Serdes 提供 RefClk；通过底板上的串口来控制输出 |
| USB JTAG&UART       | 1    | 支持烧录 FPGA，并且提供串口功能                   |
| 40P 排针            | 1    |                                                   |
| 电源开关            | 1    |                                                   |
| 12V DC              | 1    |                                                   |

## 硬件资料

[板卡规格书](https://dl.sipeed.com/shareURL/TANG/Mega_138K_Pro/1_Datasheet)
[板卡原理图](https://dl.sipeed.com/shareURL/TANG/Mega_138K_Pro/02_Schematic)
[PCB BOM](https://dl.sipeed.com/shareURL/TANG/Mega_138K_Pro/03_Designator_drawing)
[板卡尺寸图](https://dl.sipeed.com/shareURL/TANG/Mega_138K_Pro/04_Mechanical_drawing)
[板卡 3D 模型](https://dl.sipeed.com/shareURL/TANG/Mega_138K_Pro/05_3D_file)
[部分芯片手册](https://dl.sipeed.com/shareURL/TANG/Mega_138K_Pro/07_Datasheet)

## 上手使用

安装 IDE -> 编写代码 -> 烧录进板子

<!-- - 安装 IDE [点我](https://wiki.sipeed.com/hardware/zh/tang/Tang-Nano-Doc/get_started/install-the-ide.html)
- 开箱说明 [点我](https://wiki.sipeed.com/hardware/zh/tang/tang-nano-20k/example/unbox.html)
- 点灯上手指南 [点我](https://wiki.sipeed.com/hardware/zh/tang/tang-nano-20k/example/led.html) -->

例程代码 [github](https://github.com/sipeed/TangMega-138KPro-example)

### 其他学习资源

- 在线免费教程：[Verilog 教程](https://www.runoob.com/w3cnote/verilog-tutorial.html)（学习Verilog）
- 在线免费 FPGA 教程：[Verilog](https://www.asic-world.com/verilog/index.html) （英文网站）
- Verilog 刷题网站：[HDLBits](https://hdlbits.01xz.net/wiki/Main_Page)（英文网站）
- 在线高云半导体可参考视频教程：[点击这里](http://www.gowinsemi.com.cn/video_complex.aspx?FId=n15:15:26)

## 交流方式

- **交流论坛: [maixhub.com/discussion](https://maixhub.com/discussion)**
- **QQ 交流群：[834585530](https://jq.qq.com/?_wv=1027&k=wBb8XUan)**
- 直接本页下方留言
- 商业邮箱 : [support@sipeed.com](support@sipeed.com)

## 注意事项

<table>
    <tr>
        <th>事项</th>
        <th>注意事项</th>
    </tr>
    <tr>
        <td>芯片型号</td>
        <td>Tang Mega 138K Pro 使用的 FPGA 芯片具体型号是 GW5AST-LV138FPG676A ，在 IDE 中选择封装型号 FCPBG676A</td>
    </tr>
    <tr>
        <td>静电</td>
        <td>请避免静电打到 PCBA 上；接触 PCBA 之前请把手的静电释放掉</td>
    </tr>
    <tr>
        <td>容忍电压</td>
        <td> 使用 GPIO 排针引脚进行外部通信时，要确保 IO 电压是 3.3V，过高的电压会永久损坏 PCBA </td>
    </tr>
    <tr>
        <td>FPC 座子</td>
        <td>在连接 FPC 软排线的时候，请确保排线无偏侈地完整地插入到排线中</td>
    </tr>
    <tr>
        <td>PCIE 金手指</td>
        <td>在测试 PCIE 金手指时候，确保是主机端与板卡都处于关机或者未通电的状态，否则可能会因为插入过程中的易位导致金手指短路。</td>
    </tr>
    <tr>
        <td>插拔</td>
        <td>请完全断电后才进行插拔操作</td>
    </tr>
    <tr>
        <td>避免短路</td>
        <td>请在上电过程中，避免任何液体和金属触碰到 PCBA 上的元件的焊盘，否则会导致路，烧毁 PCBA</td>
    </tr>
</table>

## 联系

Tang Mega 138K 可以在多种场景实现客户不同方面的需要，技术支持和商业合作请联系邮箱 [support@sipeed.com](support@sipeed.com)

## 常见问题

### 板子通电后电源灯没亮

1. 请检查是否开启了板子的电源开关。
2. 检查自己的供电方式。