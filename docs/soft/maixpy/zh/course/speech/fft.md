---
title: FFT 信号处理
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: FFT 信号处理
---


FFT 即快速傅里叶变换（Fast Fourier Transform），将时域信号转化为频域信号，应用范围非常广，例如消除音频图像噪声。

## 使用方法

k210 带有硬件 FFT 模块，支持 64 点、 128 点、 256 点以及 512 点的 FFT。

* 导入 FFT 模块

```python
import FFT
```

* 输入时域数据（例如音频数据）并进行 FFT 运算

```python
res = FFT.run(data, points, shift)
```

相关 API 解释请参考[FFT-API](../../api_reference/Maix/fft.md)

## 例程

采集声音并进行 FFT 运算，将运算后的数据在屏幕上显示为柱状图: [demo_fft_spectrum](https://github.com/sipeed/MaixPy_scripts/blob/master/hardware/demo_fft_spectrum.py)

效果：
<iframe width="600" height="350"  src="//player.bilibili.com/player.html?aid=44617696&cid=78104545&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>


