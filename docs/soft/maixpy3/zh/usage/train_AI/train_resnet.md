# V831 ResNet18分类模型本地训练

> 2022年01月11日 以下代码由于 Maixpy3 还在施工中，此处代码仅供参考和示范，功能已在 github 和 社区供其他同学使用和参考。

## 配置训练环境

安装 python ，这里就不详细讲述怎么安装

安装 CUDA 11.1 或者安装 CUDA 10.2 ，这个就自行[百度](https://www.baidu.com/s?ie=UTF-8&wd=%E5%AE%89%E8%A3%85CUDA)

安装 pytorch-GPU ，CUDA10.2 在命令行中运行

```
pip3 install torch==1.9.0+cu102 torchvision==0.10.0+cu102 torchaudio===0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
```

CUDA 11.1 在命令行中运行

```
pip3 install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio===0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
```

等待下载并安装

下载训练脚本

```
git clone https://github.com/sipeed/maix_train.git
```

## 开始训练

resnet18 训练脚本在 maix_train\pytorch\classifier 文件夹下

打开 classifier_resnet_train.py 修改 dataset_path 的参数，填写上数据集文件夹的相对路经。如果不知道什么是相对路径，请看[这里](https://blog.csdn.net/qq_34769573/article/details/80445681)

```python
classes = ('chair', 'people')   #分类的类别，需要自己进行修改和添加
dataset_path = "data/datasets"  #数据集文件相对路径
val_split_from_data = 0.1 # 10% 
batch_size = 4                  #以下的参数根据自己的需求进行修改，不知道怎么修改的请自行学习一下深度学习的基础知识
learn_rate = 0.001              #不要去群里问，这里的参数怎么修改，这个涉及的太多基础知识了
total_epoch = 100
eval_every_epoch = 5
save_every_epoch = 20
dataload_num_workers = 2
input_shape = (3, 224, 224)
cards_id = [0]
param_save_path = 'out/classifier_{}.pth'   #这里是保存模型文件的路径
```

打开 classifier_resnet_test.py 根据自己的需求进行参数的修改

```python
test_images_path = sys.argv[1]
classes = ('chair', 'people')   #分类的类别，需要自己进行修改和添加
input_shape = (3, 224, 224)
cards_id = [0]   
param_save_path = sys.argv[2]
onnx_out_name = "out/classifier.onnx"       #模型的位置
ncnn_out_param = "out/classifier.param"     #这里是转换模型的位置（windows可以不用管）
ncnn_out_bin = "out/classifier.bin"  
```

运行 classifier_resnet_train.py 即可开始进行模型训练。

至于模型的部署请看[MaixII Dock上部署resnet18分类网络](https://bbs.sipeed.com/thread/1068)