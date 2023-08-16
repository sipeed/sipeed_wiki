---
title:  SLogic Combo8
keywords: LogicAnalyzer, debugger, link, RISCV, tool
update:
  - date: 2023-07-26
    version: v0.1
    author: ctx
    content:
      - Release docs
---

## Introduction

SLogic combo8 is a logic analyzer based on Sipeed M0s Dock for secondary development, and also has CKLink Debugger, DAP-Link Debugger, USB2UART functions, which can be switched arbitrarily by buttons.

![slogic_combo8_main](./../../../zh/logic_analyzer/combo8/assets/readme/slogic_combo8_main.png)

## Function Parameters

### SLogic Function Parameters

| Logic Analyzer | **SLogic Combo8** |
| --------------------------- | ----------------- |
| Maximum Channel Number      | 8CH               |
| Maximum Sampling Rate       | 80M               |
| Transmission Bandwidth      | 320Mb/s           |
| Sampling Mode               | Stream            |
| Typical Configuration       | 80M@4CH 40M@8CH   |
| Signal Input Range          | 0～3.6V           |
| High and Low Level Thresholds | VIH>2V VIL<0.8V   |

In Windows environment, the SLogic combo 8 has maximum transmission bandwidth of 160 Mb/s. The typical configuration includes 80M@2CH and 20M@8CH.

### CKLink Function Parameters

| CKLink       | SLogic Combo8 |
| ------------ | ------------- |
| JTAG Clock Rate | 16M           |
| Typical Dump Speed | 1200KB/s      |
| Debug Serial Port | Up to 20Mbps    |

### DAPLink Function Parameters

| DAPLink      | SLogic Combo8 |
| ------------ | ------------- |
| Debug Serial Port | Up to 20Mbps    |
| Typical Burning Speed | 110KB/s       |

### UART Function Parameters

| High Speed Four Serial Ports | **SLogic Combo8** |
| ---------------------------- | ----------------- |
| Maximum Baud Rate            | 2x20Mbps+2x1Mbps  |
| Total Bandwidth              | 42Mbps            |
