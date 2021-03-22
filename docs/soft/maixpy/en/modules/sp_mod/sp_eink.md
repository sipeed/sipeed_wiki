---
title: Use of SP_EINK
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: use of SP_EINK
---


<img src="../../../assets/hardware/module_spmod/sp_eink.png"/>

The GDEW0154M09 used by the SP_EINK module is a 1.54” electronic ink screen with a 24P FPC (0.5mm pitch) interface.

## Parameters

* Screen size: 1.54 inches
* Effective display area: 27.6mm * 27.6mm
* Color: black/white/red display
* Communication interface: SPI
* Working temperature: -40°C~85°C
* Working voltage: 2.3V~3.6V

For detailed module information, please refer to [EINK Specification and Data Manual](http://api.dl.sipeed.com/shareURL/MAIX/HDK/sp_mod/sp_eink)

## Instructions

1. Preparation: The development board with the latest firmware, sp_eink module.

2. Run: Connect the module, modify the configuration surrounded by config in [Sample Code](https://github.com/sipeed/MaixPy_scripts/tree/master/modules/spmod/sp_eink), the module will display the picture after running.

The procedure is as follows:

```python
# init
epd = SPEINK(spi1, cs, dc, rst, busy, EPD_WIDTH, EPD_HEIGHT)
epd.init()

# create red image
img_r = image.Image()
img_r = img_r.resize(EPD_WIDTH, EPD_HEIGHT)
img_r.draw_line(0, 0, 100, 100)

# create black/white image
img_bw = image.Image()
img_bw = img_bw.resize(EPD_WIDTH, EPD_HEIGHT)
img_bw.draw_line(100, 50, 200, 100)

# display
epd.display(img_r, img_bw)

# sleep mode
epd.sleep()
```

The main steps are as follows:

* Create SPEINK object (parameters: SPI object, chip select pin, reset pin, busy flag pin, horizontal resolution, vertical resolution, screen rotation angle (0, 90, 180, 270)), initialize.

* Create red and black images, set to screen size and fill the image.

* Call display (parameters are: red image, black image), the screen will flash and the image will be displayed at this time.
  
* Go to sleep.
