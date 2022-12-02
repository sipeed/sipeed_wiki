---
title: MaixPy3 camera 模块
keywords: MaixPy3，摄像头, camera API
desc: MaixPy3 camera 模块 API文档, 以及使用说明
---

>! API 仍处于非完全稳定状态, 可能在未来会有小幅改动。

## 导入模块

```python
from maix import camera
```

### camera.width & camera.height

返回当前摄像头配置的图像的宽和高，默认值为（0，0）。

```
>>> print(camera.width(), camera.height())
0 0
```

### camera.config

> 这个 API 涉及硬件容易使软件崩溃所以详细请查阅 [maix/camera.py](https://github.com/sipeed/MaixPy3/blob/release/maix/camera.py)。

主要用于配置摄像头，如获取的图像大小、旋转（部分芯片可选）、翻转（部分芯片可选）。

```python
>>> camera.camera.config(size=(240, 240))
[v4l2] Current data format information:
	width:320
	height:240
	pixelformat:56595559
[camera] config input size(240, 240, 0)
>>> print(camera.width(), camera.height())
240 240
>>>
```

现在作为开发调试的保留功能，像缩放、裁剪、翻转、旋转请使用 image 的一系列函数。

![改变摄像头分辨率可以获得更大的视角](https://wiki.sipeed.com/news/MaixPy3/camera_resize/camera_resize.html)

#### 关于增益和曝光的摄像头控制接口

> 0.5.2 以后给 v83x m2dock 系列的加入了 [exp_gain](https://github.com/sipeed/MaixPy3/commit/d7e5cb04ed31a2ffe135407a0379a701bd3a5522) 函数。

```python
from maix import camera, display, image
camera.config(size=(224, 224))
exp, gain = 16, 16 # 初值，exp 曝光[0, 65536]，gain 增益[16 - 1024]，随意设置得值会受到驱动限制。
for i in range(120):
    exp, gain = exp + 32, gain + 16
    camera.config(exp_gain=(exp, gain))
    img = camera.capture()
    display.show(img)
camera.config(exp_gain=(0, 0)) # 设置为 0, 0 表示放弃控制恢复成自动曝光。
```

做这些控制需要了解摄像头控制增益、曝光会发生什么，传统视觉有时候需要拉低曝光固定亮度去寻色寻线，这时候就需要设置特定的增益和曝光，比如拍白灯的时候需要拉低曝光才能看到灯罩的轮廓。

### camera.capture

捕获一张图像并返回 _maix_image.image 。

（可选功能一）某些设备支持选择获取多个不同尺寸的图像，如 V831 设备。
（可选功能二）可以返回其他模块实现的 image ，如 pillow 模块。

```python
>>> print(camera.capture())
<_maix_image.Image 0x1eb3a10 " width":240, "height":240, "type"=RGB, "size":172800>
```

### camera.close

关闭、释放当前设备。

```python3
camera.close()
```
