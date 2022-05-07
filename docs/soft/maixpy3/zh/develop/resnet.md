# V831上部署resnet18分类网络

> 2022年01月11日 以下代码由于 MaixPy3 还在施工中，此处代码仅供参考和示范，功能已在 github 和 社区供其他同学使用和参考。

## 前期准备
在V831上使用resnet18分类网络，我们需要在linux环境下进行。windows系统可以使用虚拟机，或者是使用WSL，具体的安装教程请自行百度，这里就不过多的进行描述

### 安装pytorch环境

我们需要在系统中安装pytorch，通过在pytorch官网上可以知道安装pytorch需要执行

    pip3 install torch==1.9.0+cpu torchvision==0.10.0+cpu torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html

或者是通过conda环境进行安装

    conda install pytorch torchvision torchaudio cpuonly -c pytorch

我们还需要安装一个`torchsummary`库来进行神经网络的可视化

    pip3 install torchsummary

### 编译ncnn转换工具

通过 `git clone https://github.com/Tencent/ncnn.git` 将ncnn的仓库拉取到本地，进行编译

安装编译环境的依赖

```bash
sudo apt update
sudo apt install build-essential git cmake libprotobuf-dev protobuf-compiler libvulkan-dev vulkan-utils libopencv-dev
```
编译ncnn需要使用到 Vulkan 后端
要使用 Vulkan 后端，请安装 Vulkan 头文件、一个 vulkan 驱动程序加载器、GLSL 到 SPIR-V 编译器和 vulkaninfo 工具。或者从<https://vulkan.lunarg.com/sdk/home>下载并安装完整的 Vulkan SDK（大约 200MB；它包含所有头文件、文档和预构建的加载程序，以及一些额外的工具和所有源代码）

```bash
wget https://sdk.lunarg.com/sdk/download/1.2.182.0/linux/vulkansdk-linux-x86_64-1.2.182.0.tar.gz
tar xvf vulkansdk-linux-x86_64-1.2.182.0.tar.gz
export VULKAN_SDK=$(pwd)/1.2.182.0/x86_64
```

拉取ncnn的子仓库

```bash
cd ncnn
git submodule update --init
```

开始编译ncnn
```bash
mkdir -p build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DNCNN_VULKAN=ON -DNCNN_SYSTEM_GLSLANG=ON -DNCNN_BUILD_EXAMPLES=ON ..
make -j$(nproc)
```

编译结束之后会在build/tools/onnx/下的到onnx2ncnn可执行文件，这个是就用ncnn的转换工具

> 将编译出来的 onnx2ncnn 添加到系统的环境变量中

## 获取模型并进行推理

> 以下代码建议在jupyter中运行

通过pytorch hub来获取resnet18的预训练模型，这里并不细说训练的过程和模型定义

label[下载](https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt)
使用以下代码进行模型的下载和推理
```python
import os
import torch
from torchsummary import summary
torch.hub._validate_not_a_forked_repo=lambda a,b,c: True
## model
model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True)
model.eval()
input_shape = (3, 224, 224)
summary(model, input_shape, device="cpu")
## test image
filename = "out/dog.jpg"
if not os.path.exists(filename):
    if not os.path.exists("out"):
        os.makedirs("out")
    import urllib
    url, filename = ("https://github.com/pytorch/hub/raw/master/images/dog.jpg", filename)
    try: urllib.URLopener().retrieve(url, filename)
    except: urllib.request.urlretrieve(url, filename)
print("test image:", filename)
## preparing input data
from PIL import Image
import numpy as np
from torchvision import transforms
input_image = Image.open(filename)
# input_image.show()
preprocess = transforms.Compose([
    transforms.Resize(max(input_shape[1:3])),
    transforms.CenterCrop(input_shape[1:3]),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
input_tensor = preprocess(input_image)
print("input data max value: {}, min value: {}".format(torch.max(input_tensor), torch.min(input_tensor)))
input_batch = input_tensor.unsqueeze(0) # create a mini-batch as expected by the model
## forward model
# move the input and model to GPU for speed if available
if torch.cuda.is_available():
    input_batch = input_batch.to('cuda')
    model.to('cuda')
with torch.no_grad():
    output = model(input_batch)
## result    
# Tensor of shape 1000, with confidence scores over Imagenet's 1000 classes
# print(output[0])
# The output has unnormalized scores. To get probabilities, you can run a softmax on it.
max_1000 = torch.nn.functional.softmax(output[0], dim=0)
max_idx = int(torch.argmax(max_1000))
with open("imagenet_classes.txt") as f:
    labels = f.read().split("\n")
print("result: idx:{}, name:{}".format(max_idx, labels[max_idx]))
```

运行后得到结果:
```python
Using cache found in /home/neucrack/.cache/torch/hub/pytorch_vision_v0.6.0
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1         [-1, 64, 112, 112]           9,408
       BatchNorm2d-2         [-1, 64, 112, 112]             128
              ReLU-3         [-1, 64, 112, 112]               0
         MaxPool2d-4           [-1, 64, 56, 56]               0
            Conv2d-5           [-1, 64, 56, 56]          36,864
       BatchNorm2d-6           [-1, 64, 56, 56]             128
              ReLU-7           [-1, 64, 56, 56]               0
            Conv2d-8           [-1, 64, 56, 56]          36,864
       BatchNorm2d-9           [-1, 64, 56, 56]             128
             ReLU-10           [-1, 64, 56, 56]               0
       BasicBlock-11           [-1, 64, 56, 56]               0
           Conv2d-12           [-1, 64, 56, 56]          36,864
      BatchNorm2d-13           [-1, 64, 56, 56]             128
             ReLU-14           [-1, 64, 56, 56]               0
           Conv2d-15           [-1, 64, 56, 56]          36,864
      BatchNorm2d-16           [-1, 64, 56, 56]             128
             ReLU-17           [-1, 64, 56, 56]               0
       BasicBlock-18           [-1, 64, 56, 56]               0
           Conv2d-19          [-1, 128, 28, 28]          73,728
      BatchNorm2d-20          [-1, 128, 28, 28]             256
             ReLU-21          [-1, 128, 28, 28]               0
           Conv2d-22          [-1, 128, 28, 28]         147,456
      BatchNorm2d-23          [-1, 128, 28, 28]             256
           Conv2d-24          [-1, 128, 28, 28]           8,192
      BatchNorm2d-25          [-1, 128, 28, 28]             256
             ReLU-26          [-1, 128, 28, 28]               0
       BasicBlock-27          [-1, 128, 28, 28]               0
           Conv2d-28          [-1, 128, 28, 28]         147,456
      BatchNorm2d-29          [-1, 128, 28, 28]             256
             ReLU-30          [-1, 128, 28, 28]               0
           Conv2d-31          [-1, 128, 28, 28]         147,456
      BatchNorm2d-32          [-1, 128, 28, 28]             256
             ReLU-33          [-1, 128, 28, 28]               0
       BasicBlock-34          [-1, 128, 28, 28]               0
           Conv2d-35          [-1, 256, 14, 14]         294,912
      BatchNorm2d-36          [-1, 256, 14, 14]             512
             ReLU-37          [-1, 256, 14, 14]               0
           Conv2d-38          [-1, 256, 14, 14]         589,824
      BatchNorm2d-39          [-1, 256, 14, 14]             512
           Conv2d-40          [-1, 256, 14, 14]          32,768
      BatchNorm2d-41          [-1, 256, 14, 14]             512
             ReLU-42          [-1, 256, 14, 14]               0
       BasicBlock-43          [-1, 256, 14, 14]               0
           Conv2d-44          [-1, 256, 14, 14]         589,824
      BatchNorm2d-45          [-1, 256, 14, 14]             512
             ReLU-46          [-1, 256, 14, 14]               0
           Conv2d-47          [-1, 256, 14, 14]         589,824
      BatchNorm2d-48          [-1, 256, 14, 14]             512
             ReLU-49          [-1, 256, 14, 14]               0
       BasicBlock-50          [-1, 256, 14, 14]               0
           Conv2d-51            [-1, 512, 7, 7]       1,179,648
      BatchNorm2d-52            [-1, 512, 7, 7]           1,024
             ReLU-53            [-1, 512, 7, 7]               0
           Conv2d-54            [-1, 512, 7, 7]       2,359,296
      BatchNorm2d-55            [-1, 512, 7, 7]           1,024
           Conv2d-56            [-1, 512, 7, 7]         131,072
      BatchNorm2d-57            [-1, 512, 7, 7]           1,024
             ReLU-58            [-1, 512, 7, 7]               0
       BasicBlock-59            [-1, 512, 7, 7]               0
           Conv2d-60            [-1, 512, 7, 7]       2,359,296
      BatchNorm2d-61            [-1, 512, 7, 7]           1,024
             ReLU-62            [-1, 512, 7, 7]               0
           Conv2d-63            [-1, 512, 7, 7]       2,359,296
      BatchNorm2d-64            [-1, 512, 7, 7]           1,024
             ReLU-65            [-1, 512, 7, 7]               0
       BasicBlock-66            [-1, 512, 7, 7]               0
AdaptiveAvgPool2d-67            [-1, 512, 1, 1]               0
           Linear-68                 [-1, 1000]         513,000
================================================================
Total params: 11,689,512
Trainable params: 11,689,512
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.57
Forward/backward pass size (MB): 62.79
Params size (MB): 44.59
Estimated Total Size (MB): 107.96
----------------------------------------------------------------
out/dog.jpg
tensor(2.6400) tensor(-2.1008)
idx:258, name:Samoyed, Samoyede

```
可以看到模型有 11,689,512的参数， 即 11MiB左右， 这个大小也就几乎是实际在 831 上运行的模型的大小了

## 模型转换

### pth转onnx
通过pytorch hub获取到的resnet18 模型是pth格式的，需要转换成onnx格式的模型

转换代码
```python
def torch_to_onnx(net, input_shape, out_name="out/model.onnx", input_names=["input0"], output_names=["output0"], device="cpu"):
    batch_size = 1
    if len(input_shape) == 3:
        x = torch.randn(batch_size, input_shape[0], input_shape[1], input_shape[2], dtype=torch.float32, requires_grad=True).to(device)
    elif len(input_shape) == 1:
        x = torch.randn(batch_size, input_shape[0], dtype=torch.float32, requires_grad=False).to(device)
    else:
        raise Exception("not support input shape")
    print("input shape:", x.shape)
    # torch.onnx._export(net, x, "out/conv0.onnx", export_params=True)
    torch.onnx.export(net, x, out_name, export_params=True, input_names = input_names, output_names=output_names)
onnx_out="out/resnet_1000.onnx"
ncnn_out_param = "out/resnet_1000.param"
ncnn_out_bin = "out/resnet_1000.bin"
input_img = filename
torch_to_onnx(model, input_shape, onnx_out, device="cuda:0")

```
在out文件夹中得到onnx格式模型文件

### onnx转ncnn

然后再利用前面编译出来的onnx2ncnn转换工具进行ncnn格式的转换

```python
def onnx_to_ncnn(input_shape, onnx="out/model.onnx", ncnn_param="out/conv0.param", ncnn_bin = "out/conv0.bin"):
    import os
    # onnx2ncnn tool compiled from ncnn/tools/onnx, and in the buld dir
    cmd = f"onnx2ncnn {onnx} {ncnn_param} {ncnn_bin}"
    os.system(cmd)
    with open(ncnn_param) as f:
        content = f.read().split("\n")
        if len(input_shape) == 1:
            content[2] += " 0={}".format(input_shape[0])
        else:
            content[2] += " 0={} 1={} 2={}".format(input_shape[2], input_shape[1], input_shape[0])
        content = "\n".join(content)
    with open(ncnn_param, "w") as f:
        f.write(content)
onnx_to_ncnn(input_shape, onnx=onnx_out, ncnn_param=ncnn_out_param, ncnn_bin=ncnn_out_bin)
```

> 这里需要确定 onnx2ncnn 是可以使用的命令，否则会无法使用这个函数进行模型转换



### ncnn量化到int8模型

通过maixhub将ncnn模型进行量化到int8模型

在 maixhub 模型转换 将 ncnn 模型转换为 awnn 支持的 int8 模型 （网页在线转换很方便人为操作，另一个方面因为全志要求不开放 awnn 所以暂时只能这样做）

阅读转换说明，可以获得更多详细的转换说明
![](./../asserts/maixhub.jpg)

这里有几组参数：

- 均值 和 归一化因子： 在 pytorch 中一般是 (输入值 - mean ) / std, awnn对输入的处理是 (输入值 - mean ) \* norm, 总之，让你训练的时候的输入到第一层网络的值范围和给awnn量化工具经过(输入值 - mean ) \* norm 计算后的值范围一致既可。 比如 这里打印了实际数据的输入范围是[-2.1008, 2.6400]， 是代码中preprocess 对象处理后得到的，即x = (x - mean) / std ==> (0-0.485)/0.229 = -2.1179, 到awnn就是x = (x - mean_2\*255) \* (1 / std \* 255) 即 mean2 = mean \* 255, norm = 1/(std \* 255), 更多可以看这里。

- 所以我们这里可以设置 均值为 0.485 \* 255 = 123.675， 设置 归一化因子为1/ (0.229 \* 255) = 0.017125， 另外两个通道同理，但是目前 awnn 只能支持三个通道值一样。。。所以填123.675, 123.675, 123.675，0.017125, 0.017125, 0.017125 即可，因为这里用了pytorch hub的预训练的参数，就这样吧， 如果自己训练，可以好好设置一下图片输入层尺寸（问不是图片怎么办？貌似 awnn 暂时之考虑到了图片。。）

- RGB 格式： 如果训练输入的图片是 RGB 就选 
- RGB量化图片， 选择一些和输入尺寸相同的图片，可以从测试集中拿一些，不一定要图片非常多，但尽量覆盖全场景（摊手

> 自己写的其它模型转换如果失败，多半是啥算子不支持，需要在 使用说明里面看支持的 算子，比如现在的版本view、 flatten、reshape 都不支持所以写模型要相当小心， 后面的版本会支持 flatten reshape 等 CPU 算子

如果不出意外， 终于得到了量化好的 awnn 能使用的模型， \*.param 和 \*.bin

## 使用模型，在v831上推理
可以使用 python 或者 C 写代码，以下两种方式

python的是需要在终端下运行的，不要使用jupyter，建议使用ssh，这样放文件什么都比较方便

### MaixPy3
python 请看MaixPy3

不想看文档的话，就是在系统开机使用的基础上， 更新 MaixPy3 就可以了：

    export TMPDIR=/root && pip install --upgrade maixpy3

然后在终端使用 python 运行脚本（可能需要根据你的文件名参数什么的改一下代码）：

https://github.com/sipeed/MaixPy3_scripts/blob/main/basic/v1.0/resnet.py

label 在这里： https://github.com/sipeed/MaixPy3/blob/main/ext_modules/_maix_nn/example/classes_label.py

baars.ttf 在这里：https://github.com/sipeed/MaixPy3_scripts/blob/main/application/base/res/baars.ttf
```python
from maix import camera, nn, display
from home.res.classes_label import labels
class Resnset:
    m = {
        "param": "/home/model/resnet18_1000_awnn.param",
        "bin": "/home/model/resnet18_1000_awnn.bin"
    }
    options = {
        "model_type":  "awnn",
        "inputs": {
            "input0": (224, 224, 3)
        },
        "outputs": {
            "output0": (1, 1, 1000)
        },
        "first_layer_conv_no_pad": False,
        "mean": [127.5, 127.5, 127.5],
        "norm": [0.00784313725490196, 0.00784313725490196, 0.00784313725490196],
    }
    def __init__(self):
        from maix import nn
        self.model = nn.load(self.m, opt=self.options)
       
    def __del__(self):
        del self.model




while True:
    img = camera.capture().resize(224, 224)
    tmp = img.tobytes()
    out = resnset.model.forward(tmp, quantize=True)
    out2 = nn.F.softmax(out)
    msg = "{:.2f}: {}".format(out2.max(), labels[out.argmax()])
    img.draw_string(0, 0, str(msg), 0.5, (255, 0, 0), 1)
    display.show(img)
```
> 如果运行报错了，请更新maixpy3再运行



### C语言 SDK， libmaix
访问这里，按照 https://github.com/sipeed/libmaix 的说明克隆仓库，并编译 https://github.com/sipeed/libmaix/tree/master/examples/nn_resnet

上传编译成功后dist目录下的所有内容到 v831, 然后执行./start_app.sh即可

> 以上内容出至：<https://neucrack.com/p/358>