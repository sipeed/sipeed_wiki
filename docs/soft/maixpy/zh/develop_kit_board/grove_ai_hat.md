---
title: Grove AI HAT
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: Grove AI HAT
---

## 外观及功能介绍

### 外观一览

![Grove AI HAT](../../assets/hardware/grove_ai_hat/grove_ai_hat1.png)

### 板载功能

| 项目             | 说明                                                   |
| ---------------- | ------------------------------------------------------ |
| CPU：            | 双核 64bit RISC-V / 400MHz (双精度FPU集成)             |
| 内存：           | 8MiB 64bit 片上 SRAM                                   |
| 存储：           | 16MiB Flash                                            |
| 屏幕（套餐）：   | 2.4 寸 TFT, 电容触摸屏幕分辨率：320\*240               |
| 摄像头（套餐）： | 搭载 **0V7740** **30W** 像素 **Sensor**                |
| 按键：           | 复位按键，电源按键（短按开机，长按 *8S* 关机）         |
| USB：            | Type-C 接口，正反盲插                                  |
| 板载传感器：     | 三轴加速度传感器（ADXL345BCCZ-RL），ADC（ADS1115IDGS） |


### 硬件板载扩展接口

该开发版对用户开放了四个 [Grove](https://cn.maixpy.sipeed.com/zh/modules/grove/) 接口,用户可以很方便的进行 DIY。

### 板载 I2C 设备

| 传感器  | 功能         | I2C 地址(7位地址) | SCL  | SDA  | 示例代码               |
| ------- | ------------ | ----------------- | ---- | ---- | ---------------------- |
| ADS1115 | ADC          | 0x48              | IO23 | IO24 | [script](https://github.com/sipeed/MaixPy_scripts/tree/master/modules/others/ads1115) |
| ADXL345 | 三轴加速度计 | 0x53              | IO23 | IO24 | [script](https://github.com/sipeed/MaixPy_scripts/tree/master/modules/others/adxl345) |

## 资源下载

[原理图](http://dl.sipeed.com/fileList/MAIX/HDK/Sipeed-Grove_AI_HAT/Grove_AI_HAT_for_Edge_Computing_v1.0_SCH_190514.pdf)