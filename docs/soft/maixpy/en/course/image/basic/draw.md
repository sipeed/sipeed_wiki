---
title: drawing and writing
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy doc: drawing, writing
---



There are two ways, the second is recommended

## First, use the `lcd` module to draw directly on the screen

```python
import image, lcd

lcd.init()

lcd.draw_string(0, 0, "hello")
```

For more functions and parameters, please refer to [lcd API Manual](/api_reference/machine_vision/lcd.md)

## Second, use the `image` module to draw in the memory, and use the `lcd.display` function to display the entire picture on the screen after drawing

```python
import image, lcd

lcd.init()

img = image.Image(size=(320, 240))
img.draw_string(0,0, "hello")
lcd.display(img)

```

For more functions and parameters, please see [image API manual](/api_reference/machine_vision/image/image.html), search for `image.draw` on the page to find all drawing functions
For Chinese (multi-language) support, please see [How to display Chinese](/course/image/image_draw_font/image_draw_font.md), or search for "font".
