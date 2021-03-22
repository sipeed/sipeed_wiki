---
title: Local model training
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: local model training
---



Local model training is performed using [sipeed/maix_train](https://github.com/sipeed/maix_train) this code, using Tensorflow as the training framework

Main support:
* Object classification model (using Mobilenet V1): Only identify what is the object in the picture
* Object detection model (using YOLO V2): Find the figure body recognized in the picture, and find its coordinates and size at the same time

## System environment

First, a computer with Linux system is required
If your main system is Windows, you can use the following system environment:
* You can use a virtual machine, `virtual box` or `vmware`, the system recommends installing `Ubuntu20.04`
* Or install dual systems, please search and learn the installation method yourself, or see [this dual system installation tutorial](https://neucrack.com/p/330)

You may want to develop under `Windows`, but it is strongly recommended to use `Linux` instead of `Windows`:
* First of all, most model training frameworks support `Linux` first, and the difficulty of developing under `Linux` will be easier than developing under `Windows`
* As a developer, learning to use `Linux` is a basic skill. Of course, unless you are a fan of `Windows`, then I believe you must have the ability to port software from other systems to `Windows`


## Software Installation

Training can use CPU for training, but the speed is relatively slow. If you use a dedicated graphics card (GPU) for acceleration, the speed will be much faster. Individuals generally use `Nvidia` graphics cards, such as `RTX 3090`, of course, use ordinary` GTX 1060 6G memory `version can be used happily

For the first contact, it is recommended to use the CPU for training first, the environment installation will be much easier, the following only talks about the method of CPU training, GPU please learn by yourself
> For GPU usage, please refer to the official Tensorflow [GPU Usage Tutorial](https://tensorflow.google.cn/install/gpu). If you encounter problems with the graphics card driver, please refer to [here](https://neucrack.com/ p/252), if you encounter problems with [docker installation](https://tensorflow.google.cn/install/docker ), you can also see [here](https://neucrack.com/p/116 )


The following method of use is excerpted from the warehouse’s [README](https://github.com/sipeed/maix_train/blob/master/README.md), if there are discrepancies, please refer to the warehouse’s `README`, pay attention to distinguish


* Clone the training code to local

```
git clone https://github.com/sipeed/maix_train --recursive
```

* Installation dependencies

```
cd maix_train
pip3 install -r requirements.txt
```
Chinese users can use Alibaba Cloud or Tsinghua's source, the download speed is faster
```
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

* Download [nncase v0.1.0-rc5](https://github.com/kendryte/nncase/releases/tag/v0.1.0-rc5) and unzip it to `maix_train/tools/ncc/ncc_v0.1`, guaranteed The path of the execution file is `maix_train/tools/ncc/ncc_v0.1/ncc`

* Configuration project

Initialize the project first
```
python3 train.py init
```
Then edit the `maix_train/instance/config.py` configuration according to your hardware situation

## Prepare the data set

Prepare the data set, the image size is `224x224`, the format can refer to the data set example under `maix_train/datasets`

See also [Maxhub's data set requirements](https://www.maixhub.com/index/mtrain/help.html)


## Train classification model

```
python3 train.py -t classifier -z datasets/test_classifier_datasets.zip train
```

Or unzip the data set to a folder, specify the data set folder
```
python3 train.py -t classifier -d datasets/test_classifier_datasets train
```

## Train the target detection model

```
python3 train.py -t detector -z datasets/test_detector_xml_format.zip train
```

## Use model

Like the model trained with `Maixhub`, a `zip` file will be generated in the `out` folder, which contains the results, copy **all** files to the root directory of the `SD` card, and then power on the development board Just run
