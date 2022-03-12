# SPMOD - LoRa


## Overview

<img src="../../assets/spmod/spmod_lora/sp_lora.png" align="right" width="" height="500" />

SPMOD_LoRa(LoRa Module) uses M-XL8 module.

## SPMOD - LoRa Introduction

- Using **Sipeed-SPMOD** interface(2.54mm * 8PIN )，unified MaixPy board interface
- Using SP-MOD SPI to communicate with LoRa module
- LoRa module:The SP_LoRa module uses M-XL8 module with LoRaTM modem and LoRa module with adjustable power amplifier. It has high performance and reliability and is connected by SP_MOD.
- 370MHz-1200MHz, Maximum 20dBm (100mW) continuous transmit power
- Size:25.0\*10.0\*4.3mm

### M-XL8 SX1276 LoRa module Introduction

| Features： | --- |
| --- | -- |
| Working frequency | 370MHz-1200Mhz |
| Transmission power | 20dBm(Maximum) |
| Communication interface | SPI |
| Supply voltage of external power supply | 1.8V~6.3V |
| Range of working temperature | -40℃ - 80℃ |
| antenna | external，IPEX |
| Reception Sensitivity | -148dbm |
| RSSI value | 127dB |
| Maximum link budget | 168dB |
| Send and receive status of current | 9.9mA |
| Sleep status of current | 50nA |
| Modulation method | FSK, GFSK, MSK, GMSK, LoRaTM及OOK |
> Built-in LoRaTM modem, built-in CRC, inherited +12dBm adjustable PA+LNA


###  SPMOD_lora pin description:

| Pin  | Name | Type  | Description    |
| -------- | -------- | ---- | ---------- |
| 1 | GND | G  | Ground |
| 2 | CS | I/O | Chip Select input pin |
| 3 | SO | I/O | Master In Slave Out |
| 4 | RST | I | Reset (active low) |
| 5 | 3V3 | V | Power supply(3.3V) |
| 6 | SCK | I | SPI clock pin|
| 7 | SI | I/O | Master Out Slave In |
| 8 | IRQ | I | Connected to DIO0 of the module,，Programmable decision function |

<img src="../../assets/spmod/spmod_lora/back.png" width="300" />

- Mode of communication

|   MCU:FUN(IO)   | SP_LCD |
| :-------------: | :----: |
|  GPIOHS7(IO_7)  |  RST   |
| SPI:MISO(IO_15) |   SO   |
| SPI:SS0(IO_20)  |   CS   |
| SPI:SCK(IO_21)  |  SCK   |
| SPI:MOSI(IO_8)  |   SI   |
|   GPIOH(IO_6)  |  IRQ   |
|  1.8-6.3V    |  3.3V  |
|   GND      |  GND   |

<img src="../../assets/spmod/spmod_lora//connection.png" height="250">

## Usage

* Process

  1. Create the LoRa object and initialize it
  2. Send or receive data

### C :

  ```c

  fpioa_set_function(SPI_LoRa_SX127X_CS_PIN_NUM, FUNC_SPI1_SS0);   // CS: 20
  fpioa_set_function(SPI_LoRa_SX127X_SCK_PIN_NUM, FUNC_SPI1_SCLK); // SCLK: 21
  fpioa_set_function(SPI_LoRa_SX127X_MOSI_PIN_NUM, FUNC_SPI1_D0);  // MOSI: 8
  fpioa_set_function(SPI_LoRa_SX127X_MISO_PIN_NUM, FUNC_SPI1_D1);  // MISO: 15

  fpioa_set_function(SPI_LoRa_SX127X_IRQ_PIN_NUM, FUNC_GPIOHS0 + SPI_LoRa_SX127X_IQR_GPIO_NUM); // IQR: 6
  fpioa_set_function(SPI_LoRa_SX127X_RST_PIN_NUM, FUNC_GPIOHS0 + SPI_LoRa_SX127X_RST_GPIO_NUM); // RST: 7

  spi_init(SPI_DEVICE_1, SPI_WORK_MODE_0, SPI_FF_STANDARD, DATALENGTH, 0);

  sx1278_begin(&SX1278, SX1278_433MHZ, SX1278_POWER_17DBM, SX1278_LoRa_SF_8,
                 SX1278_LoRa_BW_20_8KHZ, 10);

  if (master == 1)
  {
      printf("====MASTER====\r\n");
      ret = sx1278_LoRaEntryTx(&SX1278, 16, 2000);
  }
  else
  {
      printf("====SALAVE====\r\n");
      ret = sx1278_LoRaEntryRx(&SX1278, 16, 2000);
  }

  ```

### MaixPy :

  ```python

  fm.register(20, fm.fpioa.GPIOHS20, force=True) # RST
  fm.register(7, fm.fpioa.GPIOHS7, force=True) # CS

  # set gpiohs work mode to output mode
  cs = GPIO(GPIO.GPIOHS20, GPIO.OUT)
  rst = GPIO(GPIO.GPIOHS7, GPIO.IN)
  # The other pins are configured at SPI initialization time

  spi1 = SPI(SPI.SPI1, mode=SPI.MODE_MASTER, baudrate=100 * 1000,
               polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=21, mosi=8, miso = 15)

  lora = SX127x(spi=spi1, pin_ss=cs)
  lora.init()

  #######receiver###########
  receive(lora)

  ########sender###########
  # send(lora)


  ```

### Runtime environments:

|  Language  |  Board  | SDK/Firmware version |
| :----: | :------: | :----------------------------: |
|   C    | MaixCube | kendryte-standalone-sdk v0.5.6 |
| MaixPy | MaixCube |         maixpy v0.5.1          |

*The MaixPy firmware is recommended to compile from the latest source*

### Result

* C

  <center class="third">
	  <img src="../../assets/spmod/spmod_lora/lora_send_log_c.png" height="250"/><img src="../../assets/spmod/spmod_lora/lora_recv_log_c.png" height="250"/>
  </center>

* MaixPy

  <center class="third">
	  <img src="../../assets/spmod/spmod_lora/lora_send_log.png" height="250"/><img src="../../assets/spmod/spmod_lora/lora_recv_log.png" height="250"/>
  </center>

### Transplant

The following parameters need to be modified

* C

  ```c
    // board_config.h
    #define SPI_INDEX           1
    #define SPI_SCLK_RATE       600*1000
    #define SPI_CHIP_SELECT_NSS 0//SPI_CHIP_SELECT_0

    #define SPI_LoRa_SX127X_CS_PIN_NUM      20
    #define SPI_LoRa_SX127X_SCK_PIN_NUM     21
    #define SPI_LoRa_SX127X_MOSI_PIN_NUM    8
    #define SPI_LoRa_SX127X_MISO_PIN_NUM    15

    #define SPI_LoRa_SX127X_IRQ_PIN_NUM     6
    #define SPI_LoRa_SX127X_RST_PIN_NUM     7

    #define SPI_LoRa_SX127X_IQR_GPIO_NUM    6
    #define SPI_LoRa_SX127X_RST_GPIO_NUM    7
  ```

* MaixPy

  ```python
    ################### config ###################
    LoRa_RST = const(20)
    LoRa_CS = const(7)
    LoRa_SPI_SCK = const(21)
    LoRa_SPI_MOSI = const(8)
    LoRa_SPI_MISO = const(15)
    LoRa_SPI_NUM = SPI.SPI1
    LoRa_SPI_FREQ_KHZ = const(100)
    ##############################################
  ```

## Outlook

- SPMOD_LoRa Size drawing:

<img src="../../assets/spmod/spmod_lora/sipeed_spmod_lora.png" height="250" />

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