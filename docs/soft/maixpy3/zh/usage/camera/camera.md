# 摄像头

MaixPy3 目前所兼容的摄像头是依赖硬件平台，不能进行随意切换，如果有需要的可以进行商务定制，联系方式<support@sipeed.com>

## 使用摄像头拍摄一张图并显示

使用前面所介绍的开发工具进入到 Maixpy3 的环境中，复制并运行一下代码
```python
from maix import display, camera
display.show(camera.capture())
```

屏幕上就会打印出摄像头所拍摄到的第一帧画面
![](./../asserts/camera_test.jpg)

## 屏幕实时显示摄像头拍摄画面
```python
from maix import display, camera
while True:
    display.show(camera.capture())
```
![](./../asserts/camera_1.gif)

可以通过 Ctrl + C 将其停止下来

## 拍摄图片并保存下来

运行一下代码可以直接

```python
from maix import camera, dispaly
img = camera.capture()
img.save('/mnt/UDISK/123.jpg')
display(img)
```

拍摄后的照片会保存在 /mnt/UDISK 文件下，可以通过 SSH、FTP、ADB 等链接方式将文件取出来。
