# Tang Primer 20K

> 编辑于2022.08.05

## 前言

Tang Primer 20K 是基于 [GW2A-V18PG256C8IC8I7](http://www.gowinsemi.com.cn/prod_view.aspx?TypeId=10&amp;FId=t3:10:3&amp;Id=167#GW2A) 所设计的一款 dd3 sodimm 封装的核心板，额外配套了两个底板，分别为 Dock 底板和 Lite 底板。作为 Sipeed 所发售的第六款 FPGA 产品，Tang Primer 20K 一直广受关注。

得益于 GW2A 丰富的资源，Tang Primer 20K 可以满足多种项目需求；例如当下最火的“”使用并体验高云所提供的 [Gowin_EMPU_M1](http://www.gowinsemi.com.cn/prodshow_view.aspx?TypeId=71&Id=178&FId=t31:71:31#IP)、[PicoRV32](http://www.gowinsemi.com.cn/prodshow_view.aspx?TypeId=70&Id=175&FId=t31:70:31#IP)两款常用软核，或者也可以用来验证自己所设计的软核。

当然两款配套的 Dock 底板与 Lite 底板资源不同。前者所搭载的多个外设例如 dvp 摄像头、rgb屏幕和百兆以太网接口适合用户快速验证自己所写的代码，当然也可以使用高云所提供的[USB软核](http://www.gowinsemi.com.cn/enrollment_view.aspx?TypeId=67&Id=858&FId=t27:67:27#IP)，来自行开发一下有趣的东西；后者留出巨多的多个自定义 IO 来使用户自己决定所需要驱动的外设或者其他配件。

这次以底板 + 核心板的设计，能够满足大多数用户不同的基础使用需求。

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
			<td style="text-align:left">3.3V IO x 111 个 + 1.5V IO x 4 个</td>
			<td style="text-align:left"></td>
		</tr>
	</tbody>
</table>

## 底板参数

| 条目 | Dock  | Lite | 补充 |
| :--- | :--- | :--- | --- |
| 用户按键 | 5个 | 2个 | |
| 拓展接口 |<table><tr><td style="text-align:left">RGB565 接口</td><td style="text-align:left">1 x 40P\*0.5mm fpc</td></tr><tr><td style="text-align:left">DVP 接口</td><td style="text-align:left">1 x 24P\*0.5mm fpc</td></tr><tr><td style="text-align:left">麦克风阵列接口</td><td style="text-align:left">1 x 10P\*0.5mm fpc</td></tr><tr><td style="text-align:left">触摸接口</td><td style="text-align:left">1 x 4P\*0.5mm fpc</td></tr><tr><td style="text-align:left">PMOD接口</td><td style="text-align:left">4</td></tr></table>4个PMOD接口与 RGB565、DVP、麦克风阵列<br>三个接口复用| PMOD * 4 ||
| 3.5mm 耳机接口 | 1个 |||
| REG LED | WS2812 * 1个 |||
| 拨码开关 | 5P * 1个 | ||
| 滑动开关 | 1个，用于切换 USB 功能| 2个 ||
| LED | 6个 |  ||
| HDMI 接口 | 1个 |||
| USB |  |  ||
| 百兆以太网 |  |  ||
| 排针 | | 2 x 20P*2.54mm 排针 |

