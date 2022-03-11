# SPMOD - RFID


## Overview

<img src="../../assets/spmod/spmod_rfid/sp_rfid.png" style="padding-right:100px;" align="right" width="" height="500" />

SPMOD_RFID (NFC module) uses  FM17510 IC.

## SPMOD - RFID Introduction

- Using **Sipeed-SPMOD** interface(2.54mm * 8PIN )，unified MaixPy board interface
- Using SP-MOD SPI to communicate with RFID module
- 64Byte TRANSCeiver buffer FIFO
- The RIFC IC is FM17510.
- Size:25.0\*20.1\*6.2mm

### FM17510 Introduction

The FM17510 used in this module is a highly integrated non-contact reader chip working at 13.56MHz.
Supports non-contact reader mode in accordance with ISO/IEC 14443 protocol,


| Features： |
| --- |
| Supports non-contact reader mode in accordance with ISO/IEC 14443 protocol, |
| Reader mode supports M1 encryption algorithm |
| ISO14443 TYPEA supports communication rate: 106kbps， 212kbps， 424kbps |
| Support SPI serial interface, up to 10Mbps |
| Host interface independent power supply，voltage range: 2.2~3.6V |
| Range of working temperature -40℃ ~ 85℃ |
| 64Byte TRANSCeiver buffer FIFO. |
| Interrupt output mode can be equipped with flexible |
| Multiple low-power modes: Soft powerdown Mode, Hard powerdown Mode, Deep powerdown Mode(Typical value 1uA) |
| Support low-power external card detection |
| Programmable timer |
| Built-in oscillator circuit and external 27.12MHz crystal oscillator |
| Wide voltage working range 2.2V~3.6V |
| Built-in CRC coprocessor |
| programmed I/O |



###  SPMOD_RFID pin description:


| Pin | Name | Type | Description | |
| --- | --- | --- | --- | --- |
| 1 | GND | G | Ground |
| 2 | CS | I | Chip Select input pin |
| 3 | SO | I/O | Master In Slave Out  |
| 4 | NPD | I | Reset/Sleep control pin|
| 5 | 3V3 | V | Power supply(3.3V) |
| 6 | SCK | I | SPI clock pin |
| 7 | SI | I/O | Master Out Slave In |
| 8 | IRQ | O | Interrupt output pin |

<img src="../../assets/spmod/spmod_rfid/back.png" height="300" />

- Mode of connection:

|   MCU:FUN(IO)   | SP_RFID |
| :-------------: | :-----: |
| NC(IO_7)     |   NPD   |
| SPI:MISO(IO_15) |   SO    |
| SPI:SS0(IO_20)  |   CS    |
| SPI:SCK(IO_21)  |   SCK   |
| SPI:MOSI(IO_8)  |   SI    |
| NC(IO_6)    |   IRQ   |
| 2.2~3.6V    |  3.3V   |
| GND       |   GND   |

<img src="../../assets/spmod/spmod_rfid/connection.png" height="250">


## Usage

* Process
  1. Initialization
  2. Detected and bind card
  3. Read or write data

### C:

  ```c

  fpioa_set_function(RFID_CS_PIN, FUNC_GPIOHS0 + RFID_CS_HSNUM); // RFID_CS_PIN: 20;
  fpioa_set_function(RFID_CK_PIN, FUNC_GPIOHS0 + RFID_CK_HSNUM); // RFID_CK_PIN: 21;
  fpioa_set_function(RFID_MO_PIN, FUNC_GPIOHS0 + RFID_MO_HSNUM); // RFID_MO_PIN: 8;
  fpioa_set_function(RFID_MI_PIN, FUNC_GPIOHS0 + RFID_MI_HSNUM); // RFID_MI_PIN: 15;

  gpiohs_set_drive_mode(spi_io_cfg.hs_cs, GPIO_DM_OUTPUT);
  gpiohs_set_drive_mode(spi_io_cfg.hs_clk, GPIO_DM_OUTPUT);
  gpiohs_set_drive_mode(spi_io_cfg.hs_mosi, GPIO_DM_OUTPUT);
  gpiohs_set_drive_mode(spi_io_cfg.hs_miso, GPIO_DM_INPUT);

  // detected card
  PcdRequest(0x52, type)

  // auth and bind...

  // read or write 16 bytes data from sector 0x11
  PcdWrite(0x11, w_buf)
  PcdRead(0x11, &r_buf)

  ```

### MaixPy:

  ```python

  # 20: CS_NUM;
  fm.register(20, fm.fpioa.GPIOHS20, force=True)
  # set gpiohs work mode to output mode
  cs = GPIO(GPIO.GPIOHS20, GPIO.OUT)

  # RFID_SCK: 21; RFID_SI:8; RFID_SO: 15;
  spi1 = SPI(SPI.SPI1, mode=SPI.MODE_MASTER, baudrate=600 * 1000,
          polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=21, mosi=8, miso=15)

  # Create an object of the class MFRC522
  MIFAREReader = MFRC522(spi1, cs)

  # detected and auth, bind...

  # read or write 16 bytes data from sector 0x11
  MIFAREReader.MFRC522_Write(0x11, data)
  MIFAREReader.MFRC522_Read(0x11)

  ```
### Runtime environments:

|  语言  | 开发板   | SDK/固件版本                   |
| :----: | :------- | :----------------------------- |
|   C    | MaixCube | kendryte-standalone-sdk v0.5.6 |
| MaixPy | MaixCube | maixpy v0.5.1                  |

### Result:

* C

  <img src="../../assets/spmod/spmod_rfid/c_log.png" height="200" />

* MaixPy

  <img src="../../assets/spmod/spmod_rfid/maixpy_log.png" height="200" />

### Transplant:

The following parameters need to be modified

* C

  ```c
    // board_config.h
    #define RFID_CS_PIN (20)
    #define RFID_CK_PIN (21)
    #define RFID_MO_PIN (8)
    #define RFID_MI_PIN (15)

    #define RFID_CS_HSNUM (20)
    #define RFID_CK_HSNUM (21)
    #define RFID_MO_HSNUM (8)
    #define RFID_MI_HSNUM (15)
  ```

* MaixPy

  ```python
    ################### config ###################
    CS_NUM = const(20)
    SPI_FREQ_KHZ = const(600)
    SPI_SCK = const(21)
    SPI_MOSI = const(8)
    SPI_MISO = const(15)
    #############################################
  ```


## Outlook


- SPMOD_RFID Size drawing:

<img src="../../assets/spmod/spmod_rfid/sipeed_spmod_rfid.png" height="250" />


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
