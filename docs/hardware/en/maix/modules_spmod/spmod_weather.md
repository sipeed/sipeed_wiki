# SPMOD - Weather


## Overview

<img src="../../assets/spmod/spmod_weather/demo.gif" align="right" width="500" />

SPMOD - Weather (Weather station module), Integrated Magnetic sensor (QMC7983) and Humidity sensor (BME280)


## SPMOD - Weather Introduction

- Using **Sipeed-SPMOD** interface(2.54mm * 8PIN ),unified MaixPy board interface
- Connect to the board through the SP-MOD I2C interface
- Magnetic sensor: QMC7983 is a 3-axis single chip magnetic sensor integrated with AMR and ASIC,
I2C interface with standard mode and rapid mode,Stable sensitivity in a large operating temperature range,
low power consumption (75uA).
- Sensitivity: ±30 Gauss
- Humidity sensor: BME280 is a humidity sensor that can measure relative humidity, barometric pressure and ambient temperature
- Size:25.0\*10\*2.9mm


## Sensor Introduction:

| Magnetic sensor | QMC7983 |
| --- | --- |
| Supply voltage of external power supply | 2.6V~3.6V |
| Supply current of external power supply | 70uA |
| Sleep Status of Current | <1uA |
| Sensitivity | ±30 Gauss |
| humidity sensor | LSB/mG|
| RMS Noise | 2 mG |
| Interface | I2C,default address 0x2C (Select resistance adjustment) |

-----

| Humidity sensor | BME280 |
| --- | --- |
| Supply voltage of external power supply | 1.71V~3.6V |
| Supply current of external power supply | <633uA |
| Sleep Status of Current | <5uA |
| Humidity sensor： | --- |
| Response time（𝜏63％）| 1s |
| Accuracy tolerance | ±3％  relative humidity |
| Hysteresis | < 2％  relative humidity |
| Pressure sensor： | --- |
| RMS Noise | 0.2 Pa(equiv. to 1.7cm) |
| Temperature coefficient offset | ±1.5 Pa/K(equiv. to ±12.6cm at 1 °C temperature change) |
| Interface | I2C,default address 0x76 Select resistance adjustment) |

###  SPMOD_Weather pin description :

| Pin | Name | Type | Description |
| -------- | -------- | ---- | --- |
| 1  | GND | G | Ground |
| 2  | NC | NC | Not connected |
| 3  | NC | NC | Not connected |
| 4  | SDA | I/O | Receive data signal |
| 5  | 3V3 | V | Power supply(3.3V) |
| 6  | NC | NC | Not connected |
| 7  | NC | NC | Not connected |
| 8  | SCL | I | Transmit clock signal |

<img src="../../assets/spmod/spmod_weather/back.png" width="300" />

## Mode of connection:

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

<img src="../../assets/spmod/spmod_weather/connection.png" height="250">

## Usage

* Process
  1. Send AT instruction
  2. Receive the reply
  3. Determines whether the setup was successful

### C:

  ```c

    fpioa_set_function(Weather_SCL, FUNC_I2C0_SCLK + Weather_I2C_DEVICE * 2); // Weather_SCL: 6;
    fpioa_set_function(Weather_SDA, FUNC_I2C0_SDA + Weather_I2C_DEVICE * 2); // Weather_SDA: 7;

    maix_i2c_init(Weather_I2C_DEVICE, 7, 400000); // Weather_I2C_DEVICE: 0;

    rslt = qmc_init(); // Magnetic sensor QMC7983 init
    rslt = bme280_init(&dev); // Temperature, humidity and pressure sensors BME280 init
    stream_sensor_data_normal_mode(&dev); // read and print sensor data

  ```

### MaixPy:

  ```python

    i2c_bus = I2C(I2C.I2C0, freq=100*1000, scl=6, sda=7) # scl: io_6, sda: io_7

    weather=SPWeather(i2c=i2c_bus) # create sp_weather
    while 1:
        time.sleep_ms(500)
        print(weather.qmc_read_xyz) # QMC7983 read data
        print(weather.bme_values) # BME280 read data

  ```

## Runtime environments:

|  Language  |  Board  | SDK/Firmware version |
| :----: | :------: | :----------------------------- |
|   C    | MaixCube | kendryte-standalone-sdk v0.5.6 |
| MaixPy | MaixCube | maixpy v0.5.1                  |

## Result

* C

    <img src="../../assets/spmod/spmod_weather/log_c.png" height="200">

* MaixPy

    <img src="../../assets/spmod/spmod_weather/log_py.png" height="200">

## Outlook

- SPMOD_Weather Size drawing:

<img src="../../assets/spmod/spmod_weather/sipeed_spmod_weather.png" height="250" />

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
