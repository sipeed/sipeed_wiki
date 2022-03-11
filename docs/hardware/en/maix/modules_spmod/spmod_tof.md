# SPMOD - TOF


## Overview

<img src="../../assets/spmod/spmod_tof/sp_tof.png" style="padding-right:100px;" align="right" width="" height="500" />

SPMOD_TOF(TOF module) uses VL53L0X .

## SPMOD - TOF Introduction

- Using **Sipeed-SPMOD** interface(2.54mm * 8PIN )，unified MaixPy board interface
- Using SP-MOD I2C to communicate with TOF module
- ToF module:The VL53L0X sensor used in this module is an I2C interface and a long distance single point flight time measurement (ToF) sensor. It has high performance and high reliability,
- With the longest distance of 4m and the highest refresh rate of 50Hz
- With the red laser pointer, the laser is activated through XSHUT and connected by SP_MOD.
- Size:25.0\*10\*3.15mm

### VL53L0X Introduction:

| Features: | --- |
| --- | -- |
| Max ranging distance | 4000mm |
| Refresh rate | 50Hz |
| Measuring angle | 27°|
| Communication Interface | I2C |
| Range of working temperature | -40℃ - 80℃ |
| Sleep Status of Current | 5uA |
| Supply voltage of external power supply | 2.8~3.5V |
| Supply current of external power supply | Depends on the working conditions of the module, usually less than 20mA |

###  SPMOD_TOF pin description:

| Pin | Name | Type | Description | |
| --- | --- | --- | --- | --- |
| 1 | GND | G  | Ground |
| 2 | IRQ | I  | Interrupt input pin, connected to GPIO1 of VL53L0X |
| 3 | NC  | NC | Not connected |
| 4 | SDA | I/O | Receive data signal |
| 5 | 3V3 | V  | Power supply(3.3V) |
| 6 | NC  | NC | Not connected |
| 7 | SHT | I  | Xshutdown pin(active low)|
| 8 | SCL | I  | Transmit clock signal |


<img src="../../assets/spmod/spmod_tof/back.png" height="300" />

- Mode of connection:

|  MCU:FUN(IO)  | SP_RFID |
| :-----------: | :-----: |
| I2C:SDA(IO_7) |   SDA   |
|   NC(IO_15)   |   NC    |
|   NC(IO_20)   |   IRQ   |
|   NC(IO_21)   |   NC    |
| GPIOHS(IO_8)  |   SHT   |
| I2C:SCL(IO_6) |   SCL   |
|   2.8~3.5V    |  3.3V   |
|      GND      |   GND   |

<img src="../../assets/spmod/spmod_tof/connection.png" height="250">


## Usage

* Process

  1. Initializatin
  2. Adjust(option)
  3. Get distance

### C:

  ```c

  //set io mux
    fpioa_set_function(VL53L0X_SCL, FUNC_I2C0_SCLK + VL53L0X_I2C_DEVICE * 2);
    fpioa_set_function(VL53L0X_SDA, FUNC_I2C0_SDA + VL53L0X_I2C_DEVICE * 2);
    fpioa_set_function(VL53L0X_SHT, FUNC_GPIOHS0 + VL53L0X_SHT);

    gpiohs_set_drive_mode(VL53L0X_SHT, GPIO_DM_OUTPUT);

    //i2c init
    maix_i2c_init(VL53L0X_I2C_DEVICE, 7, VL53L0X_I2C_FREQ_KHZ * 1000);

    while (vl53l0x_init(&vl53l0x_dev)) {
          printf("VL53L0X init error!!!\r\n");
          msleep(500);
    }

    printf("VL53L0X init success!\r\n");

    // adjusting
    printf("VL53L0X adjusting\r\n");
    vl53l0x_calibration_test(&vl53l0x_dev);

    // get distance
    printf("VL53L0X start work\r\n");
    vl53l0x_general_test(&vl53l0x_dev);

  ```

### MaixPy:

  ```python| 工作电压 | 2.6V~3.5V (选用红色激光时： 2.8V~3.3V) |

    fm.register(VL53L0X_SHT, fm.fpioa.GPIOHS0, force=True)
    XSHUT = GPIO(GPIO.GPIOHS0, GPIO.OUT)

    i2c = I2C(VL53L0X_I2C_NUM, freq=VL53L0X_FREQ, scl=VL53L0X_SCL, sda=VL53L0X_SDA)

    # create obj and read distance
	  tof = VL53L0X(i2c)
	  while True:
      mm = tof.read()
      utime.sleep_ms(100)
      print(mm)

  ```
## Runtime enviroments

| Language |  Boards  |      SDK/firmware version      |
| :------: | :------: | :----------------------------: |
|    C     | MaixCube | kendryte-standalone-sdk v0.5.6 |
|  MaixPy  | MaixCube |         maixpy v0.5.1          |

### Result

* C

  <img src="../../assets/spmod/spmod_tof/log_c.png" height="200" />

* MaixPy

  - [None]

## Transplant

Modify the following parameters to fit other K210 boards.

* C

```c
  // board_config.h
  #define VL53L0X_I2C_DEVICE 0 // i2c device number
  #define VL53L0X_I2C_FREQ_KHZ 100 // i2c frequence
  #define VL53L0X_SCL 6 // scl
  #define VL53L0X_SDA 7 // sda
  #define VL53L0X_SHT 8 // sht
```

* MaixPy

```python
  ################### config ###################
  VL53L0X_I2C_NUM = const(I2C.I2C0)
  VL53L0X_FREQ = const(100000)
  VL53L0X_SCL = const(6)
  VL53L0X_SDA = const(7)
  VL53L0X_SHT = const(8)
  ##############################################
```


## Outlook

- SPMOD_TOF Size drawing:

<img src="../../assets/spmod/spmod_tof/sipeed_spmod_tof.png" height="250" />

-----

## Resource Link

| Resource | --- |
| --- | --- |
| Website | www.sipeed.com |
| Github | [https://github.com/sipeed](https://github.com/sipeed) |
| BBS | [http://bbs.sipeed.com](http://bbs.sipeed.com) |
| Wiki | [http://maixpy.sipeed.com](http://wiki.sipeed.com/maixpy) |
| Sipeed model shop | [https://maixhub.com/](https://maixhub.com/) |
| SDK Relevant information | [dl.sipeed.com/MAIX/SDK](dl.sipeed.com/MAIX/SDK) |
| HDK Relevant information | [dl.sipeed.com/MAIX/HDK](dl.sipeed.com/MAIX/HDK) |
| E-mail(Technical Support and Business Cooperation) | [Support@sipeed.com](mailto:support@sipeed.com) |
| telgram link | [https://t.me/sipeed](https://t.me/sipeed) |
