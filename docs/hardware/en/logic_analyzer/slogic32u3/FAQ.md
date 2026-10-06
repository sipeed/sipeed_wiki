---
title: SLogic32U3 FAQ
keywords: SLogic32U3, FAQ, troubleshooting, udev, driver, sample rate, DFU
update:
  - date: 2026-10-06
    version: v0.2
    author: Sipeed
    content:
      - Updated internal links for the doc restructure
      - Corrected the buffer size and stream-rate wording
  - date: 2026-09-30
    version: v0.1
    author: Sipeed
    content:
      - Initialize doc
---

# FAQ

## Device and Connection

### Why is the SLogic32U3 not found?

The most common reason is that the software was launched before the device was connected.

Fix: connect the device first, then launch the host app; or inside the app open **Connect to Device** → choose the driver → **Scan** → select the device.

On Linux a normal user has no USB access by default and also needs a udev rule, see below.

### Blue only / red only — what's wrong?

- **Blue only**: USB is not connected as USB3. The cable may not support USB3, a front-panel or incompatible hub is in the way, power is insufficient, or the cable is too long.
- **Red only**: a Flash load error. Usually a poor cable causing excessive voltage drop, a faulty host USB port, or hardware damage.

In normal operation the indicator should be **cyan** (blue+green). For the full indicator guide see the [Hardware Guide](./Hardware_Specification.md#act-indicator).

## Drivers and Permissions

### Do I need a driver on Windows?

**No.** The SLogic32U3 is a WinUSB device by default; Windows 10/11 is plug and play, no Zadig or manual driver install. Just run SLogicView or ngscopeclient after plugging in.

### How do I set the Linux udev rule?

The SLogic series USB VID is `359f`.

```bash
sudo tee /etc/udev/rules.d/60-sipeed.rules <<EOF
SUBSYSTEM!="usb|usb_device", GOTO="sipeed_rules_end"
ACTION!="add", GOTO="sipeed_rules_end"
ATTRS{idVendor}=="359f", MODE="0666", GROUP="plugdev", TAG+="uaccess", ENV{ID_MM_DEVICE_IGNORE}="1"
LABEL="sipeed_rules_end"
EOF
sudo udevadm control --reload
sudo udevadm trigger
```

> On Arch, use `GROUP="uucp"` instead of `GROUP="plugdev"`. Replug the device once and you can run as a normal user.

### Is macOS supported? Any extra setup?

Yes. SLogicView, ngscopeclient and sigrok-cli all provide a macOS build. If the first launch is blocked, allow it under System Settings → Privacy & Security.

## Capture and Performance

### Why can't the sample rate go higher than a certain value?

The max sample rate depends on the number of channels enabled and the USB bandwidth. **Turn off unused channels** to raise the available rate.

The mapping: 4ch@1400MHz, 8ch@800MHz, 16ch@400MHz, 32ch@200MHz. See [Software Guide · Sample rate vs channel count](./Software_User_Guide.md#sample-rate-vs-channel-count).

### Which capture mode does the SLogic32U3 use?

**Stream mode**: data streams back to the host in real time, with capture length unlimited in theory, bounded only by disk. The onboard 2 Gbit DDR3 acts as an elastic buffer to smooth USB transfer, sustaining 800 MB/s (6.4 Gbps) in practice.

See [Software Guide · Stream capture](./Software_User_Guide.md#stream-capture).

### What if I get dropped samples?

- Lower the sample rate or reduce the channels enabled.
- Use a USB3 port directly on the motherboard with a good short cable; avoid unpowered hubs and front-panel ports.
- Close other high-traffic USB devices competing for bandwidth.

## Decoding

### The decode result doesn't match?

Three common causes, in order:

1. **Threshold set wrong**: match the threshold to the DUT logic level, about 1.6 V for 3.3 V logic.
2. **Sample rate too low**: take at least 10× the highest signal frequency.
3. **Pin mapping wrong**: confirm each decoder signal maps to the right channel, e.g. MOSI / MISO / SCLK / CS for SPI.

Empty output only means the current config produced no annotations, not that there is no traffic. Go back to the waveform and confirm the levels are changing.

## Firmware and Modes

### The device is stuck in DFU mode and won't return to SLogic mode?

Usually the SLogic firmware is corrupted, often from an interrupted OTA. Re-flash the correct firmware by OTA to recover.

### Can't enter DFU mode, it says "unknown usb device"?

USB enumeration failed, usually from a too-long or poor-quality cable. Use a shorter, better USB cable.

## ADC Oscilloscope Module

### How do I enable oscilloscope (analog) mode?

Enable it in the ngscopeclient UI. ngscopeclient is now a single binary, with everything configured in the UI and no command-line arguments.

Once enabled, the 32U3 merges D0–7 / D8–15 / D16–23 / D24–31 into 4 analog channels A0–A3 (8-bit); the optional ADC module is required. See [ngscopeclient](../ngscopeclient/ngscopeclient.md).
