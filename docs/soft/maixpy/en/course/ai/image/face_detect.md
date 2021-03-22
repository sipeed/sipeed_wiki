---
title: Face detection
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: face detection
---


Find the face in a picture, and frame the face, that is, know the position and size of the face

Use the `YOLO V2` model to detect faces

## Instructions:

* Download model: Go to [here](https://dl.sipeed.com/MAIX/MaixPy/model) to download the model file `face_model_at_0x300000.kfpkg`
* Use kflash_gui to download the model to Flash, or put it in SD card
* Load model
```python
task = kpu.load(0x300000)
# task = kpu.load("/sd/face.kmodel")
anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)
kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)
```
Because the model of `YOLO V2` is used, it has a dedicated function interface, use `init_yolo2` to initialize the model

The parameters are:
* `kpu_net`: kpu network object, that is, the loaded model object, the return value of `KPU.load()`
* `threshold`: Probability threshold, only if the probability of this object is greater than this value will the output result, value range: [0, 1]
* `nms_value`: box_iou threshold, in order to prevent the same object from being framed in multiple boxes, when two boxes are framed on the same object, the intersection area of ​​the two boxes accounts for the proportion of the total occupied area of ​​the two boxes. When it is less than this value, take the box with the highest probability
* `anchor_num`: the number of anchor points, fixed here as `len(anchors)//2`
* `anchor`: The anchor point parameters are consistent with the model parameters. This parameter of the same model is fixed and bound to the model (it is determined when the model is trained) and cannot be changed to other values.

Then enter the image data and run the model

```python
code = kpu.run_yolo2(task, img)
```

To get the result, see [here](https://github.com/sipeed/MaixPy_scripts/blob/master/machine_vision/face_find/demo_find_face.py) for the complete example

API documentation see [Maix.KPU](/api_reference/Maix/kpu.md)
