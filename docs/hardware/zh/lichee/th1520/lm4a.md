---
title: LicheePi Module 4A
keywords: LicheePi, Sodimm, TH1520, RISCV, SBC
update:
  - date: 2023-03-31
    version: v0.1
    author: wonder
    content:
      - 初次编写文档
---

## 简介

LicheePi Module 4A 是一款采用 [平头哥半导体](https://www.t-head.cn/) 的 [曳影1520](https://www.t-head.cn/product/yeying) 作为主控的核心模组，主控核心包含四核玄铁 C910 CPU, 搭载 4TOPS@int8 AI 算力的 NPU，拥有 4K 视频处理能力，最大支持 16GB LPDDR4X 内存和 128G eMMC 存储，支持双千兆以太网和最大 4K 分辨率视频输出等特性，核心还额外包含一颗 C906 处理器用于音频处理。得益于 SODIMM 样式的封装， LicheePi Module 4A 可以用于多种场合，适用于多款底板。

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
  <td>曳影 1520</td>
</tr>
<tr>
  <td>CPU处理器</td>
  <td>RISC-V 64GCV C910*4@1.85GHz <br>· 每核支持 64KB I cache 和 64KB D Cache <br>· 四核共享 1MB L2 Cache <br>· 支持 TEE 和 REE，TEE/REE 支持核数启动时可配置<br>· 支持自定义且接口兼容 RISC-V 的多核调试框架<br>· 独立电源域，支持 DVFS</td>
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
  <td>ROM</td>
  <td>eMMC: <br>· 0G<br>· 8G<br>· 32G<br>· 128G</td>
</tr>
<tr>
  <td>以太网</td>
  <td> 千兆 PHY x 2</td>
</tr>
</tbody>
</table>

## 相关链接

[Github](https://github.com/sipeed/LicheePi4A)
[Sipeed 下载站(暂时空白)]()