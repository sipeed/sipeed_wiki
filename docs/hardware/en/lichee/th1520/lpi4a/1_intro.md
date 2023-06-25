---
title: 板卡介绍
keywords: Linux, Lichee, TH1520, SBC, RISCV
update:
  - date: 2023-05-08
    version: v1.0
    author: wonder
    content:
      - Release docs
---

English documents are being translated, please read these documents via web translate application at present if necessary .

## 简介

LicheePi 4A 是基于 [Lichee Module 4A](http://wiki.sipeed.com/hardware/zh/lichee/th1520/lm4a.html) 核心板的 高性能 RISC-V Linux 开发板，以 [TH1520](https://www.t-head.cn/product/yeying)  为主控核心（4xC910@1.85G， RV64GCV，4TOPS@int8 NPU， 50GFLOP GPU），板载最大 16GB 64bit LPDDR4X，128GB eMMC，支持 HDMI+MIPI 双4K 显示输出，支持 4K 摄像头接入，双千兆网口（其中一个支持POE供电）和 4 个 USB3.0 接口，多种音频输入输出（由专用 C906 核心处理）。  
![lpi4a](./../../../../zh/lichee/th1520/lpi4a/assets/intro/lpi4a.png)

LicheePi 4A 是截止目前（2023Q2）为止最强的 RISC-V SBC。性能约为上一代 RISC-V SBC [VisionFive2](https://www.starfivetech.com/en/site/boards)的2倍；未开启专用指令集加速的情况下，性能逼近基于 ARM A72 的树莓派 4，在开启相关指令集加速的情况下，可以与树莓派 4 持平。而且最高具备 16GB 超大内存，是树莓派 4 最高配置 8GB 内存的两倍！

![benchmark](./../../../../zh/lichee/th1520/lpi4a/assets/intro/benchmark.png)
![geekbench5](./../../../../zh/lichee/th1520/lpi4a/assets/intro/geekbench5.png)
 
LicheePi 4A 可以用作典型的 RISC-V 验证平台，其强大的性能可以较快速地实现本地编译，而无需使用 QEMU 进行编译。

我们在近期（2023Q2）还会放出基于LM4A的集群计算板卡 LicheeCluster 4A，最大支持 7xLM4A 进行集群计算，编译，非常适合发行版编译农场场景，尽情期待。

在保持高性能的同时，我们也尽量进行了 CostDown 设计，8GB 内存版本价格在 ￥749~ 899（\\$100 ~ \\$130），16GB 内存版本在 ￥1100~1300 （\\$155 ~\\$185）, 性价比上超越了树莓派 4（8GB ~\\$150）!
无论你是否是 RISC-V 粉丝，你都值得入手体验下 LicheePi 4A 这款划时代的高性能 RISC-V SBC！
![desktop](./../../../../zh/lichee/th1520/lpi4a/assets/intro/desktop.png)

## 欢迎投稿

本文档为在线文档，托管在 github 上，大家可以点击右上角 `编辑本页` 链接来进行编辑~ 
对成功提交文档的用户，我们视文档质量酌情提供 ￥5 ~ 150（\\$1 ~ 20）的优惠券~

## 基础参数

<table>
<thead>
<tr>
  <th colspan=2>主控参数</th>
</tr>
</thead>
<tbody>
<tr>
  <td>主控芯片</td>
  <td>TH1520</td>
</tr>
<tr>
  <td>CPU处理器</td>
  <td>RISC-V 64GCV C910*4@2GHz <br>· 每核支持 64KB I cache 和 64KB D Cache <br>· 四核共享 1MB L2 Cache <br>· 支持 TEE 和 REE，TEE/REE 支持核数启动时可配置<br>· 支持自定义且接口兼容 RISC-V 的多核调试框架<br>· 独立电源域，支持 DVFS</td>
</tr>
<tr>
  <td>图形处理器</td>
  <td>· OpenCL 1.1/1.2/2.0<br>· OpenGL ES 3.0/3.1/3.2<br>· Vulkan 1.1/1.2<br>· Android NN HAL</td>
</tr>
<tr>
  <td>NPU处理器</td>
  <td>支持 4TOPS@INT8 通用 NNA 算力，主频 1GHz <br>· 支持 TensorFlow、ONNX、Caffe <br>· 支持 CNN、RNN、DNN 等</td>
</tr>
<tr>
  <td>视频解码器</td>
  <td>实时解码器，支持 H.265/H.264/VP9/8/7/6/AVS/AVS+/AVS2.0/VC1/MPEG4 <br>· 支持 H.264 BP/MP/HP@level 5.1 解码，最大 4K 分辨率<br>· 支持 H.265/HEVC Main Profile@level 5.1 解码，最大 4K 分辨率<br>· 支持 VP9 Profile-2 解码，最大 4K 分辨率<br>· 支持 AVS2.0 解码，最大 4K 分辨率<br>· 支持 VP6/7/8/AVS/AVS+/VC1/MPEG4 解码，最大 1920x1080 分辨率<br>· 解码性能最大 4K@75fps</td>
</tr>
<tr>
  <td>视频编码器</td>
  <td>· 支持 H.264 BP/MP/HP@level4.2 编码，最大 4K 分辨率<br>· 支持 H.265/HEVC Main Profile 编码，最大 4K 分辨率<br>· 仅支持 I 帧和 P 帧<br>· 编码性能最大 4K@40fps</td>
</tr>
<tr>
  <th colspan=2>硬件特性</th>
</tr>
<tr>
  <td>RAM</td>
  <td>· 8GB 64bits LPDDR4<br>· 16GB 64bits LPDDR4<br></td>
</tr>
<tr>
  <td>存储</td>
  <td>· eMMC: 可选 空贴、 8G、 32G、 128G<br>· 支持 TF 卡</td>
</tr>
<tr>
  <td>以太网</td>
  <td>· 2 x 千兆以太网接口，可选 POE</td>
</tr>
<tr>
  <td>USB</td>
  <td>· USB3.0 x 4<br>· USB2.0 x 1（仅用于烧录）</td>
</tr>
<tr>
  <td>音频接口</td>
  <td>· 1 x 3.5mm 耳机接口<br>· 一个扬声器接口<br>· 两个板载麦克风<br></td>
</tr>
<tr>
  <td>显示接口</td>
  <td>· 1 x HDMI2.0<br>· 1 x 4-lane MIPI DSI</td>
</tr>
<tr>
  <td>摄像头接口</td>
  <td>· 2 x 2-lane MIPI CSI<br>· 1 x 4-lane MIPI CSI</td>
</tr>
<tr>
  <td>GPIO</td>
  <td>· UART<br>· IIC<br>· SPI</td>
</tr>
</tbody>
</table>

### 硬件资料下载

[Specification / Datasheet](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/01_Specification)
[Schematic](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/02_Schematic)
[BOM](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/03_Bit_number_map)
[Dimensional Drawing](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/04_Dimensional_drawing)
[3D Model](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/05_3D_model)

## 其他链接

Online store: [Aliexpress](https://www.aliexpress.com/item/1005005532736080.html)

[Github](https://github.com/sipeed/LicheePi4A)
[Sipeed 下载站](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a)

Telegram: https://t.me/linux4rv

联系邮箱：support@sipeed.com