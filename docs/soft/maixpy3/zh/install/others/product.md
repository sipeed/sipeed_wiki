---
title: 如何提交你的产品
keywords: MaixPy, MaixPy3, Python, Python3, MicroPython
desc: maixpy doc: 如何提交你的产品
---

当完成了一款芯片平台的适配后，想要合并进 MaixPy3 仓库，本文会对此做出说明。

## 提供你的编译配置

如 [envs/maix_v831.py](https://github.com/sipeed/MaixPy3/blob/main/envs/maix_v831.py) Python 包编译的配置，主要是用于区分适配在 maix 系列的 v831 产品，建议以芯片型号为区分，也许产品定义会不同，这时候就需要示例代码或文档来完成产品功能的区分了。

## 提供你的示例代码

如 [examples](https://github.com/sipeed/MaixPy3/tree/main/examples) 目录下的 maix_v831 文件夹，你可以在这里放置与你平台有关的程序、配置脚本、代码等资源。

## 提供你的相关文档

> 一般情况下可以不提供编译文档说明，这层的差异可能会在交叉编译链时解决，编译命令类似于 `python3.x setup.py xxxxx build` 的结构。

你可以在 [docs](https://github.com/sipeed/MaixPy3/tree/main/docs) 目录下存放公共文档，也可以在 [examples](https://github.com/sipeed/MaixPy3/tree/main/examples) 下的产品文件夹里存放专用的文档。

提供的文档类型可以是 markdown 或 jupyter notebook 文档。

可以提供开发方法、如何编译的文档，也可以提供各类设备特有的示例文档，建议通过 jupyter notebook 文档可以达到所见即所得的效果。

## 关于其他内容

2021年02月24日 现在仓库里还不会收录有关于交叉编译链、量产工具、烧录工具、训练工具等等与代码或文档无关的内容。

若是上述内容有不能够适应其他平台的地方，可以在 issue 里发起讨论，一起探讨和分享如何改进项目结构。

> 快快把你的代码提交进来吧！
