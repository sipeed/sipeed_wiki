---
title: 人脸检测
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 人脸检测
---


在一张图片中找出人脸， 并且框出人脸，即知道脸的位置和大小

使用了`YOLO V2`模型对人脸进行检测

## 使用方法：

* 下载模型： 到[这里](https://dl.sipeed.com/MAIX/MaixPy/model) 下载 `face_model_at_0x300000.kfpkg` 这个模型文件
* 用 kflash_gui 下载模型到 Flash， 或者放到 SD 卡中
* 加载模型
```python
task = kpu.load(0x300000)
# task = kpu.load("/sd/face.kmodel")
anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)
kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)
```
因为使用了`YOLO V2`这个模型， 它有专用的函数接口， 使用`init_yolo2`来初始化模型

参数分别为：
* `kpu_net`: kpu 网络对象, 即加载的模型对象, `KPU.load()`的返回值
* `threshold`: 概率阈值， 只有是这个物体的概率大于这个值才会输出结果， 取值范围：[0, 1]
* `nms_value`: box_iou 门限, 为了防止同一个物体被框出多个框，当在同一个物体上框出了两个框，这两个框的交叉区域占两个框总占用面积的比例 如果小于这个值时， 就取其中概率最大的一个框
* `anchor_num`: anchor 的锚点数， 这里固定为 `len(anchors)//2`
* `anchor`: 锚点参数与模型参数一致，同一个模型这个参数是固定的，和模型绑定的（训练模型时即确定了）， 不能改成其它值。

然后输入图片数据，运行模型

```python
code = kpu.run_yolo2(task, img)
```

得到结果， 完整例程看[这里](https://github.com/sipeed/MaixPy_scripts/blob/master/machine_vision/face_find/demo_find_face.py)

API 文档看 [Maix.KPU](./../../../api_reference/Maix/kpu.md)






