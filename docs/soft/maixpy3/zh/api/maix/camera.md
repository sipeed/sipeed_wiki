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

> 这个 API 涉及硬件容易使软件崩溃所以移除了，详细请查阅 [maix/camera.py](https://github.com/sipeed/MaixPy3/blob/release/maix/camera.py)。

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
