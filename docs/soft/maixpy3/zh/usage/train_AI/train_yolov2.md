# 这是用于训练 MaixII-Dock 检测模型的仓库

| 时间 | 负责人 | 更新内容 | 备注 |
| --- | --- | --- | :---: |
| 2022年1月22日 | dianjixz | 编写初稿文档 | 训练教程只能在 Linux 系统中运行，<br>并只能部署到 MaixII-Dock 开发板上运行，<br>文档还需要二次整理 |

> Windows 系统暂不支持！

## 训练环境搭建

由于训练需要用到显卡，关于安装显卡驱动、CUDA、CUDNN、OpenCv 请自行百度查阅安装，本文不做详细说明。本文章是在 Ubuntu 环境下，使用英伟达 GTX1080 显卡所编写完成的，请以该环境为参考。

需要安装的软件包介绍：
- PyTorch ：基础训练框架。
- onnx2ncnn ：模型转换工具。
- torchsummary ： 格式化打印模型信息。

文章参考：

* 显卡驱动安装：https://neucrack.com/p/252
* opencv 多版本共存：https://neucrack.com/p/349


### 安装pytorch 、torchsummary、pycocotools

进入 Pytorch 下载帮助[网页](https://pytorch.org/get-started/locally/)，根据自己所用系统的环境情况，选择对应的 CUDA 版本和安装包的类型，这里所选用的是 CUDA 10.2、Linux 系统、稳定版、pip包
```python
pip3 install torch torchvision torchaudio
```

然后再通过 pip 进行安装 torchsummary、pycocotools

```python 
pip3 install torchsummary pycocotools
```


### 编译 onnx2ncnn 工具

安装编译环境所需要用到的软件包

    sudo apt install build-essential git cmake libprotobuf-dev protobuf-compiler libvulkan-dev vulkan-utils libopencv-dev

需要先拉取整个 ncnn 转换工具的工程，在任意的文件夹位置中

    git clone https://github.com/Tencent/ncnn.git

工程编译初始化

    cd ncnn
    git submodule update --init

开始编译 onnx2ncnn 工具

    mkdir build
    cd build
    cmake -DCMAKE_BUILD_TYPE=Release -DNCNN_VULKAN=ON -DNCNN_SYSTEM_GLSLANG=OFF -DNCNN_BUILD_EXAMPLES=ON ..
    make

编译结束之后，可以在 ncnn/build/tools/onnx 目录下，能得到 **onnx2ncnn** 模型转换工具，将该可执行文件加入到环境变量中方便使用。

在 ~/.bashrc 中添加下面内容，将 **onnx2ncnn** 加入环境变量：
~~~
#!/bin/bash

export PATH=$PATH:`pwd`/tools/onnx
~~~


## 图像检测

图像检测主要采用的模型是 YOLOv2 ，由 PyTorch 平台训练完成，经由网络模型转换后部署到 MaixII-Dock 上。  

### 数据集准备  

YOLOv2 默认使用 voc 格式的数据集,文件夹取名为 custom 放到 data 目录下, 比如:
~~~ bash
#voc格式的yolo训练数据集
├── custom    #数据集文件夹名
│   ├── Annotations		#标注文件
│   ├── ImageSets		#训练参数划分
│   │    └── Main
│   │         ├── train.txt
│   │         └── val.txt
│   ├── JPEGImages		#训练图片
~~~

train.txt 和 val.txt 中, 每一行是一个数据(图像)名, 路径相对于 `JPEGImages`
~~~ bash
train.txt 写着用于训练的图片名称
val.txt  写着用于验证的图片名称
~~~
**修改配置**

修改 `data/custom.py` 中的 `CUSTOM_CLASSES` 变量为正确的 `labels`
~~~ python
CUSTOM_CLASSES = [
    "mouse",
    "sipeed_logo"
]
~~~

### 使用显卡训练

~~~ bash
python train.py -d custom --cuda -v slim_yolo_v2 -hr -ms
~~~

[//]: # "或者安装好horovod, 然后多卡训练"
[//]: # "~~~ bash"
[//]: # "horovodrun -np 4 python train.py -d custom --cuda -v slim_yolo_v2 -hr -ms"
[//]: # "~~~"

训练完成后会在 weights/custom/slim_yolo_v2 目录下生成训练中保存的参数

### 导出模型

~~~ bash
python test.py -d custom -v slim_yolo_v2 --trained_model weights/custom/slim_yolo_v2/slim_yolo_v2_1000.pth --visual_threshold 0.3 -size 224 --export
~~~

运行导出模型命令后会在 out 目录下生成 test 测试图片效果和模型文件,模型转换请参考上面模型转换章节.

### 模型部署  
等待模型转换完成,下载转换好的模型文件.  
得到的 *.param 和 *.bin 文件就是部署在 MaixII-Dock 上的文件.  
打开事例代码,替换模型文件名,分类标签和模型加载参数,然后运行即可. 
~~~ python
#检测示例代码

from maix import nn, camera, image, display
from maix.nn import decoder
import time

model = {
    "param": "/root/yolov2_int8.param",
    "bin": "/root/yolov2_int8.bin"
}
options = {
    "model_type":  "awnn",
    "inputs": {
        "input0": (224, 224, 3)
    },
    "outputs": {
        "output0": (7, 7, (1+4+2)*5)    #输出参数修改,修改格式 (7 ,7 , (1 + 4 + "类别数量" ) * 5)
    },
    "mean": [127.5, 127.5, 127.5],
    "norm": [0.0078125, 0.0078125, 0.0078125],
}

labels = ["mouse","sipeed_logo"]            #分类标签
anchors = [1.19, 1.98, 2.79, 4.59, 4.53, 8.92, 8.06, 5.29, 10.32, 10.65]

m = nn.load(model, opt=options)
yolo2_decoder = decoder.Yolo2(len(labels), anchors, net_in_size=(options["inputs"]["input0"][0], options["inputs"]["input0"][1]), net_out_size=(7, 7))

while True:
    img = camera.capture()
    AI_img = img.copy().resize(224, 224)
    out = m.forward(AI_img.tobytes(), quantize=True, layout="hwc")
    boxes, probs = yolo2_decoder.run(out, nms=0.3, threshold=0.3, img_size=(options["inputs"]["input0"][0], options["inputs"]["input0"][1]))

    if len(boxes):
        for i, box in enumerate(boxes):
            class_id = probs[i][0]
            prob = probs[i][1][class_id]
            disp_str = "{}:{:.2f}%".format(labels[class_id], prob*100)
            img.draw_rectangle(box[0], box[1], box[0] + box[2], box[1] + box[3], color = (255, 255, 255))
            x = box[0]
            y = box[1] - 20
            if y < 0:
                y = 0
            img.draw_string(x, y, disp_str, color = (255, 255, 255))

    display.show(img)


~~~

运行效果图:

![](./dnn/yolo_test.jpg)

检测说明到此结束。
