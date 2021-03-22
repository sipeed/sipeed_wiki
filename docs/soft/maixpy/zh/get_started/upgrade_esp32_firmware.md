---
title: 更新板载 ESP32 固件
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 更新板载 ESP32 固件
---


## 简介：

MaixPy 系列的开发板中 MaixDuino 板载了一块 ESP32 WIFI SOC，在默认情况下我们不需要更新板载的 ESP32 模块，但是但我们发现使用过程中存在 bug 并修复了之后我们就需要更新修复的固件。

## 更新 ESP32 固件步骤

### 准备


- 硬件: MaixDuino, USB Type-C 数据线
- 软件: ESPFLASH

- ESP32 固件更新工具：ESP32 **flash_download_tools**
  - 下载链接：[**flash_download_tools**](https://www.espressif.com/zh-hans/support/download/other-tools)
- ESP32 MaixDuino 固件：
  - 下载链接：[**flash_download_tools**](https://cn.dl.sipeed.com/MAIX/factory_firmware/)

### 更新流程：

1. 下载 **flash_download_tools**，

   ![flash_download_tools](../../assets/hardware/module_esp32/image-20200504164050916.png)
   ![flash_download_tools](../../assets/hardware/module_esp32/image-20200504164221705.png)

2. 下载 **MaixDuino ESP32 固件**
   ![update esp32](../../assets/hardware/module_esp32/image-20200504164245329.png)

3. 连接 MaixDuino, 选择 ESP32 串口(一般都是串口号比较大的)
4. 设置下载选项:
   1. 如图配置相应选项, 注意**波特率一定要设置为 115200**
   ![b6474ddd5340cc9b7cf6006f75974a7b.png](../../assets/hardware/module_esp32/image-20200504164320888.png)
   ![acf618a24b4cb8c5f8c2e98acc6cf11b.png](../../assets/hardware/module_esp32/image-20200504164450650.png)

5. 点击 **Start** 更新固件，并等待完成更新
6. 验证更新是否完成

   1. 使用 XCOM, 打开 ESP32 串口，点击 RST 复位 ESP32，如图即刷入成功

   ![96e955badd7450e7b5ba58230ae12c48.png](../../assets/hardware/module_esp32/image-20200504164747839.png)
