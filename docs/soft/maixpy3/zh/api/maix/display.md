---
title: MaixPy3 display 模块
keywords: MaixPy3，屏幕, display API
desc: MaixPy3 display 模块 API 文档, 以及使用说明
---

>! API 仍处于非完全稳定状态, 可能在未来会有小幅改动。

## 导入模块

```python
from maix import display
```

### display.width & display.height

返回当前屏幕配置的图像的宽和高。

```python
>>> print(display.width, display.height)
<function width at 0x7f54a80f9160> <function height at 0x7f54a80f91f0>
>>> print(display.width(), display.height())
240 240
>>>
```

### display.config

配置屏幕，如大小、类型，在桌面环境上  。

```python
>>> display.config((416, 416))
>>> print(display.width(), display.height())
416 416
>>>
```

> 官方的板子会自动从设备树或 fb 里取大小配置，若是桌面系统可以通过该参数配置成更大的窗口。

### display.as_image

可以把 display 作为 _maix_image.image 使用。

```python
>>> print(display.as_image())
<_maix_image.Image 0x2033160 " width":240, "height":240, "type"=RGB, "size":172800>
```

### display.show()

根据传入的 image 对象来自适应显示图像内容。

```python
from maix import display
display.show(display.as_image())
```

如果处于 IDE 模式下会自动进行图传到 jupyter rpyc 核心上。
