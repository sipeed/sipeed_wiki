# 巡线识别

对于传统的智能小车来说，巡线是一个重要的功能， Maixpy3 中内置了巡线函数

> 以下代码由于 Maixpy3 还在优化中，可能不能运行，具体的代码到 [github](https://github.com/sipeed/MaixPy3) 上查看

```python
from maix import camera, image, display

while True:
    img = camera.capture()
    ma = img.find_line()
    if ma:
        img.draw_line(ma['rect'][0], ma['rect'][1], ma['rect'][2], ma['rect'][3], (255,255,225), 1)
        img.draw_line(ma["rect"][2], ma["rect"][3], ma["rect"][4], ma["rect"][5], (255,255,225), 1)
        img.draw_line(ma["rect"][4], ma["rect"][5], ma["rect"][6], ma["rect"][7], (255,255,225), 1)
        img.draw_line(ma["rect"][6], ma["rect"][7], ma["rect"][0], ma["rect"][1], (255,255,225), 1)
        img.draw_circle(ma["cx"], ma["cy"], 2, (255,255,225), 1)
    display.show(img)
```
