---
title: Sensor 感光元件
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: Sensor 感光元件
---


sensor模块,用于设置感光元件的参数。

使用例程:

- 实时预览摄像头

    ```python
    import sensor #引入感光元件的模块
    sensor.reset()#初始化感光元件
    sensor.set_pixformat(sensor.RGB565)#设置为彩色
    sensor.set_framesize(sensor.QVGA)#设置图像的大小
    sensor.skip_frames()#跳过n张照片，在更改设置后，跳过一些帧，等待感光元件变稳定。

    while(True):
        img = sensor.snapshot()#拍摄一张照片，img为一个image对象
    ```

- 初始化

    ```python
    sensor.reset()# 初始化感光元件
    #设置彩色／黑白
    sensor.set_pixformat()# 设置像素模式。
    sensor.GRAYSCALE# 灰度，每个像素8bit。
    sensor.RGB565# 彩色，每个像素16bit。
    ```

- 设置图像大小


    sensor.QQCIF# 88x72
    sensor.QCIF# 176x144
    sensor.CIF# 352x288
    sensor.QQSIF# 88x60
    sensor.QSIF# 176x120
    sensor.SIF# 352x240
    sensor.QQQQVGA# 40x30
    sensor.QQQVGA# 80x60
    sensor.QQVGA# 160x120
    sensor.QVGA# 320x240
    sensor.VGA# 640x480

    ```python
    sensor.set_framesize()# 设置图像的大小
    ```

- 跳过一些帧

sensor.skip_frames(n=10) 跳过 n 张照片，在更改设置后，跳过一些帧，等待感光元件变稳定。

- 获取一张图像

sensor.snapshot() 拍摄一张照片，返回一个 image 对象。

- 自动增益／白平衡／曝光

sensor.set_auto_gain() 自动增益开启(True)或者关闭(False)。

在使用颜色追踪时，需要关闭自动增益。

sensor.set_auto_whitebal() 自动白平衡开启(True)或者关闭(False)。

在使用颜色追踪时，需要关闭自动白平衡。

sensor.set_auto_exposure(enable[\, exposure_us])

enable 打开(True)或关闭(False)自动曝光。默认打开。

如果 enable 为 False， 则可以用 exposure_us 设置一个固定的曝光时间(以微秒为单位)。

- 设置窗口 ROI

```python
sensor.set_windowing(roi)
```

ROI：Region Of Interest，图像处理中的术语”感兴趣区“。就是在从需要处理的图像中提取出的要处理的区域。

```python
sensor.set_framesize(sensor.VGA) # 高分辨率
sensor.set_windowing((240, 240)) #取中间的 240*240 区域
```

roi 的格式是(x, y, w, h)。


- 设置翻转

```python
#水平方向翻转
sensor.set_hmirror(True)
# 垂直方向翻转
sensor.set_vflip(True)
```
