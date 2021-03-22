---
title: Basic image transformation and common operations
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: basic image transformation and common operations
---


Here is a brief introduction to the basic transformation operations of some frequently used images

Rotate:

```python
img.rotation_corr()
```

Change the image size:

```python
img.resize()
```

For more image transformation, please see [image API](./../../../api_reference/machine_vision/image/image.md)

## Introduction to image buffer

MaixPy has designed two buffers for the image,
* One is the `RGB565` buffer, as the name suggests, is a memory that stores the information of this picture in the format of `RGB565`. Note that the order in the memory is `[pixel 1 RGB, pixel 2 RGB...]`
* The other is the `RGB888` buffer, as the name implies, a memory that stores the information of this picture in the format of `RGB88`. Note that the order in the memory is `[all pixels R, all pixels G, all pixels B]`, we also call it `AI` memory

The main reason for using two memory blocks here is that all image operations of the underlying code and `LCD` display are based on `RGB565`, but `KPU` needs the input of `RGB888`.

```
                   +---------------+
                   |               |
          +--------+ camera(sensor)+-------+
          |        |               |       |
          |        +---------------+       |
          |                                |
+---------v------+                +--------v---------+
|                | img.pix_to_ai()|                  |
|      RGB565    +--------------->+      RGB888      |
|                |                |                  |
+--------+-------+                +------+-----------+
         ^                               |
         |                               |
         |                               v
+--------+----------+             +------+-----------+
|                   |             |                  |
|     image ops     |             |   KPU            |
|                   |             |                  |
+-------------------+             +------------------+

```



When only the camera captures pictures, the hardware will automatically put a copy of the data into the `RGB888` memory area, and the other will not automatically fill the `RGB888` memory block. The software operation will only operate on the `RGB565` memory, and will not automatically update` RGB888`, (because the update takes time) This is worth noting,
This means that every time we change the memory block of `RGB565`, for example, execute `img = img.resize((224, 224))`, if you want `KPU` to use the changed image, you need to execute `img. pix_to_ai()` to manually update the image of `RGB565` to the area of ​​`RGB888`, and then you can call `kpu` related functions for model inference!

The same update in the opposite direction also provides API: `img.ai_to_pix()`, which will update the data in the `RGB888` area to the `RGB565` area


## resize modify resolution

```python
import image
img = image.Image(size=(100, 100))
img2 = img.resize(50, 50)
print(img)
print(img2)
```

## Get and modify pixel value

```python
import image
img = image.Image(size=(10, 10))
print("pixel 0:", img[0], img.get_pixel(0, 0))
img[0] = (255, 0, 0)
img = img.set_pixel(1, 0, (255, 255, 10))
print("after pixel 0 change:", img[0], img[1])
```

The second pixel `B` set here is `10`, and it is actually found to be `8`. This is a normal phenomenon. As mentioned earlier, the storage in the memory uses `RGB565` for storage, so it will Error


## Copy image

```python
import image
img = image.Image(size=(10, 10))
img2 = img.copy()
img2[0] = (255, 0, 0)
print(img[0], img2[0])
```


## Crop image

Also use the `copy` function

```python
import image
img = image.Image(size=(10, 10))
img2 = img.copy(roi=(0, 0, 5, 5))
img2[0] = (255, 0, 0)
print(img)
print(img2)
print(img[0], img2[0])
```


## Convert to bytes object

Convert to `RGB565` string

```python
import image
img = image.Image(size=(10, 10))
img[0] = (255, 0, 0)
img_bytes = img.to_bytes()
print("bytes length: %d bytes[0]: %x%x" %(len(img_bytes), img_bytes[0], img_bytes[1]))
```
The output value here is in the format of `RGB565`, which means that one pixel is stored in two bytes

In addition, you can also compress the image to `JPEG` format first, and then convert it to `bytes`
```python
import image
img = image.Image(size=(10, 10))
img = img.compressed(quality=20)
jpeg_bytes = img.to_bytes()
print("bytes length: %d bytes[0]: %x%x" %(len(jpeg_bytes), jpeg_bytes[0], jpeg_bytes[1]))
```

Using the `compressed` function here will not modify the original image, using the `compress()` function will modify the original image, but if the compressed size is larger than the original image, it will fail



## Convert to grayscale image

```python
img = img.to_grayscale(copy=False)
```

Here the `copy` parameter means whether to re-apply for a piece of memory without modifying the original image

## Convert to RGB565 color image

Convert to a color image, note that only the format has become a color image, the picture is not a color image, if you need to convert a gray image to a color image, use `img.to_rainbow()`

```python
img = img.to_rgb565(copy=True)
```

Here the `copy` parameter means whether to re-apply for a piece of memory without modifying the original image
If the original image is grayscale, it must be `True`

## Convert to color picture

```python
img = img.to_rainbow(copy=True)
```

Here the `copy` parameter means whether to re-apply for a piece of memory without modifying the original image
If the original image is grayscale, it must be `True`

## Save to file system

```python
img.save("/sd/test.jpg", quality=95)
img.save("/sd/test.bmp")
```


## Rotate

```python
img.rotation_corr([x_rotation=0.0[, y_rotation=0.0[, z_rotation=0.0[, x_translation=0.0[, y_translation=0.0[, zoom=1.0]]]]]])
```

The brackets are optional parameters, that is, which axis to rotate along a certain angle. If this function is not available in the firmware of the `minimum` version, the full version of the firmware can be used
