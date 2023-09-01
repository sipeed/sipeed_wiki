---
title:  Update Firmware
keywords: LogicAnalyzer, debugger, link, tool
update:
  - date: 2023-09-01
    version: v0.1
    author: lxo
    content:
      - Release docs
---

The following are the steps to update the firmware of SLogic Combo8

## Download Tool and Firmware

Tool: [Click to download](https://dl.sipeed.com/shareURL/SLogic/SLogic_combo_8/4_application/Tools)

Firmware: [Click to download](https://dl.sipeed.com/shareURL/SLogic/SLogic_combo_8/4_application/Firmware)

Just select the latest version of the burning tool and firmware, and unzip it after downloading.

## Configure Tool

1. Start the tool

    After decompression, the execution files of different system environments are provided in the root directory of the tool.

    For Windows users：Double-click`BLDevCube.exe`to start

    For Linux users：Double-click`BLDevCube-ubuntu`to start。Note that the Linux environment needs to add executable permissions `sudo chmod +x BLDevCube-ubuntu`

2. Select chip

    After startup, select BL616/618 and click Finish

    ![image-20230901095004741](./../../../zh/logic_analyzer/combo8/assets/download_firmware/chip_selection.png)

3. Enable `Single Download Options` and add the downloaded firmware

    ![image-20230901095354294](./../../../zh/logic_analyzer/combo8/assets/download_firmware/config_download_firmware.png)

## Configure device

Put SLogic combo 8 into burning mode

![image-20230901101839362](./../../../zh/logic_analyzer/combo8/assets/download_firmware/enter_the_burn_mode.png)

Steps:

1. Long press the button
2. Power on again
3. Observe that the LED light is off, the operation is successful

## Burn firmware

Configure the serial port and baud rate, and click `Create & Download` to download

![image-20230901102645831](./../../../zh/logic_analyzer/combo8/assets/download_firmware/download_firmware.png)

After the download is completed, the progress bar displays a green box, indicating that the download is successful and the firmware update is completed.