# 1MaixAmigo

## Overview

SIPEED MaixAmigo is a face recognition product developed based on our M1n module (main CPU: Kendryte K210) that integrates learning, development and commercial use. 
MaixAmigo integrates front and rear cameras, TF card slots, user buttons, TFT displays, a lithium battery, speakers, microphone, expansion interface, etc., Users can use MaixAmigo to easily build a face recognition access control system. It also serves as a development and debugging interface, which can also be used as a powerful AI learning development board.
## MaixAmigo Introduction

### Hardware at a Glance

![MaixAmigo](maix_Amigo.assets/image-20200730120223557.png)

### Onboard Hardware

- 3.5 inch **TFT** screen: resolution **320x480***
- 3.5 inch resistive touch screen：[FT6X36](https://focuslcds.com/content/FT6236.pdf)
- Chip reset button
- Power button: Short press to turn on, long press for 8S to turn off
- Three function buttons
- Grove interface: Onboard 3 Grove digital interfaces, sensors and controllers have unlimited possibilities for expansion
- SP-MOD interface: Onboard 3 more powerful and more scalable SP-MOD digital interfaces, I2C, SPI (standard, two-wire, four-wire mode) and other interfaces can be used

- Support gamepad
- TF card slot: multimedia resource expansion, supports large-capacity storage
- Camera: Equipped with **OV7740 30W** pixel and **GC0328 30W pixel Sensor**
- Type-C interface: USB-TypeC power supply, debugging interface, blind plug
- Power management control unit: AXP173
  - Onboard 600mAh lithium battery, support user charge and discharge control
- Audio driver IC: ES8374
  - Support audio recording and playback
- Three-axis acceleration sensor: MSA301

### Onboard expansion interface

MaixAmigo offers two highly expandable interfaces to users: SP-MOD and Grove interfaces, allowing users ease DIY projects.

#### SP-MOD interface

SP-MOD is sipeed module, simplify PMOD, super module

| interface | interface description |
|---|---|
|SP-MODE interface description|![spmod_interface_1](maix_cube.assets/spmod_interface_1-1595819569921.png)|
|Hardware interface![spmod_interface_2](maix_cube.assets/spmod_interface_2.png)|

#### Grove interface

- Grove module interface

The Grove interface cable has 4 colors, letting users quickly distinguish lines according to their color

![grove_interface](maix_cube.assets/grove_interface.jpg)

| --- | Color | Description |
| --- | --- | --- |
| pin 1 | yellow | (For example, SCL on I2C Grove Connectors) |
| pin 2 | white | (For example, SDA on I2C Grove Connectors) |
| pin 3 | red |   VCC (All Grove interfaces have VCC in red) |
| pin 4 | black |   GND (All Grove interfaces have GND in black |

The Grove module mainly has 4 kinds of interfaces:

1. Grove Digital digital interface: <br/> 
The Grove digital interface consists of four standard wires of Grove plugs. The 
two signal wires are usually called D0 and D1. 
Most modules only use D0, but some (like the LED Bar Grove displays) use both. Usually The core board will call the first Grove connector on the board as D0, and the second as D1. The first connector will be connected to the DO/D1 pin of the main control chip, and the second connector will be connected to The D1/D2 pins of the main control chip, the connectors at the back and so on.

|pin  |Function | Note |
| ---|---|---|
|pin1 | Dn first digital input |
|pin2 | Dn+1 second digital input |
|pin3 | VCC power supply 5V/3.3V |
|pin4 | GND ground |


1. Grove UART:<br/>
    The Grove UART is a special digital input and output interface. 
It uses pins 1 and 2 for serial input and transmission. 
Pin 1 is the RX line (used to receive data, so it is input), where Pin 2 is the TX line (used to transmit data to the Grove module).

|pin  |Function|Note|
| ---|---|---|
|pin1 |RX|Serial receive|
|pin2 |TX|Serial transmit|
|pin3 |VCC|Power supply 5V/3.3V|
|pin4 |GND|ground|

1. Grove I2C:<br/>
    There are many types of I2C Grove sensors available.<br/>
    Grove on MaixAmigo only supports 3.3V sensors

    The Grove I2C connector has a standard layout. Pin 1 is the SCL signal, and pin 2 is the SDA signal


|pin  | Function | Note |
| ---|---|---|
|pin1 | SCL |I2C clock |
|pin2 | SDA |I2C data |
|pin3 | VCC |Power supply, 5V/3.3V |
|pin4 | GND |Ground |

### Onboard I2C device

MaixAmigo onboard I2C sensor/IC

| IC | Device id | I2C address(7bits) |Configuration：SCL: IO_24, SDA: IO_27|
| --- | --- | --- | --- |
|---|I2C Address| <<1|MaixPy read address|
|ES8374 [audio](http://www.everest-semi.com/pdf/ES8374%20PB.pdf)|0x08|0x10|D(16)|
|MSA301 [accelerometer](https://learn.adafruit.com/msa301-triple-axis-accelerometer)|0x13|0x26|D(38)|
|AXP173 [power](http://www.datasheet-pdf.com/PDF/AXP173-Datasheet-X-Powers-966875)|0x68|0x34|D(52)|
