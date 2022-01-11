---
title: 人脸检测
keywords: 人脸检测, MaixPy3, Python, Python3
desc: maixpy doc: 人脸检测
---

> 2022年01月11日 以下代码由于 Maixpy3 还在施工中，此处代码仅供参考和示范，功能已在 github 和 社区供其他同学使用和参考。

人脸检测的模型，可以通过 maixhub 中下载，将下载之后得到的模型，通过 ssh 等连接方式，存放到开发板中

具体的部署代码在 [Github](https://github.com/sipeed/MaixPy3/blob/master/ext_modules/_maix_nn/example/yolo2_camera.py) 中，将代码复制出来，需要修改脚本中读取模型的位置，运行代码即可进行人脸检测

> 最新的镜像已经将模型存放在 /home/model 文件夹下


进行人脸检测之前，需要先对模型进行部署
```python
class face:
    labels = ["person"]
    anchors = [1.19, 1.98, 2.79, 4.59, 4.53, 8.92, 8.06, 5.29, 10.32, 10.65]
    m = {
        "param": "/home/model/face/yolo2_face_awnn.param",
        "bin": "/home/model/face/yolo2_face_awnn.bin"
    }
    options = {
        "model_type":  "awnn",
        "inputs": {
            "input0": (224, 224, 3)
        },
        "outputs": {
            "output0": (7, 7, (1+4+1)*5)
        },
        "mean": [127.5, 127.5, 127.5],
        "norm": [0.0078125, 0.0078125, 0.0078125],
    }
    def __init__(self):
        from maix import nn
        from maix.nn import decoder
        self.model = nn.load(self.m, opt=self.options)
        self.yolo = decoder.Yolo2(len(self.labels), self.anchors, net_in_size=(224, 224), net_out_size=(7, 7))
        
    def __del__(self):
        del self.model
        del self.yolo
        
global Face
Face = face()
```

部署结束之后才能进行识别

```python
from maix import camera, display, nn, image
from maix.nn import decoder
labels = ["person"]
while True:
    img = camera.capture().resize(224,224)
    out = Face.model.forward(img.tobytes(), quantize=True, layout="hwc")
    boxes, probs = Face.yolo.run(out, nms=0.3, threshold=0.5, img_size=(224, 224))
    if len(boxes):
        for i, box in enumerate(boxes):
            img.draw_rectangle(box[0], box[1], box[0]+box[2], box[1]+box[3], (255,0,0), 1)
        display.show(img)
    else:
        display.show(img)
```

