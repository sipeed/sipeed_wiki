---
title: 按键输入
keywords: maixpy3, 按键输入
desc: maixpy3 doc: 按键输入
---

## 使用教程

这里的按键输入，只是适合用于 MaixII-Dock 开发板，

```python
from evdev import InputDevice
from select import select


def detectInputKey(count):
	dev = InputDevice('/dev/input/event0')
	while True:
		select([dev], [], [])
		for event in dev.read():
			# print(event)
			if event.code == 0x02:
				print('press key S1')
			if event.code == 0x03:
				print('press key S2')
			if event.value == 1 and event.code != 0:
				count += 1
				print('press sum:', count)

detectInputKey(0)
```

