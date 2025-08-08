## Introduction

**Taobao link: [Click to Buy](https://item.taobao.com/item.htm?spm=1619a.1.0.0.3f0865abb4Wq5c&id=744014549573&ns=1&abbucket=18#detail)**

The M4N-Dock is an edge computing box featuring hybrid-precision computing capabilities, developed by Sipeed and powered by AXERA's third-generation high-efficiency AI vision chip, the AX650N. It delivers an impressive 72 TOPS@INT4 or 18 TOPS@INT8 of built-in AI computing power, capable of running popular large-scale AI models.

Equipped with an advanced ISP supporting 8K@30fps video processing and AXERA's proprietary AI-ISP technology for superior low-light night vision performance, it also integrates H.264/H.265 codecs capable of stable 8K@60fps decoding and 8K@30fps encoding. Real-world testing demonstrates reliable 32-channel 1080P@30fps decoding and 16-channel 1080P@30fps encoding.

The AX650N chip features comprehensive interfaces including 64-bit LPDDR4x memory, multi-channel MIPI input, Gigabit Ethernet, USB 3.0, and HDMI 2.0b output. Combining powerful computing with exceptional codec capabilities, it meets industry demands for high-performance edge AI computing.

The single-core NPU delivers outstanding performance (single-core performance), achieving:

- 130 FPS (7.66ms latency) for yolov5s at 640×640 resolution

- 1798 FPS (0.556ms latency) for MobileNetV2 at 224×224 resolution

Supporting diverse deep learning algorithms, it enables applications including visual structuring, behavior analysis, and status detection, with optimized support for Transformer architectures and large vision models. Comprehensive development documentation facilitates secondary development for customized solutions.


## Key Specifications

| Component | Description                                                                          |
|-----------|--------------------------------------------------------------------------------------|
| CPU       | 8x A55@1.7Ghz, integrated FPU, supports NEON acceleration                            |
| NPU       | 72 TOPS@INT4 / 18 TOPS@INT8, supporting INT4/INT8/INT16/FP16/FP32 inputs, TopN (N<=32) |
| ISP       | Supports up to 8192x4320@30fps, maximum resolution: 16384x16384, featuring AI-ISP (low-light night vision)   |
| CODEC     | H.264/H.265 encoding/decoding, up to 8K@60fps decoding & 8K@30fps encoding capability |
| DSP       | Dual-core 800MHz                                                                     |
| Memory    | 8GB 64-bit LPDDR4x (adjustable allocation: default 2GB system + 6GB AI CMM)          |
| Storage   | 32GB eMMC 5.1 onboard (system storage) plus 3x SATA 3.0 6Gb/s (1× M.2 + 2× standard SATA ports)  |
| Video Output | Dual HDMI 2.0a (4K@60fps max)                                                     |
| Video  Input | Dual 4-lane MIPI-CSI camera interfaces (3.5Gbps)                                  |
| Network      | Dual Gigabit Ethernet ports (tested throughput: 944Mbps)                          |
| PCIE         | 1-lane PCIe 2.0 (5Gbps) via Mini-PCIe interface                                   |
| USB          | 1× USB3.2 Gen1 (5Gbps) + 3× USB2.0 (480Mbps) (blue port farthest from Ethernet is OTG programming port) |
| Others       | 1x RS485 + 1x RS232 + 3x user controlled led |

## Resources

### Hardware Documentation

Datasheet: https://dl.sipeed.com/shareURL/MaixIV/M4N-Dock

### Software Documentation
Docs: https://dl.sipeed.com/shareURL/MaixIV/M4N-Dock
SDK: https://github.com/AXERA-TECH/ax650n_bsp_sdk

### AI Development
AI Toolchain (ONNX Conversion/Deployment)
- Pulsar2 (AXERA's ALL-IN-ONE Neural Network Compiler):
Docs: https://pulsar2-docs.readthedocs.io/en/latest/pulsar2/introduction.html
Download: https://huggingface.co/AXERA-TECH/Pulsar2/tree/main

op_support_list: https://pulsar2-docs.readthedocs.io/en/latest/appendix/op_support_list_ax650.html

Samples source: https://github.com/AXERA-TECH/ax-samples


## Technical Support
For custom development (kernel/OS customization, application-layer SDKs), contact: support@sipeed.