---
title: sensor（摄像头）
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: sensor（摄像头）
---


sensor 传感器模块(这里特指摄像头模块)，进行摄像头配置及图像抓取等，用于控制开发板摄像头完成摄像任务。


## 方法

### 初始化单目摄像头

重置并初始化单目摄像头

```python
sensor.reset([, freq=24000000[, set_regs=True[, dual_buff=False]]])
```

#### 参数

* `freq`: 设置摄像头时钟频率，频率越高帧率越高，但是画质可能更差。默认 `24MHz`， 如果摄像头有彩色斑点(ov7740)，可以适当调低比如 `20MHz`
* `set_regs`: 允许程序写摄像头寄存器，默认为 `True`。 如果需要自定义复位序列，可以设置为`False`，然后使用`sensor.__write_reg(addr, value)` 函数自定义写寄存器序列
* `dual_buff`: 默认为`False`。允许使用双缓冲，会增高帧率，但是内存占用也会增加(大约为384KiB)
* `choice`: 指定需要搜索的摄像头类型，ov类型(1)，gc类型(2)，mt类型(3)，不传入该参数则搜索全部类型摄像头

#### 返回值

无

### 重置双目摄像头

重置并初始化双目摄像头

> K210 只有一个 DVP 接口，同一时间只能控制一个 Sensor。但是我们可以借助 `shudown` 方法控制 PWDN 引脚以选择特定的 Sensor。 指定 Sensor 后其余操作不变。详见

例程 2

```python
sensor.binocular_reset()
```

#### 参数

无

#### 返回值

无

### 设置帧大小

用于设置摄像头输出帧大小，k210最大支持VGA格式，大于VGA将无法获取图像

> MaixPy开发板配置的屏幕是320*240分辨率，推荐设置为QVGA格式

```
sensor.set_framesize(framesize[, set_regs=True])
```

#### 参数

* `framesize`: 帧大小
* `set_regs`: 允许程序写摄像头寄存器，默认为 `True`。 如果需要自定义设置帧大小的序列，可以设置为`False`，然后使用`sensor.__write_reg(addr, value)` 函数自定义写寄存器序列

#### 返回值

* `True` : 设置成功
* `False`: 设置错误

### 设置帧格式

用于设置摄像头输出格式

> MaixPy开发板配置的屏幕使用的是RGB565，推荐设置为RGB565格式

```
sensor.set_pixformat(format[, set_regs=True])
```
#### 参数

* `format`: 帧格式
* `set_regs`: 允许程序写摄像头寄存器，默认为 `True`。 如果需要自定义设置像素格式的序列，可以设置为`False`，然后使用`sensor.__write_reg(addr, value)` 函数自定义写寄存器序列

> 可选的帧格式有`GRAYSCALE`, `RGB565`, `YUV422`

#### 返回值

* `True` : 设置成功
* `False`: 设置错误

### 图像捕捉控制

图像捕捉功能控制

```
sensor.run(enable)
```
#### 参数

* `enable`: 1 表示开始抓取图像 0 表示停止抓取图像

#### 返回值

* `True` : 设置成功
* `False`: 设置错误


### 拍摄图像

使用摄像头拍摄一张照片

```
sensor.snapshot()
```
#### 参数

无

#### 返回值

* `img`: 返回的图像对象

### 摄像头控制

关闭摄像头/切换摄像头

```
sensor.shutdown(enable/select)
```
#### 参数

单目摄像头
* `enable`: True 表示开启摄像头 False 表示关闭摄像头

双目摄像头
* `select`: 通过写入 0 或 1 来切换摄像头

#### 返回值

无

### 跳帧

跳过指定帧数或者跳过指定时间内的图像，让相机图像在改变相机设置后稳定下来

```
sensor.skip_frames(n, [, time])
```
#### 参数

* `n`: 跳过 n 帧图像

* `time`: 跳过指定时间，单位为ms

> 若 n 和 time 皆未指定，该方法跳过300毫秒的帧；若二者皆指定，该方法会跳过 n 数量的帧，但将在 time 毫秒后返回

#### 返回值

无

### 分辨率宽度

获取摄像头分辨率宽度

```
sensor.width()
```
#### 参数

无

#### 返回值

* `int`类型的摄像头分辨率宽度



### 分辨率高度

获取摄像头分辨率高度

```
sensor.height()
```
#### 参数

无

#### 返回值

* `int`类型的摄像头分辨率高度

### 获取帧缓冲

获取当前帧缓冲区

```
sensor.get_fb()
```
#### 参数

无

#### 返回值

* `image`类型的对象

### 获取ID

获取当前摄像头ID

```
sensor.get_id()
```
#### 参数

无

#### 返回值

* `int`类型的ID

### 设置彩条测试模式

将摄像头设置为彩条测试模式

> 开启彩条测试模式后，摄像头会输出一彩条图像，常用来检测摄像机总线是否连接正确。
```
sensor.set_colorbar(enable)
```
#### 参数

* `enable`: 1 表示开启彩条测试模式 0 表示关闭彩条测试模式

#### 返回值

无

### 设置对比度

设置摄像头对比度

```
sensor.set_contrast(contrast)
```
#### 参数

* `constrast`: 摄像头对比度，范围为[-2,+2]

#### 返回值

* `True` : 设置成功
* `False`: 设置错误

### 设置亮度

设置摄像头亮度

```
sensor.set_brightness(brightness)
```
#### 参数

* `brightness`: 摄像头亮度，范围为[-2,+2]

####  返回值

* `True` : 设置成功
* `False`: 设置错误

### 设置饱和度

设置摄像头饱和度

```
sensor.set_saturation(saturation)
```
#### 参数

* `constrast`: 摄像头饱和度，范围为[-2,+2]

#### 返回值

* `True` : 设置成功
* `False`: 设置错误

### 设置自动增益

设置摄像自动增益模式

```
sensor.set_auto_gain(enable,gain_db)
```

#### 参数

* `enable`: 1 表示开启自动增益 0 表示关闭自动增益
* `gain_db`: 关闭自动增益时，设置的摄像头固定增益值，单位为dB

> 如果需要追踪颜色，需要关闭自动增益


#### 返回值

无

### 获取增益值

获取摄像头增益值

```
sensor.get_gain_db()
```

#### 参数

无

#### 返回值

* `float`类型的增益值

### 设置水平镜像

设置摄像头水平镜像

```
sensor.set_hmirror(enable)
```

#### 参数

* `enable`: 1 表示开启水平镜像 0 表示关闭水平镜像

#### 返回值

无
### 设置摄像头垂直翻转

设置摄像头垂直翻转

```
sensor.set_vflip(enable)
```

#### 参数

* `enable`: 1 表示开启垂直翻转 0 表示关闭垂直翻转

#### 返回值

无

### 写入寄存器

往摄像头寄存器写入指定值

```
sensor.__write_reg(address, value)
```

#### 参数

* `address`: 寄存器地址
* `value`  ： 写入值

#### 返回值

无

> 请参阅摄像头数据手册以获取详细信息

### 读取寄存器

读取摄像头寄存器值

```
sensor.__read_reg(address)
```

#### 参数

* `address`: 寄存器地址

#### 返回值

* `int`类型的寄存器值

> 请参阅摄像头数据手册以获取详细信息

### set_jb_quality

设置传送给 IDE 图像的质量

```
sensor.set_jb_quality(quality)
```

#### 参数

`quality`：`int` 类型，图像质量百分比（0~100），数字越大质量越好

## 例程


### 例程 1

```python
# 单目摄像头

import sensor
import lcd

lcd.init()

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

while True:
    img = sensor.snapshot()
    lcd.display(img)
```

### 例程 2

```python
# 双目摄像头

import sensor
import image
import lcd
import time

lcd.init()

sensor.binocular_reset()
sensor.shutdown(0)  # 选中sensor 0
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)

sensor.shutdown(1)  # 选中sensor 1
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

while True:
    sensor.shutdown(0)  # 选中sensor 0
    img = sensor.snapshot()
    lcd.display(img)
    time.sleep_ms(100)

    sensor.shutdown(1)  # 选中sensor 1
    img = sensor.snapshot()
    lcd.display(img)
    time.sleep_ms(100)
```
