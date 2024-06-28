---
title: Tang Primer 15K Dock
keywords: FPGA, Tang, Primer, 15K
update:
  - date: 2024-06-25
    version: v0.1
    author: Serika
    content:
      - 新建文档
---
## 概述

TBD

购买链接：[淘宝](https://sipeed.taobao.com)




## 核心板概览

TBD


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
			<td style="text-align:left"><a href="https://www.gowinsemi.com.cn/prod_view.aspx?TypeId=74&FId=t3:10:3&Id=188#G15K">GW5ART-15MG132P</a>
			</td>
			<td style="text-align:left">
				<table>
					<tr>
						<td>逻辑单元(LUT4)</td>
						<td>15120</td>
					</tr>
					<tr>
						<td>寄存器(FF)</td>
						<td>15120</td>
					</tr>
					<tr>
						<td>分布式静态随机存储器S-SRAM(bits)</td>
						<td>118125</td>
					</tr>
					<tr>
						<td>块状静态随机存储器B-SRAM(bits)</td>
						<td>630</td>
					</tr>
					<tr>
						<td>块状静态随机存储器数目B-SRAM(个)</td>
						<td>35</td>
					</tr>
					<tr>
						<td>乘法器(18x18 Multiplier)</td>
						<td>28+12</td>
					</tr>
					<tr>
						<td>锁相环(PLLs)</td>
						<td>2</td>
					</tr>
					    <td>全局时钟</td>
                        <td>16</td>
                    </tr>
                    <tr>
                        <td>高速时钟</td>
                        <td>2</td>
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
					    <td>MIPI D-PHY硬核</td>
                        <td>2.5Gbps（RX/TX），<br>4个数据通道，<br>1个时钟通道</td>
                    </tr>
                    <tr>
                        <td>MIPI C-PHY硬核</td>
                        <td>2.5Gbps（RX/TX），<br>=5.75Gbps,RX/TX<br>3个三线数据通道</td>
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
						<td>GPIO Bank 总数</td>
						<td>4</td>
				</table>
			</td>
		</tr>
		<tr>
			<td style="text-align:left">Flash</td>
			<td style="text-align:left">64Mb</td>
			<td style="text-align:left">查看 <a href="#burn_flash">烧录到Flash</a></td>
		</tr>
		<tr>
			<td style="text-align:left">整体封装</td>
			<td style="text-align:left">TBD</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left">普通IO</td>
			<td style="text-align:left"> 53</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left"> MIPI IO </td>
			<td style="text-align:left"> 10</td>
			<td style="text-align:left"></td>
		</tr>
	</tbody>
</table>

## Dock 底板产品图


TBD


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
			<td style="text-align:left">TBD</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left">USB-A</td>
			<td style="text-align:left">TBD</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left"> IO插针 </td>
			<td style="text-align:left"> TBD</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left"> PMOD </td>
			<td style="text-align:left"> TBD</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left">按键</td>
			<td style="text-align:left">TBD</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left">尺寸</td>
			<td style="text-align:left">TBD</td>
			<td style="text-align:left"></td>
		</tr>
	</tbody>
</table>

## 硬件资料

规格书、原理图、尺寸图等均可在这里找到：[点击这里](https://dl.sipeed.com/shareURL/TANG/Primer_15K)

- [板卡规格书](https://dl.sipeed.com/shareURL/TANG/Primer_15K/01_Specification)
- [板卡原理图](https://dl.sipeed.com/shareURL/TANG/Primer_15K/02_Schematic)
- [板卡点位图](https://dl.sipeed.com/shareURL/TANG/Primer_15K/03_Designator_drawing)
- [板卡尺寸图](https://dl.sipeed.com/shareURL/TANG/Primer_15K/04_Mechanical_drawing)
- [3D 模型文件](https://dl.sipeed.com/shareURL/TANG/Primer_15K/05_3D_file)
- [核心板封装](https://dl.sipeed.com/shareURL/TANG/Primer_15K/06_PCB_Lib) 
- [芯片部分资料](https://dl.sipeed.com/shareURL/TANG/Primer_15K/07_Datasheet)
- [走线长度表](https://dl.sipeed.com/shareURL/TANG/Primer_15K/08_Pin_Length_table)


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
注意15K需要使用 V1.9.9.04 或更新的IDE版本。
http://www.gowinsemi.com.cn/faq.aspx

### 公开例程
github 链接： https://github.com/sipeed/TangPrimer-15K-example


## 交流方式

- **交流论坛: [maixhub.com](maixhub.com/discussion)**
- **QQ 交流群：[834585530](https://jq.qq.com/?_wv=1027&k=wBb8XUan)**
- 直接本页下方留言
- 商业邮箱 : [support@sipeed.com](support@sipeed.com)



## 相关问题

### TBD

TBD


