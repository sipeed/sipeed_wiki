---
title: 人脸识别
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 人脸识别
---


除了检测到人脸的位置以外， 还可以识别到这个人是谁（需要先对准人按按钮学习）

效果视频： [youtube](https://www.youtube.com/embed/hS_mcGptXeo) 或者 [bilibili](https://www.bilibili.com/video/BV1bJ411Q7L6)

<iframe src="https://player.bilibili.com/player.html?aid=77466790&bvid=BV1bJ411Q7L6&cid=132521878&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width=500 height=400> </iframe>

## 使用方法


* 从 [maixhub](https://www.maixhub.com) 按照说明下载模型， 获得模型`smodel`, 就是 加密版本的`kmodel`
* 按照入门教程的方法下载模型到开发板
* 运行脚本 [script](https://github.com/sipeed/MaixPy_scripts/blob/master/machine_vision/face_recognization/demo_face_recognization.py)


## 程序理解

总共用了三个模型， 分别是：
* 人脸检测模型， 这和前面的人脸检测使用的是同一个模型， 即找到人脸
* 人脸关键点检测模型，从前面找到的人脸中找到人脸的 眼睛 鼻子 和 嘴巴 的位置
* 人脸特征提取模型， 从一张人脸图片中得出一个特征值

步骤如下：
* 检测到人脸
* 裁出人脸，找到人脸的眼睛鼻子嘴巴， 这里裁成了`128x128`的图
* 把人脸图中的脸旋转到标准位置
* 用特征提取模型提取出人脸的特征值

有了前面的基础， 这里的程序就能看懂了，也就不再进行详细的阐述了，只不过是从之前的使用一个模型，变成了按照顺序分别使用三个模型，再加上一点简单的图像裁减和旋转处理，都是调用`API`，仔细看一遍代码就知道具体的细节是如何实现的了






