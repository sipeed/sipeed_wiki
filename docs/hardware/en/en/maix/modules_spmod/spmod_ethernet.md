# SPMOD - Ethernet


## Overview

<img src="../../assets/spmod/spmod_ethernet/sp_ethernet.png" align="right" width="" height="500" />

SPMOD_Ethernet(Ethernet module) uses W5500 chip.

## SPMOD - Ethernet Introduction

- Using **Sipeed-SPMOD** interface(2.54mm * 8PIN )，unified MaixPy board interface
- Connect to the board through the SP-MOD SPI interface
- Master chip:The W5500 chip is a Hardwired TCP/IP embedded Ethernet controller
- The theoretical SPI design speed is 80MHz
-	10BaseT/100BaseTX Ethernet PHY embedded, Supports Auto Negotiation (Full and half duplex, 10 and 100-based )
- Size:35.76\*19.74\*8.7mm

###  W5500 chip Introduction

| Features: | --- |
| --- | -- |
| Supply voltage of external power supply | 2.97V~3.63V |
| Supply current of external power supply | <132mA |
| Range of working temperature | -40℃~85℃ |
| Sleep Status of Current | <15mA |
| SPI Clock | The theoretical design speed is 80MHz |
| TCP/IP protocol | Support TCP,UDP,ICMP,IPv4,ARP,IGMP,PPPoE protocols |

> - Supports 8 independent sockets simultaneously
,Internal 32Kbytes Memory for TX/RX Buffers
,Supports Wake on LAN over UDP
,10BaseT/100BaseTX Ethernet PHY embedded
,Support Auto Negotiation (Full and half duplex, 10 and 100-based )
,Not support auto-MDIX feature


###  SPMOD_Ethernet pin description:

| Pin  | Name | Type  | Description  |
| -------- | -------- | ---- | ---------- |
| 1 | GND | G |  Ground |
| 2 | CS | I | Chip Select input pin |
| 3 | SO | I/0 | Master In Slave Out  |
| 4 | NC | NC | Not connected |
| 5 | 3V3 | V | Power supply(3.3V) |
| 6 | SCK | I | SPI clock pin |
| 7 | SI | I/0 | Master Out Slave In |
| 8 | NC | NC | Not connected |


<img src="" width="300" />


## Usage

- 待更新

## Outlook

- SPMOD_Ethernet Size drawing:

<img src="../../assets/spmod/spmod_ethernet/sipeed_spmod_ethernet.png" height="250" />

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