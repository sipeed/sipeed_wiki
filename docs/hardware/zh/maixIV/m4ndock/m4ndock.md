## 产品概述

**置顶淘宝链接：[立即购买](https://item.taobao.com/item.htm?spm=1619a.1.0.0.3f0865abb4Wq5c&id=744014549573&ns=1&abbucket=18#detail)**

M4N-Dock 是 Sipeed 公司推出的端侧混合精度高算力边缘计算盒子，搭载爱芯元智第三代高能效比智能视觉芯片 AX650N，内置 AI 算力 72TOPS@INT4 或 18TOPS@INT8，可运行当前热门大模型。

内置ISP支持 8K@30fps，另有爱芯独家 AI ISP，可实现微光夜视。同时含有 H.264 和 H.265 编解码器，支持单路最大 8K@60fps 解码，8K@30ps 编码，实测可稳定 32 路 1080P@30fps 解码，16 路 1080P@30fps 编码。

接口方面，AX650N 支持 64bit LPDDR4x，多路MIPI 输入，千兆 Ethernet、USB3.0 以及 HDMI 2.0b 输出。解码内置高算力和超强编解码能力，满足行业对高性能边缘智能计算的需求。

本款NPU性能强大，在仅使用单核心时，常用开源 AI 模型表现如下：yolov5s 在 640x640 分辨率图片输入下可达130帧（7.66ms）。mobilenetv2 在 224x224 分辨率图片输入下超达1798帧（0.556ms）。

通过内置多种深度学习算法，实现视觉结构化、行为分析、状态检测等应用，高效率支持 Transformer 模型和视觉大模型。提供丰富的开发文档，方便用户进行二次开发。

## 功能参数

| 设备      | 详细描述                                                                          |
| ------- | ----------------------------------------------------------------------------- |
| CPU     | 8x A55@1.7Ghz，集成 FPU，支持 NEON 加速                                               |
| NPU     | 72 TOPS@INT4 或 18 TOPS@INT8，支持 INT4/INT8/INT16/FP16/FP32 输入，支持 TopN(N<=32) |
| ISP     | 最大支持 8192x4320@30fps，最大分辨率: 16384x16384， 支持 AI ISP（微光夜视）                      |
| CODEC   | 支持 H.264/H.265 编解码，单路最大 8K@60fps 解码和 8K@30ps 编码                               |
| DSP     | 双核800Mhz                                                                      |
| RAM     | 8G 64bit LPDDR4x，系统内核和 AI CMM 使用占比可调                                          |
| ROM     | 32G eMMC 5.1，系统盘                                                              |
| SSD/HDD | 3x SATA 3.0 6Gb/s，可接 SSD/HDD，一路位于 M.2 接口，两路标准 SATA 接口                         |
| 视频输出    | 2x HDMI 2.0a，最大分辨率：4K@60fps                                                   |
| 摄像头输入   | 2x 4Lane MIPI-CSI 摄像头，最大支持 3.5Gbps                                            |
| 网络      | 2x 1Gbps 千兆以太网，实测达944Mbps                                                     |
| PCIE扩展  | 1x 1Lane PCIE2.0 5Gbps，位于 MINI-PCIE 接口                                        |
| USB扩展   | 1x USB3.2 Gen1 SS 5Gbps + 3x USB2.0 HS 480Mbps（蓝色远离网口的一个为OTG烧录端口）             |
| 外部连接    | 1x RS485 + 1x RS232                                                           |

## 资源汇总

### 硬件相关资料汇总

AX650N 芯片规格书：https://dl.sipeed.com/shareURL/MaixIV/M4N-Dock

### 软件开发资料汇总
软件开发文档：https://dl.sipeed.com/shareURL/MaixIV/M4N-Dock
软件开发SDK：https://github.com/AXERA-TECH/ax650n_bsp_sdk

### AI 开发资料汇总
AI工具链（模型转换、仿真、部署，ONNX）
Pulsar2 由爱芯元智自主研发的 ALL-IN-ONE 新一代神经网络编译器
使用文档：https://pulsar2-docs.readthedocs.io/zh_CN/latest/pulsar2/introduction.html
下载地址：https://pan.baidu.com/s/1FazlPdW79wQWVY-Qn--qVQ?pwd=sbru

模型算子支持列表：https://pulsar2-docs.readthedocs.io/zh_CN/latest/appendix/op_support_list.html

爱芯 Samples 例程：https://github.com/AXERA-TECH/ax-samples
已转换模型：https://dl.sipeed.com/shareURL/MaixIV/M4N-Dock


## 技术支持
若有特定业务开发需求需要应用层开发文档，或在系统层对内核和根文件系统有特定需求或需要定制开发，请发邮件到support@sipeed.com尝试获取支持。
