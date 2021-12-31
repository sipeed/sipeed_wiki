# 本地训练使用教程

> 没有任何的开发基础请慎重使用，出现问题请自行解决！

配置好本地训练的环境之后，就可以开始进行本地训练了，如果没有配置好的，请看上一篇[教程](https://bbs.sipeed.com/thread/932)

## 安装依赖

打开解压后得到的文件夹，打开里面的 requirements.txt 文件，将里面的 tensorflow>=2.3.1 删除，保存关闭。

![4.png](https://bbs.sipeed.com/storage/attachments/2021/07/21/2AZNFAWTnje3DQSuBplNRmJv3FXJO8rkAATuJdjf_thumb.png "1460")

在文件夹的这里输入cmd, 回车，进入命令行界面

![5.png](https://bbs.sipeed.com/storage/attachments/2021/07/21/hkzdghzlqlnZBTbcES61V7p15EnCKnYJNpPZ8tgJ_thumb.png "1463")

输入 

    pip install -r requirements.txt

如果下载速度很慢的话，可以使用中科大源来进行下载

    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

等待全部包的安装结束就可以了

## 数据集的制作

对于数据集的制作，请严格按照maixhub上的数据集[制作要求](https://www.maixhub.com/ModelTrainingHelp_zh.html)来进行。如果是分类训练可以不用进行压缩，但是要按压缩包的文件层级要求来将文件放到文件夹中
注意：对于压缩包中的文件夹名字和层级数一定要和要求中的一摸一样！一摸一样！不然会出现数据集读取不到等的一些奇奇怪怪的错误，导致训练不能开始。

## 开始训练

先进行初始化

    python train.py init

开始训练之前，我们需要将自己本地训练的参数进行修改，在instance/config.py中进行修改对应的参数，否则就会出现错误，再进行训练

将数据集放到本地训练源码中的datasets文件夹中，然后在有train.py文件层级上启动命令行界面，和安装依赖的时的启动方法一样。
> 小白不知道怎么改的可以不用去修改

![5.png](https://bbs.sipeed.com/storage/attachments/2021/07/21/CkW1EwXQiKCLsouz5mPJzhVK6S6zn1vcxH1ZcQTA_thumb.png "1461")

分类训练输入

    python train.py -t classifier -z datasets/test_classifier_datasets.zip train

如果是没有压缩的文件夹，则输入

    python train.py -t classifier -d datasets/test_classifier_datasets train

> 这里输入的命令中，在datasets/后面加的是你自己的所制作的数据集名字，不要上来就直接将复制命令运行。

目标检测输入

    python train.py -t detector -z datasets/test_detector_xml_format.zip train

> 这里输入的命令中，在datasets/后面加的是你自己的所制作的数据集名字，不要上来就直接将复制命令运行。

训练完之后就会得到一个out的文件夹，里面的文件就是训练之后得到的模型

## 常见问题

### 训练过程中发现没有使用GPU进行训练的

在命令行中输入python，然后再输入

```python
import tensorflow as tf
tf.test.is_gpu_available()
```

![6.png](https://bbs.sipeed.com/storage/attachments/2021/07/21/i7d0N1b4QdKbXFI74qbDpkoOpSPP64EotABFrXUE_thumb.png "1462")

检查一下这些文件有没有找到，和最后一行是否打印出True
![]()
如果没有，则说明你的前面的cuda和cudnn环境没有安装好，请将所有关于英伟达的软件驱动进行卸载，是卸载！！！不是将文件删除。然后再重新进行cuda和cudnn的环境配置。

### 训练中出现Internal: no kernel image is available for execution on the device

手动安装kernel可以解决

    pip install kernel

### 出现failed: TrainFailReason.ERROR_PARAM, datasets not valid: datasets format error: datasets error, not support format, please check

这种就是没有严格的安装数据集要求来进行制作，检查你的文件夹名字，就可以解决的了，特别是images这个文件夹，容易少了个s

## 出现报错之后，先自己将报错信息进行查看，看不懂可以翻译，不要报错了就直接问，自己都先排查一次