# Tang Primer 20K

> 编辑于2022.08.05

## 前言

Tang Primer 20K 是基于 [GW2A-V18PG256C8IC8I7](http://www.gowinsemi.com.cn/prod_view.aspx?TypeId=10&amp;FId=t3:10:3&amp;Id=167#GW2A) 所设计的一款 dd3 sodimm 封装的核心板，额外准备了两个底板，分别为 Dock 底板和 Lite 底板。作为 Sipeed 所发售的第六款 FPGA 产品，Tang Primer 20K 一直广受关注。

**注意： Dock 底板预计十月份发售**

得益于 GW2A 丰富的资源，Tang Primer 20K 可以满足多种项目需求；例如当下最火的“IC设计”，可以使用高云所提供的 [Gowin_EMPU_M1](http://www.gowinsemi.com.cn/prodshow_view.aspx?TypeId=71&Id=178&FId=t31:71:31#IP)、[PicoRV32](http://www.gowinsemi.com.cn/prodshow_view.aspx?TypeId=70&Id=175&FId=t31:70:31#IP)两款软核来体验一下 mcu 软核，或者也可以用来验证自己所设计的软核。

两款适用的 Dock 底板与 Lite 底板资源不同。前者所搭载有例如 dvp 摄像头、rgb屏幕和百兆以太网接口等多种外设适合用户快速验证自己所写的代码，也可以尝试使用高云所提供的[USB软核](http://www.gowinsemi.com.cn/enrollment_view.aspx?TypeId=67&Id=858&FId=t27:67:27#IP)，来自行开发一下有趣的东西；后者引出上百个自定义 IO 方便用户自行设计相关拓展模块。

这次以底板 + 核心板的设计，满足大多数用户不同的基础使用需求。

## 核心板

### 外观

<body>
<div class="imbox">
    <img src="./assets/20k_front.png" width=350>
    <img src="./assets/20k_back.png" width=350>
<style>
.imbox{
     display:flex;
     flex-direction: row;
     }
</style>
</div>
</body>

### 相关参数

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
			<td style="text-align:left">主控</td>
			<td style="text-align:left"><a href="http://www.gowinsemi.com.cn/prod_view.aspx?TypeId=10&amp;FId=t3:10:3&amp;Id=167#GW2A">GW2A-V18PG256C8IC8I7</a>
			</td>
			<td style="text-align:left">
				<table>
					<tr>
						<td>逻辑单元(LUT4)</td>
						<td>20736</td>
					</tr>
					<tr>
						<td>寄存器(FF)</td>
						<td>15552</td>
					</tr>
					<tr>
						<td>分布式静态随机存储器S-SRAM(bits)</td>
						<td>41472</td>
					</tr>
					<tr>
						<td>块状静态随机存储器B-SRAM(bits)</td>
						<td>828K</td>
					</tr>
					<tr>
						<td>块状静态随机存储器数目B-SRAM(个)</td>
						<td>46</td>
					</tr>
					<tr>
						<td>乘法器(18x18 Multiplier)</td>
						<td>48</td>
					</tr>
					<tr>
						<td>锁相环(PLLs)</td>
						<td>4</td>
					</tr>
					<tr>
						<td>I/O Bank 总数</td>
						<td>8</td>
					</tr>
				</table>
			</td>
		</tr>
		<tr>
			<td style="text-align:left">内存</td>
			<td style="text-align:left">128M DDR3</td>
			<td style="text-align:left">13Row x 10Col x 8banks x 16bits</td>
		</tr>
		<tr>
			<td style="text-align:left">Flash</td>
			<td style="text-align:left">32Mbits NOR Flash</td>
			<td style="text-align:left">W25Q32JVS</td>
		</tr>
		<tr>
			<td style="text-align:left">调试接口</td>
			<td style="text-align:left">Jtag + Uart</td>
			<td style="text-align:left">JST SH1.0 8Pins 连接器</td>
		</tr>
		<tr>
			<td style="text-align:left">SD 卡槽</td>
			<td style="text-align:left">一个</td>
			<td style="text-align:left">推拉式</td>
		</tr>
		<tr>
			<td style="text-align:left">显示接口</td>
			<td style="text-align:left">8Pins spi lcd 连接器</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left">整体封装</td>
			<td style="text-align:left">204P DDR3 Sodimm 金手指</td>
			<td style="text-align:left"></td>
		</tr>
		<tr>
			<td style="text-align:left">可用 IO</td>
			<td style="text-align:left">一共 117 个</td>
			<td style="text-align:left"></td>
		</tr>
	</tbody>
</table>

## 底板参数对比

<table>
	<thead>
		<tr>
			<th rowspan="2" colspan="2">项目</th>
			<th colspan="2">Dock</th>
			<th colspan="2">Lite</th>
		</tr>
		<tr>
			<th>数量</th>
			<th>补充说明</th>
			<th>数量</th>
			<th>补充说明</th>
		</tr>
	</thead>
	<body>
		<tr>
			<td colspan="2">RGB 接口</td>
			<td>1</td>
			<td>RGB565 40P FPC 连接器</td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">DVP 接口</td>
			<td>1</td>
			<td>24P FPC 连接器</td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">麦克风阵列接口</td>
			<td>1</td>
			<td>10P FPC 连接器</td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">触摸接口</td>
			<td>1</td>
			<td>4P FPC 连接器</td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">PMOD 接口</td>
			<td>4</td>
			<td></td>
			<td>4</td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">3.5mm 耳机接口</td>
			<td>1</td>
			<td>使用 LPA4809MSF 驱动</td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">拨码开关</td>
			<td>1</td>
			<td>5P 拨码开关</td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">滑动开关</td>
			<td>1</td>
			<td>切换板载 USB 功能</td>
			<td>2</td>
			<td>用户自定义功能</td>
		</tr>
		<tr>
			<td style="white-space:nowrap" rowspan="2">Type-C 接口</td>
			<td style="white-space:nowrap">USB-JTAG&UART</td>
			<td>1</td>
			<td>板载 BL702 芯片用来<br>下载比特流并提供串口功能</td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td>自定义 USB</td>
			<td>1</td>
			<td>USB3317 芯片与滑动开关<br>来自定义该 USB 接口功能</td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">无线天线</td>
			<td>1</td>
			<td>使用 BL702 芯片的无线功能</td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">按键</td>
			<td>6</td>
			<td>一个用来烧录 BL702,<br>剩下五个用户自定义功能</td>
			<td>2</td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">LED</td>
			<td>6</td>
			<td></td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">HDMI 接口</td>
			<td>1</td>
			<td></td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">以太网接口</td>
			<td>1</td>
			<td>TL8201F 芯片实现以太网功能</td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td colspan="2">RGB LED</td>
			<td>1</td>
			<td>WS2812 灯珠</td>
			<td></td>
			<td></td>
		</tr>
	</body>
</table>

## **适用人群**

| 用法     | FPGA                             | MCU                                | FPGA+MCU                     |
| :---- | :---------- | :------------- | :----------------- |
| 语言     | Verilog HDL/Verilog         | C/C++               | Verilog HDL/Verilog ，  C/C++                |
| 简介     | 上板验证用户HDL | 用户将软核的比特流文件下载到芯片后可将<br>Primer 20K当做普通的 MCU 来使用  | 烧入软核后可以进行异构开发 |
| 适用人群 | 初学者，FPGA 开发者        | RISC-V 开发者，Cortex-M 开发者          | 资深软硬件工程师             |

## **上手指引**

1. 检查板子是否正常

1. 下载我们打包好的用户指南文档：[下载站](https://dl.sipeed.com/shareURL/TANG/Primer_20K/07_Chip_manual/CN/%E9%80%9A%E7%94%A8%E6%8C%87%E5%BC%95) （下文提到的所有pdf文件都在这里）

2. 安装 IDE 并申请 License：[点击这里](https://wiki.sipeed.com/soft/Tang/zh/Tang-Nano-Doc/get_started/install-the-ide.html)

3. 阅读第一步下载的文件里面的：[SUG100-2.6_Gowin云源软件用户指南.pdf]((http://cdn.gowinsemi.com.cn/SUG100-2.6_Gowin%E4%BA%91%E6%BA%90%E8%BD%AF%E4%BB%B6%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf))

4. 阅读这个[教程](./examples/LED.md)完成点灯仿真实验。

    建议新手在完成这一步之后，自己重新独立新建项目、编写代码，完成这个实验，并且按自己的想法修改点灯程序，增强对FPGA和硬件描述语言的理解。
    建议在这个过程阅读以下内容，阅读完才进入下一步：
    - Verilog代码规范（自行搜索，从初学就培养良好的代码规范是非常必要的）

下面的这些内容对于初学者来说是非常有用的，对未来深入学习 FPGA 很有帮助。

   - [SUG100-2.6_Gowin云源软件用户指南.pdf](http://cdn.gowinsemi.com.cn/SUG100-2.6_Gowin%E4%BA%91%E6%BA%90%E8%BD%AF%E4%BB%B6%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)
   - [SUG949-1.1_Gowin_HDL编码风格用户指南.pdf](http://cdn.gowinsemi.com.cn/SUG949-1.1_Gowin_HDL%E7%BC%96%E7%A0%81%E9%A3%8E%E6%A0%BC%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)
   - <a href="http://cdn.gowinsemi.com.cn/UG286-1.9.1_Gowin%E6%97%B6%E9%92%9F%E8%B5%84%E6%BA%90(Clock)%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf">UG286-1.9.1_Gowin时钟资源(Clock)用户指南.pdf</a>
   - [SUG940-1.3_Gowin设计时序约束用户指南.pdf](http://cdn.gowinsemi.com.cn/SUG940-1.3_Gowin%E8%AE%BE%E8%AE%A1%E6%97%B6%E5%BA%8F%E7%BA%A6%E6%9D%9F%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)
   - [SUG502-1.3_Gowin_Programmer用户指南.pdf](http://cdn.gowinsemi.com.cn/SUG502-1.3_Gowin_Programmer%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)
   - [SUG114-2.5_Gowin在线逻辑分析仪用户指南.pdf](http://cdn.gowinsemi.com.cn/SUG114-2.5_Gowin%E5%9C%A8%E7%BA%BF%E9%80%BB%E8%BE%91%E5%88%86%E6%9E%90%E4%BB%AA%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)

上面的都已经打包进了下载站[点我跳转](https://dl.sipeed.com/shareURL/TANG/Primer_20K/07_Chip_manual/CN/%E9%80%9A%E7%94%A8%E6%8C%87%E5%BC%95)。可以点击压缩包全都下载下来

其他学习链接：
+ 在线免费教程：[菜鸟教程](https://www.runoob.com/w3cnote/verilog-tutorial.html)（学习Verilog）
+ 在线免费 FPGA 教程：[Verilog](https://www.asic-world.com/verilog/index.html)
+ Verilog 刷题网站：[HDLBits](https://hdlbits.01xz.net/wiki/Main_Page)
+ 在线高云视频教程：[点击这里](http://www.gowinsemi.com.cn/video_complex.aspx?FId=n15:15:26)

## 例程汇总

https://github.com/sipeed/TangPrimer-20K-example

部分例程教程：

- LED drive ：[点我](./examples/LED.md)

## **硬件资料汇总**

规格书、原理图、尺寸图等均可在这里找到：[点击这里](https://dl.sipeed.com/shareURL/TANG/Primer_20K)

## **注意事项**

1. 如果有什么疑问，欢迎加群 `834585530`, 或者去[论坛](bbs.sipeed.com)发帖

2. 如果使用 programmer 时候出现了红色的错误（比如找不到设备下载失败等），建议查看相关问题 [点我](https://wiki.sipeed.com/hardware/zh/tang/Tang-Nano-Doc/questions.html)

3. 避免使用 JTAG、MODE、DONE 等引脚。如果一定要使用这些引脚，请自行阅读高云《UG292-1.0原理图指导手册》

4. 请注意避免静电打到 PCBA 上；接触 PCBA 之前请把手的静电释放掉

5. 每个GPIO的工作电压已经在原理图中标注出来，请不要让 GPIO 的实际工作的电压超过额定值，否则会引起 PCBA 的永久性损坏

6. 请在上电过程中，避免任何液体和金属触碰到PCBA上的元件的焊盘，否则会导致短路，烧毁 PCBA

