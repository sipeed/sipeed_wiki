# SPMOD - Eink


## Overview

<img src="../../assets/spmod/spmod_eink/sp_eink.png" alt="XXX" style="zoom:40%;" />

SPMOD_Eink(E-paper display module) uses GDEW0154M09 E-paper display.

## SPMOD - Eink Introduction

- Using **Sipeed-SPMOD** interface(2.54mm * 8PIN )，unified MaixPy board interface
- Connect to the screen through the SP-MOD SPI interface
- E-paper display module：GDEW0154M09 is a 1.54" E-paper display，with SPI interface，and has 24P FPC(0.5mm pitch).
- Support 1 bit Black/Write full display capabilities
- Display Resolution：200x200
- Size：35*30*3.8mm

### GDEW0154M09 E-paper display Introduction

| Features： | --- |
| --- | -- |
| Supply voltage of external power supply | 2.3V~3.6V |
| Supply current of external power supply | 1~3mA |
| Range of working temperature | -40℃~85℃ |
| Sleep Status of Current | <5uA |
| Screen Size | 1.54 inch |
| Active Area | 27.6mm*27.6mm |
| Display Resolution | 200*200 |
| Color | 1 bit Black/Write full display capabilities|
| interface | 24P FPC (0.5mm pitch) |
> An integrated circuit contains gate buffer, source buffer, interface, timing control logic, oscillator,
DC-DC, SRAM, LUT, VCOM, and border are supplied with each panel.


###  SPMOD_Eink pin description ：

| Pin | Name | Type | Description |
| -------- | -------- | ---- | --- |
| 1 | GND | G | Ground |
| 2 | CS | I | Chip Select input pin |
| 3 | D/C | I | Data/Command control pin |
| 4 | RES | I | Reset (active low) |
| 5 | 3V3 | V | Power supply(3.3V) |
| 6 | SCK | I |  SPI clock pin |
| 7 | SI | I/O | Master Out Slave In |
| 8 | BSY | O | Busy status output pin |

<img src="../../assets/spmod/spmod_eink/sp_eink_back.png" height="300" />

- Mode of connection:：

|  MCU:FUN(IO)   | SP_Eink |
| :------------: | :-----: |
|  GPIOHS(IO_7)  |   RES   |
| SPIOHS(IO_15)  |   D/C   |
| SPIOHS(IO_20)  |   CS   |
| SPI:SCK(IO_21) |   SCK   |
| SPI:MOSI(IO_8) |   SI    |
|  GPIOHS(IO_6) |   BSY   |
|  2.3-3.6V   |  3.3V   |
|   GND    |   GND   |

<img src="../../assets/spmod/spmod_eink/connection.png" height="250">

### AT instruction list

| Instruction |       description        |
| :---------: | :----------------------: |
|    0x10     | start transport b/w data |
|    0x13     | start transport r/w data |
|    0x12     |  refresh data to screen  |


*See [GDEW0154M09.pdf](https://cn.dl.sipeed.com/shareURL/MAIX/HDK/sp_mod/sp_eink) for more information*

## Usage

* Process

  1.initializatin
  2.create an image and fill it
  3.send image and refresh


### C：

  ```c

  spi_init(1, SPI_WORK_MODE_0, SPI_FF_STANDARD, DATALENGTH, 0);

  fpioa_set_function(SPI_Eink_CS_PIN_NUM, FUNC_SPI1_SS0);   // SPI_Eink_CS_PIN_NUM: 20;
  fpioa_set_function(SPI_Eink_SCK_PIN_NUM, FUNC_SPI1_SCLK); // SPI_Eink_SCK_PIN_NUM: 21;
  fpioa_set_function(SPI_Eink_MOSI_PIN_NUM, FUNC_SPI1_D0);  // SPI_Eink_MOSI_PIN_NUM: 8;

  fpioa_set_function(SPI_Eink_DC_PIN_NUM, FUNC_GPIOHS0 + SPI_Eink_DC_GPIO_NUM);   // SPI_Eink_DC_PIN_NUM: 21;
  fpioa_set_function(SPI_Eink_RST_PIN_NUM, FUNC_GPIOHS0 + SPI_Eink_RST_GPIO_NUM); // SPI_Eink_RST_PIN_NUM: 7;
  fpioa_set_function(SPI_Eink_BL_PIN_NUM, FUNC_GPIOHS0 + SPI_Eink_BL_GPIO_NUM);   // SPI_Eink_BL_PIN_NUM: 6;

  gpiohs_set_drive_mode(SPI_Eink_DC_GPIO_NUM, GPIO_DM_OUTPUT);
  gpiohs_set_drive_mode(SPI_Eink_RST_GPIO_NUM, GPIO_DM_OUTPUT);

  gpiohs_set_pin(SPI_Eink_DC_GPIO_NUM, GPIO_PV_HIGH);
  gpiohs_set_pin(SPI_Eink_RST_GPIO_NUM, GPIO_PV_HIGH);

  gpiohs_set_drive_mode(SPI_Eink_BL_PIN_NUM, GPIO_DM_INPUT_PULL_UP);
  gpiohs_set_pin_edge(SPI_Eink_BL_PIN_NUM, GPIO_PE_BOTH);

    EPD_DisplayInit(); //EPD init

  //Paint initialization
  Paint_NewImage(BlackImage, EPD_WIDTH, EPD_HEIGHT, 270, WHITE); //Set screen size and display orientation
  Paint_SelectImage(BlackImage);                                 //Set the virtual canvas data storage location

  Paint_Clear(WHITE); //clear paint
  Paint_DrawString_EN(0, 0, "sipeed", &Font8, WHITE, BLACK);   //5*8
  Paint_DrawString_EN(0, 10, "sipeed", &Font12, WHITE, BLACK); //7*12
  Paint_DrawString_EN(0, 25, "sipeed", &Font16, WHITE, BLACK); //11*16
  Paint_DrawString_EN(0, 45, "sipeed", &Font20, WHITE, BLACK); //14*20
  Paint_DrawString_EN(0, 80, "sipeed", &Font24, WHITE, BLACK); //17*24
  EPD_FullDisplay(BlackImage, BlackImage, 0);                  //display image

  ```

### MaixPy：

  ```python

  spi1 = SPI(SPI.SPI1, mode=SPI.MODE_MASTER, baudrate=600 * 1000,
              polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=21, mosi=8)

  fm.register(20, fm.fpioa.GPIOHS20, force=True) # SPI_Eink_SS_PIN_NUM: 20;
  fm.register(15, fm.fpioa.GPIOHS15, force=True) # SPI_Eink_DC_PIN_NUM: 15;
  fm.register(6, fm.fpioa.GPIOHS6, force=True) # SPI_Eink_BUSY_PIN_NUM: 6;
  fm.register(7, fm.fpioa.GPIOHS7, force=True) # SPI_Eink_RST_PIN_NUM: 7;

  cs = GPIO(GPIO.GPIOHS20, GPIO.OUT)
  dc = GPIO(GPIO.GPIOHS15, GPIO.OUT)
  busy = GPIO(GPIO.GPIOHS6, GPIO.IN, GPIO.PULL_DOWN)
  rst = GPIO(GPIO.GPIOHS7, GPIO.OUT)

  epd = SPEink(spi1, cs, dc, rst, busy, SPEink_WIDTH, SPEink_HEIGHT, SPEink_ROTATION)
  epd.init()

  img = image.Image()
  img = img.resize(200, 200)
  img.draw_line(0, 0, 100, 100)

  epd.display(img)

  ```

### Runtime environments:

|  Language  |  Board  | SDK/Firmware version |
| :----: | :------: | :----------------------------: |
|   C    | MaixCube | kendryte-standalone-sdk v0.5.6 |
| MaixPy | MaixCube |         maixpy v0.5.1          |

*The MaixPy firmware is recommended to compile from the latest source*

### Result

* C

  <img src="../../assets/spmod/spmod_eink/sp_eink_c.png" height="250" />

* MaixPy

  <img src="../../assets/spmod/spmod_eink/sp_eink_py.png" height="250" />

### Transplant

The following parameters need to be modified

* C

  ```c
    // board_config.h
    #define SPI_INDEX 1
    #define SPI_SCLK_RATE 600 * 1000
    #define SPI_CHIP_SELECT_NSS 0 //SPI_CHIP_SELECT_0

    #define SPI_Eink_CS_PIN_NUM 20
    #define SPI_Eink_SCK_PIN_NUM 21
    #define SPI_Eink_MOSI_PIN_NUM 8

    #define SPI_Eink_DC_PIN_NUM 15
    #define SPI_Eink_BL_PIN_NUM 6
    #define SPI_Eink_RST_PIN_NUM 7

    #define SPI_Eink_DC_GPIO_NUM 15
    #define SPI_Eink_BL_GPIO_NUM 6
    #define SPI_Eink_RST_GPIO_NUM 7
  ```

* MaixPy

  ```python
  ################### config ###################
    SPI_Eink_NUM = SPI.SPI1
    SPI_Eink_DC_PIN_NUM = const(15)
    SPI_Eink_BUSY_PIN_NUM = const(6)
    SPI_Eink_RST_PIN_NUM = const(7)
    SPI_Eink_CS_PIN_NUM = const(20)
    SPI_Eink_SCK_PIN_NUM = const(21)
    SPI_Eink_MOSI_PIN_NUM = const(8)
    SPI_Eink_FREQ_KHZ = const(600)
  ##############################################


## Outlook

- SPMOD_Eink Size drawing:

<img src="../../assets/spmod/spmod_eink/sipeed_spmod_eink.png" height="250" />


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
| telgram link | [https://t.me/sipeed](https://t.me/sipeed)  |


