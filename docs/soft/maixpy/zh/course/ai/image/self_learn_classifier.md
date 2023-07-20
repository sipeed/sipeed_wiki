---
title: 自学习分类器（self learning classifier）
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy  自学习分类器（self learning classifier）
---


无需单独训练， 直接在开发板上对物体特征进行学习，然后直接使用

演示视频： [youtube](https://www.youtube.com/watch?v=aLW1YQrT-2A) 或者 [bilibili](https://www.bilibili.com/video/BV1Ck4y1d7tx)

## 使用方法

* [在这里](https://dl.sipeed.com/shareURL/MAIX/MaixPy/release/master) 下载版本 >= v0.5.0-33 的固件
* [下载 kmodel](https://maixhub.com/model/zoo/61)
* 使用 [kflash_gui](https://github.com/sipeed/kflash_gui) 下载固件和模型
* 运行 [示例脚本](https://github.com/sipeed/MaixPy_scripts/blob/master/machine_vision/self_learning_classifier/self_learning_classifier.py)
> 如果使用 lite 版本的 kmodel, 应该在创建 classifier 的时候传入 `fea_len` 参数为`512`，使用另外一个大一点的（1.8MiB）模型的时候则不需要这个参数:
```python
classifier = kpu.classifier(model, class_num, sample_num, fea_len=512)
```

然后运行启动后开始学习物体

* 按开发板上的 `boot 按钮` 来捕获 3 个类别 `手机`, `小车`, `键盘`， 每个类别只需要捕获一次
* 然后捕获 15 张图， 对顺序没有要求， 比如捕获 5 张 `手机`, 5 张 `小车` ， 5 张 `键盘` 的图片
* 然后它会自动学习这 15 张图的特征
* 最后识别到的图像类别会展示在左上角



## 保存/加载学习好的特征

* 使用 `classifier.save(path)` 来保存学习好的特征到`path`文件
* 使用 `KPU.classifier.load()` 来加载特征, 参考 [self_learning_classifier_load.py](https://github.com/sipeed/MaixPy_scripts/blob/master/machine_vision/self_learning_classifier/self_learning_classifier_load.py) 文件



