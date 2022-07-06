# 将自己的神经网络部署的到 MaixII-Dock 上

| 时间 | 负责人 | 更新内容 | 备注 |
| --- | --- | --- | --- |
| 2022年1月26日 | Rui | 编写文档 | --- |

对于一些自定义的神经网络结构，可以通过 MaixPy3 部署到所支持的开发板上。将边缘检测部署到 MaixII-Dock 为例，讲述一下部署的思路

## 前置知识

进行之前，需要学习神经网络的基础知识，可以通过查看前面的 【[深度神经网络基础知识](./information.md)】 快速的了解一下，想要了解更多可以自行百度神经网络的相关教程

## 边缘检测原理介绍

边缘就是值变化剧烈的地方, 如果对值的变化求导, 则边缘部分就是导数局部最大。但是在图像处理时没有具体的函数让我们求导, 使用卷积运算则可以很好的近似替代。

如下图, 假设左上为坐标原点, 横轴为 x, 纵轴为y, 如下图左上角9个像素点, P(x, y)表示坐标(x, y)的点, 要求P(1, 1)处在x轴的变化率, 则只需将P(2, 1) - P(0, 1) 得到值为0, P(1, 0)处为1-3 = -2, 这个差值即变化率, 类比成导数, 我们就能知道横轴在哪些地方变化率更大。

![](https://neucrack.com/image/1/377/conv.jpg)

上面这种方法我们可以得到横轴的变化率, 这里使用**横轴卷积核**

~~~ python
[-1, 0, 1],
[-2, 0, 2],
[-1, 0, 1]
~~~

对图像进行卷积运算, 如图中的计算方法, 像素点左右权值取2, 角上的也参与计算,但是权值为1,没有左右边的权值高。这样我们就得到了横轴的变化率图, 即边缘检测图。

注意, 这里是对横轴计算了, 比较的点左右的值变化, 所以实际看到的图像会出现明显的纵轴边缘, 如下图左边

![](https://neucrack.com/image/1/377/vertical_horizontal.jpg)

同理, 上图右边的图使用**纵轴卷积核**
```
[1, 2, 1],
[0, 0, 0],
[-1, -2, -1]
```
得到的纵轴的边缘图。

注意这里用右边减左边, 如果右边的值比左边的小会是负数, 如果我们希望只检测颜色值变大(变白)则可以直接使用, 如果两个变化方向都要检测, 则可以取绝对值. 比如下图左边是没有取绝对值, 右边取了绝对值

![](https://neucrack.com/image/1/377/without_with_abs.jpg)

得到两个方向的图后, 对其进行合并, 对每个像素平方和开方即可

![](https://neucrack.com/image/1/377/final.jpg)

这张图左边是使用 GIMP 的 sobel 边缘检测(垂直+水平)的效果, 略微有点不同:

![](https://neucrack.com/image/1/377/sobel_edge2.jpg)

不同的原因是使用水平和垂直的图平方和开根后, 直接用 `plt.imshow` 显示, 和 GIMP 的处理方式不同
```python
out = np.sqrt(np.square(out_v) + np.square(out_h))
plt.imshow(out)
```
简单地直接将值规范到`[0, 255]`就和 GIMP 的图相似了(但不完全一样)
```python
out = np.sqrt(np.square(out_v) + np.square(out_h))
out = out * 255.0 / out.max()
plt.imshow(out.astype(np.uint8))
```
![](https://neucrack.com/image/1/377/sobel_v_h.jpg)

## 定义卷积核

除了上面说了使用两次卷积计算, 也可以用只计算一次的卷积核, 比如:
```bash
[-1, -1, -1],
[ -1, 8, -1],
[ -1, -1, -1]
```
这是对于一个通道(灰度图)来说, 如果要扩充到三个通道(RGB), 卷积核参数就是如下形式
```bash
# 全边缘卷积核
conv_rgb_core_sobel = [
                        [[-1,-1,-1],[-1,8,-1], [-1,-1,-1],
                         [0,0,0],[0,0,0], [0,0,0],
                         [0,0,0],[0,0,0], [0,0,0]
                        ],

                        [[0,0,0],[0,0,0], [0,0,0],
                         [-1,-1,-1],[-1,8,-1], [-1,-1,-1],
                         [0,0,0],[0,0,0], [0,0,0]
                        ],a

                        [[0,0,0],[0,0,0], [0,0,0],
                         [0,0,0],[0,0,0], [0,0,0],
                         [-1,-1,-1],[-1,8,-1], [-1,-1,-1],
                        ]]
```

前面所有介绍的横轴边缘和纵轴边缘卷积核参数形式同理

## 代码实现边缘检测

整个边缘检测的网络模型只有一层卷积核

### 定义网络模型

```python
import torch
import torch.nn as nn
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 3, 3, padding=(0, 0), bias=False)
    def forward(self, x):
        x = self.conv1(x)
        return x
net = Net()
```

### 定义卷积核参数

```python
conv_rgb_core_sobel = [
                        [[-1,-1,-1],[-1,8,-1], [-1,    -1,    -1],
                         [0,0,0],[0,0,0], [0,0,0],
                         [0,0,0],[0,0,0], [0,0,0]
                        ],
                        [[0,0,0],[0,0,0], [0,0,0],
                         [-1,-1,-1],[-1,8,-1], [-1,    -1,    -1],
                         [0,0,0],[0,0,0], [0,0,0]
                        ],
                        [[0,0,0],[0,0,0], [0,0,0],
                         [0,0,0],[0,0,0], [0,0,0],
                         [-1,-1,-1],[-1,8,-1], [-1,    -1,    -1],
                        ]]
```

### 定义载入权重函数

```python
def sobel(net, kernel):
    sobel_kernel = np.array(kernel,    dtype='float32')
    sobel_kernel = sobel_kernel.reshape((3,    3,    3,    3))
    net.conv1.weight.data = torch.from_numpy(sobel_kernel)
params = list(net.parameters())
```

### 输入数据进行处理

加载一张图片

```python
pil_img = Image.open("./images/class1_5.jpg")
display(pil_img)
input_img = np.array(pil_img)
print(input_img.shape)
```

对图片进行归一化处理并转换成 PyTorch 张量

```python
# 归一化处理
input_tensor = (input_img.astype(np.float32) - 127.5) / 128 # to [-1, 1]
print(input_tensor.shape)
input_tensor = torch.Tensor(input_tensor).permute((2, 0, 1))
input_tensor = input_tensor.unsqueeze(0)
print("input shape:", input_tensor.shape)

# 转换成 PyTorch 张量
input_tensor = (input_img.astype(np.float32) - 127.5) / 128 # to [-1, 1]
input_tensor = torch.Tensor(input_tensor).permute((2, 0, 1))
print(input_tensor.shape)
input_tensor = input_tensor.unsqueeze(0)
print("input shape:", input_tensor.shape)
```

### 进行边缘检测

```python
# 载入网络权重
sobel(net, conv_rgb_core_sobel)

# 输入图片到网络中进行处理
with torch.no_grad():
    out = net(input_tensor)   
    sobel_img_t = out.numpy()[0].transpose([1,2,0])

# 显示输出结果
plt.figure()
plt.subplot(1, 5, 1)
plt.imshow(input_img)
plt.subplot(1, 5, 2)
plt.imshow(sobel_img_t)
```

经过卷积运算后, 前后图如下:

![](https://neucrack.com/image/1/377/sobel_edge.jpg)

注意, 输入值范围如果为`[0, 255]`, 输出值则范围会变化, 以图片形式查看时需要注意加以处理, 这里使用了`plt.imshow(out)`来显示, 这个函数会自动对图像做简单的处理, 才会看起来是黑色背景

## 模型导出
