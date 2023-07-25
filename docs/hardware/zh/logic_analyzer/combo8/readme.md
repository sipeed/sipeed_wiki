---
title:  SLogic Combo8
keywords: LogicAnalyzer, debugger, link, RISCV, tool
---

## 简介

SLogic combo8是一款基于 Sipeed M0s Dock 进行二次开发而成的逻辑分析仪，同时还兼有CKLink Debugger、DAP-Link Debugger、USB2UART功能，通过按键可以任意切换功能。


![](../assets/slogic_combo8_main.png)


## 功能参数

### SLogic功能参数

| 逻辑分析仪（仅Linux） | **SLogic Combo8** |
| --------------------- | ----------------- |
| 最大通道数            | 8CH               |
| 最高采样率            | 80M               |
| 传输带宽              | 320Mb/s           |
| 采样模式              | Stream            |
| 典型配置              | 80M@3CH 32M@8CH   |
| 信号输入范围          | 0～3.6V           |
| 高低电平门限          | VIH>2V VIL<0.8V   |

### CKLink功能参数

| CKLink       | SLogic Combo8 |
| ------------ | ------------- |
| JTAG时钟速率 | 16M           |
| 典型dump速度 | 1200KB/s      |
| 调试串口     | 最高20Mbps    |

### DAPLink功能参数

| DAPLink      | SLogic Combo8 |
| ------------ | ------------- |
| 调试串口     | 最高20Mbps    |
| 典型烧录速度 | 110KB/s       |

### UART功能参数

| 高速四串口 | **SLogic Combo8** |
| ---------- | ----------------- |
| 最高波特率 | 2x20Mbps+2x1Mbps  |
| 总带宽     | 42Mbps            |
