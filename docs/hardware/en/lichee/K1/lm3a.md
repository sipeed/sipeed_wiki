---
title: LicheePi Module 3A
keywords: LicheePi, Sodimm, K1, RISCV, SBC
update:
  - date: 2024-07-30
    version: v0.1
    author: zepan
    content:
      - Initial doc
---

## Intro

The LicheePi Module 3A is a core module that utilizes [SpaceMIT](https://spacemit.com/) [K1](https://www.spacemit.com/key-stone-k1/)  as the main controller. The main controller features an octa-core X60 CPU (RV64GCV, 256-bit Vector 1.0), offering 2 TOPS@int8 AI computing power and 1080P video processing capabilities. It supports up to 16GB of LPDDR4X memory and 128GB of eMMC storage, dual gigabit Ethernet, 1080P resolution video output, and PCIE Gen2x2. The LicheePi Module 3A is compatible with the LM4A and can be directly replaced on the baseboard.


![top](somtop.jpg)

![bot](sombot.jpg)

## Basic Parameter

<table>
<thead>
<tr>
  <th colspan=2>SOC Parameter</th>
</tr>
</thead>
<tbody>
<tr>
  <td>SOC</td>
  <td>SpaceMIT K1</td>
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
  <th colspan=2>Hardware Feature</th>
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
  <td>Ethernet</td>
  <td> GPHY x 2</td>
</tr>
<tr>
  <td>PCIe (x3)</td>
  <td>· PCIE PortA Gen2x1 (combo with USB3)<br>· PCIE PortB Gen2x2<br>· PCIE PortC Gen2x2</td>
</tr>
</tbody>
</table>

## Links
[Sipeed download site](https://dl.sipeed.com/shareURL/LICHEE/LicheePi3A)
