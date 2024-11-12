---
title: MaixCAM FAQ (Frequently Asked Questions)
---

**If you can't find your problem below, you can also refer to [MaixPy FAQ](https://wiki.sipeed.com/maixpy/doc/zh/faq.html).**

## What's the difference between MaixCAM and LicheeRV-Nano?

MaixCAM can use the resources of LicheeRV-Nano and SG2002, but **LicheeRV-Nano and other SG2002 chip products cannot use software like MaixPy, MaixCDK, MaixVision, etc.** Please do not make a wrong purchase to avoid wasting time and money.

If you want to quickly start developing applications, please choose MaixCAM. If you are a seasoned Linux developer and only want to develop based on the original SG2002 resources, you can choose LicheeRV-Nano.

## Why is there no purchase link in the official AliExpress store?

AliExpress may close the purchase link when it encounters a shortage of stock. The purchase link will be automatically opened when the stock is available. You can consult the official customer service.


## Power-on Black Screen, No Display on the Screen

* Check if the TF (micro-SD) card is installed.
* Check if the latest system image is burned onto the TF card (strongly recommended to update to the latest system image); see documentation for specific burning methods.
* Check if the TF card is fully inserted into the TF card slot, ensuring there are no gaps and it is not loose.
* Check if the screen and camera ribbon cables are correctly and securely connected; there should be no looseness.
* Check if the power LED (red light) and the system operation status LED (blue light) on the board are lit. If the red light is off, consider hardware issues such as no power supply, insufficient power supply, or a damaged board.
* Connect the board to a computer using a USB to TTL cable, open the serial port assistant on the computer, restart the board, and check the boot logs for any errors.
> If there is no log output, try swapping the TX and RX wires. For MaixCAM, the orientation of the Type-C to serial port adapter may vary, and TX RX might be reversed, meaning it does not support reversible plugging.
* The UART0_TX pin of the chip has a characteristic: when TX is pulled low, the system cannot start. Therefore, check if the UART0_TX pin is connected to any circuit that is pulling it low during startup. Releasing it before startup should resolve the issue.

## Stuck at Boot Screen, Unable to Enter System

The issue could be caused by a problem with the application environment or hardware. You can follow the steps below to troubleshoot:

* If there is important data on the card, first try to back up the data:
  * Try using MaixVision to scan and connect to the device. Use the file management function to back up important data.
  * If MaixVision cannot connect, use a card reader to back up the data. Since Windows might not directly display system contents, you can use DiskGenius to read the data.

* Reflash the latest system. If the system boots successfully, it means the system files were corrupted, and it's not a hardware issue.

* If reflashing the **latest** system image still doesn't resolve the issue, it might be a hardware problem. You can:
  * First check if the camera connection is normal.
  * Then inspect the PCB for any obvious issues, such as loose components, soldering problems, burns, or short circuits.

* You can also try using a USB-to-TTL adapter to connect the computer to the board's serial port (A16/A17 pins). Open a serial port assistant on the computer, restart the board, and check the boot log for any errors.
  > If there's no log output, try swapping the TX and RX wires. For MaixCAM, the Type-C to serial board might have reversed TX and RX, meaning it doesn't support both orientations for plugging in.

