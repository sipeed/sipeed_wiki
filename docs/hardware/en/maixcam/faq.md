---
title: MaixCAM FAQ (Frequently Asked Questions)
---

If you can't find your problem below, you can also refer to [MaixPy FAQ](https://wiki.sipeed.com/maixpy/doc/zh/faq.html).

## What's the difference between MaixCAM and LicheeRV-Nano?

MaixCAM can use the resources of LicheeRV-Nano and SG2002, but **LicheeRV-Nano and other SG2002 chip products cannot use software like MaixPy, MaixCDK, MaixVision, etc.** Please do not make a wrong purchase to avoid wasting time and money.

If you want to quickly start developing applications, please choose MaixCAM. If you are a seasoned Linux developer and only want to develop based on the original SG2002 resources, you can choose LicheeRV-Nano.

## Why is there no purchase link in the official Taobao store?

Taobao may close the purchase link when it encounters a shortage of stock. The purchase link will be automatically opened when the stock is available. You can consult the official customer service.


## Power-on Black Screen, No Display on the Screen

* Check if the TF (micro-SD) card is installed.
* Check if the latest system image is burned onto the TF card (strongly recommended to update to the latest system image); see documentation for specific burning methods.
* Check if the TF card is fully inserted into the TF card slot, ensuring there are no gaps and it is not loose.
* Check if the screen and camera ribbon cables are correctly and securely connected; there should be no looseness.
* Check if the power LED (red light) and the system operation status LED (blue light) on the board are lit. If the red light is off, consider hardware issues such as no power supply, insufficient power supply, or a damaged board.
* Connect the board to a computer using a USB to TTL cable, open the serial port assistant on the computer, restart the board, and check the boot logs for any errors.
> If there is no log output, try swapping the TX and RX wires. For MaixCAM, the orientation of the Type-C to serial port adapter may vary, and TX RX might be reversed, meaning it does not support reversible plugging.


