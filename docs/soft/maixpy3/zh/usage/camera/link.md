# 巡线识别

对于传统的智能小车来说，巡线是一个重要的功能， Maixpy3 中内置了巡线函数

> 以下代码由于 Maixpy3 还在优化中，可能不能运行，具体的代码到 [github](https://github.com/sipeed/MaixPy3) 上查看

```python
from maix import camera
from maix import vision
from PIL import Image ,ImageDraw
from maix import display

def find_line():
    while True:
        tmp = camera.read()
        # tmp = camera.capture() # r329
        if tmp:
            ma = vision.find_line(tmp)
            draw = display.get_draw()
            # draw.paste(tmp) # r329
            draw.line([(ma["rect"][0], ma["rect"][1]), (ma["rect"][2], ma["rect"][3])],fill='white',width=1)
            draw.line([(ma["rect"][2], ma["rect"][3]), (ma["rect"][4], ma["rect"][5])],fill='white',width=1)
            draw.line([(ma["rect"][4], ma["rect"][5]), (ma["rect"][6], ma["rect"][7])],fill='white',width=1)
            draw.line([(ma["rect"][6], ma["rect"][7]), (ma["rect"][0], ma["rect"][1])],fill='white',width=1)
            draw.ellipse(((ma["cx"]-2, ma["cy"]-2), (ma["cx"]+2, ma["cy"]+2)), fill=None, width=1)
            display.show()

if __name__ == "__main__":
  find_line()
```
