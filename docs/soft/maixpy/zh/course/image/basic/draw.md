---
title: 画图 写字
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 画图 写字
---



有两种方式，推荐第二种

## 第一种， 使用`lcd`模块直接在屏幕上画

```python
import image, lcd

lcd.init()

lcd.draw_string(0, 0, "hello")
```

更多的函数和参数，参见[lcd API 手册](./../../../api_reference/machine_vision/lcd.md)

## 第二种， 使用`image` 模块在内存中画，画完后使用`lcd.display`函数将整张图片展示到屏幕

```python
import image, lcd

lcd.init()

img = image.Image(size=(320, 240))
img.draw_string(0,0, "hello")
lcd.display(img)

```

更多的函数和参数，可以看 [image API 手册](./../../../api_reference/machine_vision/image/image.html) , 在页面搜索`image.draw` 可以找到所有画图函数
需要中文（多国语言）支持请看 [如何显示中文](./../../../course/image/image_draw_font/image_draw_font.md) ,或搜索 “字库” 。
