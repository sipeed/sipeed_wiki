---
title: 部署模型到 Maix-III(M3) 系列 AX-Pi 开发板
date: 2022-09-21
---

<div id="title_card">
    <div class="card" style="background-color: #fafbfe">
        <img src="../../assets/maix-iii-small.png" alt="AX-Pi 模型转换和部署">
        <div class="card_info card_purple">
            <div class="title">Maix-III 系列之 AX-Pi（爱芯派）</div>
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
}
</style>

> 有任何想法或者修改建议，欢迎留言或者直接点击右上角`编辑本页`进行修改后提交 PR

> [MaixHub](https://maixhub.com/model/zoo) 模型库有 AX-Pi 能直接运行的模型，可以直接下载使用，也欢迎上传分享你的模型~

要部署模型到 [Maix-III(M3) 系列 AX-Pi 开发板](/hardware/zh/maixIII/index.html)，需要将模型量化到 INT8，减小模型大小的同时提高运行速度，一般采用 `PTQ`(训练后量化)的方式量化模型，步骤：
* 准备好浮点模型。
* 用模型量化和格式转换工具转换成 AX-Pi 支持的格式，这里工具使用爱芯官方提供的 [superpulsar](https://superpulsar-docs.readthedocs.io) 。
* 在 AX-Pi 上运行模型。

## 准备浮点模型

使用 `Pytorch` 或者 `Tensorflow` 训练好模型， 将模型保存为 `onnx` 格式备用。

需要注意只能使用 `AX-Pi` 所支持的算子，见[算子支持列表](https://superpulsar-docs.readthedocs.io/zh_CN/latest/appendix/op_support_list.html)。

对于某些网络，可能需要将后处理剥离出来，使用`CPU`处理。

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
直接使用 `docker`命令下载镜像或者先下载镜像文件解压成 `tar` 文件，再加载镜像:

| 下载站点 | 简介 | 使用方法 |
| :--- | :--- | :--- |
| [dockerhub](https://hub.docker.com/r/sipeed/superpulsar/tags) | 执行命令即可在线下载 | `docker pull sipeed/superpulsar` |
| dockerhub 国内镜像 | 中国国内下载加速 | 1. 编辑`/etc/docker/daemon.json`添加`"registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"],`(也可以用其它镜像比如[阿里云](https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors))<br>2. `docker pull daocloud.io/sipeed/superpulsar:latest` |

> 注意这里镜像名叫 `sipeed/superpulsar`， 在文档里面有些地方可能是 `axera/neuwizard`，是等效的，只是名字不同

然后创建容器：
```shell
docker run -it --net host --rm --shm-size 32g -v $PWD:/data sipeed/superpulsar
```
> * 这里`--shm-size`共享内run大小根据你的电脑内存大小设置。
> * 不用`--rm`会保留容器，建议加个`-name xxx`来命名容器，下次通过`docker start xxx && docker attach xxx`进入容器
> * `-v 宿主机路径:/data`是把宿主机的目录挂载到容器的`/data`目录，这样就可以在容器里面直接操作宿主机的文件了。

创建容器后会自动进入容器，使用`pulsar -h`命令可以看到相关命令。

### 进行模型量化和转换

然后看 [superpulsar](https://superpulsar-docs.readthedocs.io) 文档中的转换命令以及配置文件方法进行模型量化和格式转换。
> 注意 `AX-Pi` 使用了虚拟 NPU 的概念来划分算力，以将实现全部算力给 NPU 或者 NPU 和 AI-ISP 各分一半。

## 在 AX-Pi 上运行模型

按照文档转换模型后，将模型通过 `scp` 或者 `adb` 传到 `AX-Pi` 上，使用文档中的模型测试运行命令运行模型即可。

要正式地将模型跑起来，你可能需要需要修改代码，更改输入预处理或者增加后处理，目前提供 `C/C++` SDK，代码参考 [ax-samples](https://github.com/AXERA-TECH/ax-samples)，可以交叉编译，也可以直接在 `AX-Pi` 上编译。


## QAT 量化

`QAT`(Quantization aware training)即量化感知训练，和`PTQ`在对训练好的模型进行浏览量化的做法不同，`QAT`是在训练时就模拟量化推理，以减少量化误差， 和训练后量化`PTQ`相比，有更高的精度，但是过程会更复杂，不建议一开始就使用。

[superpulsar](https://superpulsar-docs.readthedocs.io) 文档未来会更新，如果你擅长这方面，也欢迎点击右上角`编辑本页`在这里添加说明。


