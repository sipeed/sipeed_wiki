# MaixSense-A010 Development

## AT Command

| AT                             |                                                                                                                                                                                                                |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| +ISP<br>Image Signal Processor | :0: turn ISP off<br>=1: turn ISP on                                                                                                                                                                            |
| +BINN<br>full binning          | =1: output 100x100 pixel frame<br>=2: output 50x50 pixel frame<br>=4: output 25x25 pixel frame<br>                                                                                                             |
| +DISP<br>display mux           | =0: all off<br>=1: lcd display on<br>=2: usb display on<br>=3: lcd and usb display on<br>=4: uart display on<br>=5: lcd and uart display on<br>=6: usb and uart display on<br>=7: lcd, usb and uart display on |
| +BAUD<br>uart baudrate         | =0: 9600<br>=1: 57600<br>=2: 115200<br>=3: 230400<br>=4: 460800<br>=5: 921600<br>=6: 1000000<br>=7: 2000000<br>=8: 3000000                                                                                     |
| +UNIT<br>quantization unit     | =0: auto<br>=1-10: quantizated by unit(mm)                                                                                                                                                                     |
| +FPS<br>frame per second       | =1-19: set frame per second                                                                                                                                                                                    |
| +Save<br>save config           | : save current configuration                                 |

syntax:

|input|execute|comment|
|---|---|---|
|AT+ISP? |\r|Return to current ISP status|
|AT+ISP=? |\r|Returns the status of all supported ISPs|
|AT+ISP=< MODE >|\r|Select ISP status|


parameter:

|< MODE > | Meaning |
|----|----|
|0 "STOP ISP" |Close the module ISP immediately, stop the IR transmitter|
|1 "LAUNCH ISP" |It is planned to start the module ISP, and the actual drawing needs to wait 1-2 seconds|

### BINN instruction
syntax:

| Enter | Execute | Comment |
|----|----|----|
| AT+BINN? | \r | Return the current BINN status |
| AT+BINN=? | \r | Returns all supported BINN states |
| AT+BINN= < MODE > | \r | Select BINN state |

parameter:

| < MODE > | Meaning |
|----------|------|
| 1 "1x1 BINN" | 1x1 is equivalent to no binning, and the actual output resolution is 100x100. |
| 2 "2x2 BINN" | 2×2 binning, 4 pixels are merged into 1, the actual output resolution is 50×50. The module ISP is planned to be activated, and the actual output needs to wait for 1 to 2 seconds. |
| 4 "4x4 BINN" | 4×4 binning, 16 pixels are merged into one, and the actual output resolution is 25×25. |

### DISP instruction
Please enable it as needed to avoid excessive resource usage
syntax:

| Enter | Execute | Comment |
|------|------|-----|
| AT+DISP? | \r | Return to current DISP status |
| AT+DISP=? | \r | Returns all supported DISP states |
| AT+DISP=< MODE > | \r | Select DISP state |

parameter:


| < MODE > | Meaning |
|----------|------|
| 0 | all off |
| 1 | lcd display on |
| 2 | usb display on |
| 3 | lcd and usb display on |
| 4 | uart display on |
| 5 | lcd and uart display on |
| 6 | usb and uart display on |
| 7 | lcd, usb and uart display on |

### BAUD instruction
syntax:

| Enter | Execute | Comment |
|------|-----|------|
| AT+BAUD? | \r | Return to current BAUD status |
| AT+BAUD=? | \r | Returns all supported BAUD states |
| AT+BAUD=< MODE > | \r | Select BAUD state |

parameter:

| < MODE > | Meaning |
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

### UNIT directive
syntax:

| Enter | Execute | Comment |
|------|------|------|
| AT+UNIT? | \r | Returns the current UNIT value |
| AT+UNIT=? | \r | Returns all supported UNIT values |
| AT+UNIT=< UINT > | \r | Select UNIT value |

parameter:

| < UINT > | Meaning |
|----------|------|
| 0 "DEFAULT UNIT" | The default quantization strategy is used. Due to the tof characteristic, the imaging accuracy at near distances is better than that at far distances. Therefore, the difference at short distances is enlarged, and 5.1*sqrt(x) is used to quantify the original data of 16 bits into 8 bits |
| 1...9 "QUANTIZE UNIT" | Represents quantization in x mm. The smaller the value, the more details and the shorter the visual distance. Please set it properly |

### FPS command
syntax:

| Enter | Execute | Comment |
|------|-----|------|
| AT+FPS? | \r | Returns the current FPS value |
| AT+FPS=? | \r | Returns all supported FPS values |
| AT+FPS=<FPS> | \r | Select FPS value |

parameter:

| < FPS > | Meaning |
|---------|------|
| 1...19 "frame per second" | tof output frame rate, the bigger the better the smoother |

### SAVE instruction
syntax:

| Enter | Execute | Comment |
|------|------|-----|
| AT+SAVE | \r | The current configuration of the TOF camera is cured, and it needs to be reset afterwards |

Multi-machine and AE instructions are recommended to be added

### ANTIMMI instruction

syntax:

| Enter | Execute | Comment |
|------|------|-----|
| AT+ANTIMMI? | \r | Returns the current ANTIMMI state |
| AT+ANTIMMI=? | \r | Returns all supported ANTIMMI states |
| AT+ANTIMMI=< MODE > | \r | Select ANTIMMI state |

parameter:

| < MODE > | meaning |
|----------|------|
| -1       | disable anti-mmi               |
| 0        | auto anti-mmi                  |
| 1-41     | manual anti-mmi usb display on |

### Image Packet Description
When power on, the ISP will be activated by default and display the image on the display screen, and output the image data to uart and usb at the same time
Image data encapsulated into packets (not stabilized):
1. Header 2 bytes: 0X00, 0XFF
2. Packet length 2 bytes: the number of bytes of remaining data in the current packet
3. Other content 16 bytes: including packet serial number, packet length, resolution, etc.
4. Image frame
5. Check 1 byte: the lower eight bits of the "sum" of all previous bytes
6. 1 byte at the end of the packet: 0XDD