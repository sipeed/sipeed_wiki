# PicoRV on nano 9K

> Edit on 2022.07.13

## Preface

There ia an example about picoRV : [Tang Nano 9K github repository](https://github.com/sipeed/TangNano-9K-example/tree/main/picotiny).
In this turtial we just describe how to run the example simply .

## Environment

- Python
- [Gowin IDE](./../../Tang-Nano-Doc/install-the-ide.md)

## Steps

### Program FPGA

- Open picotiny project by `picotiny.gprj` file in TangNano-9K-example\picotiny\project dictionary
- Tick `Use MSPI as regular IO` in Project->Configuration->Place&Route->Dual-Purpose Pin which can be found in the top menu bar
- Right-click Place&Route which is in Process interface and choose Clean&Rerun All 
- Download the generated .fs file to the Embedded Flash of Nano 9K

Then we can use the FPGA like a mcu.

### Download firmware

Execute the following command in TangNano-9K-example\picotiny directory

```python
python .\sw\pico-programmer.py .\example-fw-flash.v COM13
```

The COM13 at the end of command line refers to the serial port number of the development board in the system.
For example, if it is allocated COM14 in your system, you need change it into COM14.

There is a countdown shows `- Waiting for reset -` when you succeed excute the command, in which time it's required to press the S1 button of the development board to complete the programming. 
The succeed done log is as below:

```powershell
\TangNano-9K-example\picotiny> python .\sw\pico-programmer.py .\example-fw-flash.v COM13
Read program with 11760 bytes
  - Waiting for reset -
    ...
Total sectors 3
Total pages 46
Flashing 1 / 3
Flashing 2 / 3
Flashing 3 / 3

Flashing completed
```

Then we can use serial port tools to execute command and use HDMI to display the code interface.
![](./../../../../../zh/tang/Tang-Nano-9K/nano_9k/picorv.jpg)

## End

Other knowledge like cross-compile is not mentioned here, so you should learn to use it by yourself.

