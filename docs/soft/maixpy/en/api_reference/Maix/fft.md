---
title: FFT operation
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: FFT operation
---

FFT fast Fourier transform module, which performs Fourier transform on input data and returns the corresponding frequency amplitude. FFT fast Fourier operation can convert time domain signal into frequency domain signal

## Module function

### Operation function

Input time domain data and perform Fourier transform

```
import FFT
res = FFT.run(data, points, shift)
```

#### Parameters

* `data`: input time domain data, `bytearray` type

* `points`: FFT calculation points, only supports 64, 128, 256 and 512 points

* `shift`: shift, default is 0

####  return value

`res`: Returns the calculated frequency domain data, presented as a `list` type. The list has `points` tuples, each tuple has 2 elements, the first element is the real part, and the second is Imaginary part

### Frequency function

FFT

```
res = FFT.freq(points, sample_rate)
```

#### Parameters

* `points`: Calculate points

* `sample_rate`: sample rate

####  return value

`res`: return a list, the list stores the frequency values ​​of all frequency points after the operation

### Amplitude function

Used to calculate the amplitude of each frequency point after FFT operation. It is currently used as a test. Users can write their own amplitude processing functions in python

```
amp = FFT.amplitude(FFT_res)
```

#### Parameters

`FFT_res`: the result of function `run`


#### return value

`res`: Return a list that stores the amplitude of each frequency point

### Routine

Collect sound and perform FFT calculation, and display the calculated data as a histogram on the screen

Example code: https://github.com/sipeed/MaixPy_scripts/blob/master/hardware/demo_fft_spectrum.py
