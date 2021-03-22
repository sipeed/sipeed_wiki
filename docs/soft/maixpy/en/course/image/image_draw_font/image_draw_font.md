---
title: How to display Chinese
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: how to display Chinese
---


MaixPy supports loading Unicode fonts. Unicode (Unicode, Universal Code, Single Code) is an industry standard in the field of computer science.

The following languages ​​are supported:

* A Latin capital letter "A" A
* ß Latin lowercase letter "Sharp S" ß
* þ Lowercase Latin letter "Thorn" þ (not supported by small fonts)
* Δ Uppercase Greek letter "Delta" Δ
* Й Capital Cyrillic "Short I" Й
* ק Hebrew letter "Qof" ק
* م Arabic letter "Meem" م
* ๗ Thai number 7 ๗
* ቐ Ethiopian syllable "Qha" ቐ
* あ Hiragana in Japanese "A" あ
* ア Japanese Katakana "A" ア
* Ye Simplified Chinese character "叶" Ye
* Turn Traditional Chinese characters "转" to turn
* 엽 Korean syllable text "Yeob" 엽

This functional interface is completed by using the `image.Image()` object. Please use the latest version of MaixPy firmware September 2, 2020.

## Font interface

Use draw_font to print font strings, similar to `img.draw_font(10, 20, 8, 8, b'/x20/xFC/xFC/x2C/xAC/x4C/x4D/xA3')`.

```python
import lcd, image
lcd.init()
img = image.Image()
tmp = b'/x20/xFC/xFC/x2C/xAC/x4C/x4D/xA3'
img.draw_font(10, 20, 8, 8, tmp, scale=1, color=(255, 255, 255))
lcd.display(img)
```

Example reference [image_draw_font.py](https://gitee.com/Sipeed/maixpy_scripts/tree/master/multimedia/gui/image/demo_draw_font/image_draw_font.py).

## Font library interface

Please use font_load / font_free to load or release the font first. This will improve the function of draw_string and support loading from the `xx.Dzk` file and Flash address. After that, draw_string will print the string through the font. Currently only `ASCII` / ` UTF-8` encoding.

> Attached font file [0xA00000_font_uincode_16_16_tblr.Dzk](https://gitee.com/Sipeed/maixpy_scripts/tree/master/multimedia/gui/image/demo_draw_font/tools/0xA00000_font_uincode_16_16_tblr.Dzk)

```python
import lcd, image
lcd.init()
img = image.Image()
# image.font_load(image.UTF8, 16, 16, 0xA00000)
image.font_load(image.UTF8, 16, 16,'/sd/0xA00000_font_uincode_16_16_tblr.Dzk')
img.draw_string(20, 90, b'こんにちは、世界', x_spacing=2, mono_space=1)
image.font_free()
lcd.display(img)
```

Example reference [image_draw_string.py](https://gitee.com/Sipeed/maixpy_scripts/tree/master/multimedia/gui/image/demo_draw_font/image_draw_string.py).

## display effect

![view_image_font](./view_image_font.jpg)

## Font Tool

We will use [FontGenerator.zip](https://gitee.com/Sipeed/maixpy_scripts/tree/master/multimedia/gui/image/demo_draw_font/tools/FontGenerator.zip) in the root directory to export the font corresponding to the font, please See the figure below to complete the export operation.

1. Select the font encoding type as Unicode encoding, which will support the languages ​​of most countries.

   ![image-20200902180913322](./image-20200902180913322.png)

2. Select the scanning mode, which is the scanning and printing direction of 5 horizontal, up and down, then left and right fonts.

   ![image-20200902181130459](./image-20200902181130459.png)

3. Create the font library after configuring the required font style as shown in the figure below.

   ![image-20200902181311553](./image-20200902181311553.png)

4. Just save it in DZK format, the font data access method is shown in the text description

   ![image-20200902181442677](./image-20200902181442677.png)

## Font tool

> Warning: It is not recommended to use font tools, and those who do not understand should not use it.

Use [Pc2Lcd2002.zip](https://gitee.com/Sipeed/maixpy_scripts/tree/master/multimedia/gui/image/demo_draw_font/tools/Pc2Lcd2002.zip) in the directory to get the character string of the font.

1. Confirm that the software is in character mode.

![image-20200902175614964](./image-20200902175614964.png)



2. Set as shown in the figure to export the desired string.

   ​ ![image-20200902180153452](./image-20200902180153452.png)

3. After filling in the text, click to generate the font.

   ![image-20200902175948599](./image-20200902175948599.png)

4. Extract the font string and use it.

   ![image-20200902180505263](./image-20200902180505263.png)

```
 This (0) is (1) test (2) test (3)

/x00/x20/x10/x17/x00/x02/xF1/x10/x10/x10/x11/x12/x14/x28/x47/x00/x80/x40/x40/xFC/x10/x10/x20/xA0/x40 /xA0/x10/x08/x08/x00/xFE/x00 This 0
/x1F/x10/x10/x1F/x10/x10/x1F/x00/xFF/x01/x11/x11/x11/x29/x45/x83/xF0/x10/x10/xF0/x10/x10/xF0/x00/xFE /x00/x00/xF8/x00/x00/x00/xFE is 1
/x00/x27/x14/x14/x85/x45/x45/x15/x15/x25/xE5/x21/x22/x22/x24/x08/x04/xC4/x44/x54/x54/x54/x54/x54/x54 /x54/x54/x04/x84/x44/x14/x08 test 2
/x00/x20/x10/x10/x07/x00/xF0/x17/x11/x11/x11/x15/x19/x17/x02/x00/x28/x24/x24/x20/xFE/x20/x20/xE0/x20 /x10/x10/x10/xCA/x0A/x06/x02 try 3
```

> You can use the graphics mode to draw your favorite font graphics, supporting 32 * 32 graphics.
>
> ![image-20200902181645277](./image-20200902181645277.png)
