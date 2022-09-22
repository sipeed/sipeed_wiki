---
title: 部署模型到 Maix-III(M3) 系列 AX-Pi 开发板
date: 2022-09-21
---

> 有任何想法或者修改建议，欢迎留言或者直接点击右上角`编辑本页`进行修改后提交 PR

> [MaixHub](https://maixhub.com/model/zoo) 模型库有 AX-Pi 能直接运行的模型，可以直接下载使用，也欢迎上传分享你的模型~

要部署模型到 Maix-III(M3) 系列 AX-Pi 开发板，需要将模型量化到 INT8，减小模型大小的同时提高运行速度，一般采用 `PTQ`(训练后量化)的方式量化模型，步骤：
* 准备好浮点模型。
* 用模型量化和格式转换工具转换成 AX-Pi 支持的格式，这里工具使用爱芯官方提供的 [superpulsar](https://superpulsar-docs.readthedocs.io) 。
* 在 AX-Pi 上运行模型。

## 准备浮点模型

使用 `Pytorch` 或者 `Tensorflow` 训练好模型， 将模型保存为 `onnx` 格式备用。

需要注意只能使用 `AX-Pi` 所支持的算子，见[算子支持列表](https://superpulsar-docs.readthedocs.io/zh_CN/latest/appendix/op_support_list.html)。

对于某些网络，可能需要将后处理剥离出来，使用`CPU`处理。

## 模型量化和格式转换

* 安装`docker`，[安装教程](https://docs.docker.com/engine/install/)。

* 下载转换工具， 转换工具是以 docker 镜像的方式提供的，下载后用 docker 加载镜像即可。
直接使用 `docker`命令下载镜像或者先下载镜像文件解压成 `tar` 文件，再加载镜像:

| 下载站点 | 下载链接 | 使用方法 |
| :--- | :--- | :--- |
| dockerhub | 执行命令在线下载 | `docker pull sipeed/superpulsar:latest` |
| daocloud | 国内推荐 | `docker pull daocloud.io/sipeed/superpulsar:latest` |
| 迅雷云盘 | TODO: | 解压出 `tar`，再 `docker load -i superpulsar.tar` |
| 百度云盘 | TODO: | 解压出 `tar`，再 `docker load -i superpulsar.tar` |
| dl.sipeed.com | TODO: | 解压出 `tar`，再 `docker load -i superpulsar.tar` |

* 然后看 [superpulsar](https://superpulsar-docs.readthedocs.io) 文档中的转换命令以及配置文件方法进行模型量化和格式转换。
> 注意 `AX-Pi` 使用了虚拟 NPU 的概念来划分算力，以将实现全部算力给 NPU 或者 NPU 和 AI-ISP 各分一半。

## 在 AX-Pi 上运行模型

按照文档转换模型后，将模型通过 `scp` 或者 `adb` 传到 `AX-Pi` 上，使用文档中的模型测试运行命令运行模型即可。

要正式地将模型跑起来，你可能需要需要修改代码，更改输入预处理或者增加后处理，目前提供 `C/C++` SDK，代码参考 [ax-samples](https://github.com/AXERA-TECH/ax-samples)，可以交叉编译，也可以直接在 `AX-Pi` 上编译。


## QAT 量化

`QAT`(Quantization aware training)即量化感知训练，和`PTQ`在对训练好的模型进行浏览量化的做法不同，`QAT`是在训练时就模拟量化推理，以减少量化误差， 和训练后量化`PTQ`相比，有更高的精度，但是过程会更复杂，不建议一开始就使用。

[superpulsar](https://superpulsar-docs.readthedocs.io) 文档未来会更新，如果你擅长这方面，也欢迎点击右上角`编辑本页`在这里添加说明。


