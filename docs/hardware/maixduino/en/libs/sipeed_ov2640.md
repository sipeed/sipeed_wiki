OV2640 - Camera
=====

The OV2640 Camera chip is a low voltage CMOS imagesensor that provides the full functionality of a single-chip UXGA (1632x1232 - 2 MegaPixel) camera and image processor.

----
## Datasheet

[OV2640-DATASHEET](http://dl.sipeed.com/MAIX/HDK/Chip_DS/OV2640-DATASHEET.pdf)

----
## snapshot()

### Description
`snapshot()` returns an image.

### Syntax

`snapshot()` 

### Returns
`uint8_t*` pixels - if pixels format is RGB565: return RGB565 pixels with every uint16_t one pixel, e.g. RED: 0xF800

### Example Code

see example [selfie](https://github.com/sipeed/Maixduino/blob/master/libraries/Sipeed_OV2640/examples/selfie/selfie.ino)

```
#include <Sipeed_OV2640.h>
#include <Sipeed_ST7789.h>

SPIClass spi0(SPI0); // MUST be SPI0 for Maix series on board LCD
Sipeed_ST7789 lcd(320, 240, spi0);

Sipeed_OV2640 camera(FRAMESIZE_QVGA, PIXFORMAT_RGB565);

void setup()
{
    Serial.begin(115200);

    lcd.begin(15000000, COLOR_RED);
    // lcd.invertDisplay(true); // comment this out when camera is on the backside

    Serial.print("camera init ");
    if(!camera.begin())
      Serial.println("failed");
    else
      Serial.println("success");
    camera.run(true);
}

void loop()
{
  uint8_t* img = camera.snapshot();
  if (img == nullptr || img == 0)
    Serial.println("snap failed");
  else
    lcd.drawImage(0, 0, camera.width(), camera.height(), (uint16_t*)img);
}
```