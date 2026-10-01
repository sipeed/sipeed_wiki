<!--
Maintainer note (not rendered): SLogic32U3 User Guide scaffold (full feature reference).
Items to do are marked "TODO"; image placeholders are given as "> 🚧 **TODO (image)**" with a suggested asset name.
Some content was migrated from SLogic16U3 and verified against the actual 32U3 (channel count, interfaces, LED behavior, etc.).
If this page grows too long, it can be split into UG_Hardware.md + UG_Software.md, updating sidebar.yaml accordingly.
-->
---
title: SLogic32U3 User Guide
keywords: SLogic32U3, User Guide, PulseView, sigrok-cli, ngscopeclient, trigger, decoder, 信号完整性
update:
  - date: 2026-09-30
    version: v0.1
    author: Sipeed
    content:
      - Initialize User Guide scaffold (sections + known hardware facts + placeholders/TODO)
---

# SLogic32U3 User Guide

This guide is the full feature reference for the SLogic32U3, covering hardware, the three host front-ends, triggering, protocol decoding and signal integrity. For a quick start, read the [Quick Start](./QS.md) first.

---

## Hardware Details

### Interface Overview

> [!NOTE]
> **📷 Image TODO**: Front / back interface callout images — must label the 4 Mini-HDMI groups, USB-C, the MODE pinhole and the ACT LED.
> File: `assets/MISC/front.jpg`, `assets/MISC/rear.jpg`｜Requirements: front-on angle, ≥1000px wide, leave room around the connectors for callouts.

- **4 × Mini-HDMI channel groups**: The 32 channels are split into 4 groups of 8 (CH0–7 / CH8–15 / CH16–23 / CH24–31), brought out through coaxial shielded probe cables. Each Mini-HDMI (HDMI Type-C 1.4) port carries 8 data lines + GND + VCC(+5V) + CK; **the GND / VCC / CK of all 4 groups share a common source** (they are not independent per group).
- **USB-C**: USB3.2 Gen2; requires a USB3-capable cable and host port.
- **MODE button**: Switches between APP (logic analyzer) and DFU (firmware update) modes — see [MODE Button and DFU Mode](#mode-button-and-dfu-mode).
- **ACT LED**: See the [Status LED](#status-led) section.
- **CK**: 100MHz LVCMOS33 **fixed clock output** (not adjustable, output only).

### Channels and Probe Cables

> [!NOTE]
> **📷 Image TODO**: Mini-HDMI coaxial probe cable + test-clip wiring detail — must show each group's 8-color scheme.
> File: `assets/MISC/probe.jpg`｜Requirements: close-up, accurate color reproduction.

- The 32 channels are split into 4 groups, each group of 8 channels fed into **one Mini-HDMI** port.
- **Channel colors**: Each group's 8 channels are marked by the **Red / Orange / Yellow / Green / Brown / Blue / White / Gray** 8-color cycle.
- **Probe cables**: The front-end is a coaxial-cable daughter board (8 channels / 1 Mini-HDMI per board). Each signal runs over coax — the core = signal (digital input impedance ≈100kΩ), the shield = signal ground.
- **VCC**: The Mini-HDMI provides a +5V output (common across the 4 groups).

### Optional ADC Oscilloscope Module

The SLogic32U3 can take an optional 4-channel ADC module that **uploads the corresponding pin sampling as an 8-bit analog signal**, making the same device double as a sampling oscilloscope.

- Channels: 4
- Resolution: 8-bit
- Sample rate: 100 MSa/s
- Analog bandwidth: 20 MHz
- Safe input voltage: ±15V
- Input impedance: determined by the probe
- How to enable: configured in the ngscopeclient (single binary) UI; the 32U3 merges D0–7 / D8–15 / D16–23 / D24–31 into 4 × 8-bit analog channels A0–A3. See [ngscopeclient](../ngscopeclient/ngscopeclient.md). **(exact UI steps TBD)**

> [!NOTE]
> **📷 Image TODO**: Optional ADC module photo + oscilloscope-mode waveform screenshot.
> File: `assets/DCIM/adc-module.jpg` (physical photo, from a colleague), `assets/Screenshots/scope-mode.png` (software screenshot, captured on real hardware).

### Status LED

> The LED behavior matches SLogic16U3. The indicator is a 3-color RGB: **Blue = power, Green = USB LINK, Red = run status**.

> [!NOTE]
> **📷 Image TODO**: ACT LED location and states — a few shots for normal connection / capturing / DFU.
> File: `assets/MISC/act-led.jpg`｜Requirements: shoot in a dark environment to bring out the LED colors.

| State | Color | Notes |
| - | - | - |
| Normal connection | Cyan (blue+green) | Powered and USB connected |
| Data transfer | Cyan + fast red blink | Capturing |
| DFU mode | Cyan + slow red blink | Firmware update mode |
| USB connection failed | Blue only | Often a non-USB3 cable/port |
| Flash load error | Red only | Excessive cable voltage drop / hardware issue |

### MODE Button and DFU Mode

**The MODE button is a hidden pinhole button** (same as 16U3 — press it with a SIM pin), used to switch between APP (SLogic logic analyzer) and DFU (firmware update) modes. It powers up in APP mode by default; press MODE to switch to DFU mode, after which you can flash firmware (see [Firmware Update](#firmware-update)).

When switched to DFU mode the LED is a **slow red blink** (same as 16U3).

### Firmware Update

> Firmware update tool: [slogic16u3-tools releases](https://github.com/sipeed/slogic16u3-tools/releases/latest) (shared toolchain with SLogic16U3). SLogic32U3 firmware is not yet released; it will be provided on the [download site](https://dl.sipeed.com/shareURL/SLogic) once officially released.

1. Enter DFU mode (press MODE, wait for the slow red blink).
2. Confirm a "SLogic DFU" device appears.
3. Flash the firmware with the tool from [slogic16u3-tools](https://github.com/sipeed/slogic16u3-tools/releases/latest) (the command looks like `spi_flash_xxx <firmware_path>`).

### Probing and Signal Integrity

> This section is key for a high-speed logic analyzer; consider fleshing it out as a tutorial (cf. Saleae's probe/grounding guides).

- **Grounding is critical**: at low frequencies and low channel counts a single ground can be shared; as frequency/channel count rises, ground-lead inductance produces a voltage drop on the ground that degrades the measurement — **at high speed, run a ground close to each signal wire**.
- **Never tie a ground to a signal line** (it can damage the device).
- **Threshold voltage**: set it to the DUT logic level (e.g. ~1.6V for 3.3V logic). When unsure, measure with a multimeter/oscilloscope first.
- **Input range 0~10V**; confirm the hardware limits before exceeding it.
- Mini-HDMI shielded cables suit high-speed signals better than jumper wires.

> 🚧 **TODO (image)**: Good/bad grounding comparison (waveforms under good vs. bad grounding). Suggested: `assets/MISC/grounding-good-bad.png`

### Safety and Precautions

- **VCC**: the Mini-HDMI provides a +5V output (common across the 4 groups); **never short it to GND**.
- When used with a mains-powered computer, the probe ground is tied to the computer ground; connect the ground only to equipotential ground points, and **never to a hot ground**.

### Drivers and Installation

#### Windows: Driverless (WinUSB)

The SLogic32U3 is a WinUSB device by default — plug-and-play on Windows 10/11, **no Zadig, no manual driver install** — a usability edge over some sigrok-ecosystem competitors. Just plug it in and run PulseView or ngscopeclient.

> The native Windows build of PulseView has **no software-level bandwidth/sample-rate cap**; the achievable rate depends only on the physical machine's performance (unlike the throttling of early SLogic16U3 native Windows exe builds).

#### Linux udev Rules

A normal user has no permission to access the USB device by default, so install a udev rule once (device VID is `359f`):

```bash
sudo tee /etc/udev/rules.d/60-sipeed.rules <<'EOF'
SUBSYSTEM!="usb|usb_device", GOTO="sipeed_rules_end"
ACTION!="add", GOTO="sipeed_rules_end"
ATTRS{idVendor}=="359f", MODE="0666", GROUP="plugdev", TAG+="uaccess", ENV{ID_MM_DEVICE_IGNORE}="1"
LABEL="sipeed_rules_end"
EOF
sudo udevadm control --reload && sudo udevadm trigger
```

> On Arch, change `GROUP="plugdev"` to `GROUP="uucp"`. After installing, replug the device once so the rule takes effect.

#### macOS

macOS is supported. PulseView, ngscopeclient and sigrok-cli all ship macOS builds; if the first launch is blocked by the system, allow it in System Settings → Privacy & Security.

---

## Software — PulseView (sigrok)

### Connecting and Device Detection

Best practice: connect the device to a USB3 port first, then start PulseView so it auto-detects on launch. If it is already running, use "Connect to Device" → pick the driver → Scan → select the device.

> 🚧 **TODO (image)**: Connect dialog screenshot. Suggested: `assets/Screenshots/pv-connect.png`

### Stream Capture and Sample Rates

The SLogic32U3 uses **Stream mode**: data is read back to the host in real time, so capture length is effectively unlimited (disk-bound), with an onboard **2Gbit (256MB) DDR** elastic buffer smoothing the USB transfer. Sustained bandwidth reaches **6.4Gbps (800MB/s)**.

Maximum sample rate at each channel count (bounded by bandwidth or the top sampling clock):

| Enabled channels | Max sample rate | Data rate |
|---|---|---|
| 4ch | 1400 MHz | 5.6 Gbps |
| 8ch | 800 MHz | 6.4 Gbps |
| 16ch | 400 MHz | 6.4 Gbps |
| 32ch | 200 MHz | 6.4 Gbps |

> 8 / 16 / 32ch all saturate the 6.4Gbps (800MB/s) bandwidth limit; 4ch is bounded by the 1400MHz top sampling clock (5.6Gbps). **Fewer enabled channels → higher available sample rate**, so enable only the channels this capture needs.

> **vs USB3.0 competitors**: the DreamSourceLab DSLogic U3Pro32 (USB3.0) does about 16ch@125MHz and 32ch@50MHz in Stream mode (per its public datasheet); the SLogic32U3 does 16ch@400MHz and 32ch@200MHz — roughly 3~4× the Stream sample rate.

### Sample Rate, Depth and Channels

- The more channels enabled, the lower the available sample rate (bounded by USB throughput).
- **How to pick a sample rate** (decision-based): as a rule of thumb take ≥10× the highest signal frequency; too low misses edges, too high may capture glitches.
- Sample rate × depth determines memory/disk usage — check free disk space before a long capture.

> 🚧 **TODO (image)**: Sample-rate/channel presets panel; waveform comparison of too-high vs too-low sample rate. Suggested: `assets/Screenshots/samplerate-presets.png`, `assets/Screenshots/samplerate-compare.png`

### Triggers

The SLogic32U3 supports **multi-channel, multi-edge combination triggers** (configured in PulseView / sigrok-cli): you can set rising / falling / any-edge / level conditions on several channels and combine them.

> ⚠️ **The ngscopeclient integration currently supports single-channel, single-edge triggers only** — for multi-channel / multi-edge combinations, use PulseView or sigrok-cli instead.

- **Pre-trigger**: supported — you can set how many samples to retain before the trigger point in the UI.

> 🚧 **TODO**: Add 1~2 trigger examples per common bus (e.g. UART start bit, I²C start condition).

> 🚧 **TODO (image)**: Trigger settings panel. Suggested: `assets/Screenshots/trigger.png`

### Navigation and Cursor Measurement

- Zoom: scroll wheel; pan: drag or Shift+scroll; vertical pan: Ctrl+scroll.
- Use cursors to measure time differences and derive baud rate / pulse width / event intervals (Shift+drag to create measurement cursors).

> 🚧 **TODO (image)**: Cursor measurement example. Suggested: `assets/Screenshots/cursors.png`

### Protocol Decoding

1. Open the Decoder panel and pick a protocol (I2C/SPI/UART/CAN/SDIO…).
2. Configure pin mapping, bit order, clock polarity/phase, baud/clock rate.
3. Decoded frames are annotated on the waveform and clickable for details; decoder stacking is supported.

**Common decode failures**: wrong threshold, insufficient sample rate, wrong pin mapping.

> 🚧 **TODO**: Add a measured 32U3 example per common protocol (wiring + trigger + decode-result screenshot).
> Suggested one subsection per protocol: `UART` / `I2C` / `SPI` / `CAN` / `SDIO`.

### File Operations

- Save session: stores samples, channel configuration, trigger and decoder state.
- Export: CSV / VCD, etc.; import existing `.sr` waveforms.

---

## Software — ngscopeclient

The SLogic32U3 is a key supported model in the ngscopeclient distribution. For full install and connection see the [ngscopeclient getting-started guide](../ngscopeclient/ngscopeclient.md).

This section only covers what is 32U3-specific (full install/connection on the shared page):

- **Single binary, all-UI configuration**: ngscopeclient is now a single executable — just run it; connection, capture mode and parameters are all set in the UI, with no separate background program or command-line arguments.
- **Connect the device**: add/select the SLogic device in the ngscopeclient UI; once connected, the channel panel shows **32** channels.
- **Filter Graph**: ngscopeclient unifies protocol decoding/math/measurement as Filter nodes chained into a processing graph.
- **ADC analog mode**: once enabled in the UI, digital pins are merged into 4 × 8-bit analog channels A0–A3 and viewed like a sampling oscilloscope (range/axes/FFT etc. available automatically). Requires an external ADC module.

> 🚧 **TODO**: Add the actual connection steps for the single-binary ngscopeclient and the exact UI steps to enable analog mode. The shared [ngscopeclient](../ngscopeclient/ngscopeclient.md) page still describes the old sigrok-bridge architecture and needs to be updated in sync.

> 🚧 **TODO (image)**: 32U3 waveform/decoding in ngscopeclient. Suggested: `assets/Screenshots/ngscope-32u3.png`

---

## Command Line — sigrok-cli

For automation, CI and headless capture.

Sipeed ships a per-platform SLogic build of `sigrok-cli`: `sigrok-cli-SLogic-xxxx.{AppImage,exe,dmg}` ([GitHub Release](https://github.com/sipeed/SLogic/releases/latest), download site is a backup mirror). The libsigrok driver name is `sipeed-slogic-analyzer`.

```bash
sigrok-cli --scan                                   # scan devices
sigrok-cli -d sipeed-slogic-analyzer --show         # show device capabilities
sigrok-cli -d sipeed-slogic-analyzer \              # capture: enable D0 only, 10MHz, 500k samples
  --config samplerate=10m -C D0 \
  --samples 500k -o capture.sr
sigrok-cli -i capture.sr -P uart:rx=D0:baudrate=115200 -A uart   # decode
```

> Capture time (s) = samples ÷ sample rate. To let an AI Agent run scan/capture/decode, see [SLogic AI Agent Integration](../slogic_agent/readme.md).
> 🚧 **TODO**: Add a complete end-to-end script example (scan → capture → decode → export CSV), and verify the exact driver-name spelling in the released `sigrok-cli`.

---

## AI Agent Integration

With `sigrok-cli-slogic-plugin`, you don't need to learn PulseView — just tell the Agent your channels and target protocol and it will scan/capture/decode automatically. For the full tutorial see [SLogic AI Agent Integration](../slogic_agent/readme.md).

---

## Real-World Constraints and Known Issues

> Following sigrok's "Known Issues" culture — state limitations honestly to build trust.

> 🚧 **TODO**: Flesh this section out as testing proceeds. Candidate items:

- Combination limits of sample rate × channel count × depth (which combinations are unavailable).
- Trigger limitations in Stream mode.
- Whether the ADC module can be used together with digital capture.
