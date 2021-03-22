---
title: 基本图像变换 和 常用操作
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 基本图像变换 和 常用操作
---


这里简单介绍一些经常用到的图像的基本变换操作

旋转：

```python
img.rotation_corr()
```

改变图像尺寸：

```python
img.resize()
```

更多的图像变换请看[image API](./../../../api_reference/machine_vision/image/image.md)

## 图像缓冲区介绍

MaixPy 为图像设计了两个缓冲区，
* 一个是`RGB565`缓冲区，顾名思义， 是以`RGB565`的格式存放这图片的信息的一块内存。注意在内存中的排序是`[像素1 RGB, 像素2 RGB...]`
* 另一个是`RGB888`缓冲区，顾名思义， 是以`RGB88`的格式存放这图片的信息的一块内存。注意在内存中的排序是`[所有像素 R, 所有像素 G， 所有像素 B]`, 我们也称之为`AI`内存

这里使用两个内存块主要的原因是底层代码所有图片操作以及`LCD`显示均是基于`RGB565`， 但是`KPU`又需要`RGB888`的输入。

```
                   +---------------+
                   |               |
          +--------+ camera(sensor)+-------+
          |        |               |       |
          |        +---------------+       |
          |                                |
+---------v------+                +--------v---------+
|                | img.pix_to_ai()|                  |
|      RGB565    +--------------->+      RGB888      |
|                |                |                  |
+--------+-------+                +------+-----------+
         ^                               |
         |                               |
         |                               v
+--------+----------+             +------+-----------+
|                   |             |                  |
|     image ops     |             |   KPU            |
|                   |             |                  |
+-------------------+             +------------------+

```



只有摄像头采集图片时，硬件会自动放一份数据到`RGB888`内存区域， 其它的都不会自动填充`RGB888`内存块， 软件操作只会对`RGB565`内存进行操作，不会自动更新`RGB888`，（因为更新需要消耗时间） 这很值得注意，
这意味着，每次我们用更改了`RGB565`内存块，比如执行了`img = img.resize((224, 224))`，如果希望`KPU`使用更改过后的图片， 需要执行`img.pix_to_ai()`来将`RGB565`的图像手动更新到`RGB888`的区域，然后才可以调用`kpu`相关的函数进行模型推理！

同样反方向更新也提供 API： `img.ai_to_pix()`， 这会将`RGB888`区域的数据更新到`RGB565`区域


## resize 修改分辨率

```python
import image
img = image.Image(size=(100, 100))
img2 = img.resize(50, 50)
print(img)
print(img2)
```

## 获取和修改像素值

```python
import image
img = image.Image(size=(10, 10))
print("pixel 0:", img[0], img.get_pixel(0, 0))
img[0] = (255, 0, 0)
img = img.set_pixel(1, 0, (255, 255, 10))
print("after pixel 0 change:", img[0], img[1])
```

这里设置的第二个像素点`B`为`10`， 实际发现读出来是`8`， 这是正常现象，因为前面说了，在内存中储存是用了`RGB565`进行储存，所以会有误差


## 复制图像

```python
import image
img = image.Image(size=(10, 10))
img2 = img.copy()
img2[0] = (255, 0, 0)
print(img[0], img2[0])
```


## 剪裁图像

同样使用`copy`函数

```python
import image
img = image.Image(size=(10, 10))
img2 = img.copy(roi=(0, 0, 5, 5))
img2[0] = (255, 0, 0)
print(img)
print(img2)
print(img[0], img2[0])
```


## 转换成 bytes 对象

转换成 `RGB565` 字符串

```python
import image
img = image.Image(size=(10, 10))
img[0] = (255, 0, 0)
img_bytes = img.to_bytes()
print("bytes length: %d bytes[0]: %x%x" %(len(img_bytes), img_bytes[0], img_bytes[1]))
```
这里输出的值为`RGB565`格式，以两个字节表示一个像素点储存

另外， 也可以先将图片压缩为 `JPEG` 格式，然后再转换成`bytes`
```python
import image
img = image.Image(size=(10, 10))
img = img.compressed(quality=20)
jpeg_bytes = img.to_bytes()
print("bytes length: %d bytes[0]: %x%x" %(len(jpeg_bytes), jpeg_bytes[0], jpeg_bytes[1]))
```

这里使用`compressed`函数不会修改原图， 使用`compress()`函数则会修改原图， 但是压缩后的大小如果比原图占用的空间还大，就会失败



## 转换为灰度图像

```python
img = img.to_grayscale(copy=False)
```

这里 `copy` 参数的意思就是是否要重新申请一片内存， 不修改原图的意思

## 转换为 RGB565 彩图

转换为 彩图， 注意只是格式成为了彩图， 画面并不是彩图， 如果需要将灰度图转换为彩图，使用`img.to_rainbow()`

```python
img = img.to_rgb565(copy=True)
```

这里 `copy` 参数的意思就是是否要重新申请一片内存， 不修改原图的意思
如果原图是灰度图， 必须是`True`

## 转换为彩图

```python
img = img.to_rainbow(copy=True)
```

这里 `copy` 参数的意思就是是否要重新申请一片内存， 不修改原图的意思
如果原图是灰度图， 必须是`True`

## 保存到文件系统

```python
img.save("/sd/test.jpg", quality=95)
img.save("/sd/test.bmp")
```


## 旋转

```python
img.rotation_corr([x_rotation=0.0[, y_rotation=0.0[, z_rotation=0.0[, x_translation=0.0[, y_translation=0.0[, zoom=1.0]]]]]])
```

中括号为可选参数，即沿着哪个轴旋转一定的角度， 如果`minimum`版本的固件里面没有这个函数， 可以用完全版本的固件




