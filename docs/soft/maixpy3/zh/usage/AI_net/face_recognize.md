---
title: 人脸识别
keywords: 人脸识别, MaixPy3, Python, Python3
desc: maixpy doc: 人脸识别
---

人脸识别的模型，可以通过 maixhub 中下载，将下载之后得到的模型，通过 ssh 等连接方式，存放到开发板中

具体的部署代码在 [Github](https://github.com/sipeed/MaixPy3/blob/master/ext_modules/_maix_nn/example/face_recognize.py) 中，将代码复制出来，需要修改脚本中读取模型的位置，运行代码即可进行人脸识别

```python
def __init__(self, threshold = 0.5, nms = 0.3, max_face_num = 1):
        model = {
            "param": "res/model_int8.param",
            "bin": "res/model_int8.bin"
        }
        model_fe = {
            "param": "res/fe_res18_117.param",
            "bin": "res/fe_res18_117.bin"
        }
        self.input_size = (224, 224, 3)
        input_size_fe = (128, 128, 3)
        self.feature_len = 256
        self.features = []

```

通过按键来进行人脸的录入，识别到正确的人脸回显示成绿的绿色的框，右键为添加人脸，左键为删除人脸