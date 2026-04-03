---
title: NanoKVM Static IP Fix
---

## Applicable Scenario

1. NanoKVM was configured with a static IP and can no longer obtain an IP address via DHCP.

## Cause

Some batches of NanoKVM were mistakenly configured at the factory with a static IP (`192.168.70.70`), which prevents normal DHCP address assignment.

## Fix Steps

Choose any one of the following methods based on your situation:

### Method 1: Reflash the firmware

Reflash the NanoKVM firmware to restore the default network configuration.
For detailed steps, refer to: [Flashing](https://wiki.sipeed.com/hardware/en/kvm/NanoKVM/system/flashing.html).

### Method 2: If the SD card can be removed easily

If it is convenient to remove the SD card, connect it to your computer with a card reader, then delete the `eth.nodhcp` file in the first partition of the SD card.

### Method 3: If the SD card is not easy to remove (e.g., Cube users)

1. Use a SIM pin or other pointed tool, insert it into the small round hole next to the USB-C port (this is the Reset button), and press down.
2. Keep holding the button, then connect the device to your computer using a USB cable.
3. Wait until a USB storage device appears on your computer. After the `boot` volume shows up, release the pin.
4. Delete the `eth.nodhcp` file in that partition.
