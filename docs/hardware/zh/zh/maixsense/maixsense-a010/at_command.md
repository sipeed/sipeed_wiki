# MaixSense-A010 二次开发手册

## AT 指令表

| AT                             |                                                                                                                                                                                                                |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| +ISP<br>Image Signal Processor | :0: turn ISP off<br>=1: turn ISP on                                                                                                                                                                            |
| +BINN<br>full binning          | =1: output 100x100 pixel frame<br>=2: output 50x50 pixel frame<br>=4: output 25x25 pixel frame<br>                                                                                                             |
| +DISP<br>display mux           | =0: all off<br>=1: lcd display on<br>=2: usb display on<br>=3: lcd and usb display on<br>=4: uart display on<br>=5: lcd and uart display on<br>=6: usb and uart display on<br>=7: lcd, usb and uart display on |
| +BAUD<br>uart baudrate         | =0: 9600<br>=1: 57600<br>=2: 115200<br>=3: 230400<br>=4: 460800<br>=5: 921600<br>=6: 1000000<br>=7: 2000000<br>=8: 3000000                                                                                     |
| +UNIT<br>quantization unit     | =0: auto<br>=1-10: quantizated by unit(mm)                                                                                                                                                                     |
| +FPS<br>frame per second       | =1-19: set frame per second                                                                                                                                                                                    |
| +Save<br>save config           | : save current configuration                                 |

句法：

|输入|执行|注释|
|---|---|---|
|AT+ISP? |\r|返回当前ISP状态|
|AT+ISP=? |\r|返回所有支持的ISP状态|
|AT+ISP=< MODE >|\r|选择ISP状态|


参数：

|< MODE >  | 含义 |
|----|----|
|0 "STOP ISP"   |立即关闭模组ISP，停止IR发射器|
|1 "LAUNCH ISP" |计划启动模组ISP，实际出图需等待1～2秒|

### BINN指令
句法：

| 输入 | 执行 | 注释 |
|----|----|----|
| AT+BINN? | \r | 返回当前BINN状态 |
| AT+BINN=? | \r | 返回所有支持的BINN状态 |
| AT+BINN= < MODE > | \r | 选择BINN状态 |

参数：

| < MODE > | 含义 |
|----------|------|
| 1 "1x1 BINN" | 1x1相当于无binning，实际出图分辨率为100x100。 |
| 2 "2x2 BINN" | 2×2binning，4个像素点合并成1个，实际出图分辨率为50×50计划启动模组ISP，实际出图需等待1～2秒。|
| 4 "4x4 BINN" | 4×4binning，16个像素点合并成1个，实际出图分辨率为25×25。 |


### DISP指令
请按需开启，避免资源过度占用
句法：

| 输入 | 执行 | 注释 |
|------|------|-----|
| AT+DISP? | \r | 返回当前DISP状态 | 
| AT+DISP=? | \r | 返回所有支持的DISP状态 |
| AT+DISP=< MODE > | \r | 选择DISP状态 |

参数：


| < MODE > | 含义 |
|----------|------|
| 0 | all off |
| 1 | lcd display on |
| 2 | usb display on |
| 3 | lcd and usb display on |
| 4 | uart display on |
| 5 | lcd and uart display on |
| 6 | usb and uart display on |
| 7 | lcd, usb and uart display on |

### BAUD指令
句法：

| 输入 | 执行 | 注释 |
|------|-----|------|
| AT+BAUD? | \r | 返回当前BAUD状态 |
| AT+BAUD=? | \r | 返回所有支持的BAUD状态 |
| AT+BAUD=< MODE > | \r | 选择BAUD状态 |

参数：

| < MODE > | 含义 |
|----------|------|
| 0 | 9600 |
| 1 | 57600 |
| 2 | 115200 |
| 3 | 230400 |
| 4 | 460800 |
| 5 | 921600 |
| 6 | 1000000 |
| 7 | 2000000 |
| 8 | 3000000 |

### UNIT指令
句法：

| 输入 | 执行 | 注释 |
|------|------|------|
| AT+UNIT? | \r | 返回当前UNIT值 |
| AT+UNIT=? | \r | 返回所有支持的UNIT值 |
| AT+UNIT=< UINT > | \r | 选择UNIT值 |

参数：

| < UINT > | 含义 | 
|----------|------|
| 0 "DEFAULT UNIT" | 采用默认量化策略，因tof特性导致成像近处精度优于远距离处，故放大近距离处差异，采用5.1*sqrt(x)将16bit的原数据量化为8bit |
| 1...9 "QUANTIZE UNIT" | 代表以x mm为单位进行量化，取值越小细节越多，同时可视距离越短，请合理设置 |

### FPS指令
句法：

| 输入 | 执行 | 注释 |
|------|-----|------|
| AT+FPS? | \r | 返回当前FPS值 |
| AT+FPS=? | \r | 返回所有支持的FPS值 |
| AT+FPS=<FPS> | \r | 选择FPS值 |

参数：

| < FPS > | 含义 |
|---------|------|
| 1...19 "frame per second" | tof出图帧率，越大越流畅 |

### SAVE指令
句法：

| 输入 | 执行 | 注释 |
|------|------|-----|
| AT+SAVE | \r | 固化TOF摄像头当前配置，事后需要复位 |

多机和 AE 指令建议加入

### ANTIMMI指令
句法：

| 输入 | 执行 | 注释 |
|------|------|-----|
| AT+ANTIMMI? | \r    | 返回当前ANTIMMI状态       |
| AT+ANTIMMI=? | \r   | 返回所有支持的ANTIMMI状态  |
| AT+ANTIMMI=< MODE > | \r | 选择ANTIMMI状态      |

参数：

| < MODE > | 含义 |
|----------|------|
| -1       | disable anti-mmi               |
| 0        | auto anti-mmi                  |
| 1-41     | manual anti-mmi usb display on |

### 图像数据包说明
上电默认启动ISP并在显示屏显示图像，同时输出图像数据到uart和usb
图像数据封装成包（未稳定）：
1. 包头2字节：0X00、0XFF 
2. 包长度2字节：当前包剩余数据的字节数 
3. 其他内容16字节：包括包序号、包长度、分辨率等等 
4. 图像帧 
5. 校验1字节：之前所有字节的“和”低八位 
6. 包尾1字节：0XDD

AT+UNIT? 可查询当前UNIT值。

设p为图像帧各像素值，主要有以下两种情况：

- 若UNIT非0，则该像素离TOF距离计算方法为 `p` x `UNIT` ;

- 若UNIT为0，则该像素离TOF距离计算方法为 (`p`/5.1)^2 。
