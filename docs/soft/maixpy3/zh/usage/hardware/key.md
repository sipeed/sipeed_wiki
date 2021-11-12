---
title: 事件输入
keywords: maixpy3, 事件输入
desc: maixpy3 doc: 事件输入
---

## 使用事件输入

> 以下代码由于 Maixpy3 还在优化中，可能不能运行，具体的代码到 [github](https://github.com/sipeed/MaixPy3) 上查看

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

