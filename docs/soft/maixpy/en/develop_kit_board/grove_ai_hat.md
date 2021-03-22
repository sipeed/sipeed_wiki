---
title: Grove AI HAT
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: Grove AI HAT
---

## Appearance and function introduction

### Appearance at a glance

![Grove AI HAT](../../assets/hardware/grove_ai_hat/grove_ai_hat1.png)

### Onboard functions

| Project           | Description                                                                      |
| ----------------- | -------------------------------------------------------------------------------- |
| CPU:              | Dual-core 64bit RISC-V / 400MHz (double-precision FPU integration)               |
| Memory:           | 8MiB 64bit on-chip SRAM                                                          |
| Storage:          | 16MiB Flash                                                                      |
| Screen (package): | 2.4 inch TFT, capacitive touch screen resolution: 320\*240                       |
| Camera (package): | Equipped with **0V7740** **30W** pixels **Sensor**                               |
| Buttons:          | Reset button, power button (short press to turn on, long press *8S* to turn off) |
| USB:              | Type-C interface, positive and negative blind plugging                           |
| Onboard sensors:  | Three-axis acceleration sensor (ADXL345BCCZ-RL), ADC (ADS1115IDGS)               |


### Hardware onboard expansion interface

The development version opens four [Grove](https://cn.maixpy.sipeed.com/eh/modules/grove/) interfaces to users, and users can easily DIY.

### Onboard I2C device

| Sensor  | Function                 | I2C address (7-bit address) | SCL  | SDA  | Sample code            |
| ------- | ------------------------ | --------------------------- | ---- | ---- | ---------------------- |
| ADS1115 | ADC                      | 0x48                        | IO23 | IO24 | [script](./ads1115.py) |
| ADXL345 | Three-axis accelerometer | 0x53                        | IO23 | IO24 | [script](./adxl345.py) |

## Download

[Schematic](./Grove_AI_HAT_for_Edge_Computing_v1.0_SCH_190514.pdf)