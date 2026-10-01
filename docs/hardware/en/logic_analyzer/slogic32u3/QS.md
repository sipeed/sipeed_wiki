<!--
Maintainer note (not rendered): SLogic32U3 Quick Start scaffold.
Items to do are marked "TODO"; image placeholders are given as "> 🚧 **TODO (image)**".
Goal: a verb-driven 5-minute loop — unbox → install software → install driver → wiring → first capture → view results.
In-depth content always links out to UG.md and is not expanded here.
-->
---
title: SLogic32U3 Quick Start
keywords: SLogic32U3, Quick Start, PulseView, sigrok, 上手
update:
  - date: 2026-09-30
    version: v0.1
    author: Sipeed
    content:
      - Initialize Quick Start scaffold
---

# SLogic32U3 Quick Start

This page takes the shortest path to your first capture. For in-depth configuration, principles and the full feature set see the [User Guide](./UG.md); for problems see the [FAQ](./FAQ.md).

## Unboxing

> [!NOTE]
> **📷 Image TODO**: Unboxing group shot (shoot after the accessory list is finalized).
> File: `assets/DCIM/unboxing.jpg`｜Requirements: top-down flat lay with all accessories in frame.

A complete hardware set includes the **SLogic32U3 main unit** and the following accessories:

> 🚧 **TODO**: Confirm the final accessory list and quantities (the table below is a placeholder — correct it against the actual product).

- SLogic32U3 main unit × 1
- Mini-HDMI shielded probe cable × **(TBD)** (for the 4 channel groups)
- Logic analyzer test clips × **(TBD)**
- USB-C data cable (USB3-rated) × 1
- Optional: ADC oscilloscope module × **(TBD)**
- **(TBD: SIM pin / instruction card / storage pouch, etc.)**

## Install the Software (PulseView)

The SLogic32U3 uses portable, no-install software. Download the latest build for your platform from [GitHub Release](https://github.com/sipeed/SLogic/releases/latest) (the download site is a backup mirror; see [Intro · Software Downloads](./Intro.md#software-downloads)).

| Platform | Action |
| - | - |
| Windows 10/11 | Unzip the portable package and double-click `pulseview.exe` |
| Linux x86_64 | `chmod +x Pulseview.appimage && ./Pulseview.appimage` |
| macOS | Open `Pulseview.dmg` and run it directly |

> 🚧 **TODO (image)**: One software-launch screenshot per platform. Suggested: `assets/Screenshots/pv-win.png` / `pv-linux.png` / `pv-macos.png`

## Install Driver / Configure Permissions

Each platform needs a one-time setup on first use, otherwise the software may not find the device.

- **Windows**: **Driverless** — the SLogic is a WinUSB device by default, plug-and-play on Windows 10/11, no Zadig needed. See [UG · Drivers and Installation](./UG.md#drivers-and-installation).
- **Linux**: Install a udev rule (device VID `359f`), otherwise a normal user has no permission to access the USB device. See [UG · Linux udev Rules](./UG.md#linux-udev-rules).
- **macOS**: Supported; if the first launch is blocked by the system, allow it in System Settings → Privacy & Security.

## Wiring and Grounding

> 🚧 **TODO (image)**: Wiring diagram (Mini-HDMI probe orientation + signal/GND mapping). Suggested: `assets/MISC/wiring.jpg`

1. Connect the SLogic32U3 directly to a **USB3** port on the computer with the USB-C cable (avoid unpowered hubs / front-panel ports).
2. Plug the Mini-HDMI shielded probe cable into the matching channel group (Mini-HDMI is keyed and only fits one way); at the probe tip, each group's 8 signals are distinguished by the Red/Orange/Yellow/Green/Brown/Blue/White/Gray 8-color cycle.
3. Connect the signal under test to any free **CH**, and **be sure to tie the DUT's GND to the SLogic's GND**.
4. For high-speed signals, **run a ground close to each signal wire** — see [UG · Probing and Signal Integrity](./UG.md#probing-and-signal-integrity).

## First Capture (UART Example)

Using a 115200 8N1 UART as an example:

1. Connect the device and start PulseView; confirm it is auto-detected (if not, see [FAQ](./FAQ.md#why-is-the-slogic32u3-device-not-found)).
2. Enable only the channels you need (e.g. D0) and disable the rest to leave bandwidth headroom.
3. Set the **voltage threshold** to match the DUT level (e.g. ~1.6V for 3.3V logic).
4. Choose a suitable **sample rate** (rule of thumb: ≥10× the highest signal frequency; 10M is plenty for this 115200 UART example).
5. Click capture.

> 🚧 **TODO (image)**: The capture-settings panel + the captured waveform, one each. Suggested: `assets/Screenshots/qs-capture-cfg.png` / `qs-uart-wave.png`

## View Results and Decode

1. Open the Decoder panel and add the **UART** decoder.
2. Configure the pin mapping (RX/TX), baud rate 115200, 8N1.
3. The decoded characters are annotated on the waveform.

> 🚧 **TODO (image)**: UART decode annotations. Suggested: `assets/Screenshots/qs-uart-decode.png`

---

## Next Steps

- To dig into capture modes / triggers / more protocols: [User Guide](./UG.md)
- For the GPU-accelerated UI or ADC oscilloscope mode: [ngscopeclient](../ngscopeclient/ngscopeclient.md)
- To let AI run capture and decoding for you: [SLogic AI Agent Integration](../slogic_agent/readme.md)
- Having problems: [FAQ](./FAQ.md)
