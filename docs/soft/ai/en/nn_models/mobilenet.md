---
title: MobileNet Object Classification Model
---

The Mobilenet network is a lightweight deep neural network proposed by Google for mobile phones and embedded scenarios. Its main feature is to use depthwise separable convolution instead of ordinary convolution, thereby reducing the amount of calculation and improving Computational efficiency of the network. The classification accuracy of the network on the ImageNet dataset has reached 70.8%. In the case of a small loss of accuracy, the amount of calculation is greatly reduced, making it possible for the neural network model to run smoothly on ordinary single-chip computers!


## Target

Input several images in order, output which category each image belongs to, and the confidence of the category.


## principle


For those who are not very interested in the detailed principles, you can simply understand:

* Convolution calculation has the function of extracting features. For example, the result of an image after a convolution calculation will extract the outline of the image, such as the classic Sobel edge detection. The result after a convolution calculation:
![](../../assets/sobel_edge2.jpg)
It can be said that through a convolution calculation, the outline of the image is extracted, which is the feature extraction function of convolution calculation.
After multiple convolution calculations, the features of different images will be extracted. You can see this process visualized at [tensorspace.org](https://tensorspace.org/html/playground/mobilenetv1.html).

* After the entire network calculation consisting of countless convolution calculations and other calculations, an image with only 1000 pixels is finally output, and different classifications of image inputs are included. Among the 1000 pixels in the output layer, the value of one of the pixels It will be larger, and the classification corresponding to this pixel is the output result of the network. For example, if a panda image is input, if the value of the 388th pixel of the output layer is large and the value is 0.8, we will recognize that this image is a panda through this network, with a confidence level of 0.8.

* As for the Mobilenet network claiming to use depthwise separable convolution (depthwise separable convolution) to replace ordinary convolution, thereby reducing the amount of calculation and improving the computational efficiency of the network, you can understand that compared to the previous convolutional network, it is still convolution Product calculation is just different from the ordinary convolution calculation method used on images, so that the number of calculations can be reduced and the calculation efficiency of the network can be improved. For the specific method, please read the relevant articles further.

* As for training, as mentioned in the basic knowledge, by continuously inputting images to the network, then let the network output the correct classification, and then calculate the gap between the classification output by the network and the correct classification through the loss function, and then through backpropagation The algorithm continuously adjusts the parameters in the network, so that the gap between the classification output by the network and the correct classification becomes smaller and smaller, and finally the network can output the correct classification. Training is actually to find the parameters in the network suitable for our data, such as the values of all convolution kernels in the network, all bias values in the network, and so on.



Regarding the specific principle of Mobilenet, we will not introduce it in detail here. Interested readers can refer to the original paper of Mobilenet ([MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/abs/1704.04861) ) and Other tripartite tutorials


## Mobilenet V2

Mobilenet V2 is an upgraded version of Mobilenet. Its main improvement is to optimize the structure of the network, making the network more efficient and more accurate.


## Try to train a model

Create a classification training project in [MaixHub](https://maixhub.com), then collect data, create a training task, and select the hardware platform you have as a parameter. If you don’t have a development board, you can use a mobile phone, and choose mobilenetv1 or mobilenetv2 for training That’s right, after the training is complete, you can deploy it with one click to see the effect.

