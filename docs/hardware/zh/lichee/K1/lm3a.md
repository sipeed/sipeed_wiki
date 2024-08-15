---
title: LicheePi Module 3A
keywords: LicheePi, Sodimm, K1, RISCV, SBC
update:
  - date: 2024-07-30
    version: v0.1
    author: zepan
    content:
      - 初次编写文档
---

## 简介

LicheePi Module 3A 是一款采用 [进迭时空](https://spacemit.com/) 的 [K1](https://www.spacemit.com/key-stone-k1/) 作为主控的核心模组，主控核心包含八核X60 CPU (RV64GCV, 256bit Vector 1.0), 具备 2TOPS@int8 AI 算力，拥有 1080P 视频处理能力，最大支持 16GB LPDDR4X 内存和 128G eMMC 存储，支持双千兆以太网和1080P分辨率视频输出等特性，还支持PCIE Gen2x2。 LicheePi Module 3A 与LM4A 兼容，可以在底板上直接替换使用。

![top](somtop.jpg)

![bot](sombot.jpg)

## 基本参数

<table>
<thead>
<tr>
  <th colspan=2>主控参数</th>
</tr>
</thead>
<tbody>
<tr>
  <td>主控芯片</td>
  <td>进迭 K1</td>
</tr>
<tr>
  <td>CPU</td>
  <td>RISC-V 64GCV X60*8@1.6GHz <br>· Cluster0 2TOPS AI-Power, 32K L1-Cache per core, 512K L2-Cache, 512KB TCM, Vector-256bit <br>· Cluster0 32K L1-Cache per core, 512K L2-Cache, Vector-256bit </td>
</tr>
<tr>
  <td>GPU</td>
  <td>· IMG BXE-2-32@819M <br>· OpenGL ES 3.2, OpenCL 3.0<br>· Vulkan 1.3<br>· 20GFLIPS </td>
</tr>
<tr>
  <td>NPU</td>
  <td>Cluster0 2TOPS@INT8  <br>· 支持 TensorFlow、ONNX、Caffe <br>· 支持 CNN、RNN、DNN 等</td>
</tr>
<tr>
  <td>Video</td>
  <td>H265&H264 @ 1080p 60fps decode/encode</td>
</tr>
<tr>
  <th colspan=2>硬件特性</th>
</tr>
<tr>
  <td>RAM</td>
  <td>· 8GB 32bits LPDDR4X<br>· 16GB 32bits LPDDR4X<br></td>
</tr>
<tr>
  <td>ROM</td>
  <td>eMMC: <br>· 32G<br>· 128G</td>
</tr>
<tr>
  <td>以太网</td>
  <td> 千兆 PHY x 2</td>
</tr>
<tr>
  <td>PCIe (x3)</td>
  <td>· PCIE PortA Gen2x1 (combo with USB3)<br>· PCIE PortB Gen2x2<br>· PCIE PortC Gen2x2</td>
</tr>
</tbody>
</table>

## 相关链接
[Sipeed 下载站](https://dl.sipeed.com/shareURL/LICHEE/LicheePi3A)