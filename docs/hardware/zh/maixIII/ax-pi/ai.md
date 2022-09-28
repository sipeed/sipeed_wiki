---
title: 是在 Maix-III(M3) 系列 AXera-Pi 开发板上运行 AI 模型和部署模型到 AXera-Pi
---


## 使用现成的模型

到 [MaixHub 模型库](https://maixhub.com/model/zoo) 找到你需要的模型，可以在过滤选项中选择`AXera-Pi 平台`来查找能在`AXera-Pi`上运行的模型。
以及可以在 [AXERA-TECH/ax-samples](https://github.com/AXERA-TECH/ax-samples) 仓库也可以找到模型。
然后下载并拷贝到开发板使用，模型详情页面会介绍如何使用模型，在使用模型前，最好先仔细看看左边目录中的`Axera-Pi`的基本操作和开发准备。

## 将你的模型转换为在 AXera-Pi 上可以使用的模型

使用模型训练框架(比如 Pytorch）训练好模型后，要在 `AXera-Pi` 上运行，还需要将模型量化为`INT8`模型，以及转换成`AXera-Pi`支持的模型格式。
同时，也要注意`AXera-Pi`的算子支持情况，在设计模型结构时就需要考虑到；
另外，有些模型可能需要将后处理从模型中分离出来，在`AXera-Pi`上单独使用代码实现后处理。
详细的模型部署方法见**[部署模型到 Maix-III(M3) 系列 AXera-Pi 开发板](/ai/zh/deploy/ax-pi.html)**

## 分享有趣的模型

部署成功后会有一份模型文件，以及一份能运行模型的代码，可以将这些文件分享到 [MaixHub 模型库](https://maixhub.com/model/zoo) ，大家一起交流学习！

