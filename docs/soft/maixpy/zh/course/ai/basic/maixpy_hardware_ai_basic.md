---
title: MaixPy AI 硬件加速基本知识
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: MaixPy AI 硬件加速基本知识
---


## 模型使用和硬件加速原理

前面我们知道了模型是一个数据机构以及很多参数， 最终以一个文件比如`kmodel`格式的文件的形式存在。
而这个模型要能在 MaixPy 的程序里面被使用， 首先需要程序能够理解`kmodel`这个文件的格式， 并且支持模型里面的算法，这样才能按照模型的描述将输入经过一些裂计算过程后得到输出。

所以，重点就是支持模型里面的算法，称**算子**， 理论上，我们可以用软件去实现这些算子， 就可以成功运行模型了， 而执行软件的物理器件是`CPU`， 神经网络模型的计算量很大，加上我们输入的是图片，图片本身的数据量就挺庞大， 就算是`K210` `400MHz` 的主频， 也无法满足流畅的推算模型。

所以， 要么升级 `CPU`，但是成本太高， 要么做一个专用的硬件， 让这个硬件专门去特定的算法，因为不像 `CPU` 一样要做通用计算， 所以速度会非常快，在电脑上， 我们通常使用专用的图像加速卡即`GPU`来加速图形计算， 在`K210`上，这个专门的硬件叫做`KPU`（kendryte proccess unit)，第一个单词是公司名， 其实和其它芯片的`NPU`做的事情是一样的。

在 MaixPy 里面，已经集成了推导模型的代码，同时使用了`KPU`进行计算加速，使用时无需编写很多代码，只需要调用几个函数即可快速运行模型


## 关于 KPU

虽然 KPU 是能够加速模型运算了， 但是由于成本、时间、功耗、体积、发热、应用领域定位等各种因素，它的能力并不能像专业领域的强力`NPU`一样，包含了每一种算子，它只能处理一部分。

KPU 实现了卷积，批归一化，激活，池化 这4钟基础操作的硬件加速， 但是它们不能分开单独使用，是一体的加速模块。

所以， 在 KPU 上面推理模型， 以下要求（如果不需要训练和设计模型，暂时不需要仔细了解）：

1. 内存限制

K210 有 6MB 通用 RAM 和 2MB KPU 专用 RAM。模型的输入和输出特征图存储在 2MB KPU RAM 中。权重和其他参数存储在 6MB 通用 RAM 中。

2. 哪些算子可以被 KPU 完全加速？

下面的约束需要全部满足。

* 特征图尺寸：输入特征图小于等于 320x240(WxH) 同时输出特征图大于等于 4x4(WxH)，通道数在 1 到 1024。
* Same 对称 paddings (TensorFlow 在 stride=2 同时尺寸为偶数时使用非对称 paddings)。
* 普通 Conv2D 和 DepthwiseConv2D，卷积核为 1x1 或 3x3，stride 为 1 或 2。
* MaxPool(2x2 或 4x4) 和 AveragePool(2x2 或 4x4)。
* 任意逐元素激活函数 (ReLU, ReLU6, LeakyRelu, Sigmoid...), KPU 不支持 PReLU。

3. 哪些算子可以被 KPU 部分加速？

* 非对称 paddings 或 valid paddings 卷积, nncase 会在其前后添加必要的 Pad 和 Crop。
* 普通 Conv2D 和 DepthwiseConv2D，卷积核为 1x1 或 3x3，但 stride 不是 1 或 2. nncase 会把它分解为 KPUConv2D 和一个 StridedSlice (可能还需要 Pad)。
* MatMul, nncase 会把它替换为一个 Pad(到 4x4)+ KPUConv2D(1x1 卷积和) + Crop(到 1x1)。
* TransposeConv2D, nncase 会把它替换为一个 SpaceToBatch + KPUConv2D + BatchToSpace。

说明来自[这里](https://github.com/kendryte/nncase/blob/master/docs/FAQ_ZH.md)


## 模型转换

前面说到， 模型其实就是一组结构和参数数据，不同的软件只能识别特定格式的模型， KPU 只认`.kmodel`格式的模型， 一般用电脑训练的模型则不是， 比如`tensorflow`是`.h5`格式或者`.tflite`格式， 要给`KPU`使用， 必须经过变成`kmodel`, 使用[nncase](https://github.com/kendryte/nncase)这个工具来达到模型转换的目的
如果你需要转换模型， 具体使用方法看这个仓库里面的介绍

## kmodel V3 模型 和 V4 模型

由于代码更新， 在过程中产生了两个大版本,`V3` 和 `V4`， 其中`V3`模型是指用 [nncase v0.1.0 RC5](https://github.com/kendryte/nncase/releases/tag/v0.1.0-rc5) 转换出来的模型; `V4`模型指用[nncase v0.2.0](https://github.com/kendryte/nncase/releases/tag/v0.2.0-beta4)转换出来的模型

两者有一定的不同，所以现在两者公存， `V3`代码量更少，占用内存小，效率也高，但是支持的算子少; `V4`支持的算子更多，但是都是软件实现的，没有硬件加速，内存使用更多，所以各有所长。 MaixPy 的固件也可以选择是否支持 `V4`。

## MaixPy 中使用模型 kmodel

1.加载 SD 卡 （TF 卡）中的模型

将模型放到 SD 卡， 然后加载


```python
   import KPU as kpu
   m = kpu.load("/sd/test.kmodel")
```

2.加载 Flash 中的模型

将模型下载到 Flash， 然后加载

```python
   import KPU as kpu
   model_addr_in_flash = 0x300000
   m = kpu.load(model_addr_in_flash)
```

此处的 `model_addr_in_flash` 为模型在 Flash 中的偏移地址，模型可以通过 kflash.py 或者 kflash_gui 烧录到 Flash 对应的地址中

1. 准备输入

一般情况下，我们会使用图像作为输入：
* 直接使用摄像头采集的数据作为输入：
```
img = sensor.snapshot()
```
这里 `img` 就可以直接作为输入， 这里需要**注意**：`snapshot`函数采集到图片后，会将图片数据放到两个地方
(1) `RGB565`内存块， 图像以 `RGB565`的形式存放在一块内存中，方便图像处理的函数使用，注意在内存中的排序是`[像素1 RGB, 像素2 RGB...]`
(2) `RGB888`内存块， 图像以`R8G8B8`的形式存放在另一块内存中，注意在内存中的排序是`[所有像素 R, 所有像素 G， 所有像素 B]`, 我们也称之为`AI`内存

**其中，实际上作为 KPU 输入的数据是`RGB888`区域**， 这个在前面的文档 [MaixPy 图像及常用操作](./../../../course/image/basic/vary.md) 章节中有仔细讲解过

* 从文件读取，或者修改过的摄像头图像

直接从摄像头采集的图像会自动填充`RGB888`区域，但是我们使用图像处理函数比如`image.resize()`时，只会修改`RGB565`，没有修改`RGB888`,因为同时修改两处内存需要耗费大量时间，而 `KPU` 的输入又是`RGB888`内存， 所以在需要进行 `KPU` 运算时， 需要同步（刷新）一下`RGB888`内存块， 使用`img.pix_to_ai()`来进行同步，否则修改对 `KPU`没有生效。
比如：
```python
img = sensor.snapshot()
img = img.resize(240, 240)
img.pix_to_ai()
```

```python
img = image.Imag("/sd/test.jpg")
img.pix_to_ai()
```

4. 前向运行模型

前向运行模型，也就是按照 输入到输出的方向走一边模型计算， 通过输入得出输出的值：

```python

feature_map = kpu.forward(m, img)
```
这里得到了`feature_map`， 是一个特征图， 比如我们前面将的`小球`和`玩具`的分类，输出特征图是两个节点， 每个节点表示了是对应物体的概率，我们将特征图转换为`list`对象
```python
p_list = feature_map[:]
print(p_list)
```
就可以得到类似 `[0.9, 0.1]` 这样的结果了



## KPU使用过程中的常见问题

### KPU能够加载多大的模型？

C 语言代码运行模型：
    当k210运行 c 代码时，能够加载 < 6MB左右的模型， 具体看 C 代码内容。
MaixPy 运行模型：
    * 当运行 MaixPy(minimum版本)时，能够加载4MB左右的模型。 如果不使用摄像头和 LCD， 最大可以加载 5MiB 左右的模型（因为摄像头和 LCD 的缓冲区占用了很多内存，但实际应用也没多大意义了）
    * 当运行 MaixPy(完整版)时，能够加载 2MiB 左右的模型
    * 另外也支持实时从`Flash`加载模型， 理论上只要单层使用内存不超过 2MiB， 整体模型可以无限大，只不过要牺牲一点运算速度。 使用方法看[这里](https://github.com/sipeed/MaixPy_scripts/tree/master/machine_vision/load_big_model)。 如果对原理和实现感兴趣，可以看[这里](https://neucrack.com/p/313)



### 报错"memory overflow"怎么办？

出现这个问题，根据前面讲到过的系统内存管理可知，一般有两个可能性：
1. 报错的地方跟系统堆无关系， 可能是`GC`内存不够导致，可是适当增加 `GC` 的总内存大小
2. 由于模型过大引起的。可以依次尝试如下解决方案:
  1. 更换maixpy mini版本固件
  2. 进行模型剪枝优化
  3. 使用 `kpu.load_flash`接口运行时实时加载模型，只是执行效率降低一点
  4. 如果内存不足，而且`kpu.load_flash`性能无法满足， 那么你可能需要使用 [C SDK](https://github.com/kendryte/kendryte-standalone-sdk)进行开发。

### 报错"load error,only support kmodel v3/v4"怎么办？

出现这个问题可以尝试如下解决方案:

1. 如果为加载 Flash 中的模型，请确保 `flash offset` 填写正确，并保证和 maixpy 固件的地址没有冲突（模型在 Flash 中的地址太靠前，然后往 Flash 烧录入固件时， 固件大小超过了模型所在的起始地址， 导致模型被破坏）
2. 如果是采用 `nncase 0.2.0`进行转换的 `kmodel V4`，请尝试采用`nncase 0.1.0`进行转换，从而生成`kmodel V3`

### 我想实现不同模型的选择加载(例如按下按钮运行目标分类，再次按下按钮则运行目标检测)，应该怎么写程序？

因为内部RAM有限，所以当需要切换不同模型进行`kpu.load(address)`前，请先执行`kpu.deinit(k210model)`释放之前模型占用的内存，然后再加载新的模型。 也就是分时复用内存














