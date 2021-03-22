---
title: Maix.freq
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: Maix.freq
---


Frequency module, support program to modify cpu and kpu frequency

## Method



### freq.set(cpu, pll1, kpu_div)

Set cpu or kpu frequency, after setting it will automatically restart to take effect

Please note that the performance of some peripherals may change after the frequency is set

```python
from Maix import freq
freq.set(cpu ​​= 400, kpu = 400)
```

The configuration file will be saved in the file system `/flash/freq.conf`, please do not modify this file, if the file does not exist, it will be created automatically

#### Parameters

Parameters that are not set will retain their previous values

**Note**: If the `cpu` frequency setting is less than `60MHz`, the default `REPL` serial port baud rate will be set to `9600`

* `cpu`: The cpu frequency you want to set, the range is [26,600] (the chip is up to `800` but has voltage requirements. The series supported by `MaixPy` does not support up to `800`, the default is `400`, different boards May behave differently, not too high for stability

* `pll1`: The output frequency of `pll1`, the value range is [26,1200] (the chip is up to 1800, MaixPy is limited to 1200), the default is `400`

* `kpu_div`: `kpu` clock frequency division, value range [1,16], default `1`. `kpu` frequency = `pll1`/`kpu_div`, for example, if you want to set the `kpu` frequency to `400`, you only need to set `pll1` to `400` and `kpu_div` to `1`. Note the `kpu` frequency range: [26,600]

#### return value

If the frequency has not changed, it returns to null.
If the frequency changes, the machine will automatically restart. Before using this interface, please confirm whether the current situation can be restarted


### freq.get()

Get the currently set frequency parameter

#### return value

`cpu` frequency and `kpu` frequency, returned as a tuple, such as `(400,400)`

### freq.get_cpu()

Get the current frequency of `cpu`

#### return value

`cpu` frequency


### freq.get_kpu()

Get the currently set `kpu` frequency

#### return value

Current `kpu` frequency
