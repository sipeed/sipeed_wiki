---
title: MAIX-III AXera-Pi

---

> 以下内容还在施工中，本周会随时变动。



# MAIX-III AXera-Pi 是什么？

[TOC]

截止 2022 年市面上的各类视觉国产 Linux AI 开发板陆续面世！在千元内的相关产品有熟悉的晶晨 A311D 、地平线 X3 、瑞芯微 RV1126、堪智 K510、全志 V85X 等芯片支持。

但它们要么资料太少、能效比差、价格太贵、没有生态、开发困难、摄像效果太差啦！是真的很难有一款板子可以满足所有人的要求！

但现在！支持国产芯片的 AI 开发工程师们，你们要多了一个更好的选择了！！

练习时长两年半，一颗 3.6 TOPS 大算力低功耗超强夜视效果的芯片来到了 SIPEED MAIX-III Linux AI 系列。

<img src="https://axera-tech.com/upload/8f/091a2540e7cdc5c7f62df022f80220.jpg" alt="img" style="zoom: 50%;" />

它就是来自「[爱芯元智](https://axera-tech.com/)」的 [AX620A](https://axera-tech.com/product/T7297367876123493768)，这是一款高算力，高能效比，低功耗的 AI SoC 芯片，芯片集成了四核 Cortex A7 @ 1Ghz CPU，拥有 3.6TOPs@INT8 的高算力 NPU，支持 4K@30fps 的 ISP，以及支持 H.264、H.265 编码的 VPU，拥有大算力和优异画质处理能力的 AX620A 可以实现更多的 AI 功能，带来最优的 AI 体验！（来自官方）

## 产品介绍

它其实早在 9月初爱芯元智参展了2022年世界人工智能大会亮相了～（当时它长这样）

<img src="/Users/junhuan/Library/Application Support/typora-user-images/image-20221011215757163.png" alt="image-20221011215757163" style="zoom: 50%;" />

最后总算是在 20221001 国庆节的时候推出了这款搭载 AX620A 的开发板，名为：MAIX-III AXera-Pi ！（以下简称 m3axpi ）

<img src="/Users/junhuan/Downloads/O1CN01Zz3KEg23vhBycn1iJ_!!2200606237318.jpg_400x400.png" alt="O1CN01Zz3KEg23vhBycn1iJ_!!2200606237318.jpg_400x400" style="zoom: 67%;" /> <img src="/Users/junhuan/Downloads/maix-iii-small.png" alt="maix-iii-small"  /> <img src="/Users/junhuan/Downloads/d038fb83-6ed4-4c2c-9a3f-eaf016a20129.png" alt="d038fb83-6ed4-4c2c-9a3f-eaf016a20129" style="zoom: 33%;" />

那么，它都带来了哪些内容呢？

- 资料太少？全中文文档教你从开箱到开发，从嵌入式 Linux 开发到 AI 模型开发指南一应俱全！
- 能效比差？这块板子四核 A7 靠一根 USB3.0 就可以跑起来！和你的外接电源散热器说再见吧！！
- 开发困难？支持 debian11 系统，内置 sdk 代码直接板上编译！还能白嫖在线 AI 模型训练到部署！！！ 
- 没有生态？SIPEED 开源累积了 LINUX、RISCV、AIOT、FPGA、MCU 等嵌入式领域的社区开发内容！！！！
- 摄像效果太差？芯片主打 AI + ISP 夜视增强！由原厂亲手为你调试从白天到夜间到超强摄像 ISP 效果！！！！！
- 价格太贵？从核心+底板+屏幕+摄像头+外壳支架总共人民币 **549** ！！！！！！（啸叫！咆哮！！）

## 产品特色

说了这么多没用的，还是赶紧把东西掏出来，让大家瞧瞧都有些什么吧！

### 影像效果

#### 夜视增强效果

- 视频

#### 暗室场景实拍

- 视频

#### AI 应用实拍

- 视频

### AI 生态

#### 大算力超多算子！

- 文档 或 芯片介绍

#### 大量现成的模型！

- 仓库

到 [MaixHub 模型库](https://maixhub.com/model/zoo) 找到你需要的模型，可以在过滤选项中选择`AXera-Pi 平台`来查找能在`AXera-Pi`上运行的模型。
以及可以在 [AXERA-TECH/ax-samples](https://github.com/AXERA-TECH/ax-samples) 仓库也可以找到模型。
然后下载并拷贝到开发板使用，模型详情页面会介绍如何使用模型，在使用模型前，最好先仔细看看左边目录中的`Axera-Pi`的基本操作和开发准备。

使用模型训练框架(比如 Pytorch）训练好模型后，要在 `AXera-Pi` 上运行，还需要将模型量化为`INT8`模型，以及转换成`AXera-Pi`支持的模型格式。
同时，也要注意`AXera-Pi`的算子支持情况，在设计模型结构时就需要考虑到；
另外，有些模型可能需要将后处理从模型中分离出来，在`AXera-Pi`上单独使用代码实现后处理。
详细的模型部署方法见**[部署模型到 Maix-III(M3) 系列 AXera-Pi 开发板](/ai/zh/deploy/ax-pi.html)**

#### 在线训练模型吧！

上 maixhub 提供

- AI 应用（都有哪些模型和效果）

#### 分享有趣的模型！

部署成功后会有一份模型文件，以及一份能运行模型的代码，可以将这些文件分享到 [MaixHub 模型库](https://maixhub.com/model/zoo) ，大家一起交流学习！

### 嵌入式

#### 超高能效比与性价比

对比主流 sbc 来说，这个配置的物料，这个功耗温度实测。

#### 基于 debian 系统开发

提供 debian11 Linux 系统，支持 SD 卡启动 DD 烧录系统，方便用户开箱上手。

#### BSP SDK 源码开放

提供 ax-sample / libmaix / bsp sdk 等源码仓库，提供 API 开发文档、SDK 开发方法等说明。

## 上手流程

为了让你最快能够把产品用起来，我们为您准备了以下使用流程：

### 1. 烧录系统启动

> 已买烧录卡的同学可以跳过这一步，插上 TF 卡即可启动 Linux Debian 系统。

- [烧录系统镜像](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/flash_system.html)

### 2. 登录到板子里

- [系统使用手册](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/basic_usage.html)

### 3. 编译代码运行

- [准备开发环境](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/dev_prepare.html)
- [SDK 开发指南](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/sdk_usage.html)

### 4. 训练模型部署

- [AI 开发指南](https://wiki.sipeed.com/ai/zh/deploy/ax-pi.html)

## 硬件参数一览

### 核心板硬件参数

> 需要整理

| 项目       | 参数                                  |
| ---------- | ------------------------------------- |
| CPU        | Quad-A7（四核A7）                     |
| NPU        | 14.4Tops@int4，3.6Tops@int8           |
| ISP        | 4K@30fps                              |
| 编解码格式 | H.264, H.265                          |
| 视频编码   | 4K@30fps                              |
| 视频解码   | 1080P@60fps                           |
| Ethernet   | 支持双路RGMII / RMII 接口模式的以太网 |
| 视频输出   | 支持MIPI DSI 4-LANE                   |
| DRAM       | 2GB LPDDR4X                           |
| 存储       | 可选16GB EMMC                         |
| IO 引出    | DDR4 SODIMM 260P 金手指全IO引出       |

### 底板的硬件参数

> 需要整理

摄像头相关参数

> 需要整理

支持的屏幕一览

### 外壳支架装配示意

> 需要整理

## 问题与解答（Q&A）

### Q：产品技术支持售后在哪？

A：我们提供两个技术 QQ 群：

### Q：产品文档资料社区在哪？

A：产品资料 http://wiki.sipeed.com/m3axpi AI 社区 http://maixhub.com 

### Q：那么，在哪可以买到？

A：复制此链接：


