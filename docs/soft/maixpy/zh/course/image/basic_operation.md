---
title: 图像的基本运算
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 图像的基本运算
---


## 坐标

### 获取/设置像素点

我们可以通过 image.get_pixel(x, y) 方法来获取一个像素点的值。

- image.get_pixel(x, y)

    对于灰度图: 返回(x,y)坐标的灰度值.

    对于彩色图: 返回(x,y)坐标的(r,g,b)的tuple.

同样，我们可以通过 image.set_pixel(x, y, pixel) 方法，来设置一个像素点的值。

- image.set_pixel(x, y, pixel)

    对于灰度图: 设置(x,y)坐标的灰度值。

    对于彩色图: 设置(x,y)坐标的(r,g,b)的值。

举例：
```python
img = sensor.snapshot()
img.get_pixel(10,10)
img.set_pixcel(10,10,(255,0,0))#设置坐标(10,10)的像素点为红色(255,0,0)
```

### 获取图像的宽度和高度

- image.width()

    返回图像的宽度(像素)

- image.height()

    返回图像的高度(像素)

- image.format()

    灰度图会返回 sensor.GRAYSCALE，彩色图会返回 sensor.RGB565。

- image.size()

    返回图像的大小(byte)

### 图像的运算

- image.invert()

    取反，对于二值化的图像，0(黑)变成1(白)，1(白)变成0(黑)。

    注：
    图像可以是另一个image对象，或者是从 (bmp/pgm/ppm)文件读入的image对象。
    两个图像都必须是相同的尺寸和类型（灰度图/彩色图）。

- image.nand(image)

    与另一个图片进行与非（NAND）运算。

- image.nor(image)

    与另一个图片进行或非（NOR）运算。

- image.xor(image)

    与另一个图片进行异或（XOR）运算。

- image.xnor(image)

    与另一个图片进行异或非（XNOR）运算。

- image.difference(image)

    从这张图片减去另一个图片。比如，对于每个通道的每个像素点，取相减绝对值操作。这个函数，经常用来做移动检测。
