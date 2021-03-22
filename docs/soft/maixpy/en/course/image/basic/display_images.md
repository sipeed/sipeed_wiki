---
title: Show picture
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy doc: show picture
---



Displaying the picture is very simple. You can use the `lcd` module directly and call the function to display it, as follows:

```python
import lcd, image

lcd.init()

img = image.Image("/sd/test.jpg")
lcd.display(img)
```

But different screen initialization sequence may be different. There are many optional parameters in `lcd.init`. See the description of API document for details. Common ones are as follows

For IPS screens, you need to reverse the color:
```python
lcd.init(type=2)
```

For the screen is not very good, you need to lower the frequency, or if you are good, you need to overclock:
```python
lcd.init(freq = 15000000)
```

In addition, you can also set the rotation direction of the screen:
```python
lcd.rotation(2)
```
The parameters are `0～3`, which respectively represent clockwise rotation `0 degrees` `90 degrees` `180 degrees` `270 degrees`

For more methods, please refer to [lcd document](/api_reference/machine_vision/lcd.md)
