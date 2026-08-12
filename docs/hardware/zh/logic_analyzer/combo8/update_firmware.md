---
title:  更新固件
keywords: LogicAnalyzer, debugger, link, tool
update:
  - date: 2026-08-12
    version: v0.2
    author: Sipeed
    content:
      - 增加 `slogic_combo8_pack_202608121500.bin` 修复说明和升级后检查项
  - date: 2023-09-01
    version: v0.1
    author: lxo
    content:
      - Release docs
---

以下是SLogic Combo 8 更新固件的步骤

## 下载烧录工具和固件

烧录工具：[点击下载](https://dl.sipeed.com/shareURL/SLogic/SLogic_combo_8/4_application/Tools)

固件：[点击下载](https://dl.sipeed.com/shareURL/SLogic/SLogic_combo_8/4_application/Firmware)

烧录工具选择最新版本。固件请选择 `slogic_combo8_pack_202608121500.bin` 或更新版本，下载完成后自行解压。

> 注：当固件名为`slogic_combo8_pack_202308171404.bin`时，日期为2023年08月17日。其他固件的日期命名规则类似。

`slogic_combo8_pack_202608121500.bin` 包含以下修复：

- LA：修复 CH7 悬空时波形不干净的问题；
- DAPLink：修复串口不稳定问题，改进高速连续传输、串口参数切换以及 USB 重新连接后的恢复过程。

## 配置烧录工具

1. 启动烧录工具

    解压后，烧录工具的根目录下提供了不同系统环境的执行文件。

    Windows用户：双击`BLDevCube.exe`启动

    Linux用户：双击`BLDevCube-ubuntu`启动。注意Linux环境需要添加可执行权限`sudo chmod +x BLDevCube-ubuntu`

2. 选择芯片

    启动后，选择 **BL616/618** 并点击Finish

    ![chip_selection](./assets/download_firmware/chip_selection.png)

3. 使能Single Download Options，并添加下载好的固件

    ![config_download_firmware](./assets/download_firmware/config_download_firmware.png)

## 配置设备

让SLogic Combo 8进入烧录模式

![enter_the_burn_mode](./assets/download_firmware/enter_the_burn_mode.png)

操作步骤：

1. 长按按键不松开
2. 重新上电
3. 观察LED灯不亮，则操作成功

## 烧录固件

配置串口号和波特率，并点击`Create & Download`即可下载

![download_firmware](./assets/download_firmware/download_firmware.png)

下载完成后，进度条显示绿框说明下载成功。重新上电，并按以下步骤确认更新结果：

1. 切换到蓝灯逻辑分析仪模式，确认系统识别到 `SLogic8 U2`；
2. 切换到绿灯 DAPLink 模式，确认系统识别到 `RV CMSIS-DAP`；
3. 如果升级是为了解决 DAPLink 串口或调试稳定性问题，请按原连接和速率重新测试。
