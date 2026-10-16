# Slogic16U3 User Guide

👷‍♂️ This guide is under active development — thank you for your patience!

---

## Revision History

| Date       | Version | Author      | Description           |
|------------|---------|-------------|-----------------------|
| 2024-09-23 | v0.1    | Sipeed Team | Initial draft         |

---

## Table of Contents

1. [Overview](#overview)
2. [Specifications](#specifications)
3. [Hardware Connection](#hardware-connection)
4. [Software Installation](#software-installation)
5. [Software Usage](#software-usage)
6. [Build Software from Source](#build-software-from-source)
7. [Firmware Update](#firmware-update)
8. [FAQ](#faq)

---

## Overview

Slogic16U3 is a high-performance logic analyzer for digital signal debugging and analysis.

<div style="display: flex; flex-wrap: wrap; gap: 10px; width: 100%;">
  <img src="../../../en/logic_analyzer/slogic16u3/assets/DCIM/DSC07963.JPG" style="width: 100%;">
  <img src="../../../en/logic_analyzer/slogic16u3/assets/DCIM/DSC07962.JPG" style="width: calc(50% - 5px);">
  <img src="../../../en/logic_analyzer/slogic16u3/assets/DCIM/DSC07961.JPG" style="width: calc(50% - 5px);">
</div>

---

## Specifications

- **Channels:** 16
- **Max Sampling Rate:** 800 MHz
- **Memory Depth:** Unlimited
- **Interface:** USB 3.0 (5 Gbps)
- **Power Supply:** USB powered (5V 900mA)
- **Dimensions:** 150 × 100 × 30 mm

---

## Hardware Connection

- **USB-C to C** or **USB-A to C** cable:
    1. PC USB-A → USB-A/C to USB-C → SLogic
    2. PC USB-C → USB-C to USB-C → SLogic
- **Indicators:** Multi-color (see FAQ)
- **Accessories:** Standard Dupont wires, high-speed shielded wires

---

## Software

### Supported OS and Tested Platforms

| OS / Platform      | Supported | Example Platform           |
|--------------------|-----------|---------------------------|
| Windows (x86_64)   | Yes       | Ultra 5 125H              |
| Linux (x86_64)     | Yes       | 8th Gen Core i5+          |
| Linux (aarch64)    | Yes       | RPI5                      |
| macOS (aarch64)    | Yes       | Apple Silicon M4          |

### Supported Protocols

A wide range of protocols are supported, including:  
AC '97, I²C, SPI, UART, CAN, JTAG, 1-Wire, PWM, USB, and many more.  
*For the latest list, refer to the software's decoder selection panel.*

### Installation

#### Windows

- Extract the portable archive and double-click `pulseview.exe` to launch.

![](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-08_11-11-10.png)

- To enable debug mode, run in terminal:
```cmd
pulseview-debug.exe -l5
```

![](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-23_11-09-53.jpg)

#### Linux

```bash
chmod +x Pulseview.appimage
./Pulseview.appimage
# ./Pulseview.appimage -l5   # enable debug mode
```

![](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-08_11-24-12.png)
![](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-08_11-33-45.png)

#### macOS

- Download and open `Pulseview.dmg` to install.

![](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-18_11-11-57.jpg)
![](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-18_11-15-40.jpg)

**Related Links:**  
Taobao, AliExpress, MaixHub  
Email: support@sipeed.com

---

## Software Usage

- The interface and workflow are similar to DSView.
- Configure channels, sample rate, sample points/time, and other parameters as needed.
- Use the software to trigger, acquire, browse, measure, decode protocols, and manage files.

### Changing the Sample Depth

- The sample depth determines how many data points are captured per acquisition.
- You can set the sample depth in the main control panel, typically as either a number of points.
- Higher sample depth allows capturing longer or more detailed signal traces, but requires more memory and may take longer to transfer.
- If you only need to capture short events, reduce the sample depth for faster operation.
- Adjust the sample depth before starting acquisition to fit your analysis needs.
- **Sample depth is unlimited if you have a large enough disk; data can be streamed directly to storage.**

![unlimited sample depth](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-25_16-53-25.png)

### Changing the Sample Rate

- **Max sample rate:** 800 MHz (depends on active channels)
    - **16 channels:** up to 200 MHz
    - **8 channels:** up to 400 MHz
    - **4 channels:** up to 800 MHz
- Set the sample rate in the main control panel.
- If higher rates are unavailable, disable unused channels.

![200MHz max on 16ch](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-25_14-30-46.png)
![400MHz max on 8ch](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-25_14-31-04.png)
![800MHz max on 4ch](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-25_14-31-20.png)

### Selecting Active Channels

- Choose between **16**, **8**, or **4** channel configurations.
- Enable/disable channels in the configuration area.
- Fewer active channels allow higher sample rates.

![entry of channel selection](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-25_14-34-42.png)
![Channel count(pulseview modified)](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-25_14-35-03.png)
![Buffer size(default)](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-25_14-42-35.png)

### Adjusting Voltage Threshold

- Set threshold from **0.1V to 6.0V** in **0.1V steps**.
- Adjust in the channel/device configuration panel.
- Match threshold to your logic level (e.g., 1.0V for 3.3V CMOS).
- Apply changes before acquisition.

![entry of volt threshold selection](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-25_14-34-42.png)
![6V max](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-25_14-45-40.png)

Tip: For 3.3V CMOS/TTL, set threshold to ~1.0V (30% of 3.3V).

### Edge Trigger

- Configure edge trigger to start capture on a specific signal transition.
- In the trigger panel, select channel and trigger type (rising, falling, or both).

![](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-25_15-05-54.png)
![](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-25_15-06-48.png)

---

## Build Software from Source

The software is open source.

- [Sipeed's libsigrok GitHub Repository](https://github.com/sipeed/libsigrok/tree/slogic-dev)

**Recommended:** Use [sigrok-util](https://github.com/sigrokproject/sigrok-util) build scripts for a simple, cross-platform experience.

**Steps:**
1. Clone sigrok-util and follow its README for dependencies.
2. Edit the build script to use Sipeed's libsigrok fork:
    ```bash
    $GIT_CLONE https://github.com/sipeed/libsigrok -b slogic-dev
    ```
3. (Optional) Add options to speed up build and reduce size:
    ```
    --disable-all-drivers --enable-sipeed-slogic-analyzer --disable-bindings --enable-cxx
    ```
4. Run the build script for your target (e.g., `./sigrok-cross-linux`, `./sigrok-cross-mingw`, `./sigrok-cross-macosx`).

For advanced/manual builds, refer to upstream sigrok and PulseView documentation.

---

## Firmware Update

SLogic16U3 firmware is updated online with the web tool **[SLogic Firmware Update](https://slogic.sipeed.com/ota/)** (https://slogic.sipeed.com/ota/) — nothing to download or install.

- **Browser**: Chrome, Edge or another Chromium-based browser on a computer (updates use WebUSB, which Firefox and Safari do not support).
- **Driver**: no driver is needed on Windows. On Linux, run the following once to allow your user to access the analyzer, then re-plug it (the page shows it too):
  ```bash
  sudo tee /etc/udev/rules.d/60-slogic.rules >/dev/null <<'END'
  SUBSYSTEM=="usb", ATTRS{idVendor}=="359f", ATTRS{idProduct}=="0300|3031|3032|30f1|30f2", MODE="0666", TAG+="uaccess"
  END
  sudo udevadm control --reload-rules && sudo udevadm trigger
  ```
- **USB cable**: use a USB data cable plugged directly into the computer, not a charging-only cable or an unpowered hub.
- **Firmware downloads**: [SLogic16U3 firmware](https://dl.sipeed.com/shareURL/SLogic/SLogic16U3/4_Firmware) (`app.bin`); future updates are published here too.

**Update steps:**

1. Download the latest firmware file.
2. Open [https://slogic.sipeed.com/ota/](https://slogic.sipeed.com/ota/) in Chrome / Edge, connect the SLogic16U3 with a USB cable and click **Select device**.
3. Follow the page to enter update mode: press the **MODE** button on the device (see [Hardware Guide · MODE Button](./Hardware_Specification.md#MODE-Button)); the LED shows <span style="color:cyan">cyan</span> with a <span style="color:red">slow red blink</span>. Then select "*SLogic DFU*" in the browser dialog.
4. Choose the downloaded firmware file and click **Update firmware**. Keep the device connected and the page open until the update finishes.
5. When the update finishes, unplug the device and plug it back in to start the new firmware.

> In principle the update only replaces the SLogic firmware and never touches the **DFU** (update-mode) function. Even if an update fails, the device stays in update mode — keep it connected and run the update again.

See [Hardware Guide · Firmware Update](./Hardware_Specification.md#Firmware-Update) for more on browsers, drivers and firmware downloads.

---

## FAQ

### Why can't I find the SLogic16U3 device in Linux?

Normal users can't access USB devices by default.  
Run Pulseview with `sudo`:

```bash
sudo ./Pulseview.appimage
```

Or set up udev rules (see below).

### How do I set up udev rules for Linux?

Create a new udev rules file:

```bash
sudo tee /etc/udev/rules.d/60-sipeed.rules <<EOF
SUBSYSTEM!="usb|usb_device", GOTO="sipeed_rules_end"
ACTION!="add", GOTO="sipeed_rules_end"
ATTRS{idVendor}=="359f", MODE="0666", GROUP="plug_dev", TAG+="uaccess"
ENV{ID_MM_DEVICE_IGNORE}="1"
LABEL="sipeed_rules_end"
EOF
```

Reload udev rules and trigger:

```bash
sudo udevadm control --reload
sudo udevadm trigger
```

Unplug and reconnect the device.  
You can now run Pulseview as a normal user.

### Why can't I use higher sample rates? Only 200M shows.

The maximum sample rate depends on the number of active channels and USB bandwidth.  
Slogic16U3's USB 3.0 provides up to ~400MB/s.  
To use higher rates (400M/800M), disable unused channels.