# SPMOD - LCD 1.14


## Outline

<img src="../../assets/spmod/spmod_lcd1.14//sp_lcd.png" align="right" width="" height="500" />

SPMOD_LCD1.14(1.14 inch LCD) uses ST7735S TFT LCD.

## SPMOD - LCD1.14 Introduction

- Using **Sipeed-SPMOD** interface(2.54mm * 8PIN )，unified MaixPy board interface
- Using commom LCD driver IC ST7735S(4-wire SPI communicate)
- Display Resolution:240\*135
- Size:35.0\*20.0mm

### ST7735S TFT LCD Introduction

| Features： | --- |
| --- | -- |
| Supply voltage of external power supply | 2.5V~4.8V |
| Supply current of external power supply | <20mA |
| Range of working temperature | -30℃ ~ 85℃ |
| Sleep Status of Current | <0.1mA |
| Screen Size | 1.14 inch |
| Active Area | 1.7mm * 10.8mm |
| Display Resolution | 160*80 |
| Color | 132 RGB channels |
| Interface | 8P FPC (0.5mm pitch) |
> DC/DC Converter,
Adjustable VCOM Generation,
Non-volatile (NV) Memory to Store Initial Register Setting,
Oscillator for Display Clock Generation,
Factory default value (module ID, module version, etc) are stored in NV memory,
Timing Controller,


###  SPMOD_LCD1.14 pin description :

| Pin | Name | Type | Description |
| -------- | -------- | ---- | --- |
| 1 | GND | G  | Ground |
| 2 | CS | I  | Chip Select input pin |
| 3 | D/C | I  | Data/Command control pin |
| 4 | RST | I  | Reset (active low) |
| 5 | 3V3 | V  | Power supply(3.3V) |
| 6 | SCK | I  | SPI clock pin |
| 7 | SI | I/O  | Master Out Slave In |
| 8 | BL | I  | BackLight control pin (active high) |

<img src="../../assets/spmod/spmod_lcd1.14/back.png" width="300" />

- Mode of connection:

|   MCU:FUN(IO)   | SP_LCD |
| :-------------: | :----: |
|  GPIOHS7(IO_7)  |  RST   |
| GPIOHS15(IO_15) |  D/C   |
| SPI:SS0(IO_20)  |   CS   |
| SPI:SCK(IO_21)  |  SCK   |
| SPI:MOSI(IO_8)  |   SI   |
|  GPIOHS6(IO_6)  |   BL   |
|  2.5~4.8V   |  3.3V  |
|  GND   |  GND   |

<img src="../../assets/spmod/spmod_lcd1.14//connection.png" height="250">

## Usage

* Process
  1. Send AT instruction
  2. Receive the reply
  3. Determines whether the setup was successful

### C :

  ```c

  fpioa_set_function(SPI_IPS_LCD_CS_PIN_NUM, FUNC_SPI1_SS0);   // SPI_IPS_LCD_CS_PIN_NUM: 20;
  fpioa_set_function(SPI_IPS_LCD_SCK_PIN_NUM, FUNC_SPI1_SCLK); // SPI_IPS_LCD_SCK_PIN_NUM: 21;
  fpioa_set_function(SPI_IPS_LCD_MOSI_PIN_NUM, FUNC_SPI1_D0);  // SPI_IPS_LCD_MOSI_PIN_NUM: 8;
  fpioa_set_function(SPI_IPS_LCD_DC_PIN_NUM, FUNC_GPIOHS0 + SPI_IPS_LCD_DC_GPIO_NUM);   // SPI_IPS_LCD_DC_PIN_NUM: 15; SPI_IPS_LCD_DC_GPIO_NUM: 15;
  fpioa_set_function(SPI_IPS_LCD_RST_PIN_NUM, FUNC_GPIOHS0 + SPI_IPS_LCD_RST_GPIO_NUM); // SPI_IPS_LCD_RST_PIN_NUM: 7; SPI_IPS_LCD_RST_GPIO_NUM: 7;
  fpioa_set_function(SPI_IPS_LCD_BL_PIN_NUM, FUNC_GPIOHS0 + SPI_IPS_LCD_BL_GPIO_NUM);   // SPI_IPS_LCD_BL_PIN_NUM: 6; SPI_IPS_LCD_BL_GPIO_NUM: 6;

  // set gpiohs work mode to output mode
  gpiohs_set_drive_mode(SPI_IPS_LCD_DC_GPIO_NUM, GPIO_DM_OUTPUT);
  gpiohs_set_drive_mode(SPI_IPS_LCD_RST_GPIO_NUM, GPIO_DM_OUTPUT);
  gpiohs_set_drive_mode(SPI_IPS_LCD_BL_GPIO_NUM, GPIO_DM_OUTPUT);

  spi_init(1, SPI_WORK_MODE_0, SPI_FF_STANDARD, DATALENGTH, 0);

  ips_lcd_init(); // init
  LCD_ShowPicture(0, 0, LCD_W, LCD_H, gImage_nanke); // display

  ```

### MaixPy :

  ```python

  # 20: SPI_LCD_CS_PIN_NUM;
  fm.register(SPI_LCD_CS_PIN_NUM, fm.fpioa.GPIOHS20, force=True)
  # 15: SPI_LCD_DC_PIN_NUM;
  fm.register(SPI_LCD_DC_PIN_NUM, fm.fpioa.GPIOHS15, force=True)
  # 6: SPI_LCD_BUSY_PIN_NUM;
  fm.register(SPI_LCD_BUSY_PIN_NUM, fm.fpioa.GPIOHS6, force=True)
  # 7: SPI_LCD_RST_PIN_NUM;
  fm.register(SPI_LCD_RST_PIN_NUM, fm.fpioa.GPIOHS7, force=True)

  # set gpiohs work mode to output mode
  cs = GPIO(GPIO.GPIOHS20, GPIO.OUT)
  dc = GPIO(GPIO.GPIOHS15, GPIO.OUT)
  busy = GPIO(GPIO.GPIOHS6, GPIO.OUT)
  rst = GPIO(GPIO.GPIOHS7, GPIO.OUT)

  # 21: SPI_LCD_SCK_PIN_NUM; 8: SPI_LCD_MOSI_PIN_NUM;
  spi1 = SPI(SPI_LCD_NUM, mode=SPI.MODE_MASTER, baudrate=SPI_LCD_FREQ_KHZ * 1000,
              polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=SPI_LCD_SCK_PIN_NUM, mosi=SPI_LCD_MOSI_PIN_NUM)

  ips = SPLCD114(spi1, cs, dc, rst, busy, IPS_WIDTH, IPS_HEIGHT, IPS_MODE)

  # create an 'image' and fill it
  img = image.Image()
  img.draw_rectangle(80, 80, 30, 30)

  # display
  ips.display(img)


  ```

## Runtime environments

| Language |  Board   |      SDK/Firmware version      |
| :------: | :------: | :----------------------------  |
|    C     | MaixCube | kendryte-standalone-sdk v0.5.6 |
|  MaixPy  | MaixCube |         maixpy v0.5.1          |

*The MaixPy firmware is recommended to compile from the latest source*

### Result


* C

  <img src="../../assets/spmod/spmod_lcd1.14//sp_lcd1.14_c.png" height="250" />

* MaixPy

  <img src="../../assets/spmod/spmod_lcd1.14//sp_lcd1.14_py.png" alt="sp_lcd1.14_py" height="250" />

### Transplant

The following parameters need to be modified.

* C

```c
  // board_config.h
  #define SPI_INDEX           1
  #define SPI_SCLK_RATE       600*1000
  #define SPI_CHIP_SELECT_NSS 0 // SPI_CHIP_SELECT_0

  #define SPI_IPS_LCD_CS_PIN_NUM      20
  #define SPI_IPS_LCD_SCK_PIN_NUM     21
  #define SPI_IPS_LCD_MOSI_PIN_NUM    8

  #define SPI_IPS_LCD_DC_PIN_NUM     15
  #define SPI_IPS_LCD_BL_PIN_NUM      6
  #define SPI_IPS_LCD_RST_PIN_NUM     7

  #define SPI_IPS_LCD_DC_GPIO_NUM     15
  #define SPI_IPS_LCD_BL_GPIO_NUM     6
  #define SPI_IPS_LCD_RST_GPIO_NUM    7

  #define USE_HORIZONTAL 3    // 0/1 is horizontal, and 2/3 is vertical.
```

* Maixpy

```python
  ################### config ###################
  SPI_LCD_NUM = SPI.SPI1
  SPI_LCD_DC_PIN_NUM = const(15)
  SPI_LCD_BUSY_PIN_NUM = const(6)
  SPI_LCD_RST_PIN_NUM = const(7)
  SPI_LCD_CS_PIN_NUM = const(20)
  SPI_LCD_SCK_PIN_NUM = const(21)
  SPI_LCD_MOSI_PIN_NUM = const(8)
  SPI_LCD_FREQ_KHZ = const(600)
  ##############################################
```


## Outlook

- SPMOD_LCD1.14 Size drawing:

<img src="../../assets/spmod/spmod_lcd1.14/sipeed_spmod_lcd1.14.png" height="250" />


-----


## Resource Link

| Resource | --- |
| --- | --- |
| Website | www.sipeed.com |
| Github | [https://github.com/sipeed](https://github.com/sipeed) |
| BBS | [http://bbs.sipeed.com](http://bbs.sipeed.com) |
| Wiki | [http://maixpy.sipeed.com](http://wiki.sipeed.com/maixpy) |
| Sipeed model shop | [https://maixhub.com/](https://maixhub.com/) |
| SDK Relevant information | [dl.sipeed.com/MAIX/SDK](dl.sipeed.com/MAIX/SDK) |
| HDK Relevant information | [dl.sipeed.com/MAIX/HDK](dl.sipeed.com/MAIX/HDK) |
| E-mail(Technical Support and Business Cooperation) | [Support@sipeed.com](mailto:support@sipeed.com) |
| telgram link | [https://t.me/sipeed](https://t.me/sipeed) |