---
title: 典型应用
keywords: Linux, Lichee, TH1520, SBC, RISCV, application
update:
  - date: 2023-05-08
    version: v1.0
    author: wonder
    content:
      - Release docs
---

## llama.cpp

llama 是 META 开源的大语言模型，[llama.cpp](https://github.com/ggerganov/llama.cpp) 是 ggerganov 开源的纯 cpp 运行的 llama 推理项目。
感谢 llama.cpp 这个优秀的项目，我们可以在 LicheePi 4A 上运行 LLM。

笔者在早些时候稍微修改了 llama.cpp [https://github.com/Zepan/llama.cpp](https://github.com/Zepan/llama.cpp)，使其可以在更小内存（低至 700MB 左右）运行 7B 模型。

可以看到 TH1520 花费约 6s 计算一个 token（未使用 V 扩展加速，V 扩展加速预计可加速 4～8 倍，如果你加入了 V 扩展支持，欢迎投稿！）
![llama_th1520](./../../../../zh/lichee/th1520/lpi4a/assets/application/llama_th1520.png)  

同时还简单测试了下在入门级 C906 内核上运行7B模型的可行性，由于 D1 的内存过小，使用了 mmap 方式只读扩展，所以引入了大量低速 IO 操作，使得运行速度大为降低，最后仅 18s/token

![llama_d1](./../../../../zh/lichee/th1520/lpi4a/assets/application/llama_d1.png)  

## YOLOX 目标检测

本教程是一个如何在 LPi4A（LicheePi 4A） 开发板平台上部署 [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) 模型完成目标检测的示例。
教程中包括了：
- 在 LPi4A 开发版上安装 Python 环境
- 使用 YOLOX 项目中的源码执行模型

教程遵循通常的模型部署流程：
1. LPi4A 上的基础 Python 环境配置
2. 获取 yolox 源码和模型
3. 安装 yolox 所依赖的 python 包
4. LPi4A 上的使用 HHB-onnxruntime 执行示例

**基础 Python 环境配置**
**基本软硬件配置**
参考 LPi4A 的 《[开箱体验](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a/2_unbox.html)》中的描述，正确安装好开发板，上电启动后以 root 权限进入。
确保已联网的状态下，更新 apt 源
```bash
sudo apt update
```

安装一些软件，用于示例中后续使用
```bash
sudo apt install wget git vim
```

安装 SHL 库
```bash
wget https://github.com/T-head-Semi/csi-nn2/releases/download/v2.4-beta.1/c920.tar.gz
tar xf c920.tar.gz
cp c920/lib/* /usr/lib/riscv64-linux-gnu/ -rf
```


**Python 环境配置**
LPi4A 烧录的系统中已默认安装 python 3.11 版本。可以使用如下命令确认
```bash
python --version
```

后续均以 python3.11 版本为例，其他版本在安装依赖时需要修改到对应版本的命令。
各种 python 程序软件依赖的软件包大多可通过 pip 安装，可以使用如下命令安装 pip
```bash
apt install python3-pip
```

安装其他python包之前，先安装 venv 包，用于创建python虚拟环境
```bash
apt install python3.11-venv
```

创建 python虚拟环境，并激活
```bash
cd /root
python3 -m venv ort
source /root/ort/bin/activate
```


至此，基本 python 环境已经创建完成，与其他体系结构类似，可以直接通过 pip install 安装纯 python 包。

opencv 安装是会依赖其他 python 包，如果 pip 不能自动下载，则可以先手动安装依赖项的安装包。如何获取安装包可以参考 [下载 riscv whl](https://www.yuque.com/za4k4z/uzn618/zsp0krgg9dlp0fhx)。
**获取 YOLOX 模型**
[YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) 是一个类 YOLO 的目标检测模型，有相当优异的性能表现。
可以直接下载 github 上的源码和模型
```bash
git clone https://github.com/Megvii-BaseDetection/YOLOX.git
cd YOLOX/demo/ONNXRuntime
wget https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_s.onnx
```

**修改源码**
本教程将使用 HHB-onnxruntime 执行模型，因此切换到。在源码中的 onnxruntime 示例目录，修改文件 demo/ONNXRuntime/onnx_inference.py 的开头新增两行代码
```bash
#!/usr/bin/env python3
# Copyright (c) Megvii, Inc. and its affiliates.

+import sys
+sys.path.insert(0, "../../")
+
import argparse
import os
```


代码中使用 sys.path.insert 指定搜索路径，以此免去从源码中安装 YOLOX 的安装包的操作。
**安装依赖包**
RISC-V 体系结构的 python 生态还有欠缺，未来完善之后，YOLOX 中依赖的包可以通过 [requirements.txt](https://github.com/Megvii-BaseDetection/YOLOX/blob/main/requirements.txt) 文件直接安装。
本教程中的 YOLOX 示例依赖了较多的 python 包，下载预编译好的 python 包
```bash
git clone -b python3.11 https://github.com/zhangwm-pt/prebuilt_whl.git
cd prebuilt_whl
```

可以按照以下顺序，手工处理。
```bash
pip install numpy-1.25.0-cp311-cp311-linux_riscv64.whl
pip install opencv_python-4.5.4+4cd224d-cp311-cp311-linux_riscv64.whl
pip install kiwisolver-1.4.4-cp311-cp311-linux_riscv64.whl
pip install Pillow-9.5.0-cp311-cp311-linux_riscv64.whl
pip install matplotlib-3.7.2.dev0+gb3bd929cf0.d20230630-cp311-cp311-linux_riscv64.whl
pip install pycocotools-2.0.6-cp311-cp311-linux_riscv64.whl
pip3 install loguru-0.7.0-py3-none-any.whl
pip3 install torch-2.0.0a0+gitc263bd4-cp311-cp311-linux_riscv64.whl
pip3 install MarkupSafe-2.1.3-cp311-cp311-linux_riscv64.whl
pip3 install torchvision-0.15.1a0-cp311-cp311-linux_riscv64.whl
pip3 install psutil-5.9.5-cp311-abi3-linux_riscv64.whl
pip3 install tqdm-4.65.0-py3-none-any.whl
pip3 install tabulate-0.9.0-py3-none-any.whl
```

安装过程中会涉及到其他纯 python 依赖包，pip 会自动从官方源下载。
**安装 HHB-onnxruntime**
HHB-onnxuruntime 是移植了 SHL 后端（execution providers），让 onnxruntime 能复用到 SHL 中针对玄铁 CPU 的高性能优化代码。

```bash
wget https://github.com/zhangwm-pt/onnxruntime/releases/download/riscv_whl/onnxruntime-1.14.1-cp311-cp311-linux_riscv64.whl
pip install onnxruntime-1.14.1-cp311-cp311-linux_riscv64.whl
```

**执行**
在示例目录中执行 onnx_inference.py 示例

```bash
python3 onnx_inference.py -m yolox_s.onnx -i soccer.jpg -o outdir -s 0.3 --input_shape 640,640
```

`python3 onnx_inference.py -m yolox_s.onnx -i soccer.jpg -o outdir -s 0.3 --input_shape640,640`
参数说明：
- -m：指定模型
- -i：指定图片
- -o：指定输出目录
- -s：指定检测的阈值
- --input_shape：指定检测时使用的图片尺寸

**参考结果**

本教程中输入如下图，是运动员踢足球的图片，预期的检测结果是检测到两个人和一个足球。

> 图片来源于网络

![yolox_detection_soccer_input.jpg](./../../../../zh/lichee/th1520/lpi4a/assets/application/yolox_detection_soccer_input.jpg)

示例正常执行后，会在 outdir 目录下生成结果图片 soccer.jpg。图片中会用框画出检测到的目标，并标注概率，效果如下图：

![yolox_detection_soccer_output.jpg](./../../../../zh/lichee/th1520/lpi4a/assets/application/yolox_detection_soccer_output.jpg)

## Minecraft Server

TODO

## Wine-CE

TODO

## 其它

欢迎投稿～ 投稿接受后可得￥5～150（$1~20）优惠券！