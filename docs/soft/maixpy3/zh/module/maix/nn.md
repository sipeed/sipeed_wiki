---
title: MaixPy3 nn模块(maix.nn)
keywords: MaixPy3, maix.nn, MaixPy3运行模型, maix.nn API
desc: MaixPy3 nn模块 API文档, 以及使用说明
---

>! API 仍处于非稳定状态, 可能在未来会有小幅改动

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

加载模型, 返回 `maix.Model` 对象

### 参数

* `model_path`: 模型路径, 可以是字符串或者字典的形式, 目前只支持字典形式
比如:
```python
{
    "param": "/root/models/sobel_int8.param",
    "bin": "/root/models/sobel_int8.bin"
}
```

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
  * `mean`: 如果在`forward`使参数`quantize=True`, 则会使用这个参数对输入数据进行归一化, 计算方法为`(x - mean) * norm`; 格式为`list` 或者 `float`(未支持, 欢迎提交 PR)
  * `norm`: 看`mean`

### 返回值

返回 `maix.Model` 对象


## 类 maix.Model

包含了一系列神经网络操作,  `maix.nn.load()` 会返回其对象

### maix.Model.forward()

只能由具体的对象调用, 不能类直接调用

#### 参数

* `inputs`: 输入, 但输入层直接输入数据对象, 可以是`Pillow`的`Image`对象, 也可以是`HWC`排列的`bytes`对象, 也可以是`numpy.ndarray`对象, 多层输入使用`list`
* `quantize`: 为`True`, 会使用 `load()` 时 `opt` 的`mean norm`参数对数据进行归一化, 并进行`int8`量化； `False`则不会对输入数据进行处理, 则输入需要先自己手动规范量化到`-128~127`范围.  
>! 这个参数未来可能会进行优化, 将归一化和量化分开

* `layout`: `"hwc"` 或者 `"chw"`(默认, 推荐)

#### 返回值

特征图, 如果是单层输出, 是一个浮点类型的 `numpy.ndarray` 对象, 如果是多层输出, 会是一个`list`对象, 包含了多个`numpy.ndarray`对象.


### maix.Model.__del__()

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
    def __init__(self, anchors):
        pass

    def run(self, fmap, nms = 0.3, thresh = 0.5, img_size = None):
        boxes = []
        probs = []
        for x, y, w, h, _probs in valid_results:
            if img:
                x = (x - w/2) * img_size[0]
                y = (y - h/2) * img_size[1]
                w *= img_size[0]
                h *= img_size[1]
                x, y, w, h = int(x), int(y), int(w), int(h)
            boxes.append((x, y, w, h))  # item type is float if img_size == 0, else int type
            probs.append(_probs)        # probs is list type, item type is float
        return [np.array(boxes), np.array(probs)]

```

使用时:

```python
from maix.nn.decoder import Yolo2

labels = ["A", "B", "C"]
anchors = [1.19, 1.98, 2.79, 4.59, 4.53, 8.92, 8.06, 5.29, 10.32, 10.65]

yolo2_decoder = Yolo2(anchors)
...
out = m.forwar(img, layout="hwc")
boxes, probs = yolo2_decoder.run(out, thres=0.5, nms=0.3, img_size=(img.width, img.height))
for i, box in enumerate(boxes):
    class_id = probs[i].argmax()
    disp_str = "{}:{:.2f}%".format(labels[class_id], probs[i][class_id]*100)
    print("final box: {}, {}".format(box, disp_str))

```

