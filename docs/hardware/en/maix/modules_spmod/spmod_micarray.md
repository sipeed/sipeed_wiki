# SPMOD - MicArray


## Overview

<img src="../../assets/spmod/spmod_micarray/sp_micarray.png" align="right" width="" height="500" />

SPMOD_MicArray(Microphone array module) uses RY3708(DC-DC)Boost Module

## SPMOD - MicArray Introduction

- Using **Sipeed-SPMOD** interface(2.54mm * 8PIN )，unified MaixPy board interface
- Transfer the SP-MOD interface to the FPC, and use the FPC to connect to the microphone array board
- 3.3V to 5V boost regulator(DC-DC)(RY3708)，easily drive microphone arrays.
- Use the Grove interface to control the LED on the microphone array module.
- It needs to be used with the SIPEED MICARRAY module.
- Size:35.0\*10.0\*11.2mm


###  BOOST DC-DC RY3708 module Introduction

| Features： | --- |
| --- | -- |
| Output voltage range | 5.1V ±0.2V |
| Supply voltage of external power supply |	3.3V ±0.2V |
| Supply current of external power supply | Depends on the working conditions of the module, usually less than 500mA |
| Range of working temperature | -40℃ ~ 85℃ |
> 1.2MHz Fixed Switching Frequency,Internal 4A Switch Current Limit,
Thermal Shutdown,Integrated 80mΩ Power MOSFET


###  SPMOD_MicArray pin description:

| Pin  | Name | Type  | Description    |
| -------- | -------- | ---- | ---------- |
| 1 | GND | G |Ground |
| 2 | D2 | I | Mic_D0 |
| 3 | D3 | I | Mic_D2 |
| 4 | D0 | I | Mic_WS |
| 5 | 3V3 | V |Power supply(3.3V) |
| 6 | D4 | I | Mic_D1 |
| 7 | D5 | I | Mic_D3 |
| 8 | D1 | I | Mic_BCK |
| 9 | CK | I | Serial clock pin to control LED |
| 10 | DA | I | Data clock pin to control LED |
<img src="" width="300" />


## Usage

- 待补充

## Outlook

- SPMOD_MicArray Size drawing:

<img src="../../assets/spmod/spmod_micarray/sipeed_spmod_micarray.png" height="250" />

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