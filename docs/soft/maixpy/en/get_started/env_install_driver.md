---
title: Install USB driver
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: install USB driver
---


Before officially using MaixPy, we need to install the serial port driver before proceeding with the next development and use; because the board is connected to the computer through a USB to serial device (K210 has no USB hardware support function).
Install the driver according to the board's USB to serial chip model.

> Operate the serial port under `Linux` or `Mac`, if you don’t want to use the `sudo` command every time, execute `sudo usermod -a -G dialout $(whoami)` to add yourself to the `dialout` user group, May need to log off or restart to take effect


- Description of the USB to serial port IC on the existing development board

| Development board model | USB to serial port IC | Description |Installation tutorial|
| --- | --- | --- | --- |
| Maix Go | STM32 | STM32 USB emulation FT2232 |[Go](install_driver/go.md)|
| Maix Dock | CH340 | |[Dock](install_driver/dock.md)|
| Maix Duino | CH552 | CH552 Simulation FT2232 |[Duino](install_driver/duino.md)|
| Maix Bit | CH552 (new version)/CH340 (old version) | CH552 analog FT2232 |[Bit](install_driver/bit.md)|
| Maix Cube | GD32(new version)/CH552(old version) | CH552 simulation FT2232 |[Cube](install_driver/ft2232.md)|
| Maix Amigo | GD32 | GD32 simulation FT2232 |[Amigo](install_driver/ft2232.md)|
| Maix Nano | CH552 | CH552 Analog FT2232 |[Nano](install_driver/nano.md)|
| Grove AI HAT | GD32 | GD32 simulation FT2232 |[Amigo](install_driver/ft2232.md)|


> Use the CH340 IC board to directly install the CH340 driver, and all others use the FT2232 driver.

## About the troubleshooting of USB serial ports

If you do not see the serial port, please troubleshoot hardware problems in the following order.

- If there is a ding-dong sound when plugged in to the computer, such as the sound of USB driver loading when the USB flash drive is inserted, it does not indicate that there is a problem with the serial chip on the hardware.
-Replace the cable and try again, replace the computer's USB port and try again, but still can't be loaded, replace the computer to confirm.

If there is no way to burn the firmware, please troubleshoot hardware problems in the following order.

- Use serial port tool to check whether there is maixpy ​​firmware in the hardware
- Set 115200 baud rate to connect to the serial port, press the reset button (RST) to receive the data from the chip, no matter what it is, it means that the serial port chip is working normally, if not, it means the hardware is abnormal.
- Based on the above, proceed to burn the firmware. Before burning, press the BOOT button of the hardware and then press the reset button, then release the BOOT button. At this time, the burning will proceed normally. If not, the Flash is damaged. You can try to burn to SRAM. If the programming fails, it means the serial port chip is abnormal.
- If you still can’t solve the problem when you get here, the hardware is indeed defective

### Introduction to K210's programming mechanism

We often call this a one-key download circuit, which means that it can easily control the BOOT and RST pins through the completion of the RST and DTR of the control serial port to enter the burning mode. As described above, the hardware circuit is expected to be automatically completed by humans. Press RST after BOOT. This is strongly related to the hardware implementation. Based on this, the TX and RX data transmission will be carried out, so we actually need to use the function pins of the UART serial port.

There are multiple types of triggers in Kflash.

We can simply divide them into several types, low-speed 115200 and high-speed 1.500000 baud rate. The difference is based on the programming methods that match these two types of baud rates. Point, if you find that the download process fails, you can appropriately reduce the baud rate. This is caused by the unstable operation of the serial port chip, and the selection of the layout in the tool will only affect the triggering of the first stage of the programming mode, and after that The configured baud rate will be used in the programming firmware, usually not exceeding the communication programming speed with the flash, which is usually 50~60 KB/S.

If you find that you cannot enter the programming mode anyway, either the programming version does not match, or there is a problem with the DTR RST pin of the serial chip (physically).
