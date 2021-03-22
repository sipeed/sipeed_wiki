---
title: Use of SP_LCD1.14
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: Use of SP_LCD1.14
---


<img src="../../../assets/hardware/module_spmod/sp_lcd1.14.png"/>

SP_LCD has a 1.14' inch LCD, 8P FPC (0.5mm pitch) interface TFT LCD screen, 180° viewing angle.

## Parameters

* Screen size: 1.14 inches
* Resolution: 240*135
* Color: 132 RGB channels
* Communication interface: SPI
* Effective display area: 21.7mm * 10.8mm
* Working voltage: 2.5V~4.8V
* Working temperature: -30°C~85°C

For detailed module information, please refer to [LCD114 Specification and Data Manual](http://api.dl.sipeed.com/shareURL/MAIX/HDK/sp_mod/sp_lcd114)

## Instructions

1. Preparation: The development board with the latest firmware, sp_lcd114 module.

2. Run: Connect the module, modify the configuration surrounded by config in [Sample Code](https://github.com/sipeed/MaixPy_scripts/tree/master/modules/spmod/sp_lcd114), the module will display the picture after running.

The procedure is as follows:

```python
# init
ips = SPLCD114(spi1, cs, dc, rst, busy, IPS_WIDTH, IPS_HEIGHT, IPS_MODE)

# create an'image' and fill it
img = image.Image()
img.draw_rectangle(80, 80, 30, 30)

# display
ips.display(img)
```

The main steps are:

* Initialization (the parameters from left to right are: SPI object, chip select pin, reset pin, busy flag pin, screen width, screen height, screen orientation).

* Create Image.
  
* Call display to display the picture (the incoming parameter is the Image object).
