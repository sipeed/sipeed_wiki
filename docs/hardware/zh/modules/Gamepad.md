# Sipeed Gamepad

## 概述

![](./../../assets/spmod/spmod_amigo_hendle/Gamepad141.jpg)

采用主控芯片： GD32F150G

通信接口：IIC（8P座子或者Grove-4P-2.0mm座子）

板载10个按键（每个按键都连接到独立的GPIO）

板载指示灯

## 硬件参数

| 项目 | 参数 |
| --- | --- |
| MCU | GD32F150G（Arm Cortex-M3）|
| 主频 | 72Mhz |
| 存储 | 64KB Flash, 8KB SRAM |
| 按键 | 10个按键（每个按键都连接到独立的GPIO） |
| 下载接口 | SWD下载 |
| 晶振 | 24MHz无源晶振 |
| LED | 板载1个电源指示灯和2个LED |
| USB接口 | 板载1个USB TYPE-C 母座（连接到MCU的USB） |

![](./../../assets/spmod/spmod_amigo_hendle/amigo_handle_5.png)

## 手柄接口

![](./../../assets/spmod/spmod_amigo_hendle/amigo_handle_3.jpg)

![](./../../assets/spmod/spmod_amigo_hendle/amigo_handle_4.jpg)

| 引脚序号 | 引脚名称 | 类型 | 引脚说明      |
| -------- | -------- | ---- | ------------- |
| 1  | GND | G  | 模块电源地 |
| 2  | NC | NC  | 悬空引脚，无功能 |
| 3  | NC | NC  | 悬空引脚，无功能 |
| 4  | SDA | I/O  | 模块I2C串行数据引脚 |
| 5  | 3V3 | V  | 模块电源输入正 |
| 6  | NC | NC  | 悬空引脚，无功能 |
| 7  | NC | NC  | 悬空引脚，无功能 |
| 8  | SCL | I  | 模块I2C串行时钟引脚 |

链接方式

单手柄：
![](./../../assets/spmod/spmod_amigo_hendle/Gamepad.143.jpg)

双手柄：

![等待完善](./../../assets/spmod/spmod_amigo_hendle/amigo_handle_6.png)
## 软件描述
| 项目| 参数 |
| --- | --- |
| 开发环境 | Maixpy IDE、 PlatformIO IDE |
| 开发语言 | C语言、 python |
| 通讯协议 | IIC |

> GD32F150G源码和例程 [https://github.com/sipeed/GD32F150-I2C-Handle](https://github.com/sipeed/GD32F150-I2C-Handle)

### 手柄测试

单手手柄输入测试
```python 
from machine import I2C
import nes, lcd
from sound import CubeAudio
import sys, time
from fpioa_manager import fm
from Maix import FPIOA, GPIO


# B A SEL START UP DOWN LEFT RIGHT  X   Y
# 1 2 4   8     16  32   64   128  254 253
i2c = I2C(I2C.I2C2, freq=400*1000, sda=27, scl=24)
lcd.init(freq=15000000)
lcd.register(0x36, 0x20
state = 0
import time
i = 0
while True:
    dev = i2c1.scan()
    print(dev)
    dev = i2c2.scan()
    print(dev)
    time.sleep(0.5)
    try:
        #i2c.writeto(0x4A, b'0')
        tmp = (i2c1.readfrom(0x4A, 2))
        print('{}-{}'.format(int(tmp[0]), int(tmp[1])))
    except Exception as e:
        print(e)
```

双手柄输入测试
```python
from machine import I2C
import nes, lcd
from sound import CubeAudio
import sys, time
from fpioa_manager import fm
from Maix import FPIOA, GPIO


# B A SEL START UP DOWN LEFT RIGHT  X   Y
# 1 2 4   8     16  32   64   128  254 253
i2c = I2C(I2C.I2C2, freq=400*1000, sda=27, scl=24)
lcd.init(freq=15000000)
lcd.register(0x36, 0x20
state = 0
import time
i = 0
while True:
    dev = i2c1.scan()
    print(dev)
    dev = i2c2.scan()
    print(dev)
    time.sleep(0.5)
    try:
        #i2c.writeto(0x4A, b'0')
        tmp = (i2c1.readfrom(0x4A, 2))
        print('{}-{}'.format(int(tmp[0]), int(tmp[1])))
    except Exception as e:
        print(e)
    try:
        #i2c.writeto(0x42, b'0')
        tmp = (i2c2.readfrom(0x42, 2))
        print('{}-{}'.format(int(tmp[0]), int(tmp[1])))
    except Exception as e:
        print(e)
```

测试代码输出

```python
    0-252       #没有输出
    1-252       #按下 B 键
    2-252       #按下 A 键
    4-252       #按下 SEL 键  
    8-252       #按下 START 键   
    16-252      #按下 UP 键 
    32-252      #按下 DOWN 键  
    64-252      #按下 LEFT 键
    128-252     #按下 RIGHT 键
    0-254       #按下 X 键
    0-253       #按下 Y 键
```

### 游戏测试

[MaixPy-NES](/soft/maixpy/zh/api_reference/media/nes.md)


## 资料下载

[Gamepad](https://dl.sipeed.com/shareURL/MAIX/HDK/Sipeed-Gamepad)
