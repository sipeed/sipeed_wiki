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

1. Power off the device and keep the SD card inserted.
2. Locate the small round hole next to the HID (PC-USB) port. **The `BOOT` button sits inside the case, deeper and lower than the hole rather than directly behind its center**, so a pin pushed straight in and then pressed downward never reaches it.
3. Insert the pin all the way into the hole, then **use the edge of the hole as a fulcrum and lever the exposed end of the pin toward the top of the device**, so that the tip inside is pushed down onto the `BOOT` button. Use moderate force: you only need to feel the button being pressed. For the illustrated full procedure, see "USB Update TF Card Image" in [Flashing](https://wiki.sipeed.com/hardware/en/kvm/NanoKVM/system/flashing.html).
4. **Keep levering the pin upward without releasing it**, then plug one end of the USB cable into **the USB-C port next to the hole** (the HID port, below the HDMI port) and connect the other end to your computer.
5. Wait until a USB storage device appears on your computer. Release the pin only after the `boot` volume shows up.
6. Delete the `eth.nodhcp` file in that partition.
