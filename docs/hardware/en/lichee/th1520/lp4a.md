---
title: Lichee Pi 4A
keywords: Linux, Lichee, TH1520, SBC, 
update:
  - date: 2023-03-31
    version: v0.1
    author: wonder
    content:
      - Create file
---

## Introduction

Lichee Pi 4A is the Risc-V linux development board using [Lichee Module 4A](http://wiki.sipeed.com/hardware/en/lichee/th1520/lm4a.html) core module, its main chip is [TH1520](https://www.t-head.cn/product/yeying), contains 4TOPS@int8 AI NPU, supports dual screen 4K resolution display and 4K mipi camera input, dual Gigabit Ethernets and Mutiple USB interfaces provides enough connections. And there is a Riscv C906 Core for audio decode.

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
  <td>Storage</td>
  <td>· eMMC: Optional Blank、 8G、 32G、 128G<br>· Support TF card</td>
</tr>
<tr>
  <td>Ethernet</td>
  <td>· 2 x Gigabit Ethernets, POE optional</td>
</tr>
<tr>
  <td>USB</td>
  <td>· USB3.0 x 4<br>· USB2.0 x 1 (Burn firmware only)</td>
</tr>
<tr>
  <td>Audio</td>
  <td>· 1 x 3.5mm Stereo port<br>· 1 x Speaker interface<br>· 2 x onboard microphones<br></td>
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

## Links

[Github](https://github.com/sipeed/LicheePi4A)
[Sipeed Download station(Blank now)]()