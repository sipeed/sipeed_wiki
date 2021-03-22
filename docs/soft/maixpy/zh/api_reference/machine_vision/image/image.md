---
title: image（机器视觉）
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: image（机器视觉）
---


移植于 `openmv`， 与 `openmv` 功能相同

## 例程

### 例程 1： 找绿色

```python
import sensor
import image
import lcd
import time
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
green_threshold   = (0,   80,  -70,   -10,   -0,   30)
while True:
	img=sensor.snapshot()
	blobs = img.find_blobs([green_threshold])
	if blobs:
		for b in blobs:
			tmp=img.draw_rectangle(b[0:4])
			tmp=img.draw_cross(b[5], b[6])
			c=img.get_pixel(b[5], b[6])
	lcd.display(img)
```

### 例程 2： 显示 fps

```python
import sensor
import image
import lcd
import time

clock = time.clock()
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
sensor.skip_frames(30)
while True:
    clock.tick()
    img = sensor.snapshot()
    fps =clock.fps()
    img.draw_string(2,2, ("%2.1ffps" %(fps)), color=(0,128,0), scale=2)
    lcd.display(img)
```


### 例程 3： 扫描二维码

```python
import sensor
import image
import lcd
import time

clock = time.clock()
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(1)
sensor.run(1)
sensor.skip_frames(30)
while True:
    clock.tick()
    img = sensor.snapshot()
    res = img.find_qrcodes()
    fps =clock.fps()
    if len(res) > 0:
        img.draw_string(2,2, res[0].payload(), color=(0,128,0), scale=2)
        print(res[0].payload())
    lcd.display(img)

```

> 如果使用了镜头，画面会有扭曲，需要矫正画面
> 使用 `lens_corr` 函数来矫正， 比如 `2.8`mm， `img.lens_corr(1.8)`




## 函数

函数还可以在本页按 `Ctrl+F` 使用浏览器的搜索功能搜 `image.` 来标记函数

### image.rgb_to_lab(rgb_tuple)

返回RGB888格式的元组 rgb_tuple (r, g, b)对应的LAB格式的元组(l, a, b)。

> RGB888是指红、绿、蓝各8位（0-255）。在LAB中，L的取值范围为0-100，a/b 的取值范围为-128到127。

### image.lab_to_rgb(lab_tuple)

返回LAB格式的元组 lab_tuple (l, a, b)对应的RGB888格式的元组(r, g, b)。

> RGB888是指红、绿、蓝各8位（0-255）。在LAB中，L的取值范围为0-100，a/b 的取值范围为-128到127。

### image.rgb_to_grayscale(rgb_tuple)

返回RGB888格式的元组 rgb_tuple (r, g, b)对应的灰度值。

> RGB888是指红、绿、蓝各8位（0-255）。灰度值取值于0-255。

### image.grayscale_to_rgb(g_value)

返回灰度值 g_value 对应的RGB888格式的元组(r, g, b)。

> RGB888是指红、绿、蓝各8位（0-255）。灰度值取值于0-255。

### image.load_decriptor(path)

从磁盘上加载一个描述符对象(descriptor object).

path 是描述符文件保存的路径。

### image.save_descriptor(path, descriptor)

保存描述符对象 descriptor 到磁盘。

path 是描述符文件保存的路径。

### image.match_descriptor(descritor0, descriptor1[, threshold=70[, filter_outliers=False]])

对于LBP描述符来说，这个函数返回的是一个体现两个描述符之间区别的整数。这一距离测度尤为必要。这个距离是对相似度的一个度量。这个测度值越接近0，LBPF特征点匹配得就越好。

对于ORB描述符来说，这个函数返回的是kptmatch对象。见上。

threshold 是用来为ORB键点过滤不明确匹配服务的。
一个较低的 threshold 值将紧扣关键点匹配算法。 threshold 值位于0-100 (int)。默认值为70。

filter_outliers 是用来为ORB键点过滤异常值服务的。 特征点允许用户提高 threshold 值。默认设置为False。

## HaarCascade 类 – 特征描述符

Haar Cascade特征描述符用于 `image.find_features()` 方法。它没有供用户调用的方法。

### 构造函数

class image.HaarCascade(path[, stages=Auto])

从一个Haar Cascade二进制文件（适合OpenMV Cam的格式）加载一个Haar Cascade。 如果您传递“frontalface”字符串 而非一条路径，这个构造函数将会把一个内置的正脸Haar Cascade载入内存。 此外，您也可以通过“eye”来把Haar Cascade载入内存。 最后，这个方法会返回载入的Haar Cascade对象，用来使用 image.find_features() 。

stages 默认值为Haar Cascade中的阶段数。然而，您可以指定一个较低的数值来加速运行特征检测器，当然这会带来较高的误报率。

> 您可以制作自己的Haar Cascades 来配合您的OpenMV Cam 使用。 首先，使用谷歌搜索“<thing> Haar Cascade”，检测是否有人已经为您想要检测的对象制作了OpenCV Haar Cascade。 如果没有，那您需要自己动手制作（工作量巨大）。 关于如何制作自己的Haar Cascade，见此 关于如何把OpenCV Haar Cascades转化成您的OpenMV Cam可以读取的模式， 见此script

问：Haar Cascade 是什么？

答：Haar Cascade是一系列用来确定一个对象是否存在于图像中的对比检查。 这一系列的对比检查分成了多个阶段，后一阶段的运行以先前阶段的完成为前提。 对比检查并不复杂，不过是像检查图像的中心垂直是否比边缘更轻微之类的过程。 大范围的检查在前期阶段首先进行，在后期进行更多更小的区域检查。

问：Haar Cascades 是如何制作而成的？

答：Haar Cascades通过标有正负的图像对发生器算法进行训练。 比如，用数百张含有猫（已被标记为内含猫）的图片和数百张不含有猫形物的图片（已作出不同标记）来训练这个生成算法。 这个生成算法最后会产生一个用来检测猫的Haar Cascades。

## Similarity 类 – 相似度对象

相似度对象由 `image.get_similarity` 返回.

### 构造函数

class image.similarity

请调用 image.get_similarity() 函数来创建此对象。

#### 方法

##### similarity.mean()
返回8x8像素块结构相似性差异的均值。范围[-1/+1]，其中 -1完全不同，+1完全相同。

您也可以通过索引 [0] 取得这个值。

##### similarity.stdev()
返回8x8像素块结构相似性差异的标准偏差。

您也可以通过索引 [1] 取得这个值。

##### similarity.min()
返回8x8像素块结构相似性差异的最小值。其中 -1完全不同，+1完全相同。

您也可以通过索引 [2] 取得这个值。

> 通过查看此值，您可以快速确定两个图像之间的任何8x8像素块是否差别很大，即远远低于+1。

##### similarity.max()

返回8x8像素块结构相似性差异的最小值。其中 -1完全不同，+1完全相同。

您也可以通过索引 [3] 取得这个值。

> 通过查看此值，您可以快速确定两个图像之间的任何8x8像素块是否都相同。即比-1大很多。

## Histogram 类 – 直方图对象

直方图对象是由 `image.get_histogram` 返回。 灰度直方图有一个包含多个二进制的通道。 所有二进制都进行标准化，使其总和为1。 RGB565有三个包含多个二进制的通道。所有二进制都进行标准化，使其总和为1。

### 构造函数

class image.histogram

请调用 `image.get_histogram()` 函数来创建此对象。

### 方法

#### histogram.bins()

返回灰度直方图的浮点数列表。 您也可以通过索引 [0] 取得这个值。

#### histogram.l_bins()

返回RGB565直方图LAB的L通道的浮点数列表。 您也可以通过索引 [0] 取得这个值。

#### histogram.a_bins()

返回RGB565直方图LAB的A通道的浮点数列表。 您也可以通过索引 [1] 取得这个值。

#### histogram.b_bins()

返回RGB565直方图LAB的B通道的浮点数列表。 您也可以通过索引 [2] 取得这个值。

#### histogram.get_percentile(percentile)

计算直方图频道的CDF，返回一个传递 percentile (0.0 - 1.0) (浮点数)中的直方图的值。

因此，若您传入0.1，该方法会告知您，当累加入累加器时，哪一个二进制会使累加器跨过0.1。

在没有异常效用破坏您的自适应色跟踪结果时，这对于确定颜色分布的最小值(0.1)和max(0.9)甚是有效。

#### histogram.get_threhsold()

使用Otsu’s 方法计算最佳阈值，将直方图分的每个通道为两半。 该方法返回一个 image.threshold 对象。 这个方法对确定最佳的 image.binary() 阈值特别有用。

#### histogram.get_statistics()

计算直方图中每个颜色通道的平均值、中值、众值、标准差、最小值、最大值、下四分值和上四分值， 并返回一个statistics对象。 您也可以使用 histogram.statistics() 和 histogram.get_stats() 作为这个方法的别名。





## Percentile 类 – 百分比值对象

百分比值对象由 `histogram.get_percentile` 返回。 灰度百分比值有一个通道。不使用 l_* 、 a_* 或 b_* 方法。 RGB565百分比值有三个通道。使用 l_* 、 a_* 和 b_* 方法。

### 构造函数

class image.percentile

请调用 histogram.get_percentile() 函数来创建此对象。

### 方法

#### percentile.value()

返回灰度百分比值（取值区间为0-255）。

您也可以通过索引 [0] 取得这个值。

#### percentile.l_value()

返回RGB565 LAB 的L通道的百分比值（取值区间为0-100）。

您也可以通过索引 [0] 取得这个值。

#### percentile.a_value()

返回RGB565 LAB 的A通道的百分比值（取值区间为-128-127）。

您也可以通过索引 [1] 取得这个值。

#### percentile.b_value()

返回RGB565 LAB 的B通道的百分比值（取值区间为-128-127）。

您也可以通过索引 [2] 取得这个值。

## Threhsold 类 – 阈值对象

阈值对象由 histogram.get_threshold 返回。

灰度图像有一个通道。没有 l_*, a_*, 和 b_* 方法.

RGB565 阈值有三个通道。使用 l_*, a_*, 和 b_* 方法。

### 构造函数

class image.threshold

请调用 histogram.get_threshold() 函数来创建此对象。

#### 方法

#### threhsold.value()

返回灰度图的阈值 (between 0 and 255)。

您也可以通过索引 [0] 取得这个值。

#### threhsold.l_value()

返回RGB565图LAB中的L阈值 (between 0 and 100).

您也可以通过索引 [0] 取得这个值。

#### threhsold.a_value()

返回RGB565图LAB中的A阈值 (between -128 and 127).

您也可以通过索引 [1] 取得这个值。

#### threhsold.b_value()

返回RGB565图LAB中的B阈值 (between -128 and 127).

您也可以通过索引 [2] 取得这个值。

## class Statistics – 统计数据对象

统计数据对象是由 histogram.get_statistics 或 image.get_statistics 返回的。

灰度统计数据有一个通道，使用非 l_* 、 a_* 或 b_* 方法。

RGB565百分比值有三个通道。使用 l_* 、 a_* 和 b_* 方法。

### 构造函数

class image.statistics
请调用 histogram.get_statistics() 或 image.get_statistics() 函数来创建此对象。

### 方法

#### statistics.mean()

返回灰度均值(0-255) (int)。

您也可以通过索引 [0] 取得这个值。

#### statistics.median()

返回灰度中值(0-255) (int)。

您也可以通过索引 [1] 取得这个值。

#### statistics.mode()

返回灰度众值(0-255) (int)。

您也可以通过索引 [2] 取得这个值。

#### statistics.stdev()

返回灰度标准差(0-255) (int)。

您也可以通过索引 [3] 取得这个值。

#### statistics.min()

返回灰度最小值(0-255) (int)。

您也可以通过索引 [4] 取得这个值。

#### statistics.max()

返回灰度最大值(0-255) (int)。

您也可以通过索引 [5] 取得这个值。

#### statistics.lq()

返回灰度下四分值(0-255) (int)。

您也可以通过索引 [6] 取得这个值。

#### statistics.uq()

返回灰度上四分值(0-255) (int)。

您也可以通过索引 [7] 取得这个值。

#### statistics.l_mean()

返回RGB5656 LAB 中L的均值(0-255) (int)。

您也可以通过索引 [0] 取得这个值。

#### statistics.l_median()

返回RGB5656 LAB 中L的中值(0-255) (int)。

您也可以通过索引 [1] 取得这个值。

#### statistics.l_mode()

返回RGB5656 LAB 中L的众值(0-255) (int)。

您也可以通过索引 [2] 取得这个值。

#### statistics.l_stdev()

返回RGB5656 LAB 中L的标准偏差值(0-255) (int)。

您也可以通过索引 [3] 取得这个值。

#### statistics.l_min()

返回RGB5656 LAB 中L的最小值(0-255) (int)。

您也可以通过索引 [4] 取得这个值。

#### statistics.l_max()

返回RGB5656 LAB 中L的最大值(0-255) (int)。

您也可以通过索引 [5] 取得这个值。

#### statistics.l_lq()

返回RGB5656 LAB 中L的下四分值(0-255) (int)。

您也可以通过索引 [6] 取得这个值。

#### statistics.l_uq()

返回RGB5656 LAB 中L的上四分值(0-255) (int)。

您也可以通过索引 [7] 取得这个值。

#### statistics.a_mean()

返回RGB5656 LAB 中A的均值(0-255) (int)。

您也可以通过索引 [8] 取得这个值。

#### statistics.a_median()

返回RGB5656 LAB 中A的中值(0-255) (int)。

您也可以通过索引 [9] 取得这个值。

#### statistics.a_mode()

返回RGB5656 LAB 中A的众值(0-255) (int)。

您也可以通过索引 [10] 取得这个值。

#### statistics.a_stdev()

返回RGB5656 LAB 中A的标准偏差值(0-255) (int)。

您也可以通过索引 [11] 取得这个值。

#### statistics.a_min()

返回RGB5656 LAB 中A的最小值(0-255) (int)。

您也可以通过索引 [12] 取得这个值。

#### statistics.a_max()

返回RGB5656 LAB 中A的最大值(0-255) (int)。

您也可以通过索引 [13] 取得这个值。

#### statistics.a_lq()

返回RGB5656 LAB 中A的下四分值(0-255) (int)。

您也可以通过索引 [14] 取得这个值。

#### statistics.a_uq()

返回RGB5656 LAB 中A的上四分值(0-255) (int)。

您也可以通过索引 [15] 取得这个值。

#### statistics.b_mean()

返回RGB5656 LAB 中B的均值(0-255) (int)。

您也可以通过索引 [16] 取得这个值。

#### statistics.b_median()

返回RGB5656 LAB 中B的中值(0-255) (int)。

您也可以通过索引 [17] 取得这个值。

#### statistics.b_mode()

返回RGB5656 LAB 中B的众值(0-255) (int)。

您也可以通过索引 [18] 取得这个值。

#### statistics.b_stdev()

返回RGB5656 LAB 中B的标准差值(0-255) (int)。

您也可以通过索引 [19] 取得这个值。

#### statistics.b_min()

返回RGB5656 LAB 中B的最小值(0-255) (int)。

您也可以通过索引 [20] 取得这个值。

#### statistics.b_max()

返回RGB5656 LAB 中B的最大值(0-255) (int)。

您也可以通过索引 [21] 取得这个值。

#### statistics.b_lq()

返回RGB5656 LAB 中B的下四分值(0-255) (int)。

您也可以通过索引 [22] 取得这个值。

#### statistics.b_uq()

返回RGB5656 LAB 中B的上四分值(0-255) (int)。

您也可以通过索引 [23] 取得这个值。

## Blob 类 – 色块对象

色块对象是由 `image.find_blobs` 返回的。

### 构造函数

class image.blob

请调用 image.find_blobs() 函数来创建此对象。

### 方法

#### blob.rect()

返回一个矩形元组(x, y, w, h) ，用于如色块边界框的 image.draw_rectangle 等 其他的 image 方法。

#### blob.x()

返回色块的边界框的x坐标(int)。

您也可以通过索引 [0] 取得这个值。

#### blob.y()
返回色块的边界框的y坐标(int)。

您也可以通过索引 [1] 取得这个值。

#### blob.w()

返回色块的边界框的w坐标(int)。

您也可以通过索引 [2] 取得这个值。

#### blob.h()

返回色块的边界框的h坐标(int)。

您也可以通过索引 [3] 取得这个值。

#### blob.pixels()

返回从属于色块(int)一部分的像素数量。

您也可以通过索引 [4] 取得这个值。

#### blob.cx()

返回色块(int)的中心x位置。

您也可以通过索引 [5] 取得这个值。

#### blob.cy()

返回色块(int)的中心x位置。

您也可以通过索引 [6] 取得这个值。

#### blob.rotation()

返回色块的旋转（单位：弧度）。如果色块类似铅笔或钢笔，那么这个值就是介于0-180之间的唯一值。 如果这个色块圆的，那么这个值就没有效用。如果这个色块完全不具有对称性，您只能由此得到0-360度的旋转。

您也可以通过索引 [7] 取得这个值。

#### blob.code()

返回一个16位的二进制数字，其中为每个颜色阈值设置一个位，这是色块的一部分。 例如，如果您通过 image.find_blobs 来寻找三个颜色阈值，这个色块可以设置为0/1/2位。 注意：除非以 merge=True 调用 image.find_blobs ，否则每个色块只能设置一位。 那么颜色阈值不同的多个色块就可以合并在一起了。 您也可以用这个方法以及多个阈值来实现颜色代码跟踪。

您也可以通过索引 [8] 取得这个值。

#### blob.count()

返回合并为这一色块的多个色块的数量。只有您以 merge=True 调用 image.find_blobs 时，这个数字才不是1。

您也可以通过索引 [9] 取得这个值。

#### blob.area()

返回色块周围的边框面积(w * h)

#### blob.density()

返回这个色块的密度比。这是在色块边界框区域内的像素点的数量。 总的来说，较低的密度比意味着这个对象的锁定得不是很好。

## Line类 – 直线对象

直线对象是由 `image.find_lines` , `image.find_line_segments`  或  `image.get_regression` 返回的。

### 构造函数

class image.line

请调用 image.find_lines(), image.find_line_segments(), 或 image.get_regression() 函数来创建此对象。

### 方法

#### line.line()

返回一个直线元组(x1, y1, x2, y2) ，用于如 image.draw_line 等其他的 image 方法。

#### line.x1()

返回直线的p1顶点 x坐标分量。

您也可以通过索引 [0] 取得这个值。

#### line.y1()

返回直线的p1 y分量。

您也可以通过索引 [1] 取得这个值。

#### line.x2()

返回直线的p2 x分量。

您也可以通过索引 [2] 取得这个值。

#### line.y2()

返回直线的p2 y分量。

您也可以通过索引 [3] 取得这个值。

#### line.length()

返回直线长度即 sqrt(((x2-x1)^2) + ((y2-y1)^2).

您也可以通过索引 [4] 取得这个值。

#### line.magnitude()

返回霍夫变换后的直线的长度。

您也可以通过索引 [5] 取得这个值。

#### line.theta()

返回霍夫变换后的直线的角度（0-179度）。

您也可以通过索引 [7] 取得这个值。

#### line.rho()

返回霍夫变换后的直线p值。

您也可以通过索引 [8] 取得这个值。

## Circle类 –圆形对象

圆形对象是由 `image.find_circles` 返回的。

### 构造函数

class image.circle

请调用 image.find_circles() 函数来创建此对象。

### 方法

#### circle.x()

返回圆的x位置。

您也可以通过索引 [0] 取得这个值。

#### circle.y()

返回圆的y位置。

您也可以通过索引 [1] 取得这个值。

#### circle.r()

返回圆的半径。

您也可以通过索引 [2] 取得这个值。

#### circle.magnitude()

返回圆的大小。

您也可以通过索引 [3] 取得这个值。

## Rect类 – 矩形对象

矩形对象是由 `image.find_rects` 返回的。

### 构造函数

class image.rect

请调用 image.find_rects() 函数来创建此对象。

### 方法

#### rect.corners()

返回一个由矩形对象的四个角组成的四个元组(x,y)的列表。四个角通常是按照从左上角开始沿顺时针顺序返回的。

#### rect.rect()

返回一个矩形元组(x, y, w, h)，用于如 矩形的边界框的 image.draw_rectangle 等其他的 image 方法。

#### rect.x()

返回矩形的左上角的x位置。

您也可以通过索引 [0] 取得这个值。

#### rect.y()

返回矩形的左上角的y位置。

您也可以通过索引 [1] 取得这个值。

#### rect.w()

返回矩形的宽度。

您也可以通过索引 [2] 取得这个值。

#### rect.h()

返回矩形的高度。

您也可以通过索引 [3] 取得这个值。

#### rect.magnitude()

返回矩形的大小。

您也可以通过索引 [4] 取得这个值。

## QRCode类 – 二维码对象

二维码对象是由 `image.find_qrcodes` 返回的。

### 构造函数

class image.qrcode

请调用 image.find_qrcodes() 函数来创建此对象。

### 方法

#### qrcode.corners()

返回一个由该对象的四个角组成的四个元组(x,y)的列表。四个角通常是按照从左上角开始沿顺时针顺序返回的。

#### qrcode.rect()

返回一个矩形元组(x, y, w, h)，用于如二维码的边界框的 image.draw_rectangle 等其他的 image 方法。

#### qrcode.x()

返回二维码的边界框的x坐标(int)。

您也可以通过索引 [0] 取得这个值。

#### qrcode.y()

返回二维码的边界框的y坐标(int)。

您也可以通过索引 [1] 取得这个值。

#### qrcode.w()

返回二维码的边界框的w坐标(int)。

您也可以通过索引 [2] 取得这个值。

#### qrcode.h()

返回二维码的边界框的h坐标(int)。

您也可以通过索引 [3] 取得这个值。

#### qrcode.payload()

返回二维码有效载荷的字符串，例如URL 。

您也可以通过索引 [4] 取得这个值。

#### qrcode.version()

返回二维码的版本号(int)。

您也可以通过索引 [5] 取得这个值。

#### qrcode.ecc_level()

返回二维码的ECC水平(int)。

您也可以通过索引 [6] 取得这个值。

#### qrcode.mask()

返回二维码的掩码(int)。

您也可以通过索引 [7] 取得这个值。

#### qrcode.data_type()

返回二维码的数据类型。

您也可以通过索引 [8] 取得这个值。

#### qrcode.eci()

返回二维码的ECI。ECI储存了QR码中存储数据字节的编码。若您想要处理包含超过标准ASCII文本的二维码，您需要查看这一数值。

您也可以通过索引 [9] 取得这个值。

#### qrcode.is_numeric()

若二维码的数据类型为数字式，则返回True。

#### qrcode.is_alphanumeric()

若二维码的数据类型为文字数字式，则返回True。

#### qrcode.is_binary()

若二维码的数据类型为二进制式，则返回True。如果您认真处理所有类型的文本，则需要检查eci是否为True，以确定数据的文本编码。通常它只是标准的ASCII，但是它也可能是有两个字节字符的UTF8。

#### qrcode.is_kanji()

若二维码的数据类型为日本汉字，则返回True。设置为True后，您就需要自行解码字符串，因为日本汉字符号每个字符是10位，而MicroPython不支持解析这类文本。

## AprilTag类 – AprilTag对象

AprilTag对象是由 `image.find_apriltags` 返回的。

### 构造函数

class image.apriltag

请调用 image.find_apriltags() 函数来创建此对象。

### 方法

#### apriltag.corners()

返回一个由该对象的四个角组成的四个元组(x,y)的列表。四个角通常是按照从左上角开始沿顺时针顺序返回的。

#### apriltag.rect()


返回一个矩形元组(x, y, w, h)，用于如AprilTag边界框的 image.draw_rectangle 等其他的 image 方法。

#### apriltag.x()

返回AprilTag边界框的x坐标(int)。

您也可以通过索引 [0] 取得这个值。

#### apriltag.y()

返回AprilTag边界框的y坐标(int)。

您也可以通过索引 [1] 取得这个值。

#### apriltag.w()

返回AprilTag边界框的w坐标(int)。

您也可以通过索引 [2] 取得这个值。

#### apriltag.h()

返回AprilTag边界框的h坐标(int)。

您也可以通过索引 [3] 取得这个值。

#### apriltag.id()

返回AprilTag的数字ID。

TAG16H5 -> 0 to 29
TAG25H7 -> 0 to 241
TAG25H9 -> 0 to 34
TAG36H10 -> 0 to 2319
TAG36H11 -> 0 to 586
ARTOOLKIT -> 0 to 511
您也可以通过索引 [4] 取得这个值。

#### apriltag.family()

返回AprilTag的数字家庭。

image.TAG16H5
image.TAG25H7
image.TAG25H9
image.TAG36H10
image.TAG36H11
image.ARTOOLKIT
您也可以通过索引 [5] 取得这个值。

#### apriltag.cx()

返回AprilTag的中心x位置(int)。

您也可以通过索引 [6] 取得这个值。

#### apriltag.cy()

返回AprilTag的中心y位置(int)。

您也可以通过索引 [7] 取得这个值。

#### apriltag.rotation()

返回以弧度计的AprilTag的旋度(int)。

您也可以通过索引 [8] 取得这个值。

#### apriltag.decision_margin()

返回AprilTag匹配的色饱和度（取值0.0 - 1.0），其中1.0为最佳。

您也可以通过索引 [9] 取得这个值。

#### apriltag.hamming()

返回AprilTag的可接受的数位误差数值。

TAG16H5 -> 最多可接受0位错误
TAG25H7 -> 最多可接受1位错误
TAG25H9 -> 最多可接受3位错误
TAG36H10 -> 最多可接受3位错误
TAG36H11 -> 最多可接受4位错误
ARTOOLKIT -> 最多可接受0位错误
您也可以通过索引 [10] 取得这个值。

#### apriltag.goodness()

返回AprilTag图像的色饱和度（取值0.0 - 1.0），其中1.0为最佳。

> 目前这一数值通常是0.0。未来我们可以启用一个称为“标签细化”的功能，以实现对更小的AprilTag的检测。然而，现在这个功能将帧速率降低到1 FPS以下。

您也可以通过索引 [11] 取得这个值。

#### apriltag.x_translation()

返回距离摄像机x方向的变换，距离的单位未知。

这个方法对于确定远离摄像机的AprilTag的位置很有用。但是，AprilTag的大小以及您使用的镜头等因素都会影响X单元归属的确定。为使用方便，我们推荐您使用查找表将该方法的输出转换为对您的应用程序有用的信息。

注意：此处的方向为从左至右。

您也可以通过索引 [12] 取得这个值。

#### apriltag.y_translation()

返回距离摄像机y方向的变换，距离的单位未知。

这个方法对于确定远离摄像机的AprilTag的位置很有用。但是，AprilTag的大小以及您使用的镜头等因素都会影响Y单元归属的确定。为使用方便，我们推荐您使用查找表将该方法的输出转换为对您的应用程序有用的信息。

注意：此处的方向为从上至下。

您也可以通过索引 [13] 取得这个值。

#### apriltag.z_translation()

返回距离摄像机z方向的变换，距离的单位未知。

T这个方法对于确定远离摄像机的AprilTag的位置很有用。但是，AprilTag的大小以及您使用的镜头等因素都会影响Z单元归属的确定。为使用方便，我们推荐您使用查找表将该方法的输出转换为对您的应用程序有用的信息。

注意：此处的方向为从前至后。

您也可以通过索引 [14] 取得这个值。

#### apriltag.x_rotation()

返回以弧度计的AprilTag在X平面上的旋度。例：目视AprilTag，从左至右移动摄像头。

您也可以通过索引 [15] 取得这个值。

#### apriltag.y_rotation()

返回以弧度计的AprilTag在Y平面上的旋度。例：目视AprilTag，从上至下移动摄像头。

您也可以通过索引 [16] 取得这个值。

#### apriltag.z_rotation()

返回以弧度计的AprilTag在Z平面上的旋度。例：目视AprilTag，旋转摄像头。

注意：这只是 apriltag.rotation() 的重命名版本。

您也可以通过索引 [17] 取得这个值。

## DataMatrix类 – 数据矩阵对象

数据矩阵对象是由 `image.find_datamatrices` 返回的。

## 构造函数

class image.datamatrix

请调用 image.find_datamatrices() 函数来创建此对象。

### 方法

#### datamatrix.corners()

返回一个由该对象的四个角组成的四个元组(x,y)的列表。四个角通常是按照从左上角开始沿顺时针顺序返回的。

#### datamatrix.rect()

返回一个矩形元组(x, y, w, h)，用于如数据矩阵的边界框的 image.draw_rectangle 等其他的 image 方法。

#### datamatrix.x()

返回数据矩阵的边界框的x坐标(int)。

您也可以通过索引 [0] 取得这个值。

#### datamatrix.y()

返回数据矩阵的边界框的y坐标(int)。

您也可以通过索引 [1] 取得这个值。

#### datamatrix.w()

返回数据矩阵的边界框的w宽度。

您也可以通过索引 [2] 取得这个值。

#### datamatrix.h()

返回数据矩阵的边界框的h高度。

您也可以通过索引 [3] 取得这个值。

#### datamatrix.payload()

返回数据矩阵的有效载荷的字符串。例：字符串。

您也可以通过索引 [4] 取得这个值。

#### datamatrix.rotation()

返回以弧度计的数据矩阵的旋度(浮点数)。

您也可以通过索引 [5] 取得这个值。

#### datamatrix.rows()

返回数据矩阵的行数(int)。

您也可以通过索引 [6] 取得这个值。

#### datamatrix.columns()

返回数据矩阵的列数(int)。

您也可以通过索引 [7] 取得这个值。

#### datamatrix.capacity()

返回这一数据矩阵所能容纳的字符的数量。

您也可以通过索引 [8] 取得这个值。

#### datamatrix.padding()

返回这一数据矩阵中未使用的字符的数量。

您也可以通过索引 [9] 取得这个值。

## BarCode类 – 条形码对象

条形码对象是由 image.find_barcodes 返回的。

## 构造函数

class image.barcode

请调用 image.find_barcodes() 函数来创建此对象。

### 方法

#### barcode.corners()

返回一个由该对象的四个角组成的四个元组(x,y)的列表。四个角通常是按照从左上角开始沿顺时针顺序返回的。

#### barcode.rect()

返回一个矩形元组(x, y, w, h)，用于如数据矩阵的边界框的 image.draw_rectangle 等其他的 image 方法。

#### barcode.x()

返回条形码的边界框的x坐标(int)。

您也可以通过索引 [0] 取得这个值。

#### barcode.y()

返回条形码的边界框的y坐标(int)。

您也可以通过索引 [1] 取得这个值。

#### barcode.w()

返回条形码的边界框的w宽度(int)。

您也可以通过索引 [2] 取得这个值。

#### barcode.h()

返回条形码的边界框的h高度(int)。

您也可以通过索引 [3] 取得这个值。

#### barcode.payload()

返回条形码的有效载荷的字符串。例：数量。

您也可以通过索引 [4] 取得这个值。

#### barcode.type()

返回条形码的列举类型 (int)。

您也可以通过索引 [5] 取得这个值。

image.EAN2
image.EAN5
image.EAN8
image.UPCE
image.ISBN10
image.UPCA
image.EAN13
image.ISBN13
image.I25
image.DATABAR
image.DATABAR_EXP
image.CODABAR
image.CODE39
image.PDF417 - 未来启用 (e.g. 现在还不能正常使用).
image.CODE93
image.CODE128

#### barcode.rotation()

返回以弧度计的条形码的旋度(浮点数)。

您也可以通过索引 [6] 取得这个值。

#### barcode.quality()

返回条形码在图像中被检测到的次数(int)。

扫描条形码时，每一条新的扫描线都能解码相同的条形码。每次进行这一过程，条形码的值都会随之增加。

您也可以通过索引 [7] 取得这个值。

## Displacement类 – 位移对象

位移对象由 image.find_displacement 返回。

### 构造函数

class image.displacement

请调用 image.find_displacement() 函数来创建此对象。

### 方法

#### displacement.x_translation()

返回两个图像之间的x平移像素。 这是精确的子像素，所以它是一个浮点数。

您也可以通过索引 [0] 取得这个值。

#### displacement.y_translation()

返回两个图像之间的y平移像素。 这是精确的子像素，所以它是一个浮点数。

您也可以通过索引 [1] 取得这个值。

#### displacement.rotation()

返回两个图像之间的z平移像素。 这是精确的子像素，所以它是一个浮点数。

您也可以通过索引 [2] 取得这个值。

#### displacement.scale()

返回两个图像之间旋转的弧度。

您也可以通过索引 [3] 取得这个值。

#### displacement.response()

返回两幅图像之间位移匹配结果的质量。 范围 0-1。响应小于0.1的 displacement 对象可能是噪声。

您也可以通过索引 [4] 取得这个值。

## Kptmatch类 – 特征点对象

特征点对象是由 `image.match_descriptor` 返回的。

### 构造函数

class image.kptmatch

请调用 image.match_descriptor() 函数来创建此对象。

### 方法

#### kptmatch.rect()

返回一个矩形元组(x, y, w, h)，用于如特征点的边界框的 image.draw_rectangle 等其他的 image 方法。

#### kptmatch.cx()

返回特征点的中心x位置(int)。

您也可以通过索引 [0] 取得这个值。

#### kptmatch.cy()

返回特征点的中心y位置(int)。

您也可以通过索引 [1] 取得这个值。

#### kptmatch.x()

返回特征点边界框的x坐标(int)。

您也可以通过索引 [2] 取得这个值。

#### kptmatch.y()

返回特征点边界框的y坐标(int)。

您也可以通过索引 [3] 取得这个值。

#### kptmatch.w()

返回特征点边界框的w宽度(int)。

您也可以通过索引 [4] 取得这个值。

#### kptmatch.h()

返回特征点边界框的h高度(int)。

您也可以通过索引 [5] 取得这个值。

#### kptmatch.count()

返回匹配的特征点的数量(int)。

您也可以通过索引 [6] 取得这个值。

#### kptmatch.theta()

返回估计的特征点的旋度(int)。

您也可以通过索引 [7] 取得这个值。

#### kptmatch.match()

返回匹配关键点的(x，y)元组列表。

您也可以通过索引 [8] 取得这个值。

## ImageWriter类 – ImageWriter对象

ImageWriter 对象使得您可以快速地将未压缩的图像写入磁盘。

##＃　构造函数

class image.ImageWriter(path)

创建一个ImageWriter对象，您就可以以用于OpenMV Cams的简单文件格式将未压缩的图像写到磁盘上。然后未压缩的图像可以使用ImageReader重新读取。

### 方法

#### imagewriter.size()

返回正在写入的文件的大小。

#### imagewriter.add_frame(img)

将一张图像写入磁盘。由于图像未被压缩，因此执行迅速，但会占用大量磁盘空间。

#### imagewriter.close()

关闭图像流文件。您必须关闭文件，否则文件会损坏。

## ImageReader 类– ImageReader对象

ImageReader对象使得您可以快速地从磁盘中读取未压缩的图像。

### 构造函数

class image.ImageReader(path)

创建一个ImageReader对象，用来回放由ImageWriter对象编写的图像数据。ImageWriter对象回放的帧会在与写入磁盘时相同的FPS下回放。

### 方法

#### imagereader.size()

返回正在读取的文件的大小。

imagereader.next_frame([copy_to_fb=True, loop=True])
从ImageWriter写就的文件中返回图像对象。若 copy_to_fb 为True，图像对象将被直接加载到帧缓冲区中。否则图像对象将被放入堆中。注意：除非图像很小，否则堆可能没有足够的空间来存储图像对象。 若 loop 为True，流的最后一个图像读取之后，回放将重新开始。否则所有帧被读取后，这个方法将返回None。

注意： imagereader.next_frame 尝试在读取帧后通过暂停播放来限制回放速度，以与帧记录的速度相匹配。 否则，这个方法会以200+FPS的速度图像快读播放所有图像。

#### imagereader.close()

关闭正在读取的文件。您需要进行这一操作，以防imagereader 对象受损。但由于是只读文件，文件不会在未关闭时受损。

## Image类 – 图像对象

图像对象是机器视觉操作的基本对象。

### 构造函数

class image.Image(path[, copy_to_fb=False])

从 path 中的文件中创建一个新的图像对象。

支持bmp/pgm/ppm/jpg/jpeg格式的图像文件。

若 copy_to_fb 为True，图像会直接载入帧缓冲区，您就可以加载大幅图片了。若为False，图像会载入MicroPython的堆中，堆远比帧缓冲区小。

在OpenMV Cam M4中，若 copy_to_fb 为False，您应该尽量把图像大小控制在8KB以下。若为True，则图像最大可为160KB。
在OpenMV Cam M7中，若 copy_to_fb 为False，您应该尽量把图像大小控制在16KB以下。若为True，则图像最大可为320KB。
图像支持“[]”记法。 令 image[index] = 8/16-bit value ，以便分配图像像素或 image[index] ，并得到一个图像像素，若是用于RGB图像的16位RGB565值的灰度图像， 这一像素则为8位。

对于JPEG图像而言，“[]”使得您可以访问压缩的节数组形式的JPEG图像色块。由于JPEG图像是压缩的字节流形式，因而对数据组的读取和写入是不透明的。

图像还支持读缓冲区操作。您可以把图像当作节数组对象，将图像输入所有类型的MicroPython函数。若您想传送一个图像，可以将它传递给UART /SPI/ I2C写入函数，可实现自动传送。

### 方法

#### image.width()

返回以像素计的图像的宽度。

#### image.height()

返回以像素计的图像的高度。

#### image.format()

返回用于灰度图的 sensor.GRAYSCALE 、用于RGB图像的 sensor.RGB565 和用于JPEG图像的 sensor.JPEG 。

#### image.size()

返回以字节计的图像大小。

#### image.get_pixel(x, y[, rgbtuple])

灰度图：返回(x, y)位置的灰度像素值。

RGB565l：返回(x, y)位置的RGB888像素元组(r, g, b)。

Bayer图像: 返回(x, y)位置的像素值。

不支持压缩图像。

> image.get_pixel() 和 `image.set_pixel()`是允许你操作Bayer模式图像的唯一方法。 Bayer模式图像是文字图像。对于偶数行，其中图像中的像素是R/G/R/G/等。 对于奇数行，其中图像中的像素是G/B/G/B/等。 每个像素是8位。

#### image.set_pixel(x, y, pixel)
灰度图：将(x, y) 位置的像素设置为灰度值 pixel 。

RGB图像：将(x, y) 位置的像素设置为RGB888元组(r, g, b) pixel 。

不支持压缩图像。

> image.get_pixel() 和 `image.set_pixel()`是允许你操作Bayer模式图像的唯一方法。 Bayer模式图像是文字图像。对于偶数行，其中图像中的像素是R/G/R/G/等。 对于奇数行，其中图像中的像素是G/B/G/B/等。 每个像素是8位。

#### image.mean_pool(x_div, y_div)

在图像中找到 x_div * y_div 正方形的平均值，并返回由每个正方形的平均值组成的修改图像。

此方法允许您在原来图像上快速缩小图像。

不支持压缩图像和bayer图像。

#### image.mean_pooled(x_div, y_div)

在图像中找到 x_div * y_div 正方形的平均值，并返回由每个正方形的平均值组成的新图像。

此方法允许您创建缩小的图像副本。

不支持压缩图像和bayer图像。

#### image.midpoint_pool(x_div, y_div[, bias=0.5])

在图像中找到 x_div * y_div 正方形的中点值，并返回由每个正方形的中点值组成的修改图像。

bias 为0.0返回每个区域的最小值，而``bias`` 为1.0返回每个区域的最大值。

此方法允许您在原来图像上快速缩小图像。

不支持压缩图像和bayer图像。

#### image.midpoint_pooled(x_div, y_div[, bias=0.5])

在图像中找到 x_div * y_div 正方形的中点值，并返回由每个正方形的中点值组成的新图像。

bias 为0.0返回每个区域的最小值，而``bias`` 为1.0返回每个区域的最大值。

此方法允许您创建缩小的图像副本。

不支持压缩图像和bayer图像。

#### image.to_grayscale([copy=False])

将图像转换为灰度图像。 此方法也会修改基础图像像素，以字节为单位更改图像大小，因此只能在灰度图像或RGB565图像上进行。 否则 copy 必须为True才能在堆上创建新的修改图像。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.to_rgb565([copy=False])

将图像转换为彩色图像。 此方法也会修改基础图像像素，以字节为单位更改图像大小，因此只能在RGB565图像上进行。 否则 copy 必须为True才能在堆上创建新的修改图像。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.to_rainbow([copy=False])

将图像转换为彩虹图像。 此方法也会修改基础图像像素，以字节为单位更改图像大小，因此只能在RGB565图像上进行。 否则 copy 必须为True才能在堆上创建新的修改图像。

彩虹图像是彩色图像，对于图像中的每个8位掩模灰度照明值具有唯一的颜色值。 例如，它为热图像提供热图颜色。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.compress([quality=50])

JPEG对图像进行适当压缩。使用这种方法与 compressed 保存堆空间相比，使用更高quality的压缩率是以破坏原始图像为代价的。

quality 是压缩质量（0-100）（int）。

#### image.compress_for_ide([quality=50])

JPEG对图像进行适当压缩。使用这种方法与 compressed 保存堆空间相比，使用更高quality的压缩率是以破坏原始图像为代价的。

这个方法压缩图像，然后通过将每6比特编码为128 - 191之间的字节将JPEG数据格式化，转换为OpenMV IDE，以便显示。进行这一步是为防止JPEG数据被误认为是字节流中的其他文本数据。

您需要使用这一方法来格式化图像数据，以便在OpenMV IDE中通过“开放终端”创建的终端窗口中显示。

quality 是压缩质量（0-100）（int）。

#### image.compressed([quality=50])

返回一个JPEG压缩图像—原始图像未经处理。但是，这个方法需要堆空间的大分配，所以图像压缩质量和图像分辨率必须很低。

quality 是压缩质量（0-100）（int）。

#### image.compressed_for_ide([quality=50])

返回一个JPEG压缩图像—原始图像未经处理。但是，这个方法需要堆空间的大分配，所以图像压缩质量和图像分辨率必须很低。

这个方法压缩图像，然后通过将每6比特编码为128 - 191之间的字节将JPEG数据格式化，转换为OpenMV IDE，以便显示。进行这一步是为防止JPEG数据被误认为是字节流中的其他文本数据。

您需要使用这一方法来格式化图像数据，以便在OpenMV IDE中通过“开放终端”创建的终端窗口中显示。

quality 是压缩质量（0-100）（int）。

#### image.copy([roi[, copy_to_fb=False]])

创建一个图像对象的副本。

Roi 是一个用以复制的矩形的感兴趣区域(x, y, w, h)。如果未指定，ROI即复制整个图像的图像矩形。但这不适用于JPEG图像。

请记住图像副本储存在MicroPython 堆中而不是帧缓冲区。同样，您需要将图像副本大小控制在8KB以下（OpenMV）或16KB以下（OpenMV Cam M7） 如果您想使用一个复制操作来使用所有的堆空间，这个函数会出现异常。过大的图像极易触发异常。

如果 copy_to_fb 为True，则该方法将帧缓冲替换为图像。 帧缓冲区具有比堆大得多的空间，并且可以容纳大图像。

#### image.save(path[, roi[, quality=50]])

将图像的副本保存到 path 中的文件系统。

支持bmp/pgm/ppm/jpg/jpeg格式的图像文件。注意：您无法将jpeg格式的压缩图像保存成未压缩的格式。

roi 是一个用以复制的矩形的感兴趣区域(x, y, w, h)。如果未指定，ROI即复制整个图像的图像矩形。但这不适用于JPEG图像。

quality 指在图像尚未被压缩时将图像保存为JPEG格式的JPEG压缩质量。

#### image.clear()

将图像中的所有像素设置为零（非常快）。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像。

#### image.draw_line(x0, y0, x1, y1[, color[, thickness=1]])

在图像上绘制一条从(x0，y0)到(x1，y1)的线。 您可以单独传递x0，y0，x1，y1，也可以传递给元组(x0，y0，x1，y1)。

color 是用于灰度或RGB565图像的RGB888元组。默认为白色。但是，您也可以传递灰度图像的基础像素值(0-255)或RGB565图像的字节反转RGB565值。

thickness 控制线的粗细像素。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.draw_rectangle(x, y, w, h[, color[, thickness=1[, fill=False]]])

在图像上绘制一个矩形。 您可以单独传递x，y，w，h或作为元组(x，y，w，h)传递。

color 是用于灰度或RGB565图像的RGB888元组。默认为白色。但是，您也可以传递灰度图像的基础像素值(0-255)或RGB565图像的字节反转RGB565值。

thickness 控制线的粗细像素。

将 fill 设置为True以填充矩形。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.draw_ellipse(cx, cy, rx, ry, rotation[, color[, thickness=1[, fill=False]]])

在图像上绘制椭圆。您可以单独传递cx、cy、rx、ry和rotation(以度为单位)，也可以作为元组传递(cx、yc、rx、ry、rotation)。

color 是用于灰度或RGB565图像的RGB888元组。默认为白色。 但是，您也可以为灰度图像传递基础像素值(0-255)，或者为RGB565图像传递字节反转的RGB565值。

thickness 控制边缘的厚度，以像素为单位。

传递 fill 设置为True来填充椭圆。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像或bayer图像。

#### image.draw_circle(x, y, radius[, color[, thickness=1[, fill=False]]])

在图像上绘制一个圆形。 您可以单独传递x，y，半径 或 作为元组(x，y，radius)传递。

color 是用于灰度或RGB565图像的RGB888元组。默认为白色。但是，您也可以传递灰度图像的基础像素值(0-255)或RGB565图像的字节反转RGB565值。

thickness 控制线的粗细像素。

将 fill 设置为True以填充圆形。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.draw_string(x, y, text[, color[, scale=1[, x_spacing=0[, y_spacing=0[, mono_space=True]]]]])

从图像中的(x, y)位置开始绘制8x10文本。您可以单独传递x，y，也可以作为元组(x，y)传递。

text 是写入图像的字符串。 \n, \r, 和 \r\n 结束符将光标移至下一行。

color 是用于灰度或RGB565图像的RGB888元组。默认为白色。但是，您也可以传递灰度图像的基础像素值(0-255)或RGB565图像的字节反转RGB565值。

可以增加 scale 以增加图像上文本的大小。

   仅整数值（例如，1/2/3 /等）。

x_spacing 允许你在字符之间添加（如果是正数）或减去（如果是负数）x像素，设置字符间距。

y_spacing 允许你在字符之间添加（如果是正数）或减去（如果是负数）y像素，设置行间距。

mono_space 默认为True，强制文本间距固定。对于大文本，这看起来很糟糕。设置False以获得非固定宽度的字符间距，看起来好多了。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.draw_cross(x, y[, color[, size=5[, thickness=1]]])

在图像上绘制一个十字。 您可以单独传递x，y或作为元组(x，y)传递。

color 是用于灰度或RGB565图像的RGB888元组。默认为白色。但是，您也可以传递灰度图像的基础像素值(0-255)或RGB565图像的字节反转RGB565值。

size 控制十字线的延伸长度。

thickness 控制边缘的像素厚度。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.draw_arrow(x0, y0, x1, y1[, color[, thickness=1]])

在图像上绘制一条从(x0，y0)到(x1，y1)的箭头。 您可以单独传递x0，y0，x1，y1，也可以传递给元组(x0，y0，x1，y1)。

color 是用于灰度或RGB565图像的RGB888元组。默认为白色。但是，您也可以传递灰度图像的基础像素值(0-255)或RGB565图像的字节反转RGB565值。

thickness 控制线的粗细像素。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.draw_image(image, x, y[, x_scale=1.0[, y_scale=1.0[, mask=None[, alpha=256]]]])

绘制一个 image ，其左上角从位置x，y开始。 您可以单独传递x，y，也可以传递给元组(x，y)。

x_scale 控制图像在x方向(浮点数)缩放的程度。

y_scale 控制图像在y方向(浮点数)缩放的程度。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 您可以使用mask掩码进行绘制操作。

alpha 控制源图像绘制到目标图像中的透明度。256 为绘制不透明的源图像，而小于 256 的值产生源图像和目标图像之间的混合。0 表示不修改目标图像。

不支持压缩图像和bayer图像。

#### image.draw_keypoints(keypoints[, color[, size=10[, thickness=1[, fill=False]]]])

在图像上画出一个特征点对象的各个点。

color 是用于灰度或RGB565图像的RGB888元组。默认为白色。但是，您也可以传递灰度图像的基础像素值(0-255)或RGB565图像的字节反转RGB565值。

size 控制特征点的大小。

thickness 控制线的粗细像素。

将 fill 设置为True以填充特征点。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.flood_fill(x, y[, seed_threshold=0.05[, floating_threshold=0.05[, color[, invert=False[, clear_background=False[, mask=None]]]]]])

从位置x，y开始填充图像的区域。 您可以单独传递x，y，也可以传递给元组(x，y)。

seed_threshold 控制填充区域中的像素与原始起始像素的差异。

floating_threshold 控制填充区域中的像素与任何相邻像素的差异。

color 是用于灰度或RGB565图像的RGB888元组。默认为白色。但是，您也可以传递灰度图像的基础像素值(0-255)或RGB565图像的字节反转RGB565值。

将 invert 传递为True，以重新填充flood_fill连接区域外的所有内容。

将 clear_background 传递为True，将其余的flood_fill没有重新着色的像素归零。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩膜中设置的像素会在flood_fill时被评估。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

此方法在OpenMV Cam M4 上不可用。

#### image.binary(thresholds[, invert=False[, zero=False[, mask=None]]])

根据像素是否在阈值列表 thresholds 中的阈值内，将图像中的所有像素设置为黑色或白色。

thresholds 必须是元组列表。 [(lo, hi), (lo, hi), ..., (lo, hi)] 定义你想追踪的颜色范围。 对于灰度图像，每个元组需要包含两个值 - 最小灰度值和最大灰度值。 仅考虑落在这些阈值之间的像素区域。 对于RGB565图像，每个元组需要有六个值(l_lo，l_hi，a_lo，a_hi，b_lo，b_hi) - 分别是LAB L，A和B通道的最小值和最大值。 为方便使用，此功能将自动修复交换的最小值和最大值。 此外，如果元组大于六个值，则忽略其余值。相反，如果元组太短，则假定其余阈值处于最大范围。

注解

获取所跟踪对象的阈值，只需在 IDE 帧缓冲区中选择（单击并拖动）跟踪对象。 直方图会相应地更新到所在区域。然后只需写下颜色分布在每个直方图通道中起始与下降位置。 这些将是 thresholds 的低值和高值。 由于上下四分位数据相差微小，故手动确定阈值为佳。

您还可以通过进入OpenMV IDE中的 工具 ->机器视觉 ->阈值编辑器 并从GUI窗口中拖动滑块来确定颜色阈值。

invert 反转阈值操作，像素在已知颜色范围之外进行匹配，而非在已知颜色范围内。

设置 zero 为True来使阈值像素为零，并使不在阈值列表中的像素保持不变。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。


#### image.invert()

将二进制图像0（黑色）变为1（白色），1（白色）变为0（黑色），非常快速地翻转二进制图像中的所有像素值。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和Bayer图像。

#### image.b_and(image[, mask=None])

用另一图像与这一图像进行逻辑与运算。

image 可以是图像对象，未压缩图像文件的路径(bmp/pgm/ppm)，也可以是标量值。 如果标量值，该值可以是RGB888元组或基础像素值(例如，灰度图像的8位灰度级或RGB图像的字节反转RGB565值)。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.b_nand(image[, mask=None])

用另一图像与这一图像进行逻辑与非运算。

image 可以是图像对象，未压缩图像文件的路径(bmp/pgm/ppm)，也可以是标量值。 如果标量值，该值可以是RGB888元组或基础像素值(例如，灰度图像的8位灰度级或RGB图像的字节反转RGB565值)。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.b_or(image[, mask=None])

用另一图像与这一图像进行逻辑或运算。

image 可以是图像对象，未压缩图像文件的路径(bmp/pgm/ppm)，也可以是标量值。 如果标量值，该值可以是RGB888元组或基础像素值(例如，灰度图像的8位灰度级或RGB图像的字节反转RGB565值)。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.b_nor(image[, mask=None])

用另一图像与这一图像进行逻辑或非运算。

image 可以是图像对象，未压缩图像文件的路径(bmp/pgm/ppm)，也可以是标量值。 如果标量值，该值可以是RGB888元组或基础像素值(例如，灰度图像的8位灰度级或RGB图像的字节反转RGB565值)。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.b_xor(image[, mask=None])

用另一图像与这一图像进行逻辑异或运算。

image 可以是图像对象，未压缩图像文件的路径(bmp/pgm/ppm)，也可以是标量值。 如果标量值，该值可以是RGB888元组或基础像素值(例如，灰度图像的8位灰度级或RGB图像的字节反转RGB565值)。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.b_xnor(image[, mask=None])

用另一图像与这一图像进行逻辑同或运算。

image 可以是图像对象，未压缩图像文件的路径(bmp/pgm/ppm)，也可以是标量值。 如果标量值，该值可以是RGB888元组或基础像素值(例如，灰度图像的8位灰度级或RGB图像的字节反转RGB565值)。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.erode(size[, threshold[, mask=None]])

从分割区域的边缘删除像素。

这一方法通过卷积图像上((size*2)+1)x((size*2)+1)像素的核来实现，如果相邻像素集的总和小于 threshold ，则对内核的中心像素进行归零。

若 threshold 未设定，这个方法的功能如标准腐蚀方法一样。若threshold设定，您就可以指定腐蚀的特定像素，例如：设置低于2个的像素周围阈值为2。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.dilate(size[, threshold[, mask=None]])

将像素添加到分割区域的边缘中。

这一方法通过卷积图像上((size*2)+1)x((size*2)+1)像素的核来实现，如果相邻像素集的总和大于 threshold ，则将内核的中心像素进行设置。

若 threshold 未设定，这个方法的功能如标准腐蚀方法一样。若threshold设定，您就可以指定腐蚀的特定像素，例如：设置低于2个的像素周围阈值为2。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.open(size[, threshold[, mask=None]])

按顺序对图像执行腐蚀和膨胀。有关更多信息，请参阅 image.erode() 和 image.dilate() 。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.close(size[, threshold[, mask=None]])

按顺序对图像执行膨胀和腐蚀。有关更多信息，请参阅 image.erode() 和 image.dilate() 。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.top_hat(size[, threshold[, mask=None]])

返回原图像和执行 image.open() 函数后图像的差异。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

不支持压缩图像和bayer图像。

#### image.black_hat(size[, threshold[, mask=None]])

返回原图像和执行 image.close() 函数后图像的差异。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

不支持压缩图像和bayer图像。

#### image.negate()

非常快速地翻转（数字反转）图像中的所有像素值。对每个颜色通道的像素值进行数值转换。例： (255 - pixel).

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.replace(image[, hmirror=False[, vflip=False[, mask=None]]])

image 可以是图像对象，未压缩图像文件的路径(bmp/pgm/ppm)，也可以是标量值。 如果标量值，该值可以是RGB888元组或基础像素值(例如，灰度图像的8位灰度级或RGB图像的字节反转RGB565值)。

将 hmirror 设置为True以水平镜像替换图像。

将 vflip 设置为True以垂直翻转替换图像。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.add(image[, mask=None])

将两个图像彼此按像素相加。

image 可以是图像对象，未压缩图像文件的路径(bmp/pgm/ppm)，也可以是标量值。 如果标量值，该值可以是RGB888元组或基础像素值(例如，灰度图像的8位灰度级或RGB图像的字节反转RGB565值)。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.sub(image[, reverse=False[, mask=None]])

将两个图像彼此按像素相减。

image 可以是图像对象，未压缩图像文件的路径(bmp/pgm/ppm)，也可以是标量值。 如果标量值，该值可以是RGB888元组或基础像素值(例如，灰度图像的8位灰度级或RGB图像的字节反转RGB565值)。

将 reverse 设置为True可以将减法操作从 this_image-image 反转为 image-this_image 。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.mul(image[, invert=False[, mask=None]])

将两个图像彼此按像素相乘。

image 可以是图像对象，未压缩图像文件的路径(bmp/pgm/ppm)，也可以是标量值。 如果标量值，该值可以是RGB888元组或基础像素值(例如，灰度图像的8位灰度级或RGB图像的字节反转RGB565值)。

将 invert 设置为True可将乘法运算从 a*b 改为 1/((1/a)*(1/b))。 特别是，这使图像变亮而不是使图像变暗(例如，乘法与刻录操作)。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.div(image[, invert=False[, mask=None]])

将此图像除以另一个图像。

image 可以是图像对象，未压缩图像文件的路径(bmp/pgm/ppm)，也可以是标量值。 如果标量值，该值可以是RGB888元组或基础像素值(例如，灰度图像的8位灰度级或RGB图像的字节反转RGB565值)。

将 invert 设置为True可将除法方向从 a/b 改为 b/a。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.min(image[, mask=None])

在像素级 用此图像和另一个图像之间的最小像素值替换此图像中的像素。

image 可以是图像对象，未压缩图像文件的路径(bmp/pgm/ppm)，也可以是标量值。 如果标量值，该值可以是RGB888元组或基础像素值(例如，灰度图像的8位灰度级或RGB图像的字节反转RGB565值)。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

这个方法在OpenMV4上不可用.

#### image.max(image[, mask=None])

在像素级 用此图像和另一个图像之间的最大像素值替换此图像中的像素。

image 可以是图像对象，未压缩图像文件的路径(bmp/pgm/ppm)，也可以是标量值。 如果标量值，该值可以是RGB888元组或基础像素值(例如，灰度图像的8位灰度级或RGB图像的字节反转RGB565值)。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.difference(image[, mask=None])

将两个图像彼此按像素取绝对值。例：对于每个颜色通道而言，将每个像素��换为ABS(this.pixel-image.pixel)。

image 可以是图像对象，未压缩图像文件的路径(bmp/pgm/ppm)，也可以是标量值。 如果标量值，该值可以是RGB888元组或基础像素值(例如，灰度图像的8位灰度级或RGB图像的字节反转RGB565值)。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.blend(image[, alpha=128[, mask=None]])

将另外一张图像 image 与这一图像融合。

image 可以是图像对象，未压缩图像文件的路径(bmp/pgm/ppm)，也可以是标量值。 如果标量值，该值可以是RGB888元组或基础像素值(例如，灰度图像的8位灰度级或RGB图像的字节反转RGB565值)。

alpha 控制要混合到这个图像中的其他图像的多少. alpha 应该是0到256之间的整数值。接近零的值会将更多其他图像混合到此图像中，接近256则相反。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.histeq([adaptive=False[, clip_limit=-1[, mask=None]]])

在图像上运行直方图均衡算法。 直方图均衡化使图像中的对比度和亮度标准化。

如果 adaptive 传递为True，那么将在图像上运行自适应直方图均衡方法，这通常比非自适应直方图限定更好，但运行时间更长。

clip_limit 提供了一种限制自适应直方图均衡的对比度的方法。 使用较小的值(例如10)可以生成良好的直方图均衡对比度受限图像。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.mean(size, [threshold=False, [offset=0, [invert=False, [mask=None]]]]])

使用盒式滤波器的标准均值模糊滤波。

Size 是内核的大小。取1 (3x3 内核)、2 (5x5 内核)或更高值。

如果你想在滤波器的输出上自适应地设置阈值，你可以传递 threshold=True 参数来启动图像的自适应阈值处理， 他根据环境像素的亮度（核函数周围的像素的亮度有关），将像素设置为1或者0。 负数 offset 值将更多像素设置为1，而正值仅将最强对比度设置为1。 设置 invert 以反转二进制图像的结果输出。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

median(size, percentile=0.5, threshold=False, offset=0, invert=False, mask])
在图像上运行中值滤波。在保留边缘的条件下，中值滤波是用来平滑表面的最佳滤波，但是运行速度极慢。

Size 是内核的大小。取1 (3x3 内核)、2 (5x5 内核)或更高值。

percentile 控制内核中所使用值的百分位数。默认情况下，每个像素都使用相邻的第五十个百分位数（中心）替换。使用最小滤波时，您可将此值设置为0，使用下四分位数滤波时设置为0.25，使用上四分位数滤波时设置为0.75，使用最大滤波时设置为1。

如果你想在滤波器的输出上自适应地设置阈值，你可以传递 threshold=True 参数来启动图像的自适应阈值处理， 他根据环境像素的亮度（核函数周围的像素的亮度有关），将像素设置为1或者0。 负数 offset 值将更多像素设置为1，而正值仅将最强对比度设置为1。 设置 invert 以反转二进制图像的结果输出。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

此方法在OpenMV Cam M4 上不可用。

#### image.mode(size[, threshold=False, offset=0, invert=False, mask])

在图像上运行众数滤波，用相邻像素的模式替换每个像素。这一方法在灰度图上运行效果良好。但由于这一操作的非线性特性，会在RGB图像边缘上产生许多伪像。

Size 是内核的大小。取1 (3x3 内核)、2 (5x5 内核)。

如果你想在滤波器的输出上自适应地设置阈值，你可以传递 threshold=True 参数来启动图像的自适应阈值处理， 他根据环境像素的亮度（核函数周围的像素的亮度有关），将像素设置为1或者0。 负数 offset 值将更多像素设置为1，而正值仅将最强对比度设置为1。 设置 invert 以反转二进制图像的结果输出。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

此方法在OpenMV Cam M4 上不可用。

#### image.midpoint(size[, bias=0.5, threshold=False, offset=0, invert=False, mask])

在图像上运行中点滤波。此滤波器找到图像中每个像素邻域的中点((max-min)/2)。

size 是内核的大小。取1 (3x3 内核)、2 (5x5 内核)或更高值。

bias 控制图像混合的最小/最大程度。0只适用于最小滤波，1仅用于最大滤波。您可以通过 bias 对图像进行最小/最大化过滤。

如果你想在滤波器的输出上自适应地设置阈值，你可以传递 threshold=True 参数来启动图像的自适应阈值处理， 他根据环境像素的亮度（核函数周围的像素的亮度有关），将像素设置为1或者0。 负数 offset 值将更多像素设置为1，而正值仅将最强对比度设置为1。 设置 invert 以反转二进制图像的结果输出。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

此方法在OpenMV Cam M4 上不可用。

#### image.morph(size, kernel, mul=Auto, add=0)

通过过滤器内核对图像进行卷积。这允许您对图像执行通用卷积。

size 将内核的大小控制为((size*2)+1)x((size*2)+1)像素。

kernel 用来卷积图像的内核，可为一个元组或一个取值[-128:127]的列表。

mul 是用以与卷积像素结果相乘的数字。若不设置，则默认一个值，该值将防止卷积输出中的缩放。

add 是用来与每个像素卷积结果相加的数值。

mul 可进行全局对比度调整，add可进行全局亮度调整。

如果你想在滤波器的输出上自适应地设置阈值，你可以传递 threshold=True 参数来启动图像的自适应阈值处理， 他根据环境像素的亮度（核函数周围的像素的亮度有关），将像素设置为1或者0。 负数 offset 值将更多像素设置为1，而正值仅将最强对比度设置为1。 设置 invert 以反转二进制图像的结果输出。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

#### image.gaussian(size[, unsharp=False[, mul[, add=0[, threshold=False[, offset=0[, invert=False[, mask=None]]]]]]])

通过平滑高斯核对图像进行卷积。

size 是内核的大小。取1 (3x3 内核)、2 (5x5 内核)或更高值。

如果 unsharp 设置为True，那么这种方法不会仅进行高斯滤波操作，而是执行非锐化掩模操作，从而提高边缘的图像清晰度。

mul 是用以与卷积像素结果相乘的数字。若不设置，则默认一个值，该值将防止卷积输出中的缩放。

add 是用来与每个像素卷积结果相加的数值。

mul 可进行全局对比度调整，add可进行全局亮度调整。

如果你想在滤波器的输出上自适应地设置阈值，你可以传递 threshold=True 参数来启动图像的自适应阈值处理， 他根据环境像素的亮度（核函数周围的像素的亮度有关），将像素设置为1或者0。 负数 offset 值将更多像素设置为1，而正值仅将最强对比度设置为1。 设置 invert 以反转二进制图像的结果输出。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

此方法在OpenMV Cam M4 上不可用。

#### image.laplacian(size[, sharpen=False[, mul[, add=0[, threshold=False[, offset=0[, invert=False[, mask=None]]]]]]])

通过边缘检测拉普拉斯核来对图像进行卷积。

size 是内核的大小。取1 (3x3 内核)、2 (5x5 内核)或更高值。

如果 sharpen 被设置为True，那么这种方法将改为锐化图像，而不是仅输出未经过阈值处理的边缘检测图像。 增加内核大小然后增加图像清晰度。

mul 是用以与卷积像素结果相乘的数字。若不设置，则默认一个值，该值将防止卷积输出中的缩放。

add 是用来与每个像素卷积结果相加的数值。

mul 可进行全局对比度调整，add可进行全局亮度调整。

如果你想在滤波器的输出上自适应地设置阈值，你可以传递 threshold=True 参数来启动图像的自适应阈值处理， 他根据环境像素的亮度（核函数周围的像素的亮度有关），将像素设置为1或者0。 负数 offset 值将更多像素设置为1，而正值仅将最强对比度设置为1。 设置 invert 以反转二进制图像的结果输出。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

此方法在OpenMV Cam M4 上不可用。

#### image.bilateral(size[, color_sigma=0.1[, space_sigma=1[, threshold=False[, offset=0[, invert=False[, mask=None]]]]]])

通过双边滤波器对图像进行卷积。 双边滤波器使图像平滑，同时保持图像中的边缘。

size 是内核的大小。取1 (3x3 内核)、2 (5x5 内核)或更高值。

color_sigma 控制使用双边滤波器匹配颜色的接近程度。增加此值可增加颜色模糊。

space_sigma 控制像素在空间方面相互模糊的程度。增加此值可增加像素模糊。

如果你想在滤波器的输出上自适应地设置阈值，你可以传递 threshold=True 参数来启动图像的自适应阈值处理， 他根据环境像素的亮度（核函数周围的像素的亮度有关），将像素设置为1或者0。 负数 offset 值将更多像素设置为1，而正值仅将最强对比度设置为1。 设置 invert 以反转二进制图像的结果输出。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

此方法在OpenMV Cam M4 上不可用。

#### image.cartoon(size[, seed_threshold=0.05[, floating_threshold=0.05[, mask=None]]])

漫游图像并使用flood-fills算法填充图像中的所有像素区域。 这通过使图像的所有区域中的颜色变平来有效地从图像中去除纹理。 为了获得最佳效果，图像应具有大量对比度，以使区域不会太容易相互渗透。

seed_threshold 控制填充区域中的像素与原始起始像素的差异。

floating_threshold 控制填充区域中的像素与任何相邻像素的差异。

mask 是另一个用作绘图操作的像素级掩码的图像。掩码应该是一个只有黑色或白色像素的图像，并且应该与你正在绘制的 image 大小相同。 仅掩码中设置的像素被修改。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

此方法在OpenMV Cam M4 上不可用。

#### image.remove_shadows([image])

从该图像中移除阴影。

如果当前图像没有“无阴影”版本出现，则此方法将尝试从图像中去除阴影，但没有真实无阴影的图像依据。 这种算法适用于去除平坦均匀背景中的阴影。 请注意，此方法需要多秒才能运行，并且仅适用于实时移除阴影，动态生成无阴影版本的图像。 该算法的未来版本将适用于更多的环境，但同样缓慢。

如果当前图像有“无阴影”版本出现，则此方法将使用“真实源”背景无阴影图像去除图像中的所有阴影以滤除阴影。 非阴影像素不会被过滤掉，因此您可以向场景中添加以前不存在的新对象，并且这些对象中的任何非阴影像素都将显示出来。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

只支持RGB565图像。

此方法在OpenMV Cam M4 上不可用。

#### image.chrominvar()

从图像中删除照明效果，仅留下颜色渐变。比 image.illuminvar() 更快但受阴影影响。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

仅支持RGB565图像。

此方法在OpenMV Cam M4 上不可用。

#### image.illuminvar()

从图像中删除照明效果，仅留下颜色渐变。比 image.chrominvar() 慢但不受阴影影响。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

仅支持RGB565图像。

此方法在OpenMV Cam M4 上不可用。

#### image.linpolar([reverse=False])

图像从笛卡尔坐标到线性极坐标重新投影。

设置 reverse = True 可以在相反的方向重新投影。

线性极坐标重新投影将图像旋转转换为x平移。

不支持压缩图像。

此方法在OpenMV Cam M4 上不可用。

#### image.logpolar([reverse=False])

图像从笛卡尔坐标到对数极坐标重新投影。

设置 reverse = True 可以在相反的方向重新投影。

对数极坐标重新投影将图像的旋转转换为x平移和缩放到y平移。

不支持压缩图像。

此方法在OpenMV Cam M4 上不可用。

#### image.lens_corr([strength=1.8[, zoom=1.0]])

进行镜头畸变校正，以去除镜头造成的图像鱼眼效果。

strength 是一个浮点数，该值确定了对图像进行去鱼眼效果的程度。在默认情况下，首先试用取值1.8，然后调整这一数值使图像显示最佳效果。

zoom 是在对图像进行缩放的数值。默认值为 1.0 。

返回图像对象，以便您可以使用 . 表示法调用另一个方法。

不支持压缩图像和bayer图像。

 #### img.rotation_corr([x_rotation=0.0[, y_rotation=0.0[, z_rotation=0.0[, x_translation=0.0[, y_translation=0.0[, zoom=1.0[, fov=60.0[, corners]]]]]]]])

通过对帧缓冲区进行3D旋转来纠正图像中的透视问题。

`x_rotation` 是图像在帧缓冲区中绕x轴旋转的角度数(也就是图像上下旋转)。

`y_rotation` 是指图像在帧缓冲区中绕y轴旋转的角度数(即左右旋转图像)。

`z_rotation` 是图像在帧缓冲区中绕z轴旋转的角度数(即图像旋转到适当位置)。

`x_translation` 是图像旋转后向左或向右移动的单位数。因为这种转换应用于3D空间，所以单位不是像素……

`y_translation` 是图像在旋转后向上或向下移动的单位数。因为这种转换应用于3D空间，所以单位不是像素……

`zoom` 是将图像缩放的倍数，默认情况下为1.0。

`fov` 是在进行2D->3D投影时在3D空间旋转图像之前内部使用的视场。当这个值接近0时，图像被放置在距离视口无限远的地方。当这个值接近180时，图像被放置在视口中。通常，你不应该改变这个值，但你可以修改它来改变2D->3D映射效果。

`corners` 是一个拥有四个(x, y) tuples 的 list，代表四个 `corner` 用来创建四点对应单应性,将第一个 `corner` 映射到(0,0),第二个 `corner` (image_width-1, 0),第三个 `corner` (image_width-1 image_height-1)和第四个 `corner` (0,image_height-1)。然后在图像被重新映射后应用3D旋转。这个参数允许你使用 rotation_corr 来做一些事情，比如鸟瞰图转换。例如:

```python
top_tilt = 10 # if the difference between top/bottom_tilt become to large this method will stop working
bottom_tilt = 0

points = [(tilt, 0), (img.width()-tilt, 0), (img.width()-1-bottom_tilt, img.height()-1), (bottom_tilt, img.height()-1)]

img.rotation_corr(corners=points)
```

返回图像对象，以便您可以使用 `.` 调用另一个方法。

不支持压缩图像或拜耳图像。

#### image.get_similarity(image)

返回一个“相似度”对象，描述两幅图像使用SSIM算法来比较两幅图像之间的8x8像素色块的相似度。

image 可以是图像对象，未压缩图像文件的路径(bmp/pgm/ppm)，也可以是标量值。 如果标量值，该值可以是RGB888元组或基础像素值(例如，灰度图像的8位灰度级或RGB图像的字节反转RGB565值)。

不支持压缩图像和bayer图像。

此方法在OpenMV Cam M4 上不可用。

#### image.get_histogram([thresholds[, invert=False[, roi[, bins[, l_bins[, a_bins[, b_bins]]]]]]])

在 roi 的所有颜色通道上进行标准化直方图运算，并返回 histogram 对象。 请参考 histogram 对象以获取更多信息。您也可以使用 image.get_hist 或 image.histogram 来调用这一方法。如果传递 thresholds 列表，则直方图信息将仅从阈值列表中的像素计算得出。

thresholds 必须是元组列表。 [(lo, hi), (lo, hi), ..., (lo, hi)] 定义你想追踪的颜色范围。 对于灰度图像，每个元组需要包含两个值 - 最小灰度值和最大灰度值。 仅考虑落在这些阈值之间的像素区域。 对于RGB565图像，每个元组需要有六个值(l_lo，l_hi，a_lo，a_hi，b_lo，b_hi) - 分别是LAB L，A和B通道的最小值和最大值。 为方便使用，此功能将自动修复交换的最小值和最大值。 此外，如果元组大于六个值，则忽略其余值。相反，如果元组太短，则假定其余阈值处于最大范围。

注解

获取所跟踪对象的阈值，只需在IDE帧缓冲区中选择（单击并拖动）跟踪对象。 直方图会相应地更新到所在区域。然后只需写下颜色分布在每个直方图通道中起始与下降位置。 这些将是 thresholds 的低值和高值。 由于上下四分位数据相差微小，故手动确定阈值为佳。

您还可以通过进入OpenMV IDE中的 工具 ->机器视觉 ->阈值编辑器 并从GUI窗口中拖动滑块来确定颜色阈值。

invert 反转阈值操作，像素在已知颜色范围之外进行匹配，而非在已知颜色范围内。

除非您需要使用颜色统计信息进行高级操作，否则只需使用`image.get_statistics()` 方法代替此方法查看图像中的像素区域。

roi 是感兴趣区域的矩形元组(x，y，w，h)。如果未指定，ROI即整个图像的图像矩形。 操作范围仅限于 roi 区域内的像素。

bins 和其他bin是用于直方图通道的箱数。对于灰度图像，使用 bins ， 对于RGB565图像，使用其他每个通道。每个通道的bin计数必须大于2。 另外，将bin计数设置为大于每个通道的唯一像素值的数量是没有意义的。 默认情况下，直方图将具有每个通道的最大bin数。

不支持压缩图像和bayer图像。

#### image.get_statistics([thresholds[, invert=False[, roi[, bins[, l_bins[, a_bins[, b_bins]]]]]]])

计算 roi 中每个颜色通道的平均值、中值、众值、标准偏差、最小值、最大值、下四分值和上四分值，并返回一个数据对象。 请参见 statistics 对象以获取更多信息。您也可以使用 image.get_stats 或 image.statistics 来调用这一方法。 如果传递 thresholds 列表，则直方图信息将仅从阈值列表中的像素计算得出。

thresholds 必须是元组列表。 [(lo, hi), (lo, hi), ..., (lo, hi)] 定义你想追踪的颜色范围。 对于灰度图像，每个元组需要包含两个值 - 最小灰度值和最大灰度值。 仅考虑落在这些阈值之间的像素区域。 对于RGB565图像，每个元组需要有六个值(l_lo，l_hi，a_lo，a_hi，b_lo，b_hi) - 分别是LAB L，A和B通道的最小值和最大值。 为方便使用，此功能将自动修复交换的最小值和最大值。 此外，如果元组大于六个值，则忽略其余值。相反，如果元组太短，则假定其余阈值处于最大范围。

注解

获取所跟踪对象的阈值，只需在IDE帧缓冲区中选择（单击并拖动）跟踪对象。 直方图会相应地更新到所在区域。然后只需写下颜色分布在每个直方图通道中起始与下降位置。 这些将是 thresholds 的低值和高值。 由于上下四分位数据相差微小，故手动确定阈值为佳。

您还可以通过进入OpenMV IDE中的 工具 ->机器视觉 ->阈值编辑器 并从GUI窗口中拖动滑块来确定颜色阈值。

invert 反转阈值操作，像素在已知颜色范围之外进行匹配，而非在已知颜色范围内。

您可以在需要获取图像中一个像素区域信息时使用这一方法。例如：若您想用帧差法来检测运动时， 您需要使用这一方法来确定图像颜色通道的变化，从而触发运动检测阈值。

roi 是感兴趣区域的矩形元组(x，y，w，h)。如果未指定，ROI即整个图像的图像矩形。 操作范围仅限于 roi 区域内的像素。

bins 和其他bin是用于直方图通道的箱数。对于灰度图像，使用 bins ， 对于RGB565图像，使用其他每个通道。每个通道的bin计数必须大于2。 另外，将bin计数设置为大于每个通道的唯一像素值的数量是没有意义的。 默认情况下，直方图将具有每个通道的最大bin数。

不支持压缩图像和bayer图像。

#### image.get_regression(thresholds[, invert=False[, roi[, x_stride=2[, y_stride=1[, area_threshold=10[, pixels_threshold=10[, robust=False]]]]]]])

对图像所有阈值像素进行线性回归计算。这一计算通过最小二乘法进行，通常速度较快，但不能处理任何异常值。 若 robust 为True，则将使用泰尔指数。泰尔指数计算图像中所有阈值像素间的所有斜率的中值。 若在阈值转换后设定太多像素，即使在80x60的图像上，这一N^2操作也可能将您的FPS降到5以下。 但是，只要阈值转换后的进行设置的像素数量较少，即使在超过30%的阈值像素为异常值的情况下，线性回归也依然有效。

这一方法返回的是一个 image.line 对象。如何轻松运用直线对象， 详见下博文： https://openmv.io/blogs/news/linear-regression-line-following

thresholds 必须是元组列表。 [(lo, hi), (lo, hi), ..., (lo, hi)] 定义你想追踪的颜色范围。 对于灰度图像，每个元组需要包含两个值 - 最小灰度值和最大灰度值。 仅考虑落在这些阈值之间的像素区域。 对于RGB565图像，每个元组需要有六个值(l_lo，l_hi，a_lo，a_hi，b_lo，b_hi) - 分别是LAB L，A和B通道的最小值和最大值。 为方便使用，此功能将自动修复交换的最小值和最大值。 此外，如果元组大于六个值，则忽略其余值。相反，如果元组太短，则假定其余阈值处于最大范围。

> 获取所跟踪对象的阈值，只需在IDE帧缓冲区中选择（单击并拖动）跟踪对象。 直方图会相应地更新到所在区域。然后只需写下颜色分布在每个直方图通道中起始与下降位置。 这些将是 thresholds 的低值和高值。 由于上下四分位数据相差微小，故手动确定阈值为佳。

您还可以通过进入OpenMV IDE中的 工具 ->机器视觉 ->阈值编辑器 并从GUI窗口中拖动滑块来确定颜色阈值。

invert 反转阈值操作，像素在已知颜色范围之外进行匹配，而非在已知颜色范围内。

roi 是感兴趣区域的矩形元组(x，y，w，h)。如果未指定，ROI即整个图像的图像矩形。 操作范围仅限于 roi 区域内的像素。

x_stride 是调用函数时要跳过的x像素数。

y_stride 是调用函数时要跳过的y像素数。

如果回归后的边界框区域小于 area_threshold ，则返回None。

如果回归后的像素数小于 pixel_threshold ，则返回None。

不支持压缩图像和bayer图像。

#### image.find_blobs(thresholds[, invert=False[, roi[, x_stride=2[, y_stride=1[, area_threshold=10[, pixels_threshold=10[, merge=False[, margin=0[, threshold_cb=None[, merge_cb=None]]]]]]]]]])

查找图像中所有色块，并返回一个包括每个色块的色块对象的列表。请观察 image.blob 对象以获取更多信息。

thresholds 必须是元组列表。 [(lo, hi), (lo, hi), ..., (lo, hi)] 定义你想追踪的颜色范围。 对于灰度图像，每个元组需要包含两个值 - 最小灰度值和最大灰度值。 仅考虑落在这些阈值之间的像素区域。 对于RGB565图像，每个元组需要有六个值(l_lo，l_hi，a_lo，a_hi，b_lo，b_hi) - 分别是LAB L，A和B通道的最小值和最大值。 为方便使用，此功能将自动修复交换的最小值和最大值。 此外，如果元组大于六个值，则忽略其余值。相反，如果元组太短，则假定其余阈值处于最大范围。

注解

获取所跟踪对象的阈值，只需在IDE帧缓冲区中选择（单击并拖动）跟踪对象。 直方图会相应地更新到所在区域。然后只需写下颜色分布在每个直方图通道中起始与下降位置。 这些将是 thresholds 的低值和高值。 由于上下四分位数据相差微小，故手动确定阈值为佳。

您还可以通过进入OpenMV IDE中的 工具 ->机器视觉 ->阈值编辑器 并从GUI窗口中拖动滑块来确定颜色阈值。

invert 反转阈值操作，像素在已知颜色范围之外进行匹配，而非在已知颜色范围内。

roi 是感兴趣区域的矩形元组(x，y，w，h)。如果未指定，ROI即整个图像的图像矩形。 操作范围仅限于 roi 区域内的像素。

x_stride 是查找某色块时需要跳过的x像素的数量。找到色块后，直线填充算法将精确像素。 若已知色块较大，可增加 x_stride 来提高查找色块的速度。

y_stride 是查找某色块时需要跳过的y像素的数量。找到色块后，直线填充算法将精确像素。 若已知色块较大，可增加 y_stride 来提高查找色块的速度。

若一个色块的边界框区域小于 area_threshold ，则会被过滤掉。

若一个色块的像素数小于 pixel_threshold ，则会被过滤掉。

merge 若为True，则合并所有没有被过滤掉的色块，这些色块的边界矩形互相交错重叠。 margin 可在相交测试中用来增大或减小色块边界矩形的大小。例如：边缘为1、相互间边界矩形为1的色块将被合并。

合并色块使颜色代码追踪得以实现。每个色块对象有一个代码值 code ，该值为一个位向量。 例如：若您在 image.find_blobs 中输入两个颜色阈值，则第一个阈值代码为1，第二个代码为2（第三个代码为4，第四个代码为8，以此类推）。 合并色块对所有的code使用逻辑或运算，以便您知道产生它们的颜色。这使得您可以追踪两个颜色，若您用两种颜色得到一个色块对象，则可能是一种颜色代码。

若您使用严格的颜色范围，无法完全追踪目标对象的所有像素，您可能需要合并色块。

最后，若您想要合并色块，但不想两种不同阈值颜色的色块被合并，只需分别两次调用 image.find_blobs ，不同阈值色块就不会被合并。

threshold_cb 可设置为用以调用阈值筛选后的每个色块的函数，以便将其从将要合并的色块列表中过滤出来。 回调函数将收到一个参数：要被筛选的色块对象。然后回调函数需返回True以保留色块或返回False以过滤色块。

merge_cb 可设置为用以调用两个即将合并的色块的函数，以禁止或准许合并。回调函数将收到两个参数—两个将被合并的色块对象。 回调函数须返回True以合并色块，或返回False以防止色块合并。

不支持压缩图像和bayer图像。

#### image.find_lines([roi[, x_stride=2[, y_stride=1[, threshold=1000[, theta_margin=25[, rho_margin=25]]]]]])

使用霍夫变换查找图像中的所有直线。返回一个 image.line 对象的列表。

roi 是感兴趣区域的矩形元组(x，y，w，h)。如果未指定，ROI即整个图像的图像矩形。操作范围仅限于 roi 区域内的像素。

x_stride 是霍夫变换时需要跳过的x像素的数量。若已知直线较大，可增加 x_stride 。

y_stride 是霍夫变换时需要跳过的y像素的数量。若已知直线较大，可增加 y_stride 。

threshold 控制从霍夫变换中监测到的直线。只返回大于或等于 threshold 的直线。 应用程序的正确的 threshold 值取决于图像。注意：一条直线的大小(magnitude)是组成直线所有索贝尔滤波像素大小的总和。

theta_margin 控制所监测的直线的合并。 直线角度为 theta_margin 的部分和直线p值为 rho_margin 的部分合并。

rho_margin 控制所监测的直线的合并。 直线角度为 theta_margin 的部分和直线p值为 rho_margin 的部分合并。

该方法通过在图像上运行索贝尔滤波器，并利用该滤波器的幅值和梯度响应来进行霍夫变换。 无需对图像进行任何预处理。但是，清理图像过滤器可得到更为稳定的结果。

不支持压缩图像和bayer图像。

此方法在OpenMV Cam M4 上不可用。

#### image.find_line_segments([roi[, merge_distance=0[, max_theta_difference=15]]])

使用霍夫转换来查找图像中的线段。返回一个 image.line 对象的列表。

roi 是一个用以复制的矩形的感兴趣区域(x, y, w, h)。如果未指定， ROI 即图像矩形。操作范围仅限于roi区域内的像素。

merge_distance 指定两条线段之间的可以相互分开而不被合并的最大像素数。

max_theta_difference 是上面 merge_distancede 要合并的的两个线段的最大角度差值。

此方法使用LSD库（也被OpenCV使用）来查找图像中的线段。这有点慢，但是非常准确，线段不会跳跃。

不支持压缩图像和bayer图像。

此方法在OpenMV Cam M4 上不可用。

#### image.find_circles([roi[, x_stride=2[, y_stride=1[, threshold=2000[, x_margin=10[, y_margin=10[, r_margin=10]]]]]]])

使用霍夫变换在图像中查找圆。返回一个 image.circle 对象列表（见上）。

roi 是一个用以复制的矩形的感兴趣区域(x, y, w, h)。如果未指定， ROI 即图像矩形。操作范围仅限于roi区域内的像素。

x_stride 是霍夫变换时需要跳过的x像素的数量。若已知圆较大，可增加 x_stride 。

y_stride 是霍夫变换时需要跳过的y像素的数量。若已知圆较大，可增加 y_stride 。

threshold 控制从霍夫变换中监测到的圆。只返回大于或等于 threshold 的圆。 应用程序的正确的 threshold 值取决于图像。注意：一个圆的大小(magnitude)是组成圆所有索贝尔滤波像素大小的总和。

x_margin 控制所检测的圆的合并。 圆像素为 x_margin 、 y_margin 和 r_margin 的部分合并。

y_margin 控制所检测的圆的合并。 圆像素为 x_margin 、 y_margin 和 r_margin 的部分合并。

r_margin 控制所检测的圆的合并。 圆像素为 x_margin 、 y_margin 和 r_margin 的部分合并。

不支持压缩图像和bayer图像。

此方法在OpenMV Cam M4 上不可用。

#### image.find_rects([roi=Auto, threshold=10000])

使用用于查找AprilTAg的相同的quad detection算法来查找图像中的矩形。 最适用与背景形成鲜明对比的矩形。AprilTag的quad detection可以处理任意缩放/旋转/剪切的矩形。 返回一个 image.rect 对象的列表。

roi 是一个用以复制的矩形的感兴趣区域(x, y, w, h)。如果未指定， ROI即图像矩形。操作范围仅限于 roi 区域内的像素。

边界大小（通过在矩形边缘上的所有像素上滑动索贝尔算子并相加该值）小于 threshold 的矩形会从返回列表中过滤出来。 threshold 的正确值取决于您的应用程序/场景。

不支持压缩图像和bayer图像。

此方法在OpenMV Cam M4 上不可用。

#### image.find_qrcodes([roi])

查找 roi 内的所有二维码并返回一个 image.qrcode 对象的列表。 请参考 image.qrcode 对象以获取更多信息。

为使这一方法成功运行，图像上二维码需比较平展。通过使用 sensor.set_windowing 函数在镜头中心放大、 image.lens_corr 函数来消解镜头的桶形畸变或通过更换视野较为狭小的镜头， 您可得到一个不受镜头畸变影响的更为平展的二维码。有些机器视觉镜头不会造成桶形失真，但是其造价远比OpenMV提供的标准镜片高，这种镜头为无畸变镜头。

roi 是一个用以复制的矩形的感兴趣区域(x, y, w, h)。如果未指定，ROI即整幅图像的图像矩形。 操作范围仅限于 roi 区域内的像素。

不支持压缩图像和bayer图像。

此方法在OpenMV Cam M4 上不可用。

image.find_apriltags([roi[, families=image.TAG36H11[, fx[, fy[, cx[, cy]]]]]])
查找 roi 内的所有AprilTag, 并返回一个 image.apriltag 对象的列表。请参考 image.apriltag 对象以获取更多信息。

与二维码相比，AprilTags可在更远距离、较差光线和更扭曲的图像环境下被检测到。 AprilTags可应对所有种类的图像失真问题，而二维码并不能。也就是说，AprilTags只能将数字ID编码作为其有效载荷。

AprilTags也可用于本地化。每个 image.apriltag 对象都从摄像机返回其三维位置信息和旋转角度。 位置信息由 fx 、 fy 、 cx 和 cy 决定，分别为X和Y方向上图像的焦距和中心点。

> 使用OpenMV IDE内置的标签生成器工具来创建AprilTags。标签生成器可创建可打印的8.5“x11”AprilTags。

roi 是一个用以复制的矩形的感兴趣区域(x, y, w, h)。如果未指定，ROI即整幅图像的图像矩形。 操作范围仅限于 roi 区域内的像素。

families 是要解码的标签家族的位掩码。是一个逻辑或：

image.TAG16H5
image.TAG25H7
image.TAG25H9
image.TAG36H10
image.TAG36H11
image.ARTOOLKIT
默认设置为最好用的 image.TAG36H11 标签家族。注意：每启用一个标签家族， find_apriltags 的速度都会略有放慢。

fx 是以像素为单位的相机x方向的焦距。标准OpenMV Cam的值为(2.8 / 3.984) * 656， 该值通过毫米计的焦距值除以X方向上感光元件的长度，再乘以X方向上感光元件的像素数量得来（对OV7725感光元件而言）。

fy 是以像素为单位的相机y方向的焦距。标准OpenMV Cam的值为(2.8 / 2.952) * 488， 该值通过毫米计的焦距值除以Y方向上感光元件的长度，再乘以Y方向上感光元件的像素数量得来（对OV7725感光元件而言）。

cx 是图像的中心，即 image.width()/2 ，而非 roi.w()/2 。

cy 是图像的中心，即 image.height()/2，而非 roi.h()/2 。

不支持压缩图像和bayer图像。

此方法在OpenMV Cam M4 上不可用。

image.find_datamatrices([roi[, effort=200]])
查找 roi 内的所有数据矩阵并返回一个 image.datamatrix 对象的列表。 请参考 image.datamatrix 对象以获取更多信息。

为使这一方法成功运行，图像上矩形码需比较平展。通过使用 sensor.set_windowing 函数在镜头中心放大、 image.lens_corr 函数来消解镜头的桶形畸变或通过更换视野较为狭小的镜头，您可得到一个不受镜头畸变影响的更为平展的矩形码。 有些机器视觉镜头不会造成桶形失真，但是其造价远比OpenMV提供的标准镜片高，这种镜头是无畸变镜头。

roi 是一个用以复制的矩形的感兴趣区域(x, y, w, h)。如果未指定，ROI即整幅图像的图像矩形。操作范围仅限于 roi 区域内的像素。

effort 控制用于查找矩形码匹配的时间。默认值为200应该适用于所有用例。 但是您也可能以帧速率为代价增加检测，或以检测为代价增加帧速率。 注意：若 effort 设置在约160以下，您就无法进行任何检测；相反，您可将其设置为您需要的任何高值，但是若设置值高于240，检测率将不会继续随之提高。

不支持压缩图像和bayer图像。

此方法在OpenMV Cam M4 上不可用。

#### image.find_barcodes([roi])

查找 roi 内所有一维条形码并返回一个 image.barcode 对象列表。 请参考 image.barcode 对象以获取更多信息。

为了获得最佳效果，请使用长640、宽40/80／160窗口。垂直程度越低，运行速度越快。由于条形码是线性一维图像，所以只需在一个方向上有较高分辨率， 而在另一方向上只需较低分辨率。注意：该函数进行水平和垂直扫描，所以您可使用宽40/80／160、长480的窗口。 最后，请一定调整镜头，这样条形码会定位在焦距产生最清晰图像的地方。模糊条码无法被解码。

该函数支持所有一维条形码：

image.EAN2
image.EAN5
image.EAN8
image.UPCE
image.ISBN10
image.UPCA
image.EAN13
image.ISBN13
image.I25
image.DATABAR (RSS-14)
image.DATABAR_EXP (RSS-Expanded)
image.CODABAR
image.CODE39
image.PDF417
image.CODE93
image.CODE128
roi 是一个用以复制的矩形的感兴趣区域(x, y, w, h)。如果未指定，ROI即整幅图像的图像矩形。操作范围仅限于 roi 区域内的像素。

不支持压缩图像和bayer图像。

此方法在OpenMV Cam M4 上不可用。

image.find_displacement(template[, roi[, template_roi[, logpolar=False]]])
从模板中查找此图像的变换偏移量。 这种方法可以用来做光流。 此方法返回一个 image.displacement 对象，其中包含使用相位相关的位移计算结果。

roi 是需要处理的矩形区域（x，y，w，h）。如果未指定，则等于图像矩形。

template_roi 是需要处理的矩形区域（x，y，w，h）。如果未指定，则等于图像矩形。

roi 和 template roi必须具有相同的w/h，但x/y可以为图像任意位置。您可以在较大图像上滑动较小的rois以获得光流渐变图像.

image.find_displacement 通常计算两个图像之间的x/y平移。但是，如果您设置 logpolar = True ， 它将会在两个图像之间找到旋转和缩放比例的变化。相同的 image.displacement 对象结果两种可能的反馈。

不支持压缩图像和bayer图像。

注解

请在长宽一致的图像（例如``sensor.B64X64``）上使用此方法。

此方法在OpenMV Cam M4 上不可用。

#### image.find_number(roi)

运行在MINST数据集上训练的LENET-6 CNN（卷积神经网络），以检测位于图像上任何位置的28x28 ROI中的数字。 返回一个包含整数和浮点数的元组，表示检测到的数字（0-9）和检测的置信度（0-1）。

roi 是感兴趣区域的矩形元组(x，y，w，h)。如果未指定，ROI即整个图像的图像矩形。 操作范围仅限于 roi 区域内的像素。

仅支持灰度图像。

注解

这种方法是实验性的。如果未来运行使用Caffe在PC上训练的任何CNN，这种方法可能会删除。 最新3.0.0版本固件已删除此函数。

此方法在OpenMV Cam M4 上不可用。

#### image.classify_object(roi)

在图像的ROI上运行CIFAR-10 CNN，以检测飞机，汽车，鸟类，猫，鹿，狗，青蛙，马，船和卡车。 此方法在内部自动将图像缩放到32x32以馈送到CNN。

roi 是感兴趣区域的矩形元组(x，y，w，h)。如果未指定，ROI即整个图像的图像矩形。 操作范围仅限于 roi 区域内的像素。

仅支持RGB565图像。

注解

这种方法是实验性的。如果未来运行使用Caffe在PC上训练的任何CNN，这种方法可能会删除。

此方法在OpenMV Cam M4 上不可用。

image.find_template(template, threshold[, roi[, step=2[, search=image.SEARCH_EX]]])
尝试使用归一化互相关(NCC)算法在图像中找到第一个模板匹配的位置。返回匹配位置的边界框元组(x, y, w, h)，否则返回None。

template 是一个与这个图像对象相匹配的小图像对象。注意：两图像须都为灰度图。

threshold 是浮点数（0.0-1.0），其中较小的值在提高检测速率同时增加误报率。相反，较高的值会降低检测速率，同时降低误报率。

roi 是感兴趣区域的矩形元组(x，y，w，h)。如果未指定，ROI即整个图像的图像矩形。 操作范围仅限于 roi 区域内的像素。

step 是查找模板时需要跳过的像素数量。跳过像素可大大提高算法运行的速度。该方法只适用于SERACH_EX模式下的算法。

search 可为 image.SEARCH_DS or image.SEARCH_EX. image.SEARCH_DS 搜索模板所用算法较 image.SEARCH_EX 更快，但若模板位于图像边缘周围，可能无法成功搜索。 image.SEARCH_EX 可对图像进行较为详尽的搜索，但其运行速度远低于 image.SEARCH_DS 。

仅支持灰度图像。

#### image.find_features(cascade[, threshold=0.5[, scale=1.5[, roi]]])

这个方法搜索与Haar Cascade匹配的所有区域的图像，并返回一个关于这些特征的边界框矩形元组(x，y，w，h)的列表。若未发现任何特征，则返回一个空白列表。

cascade 是一个Haar Cascade对象。详细信息请查看 image.HaarCascade() 。

threshold 是浮点数（0.0-1.0），其中较小的值在提高检测速率同时增加误报率。相反，较高的值会降低检测速率，同时降低误报率。

scale 是一个必须大于1.0的浮点数。较高的比例因子运行更快，但其图像匹配相应较差。理想值介于1.35-1.5之间。

roi 是感兴趣区域的矩形元组(x，y，w，h)。如果未指定，ROI即整个图像的图像矩形。 操作范围仅限于 roi 区域内的像素。

仅支持灰度图像。

#### image.find_eye(roi)

在眼睛周围的感兴趣区域(x, y, w, h)查找瞳孔。返回一个包含图像中瞳孔(x，y)位置的元组。若未发现瞳孔，则返回(0,0)。

使用这一函数之前，需首先使用 image.find_features() 和Haar算子 frontalface 来搜索某人面部。 然后使用 image.find_features 和Haar算子 find_eye 在面部搜索眼睛。 最后，在调用 image.find_features 函数后返回的每个眼睛ROI上调用这一方法，以得到瞳孔的坐标。

roi 是感兴趣区域的矩形元组(x，y，w，h)。如果未指定，ROI即整个图像的图像矩形。 操作范围仅限于 roi 区域内的像素。

仅支持灰度图像。

#### image.find_lbp(roi)

从ROI元组(x, y, w, h)中提取LBP（局部二值模式）键点。您可以使用 image.match_descriptor 函数来比较两组关键点，以获取匹配距离。

roi 是感兴趣区域的矩形元组(x，y，w，h)。如果未指定，ROI即整个图像的图像矩形。 操作范围仅限于 roi 区域内的像素。

仅支持灰度图像。

#### image.find_keypoints([roi[, threshold=20[, normalized=False[, scale_factor=1.5[, max_keypoints=100[, corner_detector=image.CORNER_AGAST]]]]]])

从ROI元组(x, y, w, h)中提取ORB键点。您可以使用 image.match_descriptor 函数来比较两组关键点，以获取匹配区域。若未发现关键点，则返回None。

roi 是感兴趣区域的矩形元组(x，y，w，h)。如果未指定，ROI即整个图像的图像矩形。 操作范围仅限于 roi 区域内的像素。

threshold 是控制提取的数量的数字（取值0-255）。对于默认的AGAST角点检测器，该值应在20左右。 对于FAST角点检测器，该值约为60-80。阈值越低，您提取的角点越多。

normalized 是布尔值。若为True，在多分辨率下关闭提取键点。 若您不关心处理扩展问题，且希望算法运行更快，就将之设置为True。

scale_factor 是一个必须大于1.0的浮点数。较高的比例因子运行更快，但其图像匹配相应较差。理想值介于1.35-1.5之间。

max_keypoints 是一个键点对象所能容纳的键点最大数量。若键点对象过大导致内存问题，请降低该值。

corner_detector 是从图像中提取键点所使用的角点检测器算法。 可为 image.CORNER_FAST 或 image.CORNER_AGAST 。FAST角点检测器运行速度更快，但其准确度较低。

仅支持灰度图像。

#### image.find_edges(edge_type[, threshold])

将图像变为黑白，仅将边缘保留为白色像素。

image.EDGE_SIMPLE - 简单的阈值高通滤波算法
image.EDGE_CANNY - Canny边缘检测算法
threshold 是一个包含一个低阈值和一个高阈值的二值元组。您可以通过调整该值来控制边缘质量。

默认为 (100, 200)。

仅支持灰度图像。

find_hog([roi[, size=8]])
用HOG（定向梯度直方图）线替换ROI中的像素。

roi 是感兴趣区域的矩形元组(x，y，w，h)。如果未指定，ROI即整个图像的图像矩形。 操作范围仅限于 roi 区域内的像素。

仅支持灰度图像。

此方法在OpenMV Cam M4 上不可用。

## 常量

### image.SEARCH_EX

详尽的模板匹配搜索。

### image.SEARCH_DS

更快的模板匹配搜索。

### image.EDGE_CANNY

使用Canny边缘检测算法对图像进行边缘检测。

### image.EDGE_SIMPLE

使用阈值高通滤波算法对图像进行边缘检测。

### image.CORNER_FAST

用于ORB键点的高速低准确率角点检测算法

### image.CORNER_AGAST

用于ORB键点的低速高准确率算法。

### image.TAG16H5

TAG1H5标签群的位掩码枚举。用于AprilTags。

### image.TAG25H7

TAG25H7标签群的位掩码枚举。用于AprilTags。

### image.TAG25H9

TAG25H9标签群的位掩码枚举。用于AprilTags。

### image.TAG36H10

TAG36H10标签群的位掩码枚举。用于AprilTags。

### image.TAG36H11

TAG36H11标签群的位掩码枚举。用于AprilTags。

### image.ARTOOLKIT

ARTOOLKIT标签群的位掩码枚举。用于AprilTags。

### image.EAN2

EAN2条形码类型枚举。

### image.EAN5

EAN5条形码类型枚举。

### image.EAN8

EAN8条形码类型枚举。

### image.UPCE

UPCE条形码类型枚举。

### image.ISBN10

ISBN10条形码类型枚举。

### image.UPCA

UPCA条形码类型枚举。

### image.EAN13

EAN13条形码类型枚举。

### image.ISBN13

ISBN13条形码类型枚举。

### image.I25

I25条形码类型枚举。

### image.DATABAR

DATABAR条形码类型枚举。

### image.DATABAR_EXP

DATABAR_EXP条形码类型枚举。

### image.CODABAR

CODABAR条形码类型枚举。

### image.CODE39

CODE39条形码类型枚举。

### image.PDF417

PDF417条形码类型枚举（目前尚不能运行）。

### image.CODE93

CODE93条形码类型枚举。

### image.CODE128

CODE128条形码类型枚举。
