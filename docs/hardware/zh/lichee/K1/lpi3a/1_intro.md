---
title: 板卡介绍
keywords: Linux, Lichee, K1, SBC, RISCV
update:
  - date: 2024-07-30
    version: v1.0
    author: zepan
    content:
      - Release docs
---

## 简介

LicheePi 3A 是基于 [Lichee Module 3A](http://wiki.sipeed.com/hardware/zh/lichee/K1/lm3a.html) 核心板的 高性能 RISC-V Linux 开发板，以 [K1](https://www.spacemit.com/key-stone-k1/)  为主控核心（8xX60@1.6G， RV64GCV，2TOPS@int8 NPU， 20GFLOP GPU），板载最大 16GB 32bit LPDDR4X，128GB eMMC，支持 HDMI+MIPI 双1080P 显示输出，支持 16MP 摄像头接入，双千兆网口（其中一个支持POE供电）和 4 个 USB3.0 接口，以及2路 PCIE Gen2x2，多种音频输入输出。  
![lpi3a](./assets/intro/lpi3a.jpg)
![pcie](./assets/intro/pcie.png)

LicheePi 3A 是目前极具性价比的中端 RISC-V SBC。多核性能约为上一代 RISC-V SBC [LPi4A](http://wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a.html)的80%, 单核性能约为 50%
[GeekBench6](https://browser.geekbench.com/v6/cpu/compare/6718771?baseline=5822041)

![benchmark](./assets/intro/benchmark.png)
![geekbench6](./assets/intro/geekbench6.png)
 
LicheePi 3A 可以用作典型的 RISC-V 验证平台，其强大的性能可以较快速地实现本地编译，而无需使用 QEMU 进行编译。

LicheePi 3A 基本与LicheePi4A兼容，如果你购买过LicheePi4A，那么可以仅购买LM3A来装在LPi4A底板上（无M.2接口）。
![desktop](./assets/intro/desktop.jpg)


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
  <td>存储</td>
  <td>· eMMC: 可选32G、 128G<br>· 支持 TF 卡<br>· 支持 NVMe SSD</td>
</tr>
<tr>
  <td>以太网</td>
  <td>· 2 x 千兆以太网接口，可选 POE</td>
</tr>
<tr>
  <td>PCIe (x3)</td>
  <td>· PCIE PortA Gen2x1 (combo with USB3)<br>· PCIE PortB Gen2x2<br>· PCIE PortC Gen2x2</td>
</tr>
<tr>
  <td>USB</td>
  <td>· USB3.0 x 4<br>· USB2.0 x 2</td>
</tr>
<tr>
  <td>音频接口</td>
  <td>· 1 x 3.5mm 耳机接口<br>· 一个扬声器接口<br>· 两个板载麦克风<br></td>
</tr>
<tr>
  <td>显示接口</td>
  <td>· 1 x HDMI1.4<br>· 1 x 4-lane MIPI DSI</td>
</tr>
<tr>
  <td>摄像头接口</td>
  <td>· 1 x 2-lane MIPI CSI<br>· 1 x 4-lane MIPI CSI</td>
</tr>
<tr>
  <td>GPIO</td>
  <td>· UART<br>· IIC<br>· SPI</td>
</tr>
</tbody>
</table>

### 硬件资料下载

[板卡规格书](https://dl.sipeed.com/shareURL/LICHEE/LicheePi3A/01_Specification)
[底板原理图](https://dl.sipeed.com/shareURL/LICHEE/LicheePi3A/02_Schematic)
[底板点位图](https://dl.sipeed.com/shareURL/LICHEE/LicheePi3A/03_Bit_number_map)
[底板尺寸图](https://dl.sipeed.com/shareURL/LICHEE/LicheePi3A/04_Dimensional_drawing)
[模型文件](https://dl.sipeed.com/shareURL/LICHEE/LicheePi3A/05_3D_model)

## 其他链接

[淘宝](https://item.taobao.com/item.htm?id=)
[Aliexpress](https://xxx)
[Sipeed 下载站](https://dl.sipeed.com/shareURL/LICHEE/LicheePi3A)

QQ群: 559614960 [点我自动加群](http://qm.qq.com/cgi-bin/qm/qr?k=5YkapIhdtWHp8AEfM5_bFFYQIX3CUQN6)
Telegram: https://t.me/linux4rv

论坛：Maixhub.com/discussion
联系邮箱：support@sipeed.com
