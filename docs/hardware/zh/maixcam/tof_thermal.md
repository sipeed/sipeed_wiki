---
title: ToF/热成像模块介绍
---


## PMOD_Thermal32

PMOD_Thermal32 模块是符合PMOD接口标准的低成本热成像模块，可以直接插入MaixCAM Pro的PMOD插槽上使用，并和与可见光摄像头组合，实现双光融合的功能。

|**模块名**  | PMOD_Thermal32   |
|-----------|------------------|
|**分辨率**  |32x24|
|**测温范围**|-40～450摄氏度|
|**视角**   | 55°x35°|
|**帧率**   | 1~30fps|
|**接口**   | I2C |

PMOD_Thermal32安装方式  
![PMOD_Thermal32安装方式](../../assets/maixcam/pmod_thermal32.jpg)

单热成像伪彩显示   
![单热成像伪彩显示 ](../../assets/maixcam/th32_1.jpg)

热成像+可见光融合显示
![热成像+可见光融合显示 ](../../assets/maixcam/th32_2.jpg)

参考使用代码：  
https://github.com/sipeed/MaixPy/blob/main/examples/ext_dev/sensors/thermography_mlx90640/mlx90640_example.py



## PMOD_TOF100

PMOD_TOF100 模块是符合PMOD接口标准的低成本面阵TOF模块，可以直接插入MaixCAM Pro的PMOD插槽上使用，并和与可见光摄像头组合，实现双光融合的功能。

|**模块名**  | PMOD_TOF100   |
|-----------|------------------|
|**分辨率**  |100x100, 50x50, 25x25|
|**测距范围**|0.2~2.5m|
|**视角**   | 70°Hx60°V|
|**激光发射器**| 940nm VCSEL|
|**帧率**  |100x100 6fps, 50x50 22fps, 25x25 30fps|
|**接口**   | SPI |

PMOD_TOF100安装方式  
![PMOD_TOF100安装方式](../../assets/maixcam/pmod_tof100.jpg)

单深度伪彩显示   
![单深度伪彩显示 ](../../assets/maixcam/tof100_1.jpg)

深度+可见光融合显示
![深度+可见光融合显示 ](../../assets/maixcam/tof100_2.jpg)

参考使用代码：  
https://github.com/sipeed/MaixPy/blob/main/examples/ext_dev/sensors/tof100/tof100_example.py


