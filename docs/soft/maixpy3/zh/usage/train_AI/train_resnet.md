# 这是用于训练 v831 分类模型的仓库

> 本文当目前针对 V831 系列产品，请注意产品与模型的匹配性。


## 训练环境搭建

由于训练需要用到显卡，关于安装显卡驱动、CUDA、CUDNN、OpenCv 请自行百度查阅安装，本文不做详细说明。本文章是在 Ubuntu 环境下，使用英伟达 GTX1080 显卡所编写完成的，请以该环境为参考。

需要安装的软件包介绍：
- PyTorch ：基础训练框架。
- onnx2ncnn ：模型转换工具。
- torchsummary ： 格式化打印模型信息。

文章参考：

* 显卡驱动安装：https://neucrack.com/p/252
* opencv 多版本共存：https://neucrack.com/p/349


### 安装pytorch 、torchsummary

进入 Pytorch 下载帮助[网页](https://pytorch.org/get-started/locally/)，根据自己所用系统的环境情况，选择对应的 CUDA 版本和安装包的类型，这里所选用的是 CUDA 10.2、Linux 系统、稳定版、pip包
```python
pip3 install torch torchvision torchaudio
```

然后再通过 pip 进行安装 torchsummary

```python 
pip install torchsummary
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

## 图像分类模型训练过程

图像分类主要采用的模型是 resnet18 ，由 PyTorch 架构训练完成，经由网络模型转换后部署到 v831 上。

**流程**是： PyTorch 训练 → onnx 模型 → ncnn 模型 → 在线工具量化 → v831 模型

### 准备

#### 获取训练工程文件

可以在 GitHub 上下载压缩包或者是通过 git 克隆到本地

    git clone https://github.com/dianjixz/v831_restnet18

工程文件结构介绍：
~~~ bash
├── classes_label.py                            #分类标签
├── classifier_resnet_test.py                   #测试程序
├── classifier_resnet_train.py                  #训练程序
├── convert.py                                  #模型转换程序
├── convs_data                                  #上传文件夹
├── convs_data.zip                              #上传的压缩包
├── data                                        #训练数据文件夹
│   ├── mouse                                  #分类文件夹
│   └── sipeed_logo
├── out                                         #训练模型输出文件夹，每隔一定训练周期输出一个模型参数
│   ├── classifier_19.pth
│   ├── classifier_39.pth
│   └── classifier_59.pth
├── restnet_img.jpeg
└── test                                        #测试数据集文件夹（不分类别）
7 directories, 921 files

~~~


#### 数据集的制作与使用



打开 resnet18 工程中的 classifier_resnet_train.py 文件。以下是训练时需要注意的一些参数。

修改 classes_label.py 文件中的 labels 值和 data 文件夹中的目录对应

~~~ python
dataset_path = "data/datasets"		#训练集的路径（保持默认）
val_split_from_data = 0.1 # 10%		#学习率（保持默认）
batch_size = 4						#训练批次，不需要改动（保持默认）
learn_rate = 0.001	                #学习率，不需要改动（保持默认）
total_epoch = 100					#训练循环，总共需要训练100个循环（保持默认）
eval_every_epoch = 5				#每个循环训练次数（保持默认）
save_every_epoch = 20				#多少个循环保存一次（保持默认）
dataload_num_workers = 2			#（保持默认）
input_shape = (3, 224, 224)			#输入尺寸（保持默认）
cards_id = [0]					#使用的训练卡（保持默认）
param_save_path = './out/classifier_{}.pth'	#参数保存路径（保持默认）
~~~

data 文件是训练数据集，test 文件是测试数据。注意两个数据集中不要有重复的图片。

训练数据集：一个分类一个文件夹， 文件夹名字就是分类的名字。

~~~ c
数据集文件夹结构
── mouse
│   ├── 20026.jpg
...
├── sipeed_logo
│   ├── 19418.jpg
...
...
~~~



### 训练:


~~~ bash
python classifier_resnet_train.py  
~~~

训练完成后，会在工程目录下生成一个 out 文件夹，在 out 文件夹下存放着训练过程中保存的训练参数。

例如：
~~~ bash
.
├── classifier_99.pth             #训练过程中保存的参数
├── classifier_final.pth          #训练完成后保存的参数
└── classifier.onnx               #生成的onnx深度学习网络文件
~~~

### 测试  

准备好你的测试图片，注意和数据集中的图片尺寸一样。新建一个 test 目录，并放在该目录下。   

运行 `python classifier_resnet_test.py images_folder_path model_param_path` 命令进行测试。  .

在该命令中会调用用户环境中的 ncnn 工具，请确保已经安装好并加入环境变量。  

模型测试并生成 ncnn 模型文件：  
~~~ bash 
python classifier_resnet_test.py ./test ./out/classifier_final.pth
~~~


运行完测试后，会生成 ncnn 模型和 ncnn 模型参数。
~~~
nihao@nihao:~/work/work_space/v831_restnet18/out$ ls
classifier_2.pth  classifier.bin  opt.bin
classifier_1.pth  classifier.onnx  opt.param
classifier_3.pth  classifier.param  opt.table
~~~

生成的 ncnn 模型此时还无法被 v831 直接使用，需要经过在线 maixhub 量化为 int8 模型才可以被使用。

### 模型转换  

在线转换需要上传一个压缩包文件.  
- 该功能只能支持上传一个无密码的 zip 压缩包  
- 压缩包内需要包含一个 images 目录，一个 xxx.bin，一个 xxx.param  
- 需要将矫正图片放入 images 目录内；矫正图片集可考虑直接采用训练中的验证数据集，并务必保证矫正时图像的预处理方式与训练和部署时一致。  
> 注意：确保 images 目录内没有混入其他文件，否则会导致模型量化错误。

zip 压缩包目录结构
~~~ bash
└─xxxx.zip
    |─ images
    |    |- xxx.jpg
    |    |- ...
    |    ...
    |
    |- xxx.bin
    └─ xxx.param
~~~

制作好压缩包后打开网址: [https://maixhub.com/modelConvert](https://maixhub.com/modelConvert) 查看使用说明。  

![](https://neucrack.com/image/1/358/maixhub.jpg)  

登陆后,上传你的压缩包等待模型转换任务完成。    

### 分类模型部署  

等待模型转换完成,下载转换好的模型文件。得到的 *.param 和 *.bin 文件就是部署在 v831 上的文件。 

将模型文件上传到 v831 上。

打开示例代码,替换模型文件名,分类标签和模型加载参数,然后运行即可。

~~~ python
#!/usr/bin/python3
#在v831运行的1000分类事例代码
from maix import nn, display, camera, image
from classes_label import labels    #分类标签,需要替换
import time


model = {
    "param": "/root/restnet18_int8.param",        #模型文件,需要替换成自己训练的模型
    "bin": "/root/restnet18_int8.bin"
}
options = {
    "model_type":  "awnn",
    "inputs": {
        "input0": (224, 224, 3)
    },
    "outputs": {
        "output0": (1, 1, len(labels))           #模型输出宽度,请输入你自己的类别数量,1000分类为(1,1,1000),10分类为(1,1,10)
    },
    "first_layer_conv_no_pad": False,
    "mean": [127.5, 127.5, 127.5],
    "norm": [0.00784313725490196, 0.00784313725490196, 0.00784313725490196],
}

print("-- load model:", model)
m = nn.load(model, opt=options)
print("-- load ok")

while True:
    img = camera.capture()
    AI_img = img.copy().resize(224, 224)
    t = time.time()
    out = m.forward(AI_img.tobytes(), quantize=True)
    t = time.time() - t
    print("-- forward time: {}s".format(t))
    msg = "{}%: {}".format(int(out.max() * 10), labels[out.argmax()])
    print(msg)
    img.draw_string(0, 0, msg, color = (255, 0, 0))
    display.show(img)
~~~

运行效果：  
![](./restnet_img.jpeg)

分类训练说明到此结束.