# MaixCube

## Overview

  SIPEED MaixCube is a face recognition product developed based on our M1n module (main control: Kendryte K210) that integrates learning, development and commercial use.
  <br/>MaixCube integrates camera, TF card slot, user buttons, TFT display, lithium battery, speaker microphone, expansion interface, etc. Users can use Maix Cube to easily build a face recognition access control system, and also reserve development and debugging Interface, it can also be used as a powerful AI learning development board.

## MaixCube appearance and function introduction

### Appearance list

![maixcube_product_appearance](maix_cube.assets/maixcube_product_appearance.png)

-1.3 inch **IPS** screen: resolution** 240*240**
-Reset button
-Power button: short press to turn on, long press *8S* to turn off
-Grove interface: **Grove** digital interface, sensor, controller expansion possibilities~
-SP-MOD interface: equipped with a more powerful and scalable **SP-MOD** digital interface, I2C, SPI (standard, two-wire, four-wire mode) and other interfaces can be used
-TF card slot: multimedia resource expansion, support large capacity storage
-Camera: equipped with **0V7740** **30W** pixels **Sensor**
-Type-C interface:
-Three-way button:

### Introduction to onboard functions

![maixcube_resources](maix_cube.assets/maixcube_resources.png)


-Power management control unit: AXP173
  -Onboard 200mAh lithium battery, support user charge and discharge control
-Audio driver IC: ES8374
  -Support audio recording and playback
-Three-axis acceleration sensor: MSA301
-Camera OV7740:
-1.3 IPS LCD:
-RGB: Two RGB LEDs on board
-USB Type-C: Type-C interface, positive and negative blind plug


### Onboard expansion interface

Maix Cube opens two highly expanded interfaces to users: SP-MOD and Grove interfaces,
Users can easily DIY

#### SP-MOD interface

SP-MOD is sipeed module, simplify PMOD, super module

| Interface | Interface description |
|---|---|
|SP-MODE interface description|![spmod_interface_1](maix_cube.assets/spmod_interface_1-1595819569921.png)|
|Hardware Interface|![spmod_interface_2](maix_cube.assets/spmod_interface_2.png)|

#### Grove interface

-Grove module interface

The Grove interface cable has 4 colors, users can quickly distinguish according to the color
![grove_interface](maix_cube.assets/grove_interface.jpg)

| --- | Color | Description |
| --- | --- | --- |
| pin 1 | Yellow | (e.g. SCL on I2C Grove Connectors) |
| pin 2 | White | (For example, SDA on I2C Grove Connectors) |
| pin 3 | Red | VCC (All Grove ports are VCC in red) |
| pin 4 | black | GND (all Grove ports are GND in red) |

Grove module mainly has 4 kinds of interfaces:

1. Grove Digital digital interface:<br/>
    The Grove digital interface consists of four standard wires of Grove plugs.<br/>
    The two signal lines are usually called D0 and D1.<br/>
    Most modules only use D0, but some (like LED Bar Grove displays) use both. Usually the core board will call the first Grove connector on the board as D0, and the second as D1. The connector will be connected to the DO/D1 pin of the main control chip, the second connector will be connected to the D1/D2 pin of the main control chip, and the following connectors will be deduced by analogy.

|pin |Function | Note |
| ---|---|---|
|pin1 | Dn First digital input |
|pin2 | Dn+1 Second digital input |
|pin3 | VCC power supply pin 5V/3.3V |
|pin4 | GND ground |


1. Grove UART :<br/>
    The Grove UART is a special digital input and output interface.<br/>
    It uses pins 1 and 2 for serial input and transmission. <br/>
    Pin 1 is the RX line (used to receive data, so it is input),
    Among them, pin 2 is the TX line (used to transmit data to the Grove module).

|pin |Function|Note|
| ---|---|---|
|pin1 |RX|Serial Receive|
|pin2 |TX|Serial transmission|
|pin3 |VCC|Power supply pin 5V/3.3V|
|pin4 |GND |Ground|

1. Grove I2C:<br/>
    There are many types of I2C Grove sensors available.<br/>The Grove on MaixCube only supports 3.3V sensors

  The Grove I2C connector has a standard layout. Pin 1 is the SCL signal, and pin 2 is the SDA signal

|pin | Function | Note |
| ---|---|---|
|pin1 | SCL |I2C clock |
|pin2 | SDA |I2C data |
|pin3 | VCC |Power supply pin, 5V/3.3V |
|pin4 | GND |Ground |

### Onboard I2C device

MaixCube onboard I2C sensor/IC

| IC | Device id | I2C address (7-bit address) | Configuration: SCL: IO_30, SDA: IO_31|
| --- | --- | --- | --- |
|---|I2C Address| <<1|MaixPy read address|
|ES8374|0x08|0x10|D(16)|
|MSA301|0x13|0x26|D(38)|
|AXP173|0x68|0x34|D(52)|
