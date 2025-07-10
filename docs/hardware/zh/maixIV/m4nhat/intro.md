## 简介

M4N-Hat 是 Sipeed 公司推出的高集成度 AI 计算模组，采用爱芯元智 AX650N/C 芯片的紧凑型解决方案。作为嵌入式设备扩展模块，在提供 72TOPS@INT4(18TOPS@INT8) 算力的同时，保留与 M4N-Dock 同源的 8K 编解码能力，专为空间受限的边缘计算场景设计。

本模组支持主流树莓派系列开发板即插即用，并支持 Transformer 架构加速。通过板载 0.8mm 4Pin USB 和 Type-A USB SS 5Gbps 接口，可快速扩展摄像头、存储等外设，是智能摄像头、工业质检等轻量级AI应用的理想选择。PCIE2.0 扩展接口完美适配树莓派5，支持构建多模态边缘计算节点，支持 QWen 2.5、QWen 3、DeepSeek、InternVL2.5 等大模型的量化部署。

## 图片展示

<div style="display: flex; flex-wrap: wrap; gap: 10px; width: 100%;">
  <img src="../assets/m4nhat/DSC07555.JPG" style="width: calc(50% - 5px);">
  <img src="../assets/m4nhat/DSC07569.JPG" style="width: calc(50% - 5px);">
  <img src="../assets/m4nhat/DSC07556.JPG" style="width: calc(50% - 5px);">
  <img src="../assets/m4nhat/neofetch.jpg" style="width: calc(50% - 5px);">
</div>

## 功能参数

| 设备     | 详细描述                                             |
| ------- | --------------------------------------------------- |
| CPU     | 8x A55@1.7Ghz，集成 FPU，支持 NEON 加速                |
| NPU     | 72 TOPS@INT4 或 18 TOPS@INT8，支持INT4/INT8/INT16/FP16/FP32 输入，支持 TopN(N<=32) |
| CODEC   | 支持 H.264/H.265 编解码，单路最大 8K@60fps 解码和 8K@30ps 编码  |
| DSP     | 双核800Mhz                                                 |
| RAM     | 8G 64bit LPDDR4x，系统内核和 AI CMM 使用占比可调，默认 2+6 配置  |
| ROM     | 32G eMMC 5.1，系统盘                                        |
| 视频输出  | 1x HDMI 2.0a，最大分辨率：4K@60fps                   |
| 摄像头输入| 1x 0.8mm 4p 外接 USB 摄像头                          |
| PCIE扩展 | 1x 16p fpc 1Lane PCIE2.0 5Gbps，兼容树莓派5          |
| USB扩展  | 1x Type-A USB SS 5Gbps + 1x Type-C USB HS 480Mbps  |
| 外部连接  | 1x 1.25mm 2p 外接扬声器 + 1x 1.25mm 2p 外接风扇 + 1x 10p fpc 外接 SPI 屏幕 + 1x 6p fpc 外接 I2C 触摸 |

![](../assets/m4n/benchmark.png)
![](../assets/m4n/normalized_benchmark.png)

| Models      | RK3588@6T| Maix4@18T  | Hailo8 26T | Hailo8 13T |
|-------------|----------|------------|------------|------------|
| Inceptionv1 | 43       | 2494       | 928        | 519        |
| MobileNetv2 | 960      | 5073       | 2433       | 1738       |
| SqueezeNet11| 694      | 5961       | -          | -          |
| ResNet18    | 543      | 2254       | -          | -          |
| ResNet50    | 294      | 1045       | 1368       | 503        |
| SwinT       | 21       | 401        | -          | -          |
| ViT-B/16    | 18       | 207        | 107        | 40         |
| YOLOv5s     | 48       | 384        | 364        | 168        |
| YOLOv5n     | 78       | 743        | -          | -          |
| YOLOv6s     | 80       | 321        | -          | -          |
| YOLOv6n     | 212      | 743        | -          | -          |
| YOLOv8s     | 39       | 279        | -          | -          |
| YOLOv8n     | 73       | 710        | -          | -          |
| YOLOxs      | 34       | 304        | -          | -          |
| YOLO11s     | 30       | 313        | -          | -          |


| Models                       | Item                         | Maix4@18T    | RK3588@6T    |
|------------------------------|------------------------------|--------------|--------------|
| SmolVLM-256M                 | Image Encoder 512*512        | 105ms        | 842ms        |
|                              | TTFT                         | 57ms         | 87ms         |
|                              | Decode                       | 80 tokens/s  | 77 tokens/s  |
| StableDiffusion 1.5(512*512) | U-Net                        | 0.43 s/it    | 5.65 s/it    |
|                              | VAE Decoder                  | 0.91 s       | 11.13 s      |
| Qwen2.5-VL-3B                | Image Encoder 448*448        | 780 ms       |              |
|                              | TTFT 320 tokens              | 2857 ms      |              |
|                              | Decode                       | 6.2 tokens/s |              |
|                              | Image Encoder 392*392        |              | 2930 ms      |
|                              | TTFT 196 tokens              |              | 1262 ms      |
|                              | Decode                       |              | 8.6 tokens/s |

## 资源汇总

### 硬件相关资料汇总

AX650N 芯片规格书：https://dl.sipeed.com/shareURL/MaixIV/M4N-Dock

### 软件开发资料汇总
软件开发文档：https://dl.sipeed.com/shareURL/MaixIV/M4N-Dock
软件开发SDK：https://www.ebaina.com/down/240000038900

### AI 开发资料汇总
大模型和AXCL：https://axcl-docs.readthedocs.io
树莓派5 AXCL专项：https://axcl-pi5-examples-cn.readthedocs.io

模型仓库：https://huggingface.co/AXERA-TECH

AI工具链（模型转换、仿真、部署，ONNX）
Pulsar2 由爱芯元智自主研发的 ALL-IN-ONE 新一代神经网络编译器
使用文档：https://pulsar2-docs.readthedocs.io/zh_CN/latest/pulsar2/introduction.html
下载地址：https://pan.baidu.com/s/1FazlPdW79wQWVY-Qn--qVQ?pwd=sbru

模型算子支持列表：https://pulsar2-docs.readthedocs.io/zh_CN/latest/appendix/op_support_list.html

爱芯 Samples 例程：https://github.com/AXERA-TECH/ax-samples


## 技术支持
若有特定业务开发需求需要应用层开发文档，或在系统层对内核和根文件系统有特定需求或需要定制开发，请发邮件到support@sipeed.com尝试获取支持。
