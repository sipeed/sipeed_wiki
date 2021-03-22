---
title: FFT运算
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: FFT运算
---

FFT快速傅里叶变换模块，对输入数据进行傅里叶变换并返回相应的频率幅值, FFT快速傅里叶运算可以将时域信号转换为频域信号

## 模块函数

###  运算函数

输入时域数据并进行傅里叶变换

```
import FFT
res = FFT.run(data, points, shift)
```

####  参数

* `data`: 输入的时域数据，`bytearray` 类型  

* `points`: FFT运算点数，仅支持64, 128，256和512点

* `shift`: 偏移，默认为0  

####  返回值

`res`: 返回计算后的频域数据，以 `list` 类型呈现，该列表有 `points` 个元组，每个元组有 2 个元素，第一个元素为实部，第二个为虚部 

### 频率函数

FFT

```
res = FFT.freq(points, sample_rate)
```

####  参数

* `points`: 计算点数

* `sample_rate`: 采样率

####  返回值

`res` : 返回一个列表，该列表存放的进行运算后后所有频率点的频率值

### 幅值函数

用于计算 FFT 运算后的各个频率点的幅值，目前用作测试，用户可以自己在python自行写幅值处理函数

```
amp = FFT.amplitude(FFT_res)
```

#### 参数

`FFT_res`: 函数 `run` 运行后的结果


#### 返回值

`res` : 返回一个列表，该列表存放了各个频率点的幅值

### 例程

采集声音并进行FFT运算，将运算后的数据在屏幕上显示为柱状图

例示代码： https://github.com/sipeed/MaixPy_scripts/blob/master/hardware/demo_fft_spectrum.py

