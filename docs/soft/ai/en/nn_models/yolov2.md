---
title: YOLOv2 Object Detection Model
---


YOLO (You Only Look Once) v2 has successfully achieved real-time target detection and has a high detection accuracy. Just like its name, you only need to look at it to know the result.

Because of its high detection efficiency, YOLO v2 can run on edge devices that are not very powerful, but it also has a disadvantage, that is, the detection ability for small objects is not enough.

## Target

Input a picture, output the target category and position in the picture, and can detect multiple objects at the same time.


## principle

Original paper: [YOLO9000: Better, Faster, Stronger](https://arxiv.org/abs/1612.08242)

The YOLOV2 backbone network is also a convolutional network, and the output layer uses a three-dimensional structure such as S x S x (Bx5+C), where S is the size of the grid, B is the number of bounding boxes predicted by each grid, and C is the category quantity.
That is, in S x S grids, each grid predicts B boxes, and each box has 5 parameters, namely x, y, w, h, p, where x, y are the center of the box The offset of the point relative to the upper left corner of the grid, w, h are the width and height of the box, p is the confidence of the box, and the last C parameters are the probability of the corresponding category.
For these B boxes, we manually determined B anchors (pre-selected boxes) in advance, each anchor has two parameters w, h, where w, h of the B prediction boxes are the scaling coefficients relative to the B anchors, In this way, the w and h of the prediction frame can be any value.
> These B Anchors are obtained by using the K-Means algorithm to cluster the width and height of all labeled boxes in the training data. The goal of clustering is to make the aspect ratio of each anchor close to the aspect ratio of the real box, so that the predicted box The aspect ratio of the frame will be closer to the aspect ratio of the real frame, thereby improving the detection accuracy. Therefore, there will be an anchors parameter in the code. This parameter is the B anchors obtained by counting the training data during training. In fact, when running the model, we must ensure that this parameter is consistent with the training time.

After obtaining all the prediction frames, it is necessary to filter the prediction frames to remove some frames with low confidence, that is, the p mentioned above, which is the threshold (threshold) we see in the code; and nms (non maximum suppression/non-maximum suppression) Calculate and remove boxes that predict the same classification and have too many overlapping parts, and keep the one with a higher probability, so we see in the code that there is an nms_threshold parameter, which is used to filter IOU (the intersection area (intersection) area/union area of two boxes) of boxes that are greater than this threshold.


It looks a bit complicated. If you want to learn in detail, you can refer to more tripartite tutorials and official papers. In fact, the pure model of the YOLO v2 model we trained can output a three-dimensional tensor such as S x S x (Bx5+C). Then the code library provides a decoding function. Call the function to input the three-dimensional tensor to get the legal prediction frame output. Even if you don’t understand the principle, it doesn’t prevent you from using this model.

## YOLO v3

Compared with YOLO v2, YOLO v3 has more outputs, which is more conducive to detecting small objects, but because of the multiple outputs, the amount of calculation will be much larger, and the frame rate is naturally lower than YOLO v2.

## Try to train a model

Create a detection training project in [MaixHub](https://maixhub.com), then collect data and label (can be marked online), create a training task, select the hardware platform you have, if there is no development board, you can use a mobile phone , select yolov2 for training, and after the training is completed, you can deploy it with one click to see the effect.

