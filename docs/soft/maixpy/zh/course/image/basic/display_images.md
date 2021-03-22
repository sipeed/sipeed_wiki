---
title: 显示图片
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 显示图片
---



显示图片很简单， 直接使用 `lcd` 模块，调用函数进行显示即可， 如下：

```python
import lcd, image

lcd.init()

img = image.Image("/sd/test.jpg")
lcd.display(img)
```

但是不同的屏幕初始化序列可能不一样， 在`lcd.init`的时候有很多可选参数， 具体看 API 文档的描述，常见的如下

对于 IPS 屏幕，需要反色：
```python
lcd.init(type=2)
```

对于屏幕体质不是很好， 需要降低频率，或者体质很好需要超频：
```python
lcd.init(freq = 15000000)
```

另外， 也可是设置屏幕的旋转方向：
```python
lcd.rotation(2)
```
参数是`0～3`, 分别代表顺时针旋转 `0度` `90度` `180度` `270度`

更多方法， 请参考 [lcd 文档](./../../../api_reference/machine_vision/lcd.md)


