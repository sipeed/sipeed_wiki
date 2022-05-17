---
title: MaixPy3 nn模块(maix.nn)
keywords: MaixPy3, maix.nn, MaixPy3运行模型, maix.nn API
desc: MaixPy3 nn模块 API文档, 以及使用说明
---

>! API 仍处于非完全稳定状态, 可能在未来会有小幅改动, 如果你遇到了语法错误， 记得回来看更新哦~

## maix.nn 基本使用介绍

* 准备模型

比如从 maixhub 下载, 这里以边缘检测模型为例, 先[下载模型](https://maixhub.com/modelInfo?modelId=24)(需要先注册登录)

* 准备一张 `224 x 224` 分辨率的图像, 比如这里放到了开发板文件系统的`/root/test.png`位置

* 运行代码, 将下面的代码保存到开发板的`test_model.py`中, 然后运行`python test_model.py`

其中最重要的就是`m = nn.load`和`m.forward()`两个函数, 即加载模型, 和进行模型前向推理

```python
from maix import nn, display
from PIL import Image
import numpy as np

test_jpg = "/root/test.png"

model = {
    "param": "/root/models/sobel_int8.param",
    "bin": "/root/models/sobel_int8.bin"
}

input_size = (224, 224, 3)
output_size = (222, 222, 3)

options = {
    "model_type":  "awnn",
    "inputs": {
        "input0": input_size
    },
    "outputs": {
        "output0": output_size
    },
    "mean": [127.5, 127.5, 127.5],
    "norm": [0.0078125, 0.0078125, 0.0078125],
}
print("-- load model:", model)
m = nn.load(model, opt=options)
print("-- load ok")

print("-- read image")
img = Image.open(test_jpg).resize(input_size[:2])
print("-- read image ok")
print("-- forward model with image as input")
out = m.forward(img, quantize=True)
print("-- forward ok")
out = out.astype(np.float32).reshape(output_size)
out = (np.abs(out) * 255 / out.max()).astype(np.uint8)
img2 = Image.fromarray(out, mode="RGB")

display.show(img2)
```

## 方法 maix.nn.load()

加载模型, 返回 `maix.nn.Model` 对象

### 参数

* `model_path`: 模型路径, 包含了字符串和字典两种形式

字典形式：
```python
{
    "param": "/root/models/sobel_int8.param",
    "bin": "/root/models/sobel_int8.bin"
}
```

字符串形式:
```python
model_path = "/root/mud/sobel_int8.mud"
```

>! 特别说明，MUD文件是模型统一描述文件，后文有[详细描述](https://wiki.sipeed.com/soft/maixpy3/zh/api/maix/nn.html#MUD%E6%96%87%E4%BB%B6)

* `opt`: 设置项, 字典形式, 包括了:
  * `model_type`: 模型类别, 目前仅支持 `awnn`
  * `inputs`: 输入层, 字典形式, 关键字是层名称, 为字符串, 如果是加密模型, 需要使用整型; 值是层形状, 为一个`tuple`类型:`(h, w, c)`. 目前只支持单层输入层(未来会支持多层输入, 欢迎提交 `PR`)
  比如:
```python
    # 未加密模型
    "inputs": {
        "input0": (224, 224, 3)
    }
    # 加密模型
    "inputs": {
        0: (224, 224, 3)
    }
```
  * `outputs`: 输出层, 同理输入层. 支持多层输出
  * `mean`: 如果在`forward`使参数`standardize=True`（默认为True）, 则会使用这个参数对输入数据进行归一化, 计算方法为`(x - mean) * norm`; 格式为`list` 或者 `float`(未支持, 欢迎提交 PR)
  * `norm`: 定义参见上述`mean`描述
>! 当`model_path`选择字符串格式时， 此项`opt`不用进行赋值，默认为None

### 返回值

返回 `maix.nn.Model` 对象


## 类 maix.nn.Model

包含了一系列神经网络操作,  `maix.nn.load()` 会返回其对象

### maix.nn.Model.forward()

只能由具体的对象调用, 不能类直接调用

#### 参数

* `inputs`: 输入, 可以是`_maix_image`的`Image`对象, 也可以是`HWC`排列的`bytes`对象, 也可以是`HWC`排列的`numpy.ndarray`对象(还未支持), 多层输入使用`list`(还未支持)
>! 这个参数未来可能会进行优化
* `standardize`: `int` 类型,默认为`1`, 当`load()`加载字典类型时， `opt` 的`mean,norm`参数对数据进行标准化；当`load()`加载字符串类型时，会根据mud文件自动进行标准化；置为`0`时不会对输入数据进行处理，则输入前需要将数据进行手动处理，处理方式跟模型训练时的数据处理一致 

* `layout`: `"hwc"` 或者 `"chw"`， 默认设置为 `"hwc"`
* `debug`: `int` 类型，默认为`0`,该值不为`0`时会打印`debug`信息和`forward`的推理耗时 

#### 返回值

特征图, 如果是单层输出, 是一个浮点类型的 `numpy.ndarray` 对象, 如果是多层输出, 会是一个`list`对象, 包含了多个`numpy.ndarray`对象.


### maix.nn.Model.__del__()

删除对象, 内存回收时会自动调用这个函数, 会释放模型占用的资源
```python
del m
```

## 模块 maix.nn.decoder

`nn` 后处理模块, 集成了常见的模型的后处理, 使用 `forward` 进行模型推理后得到特征图输出, 使用这个模块下的方法对输出的特征图进行后处理

### 类 maix.nn.decoder.Yolo2

`YOLO V2` 的后处理模块, 使用时需要创建一个对象,调用`run`方法对模型推理输出进行解码得到物体的坐标和类别.

等价于如下`python`伪代码:

```python
class Yolo2:
    def __init__(self, class_num, anchors, net_in_size=(224, 244), net_out_size=(7, 7)):
        pass

    def run(self, fmap, nms = 0.3, threshold = 0.5, img_size = None):
        boxes = []
        probs = []
        for x, y, w, h, _probs in valid_results:
            if img:
                x *= img_size[0]
                y *= img_size[1]
                w *= img_size[0]
                h *= img_size[1]
                x, y, w, h = int(x), int(y), int(w), int(h)
            boxes.append([x, y, w, h])  # item type is float if img_size == 0, else int type
            probs.append([max_probs_index, _probs]) # probs is list type, item type is float
        return [boxes, probs]

```

使用时:

```python
from maix.nn import decoder

labels = ["A", "B", "C"]
anchors = [1.19, 1.98, 2.79, 4.59, 4.53, 8.92, 8.06, 5.29, 10.32, 10.65]

yolo2_decoder = decoder.Yolo2(len(labels), anchors)
yolo2_decoder.run(bytes([0]*10))

...

out = m.forwar(img, layout="hwc")
boxes, probs = yolo2_decoder.run(out, thres=0.5, nms=0.3, img_size=(img.width, img.height))
for i, box in enumerate(boxes):
    class_id = probs[i][0]
    prob = probs[i][1][class_id]
    disp_str = "{}:{:.2f}%".format(labels[class_id], prob*100)
    print("final box: {}, {}".format(box, disp_str))

```

#### maix.nn.decoder.Yolo2.__init__()

构造对象时会自动调用

##### 参数


* `class_num`: 类别数量
* `anchors`: 预选框, `list` 类型, 数量为偶数, 必须要和训练时使用的`anchors` 相同, 也就是说跟模型绑定的参数, 如果你不知道, 请找提供模型的人提供
* `net_in_size`: 网络输入层分辨率
* `net_out_size`: 网络输出层分辨率



#### maix.nn.decoder.Yolo2.run()

执行解码(后处理), 只能对象进行调用, 不能类直接调用

##### 参数

* `fmap`: 网路输出的特征图, 一般是`forward` 函数的结果
* `nms`: 非极大值抑制(Non-Maximum Suppression), 用来去掉重复的框, `IOU`(两个框的重叠区域)大于这个值就只取概率大的一个, 取值范围:`[0, 1]`, 默认值为 `0.3`
* `threshold`: 置信度阈值, 大于这个值才认为物体有效, 取值范围:`[0, 1]`, 默认 `0.5`
* `img_size`: 源图像大小, `tuple`类型, 比如`(320, 240)`, 这会使返回值的`box` 坐标自动计算为相对于源图的坐标, 并且类型为整型, 默认`None` 则不会计算, `box` 返回相对值(百分比), 浮点类型, 范围:`[0, 1]`


##### 返回值

`[boxes, probs]`, `list` 类型, 可以参考上面的使用例子, 其中:

* `boxes`: `list` 类型, 每个元素也是一个`list`, 包含`[x, y, w, h]`, 分别代表了框左上角坐标, 以及框的宽高
* `probs`: `list` 类型, 每个元素也是一个`list`, 包含`[max_prob_idx, all_classes_probs]`
  * `all_classes_probs`: `list` 类型, 包含了该框所有类别的置信度
  * `max_prob_idx`: 整型, 代表了`all_classes_probs`中最大值的下标, 取值范围: `[0, classes_num - 1]`





## 模块 maix.nn.app

应用模块， 包含了一些有意思的应用模块

### 模块 maix.nn.app.classifier

自学习分类器（视觉）， 无需训练模型， 只使用特征提取模型， 在运行时学习多个物体特征，然后即可对物体进行分类识别。 适用于简单的分类场景。

`maix.nn.app.classifier`的`python`伪代码:

```python
class Classifier:
    def __init__(self, model, class_num, sample_num, feature_len, input_w, input_h):
        pass

    def add_class_img(self, img):
        return idx

    def add_sample_img(self, img):
        return idx

    def train(self):
        pass

    def predict(self, img):
        return idx, min_dist

    def save(self, path):
        pass

def load(model, path):
    return Classifier()

```

#### 类 Classifier

使用时需要指定类别数量，通过`add_class_img`函数传入物体图像来获得物体的特征值， 然后通过`add_sample_img`获取这几个类别的图像，用以对开始采集的图像特征值进行优化， `sample`的图像和开始采集的类别图像可以有一定的差异， 但是不要相差太大， 采集的顺序无所谓；
然后调用`train`方法进行训练(其实就是`kmeans` 聚类)， 就可以得到使用`sample`图像特征值优化过后的几个分类的特征值；
最后使用`predict`就可以对输入图像的类别进行识别

##### 构造方法： __init__(self, model, class_num, sample_num, feature_len, input_w, input_h)

* 参数：
  * `model`: `maix.nn.Model`对象， 用于获得图片的特征值
  * `class_num`: 要学习的物体类别数量， 比如 `3`
  * `sample_num`: 用以学习特征的物体数量， 比如`3*5 => 15`
  * `feature_len`: 特征值的长度， 取决于特征提取模型的输出形状， 比如例程使用`resnet18 1000 分类`模型， 倒数第二层输出长度是`512`
  * `input_w`: 输入的图像的宽度
  * `input_h`: 输入的图像的高度

##### 方法: add_class_img(self, img)

添加分类图片， 会自动调用模型推理获取图片的特征值

* 参数：
  * `img`: 输入图像， 可以是`Pillow`的`Image`对象, 也可以是`HWC`排列的`bytes`对象

* 返回值： `int` 类型, 代表返回成功添加第几个类别的特征值， 取值∈`[0, class_num)`

* 抛出错误： 如果出现错误， 比如添加图片超过类别数量等， 会抛出错误信息


##### 方法: add_sample_img(self, img)

添加样本图片， 会自动调用模型推理获取图片的特征值

* 参数：
  * `img`: 输入图像， 可以是`Pillow`的`Image`对象, 也可以是`HWC`排列的`bytes`对象

* 返回值： `int` 类型, 代表返回成功添加第几个样本图片的特征值， 取值∈`[0, sample_num)`

* 抛出错误： 如果出现错误， 比如添加图片超过设置的样本数量等， 会抛出错误信息


##### 方法: train(self)

训练样本（本质上是聚类分类）， 需要在`add_class_img`和`add_sample_img`完成后才能调用，否则会出现误差


* 抛出错误： 如果出现错误， 比如类别或者样本采集未完成， 会抛出错误信息


##### 方法： predict(self, img)

预测给定的图片所属的类别

* 参数：
  * `img`: 输入图像， 可以是`Pillow`的`Image`对象, 也可以是`HWC`排列的`bytes`对象

* 返回值：
  * `idx`: `int` 类型, 代表给定的图片的特征和这个分类最接近， 取值∈`[0, sample_num)`
  * `min_dist`: 图片的特征和`idx`类别的特征的距离， 距离越小则代表和该类越相似

* 抛出错误： 如果出现错误， 比如参数错误等， 会抛出错误


##### 方法： save(self, path)

保存当前的特征值参数到文件， 方便断电保存并下次加载使用

* 参数：
  * `path`: 保存的路径， 字符串

* 抛出错误： 保存出错， 会抛出错误信息


#### 方法 load(model, path)

加载保存的特征值参数文件， 获得[类 Classifier](#类-Classifier)的对象， 加载完成后可直接使用`predict`函数

* 参数：
  * `model`: `maix.nn.Model`对象， 用于获得图片的特征值， 需要和保存的时候使用的模型相同
  * `path`: 保存参数的路径

* 返回值： 获得[类 Classifier](#类-Classifier)的对象


### 模块 maix.nn.app.face

人脸识别模块， [这里](https://github.com/sipeed/MaixPy3/blob/main/ext_modules/_maix_nn/example/face_recognize.py)有一个`Face_Recognizer`类提供了人脸识别的简单封装， 推荐使用

#### 类 FaceRecognize

伪代码：

```python
class FaceRecognize:
  def __init__(self, model_detect, model_fea, fea_len, input_shape, threshold, nms, max_face_num)
    pass

  def get_faces(self, img, std_img = False):
    return [ prob, [x,y,w,h], [[x,y], [x,y], [x,y], [x,y], [x,y]], feature ]

  def compare(self, feature_a, feature_b):
    return score
```

[这里](https://github.com/sipeed/MaixPy3/blob/main/ext_modules/_maix_nn/example/face_recognize.py)有一个`Face_Recognizer`类提供了人脸识别的简单封装， 推荐使用

使用的模型可以到[这里下载](https://maixhub.com/modelInfo?modelId=29)

##### 构造方法: __init__(self, model_detect, model_fea, fea_len, input_shape, threshold, nms, max_face_num)


* 参数
  * `model_detect`: 检测模型， [maix.nn.Model](#类-maix.nn.Model) 对象
  * `model_fea`: 特征提取模型， [maix.nn.Model](#类-maix.nn.Model) 对象
  * `fea_len`: 人脸特征的长度，比如 `256`
  * `input_shape`: 输入图像的形状，`(w, h, c)`格式， 比如`(224, 224, 3)`
  * `threshold`: 人脸检测阈值， 默认`0.5`
  * `nms`: 人脸检测非极大值抑制值，即用来防止重复框一个人脸， 默认`0.3`
  * `max_face_num`: 支持的同时框的人脸数量，取`1`或者更多

##### 获取人脸信息: get_faces(self, img, std_img = False)

获取人脸信息， 包括位置和特征值等

* 参数
  * `img`: 输入图像， 分辨率需要和检测模型的输入相同，  比如`224 x 224`， 可以是`PIL.Image.Image`对象， 或者`bytes`对象
  * `std_img`: 取值`True`或者`False`, 选择是否返回纠正过的标准人脸图片

* 返回值: 返回一个 `list` 对象，`[ prob, box, landmarks, feature, std_img ]`，其中`std_img`根据构造函数的参数`std_img`决定是否存在
  * `prob`: 检测到人脸的概率， 比设置的`threshold`大
  * `box`: 人脸框， 值为`[x,y,w,h]` ， 分别代表左上角坐标和框的宽高
  * `landmarks`: 人脸关键点， 共`5`个点, 格式`[[x,y], [x,y], [x,y], [x,y], [x,y]]`，分别代表了左眼、右眼、鼻子、左嘴角、右嘴角的坐标
  * `feature`: 人物脸的特征值， 一个`list`，`list`中的项目值类型为`float`（未来有可能会有`feature`为`bytes`的可选项）
  * `std_img`: 人脸图像，`PIL.Image.Image`对象， 只有当构造函数的参数`std_img`为`True`时才会有这个返回值

##### 对比人脸特征: compare(self, feature_a, feature_b)

对比两个人脸特征值相似度，并返回相似度百分比

* 参数
  * `feature_a`: `get_faces`函数的返回值, 一个`list`对象或者`bytes`对象
  * `feature_b`: `get_faces`函数的返回值, 一个`list`对象或者`bytes`对象

* 返回值： 返回两个人脸特征值的对比相似度分数（百分比），取值范围 `∈` `[0.0, 100.0]`

## MUD文件

MUD 文件是模型统一描述文件，全称 model universal description file ；mud 文件可以简化模型运行 Python 代码，还可以使得不同平台的模型文件使用同一份代码运行

### 文件形式

文件以 .mud 为后缀，严格按照 INI 的格式进行解析

### 文件内容

MUD 文件是按照既定顺序和内容进行解读。不同的 MUD 文件之间结构都非常类似，由若干段落（section）组成，在每个带括号的标题下面，是若干个以单个单词开头的关键词（keyword）和一个等号，等号右边的就是关键字对应的值（value); section部分通常用`[]`进行声明，例如：
```bash
[basic]
type = awnn
param =/root/models/awnn_retinaface.param
bin =/root/models/awnn_retinaface.bin

[inputs]
input0 = 224,224,3,127.5, 127.5, 127.5,0.0078125, 0.0078125, 0.0078125

[outputs]
output0 = 1,4,2058
output1 = 1,2,2058
output2 = 1,10,2058

[extra]
outputs_scale =
inputs_scale =
```

#### section & keywords
* [basic]: 基础参数段，包含了模型模型类型、模型参数、模型结构三种文件
    * type：不同目标平台的标识，如R329称为aipu，V831代称为awnn
    * bin：V831，R329 平台模型的参数二进制文件
    * param：V831的模型结构文件，R329融合了模型参数和模型结构故此项置为空

* [inputs] :输入信息段

  input ：输入节点名称，输入个数随模型而定，其前三个参数定义为 H,W,C ，后两个的参数以此是mean，norm 
    >! H != 1 && W != 1 && C == 3 的时候，输入为三通道图像，依次按照mean_R , mean_G ，mean_B ，norm_R ，norm_G ，norm_B 的顺序往后排列  
    >  H != 1 && W != 1 && C == 1 的时候，输入为灰度图， mean_gray , norm_gray ，按顺序两个值，进行排列  
    >  H ==  1 && W == 1 && C != 1 ，输入为三维向量， mean_v , norm_v ，按顺序两个值，进行排列  

* [outputs] :输出信息段

  output ：输出节点名称，输出节点个数根据模型而定，其参数定义为 H,W,C

* [extra]:额外的参数段，一般是不同平台额外的参数。
    *  inputs_scale：输入层在量化后的scale值，按照输入顺序排列 ，如inputs_scale = input0_scale , input1_scale, input2_scale ……
    *  outputs_scale：输出层在量化后的scale值，按照输出顺序排列，如outputs_scale = ouput0_scale , output1_scale , output2_scale …… （目前仅R329需要）

