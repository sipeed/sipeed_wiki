# Introduction

---

## Introduction
SLogic16U3 is the next-generation USB3 logic analyzer. In a compact 40×40×10 mm enclosure it achieves high sampling: 800M@4CH, 400M@8CH, 200M@16CH over a 5Gbps USB3 interface. It supports software (soft) trigger and configurable voltage threshold for all channel. Starting at $69.

![SLogic16U3 product](../../../en/logic_analyzer/slogic16u3/assets/DCIM/SLogic16U3.png)

---

## Features & Specifications
| Attribute | SLogic Combo8 | SLogic16U3 | SLogic32U3 |
| - | - | - | - |
| Model | SLogic Combo8 | SLogic16U3 | SLogic32U3 |
| USB Type | USB2.0 | USB3.0 | USB3.2 Gen2 |
| Max Sample Rate | 80M | 800M | 1500M |
| Max Channels | 8 | 16 | 32 |
| Max Bandwidth | 0.3Gbps | 3.2Gbps | 6.4Gbps |
| Typical Comb. (stream, unlimited) | 80M@4CH, 40M@8CH | 800M@4CH, 400M@8CH, 200M@16CH | 1500M@4CH, 800M@8CH, 400M@16CH, 200M@32CH |
| Sigrok Compatible | Y | Y | Y |
| Adjustable Threshold | N | Y | Y |
| Case | Plastic | Aluminum | Aluminum |
| Extra Feature | DAP-Link, CK-Link, 4-UART |  | Extend ADC -> Oscilloscope |
| Size | 20x40x10mm | 40x40x10mm | 50x50x10mm |
| Price | $15 | $69 | $149 |

---

## Product Images

- size: 40x40x10mm
- view: top/front/back
<div style="display: flex; flex-wrap: wrap; gap: 10px; width: 100%;">
  <img src="../../../en/logic_analyzer/slogic16u3/assets/DCIM/DSC07963.png" style="width: 100%;">
  <img src="../../../en/logic_analyzer/slogic16u3/assets/DCIM/DSC07962.png" style="width: calc(50% - 5px);">
  <img src="../../../en/logic_analyzer/slogic16u3/assets/DCIM/DSC07961.png" style="width: calc(50% - 5px);">
  <img src="../../../zh/logic_analyzer/slogic16u3/assets/MISC/la_frontview.jpg" style="width: calc(50% - 5px);">
  <img src="../../../zh/logic_analyzer/slogic16u3/assets/MISC/la_rearview.jpg" style="width: calc(50% - 5px);">
</div>

---

## Software installation

### Supported OS
![](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/supported-platforms.png)
- Windows 10/11 (x86_64)
  - Due to the conservative Windows driver, it cannot reach full speed; the native .exe version must run throttled (maximum supported 200M@8CH).
  - Additionally, it can run at full speed in a Linux virtual machine.
  - ![](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-27_11-05-12.png)
- Linux (x86_64, aarch64)
- macOS (Apple Silicon M4)
- Raspberry Pi 5
  - ![](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-27_11-55-18.png)

### Downloads
- Binary downloads: https://dl.sipeed.com/shareURL/SLogic
- Source code (slogic-dev branch): https://github.com/sipeed/libsigrok/tree/slogic-dev

#### Windows

- Extract the portable archive and double-click `pulseview.exe` to launch.
- To enable debug mode, run in terminal:
```cmd
pulseview-debug.exe -l5
```

![](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-23_11-09-53.png)

#### Linux

```bash
chmod +x Pulseview.appimage
./Pulseview.appimage
# ./Pulseview.appimage -l5   # enable debug mode
```

![](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-26_19-12-07.png)

#### macOS

- Download and open `Pulseview.dmg` to run directly.

![](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-18_11-11-57.png)


---

## Related links
- Buy (Taobao): http://addme
- Buy (AliExpress): http://addme
- MaixHub: [maixhub.com](https://maixhub.com/discussion/slogic)
- Support email: support@sipeed.com
- GitHub (libsigrok slogic-dev): https://github.com/sipeed/libsigrok/tree/slogic-dev
- Sipeed GitHub: https://github.com/sipeed
- GitHub (SLogic16U3 Tools): https://github.com/sipeed/slogic16u3-tools
- Community (Discord): https://discord.com/channels/1359800784375644291/1359802057569206323
