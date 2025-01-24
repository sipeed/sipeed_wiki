---
title: 部署模型到 Maix-III(M3) 系列 AXera-Pi 开发板
date: 2022-09-21
#update:
#  - date: 2022-09-30
#    author: neucrack
#    content: 初版文档
---

<div id="title_card">
    <div class="card" style="background-color: #fafbfe">
        <img src="../../assets/maix-iii-small.png" alt="AXera-Pi 模型转换和部署">
        <div class="card_info card_purple">
            <div class="title">Maix-III 系列之 AXera-Pi（爱芯派）</div>
            <div class="brief">
                <div>高算力、独特 AI-ISP 影像系统</div>
                <div>最高 3.6Tops@INT8，丰富算子支持</div>
            </div>
        </div>
    </div>
</div>
<style>
#title_card {
    width:100%;
    text-align:center;
    background-color: #fafbfe;
    margin-bottom: 1em;
}
#title_card img {
  max-height: 20em;
}
.card_purple {
    background-color: #d1c4e9;
    color: #673ab7;
}
.dark .card_purple {
    background-color: #370040;
    color: #ffffffba;
}
.title {
    font-size: 1.5em;
    font-weight: 800;
    padding: 0.8em;
}
</style>

> 有任何想法或者修改建议，欢迎留言或者直接点击右上角`编辑本页`进行修改后提交 PR

> [MaixHub](https://maixhub.com/model/zoo) 模型库有 AXera-Pi 能直接运行的模型，可以直接下载使用，也欢迎上传分享你的模型~

[点击可以查看 Maix-III(M3) 系列 AXera-Pi 开发板详情和基础使用文档](/hardware/zh/maixIII/index.html)

要部署模型到`AXera-Pi`，需要将模型量化到 INT8，减小模型大小的同时提高运行速度，一般采用 `PTQ`(训练后量化)的方式量化模型，步骤：
**1.** 准备好浮点模型。
**2.** 用模型量化和格式转换工具转换成 AXera-Pi 支持的格式，这里工具使用爱芯官方提供的 [pulsar](https://pulsar-docs.readthedocs.io) 。
> 本文提供了快速入门和流程向导，强烈建议先通看一遍，再查看 pulsar 文档获得更多具体内容。
**3.** 在 AXera-Pi 上运行模型。

## 准备浮点模型

使用 `Pytorch` 或者 `TensorFlow` 训练好模型， 将模型保存为 `onnx` 格式备用。

需要注意只能使用 `AXera-Pi` 所支持的算子，见[算子支持列表](https://pulsar-docs.readthedocs.io/zh_CN/latest/appendix/op_support_list.html)。

对于某些网络，可能需要将后处理剥离出来，使用`CPU`处理。

### 举例

比如我们用一个 PyTorch Hub 上面的 [mobilenetv2](https://pytorch.org/hub/pytorch_vision_mobilenet_v2/):
```python
import torch
model = torch.hub.load('pytorch/vision:v0.10.0', 'mobilenet_v2', pretrained=True)
model.eval()
```

导出为 `onnx` 格式:
```python
x = torch.randn(1, 3, 224, 224)
torch.onnx.export(model, x, "mobilenetv2.onnx", export_params = True, verbose=True, opset_version=11)
```
有些模型可以使用 `onnxsim` 精简下网络结构（这个模型实际上不需要）：
```
pip install onnx-simplifier
python -m onnxsim mobilenetv2.onnx mobilenetv2-sim.onnx
```


## 模型量化和格式转换

### 安装`docker`

[安装教程](https://docs.docker.com/engine/install/)

安装好后查看
```
docker --version
```

`Linux`下添加当前用户到 `docker`组，这样就不需要使用 `sudo` 运行`docker`命令了。可以用以下命令来添加：
```shell
sudo gpasswd -a $USER docker
newgrp docker
```

### 下载转换工具

转换工具是以 docker 镜像的方式提供的，下载后用 docker 加载镜像即可。

| 下载站点 | 简介 | 使用方法 |
| :--- | :--- | :--- |
| [dockerhub](https://hub.docker.com/r/sipeed/pulsar/tags) | 执行命令即可在线下载 | `docker pull sipeed/pulsar` |
| dockerhub 国内镜像 | 中国国内下载加速 | 1. 编辑`/etc/docker/daemon.json`添加`"registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"],`(也可以用其它镜像比如[阿里云](https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors))<br>2. 然后 `docker pull sipeed/pulsar` 拉取镜像 |

拉取完成后使用`docker images`命令可以看到`sipeed/pulsar:latest`镜像
> 注意这里镜像名叫 `sipeed/pulsar`， 在文档里面有些地方可能是 `axera/neuwizard`，是等效的，只是名字不同

然后创建容器：
```shell
docker run -it --net host --rm --shm-size 32g -v $PWD:/data sipeed/pulsar
```
> * 这里`--shm-size`共享内run大小根据你的电脑内存大小设置。
> * 不用`--rm`会保留容器，建议加个`-name xxx`来命名容器，下次通过`docker start xxx && docker attach xxx`进入容器
> * `-v 宿主机路径:/data`是把宿主机的目录挂载到容器的`/data`目录，这样就可以在容器里面直接操作宿主机的文件了。

创建容器后会自动进入容器，使用 `pulsar -h` 命令可以看到相关命令。

### 进行模型量化和转换

然后看 [pulsar](https://pulsar-docs.readthedocs.io) 文档中的转换命令以及配置文件方法进行模型量化和格式转换。
> 注意 `AXera-Pi` 使用了虚拟 NPU 的概念来划分算力，以将实现全部算力给 NPU 或者 NPU 和 AI-ISP 各分一半。

#### 举例

仍然以 `mobilenetv2` 为例：
* 根据`pulsar`文档，准备好配置文件`config_mobilenetv2.prototxt`, (具体格式说明见[配置文件详细说明](https://pulsar-docs.readthedocs.io/zh_CN/latest/test_configs/config.html)),内容如下：
.. details:: config_mobilenetv2.prototxt
    ```protobuf
    # 基本配置参数：输入输出
    input_type: INPUT_TYPE_ONNX
    output_type: OUTPUT_TYPE_JOINT

    # 硬件平台选择
    target_hardware: TARGET_HARDWARE_AX620

    # CPU 后端选择，默认采用 AXE
    cpu_backend_settings {
        onnx_setting {
            mode: DISABLED
        }
        axe_setting {
            mode: ENABLED
            axe_param {
                optimize_slim_model: true
            }
        }
    }

    # onnx 模型输入数据类型描述
    src_input_tensors {
        color_space: TENSOR_COLOR_SPACE_RGB
    }

    # joint 模型输入数据类型设置
    dst_input_tensors {
        color_space: TENSOR_COLOR_SPACE_RGB
    }

    # neuwizard 工具的配置参数
    neuwizard_conf {
        operator_conf {
            input_conf_items {
                attributes {
                    input_modifications {
                        # y = x * (slope / slope_divisor) + (bias / bias_divisor)
                        # 这里就是先把数据归一到[0, 1]
                        affine_preprocess {
                            slope: 1
                            slope_divisor: 255
                            bias: 0
                        }
                    }
                    input_modifications {
                        # y = (x - mean) / std
                        # 按照训练的时候的参数标准化
                        input_normalization {
                            mean: [0.485,0.456,0.406]  ## 均值， 注意这里的顺序根据 src_input_tensors.color_space 而定， 比如这里是 [R G B]
                            std: [0.229,0.224,0.255]   ## 方差
                        }
                    }
                }
            }
        }
        dataset_conf_calibration {
            path: "imagenet-1k-images-rgb.tar" # 设置 PTQ 校准数据集路径
            type: DATASET_TYPE_TAR         # 数据集类型：tar 包
            size: 256                      # 量化校准过程中实际使用的图片张数
            batch_size: 1
    }
    }

    # pulsar compiler 的 batch size 配置参数
    pulsar_conf {
        ax620_virtual_npu: AX620_VIRTUAL_NPU_MODE_111 # 使用虚拟 NPU， NPU 和 AI-ISP 各分一半， 111 代表 NPU
                        #  AX620_VIRTUAL_NPU_MODE_0   # 不使用虚拟 NPU， 全部算力给 NPU
                        #  AX620_VIRTUAL_NPU_MODE_112 # 使用虚拟 NPU， NPU 和 AI-ISP 各分一半， 112 代表 AI-ISP 特用，千万别乱设置
        batch_size: 1
    }
    ```
    > 注意这里的预处理要和训练模型时相同，即 [mobilenetV2](https://pytorch.org/hub/pytorch_vision_mobilenet_v2/) 的预处理说明，这里是先归一再减`mean`除以`std`。
    > 以及`imagenet-1k-images-rgb.tar`是从训练集中抠出来的一部分图片，用于量化校准，在这里训练集是`imagenet`，测试用可以在[百度云](https://pan.baidu.com/s/1TiZSIm0fpqbLn-2qLBX58g?pwd=1rpb)或者[github](https://github.com/sipeed/sipeed_wiki/releases/download/v0.0.0/imagenet-1k-images-rgb.tar)下载，也可以你自己从[imagenet](https://www.image-net.org/)里面抠图出来。TODO: 需不需要手动先缩放到输入尺寸？
    > 这里 `ax620_virtual_npu` 设置为了 `AX620_VIRTUAL_NPU_MODE_111`，这很重要，如果要用摄像头的话，必须要设置为这个， 否则可能会初始化失败，因为默认使用摄像头开启了 `AI-ISP` 会启用虚拟 NPU 并使用另一半算力，为保证我们第一次能使用，先这样设置，后面会详细介绍。

然后在 `docker`容器里面执行（注意文件通过前面`docker run`的`-v`参数指定了挂载宿主机的目录到`docker`容器里面，直接拷贝到宿主机的目录就好了）：
```
pulsar build --input mobilenetv2.onnx --output mobilenetv2.joint --config config_mobilenetv2.prototxt --output_config out_config_mobilenet_v2.prototxt
```
耐心等待，可能需要一小会儿时间，就会得到转换的模型结果`mobilenetv2.joint`了

### 在 docker 中使用 GPU 进行模型量化和格式转换

默认 docker 不能使用显卡驱动，但是有要用的话方法也不难：
* 宿主机正常安装显卡驱动，比如 `ubuntu` 直接可以在包管理器中安装
* 按照 [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) 的说明安装， 然后测试是否可用：
```
docker run --rm --gpus all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi
```
这会执行 `nvidia-smi` 命令，就可以看到映射到 docker 里面的显卡信息了。
* 在需要使用显卡的容器创建时加上 `--gpus all` 参数来将所有显卡驱动映射到容器内，也可以指定特定显卡编号 `--gpus '"device=2,3"'`, 比如：
```
docker run -it --net host --rm --gpus all --shm-size 32g -v $PWD:/data sipeed/pulsar
```
注意当前版本（0.6.1.20）的 `pulsar build` 仅支持 sm_37 sm_50 sm_60 sm_70 sm_75 架构 GPU，30/40 系列 GPU 暂不支持。


## 在 AXera-Pi 上测试运行模型

按照文档转换模型后，将模型通过 `scp` 或者 `adb` 传到 `AXera-Pi` 上，使用文档中的模型测试运行命令运行模型即可。

### 举例

仍然以`mobilenetv2`为例：
测试图片保存到`cat.jpg`：
<img src="../../assets/cat.jpg" style="max-height: 20em;">

* 先在电脑上跑一下和`onnx`的结果对比:
```
pulsar run mobilenetv2.onnx mobilenetv2.joint --input cat.jpg --config out_config_mobilenet_v2.prototxt --output_gt gt
```
得到余弦距离，这里为 `0.9862` ，说明 `joint` 模型和 `onnx` 模型的输出结果相似度 `98.62%`，在可以接受的范围内，如果值太小，则表示量化过程中出现了误差，需要考虑是不是设置有误或者量化输入数据有误或者模型设计有问题。
```log
Layer: 536  2-norm RE: 17.03%  cosine-sim: 0.9862
```

* 拷贝模型到 `AXera-Pi` 上直接跑一下(通过 `scp` 命令拷贝 `joint` 格式模型文件到开发板）：
在板子上运行模型：
```
time run_joint mobilenetv2.joint --repeat 100 --warmup 10
```
可以看到模型运行时间 `2.1ms`，这里我们没有启用虚拟 NPU，如果启用了虚拟 NPU，则时间加倍为 `4ms`。以及 `overhead 250.42 ms` 即其它耗时（比如 模型加载 内存分配 等）。
```
Run task took 2143 us (99 rounds for average)
        Run NEU took an average of 2108 us (overhead 9 us)

```
如果要测试输入，需要先将图片转换为二进制内容，`HWC + RGB` 排列，用 `--data` 指定二进制文件。

.. details::转换为二进制文件脚本
    ```python
    from PIL import Image
    import sys
    out_path = sys.argv[2]
    img = Image.open(sys.argv[1])
    img = img.convert('RGB')
    img = img.resize((224, 224))
    rgb888 = img.tobytes()
    with open(out_path, "wb") as f:
        f.write(rgb888)
    ```
    执行`python convert.py cat.jpg cat.bin`，得到`cat.bin`文件。
```
run_joint mobilenetv2.joint --data cat.bin --bin-out-dir ./
```
然后目录下会生成一个`bin`文件，大小是`4000`个字节，即`1000`个`float32`，可以用`python`加载找出最大值
```python
out = np.fromfile("536.bin", dtype=np.float32)
print(out.argmax(), out.max())
```
得到结果`282 8.638927`，在[labels](https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt)中找到下标第`282`即`283`行，是`tiger cat`，结果和直接电脑运行浮点模型结果`282 9.110947`也一致，虽然值有略微差异，但是在可以接受的范围内。
> 注意这里没有进行`softmax`计算，`out.max()`值不是概率值。

## 编写代码运行模型

要正式地将模型跑起来，你可能需要需要修改代码，更改输入预处理或者增加后处理，目前提供 `C/C++` SDK，代码参考 [ax-samples](https://github.com/AXERA-TECH/ax-samples)，可以交叉编译，也可以直接在 `AXera-Pi` 上编译。

运行分类模型的代码在[ax_classification_steps.cc](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax_classification_steps.cc)，按照仓库的编译说明编译后得到`build/bin/install/ax_classification`可执行文件，拷贝到开发板执行
```
./ax_classification -m mobilenetv2.joint -i cat.jpg
```
> 在代码中使用了 `opencv` 读取了图片，格式为 `BGR`，在运行模型时会根据转换模型时的配置自动判断是否转成 `RGB`，所以直接用了 `mw::prepare_io` 拷贝 `BGR` 的图到输入缓冲区了，后面就交给底层库处理了。

如果你的模型不是简单的分类模型，那你可能需要在模型推理结束后添加后处理的代码以达到解析结果的目的。

## 使用摄像头和屏幕

到此，模型单独运行已经走通了，如果要基于此做应用，因为是 `Linux`，有很多通用的开发方法和库，如果你希望将摄像头和屏幕联合起来使用，可以使用[libmaix](https://github.com/sipeed/libmaix)，或者你也可以直接使用[axpi_bsp_sdk](https://github.com/sipeed/axpi_bsp_sdk)进行开发（难度会比较大一点）。
* 看[SDK 开发说明](/hardware/zh/maixIII/ax-pi/sdk.html) 编译并执行[摄像头屏幕显示例程](https://github.com/sipeed/libmaix/tree/release/examples/axpi)，因为仓库都在`github`，所以最好是有个好的代理服务器。
* 将模型运行代码合并到例程中，有个问题要十分注意，如果要使用摄像头，默认`AI-ISP`会打开（暂未提供关闭的方式，后面更新TODO:），**所以模型转换的时候要指定模型为虚拟NPU运行，即配置文件中设置`ax620_virtual_npu: AX620_VIRTUAL_NPU_MODE_111`，否则初始化会失败**。
> 可以直接使用[1000分类例程](https://github.com/sipeed/libmaix/tree/release/examples/axpi_classification_cam).
> 在板子编译通过后执行`./dist/axpi_classification_cam -m mobilenetv2.joint` 即可开始识别。模型也可以到[MaixHub 模型库下载](https://maixhub.com/model/zoo/89)


## QAT 量化 和其它优化方法

`QAT`(Quantization aware training)即量化感知训练，和 `PTQ` 在对训练好的模型进行浏览量化的做法不同，`QAT` 是在训练时就模拟量化推理，以减少量化误差， 和训练后量化 `PTQ` 相比，有更高的精度，但是过程会更复杂，不建议一开始就使用。

更多详情看[superpulsar](https://pulsar-docs.readthedocs.io)， 文档会持续更新，如果你擅长这方面，也欢迎点击右上角`编辑本页`在这里添加说明。


## 其它参考和分享汇总

> 欢迎贴上你的分享，点击右上角`编辑本页`添加。

* [爱芯元智AX620A部署yolov5 6.0模型实录](https://zhuanlan.zhihu.com/p/569083585)
* [AX620A运行yolov5s自训练模型全过程记录（windows）](http://t.csdn.cn/oNeYG)
* [MOT：如何在爱芯派上实现多目标跟踪的神奇效果！](https://www.yuque.com/prophetmu/chenmumu/ax_tracker)
* [MMPose：在爱芯派上玩转你的关键点检测！](https://www.yuque.com/prophetmu/chenmumu/m3axpi_keypoint)
* [2023年最新 使用 YOLOv8 训练自己的数据集，并在 爱芯派硬件 上实现 目标检测 和 钢筋检测 ！！](https://www.yuque.com/prophetmu/chenmumu/m3axpi)
