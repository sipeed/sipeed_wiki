---
title: FFT signal processing
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: FFT signal processing
---


FFT is Fast Fourier Transform (Fast Fourier Transform), which converts time-domain signals into frequency-domain signals, and has a wide range of applications, such as eliminating audio image noise.

## Instructions

k210 is equipped with a hardware FFT module, which supports 64-point, 128-point, 256-point and 512-point FFT.

* Import FFT module

```python
import FFT
```

* Input time domain data (such as audio data) and perform FFT operation

```python
res = FFT.run(data, points, shift)
```

For related API explanation, please refer to [FFT-API](../../api_reference/Maix/fft.md)

## Routine

Collect sound and perform FFT calculation, and display the calculated data as a histogram on the screen: [demo_fft_spectrum](https://github.com/sipeed/MaixPy_scripts/blob/master/hardware/demo_fft_spectrum.py)

effect:
<iframe width="600" height="350" src="//player.bilibili.com/player.html?aid=44617696&cid=78104545&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
