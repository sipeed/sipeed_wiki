---
title: 1000 种物体分类模型
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 1000 种物体分类模型
---


可以识别 1000 种物体

## 使用方法

* 使用`minimum` 版本固件
* [下载模型文件](https://dl.sipeed.com/fileList/MAIX/MaixPy/model/mobilenet_0x300000.kfpkg)
* 使用 `kflash_gui` 烧录模型文件到 `Flash`, 这个模型文件回自动烧录到地址0x300000上，不需要手动选择地址
* 保存文件[labels.txt](https://github.com/sipeed/MaixPy_scripts/tree/master/machine_vision/mobilenet_1000_class/labels.txt) ([备用链接](https://en.bbs.sipeed.com/uploads/default/original/1X/d41ad9dfbe01f228abe726986fbf1baf4e288f2e.zip)) 到文件系统，具体方法见入门教程（发挥你的聪明才智）（参考答案：因为内容太多，如果使用 REPL 直接复制粘贴可能数据会出错， 所以要使用 工具传输。最简单的是放到 SD 卡； 如果要放到 `/flash`，minimum 可能不支持 IDE， 可以使用`upyloader`发送文件）
* 因为这个模型有`4.2MiB`，比较大，所以使用了`minimum`的固件，同时保证`GC`使用的内存不要太大，可以通过以下方式设置小一点,把内存留给模型使用

```python
from Maix import utils
import machine

utils.gc_heap_size(256*1024)
machine.reset()
```

* 导入模型

```python
import KPU as kpu
task = kpu.load(0x300000)
```

* 读入 labels

```python
f=open('/sd/labels.txt','r')
labels=f.readlines()
f.close()
```

* 初始化摄像头, LCD

可以根据自己的硬件安装情况设置摄像头是否镜像，以及 LCD 是否旋转等

略，请参考前面的教程

* 识别物体

```python
fmap = kpu.forward(task, img)
plist=fmap[:]
pmax=max(plist)
max_index=plist.index(pmax)
```

这里把运行的结果转换成了一个`list`对象， 然后找到了最大值的下标， 通过这个下标我们就知道标签名是什么了（`labels[max_index]`）


* 显示结果

```python
img = img.draw_string(0, 0, "%.2f : %s" %(pmax, labels[max_index].strip()), color=(255, 0, 0))
lcd.display(img, oft=(0,0))
print(fps)
```


完整例程看 [maixpy_scripts](https://github.com/sipeed/MaixPy_scripts/tree/master/machine_vision/mobilenet_1000_class)


