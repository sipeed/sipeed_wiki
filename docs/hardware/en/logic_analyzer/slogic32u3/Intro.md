<!--
Maintainer note (not rendered to the site):
This page is a draft scaffold of the SLogic32U3 docs. All content still to be filled is marked with the literal token "TODO",
trackable via `grep -rn TODO docs/hardware/en/logic_analyzer/slogic32u3`.
Image placeholders are given as "> 🚧 **TODO (image)**" with a suggested asset filename (under ./assets/).
Specs marked "(TBD)" need final confirmation from hardware/R&D before the marker is removed.
-->
---
title: SLogic32U3 Introduction
keywords: LogicAnalyzer, SLogic, SLogic32U3, USB3.2, 10Gbps, sigrok, PulseView, ngscopeclient
update:
  - date: 2026-09-30
    version: v0.1
    author: Sipeed
    content:
      - Initialize doc scaffold (known specs with placeholder/TODO items)
---

# SLogic32U3 Introduction: The World's First 10Gbps USB3.2 Logic Analyzer

The SLogic32U3 is the flagship logic analyzer of the Sipeed SLogic series. Housed in an aluminum enclosure, it delivers 32-channel high-speed Stream capture over a USB3.2 Gen2 (10Gbps line rate) interface at a steady 6.4Gbps (800MB/s): 1400M@4CH, 800M@8CH, 400M@16CH, 200M@32CH. Digital inputs accept a 0~10V range with a 0~6V adjustable threshold, and an optional 4-channel ADC module gives the same device sampling-oscilloscope capability. On the software side it works with sigrok/PulseView, ngscopeclient and sigrok-cli, and can be driven by an AI Agent for automated capture and decoding.

<div style="text-align:center;">
  <img src="../../../zh/logic_analyzer/slogic32u3/assets/SLogic32U3-photo.jpg" alt="SLogic32U3" style="max-width:100%;">
</div>

> [!NOTE]
> **📷 Image TODO**: Hero product shot — a clear photo of the front showing the 4×Mini-HDMI + USB-C side.
> File: `assets/DCIM/SLogic32U3-hero.jpg`｜Requirements: landscape, ≥1000px wide, light background, no obvious glare on the body. Currently using `SLogic32U3-photo.jpg` as a placeholder.

---

## Key Features

1. **10Gbps USB3.2 Gen2**: The world's first USB3.2 Gen2 logic analyzer. **Stream mode sustains 6.4Gbps (800MB/s)**, backed by an onboard 2Gbit DDR elastic buffer, keeping high sample rates even at high channel counts (see the spec table below for each tier).
2. **32 channels / up to 1400MSa/s**: 1400M@4CH, 800M@8CH, 400M@16CH, 200M@32CH, covering everything from single-bus debugging to multi-lane parallel bus analysis.
3. **Adjustable threshold + wide input range**: 0~10V digital input, 0~6V adjustable logic threshold, matching 1.2V/1.8V/3.3V/5V and other logic levels.
4. **Mini-HDMI shielded probes**: The 32 channels are split into 4 groups of 8, each group routed through one Mini-HDMI connector and marked by an 8-color cycle (Red/Orange/Yellow/Green/Brown/Blue/White/Gray), balancing high-speed signal integrity with wiring convenience.
5. **Optional ADC → oscilloscope**: An optional 4-channel ADC module (8-bit, 100 MSa/s, 20 MHz analog bandwidth, ±15V safe input) turns the same device into a sampling oscilloscope for mixed-signal observation. Enabled in the ngscopeclient UI.
6. **Multiple front-ends + portable, no install**: Choose PulseView (sigrok), ngscopeclient or sigrok-cli — no system-level installation, plug and play.
7. **AI Agent integration**: With `sigrok-cli-slogic-plugin`, just tell the Agent your channels and target protocol and it will scan, capture `.sr` waveforms and decode automatically. See [SLogic AI Agent Integration](../slogic_agent/readme.md).

---

## Technical Specifications

| Item | Specification |
| :--- | :--- |
| Digital channels | 32 |
| Max sample rate | 1400 MSa/s (4CH) |
| Sample-rate / channel tiers | 1400M@4CH · 800M@8CH · 400M@16CH · 200M@32CH |
| USB interface | USB3.2 Gen2 (10Gbps line rate, steady 6.4Gbps / 800MB/s) |
| Capture mode | Stream (streaming, real-time readback); onboard 2Gbit (256MB) DDR elastic buffer |
| Input voltage range | 0 ~ 10V |
| Adjustable threshold (Vth) | 0 ~ 6V, 0.1V steps (below Vth = 0, above = 1) |
| Input impedance | 100 kΩ (digital input) |
| Min capturable pulse width | ≈0.71 ns (1/1400MHz, counted as 1 sample interval) |
| Trigger | Multi-channel / multi-edge combinations (PulseView, sigrok-cli); the ngscopeclient integration is currently single-channel single-edge only |
| Capture depth | Stream effectively unlimited (disk-bound), onboard 2Gbit (256MB) DDR elastic buffer |
| Optional ADC module | 4 channels, 8-bit, 100 MSa/s, 20 MHz analog bandwidth, ±15V safe input, input impedance determined by the probe |
| Interface / connectors | 4 × Mini-HDMI (HDMI Type-C 1.4, 8 channels per port, coaxial shielded) + USB-C |
| Power | USB powered, rated 5V @ 65mA |
| Enclosure / dimensions | Aluminum, 50 × 50 × 10 mm |
| Supported OS | Windows 10/11 x64, Linux x86_64, macOS |
| Pricing | See the crowdfunding page (currently crowdfunding only) |

---

## SLogic Series Comparison

| Attribute | SLogic Combo8 | SLogic16U3 | SLogic32U3 |
| - | - | - | - |
| USB type | USB2.0 | USB3.0 | USB3.2 Gen2 |
| Max sample rate | 80M | 800M | 1400M |
| Max channels | 8 | 16 | 32 |
| Max bandwidth | 0.3Gbps | 3.2Gbps | 6.4Gbps |
| Typical comb. (stream) | 80M@4CH, 40M@8CH | 800M@4CH, 400M@8CH, 200M@16CH | 1400M@4CH, 800M@8CH, 400M@16CH, 200M@32CH |
| Sigrok compatible | Y | Y | Y |
| Adjustable threshold | N | Y | Y |
| Enclosure | Plastic | Aluminum | Aluminum |
| Extras | DAP-Link, CK-Link, 4-UART | | Optional ADC → oscilloscope |
| Dimensions | 20x40x10mm | 40x40x10mm | 50x50x10mm |
| Price | ￥69 | ￥369 | See crowdfunding page |

---

## Ecosystem Compatibility

The SLogic32U3 offers 4 ways to use it — pick as needed:

| Front-end | Role | Best for |
| - | - | - |
| **PulseView (sigrok)** | The most common GUI | Everyday capture, protocol decoding, fastest to pick up |
| **ngscopeclient** | GPU-accelerated, Filter Graph, mixed-signal | Advanced analysis, ADC oscilloscope mode |
| **sigrok-cli** | Command line | Automation / CI / headless capture |
| **AI Agent** | Natural-language driven | Let the Agent run scan/capture/decode for you |

> For detailed usage see the [User Guide](./UG.md), [ngscopeclient](../ngscopeclient/ngscopeclient.md) and [SLogic AI Agent Integration](../slogic_agent/readme.md).

---

## Software Downloads

Get the latest multi-platform host software from **GitHub Release**; the download site is a backup mirror.

- **GitHub Release (recommended, latest)**: https://github.com/sipeed/SLogic/releases/latest
- Download site (backup mirror): https://dl.sipeed.com/shareURL/SLogic
- SLogic build of sigrok-cli (command line): `sigrok-cli-SLogic-xxxx.{AppImage,exe,dmg}`
- AI Agent Plugin: `https://dl.sipeed.com/fileList/SLogic/sigrok-cli-slogic-plugin.zip`
- Source code (libsigrok, slogic-dev branch): https://github.com/sipeed/libsigrok/tree/slogic-dev
- libsigrok driver name: `sipeed-slogic-analyzer`
- Firmware update tool: https://github.com/sipeed/slogic16u3-tools/releases/latest (shared with SLogic16U3; SLogic32U3 firmware is not yet released and will be provided on the download site once officially released)

---

## Related Links

- Buy (crowdfunding): https://www.kickstarter.com/projects/zepan/slogic32u3-the-worlds-first-10gbps-usb32-logic-analyzer/
- Retail (Taobao / AliExpress): crowdfunding only for now; retail not yet open
- MaixHub discussion: [maixhub.com](https://maixhub.com/discussion/slogic)
- Support email: support@sipeed.com
- Sipeed GitHub: https://github.com/sipeed
- Community (Discord): [discord.gg/V4sAZ9XWpN](https://discord.gg/V4sAZ9XWpN)
