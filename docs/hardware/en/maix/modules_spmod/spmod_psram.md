# SPMOD - PSRAM


## Overview

<img src="../../assets/spmod/spmod_psram/sp_psram.png" align="right" width="" height="500" />

SPMOD_PSRAM(PSRAM module) uses IPS6404L-SQ PSRAM.

## SPMOD - PSRAM Introduction

- Using **Sipeed-SPMOD** interface(2.54mm * 8PIN )，unified MaixPy board interface
- Connect to the board through the SP-MOD SPI/QPI interface
- Pseudo−SRAM:IPS6404L-SQ is 64 Mbit of SPI/QPI (serial/quad parallel interface) Pseudo−SRAM device.
- Working frequency:104MHz
- CLK period:30.3ns
- Size:15.0\*10.0\*13.3mm

###  IPS6404L-SQ Introduction：

| Features: | --- |
| --- | -- |
| Supply voltage of external power supply | 2.7V~3.6V |
| Supply current of external power supply | 10mA |
| Range of working temperature | -30℃~85℃ |
| Sleep Status of Current | <250μA |
| Working frequency | 104Mhz |
| Response time of SPI read | 30.3ns |
| Response time of other operations | 9.3ns |
| interface | PI/QPI optional, default SPI |


###  SPMOD_PSRAM pin description:

| Pin  | Name | Type  | Decription    |
| -------- | -------- | ---- | ---------- |
| 1 | GND  | G | Ground |
| 2 | CS | I  | Chip Select input pin |
| 3 | D1 | I/0 | Master In Slave Out |
| 4 | D3 | I/O | No function (IO3 in QSPI mode) |
| 5 | 3V3 | V | Power supply(3.3V) |
| 6 | SCK | I | SPI clock pin |
| 7 | D0 | I/0 | Master Out Slave In (IO0 in QSPI mode) |
| 8 | D2 | I/O | No function (IO2 in QSPI mode) |


<img src="" width="300" />


## Usage

- wait upgrade

## Outlook

- SPMOD_PSRAM Size drawing:

<img src="../../assets/spmod/spmod_psram/sipeed_spmod_psram.png" height="250" />

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
