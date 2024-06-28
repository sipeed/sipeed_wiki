---
title: Tang Mega 60K Dock
keywords: FPGA, Tang, Mega, 60K
update:
  - date: 2024-06-25
    version: v0.1
    author: Serika
    content:
      - 新建文档
---

## 产品概述

TBD

购买链接：[淘宝](https://sipeed.taobao.com)

## 板卡特点

TBD

## 产品外观

TBD

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
			<td style="text-align:left"><a href="https://www.gowinsemi.com.cn/prod_view.aspx?TypeId=74&FId=t3:10:3&Id=188#GW5AT">GW5AT-LV60PG484A</a>
			</td>
			<td style="text-align:left">
				<table>
					<tr>
						<td>逻辑单元(LUT4)</td>
						<td>59904</td>
					</tr>
					<tr>
						<td>寄存器(FF)</td>
						<td>59904</td>
					</tr>
					<tr>
						<td>分布式静态随机存储器S-SRAM(Kbits)</td>
						<td>468</td>
					</tr>
					<tr>
						<td>块状静态随机存储器B-SRAM(Kbits)</td>
						<td>2124</td>
					</tr>
					<tr>
						<td>块状静态随机存储器数目B-SRAM(个)</td>
						<td>118</td>
					</tr>
					<tr>
						<td>乘法器(18x18 Multiplier)</td>
						<td>118</td>
					</tr>
					<tr>
						<td>锁相环(PLLs)</td>
						<td>8</td>
					</tr>
                    <tr>
                        <td>全局时钟</td>
                        <td>16</td>
                    </tr>
                    <tr>
                        <td>高速时钟</td>
                        <td>20</td>
                    </tr>
                    <tr>
                        <td>Transceivers</td>
                        <td>4</td>
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
                        <td>1333</td>
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
						<td>11</td>
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

TBD

## 硬件资料

[板卡规格书](https://dl.sipeed.com/shareURL/TANG/Mega_60K/01_Specification)
[板卡原理图](https://dl.sipeed.com/shareURL/TANG/Mega_60K/02_Schematic)
[PCB BOM](https://dl.sipeed.com/shareURL/TANG/Mega_60K/03_Designator_drawing)
[板卡尺寸图](https://dl.sipeed.com/shareURL/TANG/Mega_60K/04_Mechanical_drawing)
[板卡 3D 模型](https://dl.sipeed.com/shareURL/TANG/Mega_60K/05_3D_file)
[部分芯片手册](https://dl.sipeed.com/shareURL/TANG/Mega_60K/07_Datasheet)

## 上手使用
注意60K目前未被教育版支持，需要下载 V1.9.9.04 或更新版本的商业版IDE使用。  
Lic 可以在高云官网申请，或者使用Sipeed提供的在线Lic服务，在IDE中选择Float Lic，填写以下信息即可：
~~~
ip: 106.55.34.119
port: 10559
~~~
如果上面的IP不能工作, 尝试使用 "gowinlic.sipeed.com" 域名对应的IP.

安装 IDE [点我](https://wiki.sipeed.com/hardware/zh/tang/Tang-Nano-Doc/get_started/install-the-ide.html)


例程代码 [github](https://github.com/sipeed/TangMega-60K-example)

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
        <td>Tang Mega 60K 使用的 FPGA 芯片具体型号是 <b>GW5AT-LV60PG484A</b> <br>在 IDE 中选择封装型号 <b>PBG484A</b></br></td>
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

Tang Mega 60K 可以在多种场景实现客户不同方面的需要，技术支持和商业合作请联系邮箱 [support@sipeed.com](support@sipeed.com)

## 常见问题

### 板子通电后电源灯没亮

TBD
