# 颜色识别
MaixPy3 移植了 OpenCV 中一些对于颜色处理的功能，并这些功能进行封装，让用户可以更加容易的进行使用和开发，对于寻找色块、识别颜色也是轻轻松松的。

## 寻找色块
```python
from maix import camera
from PIL import Image, ImageDraw
from maix import display
import time
try:
  from maix import vision as maix_cv
except:
  from _maix_opencv import _v83x_opencv
  maix_cv = _v83x_opencv()

class funation:
    green = [(28,-36,-14,68,-5,15)]  #绿色
    red = [(20,22,-3,55,52,42)]    #红色
    yellow = [(35,-6,22,88,5,81)]   #黄色
    bull = [(13, 11, -91, 54, 48, -28)]  #蓝色
    white = [(41,6,-32,74,11,-12)]  #白色
    black = [(10,-3,-28,50,10,-4)]  #黑色
    def __init__(self,device=None):
        self.event = self.run
    def __del__(self):
      print("maix_cv_find_blob_lab will exit!")
    def run(self):
        tmp = camera.read(video_num = 0)
        if tmp:
            t = time.time()
            ma = maix_cv.find_blob_lab(tmp, self.bull)
            t = time.time() - t
            print("-- forward time: {}s".format(t))
            # print(ma)
            draw = display.get_draw()
            if ma:
                for i in ma:
                    draw.rectangle((i["x"], i["y"], i["x"] + i["w"], i["y"] + i["h"]), outline='red', width=1)
                display.show()
            else:
                display.clear()
        else:
            print('tmp err')


if __name__ == "__main__":
    import signal
    def handle_signalm(signum,frame):
        print("father over")
        exit(0)
    signal.signal(signal.SIGINT,handle_signalm)
    camera.config(size=(224,224))
    start = funation()
    while True:
        start.event()
```
通过修改上述代码第26行 `maix_cv.find_blob_lab()` 函数中的第二个参数，即可实现寻找别的颜色

## 识别色块

识别色块是通过识别指定区域内的颜色，和寻找颜色不一样，并不只是识别单一种颜色。

```python
from maix import camera
from PIL import Image, ImageDraw
from maix import display
import time
from maix import vision as maix_cv



import numpy as np

M = np.array([[0.412453, 0.357580, 0.180423],
              [0.212671, 0.715160, 0.072169],
              [0.019334, 0.119193, 0.950227]])


# im_channel取值范围：[0,1]
def f(im_channel):
    return np.power(im_channel, 1 / 3) if im_channel > 0.008856 else 7.787 * im_channel + 0.137931


def anti_f(im_channel):
    return np.power(im_channel, 3) if im_channel > 0.206893 else (im_channel - 0.137931) / 7.787


# region Lab 转 RGB
def __lab2xyz__(Lab):
    fY = (Lab[0] + 16.0) / 116.0
    fX = Lab[1] / 500.0 + fY
    fZ = fY - Lab[2] / 200.0

    x = anti_f(fX)
    y = anti_f(fY)
    z = anti_f(fZ)

    x = x * 0.95047
    y = y * 1.0
    z = z * 1.0883

    return (x, y, z)


def __xyz2rgb(xyz):
    xyz = np.array(xyz)
    xyz = xyz * 255
    rgb = np.dot(np.linalg.inv(M), xyz.T)
    # rgb = rgb * 255
    rgb = np.uint8(np.clip(rgb, 0, 255))
    return rgb


def Lab2RGB(Lab):
    xyz = __lab2xyz__(Lab)
    rgb = __xyz2rgb(xyz)
    return rgb


class funation:
    mk = [(46, 46, 194, 194),(64,64,77,77),(113,64,126,77),(163,64,176,77),(64,113,77,127),(113,113,127,127),(163,113,176,127),(64,163,77,176),(113,163,127,176),(163,163,176,176)]
    md = [(0, 0, 15, 15),(15, 0, 30, 15),(30, 0, 45, 15), (0, 15, 15, 30), (15, 15, 30, 30),(30, 15, 45, 30),(0, 30, 15, 45),  (15, 30, 30, 45),   (30, 30, 45, 45)]

    def __init__(self,device=None):  
        self.event = self.run
    def __del__(self):
      print("maix_cv_find_blob_lab will exit!")
    def run(self):
        tmp = camera.read(video_num = 0)
        draw = display.get_draw()

        for i,idx in enumerate(self.mk):
            if i == 0:
                draw.rectangle(idx, outline='red', width=1)
            else:
                draw.rectangle(idx, outline='red', width=1)
                mda = idx[0:2] + (13,13)
                lab_c = maix_cv.get_blob_lab(tmp, mda, 0)[0:3]
                rgb_c = Lab2RGB(lab_c)
                print(rgb_c)
                draw.rectangle(self.md[i-1], outline='white', width=1,fill = tuple(rgb_c))

        display.show()


if __name__ == "__main__":
    import signal
    def handle_signalm(signum,frame):
        print("father over")
        exit(0)
    signal.signal(signal.SIGINT,handle_signalm)
    camera.config(size=(224,224))
    start = funation()
    while True:
```
