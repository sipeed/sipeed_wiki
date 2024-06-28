---
title: Tang Mega 138K Dock
keywords: FPGA, Tang, Mega, 138K
update:
  - date: 2024-06-25
    version: v0.1
    author: Serika
    content:
      - 新建文档
---


## 产品概述

**Tang Mega 138K** 使用 22nm 制程 **GW5AST-LV138P484A** FPGA 芯片，具有 138240 个查找表单元和近 300 个 DSP 单元。含有八个速度范围在 270Mbps ~ 6.6Gbps 高速收发器，适合用于 PCIE 等高速口传递数据。此外，芯片含有硬核 PCIE，在使用 PCIE 的时候消耗更好的资源，并且得到更佳的性能。适用于高速通信、协议转换、高性能计算等场合。
相比138K Pro Dock，138K Dock具有更小的体积和更低的价格，并用USB3.0代替了SFP收发器。这不仅有效的降低了高速通讯的成本，还带来了更好的通用性。

淘宝购买链接：[点我](https://item.taobao.com/item.htm?id=740536508140)

## 板卡特点

- 大容量 LUT
- 大容量 内存
- PCIE2.0 x 4
- USB3.0 x1
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
			<td style="text-align:left"><a href="https://www.gowinsemi.com.cn/prod_view.aspx?TypeId=74&FId=t3:10:3&Id=188#GW5AST">GW5AST-LV138PG484A</a>
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
                        <td>4</td>
                    </tr>
                    <tr>
                        <td>Transceivers 速率</td>
                        <td>270Mbps-6.6Gbps</td>
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
                        <td>1333</td>
                    </tr>
                        <td>硬核处理器</td>
                        <td>RiscV AE350_SOC</td>
                    </tr>
                    <tr>
                        <td>ADC</td>
                        <td>2</td>
                    </tr>
					<tr>
						<td>IO Bank 总数</td>
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
			<td style="text-align:left">128Mbits Flash x 1</td>
			<td style="text-align:left">查看 <a href="#burn_flash">烧录到Flash</a></td>
		</tr>
		<tr>
			<td style="text-align:left">调试接口</td>
			<td style="text-align:left">Jtag + Uart</td>
			<td style="text-align:left">JST SH1.0 8Pins 连接器</td>
		</tr>
		<tr>
			<td style="text-align:left">整体封装</td>
			<td style="text-align:left">35mm x 45mm 大小</td>
			<td style="text-align:left">BTB连接器连接核心板和底板</td>
		</tr>
	</tbody>
</table>

### 底板参数

| 项目                 | 数量 | 备注                                              |
| :------------------  | ---- | ------------------------------------------------- |
| LED                  | 4+8  | 4个电量指示灯+8个PMOD外接                          |
| WS2812               | 1    | 与 aRGB 灯带连接器同数据引脚                       |
| Buttons              | 3+1  | 3个用户按键+1个reconfig按键                        |
| PCIe                 | 1    | 4-lane @ 5Gbps，CH569 16bit HSPI                  |
| USB3                 | 2    | SuperSpeed @ 5Gbps                                |
| GbE                  | 1    | 千兆以太网                                        |
| DVI RX               | 1    | 与 DVI TX 互相占用                                |
| DVI TX               | 1    | 与 DVI RX 互相占用                                |
| PMOD                 | 2    | 与上边的40P排针和DVP复用                          |
| ADC                  | 2    | 2个差分输入通道                                   |
| aRGB CONN.           | 1    | 与 WS2812 同数据引脚                              |
| DVP Interface        | 1    | 与上侧的40P排针和PMOD复用                         |
| RGB Interface        | 1    | 支持 RGB888 屏幕                                  |
| MIC ARRAY Interface  | 1    | 支持连接 Sipeed 6+1 麦克风阵列                    |
| SD Slot              | 1    | 1-bit SDIO/MMC 或SPI模式                          |
| BATT CONN.           | 1    | 支持3.7V锂电池，自带充放电管理                     |
| PWM FAN CONN.        | 1    | 支持5V PWM风扇，支持测速                           |
| Speaker CONN.        | 2    | 支持两个3W扬声器                                   |
| 3.5mm Headphone CONN.| 1    | 立体声输出，无Mic                                  |
| MS5351               | 1    | 为 Serdes 提供 RefClk；通过底板上的串口来控制输出  |
| USB JTAG & UART      | 1    | 支持烧录 FPGA，并且提供串口功能                    |
| 40P 排针             | 2    | 上侧的40P排针与PMOD和DVP复用                       |
| 电源开关             | 1    | 长按2s切换开关机状态                               |
| 12V DC               | 1    | 规格DC5521                                        |

## 硬件资料

[板卡规格书](https://dl.sipeed.com/shareURL/TANG/Mega_138K/01_Specification)
[板卡原理图](https://dl.sipeed.com/shareURL/TANG/Mega_138K/02_Schematic)
[PCB BOM](https://dl.sipeed.com/shareURL/TANG/Mega_138K/03_Designator_drawing)
[板卡尺寸图](https://dl.sipeed.com/shareURL/TANG/Mega_138K/04_Mechanical_drawing)
[板卡 3D 模型](https://dl.sipeed.com/shareURL/TANG/Mega_138K/05_3D_file)
[部分芯片手册](https://dl.sipeed.com/shareURL/TANG/Mega_138K/07_Datasheet)

## 上手使用
注意138K目前未被教育版支持，需要下载 V1.9.9 或更新版本的商业版IDE使用。  
Lic 可以在高云官网申请，或者使用Sipeed提供的在线Lic服务，在IDE中选择Float Lic，填写以下信息即可：
~~~
ip: 106.55.34.119
port: 10559
~~~
如果上面的IP不能工作, 尝试使用 "gowinlic.sipeed.com" 域名对应的IP.

安装 IDE [点我](https://wiki.sipeed.com/hardware/zh/tang/Tang-Nano-Doc/get_started/install-the-ide.html)


例程代码 [github](https://github.com/sipeed/TangMega-138K-example)

### 其他学习资源

- 在线免费教程：[Verilog 教程](https://www.runoob.com/w3cnote/verilog-tutorial.html)（学习Verilog）
- 在线免费 FPGA 教程：[Verilog](https://www.asic-world.com/verilog/index.html) （英文网站）
- Verilog 刷题网站：[HDLBits](https://hdlbits.01xz.net/wiki/Main_Page)（英文网站）
- 在线高云半导体可参考视频教程：[点击这里](http://www.gowinsemi.com.cn/video_complex.aspx?FId=n15:15:26)

## 交流方式

- **交流论坛: [maixhub.com/discussion](https://maixhub.com/discussion)**
- **QQ 交流群：[834585530](https://jq.qq.com/?_wv=1027&k=wBb8XUan)**
- 直接本页下方留言
- 前往**[Github项目主页](https://github.com/sipeed/TangMega-138K-example)**提交issue
- 商业邮箱 : [support@sipeed.com](support@sipeed.com)

## 注意事项

<table>
    <tr>
        <th>事项</th>
        <th>注意事项</th>
    </tr>
    <tr>
        <td>芯片型号</td>
        <td>Tang Mega 138K 使用的 FPGA 芯片具体型号是 <b>GW5AST-LV138PG484A</b>  <br>在 IDE 中选择封装型号 <b>PBG484A</b></br></td>
    </tr>
    <tr>
        <td>静电</td>
        <td>请避免静电打到 PCBA 上；接触 PCBA 之前请把手的静电释放掉</td>
    </tr>
    <tr>
        <td>容忍电压</td>
        <td> 使用 GPIO 排针引脚进行外部通信时，要确保 IO 电压是 <b>3.3V</b>，过高的电压会永久损坏 PCBA </td>
    </tr>
    <tr>
        <td>FPC 座子</td>
        <td>在连接 FPC 软排线的时候，请确保排线无偏侈地完整地插入到排线中</td>
    </tr>
    <tr>
        <td>PCIe 金手指</td>
        <td>在测试 PCIe 金手指时候，确保是主机端与板卡都处于关机或者未通电的状态，否则可能会因为插入过程中的易位导致金手指短路。</td>
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

### 板子通电后底板只亮了四个指示灯，SOM的指示灯没亮

1. 请检查是否开启了板子的电源，**PWR按键**（HDMI接口旁边）长按2S开启电源；

### 板子通电后，底板Battery-Indicator指示灯在闪烁

1. 正常现象，通常是最后一颗LED（靠近12V DC连接器）在闪烁；
2. 当板子连接3.7V锂电池时，这些LED将作为电池电量指示灯。

### 长按PWR按钮 2s 后，底板指示灯全部熄灭又依次亮起

1. 检查自己的供电方式，出现这种情况意味着供电能力不足；
2. 解决方案（任选一种）：
    a. 同时连接板子的**USB-3.0**和**USB-DEBUG**进行供电，即双5V USB电源供电；
    b. 连接12V DC电源对板子进行供电，如使用配件中的USB-C转12V DC连接器，则需要连接有12V输出能力的PD电源；
    c. 连接3.7V锂电池对板子进行供电，注意电池电压必须≥3.6V且连续放电能力≥600mA。

### IDE找不到型号GW5AST-LV138PG484A

1. 教育版不支持138K，请更换商业版。如下图所示即为教育版（不支持138K）；
<img src="../assets/questions/no_model_in_IDE.png" width="35%">

2. IDE版本过老，必须更新IDE ≥ 1.9.9。

### 如何下载到外部 FLASH {#burn_flash}

1. 进行如下选项设置：

<img src="./assets/flash_mode.png" alt="flash_mode" width=35%>

2. 检查拨码开关的位置，正确的位置如下图所示：

<img src="./assets/dip-key_defualt.png" alt="dip-key_defualt" width=35%>

### 烧录后没反应或者引脚现象不对

1. 首先确定IDE选择了正确的型号 **GW5AST-LV138PG484AC1/10**，下图中的每一个参数都要求一致；

<img src="./assets/partno_138K.png" alt="device_choose" width=35%>

2. 然后检查自己的代码和对应的仿真波形是否满足要求，使用云源软件（GOWIN IDE）的GAO工具可以进行片上仿真。更多详情请参考GOWIN文档[SUG100](https://cdn.gowinsemi.com.cn/SUG100-4.0_Gowin%E4%BA%91%E6%BA%90%E8%BD%AF%E4%BB%B6%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)中关于GAO工具的描述。

### 更多问题及其解决办法前往[相关问题](./../Tang-Nano-Doc/questions.md)查看