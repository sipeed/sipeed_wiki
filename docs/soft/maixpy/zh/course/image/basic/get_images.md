---
title: 获得图像
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 获得图像
---


可以从摄像头获得图像，也可以从文件系统读取图片文件， 也可以从网络获取图片

## 从摄像头获取


这部分已经在前面的教程有提过

``` python
import sensor, lcd

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
sensor.skip_frames()

img = sensor.snapshot()
print(img)
```

* `import sensor`: 首先导入内置的`sensor`（摄像头）库
* `sensor.reset()`: 初始化摄像头，这里失败需要检查硬件
* `sensor.set_pixformat(sensor.RGB565)`: 设置摄像头为`RGB565`格式，默认都是用`RGB565`即可
* `sensor.set_framesize(sensor.QVGA)`: 分辨率为`QVGA`，即`320x240`
* `sensor.run(1)`: 开始运行，在现在的版本中也可以不调用，在上面设置完成后，摄像头会自动开始运行
* `sensor.skip_frames()`: 摄像头刚启动时，图像质量还没稳定，所以跳过一些图像
* `sensor.snapshot()`:从摄像头取一帧图像数据，返回值是一张图像的对象

除了以上的函数， 你可能还需要设置图像为镜像（`hmirror`)，比如前置摄像头； 或者上下翻转(`vflip`)， 以及白平衡等等， 具体看 [sensor 模块的 API 手册](./../../../api_reference/machine_vision/sensor.md)


## 从文件读取

```python
import image

img = image.Image("/sd/test.jpg")
print(img)
```

当然你也可以把图片保存到文件系统`
```python
img.save("/sd/test2.jpg", quality=95)
```


## 从内存读取（或者网络读取）

可以先将文件读取到内存， 具体是从哪里读取的看你的应用了， 比如网络，或者串口 SPI 等等， 
构造一个 `bytes`对象

```python
import image

jpeg_buff = b'\xFF'   # jpeg buffer
img = image.Image(jpeg_buff, from_bytes = True)
print(img)
```

## 直接创建一个空白图像

```python
import image

img = image.Image(size=(320, 240))
```

这张图片是全黑的空白图像



