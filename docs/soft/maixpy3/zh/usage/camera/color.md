# 颜色识别

## 寻找色块

寻找色块可以通过指定 HSV 阈值，进行颜色的确定，下面的例程代码可以通过修改中的函数参数进行修改寻找的颜色， 以下是 Maixpy3 中内置的颜色，可直接进行调用

    green = [(28,-36,-14,68,-5,15)]  #绿色
    red = [(20,22,-3,55,52,42)]    #红色
    yellow = [(35,-6,22,88,5,81)]   #黄色
    blue = [(13, 11, -91, 54, 48, -28)]  #蓝色
    white = [(41,6,-32,74,11,-12)]  #白色
    black = [(10,-3,-28,50,10,-4)]  #黑色



```python
from maix import camera
from maix import vision
from PIL import Image, ImageDraw
from maix import display

def find_blob():
    while True:
        tmp = camera.read()
        ma = vision.find_blob(tmp, (95, 219, 0, 255, 255, 255))
        # ma = cv.find_blob(tmp, (95, 219, 0, 255, 255, 255),tilt=1)
        print(ma)
        draw = display.get_draw()
        if ma:
            for i in ma:
                draw.rectangle((i["x"], i["y"], i["x"] + i["w"], i["y"] + i["h"]), outline='red', width=1)
            display.show()
        else:
            display.clear()

        
if __name__ == "__main__":
  find_blob()
```


## 识别色块

寻找色块是需要通过设置 HSV 的阈值进行寻找色块，但是对于一些没有内置 HSV 阈值的颜色，可以通过使用识别色块来进行颜色 HSV 阈值识别，这样就不需要进行手动阈值设置，使用以下例程代码，就可以返回在框选中颜色的 HSV 阈值。

> 以下代码由于 Maixpy3 还在优化中，可能不能运行，具体的代码到 [github](https://github.com/sipeed/MaixPy3) 上查看

```python
from maix import camera
from maix import vision
from PIL import Image, ImageDraw
from maix import display

def get_blob_hsv():
    while True:
        tmp = camera.read()
        ma = vision.get_blob_hsv(tmp,[110,110,20,20],5)
        print(ma)
        draw = display.get_draw()
        draw.rectangle((110,110, 130, 130), outline='red', width=1) 
        display.show()

        
if __name__ == "__main__":
  get_blob_hsv()

```

![缺示例图片]()

颜色在计算机视觉当中是有多种表达形式，如 RBG 、 CMYK、 HSV等

## HSV格式

Maixpy3 中使用的格式是 HSV 格式，通过调整 HSV 中的各个阈值进行识别

![](./../../assets/get_started/HSV.jpg)

- **色调H**
用角度度量，取值范围为0°～360°，从红色开始按逆时针方向计算，红色为0°，绿色为120°,蓝色为240°。它们的补色是：黄色为60°，青色为180°,紫色为300°

- **饱和度S**
饱和度S表示颜色接近光谱色的程度。一种颜色，可以看成是某种光谱色与白色混合的结果。其中光谱色所占的比例愈大，颜色接近光谱色的程度就愈高，颜色的饱和度也就愈高。饱和度高，颜色则深而艳。光谱色的白光成分为0，饱和度达到最高。通常取值范围为0%～100%，值越大，颜色越饱和。

- **明度V**
明度表示颜色明亮的程度，对于光源色，明度值与发光体的光亮度有关；对于物体色，此值和物体的透射比或反射比有关。通常取值范围为0%（黑）到100%（白）



