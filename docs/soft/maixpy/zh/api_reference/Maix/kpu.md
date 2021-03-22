---
title: KPU
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: KPU
---


KPU是通用的神经网络处理器，它可以在低功耗的情况下实现卷积神经网络计算，时时获取被检测目标的大小、坐标和种类，对人脸或者物体进行检测和分类。

* KPU 具备以下几个特点：
  * 支持主流训练框架按照特定限制规则训练出来的定点化模型
  * 对网络层数无直接限制，支持每层卷积神经网络参数单独配置，包括输入输出通道数目、输入输 出行宽列高
  * 支持两种卷积内核 1x1 和 3x3
  * 支持任意形式的激活函数
  * 实时工作时最大支持神经网络参数大小为 5.5MiB 到 5.9MiB
  * 非实时工作时最大支持网络参数大小为（Flash 容量-软件体积）




## 例程

### 运行人脸检测

模型下载地址：[http://dl.sipeed.com/MAIX/MaixPy/model](http://dl.sipeed.com/MAIX/MaixPy/model) , 下载`face_model_at_0x300000.kfpkg`

完整例程： [face_find](https://github.com/sipeed/MaixPy_scripts/tree/master/machine_vision/face_find)

### 运行特征图

模型下载地址：[http://dl.sipeed.com/MAIX/MaixPy/model](http://dl.sipeed.com/MAIX/MaixPy/model) , 下载`face_model_at_0x300000.kfpkg`

该模型是8bit定点模型，约380KB大小，层信息为：
```
1 2        :160x120
3 4 5 6	   :80x60
7 8 9 10   :40x30
11~16      :20x15
```

```python
import sensor
import image
import lcd
import KPU as kpu
index=3  
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
task=kpu.load(0x300000)
img=image.Image()
info=kpu.netinfo(task)
layer=info[index]
w=layer.wo()
h=layer.ho()
num=int(320*240/w/h)
list=[None]*num
x_step=int(320/w)
y_step=int(240/h)
img_lcd=image.Image()
while True:
    img=sensor.snapshot()
    fmap=kpu.forward(task,img,index)
    for i in range(0,num):
        list[i]=kpu.fmap(fmap,i)
    for i in range(0,num):
        list[i].stretch(64,255)
    for i in range(0,num):
        a=img_lcd.draw_image(list[i],((i%x_step)*w,(int(i/x_step))*h))
	   lcd.display(img_lcd)
   	kpu.fmap_free(fmap)
```

-----------------------------


## 模块方法

### load

从flash或者文件系统中加载模型

```python
KPU.load(offset, file_path)
```

#### 参数

`offset` 和 `file_path` 参数只能二选一，不需要关键词，直接传参即可

* `offset`: 模型在 flash 中的偏移大小，如 `0xd00000` 表示模型烧录在13M起始的地方, `0x300000`表示在 `Flash` `3M`的地方
* `file_path`: 模型在文件系统中为文件名， 如 `“/sd/xxx.kmodel”`

##### 返回

如果正确加载，会返回返回值， 否则会抛出错误， 请看抛出的错误提示， 另外错误代码参考[这里](https://github.com/sipeed/MaixPy/blob/fa3cf2c96353fa698e9386e42be8b3c9cf495114/components/kendryte_sdk/include/sipeed_kpu.h#L6-L23)

如果发现错误代码是小于 `2000` 的值， 则是固件版本太低，需要更新固件版本

* `kpu_net`: kpu 网络对象

### load_flash

与 load 方法作用相同，

```python
kpu.load_flash(model_addr, is_dual_buf, batch_size, spi_speed)
```

#### 参数

* `model_addr`：Flash addr 经过预处理的模型烧录到 flash 中的偏移地址。注意，这里需要预处理模型文件[说明](https://github.com/sipeed/MaixPy_scripts/blob/master/machine_vision/load_big_model/README_ZH.md)。
* `is_dual_buf`：`0`,单一缓冲区加载，使用较少的 RAM 和较慢的速度动态加载该模型文件； `1`，开启双缓冲加载，需要更大的 RAM， 运行速度相对较快。
* `batch_size`：将 `is_dual_buf` 设置为 1 时，需要设置 load batch_size，建议值为 `0x4000~0x10000`，可以测试出模型的最佳值。如果 `is_dual_buf` 为 0 则设置为 0
* `spi_speed`：使用 SPI flash 加载模型文件时，我们会暂时将 flash 设置为高速模式，并设置所需的 spi 时钟频率。该值应 <= 80000000(实际频率，设值可能不等于实际频率。)

#### 返回值

* `kpu_net`: kpu 网络对象

### init_yolo2


为`yolo2`网络模型传入初始化参数， 只有使用`yolo2`时使用

```python
KPU.init_yolo2(kpu_net, threshold, nms_value, anchor_num, anchor)
```

比如：

```python
import KPU as kpu
task = kpu.load(0x300000)
anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)
kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)
```

#### 参数

* `kpu_net`: kpu 网络对象, 即加载的模型对象, `KPU.load()`的返回值
* `threshold`: 概率阈值， 只有是这个物体的概率大于这个值才会输出结果， 取值范围：[0, 1]
* `nms_value`: box_iou 门限, 为了防止同一个物体被框出多个框，当在同一个物体上框出了两个框，这两个框的交叉区域占两个框总占用面积的比例 如果小于这个值时， 就取其中概率最大的一个框
* `anchor_num`: anchor 的锚点数， 这里固定为 `len(anchors)//2`
* `anchor`: 锚点参数与模型参数一致，同一个模型这个参数是固定的，和模型绑定的（训练模型时即确定了）， 不能改成其它值。

#### 返回值

* `success`： `bool`类型， 是否成功


### deinit

释放模型占用的内存， 立即释放， 但是变量还在，可以使用`del kpu_net_object` 的方式删除，
另外也可以直接只使用`del kpu_net_object`来标记对象已被删除，下一次`GC`进行内存回收或者手动调用`gc.collect()`时，会自动释放内存

```python
KPU.deinit(kpu_net)
```

比如：

```python
import KPU as kpu
import gc
task = kpu.load(0x300000)
kpu.deinit(task)
del task
gc.collect()
```

或者：

```python
import KPU as kpu
import gc
task = kpu.load(0x300000)
del task
gc.collect()
```


#### 参数

`kpu_net`: `KPU.load()` 返回的 `kpu_net` 对象

#### 返回值

* `success`： `bool` 类型， 是否成功


### run_yolo2

```python
import KPU as kpu
import image
task = kpu.load(offset or file_path)
anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)
kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)
img = image.Image()
kpu.run_yolo2(task, img) #此处不对，请参考例程
```

#### 参数

* `kpu_net`: kpu_load 返回的 kpu_net 对象
* `image_t`：从 sensor 采集到的图像

##### 返回

* `list`: kpu_yolo2_find 的列表 

### forward

计算已加载的网络模型到指定层数，输出目标层的特征图

```python
fmap=KPU.forward(kpu_net, img, end_layer)
```

```python
import KPU as kpu
task = kpu.load(offset or file_path)
……
fmap=kpu.forward(task,img, 3)
```

#### 参数

* `kpu_net`: kpu_net 对象
* `img`: 图像 `image.Image` 对象
* `end_layer`: 指定计算到网络的第几层， 取值从`0`开始

##### 返回

* `fmap`: 特征图对象，内含当前层所有通道的特征图


### fmap

取特征图的指定通道数据到`image.Image`对象

```python
img=KPU.fmap(fmap, channel)
```

#### 参数

* `fmap`: 特征图 对象
* `channel`: 指定特征图的通道号, 从`0`开始

##### 返回

* `img`: 特征图对应通道生成的灰度图，类型`image.Image`


### fmap_free

释放特征图对象

```python
KPU.fmap_free(fmap)
```

#### 参数

* `fmap`: 特征图 对象

##### 返回

* 无

### netinfo 

获取模型的网络结构信息

```python
info_list = kpu.netinfo(task)
```

#### 参数

* `kpu_net`: kpu_net 对象, `KPU.load()`返回值

##### 返回

* `info_list`：所有层的信息list, 包含信息为：
  * `index`：当前层在网络中的层数
  * `wi`：输入宽度
  * `hi`：输入高度
  * `wo`：输出宽度
  * `ho`：输出高度
  * `chi`：输入通道数
  * `cho`：输出通道数
  * `dw`：是否为depth wise layer
  * `kernel_type`：卷积核类型，0为1x1， 1为3x3
  * `pool_type`：池化类型，0不池化; 1：2x2 max pooling; 2:...
  * `para_size`：当前层的卷积参数字节数


### set_outputs

```python
success = set_outputs(kput_net, out_idx, width, height, channel)
```

手动设置输出层形状， 对于 nncase v0.2.0 转换出来的 V4 的 kmodel 模型，
在 `load` 之后需要调用此函数手动设置输出层形状， V3 模型不需要


#### 参数

* `kpu_net`: kpu_net 对象
* `out_idx`: 输出层下表， 从 `0` 开始， 比如第一层输出层是`0`
* `width`： 层宽度， 如果是一维输出，则为`1`
* `height`: 层高度， 如果是一维输出，则为`1`
* `channnel`： 层通道数，如果是一维输出，则这里为一维输出的长度

##### 返回

* `success`： 是否设置成功， 如果不成功，注意看输出的提示信息， 参考[错误代码](https://github.com/sipeed/MaixPy/blob/fa3cf2c96353fa698e9386e42be8b3c9cf495114/components/kendryte_sdk/include/sipeed_kpu.h#L6-L23)


### memtest

打印内存使用情况，包括`GC`内存和系统堆内存

* 注意执行这个函数会自动先执行`gc.collect()`进行内存回收一次，再打印`GC`剩余内存
* 系统堆内存只做参考，不一定准确，有时可能出现已经释放了内存，但是显示依然没有释放，以实际能不能分配到内存为准

```python
KPU.memtest()
```
### face_encode

将 `forward` 返回的特征图进行量化，更多详情请查看：[kpu issue](https://github.com/sipeed/MaixPy/issues/342)

```python
feature = kpu.face_encode(fmap[:])
```

#### 参数

`fmap[:]`：`list` 类型，将 `forward` 函数返回值转化为列表所得到的

#### 返回值

`feature`：`list` 类型，量化后的列表

### face_compare

将 face_encode 返回的量化值与已录入的人脸进行比较

```python
score = kpu.face_compare(record_ftrs[j], feature)
```

#### 参数

`record_ftrs[j] `：`list` 类型，以录入的人脸数据
`feature`：`list` 类型，需要比较的人脸数据， `face_encode` 的返回值

#### 返回值

`score`：`int` 类型，比较得分（0~100），得分越高相似度越大




