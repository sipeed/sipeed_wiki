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

LicheePi 4A is the high performance RISC-V linux development board using [Lichee Module 4A](http://wiki.sipeed.com/hardware/en/lichee/th1520/lm4a.html), based on [TH1520](https://www.t-head.cn/product/yeying) SOC (4xC910@1.85G, RV64GCV, 4TOPS@int8 NPU,  50GFLOP GPU), LicheePi 4A contains maximum 16GB 64bit LPDDR4X, 128GB eMMC, supports HDMI+MIPI dual 4K display, supports 4K camera input, dual Gigabit Ethernet interfaces (one of these supports POE) amd 4 USB3.0 interfaces, supports kinds of audio processing by C906 core.
![lpi4a](./../../../../zh/lichee/th1520/lpi4a/assets/intro/lpi4a.png)

LicheePi 4A 是截止目前（2023Q2）为止最强的 RISC-V SBC。性能约为上一代 RISC-V SBC [VisionFive2](https://www.starfivetech.com/en/site/boards)的2倍；未开启专用指令集加速的情况下, 性能逼近基于 ARM A72 的树莓派 4, 在开启相关指令集加速的情况下, 可以与树莓派 4 持平。而且最高具备 16GB 超大内存, 是树莓派 4 最高配置 8GB 内存的两倍！

![benchmark](./../../../../zh/lichee/th1520/lpi4a/assets/intro/benchmark.png)
![geekbench5](./../../../../zh/lichee/th1520/lpi4a/assets/intro/geekbench5.png)
 
LicheePi 4A 可以用作典型的 RISC-V 验证平台, 其强大的性能可以较快速地实现本地编译, 而无需使用 QEMU 进行编译。

我们在近期（2023Q2）还会放出基于LM4A的集群计算板卡 LicheeCluster 4A, 最大支持 7xLM4A 进行集群计算, 编译, 非常适合发行版编译农场场景, 尽情期待。

在保持高性能的同时, 我们也尽量进行了 CostDown 设计, 8GB 内存版本价格在 ￥749~ 899（\\$100 ~ \\$130）, 16GB 内存版本在 ￥1100~1300 （\\$155 ~\\$185）, 性价比上超越了树莓派 4（8GB ~\\$150）!
无论你是否是 RISC-V 粉丝, 你都值得入手体验下 LicheePi 4A 这款划时代的高性能 RISC-V SBC！
![desktop](./../../../../zh/lichee/th1520/lpi4a/assets/intro/desktop.png)

## 欢迎投稿

本文档为在线文档, 托管在 github 上, 大家可以点击右上角 `编辑本页` 链接来进行编辑~ 
对成功提交文档的用户, 我们视文档质量酌情提供 ￥5 ~ 150（\\$1 ~ 20）的优惠券~

## Parameters

<table>
<thead>
<tr>
  <th colspan=2>Main Chip</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Name</td>
  <td>TH1520</td>
</tr>
<tr>
  <td>CPU</td>
  <td>RISC-V 64GCV C910*4@2GHz <br>· Each core contains 64KB I cache amd 64KB D Cache <br>· 1MB of Shared L2 Cache <br>· Support TEE and REE, configured during core booting<br>· Support multi-core debugging framework of custom and RISC-V compatible interface<br>· Independent power domain, supports DVFS</td>
</tr>
<tr>
  <td>GPU</td>
  <td>· OpenCL 1.1/1.2/2.0<br>· OpenGL ES 3.0/3.1/3.2<br>· Vulkan 1.1/1.2<br>· Android NN HAL</td>
</tr>
<tr>
  <td>NPU</td>
  <td>Support 4TOPS@INT8, up to 1GHz <br>· Support TensorFlow、ONNX、Caffe <br>· Support CNN、RNN、DNN </td>
</tr>
<tr>
  <td>Decode</td>
  <td>Real-time decoder, support H.265/H.264/VP9/8/7/6/AVS/AVS+/AVS2.0/VC1/MPEG4 <br>· Supports H.264 BP/MP/HP@level 5.1 decoding, up to 4K resolution<br>· Supports H.265/HEVC Main Profile@level 5.1 decoding, up to 4K resolution<br>· Supports VP9 Profile-2 decoding, up to 4K resolution<br>· Supports AVS2.0 decoding, up to 4K resolution<br>· Supports VP6/7/8/AVS/AVS+/VC1/MPEG4 decoding, up to 1920x1080 resolution<br>· Decoding at 4K@75fps maximum</td>
</tr>
<tr>
  <td>Encode</td>
  <td>· Supports H.264 BP/MP/HP@level4.2 encoding, up to 4K resolution<br>· Supports H.265/HEVC Main Profile encoding, up to 4K resolution<br>· Only supports I-frames and P-frames<br>· Encoding at 4K@40fps maximum</td>
</tr>
<tr>
  <th colspan=2>Hardware features</th>
</tr>
<tr>
  <td>RAM</td>
  <td>· 8GB 64bits LPDDR4<br>· 16GB 64bits LPDDR4<br></td>
</tr>
<tr>
  <td>Storage</td>
  <td>· eMMC(Optional): None 、 8G、 32G、 128G<br>· Support TF card</td>
</tr>
<tr>
  <td>Ethernet</td>
  <td>· 2 x Gigabit Ethernet interfaces, Optional POE</td>
</tr>
<tr>
  <td>USB</td>
  <td>· USB3.0 x 4<br>· USB2.0 x 1 (For power supply or flashing OS)</td>
</tr>
<tr>
  <td>Audio</td>
  <td>· 1 x 3.5mm stereo interface<br>· One audio interface<br>· Two onboard microphones<br></td>
</tr>
<tr>
  <td>Display</td>
  <td>· 1 x HDMI2.0<br>· 1 x 4-lane MIPI DSI</td>
</tr>
<tr>
  <td>Camera</td>
  <td>· 2 x 2-lane MIPI CSI<br>· 1 x 4-lane MIPI CSI</td>
</tr>
<tr>
  <td>GPIO</td>
  <td>· UART<br>· IIC<br>· SPI</td>
</tr>
</tbody>
</table>

### Hardware information

[Specification / Datasheet](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/01_Specification)
[Schematic](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/02_Schematic)
[BOM](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/03_Bit_number_map)
[Dimensional Drawing](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/04_Dimensional_drawing)
[3D Model](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/05_3D_model)

## Other Site

Online store: [Aliexpress](https://www.aliexpress.com/item/1005005532736080.html)

[Github](https://github.com/sipeed/LicheePi4A)
[Sipeed Site](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a)

Telegram: https://t.me/linux4rv

Contact email：support@sipeed.com