---
title: basic operations of the image
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: basic operations of images
---


## Coordinates

### Get/Set pixels

We can get the value of a pixel through the image.get_pixel(x, y) method.

-image.get_pixel(x, y)

    For grayscale image: Return the grayscale value of (x,y) coordinates.

    For color images: return the (r, g, b) tuple of (x, y) coordinates.

Similarly, we can use the image.set_pixel(x, y, pixel) method to set the value of a pixel.

-image.set_pixel(x, y, pixel)

    For grayscale image: Set the grayscale value of (x,y) coordinates.

    For color images: Set the (r, g, b) value of (x, y) coordinates.

For example:
```python
img = sensor.snapshot()
img.get_pixel(10,10)
img.set_pixcel(10,10,(255,0,0))#Set the pixel of coordinate (10,10) to red (255,0,0)
```

### Get the width and height of the image

-image.width()

    Returns the width of the image (pixels)

-image.height()

    Returns the height of the image (pixels)

-image.format()

    The grayscale image will return sensor.GRAYSCALE, and the color image will return sensor.RGB565.

-image.size()

    Returns the size of the image (byte)

### Image operation

-image.invert()

    Inversely, for a binarized image, 0 (black) becomes 1 (white), and 1 (white) becomes 0 (black).

    Note:
    The image can be another image object, or an image object read in from a (bmp/pgm/ppm) file.
    Both images must be the same size and type (grayscale image/color image).

-image.nand(image)

    Perform NAND operation with another picture.

-image.nor(image)

    Perform a NOR operation with another picture.

-image.xor(image)

    Perform an exclusive OR (XOR) operation with another picture.

-image.xnor(image)

    Perform XNOR operation with another image.

-image.difference(image)

    Subtract another picture from this picture. For example, for each pixel of each channel, subtract the absolute value operation. This function is often used for motion detection.
