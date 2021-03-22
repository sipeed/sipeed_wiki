---
title: Basic knowledge of MaixPy AI hardware acceleration
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: Basic knowledge of MaixPy AI hardware acceleration
---


## Model usage and hardware acceleration principle

Earlier, we learned that a model is a data organization and many parameters, and finally exists in the form of a file such as a file in the format of `kmodel`.
And for this model to be used in the MaixPy program, the program must first understand the file format of `kmodel` and support the algorithm in the model, so that the input can be output after some split calculation processes according to the description of the model.

Therefore, the key point is to support the algorithms in the model, called **operators**. In theory, we can use software to implement these operators, and then we can successfully run the model. The physical device that executes the software is the CPU. The network model is very computationally intensive. In addition, what we input is a picture. The picture itself has a huge amount of data. Even the main frequency of `K210` and `400MHz` cannot satisfy the smooth calculation model.

Therefore, either upgrade the `CPU`, but the cost is too high, or make a dedicated hardware, let this hardware specialize in a specific algorithm, because it does not do general calculations like the `CPU`, so the speed will be very fast. , We usually use a dedicated graphics accelerator card called `GPU` to accelerate graphics calculations. On the `K210`, this dedicated hardware is called `KPU` (kendryte proccess unit). The first one is the company name, which is actually the same as other chips. The `NPU` does the same thing.

In MaixPy, the code to derive the model has been integrated, and the `KPU` is used for calculation acceleration. There is no need to write a lot of code when using it. You only need to call a few functions to quickly run the model.


## About KPU

Although KPU can accelerate model calculations, due to various factors such as cost, time, power consumption, volume, heat generation, application field positioning and other factors, its capabilities are not like the powerful `NPU` in the professional field, including every type Operator, it can only handle part of it.

KPU implements the hardware acceleration of the four basic operations of convolution, batch normalization, activation, and pooling, but they cannot be used separately and are an integrated acceleration module.

Therefore, inference models on KPU, the following requirements (if you do not need to train and design the model, you do not need to understand it carefully):

1. Memory limitations

K210 has 6MB general RAM and 2MB KPU dedicated RAM. The input and output feature maps of the model are stored in 2MB KPU RAM. Weights and other parameters are stored in 6MB general-purpose RAM.

2. Which operators can be fully accelerated by KPU?

The following constraints need to be met.

* Feature map size: the input feature map is less than or equal to 320x240 (WxH) while the output feature map is greater than or equal to 4x4 (WxH), and the number of channels is from 1 to 1024.
* Same symmetric paddings (TensorFlow uses asymmetric paddings when stride=2 and the size is even).
* For ordinary Conv2D and DepthwiseConv2D, the convolution kernel is 1x1 or 3x3, and the stride is 1 or 2.
* MaxPool(2x2 or 4x4) and AveragePool(2x2 or 4x4).
* Any element-wise activation function (ReLU, ReLU6, LeakyRelu, Sigmoid...), KPU does not support PReLU.

3. Which operators can be partially accelerated by KPU?

* Asymmetric paddings or valid paddings convolution, nncase will add necessary Pad and Crop before and after it.
* Ordinary Conv2D and DepthwiseConv2D, the convolution kernel is 1x1 or 3x3, but stride is not 1 or 2. nncase will decompose it into KPUConv2D and a StridedSlice (may also need Pad).
* MatMul, nncase will replace it with a Pad (to 4x4) + KPUConv2D (1x1 convolution sum) + Crop (to 1x1).
* TransposeConv2D, nncase will replace it with a SpaceToBatch + KPUConv2D + BatchToSpace.

Instructions are from [here](https://github.com/kendryte/nncase/blob/master/docs/FAQ_ZH.md)


## Model conversion

As mentioned earlier, a model is actually a set of structure and parameter data. Different software can only recognize models in a specific format. KPU only recognizes models in `.kmodel` format. Generally, models trained on computers do not, such as `tensorflow` `.h5` format or `.tflite` format, to be used by `KPU`, it must be changed to `kmodel`, and use [nncase](https://github.com/kendryte/nncase) tool to achieve model conversion the goal of
If you need to convert the model, see the introduction in this warehouse for specific usage

## kmodel V3 model and V4 model

Due to the code update, two major versions were produced in the process, `V3` and `V4`, where the `V3` model refers to the use of [nncase v0.1.0 RC5](https://github.com/kendryte/nncase/ releases/tag/v0.1.0-rc5) The converted model; `V4` model refers to [nncase v0.2.0](https://github.com/kendryte/nncase/releases/tag/v0.2.0-beta4) Converted model

There is a certain difference between the two, so now the two are publicly stored, `V3` has less code, less memory, and higher efficiency, but it supports fewer operators; `V4` supports more operators, but both Realized by software, no hardware acceleration, more memory usage, so each has its own strengths. MaixPy firmware can also choose whether to support `V4`.

## Use model kmodel in MaixPy

1. Load the model in the SD card (TF card)

Put the model on the SD card, then load


```python
   import KPU as kpu
   m = kpu.load("/sd/test.kmodel")
```

2. Load the model in Flash

Download the model to Flash, then load

```python
   import KPU as kpu
   model_addr_in_flash = 0x300000
   m = kpu.load(model_addr_in_flash)
```

Here `model_addr_in_flash` is the offset address of the model in Flash, and the model can be burned to the corresponding address of Flash through kflash.py or kflash_gui

3. Ready to enter

In general, we will use images as input:
* Directly use the data collected by the camera as input:
```
img = sensor.snapshot()
```
Here `img` can be directly used as input, here need **note**: After the `snapshot` function collects the image, it will put the image data in two places
(1) `RGB565` memory block, the image is stored in a memory in the form of `RGB565`, which is convenient for image processing functions. Note that the order in the memory is `[pixel 1 RGB, pixel 2 RGB...]`
(2) `RGB888` memory block, the image is stored in another memory in the form of `R8G8B8`, note that the order in the memory is `[all pixels R, all pixels G, all pixels B]`, which we also call For `AI` memory

**Among them, the data actually input as KPU is `RGB888` area**, this is explained in detail in the previous document [MaixPy image and common operations](/course/basic/image/vary.md) chapter

* Read from file, or modified camera image

The image collected directly from the camera will automatically fill the `RGB888` area, but when we use image processing functions such as `image.resize()`, only `RGB565` will be modified, and `RGB888` will not be modified, because it needs to modify two memory at the same time It takes a lot of time, and the input of `KPU` is `RGB888` memory, so when you need to perform `KPU` operations, you need to synchronize (refresh) the `RGB888` memory block, and use `img.pix_to_ai()` to synchronize , Otherwise the modification has no effect on `KPU`.
such as:
```python
img = sensor.snapshot()
img = img.resize(240, 240)
img.pix_to_ai()
```

```python
img = image.Imag("/sd/test.jpg")
img.pix_to_ai()
```

4. Forward running model

Run the model forward, that is, walk the model calculation in the direction from input to output, and get the output value through input:

```python

feature_map = kpu.forward(m, img)
```
Here we get the `feature_map`, which is a feature map. For example, the classification of `small balls` and `toys` we used earlier, the output feature map is two nodes, each node represents the probability of the corresponding object, we will feature Figure converted to `list` object
```python
p_list = feature_map[:]
print(p_list)
```
You can get a result similar to `[0.9, 0.1]`



## Common problems in the use of KPU

### How big a model can KPU load?

C language code running model:
    When k210 runs the c code, it can load the model <6MB, depending on the content of the C code.
MaixPy running model:
    * When running MaixPy (minimum version), a model of about 4MB can be loaded. If you don’t use the camera and LCD, you can load up to 5MiB of models (because the buffer of the camera and LCD takes up a lot of memory, but the actual application is not very meaningful)
    * When running MaixPy (full version), it can load a model of about 2MiB
    * In addition, it also supports real-time loading of models from `Flash`. In theory, as long as the single-layer memory does not exceed 2MiB, the overall model can be infinitely large, but at the expense of computing speed. For usage, see [here](https://github.com/sipeed/MaixPy_scripts/tree/master/machine_vision/load_big_model). If you are interested in the principle and implementation, you can see [here](https://neucrack.com/p/313)



### What should I do if I report an error "memory overflow"?

When this problem occurs, according to the system memory management mentioned earlier, there are generally two possibilities:
1. The place where the error is reported has nothing to do with the system heap. It may be caused by insufficient memory in `GC`, but increase the total memory size of `GC` appropriately
2. Caused by the model being too large. You can try the following solutions in turn:
  1. Change the firmware of maixpy ​​mini version
  2. Perform model pruning optimization
  3. Use the `kpu.load_flash` interface to load the model in real time when running, but the execution efficiency is reduced a bit
  4. If the memory is insufficient and the performance of `kpu.load_flash` cannot be satisfied, then you may need to use [C SDK](https://github.com/kendryte/kendryte-standalone-sdk) for development.

### What should I do if I report an error "load error, only support kmodel v3/v4"?

If this problem occurs, you can try the following solutions:

1. If you are loading the model in the Flash, please make sure that the `flash offset` is filled in correctly and that there is no conflict with the address of the maixpy ​​firmware (the address of the model in the Flash is too high, and then when the firmware is programmed into the Flash, the firmware size Exceeded the starting address of the model, causing the model to be destroyed)
2. If it is `kmodel V4` converted with `nncase 0.2.0`, please try to convert with `nncase 0.1.0` to generate `kmodel V3`

### I want to select and load different models (for example, press the button to run the target classification, press the button again to run the target detection), how should I write the program?

Because the internal RAM is limited, when you need to switch between different models for `kpu.load(address)`, please execute `kpu.deinit(k210model)` to release the memory occupied by the previous model, and then load the new model.Time-shared memory
