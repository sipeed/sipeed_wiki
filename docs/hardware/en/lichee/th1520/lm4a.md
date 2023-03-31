---
title: LicheePi Module 4A
keywords: LicheePi, Sodimm, TH1520, RISCV, SBC
update:
  - date: 2023-03-31
    version: v0.1
    author: wonder
    content:
      - Create file
---

## Introduction

LicheePi Module 4A is the Core Module using the [T-Head](https://www.t-head.cn/) RISC-V [TH1520](https://www.t-head.cn/product/yeying) SOC, containing 4 Risc-V C910 cores and 4TOPS@int8 AI NPU inside, supports 16GB LPDDR4X ram and 128GB eMMC storage, supports double gigabit Ethernet and maximum 4K resolution video output. The core also contains an additional C906 processor for audio processing. Because of the SODIMM style package, the LicheePi Module 4A can be used in various scenarios and is suitable for various types of baseboards.

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
  <td>RISC-V 64GCV C910*4@2GHz <br>· Each core contains 64KB I cache amd 64KB D Cache <br>· Shared 1MB L2 Cache <br>· Support TEE and REE, configered at core booting<br>· Support multi-core debugging framework of custom and RISC-V compatible interface<br>· Independent power domain, supports DVFS</td>
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
  <td>Real-time decoder, support H.265/H.264/VP9/8/7/6/AVS/AVS+/AVS2.0/VC1/MPEG4 <br>· Support H.264 BP/MP/HP@level 5.1 decoding, up to 4K resolution<br>· Support H.265/HEVC Main Profile@level 5.1 decoding, up to 4K resolution<br>· Support VP9 Profile-2 decoding, up to 4K resolution<br>· Support AVS2.0 decoding, up to 4K resolution<br>· Support VP6/7/8/AVS/AVS+/VC1/MPEG4 decoding, up to 1920x1080 resolution<br>· Decoding at 4K@75fps maximum</td>
</tr>
<tr>
  <td>Encode</td>
  <td>· Support H.264 BP/MP/HP@level4.2 encoding, up to 4K resolution<br>· Support H.265/HEVC Main Profile encoding, up to 4K resolution<br>· Only support I-frame and P-frame<br>· Encoding at 4K@40fps maximum</td>
</tr>
<tr>
  <th colspan=2>Hardware information</th>
</tr>
<tr>
  <td>RAM</td>
  <td>· 8GB 64bits LPDDR4<br>· 16GB 64bits LPDDR4<br></td>
</tr>
<tr>
  <td>ROM</td>
  <td>eMMC: <br>· 0G<br>· 8G<br>· 32G<br>· 128G</td>
</tr>
<tr>
  <td>Ethernet</td>
  <td> Gigabit PHY x 2</td>
</tr>
</tbody>
</table>

## Links

[Github](https://github.com/sipeed/LicheePi4A)
[Sipeed Download station(Blank now)]()