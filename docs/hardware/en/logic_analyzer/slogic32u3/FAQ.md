<!--
Maintainer note (not rendered): SLogic32U3 FAQ scaffold.
Items to do are marked "TODO". Some entries were migrated from the SLogic16U3 FAQ and verified against the actual 32U3 (device name, VID, LED behavior, driver method, etc.).
Goal: categorized, "symptom → cause → fix" decision-style troubleshooting that also covers usage questions (which competitors' FAQs often miss).
-->
---
title: SLogic32U3 FAQ
keywords: SLogic32U3, FAQ, troubleshooting, udev, Zadig, 驱动, 采样率
update:
  - date: 2026-09-30
    version: v0.1
    author: Sipeed
    content:
      - Initialize FAQ scaffold
---

# SLogic32U3 FAQ

## Device and Connection

### Why is the SLogic32U3 device not found?

The most common cause is that the software was started before the device was connected. Fix: connect the device first, then start PulseView; or, inside the software, open "Connect to Device" → pick the driver → Scan → select the device.

On Linux, a normal user has no permission to access the USB device by default — see the udev rule below.

### What does a blue-only / red-only LED mean?

> The LED behavior matches SLogic16U3.

- **Blue only**: USB did not come up as USB3 — the cable isn't USB3-capable, it's plugged into a front-panel port / incompatible hub, insufficient power, or the cable is too long.
- **Red only**: a poor cable with excessive voltage drop, a faulty host USB port, or hardware damage.

## Drivers and Permissions

### Do I need to install a driver on Windows?

**No.** The SLogic32U3 is a WinUSB device by default — plug-and-play on Windows 10/11, no Zadig or manual driver install. Just plug it in and run PulseView or ngscopeclient.

### How do I set up udev rules on Linux?

> The SLogic series USB VID is `359f`.

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

> On Arch, use `GROUP="uucp"` instead. After that, replug the device and you can run as a normal user.

### Is macOS supported? Any extra configuration?

Yes. PulseView, ngscopeclient and sigrok-cli all ship macOS builds. If the first launch is blocked by the system, allow it in System Settings → Privacy & Security.

## Capture and Performance

### Why can't the sample rate go higher / why is it capped?

The maximum sample rate depends on the number of enabled channels and USB bandwidth — **disable unused channels** to raise the available sample rate. See [UG · Sample Rate Constraints](./UG.md#sample-rate-depth-and-channels).

### Which capture mode does the SLogic32U3 use?

The SLogic32U3 is **Stream mode**: real-time readback, effectively unlimited capture length (disk-bound), with an onboard 2Gbit (256MB) DDR elastic buffer and a sustained 6.4Gbps (800MB/s) bandwidth. The sample rate varies with the number of enabled channels: 4ch@1400MHz / 8ch@800MHz / 16ch@400MHz / 32ch@200MHz — enable only the channels you need to get a higher sample rate. See [UG · Stream Capture](./UG.md#stream-capture-and-sample-rates).

### What should I do about dropped samples?

- Lower the sample rate or reduce the number of enabled channels.
- Use a USB3 port directly on the motherboard + a high-quality short cable, and avoid unpowered hubs.

## Decoding

### Protocol decode results don't match?

Common causes: **wrong threshold / insufficient sample rate / wrong pin mapping**. Check each: threshold matches the DUT level, sample rate ≥ 10× the signal frequency, pin mapping correct (e.g. SPI's MOSI/MISO/SCLK/CS).

## Firmware and Modes

### The device is stuck in DFU mode and won't switch back to SLogic mode?

Usually the SLogic firmware is corrupted (a failed OTA). Fix: re-OTA the correct firmware.

### Can't enter DFU mode — it shows "unknown usb device"?

USB enumeration failed, usually due to a too-long or poor-quality cable. Fix: use a shorter, better-quality USB cable.

## ADC Oscilloscope Module

### How do I enable oscilloscope (analog) mode?

Enable it in the ngscopeclient UI (ngscopeclient is now a single-binary program, configured entirely in the UI with no command-line arguments). The 32U3 merges D0–7 / D8–15 / D16–23 / D24–31 into 4 × 8-bit analog channels A0–A3; requires an external ADC module. See [ngscopeclient](../ngscopeclient/ngscopeclient.md).

> 🚧 **TODO**: Add the exact UI steps to enable/switch analog mode in ngscopeclient.

### Can the ADC module be used together with digital capture?

> 🚧 **TODO**: Confirm and fill in.

---

> 🚧 **TODO**: Keep adding high-frequency "usage" questions from beta feedback (competitors' FAQs mostly cover only drivers/after-sales — this is our differentiator).
