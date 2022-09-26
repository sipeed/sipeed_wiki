---
title: Maix-III 系列 AX-Pi 开发板 SDK 使用介绍
---

## SDK 和源码下载

SDK 源码在 [libmaix](https://github.com/sipeed/libmaix)， 点击页面`Code` -> `Download ZIP` 下载， 或者使用 git 命令下载：

```bash
git clone https://github.com/sipeed/libmaix.git
```

另外， AI 模型及例程在 [MaixHub 模型库](https://maixhub.com/model/zoo) 可以找到， 以及 [AXERA-TECH/ax-samples](https://github.com/AXERA-TECH/ax-samples) 仓库。


## 编译 SDK

对于 `libmaix`， 按照其`README.md` 文件描述的方法编译即可， 不过需要在`menuconfig`命令中选择 `AX-Pi` 作为编译目标。

这里简要介绍一下编译过程：

TODO:

## 组合 SDK 和 AI 模型例程

比如我们要跑一个视觉 AI 模型，需要用到摄像头，屏幕，还有 AI 模型。
其中 摄像头和屏幕的使用在`libmaix`中已经有例程，可以直接使用，基于摄像头屏幕使用例程，将 AI 模型的例程拷贝到例程目录中，调整一下 API 调用即可。

举例：

TODO：




