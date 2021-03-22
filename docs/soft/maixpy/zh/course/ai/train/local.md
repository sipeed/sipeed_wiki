---
title: 本地模型训练
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 本地模型训练
---



本地模型训练使用 [sipeed/maix_train](https://github.com/sipeed/maix_train) 这份代码进行， 使用了 Tensorflow 作为训练框架

主要支持：
* 物体分类模型（使用 Mobilenet V1）： 只识别图片中的物体是什么
* 物体检测模型（使用 YOLO V2）： 找到图片中认识的图体，并同时找到其坐标和大小

## 系统环境

首先，需要一台有 Linux 系统的电脑
如果你的主力系统是 Windows， 你可以用以下系统环境：
* 使用虚拟机, `virtual box` 或者 `vmware` 都可以， 系统推荐安装`Ubuntu20.04`
* 或者安装双系统，安装方法请自行搜索学习，或者看[这个双系统安装教程](https://neucrack.com/p/330)

你可能想着在 `Windows` 下面进行开发， 但是这里强烈建议使用`Linux`而不是`Windows`：
* 首先，大多数模型训练框架都是首先支持 `Linux`， 在`Linux`下面开发的难度会比`Windows`下开发更加容易
* 作为一个开发者， 学会使用`Linux`是基础技能，当然，除非你是`Windows`狂热粉， 那我相信你一定有把其它系统的软件移植到`Windows`的能力


## 软件安装

训练可以使用 CPU 进行训练，但是速度比较慢， 如果使用专用的显卡（GPU）进行加速，速度会快非常多，个人一般使用`Nvidia`的显卡， 比如`RTX 3090`， 当然，使用普通的`GTX 1060 6G内存`版本就可以愉快使用了

初次接触，建议先使用 CPU 进行训练，环境安装会简单很多很多， 以下只讲 CPU 训练的方法， GPU 请自行学习
> GPU 使用可以参考 Tensorflow 官方 [GPU 使用教程](https://tensorflow.google.cn/install/gpu)， 如果你显卡驱动遇到了问题，可以参考[这里](https://neucrack.com/p/252)， 另外如果你用 [docker 安装](https://tensorflow.google.cn/install/docker )遇到了问题， 也可以看[这里](https://neucrack.com/p/116)


接下来的使用方法摘抄于仓库的 [README](https://github.com/sipeed/maix_train/blob/master/README.md), 如果有出入， 以仓库的`README`为准，注意分辨


* 将训练代码克隆到本地

```
git clone https://github.com/sipeed/maix_train --recursive
```

* 安装依赖

```
cd maix_train
pip3 install -r requirements.txt
```
中国用户可以使用阿里云或者清华的源， 下载速度更快
```
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

* 下载 [nncase v0.1.0-rc5](https://github.com/kendryte/nncase/releases/tag/v0.1.0-rc5) 并解压到 `maix_train/tools/ncc/ncc_v0.1`, 保证可执行文件的路径是 `maix_train/tools/ncc/ncc_v0.1/ncc`

* 配置工程

先初始化工程
```
python3 train.py init
```
然后根据你的硬件情况，编辑`maix_train/instance/config.py`配置

## 准备数据集

准备数据集， 图片大小为 `224x224`， 格式可以参考`maix_train/datasets`下的数据集示例

也可以看 [Maxhub 的数据集要求](https://www.maixhub.com/index/mtrain/help.html)


##  训练分类模型

```
python3 train.py -t classifier -z datasets/test_classifier_datasets.zip train
```

或者解压数据集到文件夹，指定数据集文件夹
```
python3 train.py -t classifier -d datasets/test_classifier_datasets train
```

## 训练目标检测模型

```
python3 train.py -t detector -z datasets/test_detector_xml_format.zip train
```

## 使用模型

和使用`Maixhub`训练的模型一样， 在`out`文件夹会生成一个`zip`文件，里面包含了结果，把**所有**文件拷贝到`SD`卡根目录，然后开发板上电运行即可





