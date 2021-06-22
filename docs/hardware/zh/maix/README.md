---
title: Sipeed Hardware
keywords: Sipeed, Hardware, 矽速, 硬件资料, 文档, 资料下载
desc: 矽速科技的硬件资料站
---

# Sipeed HardWare WIKI

[English](./../../en/maix/README.md)

## K210 核心模组

* [K210 核心模块](./core_modules/k210_core_modules.md)
    - [M1/M1w](./core_modules/k210_core_modules.md)
    - [M1n](./core_modules/k210_core_modules.md)

## MaixPy 系列开发板

* [MaixPy 开发板](./maixpy_develop_kit_board/develop_kit_board.md)
  - [Maix Go](./maixpy_develop_kit_board/maix_go.md)
  - [Maix Dock(M1/M1W)](./maixpy_develop_kit_board/maix_dock.md)
  - [Maix Bit](./maixpy_develop_kit_board/maix_bit.md)
  - [Maix Duino](./maixpy_develop_kit_board/maix_duino.md)
  - [Maix Nano](./maixpy_develop_kit_board/maix_nano.md)
  - [Maix Cube](./zh/maixpy_develop_kit_board/maix_cube.md)
  - [Maix Amigo](./maixpy_develop_kit_board/maix_Amigo.md)

## MaixPy 开发板

目前 MaixPy 系列开发板有一下这几款型号:

- Maix Go

- Maix Dock

- Maix Duino

- Maix Bit

- Maix Cube

- Maix Amigo

## 差异对比

| 型号 | USB IC | 核心模块 | WIFI 功能 |备注 |
|---| --- | --- | --- | --- |
| Maix Go <img src="./assets/dk_board/maix_go/Go.jpg" width="260"> | STM32 | M1W | M1W 模块集成 ESP8285 | 新版本 go 板载 mic |
| Maix Dock <img src="./assets/dk_board/maix_dock/Dan_Dock.png" width="260"> | CH340 | M1/M1W | Dock M1 (不支持 WIFI)<br/>Dock M1W(支持,M1W 模块集成 ESP8285) | --- |
| Maix Duino <img src="./assets/dk_board/maix_duino/maixduino_0.png" width="260"> | CH552 | M1 | 板载 ESP32 （支持 WIFI, 蓝牙功能暂时未支持） | --- |
| Maix Bit <img src="./assets/dk_board/maix_bit/BiT.png" width="260"> | CH552/CH340 | --- | 无 | --- | 
| Maix Cube <img src="./assets/dk_board/maix_cube/maixcube_product_appearance.png" width="260"> | GD32/CH552 | M1n | 无 | --- |
|Maix Amigo <img src="./assets/dk_board/maxi_amigo/maix_amigo_0.png" width="260"> | GD32 | M1n | --- | --- |

| 型号 | USB IC | 核心模块 | WIFI 功能 |备注 |
|---| --- | --- | --- | --- |
| [Maix Go](./maixpy_develop_kit_board/maix_go.md)  | STM32 | M1W | M1W 模块集成 ESP8285 | 新版本 go 板载 mic |
| Maix Dock | CH340 | M1/M1W | Dock M1 (不支持 WIFI)<br/>Dock M1W(支持,M1W 模块集成 ESP8285) | --- |
| Maix Duino | CH552 | M1 | 板载 ESP32 （支持 WIFI, 蓝牙功能暂时未支持） | --- |
| Maix Bit | CH552/CH340 | --- | 无 | --- | 
| Maix Cube | GD32/CH552 | M1n | 无 | --- |
|Maix Amigo | GD32 | M1n | --- | --- |


### MaixPy 外设模块

* [扩展接口 Grove](./)
    - [Grove-RGB LED](./)
* [扩展接口 SP-MOD](./)
    - [转接板类](./)
    - [SP-Extender](./modules_spmod/spmod_extender.md)
    - [SP-Grove](./modules_spmod/spmod_grove.md)
    - [SP-FPC](./modules_spmod/spmod_fpc.md)
    - [SP-MicArray](./modules_spmod/spmod_micarray.md)
    - [SP-JoyStick](./modules_spmod/spmod_joystick.md)
    - [SP-JoyStick2](./zh/modules_spmod/spmod_joystick.md)
    - [SP-Servo](./modules_spmod/spmod_servo.md)
    - [SP-Type-C](./)
    - 传感器类
    - [SP-Weather](./modules_spmod/spmod_weather.md)
    - [SP-TOF-1P](./modules_spmod/spmod_tof.md)
    - 通信类
    - [SP-BLE](./modules_spmod/spmod_bt.md)
    - [SP-LoRa](./modules_spmod/spmod_lora.md)
    - [SP-PSRAM](./modules_spmod/spmod_psram.md)
    - [SP-RFID](./modules_spmod/spmod_rfid.md)
    - [SP-Ethernet](./modules_spmod/spmod_ethernet.md)
    - 显示类
    - [SP-LCD 1.14](./modules_spmod/spmod_lcd1.14.md)
    - [SP-Eink](./modules_spmod/spmod_eink.md)

## 模块&&调试器

### 调试器

- [Sipeed RV Debugger](./)
- [双串口 USB 模块](./)

### 模块

- Camera(Sensor)

    - [OV2640](./)
    - [OV2640-M12](./)
    - [双摄像头模块(OV2640)](./)
    - [GC0328](./)
    - [双摄像头模块(GC0328)](./)
    - [OV7740](./)

- [麦克风模块](./)
  - [单麦克风模块](./)
  - [麦克风阵列](./)

- [LCD 1.3/2.4/2.8/4.3/5 寸](./)
