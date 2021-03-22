---
title: FPIOA (现场可编程 IO 阵列， Field Programmable Input and Output Array)
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: FPIOA (现场可编程 IO 阵列， Field Programmable Input and Output Array)
---


K210 支持每个外设随意映射到任意引脚， 使用 FPIOA 功能来实现。

**注意**:

以下 GPIOHS 默认已经被使用， 程序中如非必要尽量不要使用：

| GPIOHS | 功能| 描述 |
| ------ | --- | --- |
| GPIOHS5 | LCD_DC      | LCD 读写信号引脚 |
| GPIOHS4 | LCD_RST     | LCD 复位芯片脚 |
| GPIOHS29 | SD_CS       | SD 卡 SPI 片选 |
| GPIOHS28 | MIC_LED_CLK | SK9822_DAT |
| GPIOHS27 | MIC_LED_DATA | SK9822_CLK |



## 类 `FPIOA`

### 方法

#### help(func)

显示外设及其简要描述

##### 参数

* `func`： 外设名（功能/编号），可以不传参， 则以表格的形式显示所有外设名即简要描述，这个表格也可以在本页的末尾找到（[附录：外设表](#附录：-外设表)）；</br>
   如果传参，则传一个整型值， 找到该编号对应的外设后会打印外设名和描述，</br>
   比如 `FPIOA.JTAG_TCLK` 或者 `fm.fpioa.JTAG_TCLK`（`fm`在本页后面介绍） 或者 `0`

比如：

```python
from Maix import FPIOA

fpioa = FPIOA()
fpioa.help()
fpioa.help(0)
fpioa.help(fpioa.JTAG_TCLK)
fm.fpioa.help()
fm.fpioa.help(fm.fpioa.JTAG_TCLK)

```

##### 返回

外设名及其简要描述

#### set_function(pin, func)

设置引脚对应的外设功能， 即引脚映射

##### 参数

* `pin`： 引脚编号，取值 [0, 47]， 具体的引脚连接请看电路图， 也可以使用 `board_info.` 然后按 `TAB` 按键补全来获得板子的常用引脚，比如 `board_info.LED_G`
* `func`： 外设功能，传一个整型值，可以通过  `fm.fpioa.help()`或者查本页末尾的 [附录： 外设表](#附录：-外设表) 表得到

比如 需要将连接 `绿色 LED` 的引脚映射到 `高速 GPIO0` 上：

```python
fpioa = FPIOA()
fpioa.set_function(board_info.LED_G, fm.fpioa.GPIOHS0)
```

#### get_Pin_num(func)

获取外设映射到哪个引脚上了

##### 参数

* `func`： 外设功能，传一个整型值，可以通过  `fm.fpioa.help()`或者查本页末尾的 [附录： 外设表](#附录：-外设表) 表得到

比如：

```python
fpioa = FPIOA()
fpioa.set_function(board_info.LED_G, fm.fpioa.GPIOHS0)
pin = fpioa.get_Pin_num(fm.fpioa.GPIOHS0)
if pin == board_info.LED_G:
    print("set function ok")
```


## 附录： 外设表

|   外设功能（func）  |             简要描述              |
| ----------------- | -------------------------------- |
|  JTAG_TCLK        |  JTAG Test Clock                 |
|  JTAG_TDI         |  JTAG Test Data In               |
|  JTAG_TMS         |  JTAG Test Mode Select           |
|  JTAG_TDO         |  JTAG Test Data Out              |
|  SPI0_D0          |  SPI0 Data 0                     |
|  SPI0_D1          |  SPI0 Data 1                     |
|  SPI0_D2          |  SPI0 Data 2                     |
|  SPI0_D3          |  SPI0 Data 3                     |
|  SPI0_D4          |  SPI0 Data 4                     |
|  SPI0_D5          |  SPI0 Data 5                     |
|  SPI0_D6          |  SPI0 Data 6                     |
|  SPI0_D7          |  SPI0 Data 7                     |
|  SPI0_SS0         |  SPI0 Chip Select 0              |
|  SPI0_SS1         |  SPI0 Chip Select 1              |
|  SPI0_SS2         |  SPI0 Chip Select 2              |
|  SPI0_SS3         |  SPI0 Chip Select 3              |
|  SPI0_ARB         |  SPI0 Arbitration                |
|  SPI0_SCLK        |  SPI0 Serial Clock               |
|  UARTHS_RX        |  UART High speed Receiver        |
|  UARTHS_TX        |  UART High speed Transmitter     |
|  RESV6            |  Reserved function               |
|  RESV7            |  Reserved function               |
|  CLK_SPI1         |  Clock SPI1                      |
|  CLK_I2C1         |  Clock I2C1                      |
|  GPIOHS0          |  GPIO High speed 0               |
|  GPIOHS1          |  GPIO High speed 1               |
|  GPIOHS2          |  GPIO High speed 2               |
|  GPIOHS3          |  GPIO High speed 3               |
|  GPIOHS4          |  GPIO High speed 4               |
|  GPIOHS5          |  GPIO High speed 5               |
|  GPIOHS6          |  GPIO High speed 6               |
|  GPIOHS7          |  GPIO High speed 7               |
|  GPIOHS8          |  GPIO High speed 8               |
|  GPIOHS9          |  GPIO High speed 9               |
|  GPIOHS10         |  GPIO High speed 10              |
|  GPIOHS11         |  GPIO High speed 11              |
|  GPIOHS12         |  GPIO High speed 12              |
|  GPIOHS13         |  GPIO High speed 13              |
|  GPIOHS14         |  GPIO High speed 14              |
|  GPIOHS15         |  GPIO High speed 15              |
|  GPIOHS16         |  GPIO High speed 16              |
|  GPIOHS17         |  GPIO High speed 17              |
|  GPIOHS18         |  GPIO High speed 18              |
|  GPIOHS19         |  GPIO High speed 19              |
|  GPIOHS20         |  GPIO High speed 20              |
|  GPIOHS21         |  GPIO High speed 21              |
|  GPIOHS22         |  GPIO High speed 22              |
|  GPIOHS23         |  GPIO High speed 23              |
|  GPIOHS24         |  GPIO High speed 24              |
|  GPIOHS25         |  GPIO High speed 25              |
|  GPIOHS26         |  GPIO High speed 26              |
|  GPIOHS27         |  GPIO High speed 27              |
|  GPIOHS28         |  GPIO High speed 28              |
|  GPIOHS29         |  GPIO High speed 29              |
|  GPIOHS30         |  GPIO High speed 30              |
|  GPIOHS31         |  GPIO High speed 31              |
|  GPIO0            |  GPIO pin 0                      |
|  GPIO1            |  GPIO pin 1                      |
|  GPIO2            |  GPIO pin 2                      |
|  GPIO3            |  GPIO pin 3                      |
|  GPIO4            |  GPIO pin 4                      |
|  GPIO5            |  GPIO pin 5                      |
|  GPIO6            |  GPIO pin 6                      |
|  GPIO7            |  GPIO pin 7                      |
|  UART1_RX         |  UART1 Receiver                  |
|  UART1_TX         |  UART1 Transmitter               |
|  UART2_RX         |  UART2 Receiver                  |
|  UART2_TX         |  UART2 Transmitter               |
|  UART3_RX         |  UART3 Receiver                  |
|  UART3_TX         |  UART3 Transmitter               |
|  SPI1_D0          |  SPI1 Data 0                     |
|  SPI1_D1          |  SPI1 Data 1                     |
|  SPI1_D2          |  SPI1 Data 2                     |
|  SPI1_D3          |  SPI1 Data 3                     |
|  SPI1_D4          |  SPI1 Data 4                     |
|  SPI1_D5          |  SPI1 Data 5                     |
|  SPI1_D6          |  SPI1 Data 6                     |
|  SPI1_D7          |  SPI1 Data 7                     |
|  SPI1_SS0         |  SPI1 Chip Select 0              |
|  SPI1_SS1         |  SPI1 Chip Select 1              |
|  SPI1_SS2         |  SPI1 Chip Select 2              |
|  SPI1_SS3         |  SPI1 Chip Select 3              |
|  SPI1_ARB         |  SPI1 Arbitration                |
|  SPI1_SCLK        |  SPI1 Serial Clock               |
|  SPI_SLAVE_D0     |  SPI Slave Data 0                |
|  SPI_SLAVE_SS     |  SPI Slave Select                |
|  SPI_SLAVE_SCLK   |  SPI Slave Serial Clock          |
|  I2S0_MCLK        |  I2S0 Master Clock               |
|  I2S0_SCLK        |  I2S0 Serial Clock(BCLK)         |
|  I2S0_WS          |  I2S0 Word Select(LRCLK)         |
|  I2S0_IN_D0       |  I2S0 Serial Data Input 0        |
|  I2S0_IN_D1       |  I2S0 Serial Data Input 1        |
|  I2S0_IN_D2       |  I2S0 Serial Data Input 2        |
|  I2S0_IN_D3       |  I2S0 Serial Data Input 3        |
|  I2S0_OUT_D0      |  I2S0 Serial Data Output 0       |
|  I2S0_OUT_D1      |  I2S0 Serial Data Output 1       |
|  I2S0_OUT_D2      |  I2S0 Serial Data Output 2       |
|  I2S0_OUT_D3      |  I2S0 Serial Data Output 3       |
|  I2S1_MCLK        |  I2S1 Master Clock               |
|  I2S1_SCLK        |  I2S1 Serial Clock(BCLK)         |
|  I2S1_WS          |  I2S1 Word Select(LRCLK)         |
|  I2S1_IN_D0       |  I2S1 Serial Data Input 0        |
|  I2S1_IN_D1       |  I2S1 Serial Data Input 1        |
|  I2S1_IN_D2       |  I2S1 Serial Data Input 2        |
|  I2S1_IN_D3       |  I2S1 Serial Data Input 3        |
|  I2S1_OUT_D0      |  I2S1 Serial Data Output 0       |
|  I2S1_OUT_D1      |  I2S1 Serial Data Output 1       |
|  I2S1_OUT_D2      |  I2S1 Serial Data Output 2       |
|  I2S1_OUT_D3      |  I2S1 Serial Data Output 3       |
|  I2S2_MCLK        |  I2S2 Master Clock               |
|  I2S2_SCLK        |  I2S2 Serial Clock(BCLK)         |
|  I2S2_WS          |  I2S2 Word Select(LRCLK)         |
|  I2S2_IN_D0       |  I2S2 Serial Data Input 0        |
|  I2S2_IN_D1       |  I2S2 Serial Data Input 1        |
|  I2S2_IN_D2       |  I2S2 Serial Data Input 2        |
|  I2S2_IN_D3       |  I2S2 Serial Data Input 3        |
|  I2S2_OUT_D0      |  I2S2 Serial Data Output 0       |
|  I2S2_OUT_D1      |  I2S2 Serial Data Output 1       |
|  I2S2_OUT_D2      |  I2S2 Serial Data Output 2       |
|  I2S2_OUT_D3      |  I2S2 Serial Data Output 3       |
|  RESV0            |  Reserved function               |
|  RESV1            |  Reserved function               |
|  RESV2            |  Reserved function               |
|  RESV3            |  Reserved function               |
|  RESV4            |  Reserved function               |
|  RESV5            |  Reserved function               |
|  I2C0_SCLK        |  I2C0 Serial Clock               |
|  I2C0_SDA         |  I2C0 Serial Data                |
|  I2C1_SCLK        |  I2C1 Serial Clock               |
|  I2C1_SDA         |  I2C1 Serial Data                |
|  I2C2_SCLK        |  I2C2 Serial Clock               |
|  I2C2_SDA         |  I2C2 Serial Data                |
|  CMOS_XCLK        |  DVP System Clock                |
|  CMOS_RST         |  DVP System Reset                |
|  CMOS_PWDN        |  DVP Power Down Mode             |
|  CMOS_VSYNC       |  DVP Vertical Sync               |
|  CMOS_HREF        |  DVP Horizontal Reference output |
|  CMOS_PCLK        |  Pixel Clock                     |
|  CMOS_D0          |  Data Bit 0                      |
|  CMOS_D1          |  Data Bit 1                      |
|  CMOS_D2          |  Data Bit 2                      |
|  CMOS_D3          |  Data Bit 3                      |
|  CMOS_D4          |  Data Bit 4                      |
|  CMOS_D5          |  Data Bit 5                      |
|  CMOS_D6          |  Data Bit 6                      |
|  CMOS_D7          |  Data Bit 7                      |
|  SCCB_SCLK        |  SCCB Serial Clock               |
|  SCCB_SDA         |  SCCB Serial Data                |
|  UART1_CTS        |  UART1 Clear To Send             |
|  UART1_DSR        |  UART1 Data Set Ready            |
|  UART1_DCD        |  UART1 Data Carrier Detect       |
|  UART1_RI         |  UART1 Ring Indicator            |
|  UART1_SIR_IN     |  UART1 Serial Infrared Input     |
|  UART1_DTR        |  UART1 Data Terminal Ready       |
|  UART1_RTS        |  UART1 Request To Send           |
|  UART1_OUT2       |  UART1 User-designated Output 2  |
|  UART1_OUT1       |  UART1 User-designated Output 1  |
|  UART1_SIR_OUT    |  UART1 Serial Infrared Output    |
|  UART1_BAUD       |  UART1 Transmit Clock Output     |
|  UART1_RE         |  UART1 Receiver Output Enable    |
|  UART1_DE         |  UART1 Driver Output Enable      |
|  UART1_RS485_EN   |  UART1 RS485 Enable              |
|  UART2_CTS        |  UART2 Clear To Send             |
|  UART2_DSR        |  UART2 Data Set Ready            |
|  UART2_DCD        |  UART2 Data Carrier Detect       |
|  UART2_RI         |  UART2 Ring Indicator            |
|  UART2_SIR_IN     |  UART2 Serial Infrared Input     |
|  UART2_DTR        |  UART2 Data Terminal Ready       |
|  UART2_RTS        |  UART2 Request To Send           |
|  UART2_OUT2       |  UART2 User-designated Output 2  |
|  UART2_OUT1       |  UART2 User-designated Output 1  |
|  UART2_SIR_OUT    |  UART2 Serial Infrared Output    |
|  UART2_BAUD       |  UART2 Transmit Clock Output     |
|  UART2_RE         |  UART2 Receiver Output Enable    |
|  UART2_DE         |  UART2 Driver Output Enable      |
|  UART2_RS485_EN   |  UART2 RS485 Enable              |
|  UART3_CTS        |  UART3 Clear To Send             |
|  UART3_DSR        |  UART3 Data Set Ready            |
|  UART3_DCD        |  UART3 Data Carrier Detect       |
|  UART3_RI         |  UART3 Ring Indicator            |
|  UART3_SIR_IN     |  UART3 Serial Infrared Input     |
|  UART3_DTR        |  UART3 Data Terminal Ready       |
|  UART3_RTS        |  UART3 Request To Send           |
|  UART3_OUT2       |  UART3 User-designated Output 2  |
|  UART3_OUT1       |  UART3 User-designated Output 1  |
|  UART3_SIR_OUT    |  UART3 Serial Infrared Output    |
|  UART3_BAUD       |  UART3 Transmit Clock Output     |
|  UART3_RE         |  UART3 Receiver Output Enable    |
|  UART3_DE         |  UART3 Driver Output Enable      |
|  UART3_RS485_EN   |  UART3 RS485 Enable              |
|  TIMER0_TOGGLE1   |  TIMER0 Toggle Output 1          |
|  TIMER0_TOGGLE2   |  TIMER0 Toggle Output 2          |
|  TIMER0_TOGGLE3   |  TIMER0 Toggle Output 3          |
|  TIMER0_TOGGLE4   |  TIMER0 Toggle Output 4          |
|  TIMER1_TOGGLE1   |  TIMER1 Toggle Output 1          |
|  TIMER1_TOGGLE2   |  TIMER1 Toggle Output 2          |
|  TIMER1_TOGGLE3   |  TIMER1 Toggle Output 3          |
|  TIMER1_TOGGLE4   |  TIMER1 Toggle Output 4          |
|  TIMER2_TOGGLE1   |  TIMER2 Toggle Output 1          |
|  TIMER2_TOGGLE2   |  TIMER2 Toggle Output 2          |
|  TIMER2_TOGGLE3   |  TIMER2 Toggle Output 3          |
|  TIMER2_TOGGLE4   |  TIMER2 Toggle Output 4          |
|  CLK_SPI2         |  Clock SPI2                      |
|  CLK_I2C2         |  Clock I2C2                      |
