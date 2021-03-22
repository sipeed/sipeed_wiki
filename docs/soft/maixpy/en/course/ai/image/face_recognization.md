---
title: Face recognition
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: face recognition
---


In addition to detecting the position of the face, it can also identify who the person is (you need to target the person and press the button to learn)

Effect video: [youtube](https://www.youtube.com/embed/hS_mcGptXeo) or [bilibili](https://www.bilibili.com/video/BV1bJ411Q7L6)

<iframe src="https://player.bilibili.com/player.html?aid=77466790&bvid=BV1bJ411Q7L6&cid=132521878&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen ="true" width=500 height=400> </iframe>

## Instructions


* Download the model from [maixhub](https://www.maixhub.com/index/index/detail/id/235.html) and follow the instructions to obtain the model `smodel`, which is the encrypted version of `kmodel`
* Download the model to the development board according to the method of the introductory tutorial
* Run script [script](https://github.com/sipeed/MaixPy_scripts/blob/master/machine_vision/face_recognization/demo_face_recognization.py)


## Program understanding

There are three models in common, namely:
* Face detection model, which uses the same model as the previous face detection, that is, find the face
* Face key point detection model, find the position of the eyes, nose and mouth of the face from the face found in the front
* Face feature extraction model to obtain a feature value from a face picture

Proceed as follows:
* Face detected
* Cut out the face, find the eyes, nose and mouth of the face, here is a picture of `128x128`
* Rotate the face in the face image to the standard position
* Use the feature extraction model to extract the feature value of the face

With the previous foundation, the program here can be understood, and I will not elaborate on it. It just changed from using one model before to using three models in order, plus one more point. Simple image cropping and rotation processing are all calling `API`, look at the code carefully to know how the specific details are implemented
