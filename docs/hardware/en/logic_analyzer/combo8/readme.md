---
title:  SLogic Combo 8
keywords: LogicAnalyzer, debugger, link, RISCV, tool
update:
  - date: 2023-07-26
    version: v0.1
    author: ctx
    content:
      - Release docs
---

## Introduction

SLogic Combo 8 is a development tool with functions of logic analyzer, CKLink debugger, DAP-Link debugger and USB2UART, which can be switched arbitrarily by buttons.

![slogic_combo8_main](./../../../zh/logic_analyzer/combo8/assets/readme/slogic_combo8_main.png)

## Function Parameters

### SLogic Function Parameters

| Logic Analyzer | **SLogic Combo 8** |
| --------------------------- | ----------------- |
| Maximum Channel Number      | 8CH               |
| Maximum Sampling Rate       | 80M               |
| Transmission Bandwidth      | 320Mb/s           |
| Sampling Mode               | Stream            |
| Typical Configuration       | 80M@4CH 40M@8CH   |
| Signal Input Range          | 0～3.6V           |
| High and Low Level Thresholds | VIH>2V VIL<0.8V   |

In Windows environment, the SLogic Combo 8 has maximum transmission bandwidth of 160 Mb/s. The typical configuration includes 80M@2CH and 40M@4CH.

### CKLink Function Parameters

| CKLink       | SLogic Combo 8 |
| ------------ | ------------- |
| JTAG Clock Rate | 16M           |
| Typical Dump Speed | 1200KB/s      |
| Debug Serial Port | Up to 20Mbps    |

### DAPLink Function Parameters

| DAPLink      | SLogic Combo 8 |
| ------------ | ------------- |
| Debug Serial Port | Up to 20Mbps    |
| Typical Burning Speed | 110KB/s       |

### UART Function Parameters

| High Speed Four Serial Ports | **SLogic Combo 8** |
| ---------------------------- | ----------------- |
| Maximum Baud Rate            | 2x20Mbps+2x1Mbps  |
| Total Bandwidth              | 42Mbps            |

## Get Started Now

Click the link below to enter the corresponding chapter:
[Basic Operation](./basic_operation.md)
[Using as Logic Analyzer](./use_logic_function.md)
[Using as CKLink](./use_cklink_function.md)
[Using as DAPLink](./use_daplink_function.md)
[Using as Serial Module](./use_fouruart_function.md)
[Update firmware](./update_firmware.md)

## Others Links

[Sipeed Download station](https://dl.sipeed.com/shareURL/SLogic/SLogic_combo_8/4_application/Firmware)
[Forum](maixhub.com/discussion)

Support Email：support@sipeed.com