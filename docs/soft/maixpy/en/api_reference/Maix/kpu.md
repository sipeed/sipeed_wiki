---
title: KPU
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: KPU
---


KPU is a general-purpose neural network processor, which can realize convolutional neural network calculations with low power consumption, obtain the size, coordinates, and types of detected objects from time to time, and detect and classify faces or objects.

* KPU has the following characteristics:
  * Support fixed-point models trained by mainstream training frameworks according to specific restriction rules
  * There is no direct limit on the number of network layers, and each layer of convolutional neural network parameters can be configured separately, including the number of input and output channels, input and output row width and column height
  * Support two convolution kernels 1x1 and 3x3
  * Support any form of activation function
  * When working in real time, the maximum supported neural network parameter size is 5.5MiB to 5.9MiB
  * The maximum supported network parameter size during non-real-time work is (Flash capacity-software volume)




## Routine

### Run face detection

Model download address: [http://dl.sipeed.com/MAIX/MaixPy/model](http://dl.sipeed.com/MAIX/MaixPy/model), download `face_model_at_0x300000.kfpkg`

Complete example: [face_find](https://github.com/sipeed/MaixPy_scripts/tree/master/machine_vision/face_find)

### Running feature map

Model download address: [http://dl.sipeed.com/MAIX/MaixPy/model](http://dl.sipeed.com/MAIX/MaixPy/model), download `face_model_at_0x300000.kfpkg`

The model is an 8bit fixed-point model, about 380KB in size, the layer information is:
```
1 2 :160x120
3 4 5 6 :80x60
7 8 9 10: 40x30
11~16 :20x15
```

```python
import sensor
import image
import lcd
import KPU as kpu
index=3
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
task=kpu.load(0x300000)
img=image.Image()
info=kpu.netinfo(task)
layer=info[index]
w=layer.wo()
h=layer.ho()
num=int(320*240/w/h)
list=[None]*num
x_step=int(320/w)
y_step=int(240/h)
img_lcd=image.Image()
while True:
    img=sensor.snapshot()
    fmap=kpu.forward(task,img,index)
    for i in range(0,num):
        list[i]=kpu.fmap(fmap,i)
    for i in range(0,num):
        list[i].stretch(64,255)
    for i in range(0,num):
        a=img_lcd.draw_image(list[i],((i%x_step)*w,(int(i/x_step))*h))
lcd.display(img_lcd)
   kpu.fmap_free(fmap)
```

-----------------------------


## Module method

### load

Load model from flash or file system

```python
KPU.load(offset, file_path)
```

#### Parameters

The `offset` and `file_path` parameters can only choose one of the two, no keywords are required, just pass the parameters directly

* `offset`: the offset size of the model in the flash. For example, `0xd00000` means the model is burned at the beginning of 13M, and `0x300000` means at the place of `Flash` and `3M`
* `file_path`: The model is the file name in the file system, such as `“/sd/xxx.kmodel”`

##### Back

If it is loaded correctly, the return value will be returned, otherwise an error will be thrown. Please see the error message thrown. In addition, please refer to [here](https://github.com/sipeed/MaixPy/blob/fa3cf2c96353fa698e9386e42be8b3c9cf495114/components/kendryte_sdk/include/sipeed_kpu.h#L6-L23)

If the error code is found to be less than the value of `2000`, the firmware version is too low, and the firmware version needs to be updated

* `kpu_net`: kpu network object

### load_flash

Same function as load method,

```python
kpu.load_flash(model_addr, is_dual_buf, batch_size, spi_speed)
```

#### Parameters

* `model_addr`: Flash addr's preprocessed model burned to the offset address in flash. Note that the model file [description](https://github.com/sipeed/MaixPy_scripts/blob/master/machine_vision/load_big_model/README_ZH.md) needs to be preprocessed here.
* `is_dual_buf`: `0`, single buffer loading, using less RAM and slower speed to dynamically load the model file; `1`, enabling double buffer loading, requires larger RAM, and running speed is relatively fast .
* `batch_size`: When setting `is_dual_buf` to 1, load batch_size needs to be set. The recommended value is `0x4000~0x10000`, which can test the best value of the model. If `is_dual_buf` is 0 then set to 0
* `spi_speed`: When using SPI flash to load the model file, we will temporarily set the flash to high-speed mode and set the required spi clock frequency. The value should be <= 80000000 (the actual frequency, the set value may not be equal to the actual frequency.)

#### return value

* `kpu_net`: kpu network object

### init_yolo2


Pass in initialization parameters for the `yolo2` network model, only used when `yolo2` is used

```python
KPU.init_yolo2(kpu_net, threshold, nms_value, anchor_num, anchor)
```

such as:

```python
import KPU as kpu
task = kpu.load(0x300000)
anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)
kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)
```

#### Parameters

* `kpu_net`: kpu network object, that is, the loaded model object, the return value of `KPU.load()`
* `threshold`: Probability threshold, only if the probability of this object is greater than this value will the output result, value range: [0, 1]
* `nms_value`: box_iou threshold, in order to prevent the same object from being framed in multiple boxes, when two boxes are framed on the same object, the intersection area of ​​the two boxes accounts for the proportion of the total occupied area of ​​the two boxes. When it is less than this value, take the box with the highest probability
* `anchor_num`: the number of anchor points, fixed here as `len(anchors)//2`
* `anchor`: The anchor point parameters are consistent with the model parameters. This parameter of the same model is fixed and bound to the model (it is determined when the model is trained) and cannot be changed to other values.

#### return value

* `success`: `bool` type, success


### deinit

Release the memory occupied by the model and release it immediately, but the variables are still there, you can use the way of `del kpu_net_object` to delete,
In addition, you can also just use `del kpu_net_object` to mark that the object has been deleted. The next time `GC` performs memory collection or manually calls `gc.collect()`, the memory will be automatically released

```python
KPU.deinit(kpu_net)
```

such as:

```python
import KPU as kpu
import gc
task = kpu.load(0x300000)
kpu.deinit(task)
del task
gc.collect()
```

or:

```python
import KPU as kpu
import gc
task = kpu.load(0x300000)
del task
gc.collect()
```


#### Parameters

`kpu_net`: `kpu_net` object returned by `KPU.load()`

#### return value

* `success`: `bool` type, success


### run_yolo2

```python
import KPU as kpu
import image
task = kpu.load(offset or file_path)
anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)
kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)
img = image.Image()
kpu.run_yolo2(task, img) #This is wrong, please refer to the routine
```

#### Parameters

* `kpu_net`: kpu_net object returned by kpu_load
* `image_t`: the image collected from the sensor

##### Back

* `list`: list of kpu_yolo2_find

### forward

Calculate the loaded network model to the specified number of layers, and output the feature map of the target layer

```python
fmap=KPU.forward(kpu_net, img, end_layer)
```

```python
import KPU as kpu
task = kpu.load(offset or file_path)
...
fmap=kpu.forward(task,img, 3)
```

#### Parameters

* `kpu_net`: kpu_net object
* `img`: image `image.Image` object
* `end_layer`: Specify which layer is calculated to the network, the value starts from `0`

##### Back

* `fmap`: Feature map object, containing feature maps of all channels in the current layer


### fmap

Take the specified channel data of the feature map to the `image.Image` object

```python
img=KPU.fmap(fmap, channel)
```

#### Parameters

* `fmap`: Feature map object
* `channel`: Specify the channel number of the feature map, starting from `0`

##### Back

* `img`: The grayscale image generated by the feature image corresponding to the channel, type `image.Image`


### fmap_free

Release feature map object
```python
KPU.fmap_free(fmap)
```

#### Parameters

* `fmap`: Feature map object

##### Back

* None

### netinfo

Get the network structure information of the model

```python
info_list = kpu.netinfo(task)
```

#### Parameters

* `kpu_net`: kpu_net object, `KPU.load()` return value

##### Back

* `info_list`: information list of all layers, including information:
  * `index`: the number of the current layer in the network
  * `wi`: input width
  * `hi`: input height
  * `wo`: output width
  * `ho`: output height
  * `chi`: Number of input channels
  * `cho`: Number of output channels
  * `dw`: Whether it is a depth wise layer
  * `kernel_type`: Convolution kernel type, 0 is 1x1, 1 is 3x3
  * `pool_type`: Pooling type, 0 no pooling; 1: 2x2 max pooling; 2:...
  * `para_size`: the number of bytes of the convolution parameter of the current layer


### set_outputs

```python
success = set_outputs(kput_net, out_idx, width, height, channel)
```

Manually set the shape of the output layer. For the V4 kmodel model converted from nncase v0.2.0,
After `load`, you need to call this function to manually set the output layer shape, V3 model does not need


#### Parameters

* `kpu_net`: kpu_net object
* `out_idx`: The following table of the output layer, starting from `0`, for example, the first output layer is `0`
* `width`: layer width, if it is a one-dimensional output, it is `1`
* `height`: layer height, if it is a one-dimensional output, it is `1`
* `channnel`: The number of layer channels, if it is a one-dimensional output, then here is the length of the one-dimensional output

##### Back

* `success`: Whether the setting is successful, if not, please pay attention to the output prompt information, refer to [error code](https://github.com/sipeed/MaixPy/blob/fa3cf2c96353fa698e9386e42be8b3c9cf495114/components/kendryte_sdk/include/sipeed_kpu. h#L6-L23)


### memtest

Print memory usage, including `GC` memory and system heap memory

* Note that executing this function will automatically execute `gc.collect()` to collect memory once, and then print the remaining memory of `GC`
* The system heap memory is for reference only and may not be accurate. Sometimes it may appear that the memory has been released, but the display is still not released. The actual memory can be allocated to prevail.

```python
KPU.memtest()
```
### face_encode

Quantify the feature map returned by `forward`. For more details, please see: [kpu issue](https://github.com/sipeed/MaixPy/issues/342)

```python
feature = kpu.face_encode(fmap[:])
```

#### Parameters

`fmap[:]`: `list` type, convert the return value of the `forward` function into a list

#### return value

`feature`: `list` type, quantified list

### face_compare

Compare the quantized value returned by face_encode with the entered face

```python
score = kpu.face_compare(record_ftrs[j], feature)
```

#### Parameters

`record_ftrs[j] `: `list` type, with recorded face data
`feature`: `list` type, face data to be compared, return value of `face_encode`

#### return value

`score`: `int` type, compare score (0~100), the higher the score, the greater the similarity
