# Tang Primer 25K

## 概述

Tang Primer 25K 是基于 [GW5A-LV25MG121](http://www.gowinsemi.com.cn/prod_view.aspx?TypeId=74&FId=t3:10:3&Id=188) 所设计的一款极小封装的核心板（23x18mm），并配套全引脚引出(除MIPI高速脚外)的25K Dock底板。

极小的核心板尺寸可以应用于任何体积受限的场景。  
简洁的底板可以连接USB手柄，插接40Pin SDRAM模块，3个PMOD接口可以连接HDMI显示器，PS2手柄组成典型的RetroGame主机形态。
也可以搭配Sipeed出的系列PMOD模块产品，作为FPGA大学教学使用。


<div>
    <img src="./assets/25k_45.jpg" width=45%>
    <img src="./assets/25k_dock_45.jpg" width=45%>
</div>

购买链接：[淘宝](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-24984936573.29.19b22db2a329yr&id=746293292946)




## 核心板概览
<div>
    <img src="./assets/25k_top.jpg" width=45%>
    <img src="./assets/25k_bot.jpg" width=45%>
</div>



## 基础参数

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
			<td style="text-align:left"><a href="http://www.gowinsemi.com.cn/prod_view.aspx?TypeId=74&FId=t3:10:3&Id=188">GW5A-LV25MG121</a>
			</td>
			<td style="text-align:left">
				<table>
					<tr>
						<td>逻辑单元(LUT4)</td>
						<td>23040</td>
					</tr>
					<tr>
						<td>寄存器(FF)</td>
						<td>23040</td>
					</tr>
					<tr>
						<td>分布式静态随机存储器S-SRAM(bits)</td>
						<td>180K</td>
					</tr>
					<tr>
						<td>块状静态随机存储器B-SRAM(bits)</td>
						<td>1008K</td>
					</tr>
					<tr>
						<td>块状静态随机存储器数目B-SRAM(个)</td>
						<td>56</td>
					</tr>
					<tr>
						<td>乘法器(18x18 Multiplier)</td>
						<td>28</td>
					</tr>
					<tr>
						<td>锁相环(PLLs)</td>
						<td>6</td>
					</tr>
					<tr>
						<td>I/O Bank 总数</td>
						<td>8</td>
					</tr>
				</table>
			</td>
		</tr>
		<tr>
			<td style="text-align:left">Flash</td>
			<td style="text-align:left">64Mbits NOR Flash</td>
			<td style="text-align:left">查看 <a href="#burn_flash">烧录到Flash</a></td>
		</tr>
		<tr>
			<td style="text-align:left">整体封装</td>
			<td style="text-align:left">2x60P BTB 核心板</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left">普通IO</td>
			<td style="text-align:left"> 75</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left"> MIPI IO </td>
			<td style="text-align:left"> 4lane Data</td>
			<td style="text-align:left"></td>
		</tr>
	</tbody>
</table>

## Dock 底板产品图


<div>
<img src="./assets/25k_dock_top.jpg"  width=45%>
<img src="./assets/25k_dock_bot.jpg"  width=45%>
</div>


## 板卡参数

<table>
	<thead>
		<tr>
			<th style="text-align:center">项目</th>
			<th style="text-align:center">参数</th>
			<th style="text-align:center">备注</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align:left">调试器</td>
			<td style="text-align:left">板载高速调试器，支持JTAG+UART，使用USB-C口烧录</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left">USB-A</td>
			<td style="text-align:left">一个，可作为USB1.1 Host接游戏手柄等HID设备</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left"> IO插针 </td>
			<td style="text-align:left"> 一个2x20Pin 2.54插针</td>
			<td style="text-align:left">支持SDRAM模块</td>
		</tr>
		<tr>
			<td style="text-align:left"> PMOD </td>
			<td style="text-align:left"> 3个</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left">按键</td>
			<td style="text-align:left">2个</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left">尺寸</td>
			<td style="text-align:left">64x40mm</td>
			<td style="text-align:left"></td>
		</tr>
	</tbody>
</table>

## 硬件资料

规格书、原理图、尺寸图等均可在这里找到：[点击这里](https://dl.sipeed.com/shareURL/TANG/Primer_25K)

- [板卡规格书](https://dl.sipeed.com/shareURL/TANG/Primer_25K/01_Specification)
- [板卡原理图](https://dl.sipeed.com/shareURL/TANG/Primer_25K/02_Schematic)
- [板卡点位图](https://dl.sipeed.com/shareURL/TANG/Primer_25K/03_Designator_drawing)
- [板卡尺寸图](https://dl.sipeed.com/shareURL/TANG/Primer_25K/04_Mechanical_drawing)
- [3D 模型文件](https://dl.sipeed.com/shareURL/TANG/Primer_25K/05_3D_file)
- [核心板封装](https://dl.sipeed.com/shareURL/TANG/Primer_25K/06_PCB_Lib) 
- [芯片部分资料](https://dl.sipeed.com/shareURL/TANG/Primer_25K/07_Datasheet)
- [走线长度表](https://dl.sipeed.com/shareURL/TANG/Primer_25K/08_Pin_Length_table)


## 上手简明

`准备开发环境` -> `学习相关语法` -> `查看开箱指南` -> `基础代码编写` -> `查看官方文档`

1. 安装 IDE ：[点击这里](./../Tang-Nano-Doc/get_started/install-the-ide.md)

2. 查看 [上手指南](https://wiki.sipeed.com/hardware/zh/tang/tang-primer-20k/start.html) 来避免一些问题，并且从那里面可以开始进行代码实战。

3. 如果进行完上面的点灯操作后后感觉有压力，可以自己查漏补缺：
   可以在下面的这些网站学习 Verilog:
	+ 在线免费教程：[Verilog 教程](https://www.runoob.com/w3cnote/verilog-tutorial.html)（学习Verilog）
	+ 在线免费 FPGA 教程：[Verilog](https://www.asic-world.com/verilog/index.html) （英文网站）
	+ Verilog 刷题网站：[HDLBits](https://hdlbits.01xz.net/wiki/Main_Page)（英文网站）
	+ 在线高云半导体可参考视频教程：[点击这里](http://www.gowinsemi.com.cn/video_complex.aspx?FId=n15:15:26)

   对 IDE 使用有疑问的话，可以查看官方的一些文档来熟悉相关内容
   - [SUG100-2.6_Gowin云源软件用户指南.pdf](http://cdn.gowinsemi.com.cn/SUG100-2.6_Gowin%E4%BA%91%E6%BA%90%E8%BD%AF%E4%BB%B6%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)
   - [SUG949-1.1_Gowin_HDL编码风格用户指南.pdf](http://cdn.gowinsemi.com.cn/SUG949-1.1_Gowin_HDL%E7%BC%96%E7%A0%81%E9%A3%8E%E6%A0%BC%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)
   - <a href="http://cdn.gowinsemi.com.cn/UG286-1.9.1_Gowin%E6%97%B6%E9%92%9F%E8%B5%84%E6%BA%90(Clock)%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf">UG286-1.9.1_Gowin时钟资源(Clock)用户指南.pdf</a>
   - [SUG940-1.3_Gowin设计时序约束用户指南.pdf](http://cdn.gowinsemi.com.cn/SUG940-1.3_Gowin%E8%AE%BE%E8%AE%A1%E6%97%B6%E5%BA%8F%E7%BA%A6%E6%9D%9F%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)
   - [SUG502-1.3_Gowin_Programmer用户指南.pdf](http://cdn.gowinsemi.com.cn/SUG502-1.3_Gowin_Programmer%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)
   - [SUG114-2.5_Gowin在线逻辑分析仪用户指南.pdf](http://cdn.gowinsemi.com.cn/SUG114-2.5_Gowin%E5%9C%A8%E7%BA%BF%E9%80%BB%E8%BE%91%E5%88%86%E6%9E%90%E4%BB%AA%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)

   上面的所有文档都已经打包进了下载站[点我跳转](https://dl.sipeed.com/shareURL/TANG/Primer_20K/07_Chip_manual/CN/%E9%80%9A%E7%94%A8%E6%8C%87%E5%BC%95)，需要的话可以点击压缩包全都下载下来。

## 例程汇总
注意25K需要使用 V1.9.9Beta-4 或更新的IDE版本。
http://www.gowinsemi.com.cn/faq.aspx

### 公开例程
github 链接： https://github.com/sipeed/TangPrimer-25K-example


## 交流方式

- **交流论坛: [maixhub.com](maixhub.com/discussion)**
- **QQ 交流群：[834585530](https://jq.qq.com/?_wv=1027&k=wBb8XUan)**
- 直接本页下方留言
- 商业邮箱 : [support@sipeed.com](support@sipeed.com)



## 相关问题

### 如何下载到外部 FLASH {#burn_flash}

进行如下选项设置：

<img src="./assets/flash_mode.png" alt="flash_mode" width=75%>

### 烧录后没反应或者引脚现象不对

首先确定选择了正确的型号，下图中的每一个参数都要求一致

<img src="./assets/partno.jpg" alt="device_choose" width=75%>

然后检查自己的代码和对应的仿真波形是否满足要求

### 更多问题及其解决办法前往[相关问题](./../Tang-Nano-Doc/questions.md)查看
