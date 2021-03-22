---
title: image (machine vision)
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: image (machine vision)
---


Ported to `openmv`, same function as `openmv`

## Routine

### Routine 1: Find green

```python
import sensor
import image
import lcd
import time
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
green_threshold = (0, 80, -70, -10, -0, 30)
while True:
img=sensor.snapshot()
blobs = img.find_blobs([green_threshold])
if blobs:
for b in blobs:
tmp=img.draw_rectangle(b[0:4])
tmp=img.draw_cross(b[5], b[6])
c=img.get_pixel(b[5], b[6])
lcd.display(img)
```

### Example 2: Display fps

```python
import sensor
import image
import lcd
import time

clock = time.clock()
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
sensor.skip_frames(30)
while True:
    clock.tick()
    img = sensor.snapshot()
    fps =clock.fps()
    img.draw_string(2,2, ("%2.1ffps" %(fps)), color=(0,128,0), scale=2)
    lcd.display(img)
```


### Example 3: Scan the QR code

```python
import sensor
import image
import lcd
import time

clock = time.clock()
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(1)
sensor.run(1)
sensor.skip_frames(30)
while True:
    clock.tick()
    img = sensor.snapshot()
    res = img.find_qrcodes()
    fps =clock.fps()
    if len(res)> 0:
        img.draw_string(2,2, res[0].payload(), color=(0,128,0), scale=2)
        print(res[0].payload())
    lcd.display(img)

```

> If a lens is used, the picture will be distorted and the picture needs to be corrected
> Use the `lens_corr` function to correct, such as `2.8`mm, `img.lens_corr(1.8)`




## Function

Function can also press `Ctrl+F` on this page and use the browser's search function to search `image.` to mark the function

### image.rgb_to_lab(rgb_tuple)

Return the tuple of RGB888 format rgb_tuple (r, g, b) corresponding to the tuple (l, a, b) of LAB format.

> RGB888 means 8 bits each for red, green and blue (0-255). In LAB, the range of L is 0-100, and the range of a/b is -128 to 127.

### image.lab_to_rgb(lab_tuple)

Return the tuple in LAB format lab_tuple (l, a, b) and the corresponding tuple (r, g, b) in RGB888 format.

> RGB888 means 8 bits each for red, green and blue (0-255). In LAB, the range of L is 0-100, and the range of a/b is -128 to 127.

### image.rgb_to_grayscale(rgb_tuple)

Returns the gray value corresponding to the tuple rgb_tuple (r, g, b) in RGB888 format.

> RGB888 means 8 bits each for red, green and blue (0-255). The gray value ranges from 0-255.

### image.grayscale_to_rgb(g_value)

Returns the tuple (r, g, b) in RGB888 format corresponding to the gray value g_value.

> RGB888 means 8 bits each for red, green and blue (0-255). The gray value ranges from 0-255.

### image.load_decriptor(path)

Load a descriptor object from the disk.

path is the path where the descriptor file is saved.

### image.save_descriptor(path, descriptor)

Save the descriptor object descriptor to disk.

path is the path where the descriptor file is saved.

### image.match_descriptor(descritor0, descriptor1[, threshold=70[, filter_outliers=False]])

For LBP descriptors, this function returns an integer that reflects the difference between the two descriptors. This distance measurement is particularly necessary. This distance is a measure of similarity. The closer this measure is to 0, the better the matching of LBPF feature points.

For ORB descriptors, this function returns a kptmatch object. See above.

threshold is used to filter ambiguous matching services for ORB keys.
A lower threshold value will be closely tied to the key point matching algorithm. The threshold value is between 0-100 (int). The default value is 70.

filter_outliers is used to filter outliers for ORB key points. Feature points allow users to increase the threshold value. The default setting is False.

## HaarCascade class-feature descriptor

Haar Cascade feature descriptors are used in the `image.find_features()` method. It has no methods for users to call.

### Constructor

class image.HaarCascade(path[, stages=Auto])

Load a Haar Cascade from a Haar Cascade binary file (format suitable for OpenMV Cam). If you pass the "frontalface" string instead of a path, this constructor will load a built-in frontalface Haar Cascade into memory. In addition, you can also load Haar Cascade into memory through "eye". Finally, this method returns the loaded Haar Cascade object, which is used to use image.find_features().

The default value of stages is the number of stages in Haar Cascade. However, you can specify a lower value to speed up the running of the feature detector, which of course will bring a higher false alarm rate.

> You can make your own Haar Cascades to work with your OpenMV Cam. First, use Google to search for "<thing> Haar Cascade" to check if someone has made an OpenCV Haar Cascade for the object you want to detect. If not, then you need to do it yourself (huge workload). For how to make your own Haar Cascade, see here For how to convert OpenCV Haar Cascades into a mode that your OpenMV Cam can read, see this script

Q: What is Haar Cascade?

Answer: Haar Cascade is a series of comparative checks to determine whether an object is present in the image. This series of comparative inspections is divided into multiple stages, and the operation of the latter stage is based on the completion of the previous stage. Contrast checking is not complicated, but a process like checking whether the center of the image is slightly more vertical than the edges. Large-scale inspections are carried out first in the early stage, and more and smaller areas are inspected in the later stage.

Q: How are Haar Cascades made?

Answer: Haar Cascades trains the generator algorithm through positive and negative images. For example, use hundreds of pictures containing cats (which have been marked as containing cats) and hundreds of pictures that do not contain cats (which have been marked differently) to train this generation algorithm. This generation algorithm will finally generate a Haar Cascades for detecting cats.

## Similarity Class-Similarity Object

The similarity object is returned by `image.get_similarity`.

### Constructor

class image.similarity

Please call the image.get_similarity() function to create this object.

#### Method

##### similarity.mean()
Returns the mean value of the similarity difference of 8x8 pixel block structure. The range is [-1/+1], where -1 is completely different and +1 is completely the same.

You can also get this value by index [0].

##### similarity.stdev()
Returns the standard deviation of the similarity difference of the 8x8 pixel block structure.

You can also get this value via index [1].

##### similarity.min()
Returns the minimum value of the similarity difference of the 8x8 pixel block structure. Where -1 is completely different and +1 is completely the same.

You can also get this value via index [2].

> By looking at this value, you can quickly determine whether any 8x8 pixel blocks between the two images are very different, that is, far below +1.

##### similarity.max()

Returns the minimum value of the similarity difference of the 8x8 pixel block structure. Where -1 is completely different and +1 is completely the same.

You can also get this value through index [3].

> By looking at this value, you can quickly determine whether any 8x8 pixel blocks between the two images are the same. That is much larger than -1.

## Histogram class-histogram object

The histogram object is returned by `image.get_histogram`. The grayscale histogram has a channel that contains multiple bins. All binaries are normalized so that their sum is 1. RGB565 has three channels containing multiple binary. All binaries are normalized so that their sum is 1.

### Constructor

class image.histogram

Please call the `image.get_histogram()` function to create this object.

### Method

#### histogram.bins()

Returns a list of floating point numbers in the gray histogram. You can also get this value by index [0].

#### histogram.l_bins()

Returns the list of floating point numbers of the L channel of the RGB565 histogram LAB. You can also get this value by index [0].

#### histogram.a_bins()

Returns the list of floating point numbers of the A channel of the RGB565 histogram LAB. You can also get this value via index [1].

#### histogram.b_bins()

Returns the list of floating point numbers of channel B of RGB565 histogram LAB. You can also get this value via index [2].
#### histogram.get_percentile(percentile)

Calculate the CDF of the histogram channel and return a value of the histogram passed in percentile (0.0-1.0) (floating point number).

Therefore, if you pass in 0.1, the method will tell you which binary will make the accumulator cross 0.1 when it is added to the accumulator.

This is very effective for determining the minimum value (0.1) and max (0.9) of the color distribution when there is no anomalous utility to spoil your adaptive color tracking results.

#### histogram.get_threhsold()

Use Otsu’s method to calculate the optimal threshold, dividing each channel of the histogram into two halves. This method returns an image.threshold object. This method is particularly useful for determining the optimal image.binary() threshold.

#### histogram.get_statistics()

Calculate the average, median, mode, standard deviation, minimum, maximum, lower quartile, and upper quartile of each color channel in the histogram, and return a statistics object. You can also use histogram.statistics() and histogram.get_stats() as aliases for this method.





## Percentile class-percentage value object

The percentage value object is returned by `histogram.get_percentile`. The gray percentage value has one channel. Do not use l_*, a_* or b_* methods. The RGB565 percentage value has three channels. Use the l_*, a_* and b_* methods.

### Constructor

class image.percentile

Please call the histogram.get_percentile() function to create this object.

### Method

#### percentile.value()

Returns the gray percentage value (the value range is 0-255).

You can also get this value by index [0].

#### percentile.l_value()

Returns the percentage value of the L channel of RGB565 LAB (value range is 0-100).

You can also get this value by index [0].

#### percentile.a_value()

Returns the percentage value of the A channel of RGB565 LAB (the value range is -128-127).

You can also get this value via index [1].

#### percentile.b_value()

Returns the percentage value of the B channel of RGB565 LAB (the value range is -128-127).

You can also get this value via index [2].

## Threhsold Class-Threshold Object

The threshold object is returned by histogram.get_threshold.

Grayscale images have one channel. There are no l_*, a_*, and b_* methods.

The RGB565 threshold has three channels. Use l_*, a_*, and b_* methods.

### Constructor

class image.threshold

Please call the histogram.get_threshold() function to create this object.

#### Method

#### threhsold.value()

Returns the threshold of the grayscale image (between 0 and 255).

You can also get this value by index [0].

#### threhsold.l_value()

Return the L threshold (between 0 and 100) in the RGB565 image LAB.

You can also get this value by index [0].

#### threhsold.a_value()

Return the A threshold (between -128 and 127) in the RGB565 image LAB.

You can also get this value via index [1].

#### threhsold.b_value()

Return the B threshold (between -128 and 127) in the RGB565 image LAB.

You can also get this value via index [2].

## class Statistics – Statistical data object

The statistical data object is returned by histogram.get_statistics or image.get_statistics.

The grayscale statistics have one channel, using methods other than l_*, a_* or b_*.

The RGB565 percentage value has three channels. Use the l_*, a_* and b_* methods.

### Constructor

class image.statistics
Please call histogram.get_statistics() or image.get_statistics() function to create this object.

### Method

#### statistics.mean()

Returns the average gray value (0-255) (int).

You can also get this value by index [0].

#### statistics.median()

Returns the median gray value (0-255) (int).

You can also get this value via index [1].

#### statistics.mode()

Returns the gray mode value (0-255) (int).

You can also get this value via index [2].

#### statistics.stdev()

Returns the gray standard deviation (0-255) (int).

You can also get this value through index [3].

#### statistics.min()

Returns the minimum value of gray scale (0-255) (int).

You can also get this value via index [4].

#### statistics.max()

Returns the maximum gray value (0-255) (int).

You can also get this value via index [5].

#### statistics.lq()

Returns the quarter value (0-255) (int) in grayscale.

You can also get this value via index [6].

#### statistics.uq()

Returns the quarter value of the gray scale (0-255) (int).

You can also get this value via index [7].

#### statistics.l_mean()

Returns the mean value of L (0-255) (int) in RGB5656 LAB.

You can also get this value by index [0].

#### statistics.l_median()

Returns the median (0-255) (int) of L in RGB5656 LAB.

You can also get this value via index [1].

#### statistics.l_mode()

Returns the mode (0-255) (int) of L in RGB5656 LAB.

You can also get this value via index [2].

#### statistics.l_stdev()

Returns the standard deviation value of L in RGB5656 LAB (0-255) (int).

You can also get this value through index [3].

#### statistics.l_min()

Returns the minimum value of L in RGB5656 LAB (0-255) (int).

You can also get this value via index [4].

#### statistics.l_max()

Returns the maximum value of L in RGB5656 LAB (0-255) (int).

You can also get this value via index [5].

#### statistics.l_lq()

Returns the lower quartile of L in RGB5656 LAB (0-255) (int).

You can also get this value via index [6].

#### statistics.l_uq()

Returns the upper quartile (0-255) (int) of L in RGB5656 LAB.

You can also get this value via index [7].

#### statistics.a_mean()

Returns the mean value (0-255) (int) of A in RGB5656 LAB.

You can also get this value through index [8].

#### statistics.a_median()

Returns the median value (0-255) (int) of A in RGB5656 LAB.

You can also get this value via index [9].

#### statistics.a_mode()

Returns the mode (0-255) (int) of A in RGB5656 LAB.

You can also get this value via index [10].

#### statistics.a_stdev()

Returns the standard deviation value (0-255) (int) of A in RGB5656 LAB.

You can also get this value through the index [11].

#### statistics.a_min()

Returns the minimum value of A in RGB5656 LAB (0-255) (int).

You can also get this value through the index [12].

#### statistics.a_max()

Returns the maximum value of A (0-255) (int) in RGB5656 LAB.

You can also get this value through the index [13].

#### statistics.a_lq()

Returns the lower quartile (0-255) (int) of A in RGB5656 LAB.

You can also get this value through the index [14].

#### statistics.a_uq()

Returns the upper quartile (0-255) (int) of A in RGB5656 LAB.

You can also get this value via index [15].

#### statistics.b_mean()

Returns the mean value of B in RGB5656 LAB (0-255) (int).

You can also get this value via index [16].

#### statistics.b_median()

Returns the median (0-255) (int) of B in RGB5656 LAB.

You can also get this value via index [17].

#### statistics.b_mode()

Returns the mode (0-255) (int) of B in RGB5656 LAB.

You can also get this value through the index [18].

#### statistics.b_stdev()

Returns the standard deviation of B in RGB5656 LAB (0-255) (int).

You can also get this value through index [19].

#### statistics.b_min()

Returns the minimum value (0-255) (int) of B in RGB5656 LAB.

You can also get this value via index [20].

#### statistics.b_max()

Returns the maximum value of B in RGB5656 LAB (0-255) (int).

You can also get this value through the index [21].

#### statistics.b_lq()

Returns the lower quartile of B in RGB5656 LAB (0-255) (int).

You can also get this value through the index [22].

#### statistics.b_uq()

Returns the upper quartile (0-255) (int) of B in RGB5656 LAB.

You can also get this value through the index [23].

## Blob class-color block object

The color block object is returned by `image.find_blobs`.

### Constructor

class image.blob

Please call the image.find_blobs() function to create this object.

### Method

#### blob.rect()

Returns a rectangular tuple (x, y, w, h), which is used in other image methods such as image.draw_rectangle of the color block bounding box.

#### blob.x()

Returns the x coordinate (int) of the bounding box of the color patch.

You can also get this value by index [0].

#### blob.y()
Returns the y coordinate (int) of the bounding box of the color patch.

You can also get this value via index [1].

#### blob.w()

Returns the w coordinate (int) of the bounding box of the color patch.

You can also get this value via index [2].

#### blob.h()

Returns the h coordinate (int) of the bounding box of the color patch.

You can also get this value through index [3].

#### blob.pixels()

Returns the number of pixels that are part of the color block (int).

You can also get this value via index [4].

#### blob.cx()

Returns the center x position of the color block (int).

You can also get this value via index [5].
#### blob.cy()

Returns the center x position of the color block (int).

You can also get this value via index [6].

#### blob.rotation()

Returns the rotation of the color block (unit: radians). If the color block resembles a pencil or pen, then this value is the only value between 0-180. If the color block is round, then this value has no effect. If this color block has no symmetry at all, you can only get a 0-360 degree rotation.

You can also get this value via index [7].

#### blob.code()

Returns a 16-bit binary number, where one bit is set for each color threshold, which is part of the color block. For example, if you use image.find_blobs to find three color thresholds, this color block can be set to 0/1/2 bits. Note: Unless you call image.find_blobs with merge=True, you can only set one bit per color block. Then multiple color blocks with different color thresholds can be merged together. You can also use this method and multiple thresholds to implement color code tracking.

You can also get this value through index [8].

#### blob.count()

Returns the number of multiple color blocks merged into this color block. Only when you call image.find_blobs with merge=True, this number is not 1.

You can also get this value via index [9].

#### blob.area()

Return the border area around the color block (w * h)

#### blob.density()

Returns the density ratio of this color patch. This is the number of pixels in the bounding box area of ​​the color block. In general, a lower density ratio means that the object is not locked well.

## Line class-line object

The line object is returned by `image.find_lines`, `image.find_line_segments` or `image.get_regression`.

### Constructor

class image.line

Please call image.find_lines(), image.find_line_segments(), or image.get_regression() function to create this object.

### Method

#### line.line()

Return a straight line tuple (x1, y1, x2, y2) for use in other image methods such as image.draw_line.

#### line.x1()

Returns the x coordinate component of the p1 vertex of the line.

You can also get this value by index [0].

#### line.y1()

Returns the p1 y component of the line.

You can also get this value via index [1].

#### line.x2()

Returns the p2 x component of the line.

You can also get this value via index [2].

#### line.y2()

Returns the p2 y component of the line.

You can also get this value through index [3].

#### line.length()

The length of the return line is sqrt(((x2-x1)^2) + ((y2-y1)^2).

You can also get this value via index [4].

#### line.magnitude()

Returns the length of the straight line after Hough transformation.

You can also get this value via index [5].

#### line.theta()

Returns the angle of the straight line after Hough transformation (0-179 degrees).

You can also get this value via index [7].

#### line.rho()

Returns the p-value of the straight line after Hough transform.

You can also get this value through index [8].

## Circle class-round object

The circular object is returned by `image.find_circles`.

### Constructor

class image.circle

Please call the image.find_circles() function to create this object.

### Method

#### circle.x()

Returns the x position of the circle.

You can also get this value by index [0].

#### circle.y()

Returns the y position of the circle.

You can also get this value via index [1].

#### circle.r()

Returns the radius of the circle.

You can also get this value via index [2].

#### circle.magnitude()

Returns the size of the circle.

You can also get this value through index [3].

## Rect Class-Rectangle Object

The rectangle object is returned by `image.find_rects`.

### Constructor

class image.rect

Please call the image.find_rects() function to create this object.

### Method

#### rect.corners()

Returns a list of four tuples (x, y) consisting of the four corners of the rectangular object. The four corners are usually returned in clockwise order starting from the upper left corner.

#### rect.rect()

Returns a rectangle tuple (x, y, w, h), used in other image methods such as image.draw_rectangle of the bounding box of the rectangle.

#### rect.x()

Returns the x position of the upper left corner of the rectangle.

You can also get this value by index [0].

#### rect.y()

Returns the y position of the upper left corner of the rectangle.

You can also get this value via index [1].

#### rect.w()

Returns the width of the rectangle.

You can also get this value via index [2].

#### rect.h()

Returns the height of the rectangle.

You can also get this value through index [3].

#### rect.magnitude()

Returns the size of the rectangle.

You can also get this value via index [4].

## QRCode class-QR code object

The QR code object is returned by `image.find_qrcodes`.

### Constructor

class image.qrcode

Please call the image.find_qrcodes() function to create this object.

### Method

#### qrcode.corners()

Returns a list of four tuples (x, y) consisting of the four corners of the object. The four corners are usually returned in clockwise order starting from the upper left corner.

#### qrcode.rect()

Returns a rectangular tuple (x, y, w, h), used in other image methods such as image.draw_rectangle of the bounding box of the QR code.

#### qrcode.x()

Returns the x coordinate (int) of the bounding box of the QR code.

You can also get this value by index [0].

#### qrcode.y()

Returns the y coordinate (int) of the bounding box of the QR code.

You can also get this value via index [1].

#### qrcode.w()

Returns the w coordinate (int) of the bounding box of the QR code.

You can also get this value via index [2].

#### qrcode.h()

Returns the h coordinate (int) of the bounding box of the QR code.

You can also get this value through index [3].

#### qrcode.payload()

Returns the string of the QR code payload, such as URL.

You can also get this value via index [4].

#### qrcode.version()

Returns the version number (int) of the QR code.

You can also get this value via index [5].

#### qrcode.ecc_level()

Returns the ECC level of the QR code (int).

You can also get this value via index [6].

#### qrcode.mask()

Returns the mask (int) of the QR code.

You can also get this value via index [7].

#### qrcode.data_type()

Returns the data type of the QR code.

You can also get this value through index [8].

#### qrcode.eci()

Returns the ECI of the QR code. ECI stores the code of the data bytes stored in the QR code. If you want to process a QR code that contains more than standard ASCII text, you need to check this value.

You can also get this value via index [9].

#### qrcode.is_numeric()

If the data type of the QR code is digital, it returns True.

#### qrcode.is_alphanumeric()

If the data type of the QR code is alphanumeric, it returns True.

#### qrcode.is_binary()

If the data type of the QR code is binary, it returns True. If you are serious about handling all types of text, you need to check whether eci is True to determine the text encoding of the data. Usually it is just standard ASCII, but it may also be UTF8 with two-byte characters.

#### qrcode.is_kanji()

If the data type of the QR code is Kanji, it returns True. After setting it to True, you need to decode the string yourself, because each character of the Kanji is 10 digits, and MicroPython does not support parsing this type of text.

## AprilTag Class – AprilTag Object

The AprilTag object is returned by `image.find_apriltags`.

### Constructor

class image.apriltag

Please call the image.find_apriltags() function to create this object.

### Method

#### apriltag.corners()

Returns a list of four tuples (x, y) consisting of the four corners of the object. The four corners are usually returned in clockwise order starting from the upper left corner.

#### apriltag.rect()


Return a rectangular tuple (x, y, w, h), used in other image methods such as image.draw_rectangle of AprilTag bounding box.

#### apriltag.x()

Returns the x coordinate (int) of the AprilTag bounding box.

You can also get this value by index [0].

#### apriltag.y()

Returns the y coordinate (int) of the bounding box of AprilTag.

You can also get this value via index [1].

#### apriltag.w()

Returns the w coordinate (int) of the bounding box of AprilTag.

You can also get this value via index [2].

#### apriltag.h()

Returns the h coordinate (int) of the bounding box of AprilTag.

You can also get this value through index [3].

#### apriltag.id()

Returns the numeric ID of AprilTag.

TAG16H5 -> 0 to 29
TAG25H7 -> 0 to 241
TAG25H9 -> 0 to 34
TAG36H10 -> 0 to 2319
TAG36H11 -> 0 to 586
ARTOOLKIT -> 0 to 511
You can also get this value via index [4].

#### apriltag.family()

Return to AprilTag's digital home.

image.TAG16H5
image.TAG25H7
image.TAG25H9
image.TAG36H10
image.TAG36H11
image.ARTOOLKIT
You can also get this value via index [5].

#### apriltag.cx()

Returns the center x position (int) of AprilTag.

You can also get this value via index [6].

#### apriltag.cy()

Returns the center y position (int) of AprilTag.

You can also get this value via index [7].

#### apriltag.rotation()

Returns the curl of AprilTag in radians (int).

You can also get this value through index [8].

#### apriltag.decision_margin()

Return the color saturation of AprilTag matching (value 0.0-1.0), where 1.0 is the best.

You can also get this value via index [9].

#### apriltag.hamming()

Returns the acceptable digital error value of AprilTag.

TAG16H5 -> can accept up to 0 bit errors
TAG25H7 -> can accept up to 1 bit error
TAG25H9 -> Accept up to 3 errors
TAG36H10 -> can accept up to 3 errors
TAG36H11 -> can accept up to 4 errors
ARTOOLKIT -> can accept up to 0 errors
You can also get this value via index [10].
#### apriltag.goodness()

Returns the color saturation of the AprilTag image (value 0.0-1.0), where 1.0 is the best.

> Currently this value is usually 0.0. In the future, we can enable a function called "tag refinement" to realize the detection of smaller AprilTags. However, this feature now reduces the frame rate below 1 FPS.

You can also get this value through the index [11].

#### apriltag.x_translation()

Returns the transformation in the x direction from the camera. The unit of the distance is unknown.

This method is useful for determining the position of AprilTag far away from the camera. However, factors such as the size of AprilTag and the lens you use will affect the determination of the attribution of the X unit. For ease of use, we recommend that you use a lookup table to convert the output of this method into useful information for your application.

Note: The direction here is from left to right.

You can also get this value through the index [12].

#### apriltag.y_translation()

Returns the transformation in the y direction from the camera. The unit of the distance is unknown.

This method is useful for determining the position of AprilTag far away from the camera. However, the size of the AprilTag and the lens you use will affect the determination of the Y unit. For ease of use, we recommend that you use a lookup table to convert the output of this method into useful information for your application.

Note: The direction here is from top to bottom.

You can also get this value through the index [13].

#### apriltag.z_translation()

Returns the transformation in the z direction from the camera. The unit of the distance is unknown.

This method is useful for determining the position of AprilTag far away from the camera. However, the size of the AprilTag and the lens you use will affect the determination of the Z unit. For ease of use, we recommend that you use a lookup table to convert the output of this method into useful information for your application.

Note: The direction here is from front to back.

You can also get this value through the index [14].

#### apriltag.x_rotation()

Returns the rotation of AprilTag on the X plane in radians. Example: Looking at AprilTag, move the camera from left to right.

You can also get this value via index [15].

#### apriltag.y_rotation()

Returns the rotation of AprilTag in radians on the Y plane. Example: Visually observe AprilTag and move the camera from top to bottom.

You can also get this value via index [16].

#### apriltag.z_rotation()

Returns the rotation of the AprilTag in radians on the Z plane. Example: Look at AprilTag and rotate the camera.

Note: This is just a renamed version of apriltag.rotation().

You can also get this value via index [17].

## DataMatrix Class-Data Matrix Object

The data matrix object is returned by `image.find_datamatrices`.

## Constructor

class image.datamatrix

Please call the image.find_datamatrices() function to create this object.

### Method

#### datamatrix.corners()

Returns a list of four tuples (x, y) consisting of the four corners of the object. The four corners are usually returned in clockwise order starting from the upper left corner.

#### datamatrix.rect()

Return a rectangular tuple (x, y, w, h), used in other image methods such as image.draw_rectangle of the bounding box of the data matrix.

#### datamatrix.x()

Returns the x coordinate (int) of the bounding box of the data matrix.

You can also get this value by index [0].

#### datamatrix.y()

Returns the y coordinate (int) of the bounding box of the data matrix.

You can also get this value via index [1].

#### datamatrix.w()

Returns the w width of the bounding box of the data matrix.

You can also get this value via index [2].

#### datamatrix.h()

Returns the h height of the bounding box of the data matrix.

You can also get this value through index [3].

#### datamatrix.payload()

Returns the string of the payload of the data matrix. Example: string.

You can also get this value via index [4].

#### datamatrix.rotation()

Returns the curl (floating point number) of the data matrix in radians.

You can also get this value via index [5].

#### datamatrix.rows()

Returns the number of rows of the data matrix (int).

You can also get this value via index [6].

#### datamatrix.columns()

Returns the number of columns of the data matrix (int).

You can also get this value via index [7].

#### datamatrix.capacity()

Returns the number of characters that this data matrix can hold.

You can also get this value through index [8].

#### datamatrix.padding()

Returns the number of unused characters in this data matrix.

You can also get this value via index [9].

## BarCode Class-Barcode Object

The barcode object is returned by image.find_barcodes.

## Constructor

class image.barcode

Please call the image.find_barcodes() function to create this object.

### Method

#### barcode.corners()

Returns a list of four tuples (x, y) consisting of the four corners of the object. The four corners are usually returned in clockwise order starting from the upper left corner.

#### barcode.rect()

Return a rectangular tuple (x, y, w, h), used in other image methods such as image.draw_rectangle of the bounding box of the data matrix.

#### barcode.x()

Returns the x coordinate (int) of the bounding box of the barcode.

You can also get this value by index [0].

#### barcode.y()

Returns the y coordinate (int) of the bounding box of the barcode.

You can also get this value via index [1].

#### barcode.w()

Returns the w width (int) of the bounding box of the barcode.

You can also get this value via index [2].

#### barcode.h()

Returns the h height (int) of the bounding box of the barcode.

You can also get this value through index [3].

#### barcode.payload()

Returns the string of the payload of the barcode. Example: Quantity.

You can also get this value via index [4].

#### barcode.type()

Returns the enumeration type (int) of the barcode.

You can also get this value via index [5].

image.EAN2
image.EAN5
image.EAN8
image.UPCE
image.ISBN10
image.UPCA
image.EAN13
image.ISBN13
image.I25
image.DATABAR
image.DATABAR_EXP
image.CODABAR
image.CODE39
image.PDF417-To be enabled in the future (e.g. not yet available for normal use).
image.CODE93
image.CODE128

#### barcode.rotation()

Returns the curl (floating point number) of the barcode in radians.

You can also get this value via index [6].

#### barcode.quality()

Returns the number of times the barcode was detected in the image (int).

When scanning a barcode, each new scan line can decode the same barcode. Each time this process is performed, the value of the barcode will increase accordingly.

You can also get this value via index [7].

## Displacement class-displacement object

The displacement object is returned by image.find_displacement.

### Constructor

class image.displacement

Please call the image.find_displacement() function to create this object.

### Method

#### displacement.x_translation()

Returns the x translation pixel between two images. This is a precise sub-pixel, so it is a floating point number.

You can also get this value by index [0].

#### displacement.y_translation()

Returns the y translation pixel between two images. This is a precise sub-pixel, so it is a floating point number.

You can also get this value via index [1].

#### displacement.rotation()

Returns the z-shift pixel between two images. This is a precise sub-pixel, so it is a floating point number.

You can also get this value via index [2].

#### displacement.scale()

Returns the arc of rotation between two images.

You can also get this value through index [3].

#### displacement.response()

Returns the quality of the result of displacement matching between two images. Range 0-1. Displacement objects with a response less than 0.1 may be noise.

You can also get this value via index [4].

## Kptmatch class – feature point object

The feature point object is returned by `image.match_descriptor`.

### Constructor

class image.kptmatch

Please call the image.match_descriptor() function to create this object.

### Method

#### kptmatch.rect()

Return a rectangular tuple (x, y, w, h), used in other image methods such as image.draw_rectangle of the bounding box of the feature point.

#### kptmatch.cx()

Returns the center x position of the feature point (int).

You can also get this value by index [0].

#### kptmatch.cy()

Returns the center y position (int) of the feature point.

You can also get this value via index [1].

#### kptmatch.x()

Returns the x coordinate (int) of the bounding box of the feature point.

You can also get this value via index [2].

#### kptmatch.y()

Returns the y coordinate (int) of the bounding box of the feature point.

You can also get this value through index [3].

#### kptmatch.w()

Returns the w width (int) of the bounding box of the feature point.

You can also get this value via index [4].

#### kptmatch.h()

Returns the h height (int) of the bounding box of the feature point.

You can also get this value via index [5].

#### kptmatch.count()

Returns the number of matched feature points (int).

You can also get this value via index [6].

#### kptmatch.theta()

Returns the curl of the estimated feature point (int).

You can also get this value via index [7].

#### kptmatch.match()

Returns a list of (x, y) tuples matching key points.

You can also get this value through index [8].

## ImageWriter class-ImageWriter object

The ImageWriter object allows you to quickly write uncompressed images to disk.

### Constructor

class image.ImageWriter(path)

By creating an ImageWriter object, you can write uncompressed images to disk in the simple file format used for OpenMV Cams. Then the uncompressed image can be re-read using ImageReader.

### Method

#### imagewriter.size()

Returns the size of the file being written.

#### imagewriter.add_frame(img)

Write an image to disk. Because the image is not compressed, it executes quickly, but it takes up a lot of disk space.

#### imagewriter.close()

Close the image stream file. You must close the file or the file will be damaged.

## ImageReader class – ImageReader object

The ImageReader object allows you to quickly read uncompressed images from disk.
### Constructor

class image.ImageReader(path)

Create an ImageReader object to play back the image data written by the ImageWriter object. The frames played back by the ImageWriter object will be played back at the same FPS as when they were written to disk.

### Method

#### imagereader.size()

Returns the size of the file being read.

imagereader.next_frame([copy_to_fb=True, loop=True])
Return the image object from the file written by ImageWriter. If copy_to_fb is True, the image object will be directly loaded into the frame buffer. Otherwise, the image object will be put into the heap. Note: Unless the image is small, the heap may not have enough space to store the image object. If loop is True, playback will restart after the last image of the stream is read. Otherwise, this method will return None after all frames have been read.

Note: imagereader.next_frame tries to limit the playback speed by pausing the playback after reading the frame to match the frame recording speed. Otherwise, this method will quickly read and play all images at a speed of 200+FPS.

#### imagereader.close()

Close the file being read. You need to do this to prevent damage to the imagereader object. But because it is a read-only file, the file will not be damaged when it is not closed.

## Image class-image objects

Image objects are the basic objects of machine vision operations.

### Constructor

class image.Image(path[, copy_to_fb=False])

Create a new image object from the file in path.

Support image files in bmp/pgm/ppm/jpg/jpeg format.

If copy_to_fb is True, the image will be directly loaded into the frame buffer, and you can load a large image. If False, the image will be loaded into the MicroPython heap, which is much smaller than the frame buffer.

In OpenMV Cam M4, if copy_to_fb is False, you should try to keep the image size below 8KB. If True, the image can be up to 160KB.
In OpenMV Cam M7, if copy_to_fb is False, you should try to keep the image size below 16KB. If True, the maximum image size can be 320KB.
The image supports the "[]" notation. Let image[index] = 8/16-bit value to allocate image pixels or image[index] and get an image pixel. If it is a 16-bit RGB565 grayscale image for RGB image, this pixel is 8 Bit.

For JPEG images, "[]" allows you to access JPEG image color patches in the form of a compressed section array. Since the JPEG image is a compressed byte stream, the reading and writing of the data group is opaque.

The image also supports read buffer operation. You can treat the image as a section array object and input the image into all types of MicroPython functions. If you want to transmit an image, you can pass it to the UART/SPI/I2C write function, which can realize automatic transmission.

### Method

#### image.width()

Returns the width of the image in pixels.

#### image.height()

Returns the height of the image in pixels.

#### image.format()

Return sensor.GRAYSCALE for grayscale images, sensor.RGB565 for RGB images, and sensor.JPEG for JPEG images.

#### image.size()

Returns the size of the image in bytes.

#### image.get_pixel(x, y[, rgbtuple])

Grayscale image: returns the grayscale pixel value at (x, y) position.

RGB565l: Returns the RGB888 pixel tuple (r, g, b) at position (x, y).

Bayer image: Returns the pixel value at position (x, y).

Does not support compressed images.

> image.get_pixel() and `image.set_pixel()` are the only methods that allow you to manipulate Bayer mode images. The Bayer mode image is a text image. For even rows, the pixels in the image are R/G/R/G/ etc. For odd lines, the pixels in the image are G/B/G/B/ etc. Each pixel is 8 bits.

#### image.set_pixel(x, y, pixel)
Grayscale image: Set the pixel at position (x, y) to the grayscale value pixel.

RGB image: Set the pixel at position (x, y) to RGB888 tuple (r, g, b) pixel.

Does not support compressed images.

> image.get_pixel() and `image.set_pixel()` are the only methods that allow you to manipulate Bayer mode images. The Bayer mode image is a text image. For even rows, the pixels in the image are R/G/R/G/ etc. For odd lines, the pixels in the image are G/B/G/B/ etc. Each pixel is 8 bits.

#### image.mean_pool(x_div, y_div)

Find the average value of x_div * y_div squares in the image and return the modified image composed of the average value of each square.

This method allows you to quickly shrink the image on the original image.

Does not support compressed images and bayer images.

#### image.mean_pooled(x_div, y_div)

Find the average value of x_div * y_div squares in the image and return a new image composed of the average value of each square.

This method allows you to create a reduced image copy.

Does not support compressed images and bayer images.

#### image.midpoint_pool(x_div, y_div[, bias=0.5])

Find the midpoint value of the x_div * y_div square in the image, and return the modified image composed of the midpoint value of each square.

A bias of 0.0 returns the minimum value of each region, and a ``bias'' of 1.0 returns the maximum value of each region.

This method allows you to quickly shrink the image on the original image.

Does not support compressed images and bayer images.

#### image.midpoint_pooled(x_div, y_div[, bias=0.5])

Find the midpoint value of the x_div * y_div squares in the image, and return a new image composed of the midpoint value of each square.

A bias of 0.0 returns the minimum value of each region, and a ``bias'' of 1.0 returns the maximum value of each region.

This method allows you to create a reduced image copy.

Does not support compressed images and bayer images.

#### image.to_grayscale([copy=False])

Convert the image to a grayscale image. This method will also modify the basic image pixels and change the image size in bytes, so it can only be performed on grayscale images or RGB565 images. Otherwise, copy must be True to create a new modified image on the heap.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.to_rgb565([copy=False])

Convert the image to a color image. This method will also modify the base image pixels and change the image size in bytes, so it can only be performed on RGB565 images. Otherwise, copy must be True to create a new modified image on the heap.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.to_rainbow([copy=False])

Convert the image to a rainbow image. This method will also modify the base image pixels and change the image size in bytes, so it can only be performed on RGB565 images. Otherwise, copy must be True to create a new modified image on the heap.

The rainbow image is a color image, and has a unique color value for each 8-bit mask gray-scale illumination value in the image. For example, it provides heat map colors for thermal images.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.compress([quality=50])

JPEG compresses the image appropriately. Compared with compressed save heap space, using this method uses a higher quality compression ratio at the cost of destroying the original image.

quality is the compression quality (0-100) (int).

#### image.compress_for_ide([quality=50])

JPEG compresses the image appropriately. Compared with compressed save heap space, using this method uses a higher quality compression ratio at the cost of destroying the original image.

This method compresses the image, and then formats the JPEG data by encoding every 6 bits into bytes between 128-191, and converts it to OpenMV IDE for display. This step is done to prevent the JPEG data from being mistaken for other text data in the byte stream.

You need to use this method to format the image data for display in the terminal window created by "Open Terminal" in OpenMV IDE.

quality is the compression quality (0-100) (int).

#### image.compressed([quality=50])

Return a JPEG compressed image—the original image is unprocessed. However, this method requires a large allocation of heap space, so image compression quality and image resolution must be very low.

quality is the compression quality (0-100) (int).

#### image.compressed_for_ide([quality=50])

Return a JPEG compressed image—the original image is unprocessed. However, this method requires a large allocation of heap space, so image compression quality and image resolution must be very low.

This method compresses the image, and then formats the JPEG data by encoding every 6 bits into bytes between 128-191, and converts it to OpenMV IDE for display. This step is done to prevent the JPEG data from being mistaken for other text data in the byte stream.

You need to use this method to format the image data for display in the terminal window created by "Open Terminal" in OpenMV IDE.

quality is the compression quality (0-100) (int).

#### image.copy([roi[, copy_to_fb=False]])

Create a copy of the image object.

Roi is a rectangular region of interest (x, y, w, h) to be copied. If not specified, the ROI will copy the entire image rectangle. But this does not apply to JPEG images.

Remember that the image copy is stored in the MicroPython heap, not the frame buffer. Similarly, you need to control the image copy size below 8KB (OpenMV) or below 16KB (OpenMV Cam M7). If you want to use one copy operation to use all the heap space, this function will be abnormal. An image that is too large can easily trigger abnormalities.

If copy_to_fb is True, this method replaces the frame buffer with an image. The frame buffer has much larger space than the heap and can hold large images.

#### image.save(path[, roi[, quality=50]])

Save a copy of the image to the file system in path.

Support image files in bmp/pgm/ppm/jpg/jpeg format. Note: You cannot save compressed images in jpeg format into uncompressed format.

roi is a rectangular region of interest (x, y, w, h) to be copied. If not specified, the ROI will copy the entire image rectangle. But this does not apply to JPEG images.

quality refers to the JPEG compression quality that saves the image as JPEG format when the image has not been compressed.

#### image.clear()

Set all pixels in the image to zero (very fast).

Return the image object so that you can call another method using. Notation.

Does not support compressed images.

#### image.draw_line(x0, y0, x1, y1[, color[, thickness=1]])

Draw a line from (x0, y0) to (x1, y1) on the image. You can pass x0, y0, x1, y1 individually, or to tuples (x0, y0, x1, y1).

color is an RGB888 tuple for grayscale or RGB565 images. The default is white. However, you can also pass the basic pixel value (0-255) of the grayscale image or the byte inverted RGB565 value of the RGB565 image.

thickness Controls the thickness of the line in pixels.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.
#### image.draw_rectangle(x, y, w, h[, color[, thickness=1[, fill=False]]])

Draw a rectangle on the image. You can pass x, y, w, h individually or as a tuple (x, y, w, h).

color is an RGB888 tuple for grayscale or RGB565 images. The default is white. However, you can also pass the basic pixel value (0-255) of the grayscale image or the byte inverted RGB565 value of the RGB565 image.

thickness Controls the thickness of the line in pixels.

Set fill to True to fill the rectangle.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.draw_ellipse(cx, cy, rx, ry, rotation[, color[, thickness=1[, fill=False]]])

Draws an ellipse on the image. You may either pass cx, cy, rx, ry, and the rotation (in degrees) separately or as a tuple (cx, yc, rx, ry, rotation).

color is an RGB888 tuple for Grayscale or RGB565 images. Defaults to white. However, you may also pass the underlying pixel value (0-255) for grayscale images or a RGB565 value for RGB565 images.

thickness controls how thick the edges are in pixels.

Pass fill set to True to fill the ellipse.

Returns the image object so you can call another method using . notation.

Not supported on compressed images or bayer images.

#### image.draw_circle(x, y, radius[, color[, thickness=1[, fill=False]]])

Draw a circle on the image. You can pass x, y, radius individually or as a tuple (x, y, radius).

color is an RGB888 tuple for grayscale or RGB565 images. The default is white. However, you can also pass the basic pixel value (0-255) of the grayscale image or the byte inverted RGB565 value of the RGB565 image.

thickness Controls the thickness of the line in pixels.

Set fill to True to fill the circle.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.draw_string(x, y, text[, color[, scale=1[, x_spacing=0[, y_spacing=0[, mono_space=True]]]]])

Draw 8x10 text from the position (x, y) in the image. You can pass x, y individually or as a tuple (x, y).

text is the character string written into the image. The \n, \r, and \r\n end characters move the cursor to the next line.

color is an RGB888 tuple for grayscale or RGB565 images. The default is white. However, you can also pass the basic pixel value (0-255) of the grayscale image or the byte inverted RGB565 value of the RGB565 image.

You can increase the scale to increase the size of the text on the image.

   Only integer values ​​(for example, 1/2/3/etc).

x_spacing allows you to add (if positive) or subtract (if negative) x pixels between characters to set the character spacing.

y_spacing allows you to add (if it is a positive number) or subtract (if it is a negative number) y pixels between characters to set line spacing.

mono_space defaults to True, which forces the text spacing to be fixed. For large text, this looks terrible. Set False to get non-fixed width character spacing, which looks much better.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.draw_cross(x, y[, color[, size=5[, thickness=1]]])

Draw a cross on the image. You can pass x, y individually or as a tuple (x, y).

color is an RGB888 tuple for grayscale or RGB565 images. The default is white. However, you can also pass the basic pixel value (0-255) of the grayscale image or the byte inverted RGB565 value of the RGB565 image.

size controls the extension length of the crosshairs.

thickness controls the pixel thickness of the edge.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.draw_arrow(x0, y0, x1, y1[, color[, thickness=1]])

Draw an arrow from (x0, y0) to (x1, y1) on the image. You can pass x0, y0, x1, y1 individually, or to tuples (x0, y0, x1, y1).

color is an RGB888 tuple for grayscale or RGB565 images. The default is white. However, you can also pass the basic pixel value (0-255) of the grayscale image or the byte inverted RGB565 value of the RGB565 image.

thickness Controls the thickness of the line in pixels.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.draw_image(image, x, y[, x_scale=1.0[, y_scale=1.0[, mask=None[, alpha=256]]]])

Draw an image whose upper left corner starts at position x, y. You can pass x, y individually or to a tuple (x, y).

x_scale controls the scale of the image in the x direction (floating point number).

y_scale controls the scale of the image in the y direction (floating point number).

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. You can use the mask mask for drawing operations.

Alpha controls the transparency of the source image drawn into the target image. 256 is to draw an opaque source image, and a value less than 256 produces a blend between the source image and the target image. 0 means not to modify the target image.

Does not support compressed images and bayer images.

#### image.draw_keypoints(keypoints[, color[, size=10[, thickness=1[, fill=False]]]])

Draw each point of a feature point object on the image.

color is an RGB888 tuple for grayscale or RGB565 images. The default is white. However, you can also pass the basic pixel value (0-255) of the grayscale image or the byte inverted RGB565 value of the RGB565 image.

size controls the size of feature points.

thickness Controls the thickness of the line in pixels.

Set fill to True to fill the feature points.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.flood_fill(x, y[, seed_threshold=0.05[, floating_threshold=0.05[, color[, invert=False[, clear_background=False[, mask=None]]]]]]])

Fill the area of ​​the image from position x, y. You can pass x, y individually or to a tuple (x, y).

seed_threshold controls the difference between the pixels in the filled area and the original starting pixels.

floating_threshold controls the difference between the pixels in the filled area and any adjacent pixels.

color is an RGB888 tuple for grayscale or RGB565 images. The default is white. However, you can also pass the basic pixel value (0-255) of the grayscale image or the byte inverted RGB565 value of the RGB565 image.

Pass invert as True to refill all content outside the flood_fill connection area.

Pass clear_background as True, and reset the remaining flood_fill pixels that have not been recolored.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask will be evaluated during flood_fill.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

This method is not available on OpenMV Cam M4.

#### image.binary(thresholds[, invert=False[, zero=False[, mask=None]]])

Set all pixels in the image to black or white according to whether the pixel is within the threshold in the threshold list thresholds.

thresholds must be a list of tuples. [(lo, hi), (lo, hi), ..., (lo, hi)] Define the color range you want to track. For grayscale images, each tuple needs to contain two values-the minimum gray value and the maximum gray value. Only the areas of pixels that fall between these thresholds are considered. For an RGB565 image, each tuple needs to have six values ​​(l_lo, l_hi, a_lo, a_hi, b_lo, b_hi)-the minimum and maximum values ​​of LAB L, A and B channels, respectively. For ease of use, this function will automatically repair the minimum and maximum values ​​of exchange. In addition, if the tuple is greater than six values, the remaining values ​​are ignored. Conversely, if the tuple is too short, it is assumed that the remaining thresholds are in the maximum range.

annotation

To obtain the threshold of the tracked object, simply select (click and drag) the tracked object in the IDE frame buffer. The histogram will be updated accordingly to the area. Then just write down the starting and falling positions of the color distribution in each histogram channel. These will be the low and high values ​​of thresholds. Since the difference between the upper and lower quartiles is small, it is better to manually determine the threshold.

You can also determine the color threshold by entering Tools -> Machine Vision -> Threshold Editor in OpenMV IDE and dragging the slider from the GUI window.

invert Inversion threshold operation, pixels are matched outside the known color range instead of in the known color range.

Set zero to True to make the threshold pixels zero and keep the pixels not in the threshold list unchanged.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.


#### image.invert()

Change the binary image 0 (black) to 1 (white) and 1 (white) to 0 (black), flipping all the pixel values ​​in the binary image very quickly.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and Bayer images.

#### image.b_and(image[, mask=None])

Use another image to perform a logical AND operation with this image.

image can be an image object, the path of an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value, the value can be an RGB888 tuple or a basic pixel value (for example, 8-bit grayscale of a grayscale image or byte-reversed RGB565 value of an RGB image).

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.b_nand(image[, mask=None])

Use another image to perform logical AND operation with this image.

image can be an image object, the path of an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value, the value can be an RGB888 tuple or a basic pixel value (for example, 8-bit grayscale of a grayscale image or byte-reversed RGB565 value of an RGB image).

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.b_or(image[, mask=None])

Use another image to perform a logical OR operation with this image.

image can be an image object, the path of an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value, the value can be an RGB888 tuple or a basic pixel value (for example, 8-bit grayscale of a grayscale image or byte-reversed RGB565 value of an RGB image).

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.
#### image.b_nor(image[, mask=None])

Use another image to perform logical NOR operation with this image.

image can be an image object, the path of an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value, the value can be an RGB888 tuple or a basic pixel value (for example, 8-bit grayscale of a grayscale image or byte-reversed RGB565 value of an RGB image).

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.b_xor(image[, mask=None])

Use another image to perform a logical XOR operation with this image.

image can be an image object, the path of an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value, the value can be an RGB888 tuple or a basic pixel value (for example, 8-bit grayscale of a grayscale image or byte-reversed RGB565 value of an RGB image).

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.b_xnor(image[, mask=None])

Use another image to perform logical XOR operation with this image.

image can be an image object, the path of an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value, the value can be an RGB888 tuple or a basic pixel value (for example, 8-bit grayscale of a grayscale image or byte-reversed RGB565 value of an RGB image).

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.erode(size[, threshold[, mask=None]])

Delete pixels from the edge of the divided area.

This method is implemented by convolving a kernel of ((size*2)+1)x((size*2)+1) pixels on the image. If the sum of the adjacent pixel sets is less than the threshold, the central pixel of the kernel Zero.

If the threshold is not set, this method functions as the standard corrosion method. If the threshold is set, you can specify the specific pixels to be eroded, for example: set the threshold value 2 for pixels below 2.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.dilate(size[, threshold[, mask=None]])

Add pixels to the edges of the segmented area.

This method is implemented by convolving a kernel of ((size*2)+1)x((size*2)+1) pixels on the image. If the sum of the adjacent pixel sets is greater than the threshold, the central pixel of the kernel is Set up.

If the threshold is not set, this method functions as the standard corrosion method. If the threshold is set, you can specify the specific pixels to be eroded, for example: set the threshold value 2 for pixels below 2.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.open(size[, threshold[, mask=None]])

Perform erosion and dilation on the image in sequence. For more information, see image.erode() and image.dilate().

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.close(size[, threshold[, mask=None]])

Perform dilation and erosion on the image in sequence. For more information, see image.erode() and image.dilate().

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.top_hat(size[, threshold[, mask=None]])

Return the difference between the original image and the image after executing the image.open() function.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Does not support compressed images and bayer images.

#### image.black_hat(size[, threshold[, mask=None]])

Return the difference between the original image and the image after executing the image.close() function.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Does not support compressed images and bayer images.

#### image.negate()

Flip (digitally invert) all pixel values ​​in the image very quickly. Perform numerical conversion on the pixel value of each color channel. Example: (255-pixel).

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.replace(image[, hmirror=False[, vflip=False[, mask=None]]])

image can be an image object, the path of an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value, the value can be an RGB888 tuple or a basic pixel value (for example, 8-bit grayscale of a grayscale image or byte-reversed RGB565 value of an RGB image).

Set hmirror to True to mirror the replacement image horizontally.

Set vflip to True to flip the replacement image vertically.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.add(image[, mask=None])

Add two images to each other pixel by pixel.

image can be an image object, the path of an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value, the value can be an RGB888 tuple or a basic pixel value (for example, 8-bit grayscale of a grayscale image or byte-reversed RGB565 value of an RGB image).

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.sub(image[, reverse=False[, mask=None]])

Subtract two images from each other pixel by pixel.

image can be an image object, the path of an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value, the value can be an RGB888 tuple or a basic pixel value (for example, 8-bit grayscale of a grayscale image or byte-reversed RGB565 value of an RGB image).

Setting reverse to True can reverse the subtraction operation from this_image-image to image-this_image.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.mul(image[, invert=False[, mask=None]])

Multiply two images by pixel.

image can be an image object, the path of an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value, the value can be an RGB888 tuple or a basic pixel value (for example, 8-bit grayscale of a grayscale image or byte-reversed RGB565 value of an RGB image).

Set invert to True to change the multiplication operation from a*b to 1/((1/a)*(1/b)). In particular, this brightens the image instead of darkening it (for example, multiplication and burning operations).

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.div(image[, invert=False[, mask=None]])

Divide this image by another image.

image can be an image object, the path of an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value, the value can be an RGB888 tuple or a basic pixel value (for example, 8-bit grayscale of a grayscale image or byte-reversed RGB565 value of an RGB image).

Set invert to True to change the division direction from a/b to b/a.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.min(image[, mask=None])

At the pixel level, replace the pixels in this image with the smallest pixel value between this image and another image.

image can be an image object, the path of an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value, the value can be an RGB888 tuple or a basic pixel value (for example, 8-bit grayscale of a grayscale image or byte-reversed RGB565 value of an RGB image).

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

This method is not available on OpenMV4.
#### image.max(image[, mask=None])

At the pixel level, replace the pixels in this image with the maximum pixel value between this image and another image.

image can be an image object, the path of an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value, the value can be an RGB888 tuple or a basic pixel value (for example, 8-bit grayscale of a grayscale image or byte-reversed RGB565 value of an RGB image).

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.difference(image[, mask=None])

Take the absolute value of the two images pixel by pixel. Example: For each color channel, change each pixel �� to ABS (this.pixel-image.pixel).

image can be an image object, the path of an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value, the value can be an RGB888 tuple or a basic pixel value (for example, 8-bit grayscale of a grayscale image or byte-reversed RGB565 value of an RGB image).

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.blend(image[, alpha=128[, mask=None]])

Fuse another image image with this image.

image can be an image object, the path of an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value, the value can be an RGB888 tuple or a basic pixel value (for example, 8-bit grayscale of a grayscale image or byte-reversed RGB565 value of an RGB image).

Alpha controls how much other images are blended into this image. Alpha should be an integer value between 0 and 256. A value close to zero will blend more other images into this image, a value close to 256 is the opposite.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.histeq([adaptive=False[, clip_limit=-1[, mask=None]]])

Run the histogram equalization algorithm on the image. Histogram equalization normalizes the contrast and brightness in the image.

If adaptive is passed as True, then an adaptive histogram equalization method will be run on the image, which is usually better than non-adaptive histogram definition, but it takes longer to run.

clip_limit provides a way to limit the contrast of adaptive histogram equalization. Use a small value (for example, 10) to generate a good histogram equalization contrast limited image.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.mean(size, [threshold=False, [offset=0, [invert=False, [mask=None]]]]])

Standard mean fuzzy filtering using box filters.

Size is the size of the kernel. Take 1 (3x3 core), 2 (5x5 core) or higher.

If you want to set the threshold adaptively on the output of the filter, you can pass the threshold=True parameter to start the adaptive threshold processing of the image, which will be based on the brightness of the environment pixel (related to the brightness of the pixels around the kernel function). Set to 1 or 0. A negative offset value sets more pixels to 1, while a positive value only sets the strongest contrast to 1. Set invert to invert the result output of the binary image.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

median(size, percentile=0.5, threshold=False, offset=0, invert=False, mask])
Run median filtering on the image. Under the condition of preserving the edges, the median filter is the best filter to smooth the surface, but it runs very slowly.

Size is the size of the kernel. Take 1 (3x3 core), 2 (5x5 core) or higher.

percentile controls the percentile of the value used in the kernel. By default, each pixel is replaced with the adjacent 50th percentile (center). You can set this value to 0 when using minimum filtering, 0.25 when using lower quartile filtering, 0.75 when using upper quartile filtering, and 1 when using maximum filtering.

If you want to set the threshold adaptively on the output of the filter, you can pass the threshold=True parameter to start the adaptive threshold processing of the image, which will be based on the brightness of the environment pixel (related to the brightness of the pixels around the kernel function). Set to 1 or 0. A negative offset value sets more pixels to 1, while a positive value only sets the strongest contrast to 1. Set invert to invert the result output of the binary image.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

This method is not available on OpenMV Cam M4.

#### image.mode(size[, threshold=False, offset=0, invert=False, mask])

Run a mode filter on the image, replacing each pixel with the pattern of neighboring pixels. This method works well on grayscale images. However, due to the non-linear nature of this operation, many artifacts will be generated on the edges of the RGB image.

Size is the size of the kernel. Take 1 (3x3 core) and 2 (5x5 core).

If you want to set the threshold adaptively on the output of the filter, you can pass the threshold=True parameter to start the adaptive threshold processing of the image, which will be based on the brightness of the environment pixel (related to the brightness of the pixels around the kernel function). Set to 1 or 0. A negative offset value sets more pixels to 1, while a positive value only sets the strongest contrast to 1. Set invert to invert the result output of the binary image.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

This method is not available on OpenMV Cam M4.

#### image.midpoint(size[, bias=0.5, threshold=False, offset=0, invert=False, mask])

Run midpoint filtering on the image. This filter finds the midpoint ((max-min)/2) of the neighborhood of each pixel in the image.

size is the size of the kernel. Take 1 (3x3 core), 2 (5x5 core) or higher.

Bias controls the minimum/maximum degree of image blending. 0 only applies to minimum filtering, and 1 only applies to maximum filtering. You can use bias to perform minimum/maximum filtering on the image.

If you want to set the threshold adaptively on the output of the filter, you can pass the threshold=True parameter to start the adaptive threshold processing of the image, which will be based on the brightness of the environment pixel (related to the brightness of the pixels around the kernel function). Set to 1 or 0. A negative offset value sets more pixels to 1, while a positive value only sets the strongest contrast to 1. Set invert to invert the result output of the binary image.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

This method is not available on OpenMV Cam M4.

#### image.morph(size, kernel, mul=Auto, add=0)

Convolve the image through the filter kernel. This allows you to perform general convolution on the image.

size controls the size of the kernel to ((size*2)+1)x((size*2)+1) pixels.

kernel The kernel used to convolve the image, which can be a tuple or a list of values ​​[-128:127].

mul is the number used to multiply the result of the convolution pixel. If not set, it will default to a value which will prevent scaling in the convolution output.

add is the value used to add to the convolution result of each pixel.

mul can adjust the global contrast, add can adjust the global brightness.

If you want to set the threshold adaptively on the output of the filter, you can pass the threshold=True parameter to start the adaptive threshold processing of the image, which will be based on the brightness of the environment pixel (related to the brightness of the pixels around the kernel function). Set to 1 or 0. A negative offset value sets more pixels to 1, while a positive value only sets the strongest contrast to 1. Set invert to invert the result output of the binary image.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

#### image.gaussian(size[, unsharp=False[, mul[, add=0[, threshold=False[, offset=0[, invert=False[, mask=None]]]]]]])

Convolve the image by smoothing Gaussian kernel.

size is the size of the kernel. Take 1 (3x3 core), 2 (5x5 core) or higher.

If unsharp is set to True, this method will not only perform Gaussian filtering operations, but perform unsharp masking operations, thereby improving the image sharpness of the edges.

mul is the number used to multiply the result of the convolution pixel. If not set, it will default to a value which will prevent scaling in the convolution output.

add is the value used to add to the convolution result of each pixel.

mul can adjust the global contrast, add can adjust the global brightness.

If you want to set the threshold adaptively on the output of the filter, you can pass the threshold=True parameter to start the adaptive threshold processing of the image, which will be based on the brightness of the environment pixel (related to the brightness of the pixels around the kernel function). Set to 1 or 0. A negative offset value sets more pixels to 1, while a positive value only sets the strongest contrast to 1. Set invert to invert the result output of the binary image.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

This method is not available on OpenMV Cam M4.
#### image.laplacian(size[, sharpen=False[, mul[, add=0[, threshold=False[, offset=0[, invert=False[, mask=None]]]]]]])

The image is convolved by edge detection Laplacian kernel.

size is the size of the kernel. Take 1 (3x3 core), 2 (5x5 core) or higher.

If sharpen is set to True, then this method will change to sharpen the image instead of outputting only the edge detection image that has not been thresholded. Increase the kernel size and then increase the image clarity.

mul is the number used to multiply the result of the convolution pixel. If not set, it will default to a value which will prevent scaling in the convolution output.

add is the value used to add to the convolution result of each pixel.

mul can adjust the global contrast, add can adjust the global brightness.

If you want to set the threshold adaptively on the output of the filter, you can pass the threshold=True parameter to start the adaptive threshold processing of the image, which will be based on the brightness of the environment pixel (related to the brightness of the pixels around the kernel function). Set to 1 or 0. A negative offset value sets more pixels to 1, while a positive value only sets the strongest contrast to 1. Set invert to invert the result output of the binary image.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

This method is not available on OpenMV Cam M4.

#### image.bilateral(size[, color_sigma=0.1[, space_sigma=1[, threshold=False[, offset=0[, invert=False[, mask=None]]]]]])

The image is convolved through a bilateral filter. The bilateral filter smoothes the image while maintaining the edges in the image.

size is the size of the kernel. Take 1 (3x3 core), 2 (5x5 core) or higher.

color_sigma controls how close the color is matched with the bilateral filter. Increase this value to increase color blur.

space_sigma controls the degree of mutual blurring of pixels in space. Increase this value to increase pixel blur.

If you want to set the threshold adaptively on the output of the filter, you can pass the threshold=True parameter to start the adaptive threshold processing of the image, which will be based on the brightness of the environment pixel (related to the brightness of the pixels around the kernel function). Set to 1 or 0. A negative offset value sets more pixels to 1, while a positive value only sets the strongest contrast to 1. Set invert to invert the result output of the binary image.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

This method is not available on OpenMV Cam M4.

#### image.cartoon(size[, seed_threshold=0.05[, floating_threshold=0.05[, mask=None]]])

Walk through the image and use the flood-fills algorithm to fill all pixel areas in the image. This effectively removes texture from the image by flattening the colors in all areas of the image. For best results, the image should have a lot of contrast so that the areas do not penetrate each other too easily.

seed_threshold controls the difference between the pixels in the filled area and the original starting pixels.

floating_threshold controls the difference between the pixels in the filled area and any adjacent pixels.

mask is another image used as a pixel-level mask for drawing operations. The mask should be an image with only black or white pixels and should be the same size as the image you are drawing. Only the pixels set in the mask are modified.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

This method is not available on OpenMV Cam M4.

#### image.remove_shadows([image])

Remove the shadow from the image.

If there is no "shadow-free" version of the current image, this method will try to remove the shadow from the image, but there is no real shadow-free image basis. This algorithm is suitable for removing shadows in a flat and uniform background. Please note that this method takes many seconds to run, and is only suitable for removing shadows in real time and dynamically generating a shadowless version of the image. Future versions of the algorithm will be applicable to more environments, but are equally slow.

If a "no shadow" version of the current image appears, this method will use the "true source" background non-shadow image to remove all shadows in the image to filter out the shadows. Non-shadow pixels are not filtered out, so you can add new objects to the scene that did not exist before, and any non-shadow pixels in those objects will be displayed.

Return the image object so that you can call another method using. Notation.

Only supports RGB565 images.

This method is not available on OpenMV Cam M4.

#### image.chrominvar()

Remove the lighting effect from the image, leaving only the color gradient. Faster than image.illuminvar() but affected by shadows.

Return the image object so that you can call another method using. Notation.

Only supports RGB565 images.

This method is not available on OpenMV Cam M4.

#### image.illuminvar()

Remove the lighting effect from the image, leaving only the color gradient. Slower than image.chrominvar() but not affected by shadows.

Return the image object so that you can call another method using. Notation.

Only supports RGB565 images.

This method is not available on OpenMV Cam M4.

#### image.linpolar([reverse=False])

The image is reprojected from Cartesian coordinates to linear polar coordinates.

Set reverse = True to reproject in the opposite direction.

Linear polar reprojection converts image rotation to x translation.

Does not support compressed images.

This method is not available on OpenMV Cam M4.

#### image.logpolar([reverse=False])

The image is reprojected from Cartesian coordinates to log-polar coordinates.

Set reverse = True to reproject in the opposite direction.

Log polar reprojection transforms the rotation of the image into x translation and scaling to y translation.

Does not support compressed images.

This method is not available on OpenMV Cam M4.

#### image.lens_corr([strength=1.8[, zoom=1.0]])

Perform lens distortion correction to remove the fisheye effect of the image caused by the lens.

strength is a floating point number, which determines the degree of de-fishing effect on the image. By default, first try the value 1.8, and then adjust this value to make the image display the best effect.

zoom is the value used to zoom the image. The default value is 1.0.

Return the image object so that you can call another method using. Notation.

Does not support compressed images and bayer images.

 #### img.rotation_corr([x_rotation=0.0[, y_rotation=0.0[, z_rotation=0.0[, x_translation=0.0[, y_translation=0.0[, zoom=1.0[, fov=60.0[, corners]]]]] ]]])

Correct the perspective problem in the image by 3D rotation of the frame buffer.

`x_rotation` is the number of degrees that the image is rotated around the x axis in the frame buffer (that is, the image is rotated up and down).

`y_rotation` refers to the number of degrees the image is rotated around the y axis in the frame buffer (ie, rotate the image left and right).

`z_rotation` is the number of degrees the image is rotated around the z axis in the frame buffer (ie, the image is rotated to the appropriate position).

`x_translation` is the number of units to move the image to the left or right after rotation. Because this conversion is applied to 3D space, the unit is not a pixel...

`y_translation` is the number of units by which the image moves up or down after being rotated. Because this conversion is applied to 3D space, the unit is not a pixel...

`zoom` is the multiple to zoom the image, 1.0 by default.

`fov` is the field of view used internally before rotating the image in 3D space when performing 2D->3D projection. When this value is close to 0, the image is placed infinitely far from the viewport. When this value is close to 180, the image is placed in the viewport. Normally, you should not change this value, but you can modify it to change the 2D->3D mapping effect.

`corners` is a list of four (x, y) tuples, representing four `corners` used to create four-point correspondence homography, mapping the first `corner` to (0,0), and the second A `corner` (image_width-1, 0), a third `corner` (image_width-1 image_height-1) and a fourth `corner` (0, image_height-1). Then apply 3D rotation after the image is remapped. This parameter allows you to use rotation_corr to do things, such as bird's-eye view conversion. E.g:

```python
top_tilt = 10 # if the difference between top/bottom_tilt become to large this method will stop working
bottom_tilt = 0

points = [(tilt, 0), (img.width()-tilt, 0), (img.width()-1-bottom_tilt, img.height()-1), (bottom_tilt, img.height()- 1)]

img.rotation_corr(corners=points)
```

Return the image object so that you can use `.` to call another method.

Does not support compressed images or Bayer images.

#### image.get_similarity(image)

Return a "similarity" object, describing two images using the SSIM algorithm to compare the similarity of the 8x8 pixel color patches between the two images.

image can be an image object, the path of an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value, the value can be an RGB888 tuple or a basic pixel value (for example, 8-bit grayscale of a grayscale image or byte-reversed RGB565 value of an RGB image).

Does not support compressed images and bayer images.

This method is not available on OpenMV Cam M4.
#### image.get_histogram([thresholds[, invert=False[, roi[, bins[, l_bins[, a_bins[, b_bins]]]]]]])

Perform normalized histogram operations on all color channels of roi and return a histogram object. Please refer to the histogram object for more information. You can also use image.get_hist or image.histogram to call this method. If you pass the thresholds list, the histogram information will only be calculated from the pixels in the threshold list.

thresholds must be a list of tuples. [(lo, hi), (lo, hi), ..., (lo, hi)] Define the color range you want to track. For grayscale images, each tuple needs to contain two values-the minimum gray value and the maximum gray value. Only the areas of pixels that fall between these thresholds are considered. For an RGB565 image, each tuple needs to have six values ​​(l_lo, l_hi, a_lo, a_hi, b_lo, b_hi)-the minimum and maximum values ​​of LAB L, A and B channels, respectively. For ease of use, this function will automatically repair the minimum and maximum values ​​of exchange. In addition, if the tuple is greater than six values, the remaining values ​​are ignored. Conversely, if the tuple is too short, it is assumed that the remaining thresholds are in the maximum range.

annotation

To obtain the threshold of the tracked object, simply select (click and drag) the tracked object in the IDE frame buffer. The histogram will be updated accordingly to the area. Then just write down the starting and falling positions of the color distribution in each histogram channel. These will be the low and high values ​​of thresholds. Since the difference between the upper and lower quartiles is small, it is better to manually determine the threshold.

You can also determine the color threshold by entering Tools -> Machine Vision -> Threshold Editor in OpenMV IDE and dragging the slider from the GUI window.

invert Inversion threshold operation, pixels are matched outside the known color range instead of in the known color range.

Unless you need to use color statistics for advanced operations, just use the `image.get_statistics()` method instead of this method to view the pixel area in the image.

roi is the rectangular tuple (x, y, w, h) of the region of interest. If not specified, the ROI is the image rectangle of the entire image. The operating range is limited to the pixels in the roi area.

bins and other bins are the number of bins used for the histogram channel. For grayscale images, use bins, and for RGB565 images, use every other channel. The bin count of each channel must be greater than 2. In addition, setting the bin count to be greater than the number of unique pixel values ​​for each channel is meaningless. By default, the histogram will have the maximum number of bins per channel.

Does not support compressed images and bayer images.

#### image.get_statistics([thresholds[, invert=False[, roi[, bins[, l_bins[, a_bins[, b_bins]]]]]]])

Calculate the average, median, mode, standard deviation, minimum, maximum, lower quartile and upper quartile of each color channel in roi, and return a data object. See the statistics object for more information. You can also use image.get_stats or image.statistics to call this method. If you pass the thresholds list, the histogram information will only be calculated from the pixels in the threshold list.

thresholds must be a list of tuples. [(lo, hi), (lo, hi), ..., (lo, hi)] Define the color range you want to track. For grayscale images, each tuple needs to contain two values-the minimum gray value and the maximum gray value. Only the areas of pixels that fall between these thresholds are considered. For an RGB565 image, each tuple needs to have six values ​​(l_lo, l_hi, a_lo, a_hi, b_lo, b_hi)-the minimum and maximum values ​​of LAB L, A and B channels, respectively. For ease of use, this function will automatically repair the minimum and maximum values ​​of exchange. In addition, if the tuple is greater than six values, the remaining values ​​are ignored. Conversely, if the tuple is too short, it is assumed that the remaining thresholds are in the maximum range.

annotation

To obtain the threshold of the tracked object, simply select (click and drag) the tracked object in the IDE frame buffer. The histogram will be updated accordingly to the area. Then just write down the starting and falling positions of the color distribution in each histogram channel. These will be the low and high values ​​of thresholds. Since the difference between the upper and lower quartiles is small, it is better to manually determine the threshold.

You can also determine the color threshold by entering Tools -> Machine Vision -> Threshold Editor in OpenMV IDE and dragging the slider from the GUI window.

invert Inversion threshold operation, pixels are matched outside the known color range instead of in the known color range.

You can use this method when you need to obtain information about a pixel area in an image. For example: If you want to use the frame difference method to detect motion, you need to use this method to determine the change of the image color channel, thereby triggering the motion detection threshold.

roi is the rectangular tuple (x, y, w, h) of the region of interest. If not specified, the ROI is the image rectangle of the entire image. The operating range is limited to the pixels in the roi area.

bins and other bins are the number of bins used for the histogram channel. For grayscale images, use bins, and for RGB565 images, use every other channel. The bin count of each channel must be greater than 2. In addition, setting the bin count to be greater than the number of unique pixel values ​​for each channel is meaningless. By default, the histogram will have the maximum number of bins per channel.

Does not support compressed images and bayer images.

#### image.get_regression(thresholds[, invert=False[, roi[, x_stride=2[, y_stride=1[, area_threshold=10[, pixels_threshold=10[, robust=False]]]]]]]])

Perform linear regression calculation on all threshold pixels of the image. This calculation is performed by the least square method, which is usually faster, but cannot handle any outliers. If robust is True, the Theil index will be used. The Theil index calculates the median of all slopes between all threshold pixels in the image. If you set too many pixels after threshold conversion, this N^2 operation may drop your FPS below 5 even on an 80x60 image. However, as long as the number of pixels to be set after the threshold conversion is small, linear regression is still effective even when more than 30% of the threshold pixels are abnormal values.

This method returns an image.line object. How to easily use linear objects, please refer to the following blog post: https://openmv.io/blogs/news/linear-regression-line-following

thresholds must be a list of tuples. [(lo, hi), (lo, hi), ..., (lo, hi)] Define the color range you want to track. For grayscale images, each tuple needs to contain two values-the minimum gray value and the maximum gray value. Only the areas of pixels that fall between these thresholds are considered. For an RGB565 image, each tuple needs to have six values ​​(l_lo, l_hi, a_lo, a_hi, b_lo, b_hi)-the minimum and maximum values ​​of LAB L, A and B channels, respectively. For ease of use, this function will automatically repair the minimum and maximum values ​​of exchange. In addition, if the tuple is greater than six values, the remaining values ​​are ignored. Conversely, if the tuple is too short, it is assumed that the remaining thresholds are in the maximum range.

> To obtain the threshold of the tracked object, just select (click and drag) the tracked object in the IDE frame buffer. The histogram will be updated accordingly to the area. Then just write down the starting and falling positions of the color distribution in each histogram channel. These will be the low and high values ​​of thresholds. Since the difference between the upper and lower quartiles is small, it is better to manually determine the threshold.

You can also determine the color threshold by entering Tools -> Machine Vision -> Threshold Editor in OpenMV IDE and dragging the slider from the GUI window.

invert Inversion threshold operation, pixels are matched outside the known color range instead of in the known color range.

roi is the rectangular tuple (x, y, w, h) of the region of interest. If not specified, the ROI is the image rectangle of the entire image. The operating range is limited to the pixels in the roi area.

x_stride is the number of x pixels to skip when calling the function.

y_stride is the number of y pixels to skip when calling the function.

If the bounding box area after regression is less than area_threshold, None is returned.

If the number of pixels after regression is less than pixel_threshold, None is returned.

Does not support compressed images and bayer images.
#### image.find_blobs(thresholds[, invert=False[, roi[, x_stride=2[, y_stride=1[, area_threshold=10[, pixels_threshold=10[, merge=False[, margin=0[, threshold_cb =None[, merge_cb=None]]]]]]]]]]])

Find all the color blocks in the image and return a list of color block objects including each color block. Please observe the image.blob object for more information.

thresholds must be a list of tuples. [(lo, hi), (lo, hi), ..., (lo, hi)] Define the color range you want to track. For grayscale images, each tuple needs to contain two values-the minimum gray value and the maximum gray value. Only the areas of pixels that fall between these thresholds are considered. For an RGB565 image, each tuple needs to have six values ​​(l_lo, l_hi, a_lo, a_hi, b_lo, b_hi)-the minimum and maximum values ​​of LAB L, A and B channels, respectively. For ease of use, this function will automatically repair the minimum and maximum values ​​of exchange. In addition, if the tuple is greater than six values, the remaining values ​​are ignored. Conversely, if the tuple is too short, it is assumed that the remaining thresholds are in the maximum range.

annotation

To obtain the threshold of the tracked object, simply select (click and drag) the tracked object in the IDE frame buffer. The histogram will be updated accordingly to the area. Then just write down the starting and falling positions of the color distribution in each histogram channel. These will be the low and high values ​​of thresholds. Since the difference between the upper and lower quartiles is small, it is better to manually determine the threshold.

You can also determine the color threshold by entering Tools -> Machine Vision -> Threshold Editor in OpenMV IDE and dragging the slider from the GUI window.

invert Inversion threshold operation, pixels are matched outside the known color range instead of in the known color range.

roi is the rectangular tuple (x, y, w, h) of the region of interest. If not specified, the ROI is the image rectangle of the entire image. The operating range is limited to the pixels in the roi area.

x_stride is the number of x pixels that need to be skipped when searching for a color block. After finding the color block, the straight line filling algorithm will accurately pixel. If the color block is known to be large, you can increase x_stride to increase the speed of finding the color block.

y_stride is the number of y pixels that need to be skipped when searching for a color block. After finding the color block, the straight line filling algorithm will accurately pixel. If the color block is known to be large, y_stride can be increased to increase the speed of searching for the color block.

If the bounding box area of ​​a color block is smaller than area_threshold, it will be filtered out.

If the number of pixels of a color block is less than pixel_threshold, it will be filtered out.

If merge is True, all color blocks that have not been filtered out are merged. The bounding rectangles of these color blocks overlap each other. Margin can be used to increase or decrease the size of the color block boundary rectangle in the intersection test. For example: the color blocks whose edges are 1 and the mutual boundary rectangle is 1 will be merged.

Combining color blocks enables color code tracking. Each color block object has a code value code, which is a bit vector. For example: if you enter two color thresholds in image.find_blobs, the first threshold code is 1, the second code is 2 (the third code is 4, the fourth code is 8, and so on). The merged color block uses a logical OR operation on all codes so that you know the colors that produced them. This allows you to track two colors. If you use two colors to get a color block object, it may be a color code.

If you use a strict color range and cannot fully track all pixels of the target object, you may need to merge color blocks.

Finally, if you want to merge color blocks, but do not want to merge color blocks of two different threshold colors, just call image.find_blobs twice, and the color blocks of different threshold values ​​will not be merged.

threshold_cb can be set to call the function of each color block after threshold filtering, so as to filter it from the list of color blocks to be merged. The callback function will receive one parameter: the color block object to be filtered. Then the callback function needs to return True to keep the color blocks or return False to filter the color blocks.

merge_cb can be set as a function to call two color blocks to be merged to prohibit or permit the merge. The callback function will receive two parameters-two color patch objects to be merged. The callback function must return True to merge color blocks, or return False to prevent color blocks from merging.

Does not support compressed images and bayer images.

#### image.find_lines([roi[, x_stride=2[, y_stride=1[, threshold=1000[, theta_margin=25[, rho_margin=25]]]]]])

Use Hough Transform to find all straight lines in the image. Return a list of image.line objects.

roi is the rectangular tuple (x, y, w, h) of the region of interest. If not specified, the ROI is the image rectangle of the entire image. The operating range is limited to the pixels in the roi area.

x_stride is the number of x pixels that need to be skipped during Hough transform. If the known straight line is larger, you can increase x_stride.

y_stride is the number of y pixels that need to be skipped during Hough transform. If the known straight line is larger, you can increase y_stride.

threshold controls the straight line detected from the Hough transform. Only return lines greater than or equal to threshold. The correct threshold value for the application depends on the image. Note: The magnitude of a straight line (magnitude) is the sum of the pixel sizes of all Sobel filters that make up the straight line.

theta_margin controls the merging of the monitored lines. The part where the angle of the straight line is theta_margin is merged with the part where the p value of the straight line is rho_margin.

rho_margin controls the merging of the monitored lines. The part where the angle of the straight line is theta_margin and the part where the p value of the straight line is rho_margin are merged.

This method runs the Sobel filter on the image and uses the amplitude and gradient response of the filter to perform the Hough transform. No preprocessing of the image is required. However, cleaning the image filter can get more stable results.

Does not support compressed images and bayer images.

This method is not available on OpenMV Cam M4.

#### image.find_line_segments([roi[, merge_distance=0[, max_theta_difference=15]]])

Use Hough Transform to find line segments in the image. Return a list of image.line objects.

roi is a rectangular region of interest (x, y, w, h) to be copied. If not specified, ROI is the image rectangle. The operating range is limited to pixels in the roi area.

merge_distance specifies the maximum number of pixels between two line segments that can be separated from each other without being merged.

max_theta_difference is the maximum angle difference between the two line segments to be merged by the above merge_distancede.

This method uses the LSD library (also used by OpenCV) to find line segments in the image. This is a bit slow, but very accurate, and the line segments will not jump.

Does not support compressed images and bayer images.

This method is not available on OpenMV Cam M4.

#### image.find_circles([roi[, x_stride=2[, y_stride=1[, threshold=2000[, x_margin=10[, y_margin=10[, r_margin=10]]]]]]])

Use the Hough transform to find the circle in the image. Return a list of image.circle objects (see above).

roi is a rectangular region of interest (x, y, w, h) to be copied. If not specified, ROI is the image rectangle. The operating range is limited to pixels in the roi area.

x_stride is the number of x pixels that need to be skipped during Hough transform. If the circle is known to be larger, you can increase x_stride.

y_stride is the number of y pixels that need to be skipped during Hough transform. If the circle is known to be larger, y_stride can be increased.

threshold controls the circle detected from the Hough transform. Only return circles greater than or equal to threshold. The correct threshold value for the application depends on the image. Note: The size of a circle (magnitude) is the sum of the sizes of all Sobel filter pixels that make up the circle.

x_margin controls the merging of the detected circles. The round pixels are the partial merge of x_margin, y_margin and r_margin.

y_margin controls the merging of the detected circles. The round pixels are the partial merge of x_margin, y_margin and r_margin.

r_margin controls the merging of the detected circles. The round pixels are the partial merge of x_margin, y_margin and r_margin.

Does not support compressed images and bayer images.

This method is not available on OpenMV Cam M4.

#### image.find_rects([roi=Auto, threshold=10000])

Use the same quad detection algorithm used to find AprilTAg to find rectangles in the image. Best for rectangles that contrast sharply with the background. AprilTag's quad detection can handle arbitrary scaling/rotation/cutting of rectangles. Returns a list of image.rect objects.

roi is a rectangular region of interest (x, y, w, h) to be copied. If not specified, ROI is the image rectangle. The operating range is limited to the pixels in the roi area.

Rectangles with a boundary size (by sliding the Sobel operator on all pixels on the edge of the rectangle and adding the value) less than threshold will be filtered from the returned list. The correct value of threshold depends on your application/scenario.

Does not support compressed images and bayer images.

This method is not available on OpenMV Cam M4.

#### image.find_qrcodes([roi])

Find all QR codes in roi and return a list of image.qrcode objects. Please refer to the image.qrcode object for more information.

In order for this method to run successfully, the QR code on the image needs to be relatively flat. By using the sensor.set_windowing function to zoom in the center of the lens, the image.lens_corr function to eliminate the barrel distortion of the lens or by changing the lens with a narrower field of view, you can get a flatter QR code that is not affected by lens distortion. Some machine vision lenses do not cause barrel distortion, but their cost is much higher than the standard lenses provided by OpenMV, which are distortion-free lenses.

roi is a rectangular region of interest (x, y, w, h) to be copied. If not specified, ROI is the image rectangle of the entire image. The operating range is limited to the pixels in the roi area.

Does not support compressed images and bayer images.

This method is not available on OpenMV Cam M4.

image.find_apriltags([roi[, families=image.TAG36H11[, fx[, fy[, cx[, cy]]]]]])
Find all AprilTags in roi, and return a list of image.apriltag objects. Please refer to the image.apriltag object for more information.

Compared with two-dimensional codes, AprilTags can be detected at longer distances, poorer light, and more distorted image environments. AprilTags can deal with all kinds of image distortion problems, but two-dimensional codes cannot. In other words, AprilTags can only encode a digital ID as its payload.

AprilTags can also be used for localization. Each image.apriltag object returns its three-dimensional position information and rotation angle from the camera. The position information is determined by fx, fy, cx and cy, which are the focal length and center point of the image in the X and Y directions, respectively.
> Use the built-in tag generator tool of OpenMV IDE to create AprilTags. The label generator can create printable 8.5"x11" AprilTags.

roi is a rectangular region of interest (x, y, w, h) to be copied. If not specified, ROI is the image rectangle of the entire image. The operating range is limited to the pixels in the roi area.

families is the bit mask of the tag family to be decoded. Is a logical OR:

image.TAG16H5
image.TAG25H7
image.TAG25H9
image.TAG36H10
image.TAG36H11
image.ARTOOLKIT
The default setting is the best image.TAG36H11 tag family. Note: Each time you enable a tag family, the speed of find_apriltags will slow down slightly.

fx is the focal length of the camera in the x direction in pixels. The value of the standard OpenMV Cam is (2.8 / 3.984) * 656, which is obtained by dividing the focal length in millimeters by the length of the photosensitive element in the X direction, and multiplying it by the number of pixels of the photosensitive element in the X direction (for OV7725 photosensitive element In terms of).

fy is the focal length of the camera in the y direction in pixels. The value of the standard OpenMV Cam is (2.8 / 2.952) * 488, which is obtained by dividing the focal length in millimeters by the length of the photosensitive element in the Y direction, and multiplying it by the number of pixels of the photosensitive element in the Y direction (for OV7725 photosensitive element In terms of).

cx is the center of the image, which is image.width()/2 instead of roi.w()/2.

cy is the center of the image, ie image.height()/2, not roi.h()/2.

Does not support compressed images and bayer images.

This method is not available on OpenMV Cam M4.

image.find_datamatrices([roi[, effort=200]])
Find all data matrices in roi and return a list of image.datamatrix objects. Please refer to the image.datamatrix object for more information.

In order for this method to run successfully, the rectangular code on the image needs to be relatively flat. By using the sensor.set_windowing function to zoom in at the center of the lens, the image.lens_corr function to eliminate the barrel distortion of the lens, or by changing the lens with a narrower field of view, you can get a flatter rectangular code that is not affected by lens distortion. Some machine vision lenses do not cause barrel distortion, but their cost is much higher than the standard lens provided by OpenMV, which is a distortion-free lens.

roi is a rectangular region of interest (x, y, w, h) to be copied. If not specified, ROI is the image rectangle of the entire image. The operating range is limited to the pixels in the roi area.

effort controls the time used to find a rectangle code match. The default value of 200 should apply to all use cases. But you may also increase detection at the expense of frame rate, or increase frame rate at the expense of detection. Note: If effort is set below about 160, you will not be able to perform any detection; instead, you can set it to any high value you need, but if the setting is higher than 240, the detection rate will not continue to increase.

Does not support compressed images and bayer images.

This method is not available on OpenMV Cam M4.

#### image.find_barcodes([roi])

Find all one-dimensional barcodes in roi and return a list of image.barcode objects. Please refer to the image.barcode object for more information.

For best results, please use a window of 640 length and 40/80/160 width. The lower the verticality, the faster the running speed. Since the barcode is a linear one-dimensional image, it only needs to have a higher resolution in one direction and a lower resolution in the other direction. Note: This function performs horizontal and vertical scanning, so you can use a window with a width of 40/80/160 and a length of 480. Finally, be sure to adjust the lens so that the barcode will be positioned where the focal length produces the clearest image. Fuzzy barcodes cannot be decoded.

This function supports all one-dimensional barcodes:

image.EAN2
image.EAN5
image.EAN8
image.UPCE
image.ISBN10
image.UPCA
image.EAN13
image.ISBN13
image.I25
image.DATABAR (RSS-14)
image.DATABAR_EXP (RSS-Expanded)
image.CODABAR
image.CODE39
image.PDF417
image.CODE93
image.CODE128
roi is a rectangular region of interest (x, y, w, h) to be copied. If not specified, ROI is the image rectangle of the entire image. The operating range is limited to the pixels in the roi area.

Does not support compressed images and bayer images.

This method is not available on OpenMV Cam M4.

image.find_displacement(template[, roi[, template_roi[, logpolar=False]]])
Find the transformation offset of this image from the template. This method can be used to make optical flow. This method returns an image.displacement object that contains the result of the displacement calculation using phase correlation.

roi is the rectangular area (x, y, w, h) to be processed. If not specified, it is equal to the image rectangle.

template_roi is the rectangular area (x, y, w, h) to be processed. If not specified, it is equal to the image rectangle.

roi and template roi must have the same w/h, but x/y can be anywhere in the image. You can slide the smaller rois on the larger image to get the optical flow gradient image.

image.find_displacement usually calculates the x/y translation between two images. However, if you set logpolar = True, it will find changes in rotation and scaling between the two images. The same image.displacement object results in two possible feedbacks.

Does not support compressed images and bayer images.

annotation

Please use this method on images with the same length and width (such as ``sensor.B64X64'').

This method is not available on OpenMV Cam M4.

#### image.find_number(roi)

Run LENET-6 CNN (Convolutional Neural Network) trained on the MINST dataset to detect numbers in 28x28 ROI located anywhere on the image. Return a tuple containing integers and floating-point numbers, representing the detected number (0-9) and the detection confidence (0-1).

roi is the rectangular tuple (x, y, w, h) of the region of interest. If not specified, the ROI is the image rectangle of the entire image. The operating range is limited to the pixels in the roi area.

Only grayscale images are supported.

annotation

This method is experimental. If you run any CNN trained on PC using Caffe in the future, this method may be deleted. The latest firmware version 3.0.0 has removed this function.

This method is not available on OpenMV Cam M4.

#### image.classify_object(roi)

Run CIFAR-10 CNN on the ROI of the image to detect airplanes, cars, birds, cats, deer, dogs, frogs, horses, boats and trucks. This method automatically scales the image to 32x32 internally to feed the CNN.

roi is the rectangular tuple (x, y, w, h) of the region of interest. If not specified, the ROI is the image rectangle of the entire image. The operating range is limited to the pixels in the roi area.

Only supports RGB565 images.

annotation

This method is experimental. If you run any CNN trained on PC using Caffe in the future, this method may be deleted.

This method is not available on OpenMV Cam M4.

image.find_template(template, threshold[, roi[, step=2[, search=image.SEARCH_EX]]])
Try to use the normalized cross-correlation (NCC) algorithm to find the first template match in the image. Returns the bounding box tuple (x, y, w, h) of the matching position, otherwise returns None.

template is a small image object that matches this image object. Note: Both images must be grayscale.

Threshold is a floating point number (0.0-1.0), where the smaller value increases the detection rate while increasing the false alarm rate. Conversely, a higher value will reduce the detection rate and at the same time reduce the false alarm rate.

roi is the rectangular tuple (x, y, w, h) of the region of interest. If not specified, the ROI is the image rectangle of the entire image. The operating range is limited to the pixels in the roi area.

step is the number of pixels that need to be skipped when searching for a template. Skipping pixels can greatly increase the speed of the algorithm. This method is only applicable to algorithms in SERACH_EX mode.

search can be image.SEARCH_DS or image.SEARCH_EX. The algorithm used by image.SEARCH_DS to search for a template is faster than image.SEARCH_EX, but if the template is located around the edge of the image, the search may not succeed. image.SEARCH_EX can perform a more detailed search on images, but its running speed is much slower than image.SEARCH_DS.

Only grayscale images are supported.

#### image.find_features(cascade[, threshold=0.5[, scale=1.5[, roi]]])

This method searches images of all regions that match Haar Cascade and returns a list of bounding box rectangle tuples (x, y, w, h) about these features. If no features are found, a blank list is returned.

cascade is a Haar Cascade object. See image.HaarCascade() for details.

Threshold is a floating point number (0.0-1.0), where the smaller value increases the detection rate while increasing the false alarm rate. Conversely, a higher value will reduce the detection rate and at the same time reduce the false alarm rate.

scale is a floating point number that must be greater than 1.0. A higher scale factor runs faster, but its image matching is relatively poor. The ideal value is between 1.35-1.5.

roi is the rectangular tuple (x, y, w, h) of the region of interest. If not specified, the ROI is the image rectangle of the entire image. The operating range is limited to the pixels in the roi area.

Only grayscale images are supported.

#### image.find_eye(roi)

Find the pupil in the area of ​​interest (x, y, w, h) around the eye. Returns a tuple containing the position of the pupil (x, y) in the image. If no pupil is found, return (0,0).

Before using this function, first use image.find_features() and Haar operator frontalface to search for someone's face. Then use image.find_features and Haar operator find_eye to search for eyes on the face. Finally, call this method on each eye ROI returned after calling the image.find_features function to get the coordinates of the pupil.

roi is the rectangular tuple (x, y, w, h) of the region of interest. If not specified, the ROI is the image rectangle of the entire image. The operating range is limited to the pixels in the roi area.

Only grayscale images are supported.

#### image.find_lbp(roi)

Extract LBP (local binary mode) key points from the ROI tuple (x, y, w, h). You can use the image.match_descriptor function to compare two sets of key points to get the matching distance.

roi is the rectangular tuple (x, y, w, h) of the region of interest. If not specified, the ROI is the image rectangle of the entire image. The operating range is limited to the pixels in the roi area.

Only grayscale images are supported.
#### image.find_keypoints([roi[, threshold=20[, normalized=False[, scale_factor=1.5[, max_keypoints=100[, corner_detector=image.CORNER_AGAST]]]]]]])

Extract ORB key points from the ROI tuple (x, y, w, h). You can use the image.match_descriptor function to compare two sets of key points to get the matching area. If no key point is found, None is returned.

roi is the rectangular tuple (x, y, w, h) of the region of interest. If not specified, the ROI is the image rectangle of the entire image. The operating range is limited to the pixels in the roi area.

threshold is a number that controls the number of extractions (values ​​0-255). For the default AGAST corner detector, this value should be around 20. For FAST corner detectors, this value is about 60-80. The lower the threshold, the more corner points you extract.

normalized is a boolean value. If True, turn off the key point extraction in multi-resolution. If you don't care about dealing with scaling issues and want the algorithm to run faster, set it to True.

scale_factor is a floating point number that must be greater than 1.0. A higher scale factor runs faster, but its image matching is relatively poor. The ideal value is between 1.35-1.5.

max_keypoints is the maximum number of keypoints that a keypoint object can hold. If the key point object is too large and causes memory problems, please lower the value.

corner_detector is the corner detector algorithm used to extract the key points from the image. Can be image.CORNER_FAST or image.CORNER_AGAST. The FAST corner detector runs faster, but its accuracy is lower.

Only grayscale images are supported.

#### image.find_edges(edge_type[, threshold])

Turn the image into black and white, leaving only the edges as white pixels.

image.EDGE_SIMPLE-Simple threshold high-pass filtering algorithm
image.EDGE_CANNY-Canny edge detection algorithm
threshold is a binary tuple containing a low threshold and a high threshold. You can control the edge quality by adjusting this value.

The default is (100, 200).

Only grayscale images are supported.

find_hog([roi[, size=8]])
Replace the pixels in the ROI with HOG (Histogram of Oriented Gradient) lines.

roi is the rectangular tuple (x, y, w, h) of the region of interest. If not specified, the ROI is the image rectangle of the entire image. The operating range is limited to the pixels in the roi area.

Only grayscale images are supported.

This method is not available on OpenMV Cam M4.

## Constant

### image.SEARCH_EX

Exhaustive template matching search.

### image.SEARCH_DS

Faster template matching search.

### image.EDGE_CANNY

Use the Canny edge detection algorithm to perform edge detection on the image.

### image.EDGE_SIMPLE

Use threshold high-pass filtering algorithm to detect the edge of the image.

### image.CORNER_FAST

High-speed and low-accuracy corner detection algorithm for ORB key points

### image.CORNER_AGAST

Low-speed and high-accuracy algorithm for ORB key points.

### image.TAG16H5

Bit mask enumeration of TAG1H5 tag group. Used for AprilTags.

### image.TAG25H7

Bit mask enumeration of TAG25H7 tag group. Used for AprilTags.

### image.TAG25H9

Bitmask enumeration of TAG25H9 tag group. Used for AprilTags.

### image.TAG36H10

Bit mask enumeration of TAG36H10 tag group. Used for AprilTags.

### image.TAG36H11

Bit mask enumeration of TAG36H11 tag group. Used for AprilTags.

### image.ARTOOLKIT

The bit mask enumeration of the ARTOOLKIT tag group. Used for AprilTags.

### image.EAN2

EAN2 barcode type enumeration.

### image.EAN5

EAN5 barcode type enumeration.

### image.EAN8

EAN8 barcode type enumeration.

### image.UPCE

UPCE barcode type enumeration.

### image.ISBN10

ISBN10 barcode type enumeration.

### image.UPCA

UPCA barcode type enumeration.

### image.EAN13

EAN13 barcode type enumeration.

### image.ISBN13

ISBN13 barcode type enumeration.

### image.I25

I25 barcode type enumeration.

### image.DATABAR

DATABAR barcode type enumeration.

### image.DATABAR_EXP

DATABAR_EXP barcode type enumeration.

### image.CODABAR

Enumeration of CODABAR barcode types.

### image.CODE39

CODE39 barcode type enumeration.

### image.PDF417

PDF417 barcode type enumeration (currently not working).

### image.CODE93

CODE93 barcode type enumeration.

### image.CODE128

CODE128 barcode type enumeration.
