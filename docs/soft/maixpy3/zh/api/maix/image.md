---
title: MaixPy3 image 模块
keywords: MaixPy3，图像处理，图像算法，传统视觉, image API
desc: MaixPy3 image 模块 API 文档, 以及使用说明
---

>! API 仍处于非完全稳定状态, 可能在未来会有小幅改动。

## 导入模块

Image 对象是机器视觉操作的基本对象。

```python
from maix import image
```

image(_maix_image) 模块采用 pybind11 c++ 语言进行开发。

```bash
            any_image
         |              |
         V              V
    maix_vision      other
                | |
                 T
                 V
            maix_image
```

## 图像模块全局接口

> 0.4.6 到 0.4.8 后才引入全局模块接口。

- image.new

  创建 Image 对象，对应下述的 Image.open 实现。

- image.load

  加载图像数据，并创建 Image 对象，对应下述的 Image.load 实现。

- image.open

  打开图像文件，并创建 Image 对象，对应下述的 Image.open 实现。

- image.load_freetype(path="xxx.ttf")

  加载 freetype 字体,加载后执行 draw_string() 函数将会用该函数加载的字体.

- image.get_string_size(str="hello", [scale=1.0])

  计算某个字符串的高度和长度，方便字符串确定显示的位置。
  str 字符串， scale 对应 draw_string 的 scale 参数。

- image.free_freetype()

  释放当前加载 freetype 字体。

## Image 对象属性变量

- Image.width

  返回以像素计的图像的宽度。

- Image.height

  返回以像素计的图像的高度。

- Image.mode

  返回图像的格式,目前支持"RGB", "RGBA", "L", "RGB16"(RGB565)

- Image.size

  返回以像素计的图像的大小，如相同 width height 但不同 mode 的 RGB 和 RGBA 不同缓冲区长度。

## Image 对象基础接口

打开、关闭、加载、保存、转换、复制、清除、序列化。

- Image.new([size = (240, 240), [color = (0, 0, 0) , [mode = "RGB"]]])

  创建一张新的图片,size为图像尺寸,color为图像填充颜色,mode为图像格式.目前支持"RGB", "RGBA", "L", "RGB16"(RGB565)
  返回 Image 对象，以便您可以使用 . 表示法调用另一个方法。

- Image.open(path)

  从二进制文件中打开一张图片,path为路径名,会统一转换成RGB模式.Image.open("./tmp.jpg")

- Image.save(path)

  将Image 对象保存成二进制文件,Image.save("./tmp.jpg")

- Image.load(data, [size = (240, 240) , [mode = "RGB"]])

  在 python 对象中加载出一张图像,会将 python 对象的数据 copy 到 Image 对象内部，如将 tobytes 的二进制数据重新恢复成 Image对象。
  date可以是PIL对象, image.Image() 对象,bytes对象,numpy 对象.
  当data为bytes,numpy对象时,需要提供size和mode参数.
  返回 Image 对象，以便您可以使用 . 表示法调用另一个方法。

- Image.copy([img = "maix_image"])

  返回一张img类的Image 对象,img可以是"maix_image", "PIL", "numpy"
  返回 Image 对象，以便您可以使用 . 表示法调用另一个方法。

- Image.clear()

  清除 image.Image 对象内部的图像数据，但不删除对象。

- Image.delete()

  释放 image.Image 对象。

- Image.tobytes()

  返回图像的 bytes 数据，用于序列化数据。

- Image.resize(w, h, func = 1, padding = 1, size=(0, 0))

  将图像调整至(w, h)大小,func 可选,size 可选（和 w h 互斥），padding 默认会按比例缩放填充，而不是 CV 的拉伸图像变形。
    0     (INTER_NEAREST 最近邻插值)
    1     (INTER_LINEAR 双线性插值)（默认设置）
    2     (INTER_CUBIC 4x4像素邻域的双三次插值)
    3     (INTER_AREA 使用像素区域关系进行重采样)
    4     (INTER_LANCZOS4 8x8像素邻域的Lanczos插值)

  返回 Image 对象，以便您可以使用 . 表示法调用另一个方法。

- Image.draw_line(x1, y1, x2, y2, [color = (127, 127, 127), [thickness = 1]])

  在图像上绘制一条从(x0，y0)到(x1，y1)的线。
  color 是RGB888元组。默认为灰色。
  thickness 控制线的粗细像素。
  返回 Image 对象，以便您可以使用 . 表示法调用另一个方法。

- Image.draw_cross(x1, y1, c, size, [color = (127, 127, 127), [thickness = 1]])

  还不确定实现接口，待测试和设计。

- Image.draw_rectangle(x1, y1, x2, y2, [color = (127, 127, 127), [thickness = 1]])

  在图像上绘制一个矩形。
  color 是RGB888元组。默认为灰色。
  thickness 控制线的粗细像素。当thickness=-1时,将会用color颜色填充整个区域.
  返回 Image 对象，以便您可以使用 . 表示法调用另一个方法。

- Image.draw_circle(x, y, radius, [color = (127, 127, 127), [thickness = 1]])

  在图像上绘制一个圆形。x, y为圆的中心点坐标, radius为圆的半径
  color 是RGB888元组。默认为灰色。
  thickness 控制线的粗细像素。当thickness=-1时,将会用color颜色填充整个区域.
  返回 Image 对象，以便您可以使用 . 表示法调用另一个方法。

- Image.draw_ellipse(cx, xy, rx, ry, angle, startAngle, endAngle, [color = (127, 127, 127), [thickness = 1]])

  在图像上绘制椭圆。
  cx, xy, rx, ry ,椭圆的中心坐标和长轴短轴.
  angle 椭圆旋转角度(0~180)
  startAngle椭圆的开始绘图角度(0~360),
  endAngle椭圆的结束绘图角度(0~360),
  color 是RGB888元组。默认为灰色。
  thickness 控制线的粗细像素。当thickness=-1时,将会用color颜色填充整个区域.
  返回 Image 对象，以便您可以使用 . 表示法调用另一个方法。

- Image.draw_string(x, y, str, [scale = 1.0, [color = (127, 127, 127), [thickness = 1]]])

  从图像中的(x, y)位置开始绘制文本
  scale 可以放大/缩小图像上文本的大小。您可以传递大于0的整数或浮点值。
  color 是RGB888元组。默认为灰色。
  thickness 控制线的粗细像素。您可以传递大于0的整数.
  返回 Image 对象，以便您可以使用 . 表示法调用另一个方法。

- Image.rotate(rotate = 1.0)

  旋转图像到固定的角度,保持图像的尺寸不变
  rotate旋转角度.您可以传递大于0的浮点值.
  返回 Image 对象，以便您可以使用 . 表示法调用另一个方法。

- Image.flip(flip = 1)

  沿着 x 或 y 轴进行翻转图像，保持图像的尺寸不变，参数 -1 horizontal & vertical, 1 horizontal, 0 vertical 。

- Image.convert(mode = "RGB")

  转换图像的格式.
  mode为图像格式.目前支持"RGB", "RGBA", "L", "RGB16"(RGB565)
  返回 Image 对象，以便您可以使用 . 表示法调用另一个方法。

- Image.crop(x, y, w, h)

  别名为 cut 函数接口。
  裁剪图片返回一张全新的图片
  x, y, w, h裁剪图像的位置和大小
  返回 Image 对象，以便您可以使用 . 表示法调用另一个方法。

- Image.draw_image(img, x, y)

  将传递的img图像画在 image.Image() 对象内部的图像上
  img只能传递 image.Image() 对象的图像.
  返回 Image 对象，以便您可以使用 . 表示法调用另一个方法。

- Image.get_pixel(x, y)

  得到图像x,y位置的像素值,返回是一个四元组对象,(r, g, b, a),如果为灰度,那只有r有效

## Image 对象视觉操作

maix_vision 类是对于图像的一系列操作方法的集合

- maix_vision.get_blob_color(roi = (0, 0, 0, 0), critical = 0, co = 0)

  统计函数,得到图像感兴趣区域的最大颜色值.
  roi 是感兴趣区域的矩形元组(x，y，w，h)。如果未指定，ROI即整个图像的图像矩形。 操作范围仅限于 roi 区域内的像素。尽量选取较小的区域,区域较大时统计效果比较差.
  critical为返回值区域范围,简单将统计到的最大颜色值和critical相加或相减,当为0时,返回原来的色值.
  co为返回的颜色空间模型.可选为
  0       rgb
  1       lab
  2       hsv
  返回值:
  当co为0时返回[r, g, b]
  当co为1时返回[L - critical, A - critical, B - critical, L + critical, A + critical, B + critical]
  当co为2时同1

- maix_vision.find_blobs(thresholds, roi = (0,0,0,0), x_stride = 2, y_stride = 2, invert = 0, area_threshold = 10, pixels_threshold = 10, merge = 0, margin = 0, tilt = 0, co = 1)

  查找图像中所有色块，并返回一个包括每个色块的色块对象的列表。
  thresholds 必须是元组列表. [(minL, minA, minB, maxL, maxA, maxB)]
  roi 是感兴趣区域的矩形元组(x，y，w，h)。如果未指定，ROI即整个图像的图像矩形。 操作范围仅限于 roi 区域内的像素。
  x_stride 是查找某色块时需要跳过的x像素的数量。找到色块后，直线填充算法将精确像素。 若已知色块较大，可增加 x_stride 来提高查找色块的速度。
  y_stride 是查找某色块时需要跳过的y像素的数量。找到色块后，直线填充算法将精确像素。 若已知色块较大，可增加 y_stride 来提高查找色块的速度。
  invert 反转阈值操作，像素在已知颜色范围之外进行匹配，而非在已知颜色范围内。
  若一个色块的边界框区域小于 area_threshold ，则会被过滤掉。
  若一个色块的像素数小于 pixels_threshold ，则会被过滤掉。
  merge 若为True，则合并所有没有被过滤掉的色块，这些色块的边界矩形互相交错重叠。
  margin 可在相交测试中用来增大或减小色块边界矩形的大小。例如：边缘为1、相互间边界矩形为1的色块将被合并。
  tilt设置是否查找最小斜矩形框,为0则不查找.
  co为返回的颜色空间模型.可选为,如果不是特殊需要,请保持默认
  0       rgb
  1       lab
  2       hsv
  3       灰度
  返回值:[{'x': 140, 'y': 88, 'w': 15, 'h': 7, 'pixels': 43, 'cx': 147, 'cy': 91}]
  (x, y, w, h)色块的外框,pixels,色块的像素大小,(cx, cy)色块的中心点.

- maix_vision.find_ball_color(thresholds, co = 1)

  该函数是在maix_vision.find_blobs的基础上通过基尔霍夫圆拟合,并返回拟合的圆.
  thresholds 必须是元组列表. [(minL, minA, minB, maxL, maxA, maxB)]
  co为返回的颜色空间模型.可选为,如果不是特殊需要,请保持默认
  0       rgb
  1       lab
  2       hsv
  返回值:

- maix_vision.find_line()

  该函数是内置的寻线函数.通过自适应的图像操作,将图像中的黑线选出来,然后返回黑线的矩形区域,可以作为小车的寻线函数.
  返回值:
  {'rect': [9, 229, 9, 9, 145, 9, 145, 229], 'pixels': 12959, 'cx': 77, 'cy': 119, 'rotation': -1.570796251296997}
  rect为线的框,
  pixels为线的像素大小
  (cx, cy)框的中心点
  rotation为框的偏转角度(弧度制)

> 下述函数可用，但暂时没写说明。

- get_statistics

- rotation_corr

- gamma_corr

- lens_corr

- mean

- find_rects

- find_lines

- find_circles

- find_line_segments

- find_apriltags

- find_qrcodes

- find_barcodes
