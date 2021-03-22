---
title: 1000 object classification models
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: 1000 object classification models
---


Can recognize 1000 objects

## Instructions

* Use `minimum` version firmware
* [Download model file](https://dl.sipeed.com/MAIX/MaixPy/model), download `mobilenet_0x300000.kfpkg`
* Use `kflash_gui` to burn this file to `Flash`, the default address is `0x300000`
* Save the file [labels.txt](https://github.com/sipeed/MaixPy_scripts/tree/master/machine_vision/mobilenet_1000_class/labels.txt) ([Alternate Link](https://en.bbs.sipeed.com /uploads/default/original/1X/d41ad9dfbe01f228abe726986fbf1baf4e288f2e.zip)) to the file system, see the introductory tutorial (use your ingenuity) for specific methods (reference answer: because there is too much content, if you use the REPL to copy and paste directly, data may be wrong. So use a tool to transfer. The easiest way is to put it on the SD card; if you want to put it in `/flash`, the minimum may not support IDE, you can use `upyloader` to send files)
* Because this model has `4.2MiB`, which is relatively large, so the firmware of `minimum` is used, and the memory used by `GC` is not too large. You can set a smaller size in the following way and leave the memory for the model

```python
from Maix import utils
import machine

utils.gc_heap_size(256*1024)
machine.reset()
```

* Import model

```python
import KPU as kpu
task = kpu.load(0x300000)
```

* Read in labels

```python
f=open('/sd/labels.txt','r')
labels=f.readlines()
f.close()
```

* Initialize the camera, LCD

You can set whether the camera is mirrored and whether the LCD is rotated according to your own hardware installation

Slightly, please refer to the previous tutorial

* Identify objects

```python
fmap = kpu.forward(task, img)
plist=fmap[:]
pmax=max(plist)
max_index=plist.index(pmax)
```

Here, the result of the operation is converted into a `list` object, and then the subscript of the maximum value is found. Through this subscript, we know what the label name is (`labels[max_index]`)


* show result

```python
img = img.draw_string(0, 0, "%.2f: %s" %(pmax, labels[max_index].strip()), color=(255, 0, 0))
lcd.display(img, oft=(0,0))
print(fps)
```


See the complete example [maixpy_scripts](https://github.com/sipeed/MaixPy_scripts/tree/master/machine_vision/mobilenet_1000_class)
