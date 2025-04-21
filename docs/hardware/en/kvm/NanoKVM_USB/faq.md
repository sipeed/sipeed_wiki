---
title: F&Q
keywords: NanoKVM-USB, Lichee, PiKVM, RISCV, tool
---

## Exception Fixes

### No ttyUSBx Serial Device After Opening Web Page on Linux

+ This may be due to a missing serial driver. Please reinstall the CH34x driver using the following steps:

1. Download the driver from the WCH official website (download link: [https://www.wch.cn/download/CH341SER_LINUX_ZIP.html](https://www.wch.cn/download/CH341SER_LINUX_ZIP.html)), extract it, and navigate to the `driver` directory.
2. Run `uname -r` to check your operating system's release version. Find the corresponding version in (this link)[https://elixir.bootlin.com/linux/v6.2/source/drivers/usb/serial/ch341.c] and copy the content into `ch341.c`.
3. Execute the `make` command to compile the driver.
4. Run `sudo make load` to install the driver.
5. Replace the old driver: `cp ch341.ko /lib/modules/$(uname -r)/kernel/drivers/usb/serial/ch341.ko`.

+ Some Linux distributions come with `brltty`, a Braille display tool that occupies the `/dev/ttyUSB0` serial port, causing the webpage to be unable to detect it. If you are not using `brltty`, it is recommended to uninstall it with `sudo apt remove brltty`.

### Unable to Open NanoKVM-USB Corresponding Serial Device After Opening Web Page

+ This may be due to other programs occupying the serial port. Please ensure it is not in use before trying again.
+ Linux may lack permissions to open the serial port. Execute `sudo chmod 777 /dev/ttyUSB*` in the terminal.
+ The Chrome browser may not have detected the serial port. Please refresh the webpage or restart Chrome.
+ Chrome may lack sufficient permissions. Please grant the necessary permissions.

### DP-HDMI Adapter

+ Some passive DP to HDMI converters only perform level conversion in their internal circuitry, resulting in poor compatibility with NanoKVM-USB. This manifests as the video signal not appearing when waking from sleep; the NanoKVM-USB still shows a black screen, requiring manual unplugging and replugging of the HDMI cable.

### No HDMI Loop Out

+ The beta version hardware only supports USB power from the HOST side. Please ensure proper power supply from the HOST side during use.

### Loop Out Display

+ The NanoKVM-USB uses its own EDID (Extended Display Identification Data) before connecting to the loop-out display. After connecting to the loop-out display, it switches to the EDID of the loop-out display.
+ Since the EDID contains information about the display manufacturer and color settings, the resolution list in the Target system settings may appear different before and after connecting the loop-out display. Additionally, the color of the video captured via USB may vary before and after the connection.

### Other

+ If the above methods do not resolve the issue, please describe your purchased model and the encountered problem on the forum, GitHub, or QQ group, and we will respond patiently.

## Known Issues

### Latency:

+ The ARM version of macOS experiences increased latency when connected to a Raspberry Pi via NanoKVM-USB; other combinations are not affected.

## Feedback Methods

- [GitHub Issues](https://github.com/sipeed/NanoKVM)
- [MaixHub Forum](https://maixhub.com/discussion/nanokvm)
- QQ Group: 703230713