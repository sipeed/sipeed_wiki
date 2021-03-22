---
title: Board
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: Board
---


> **This document has passed the test of MaixPy 0.5.1-128. **

This is a MaixPy board-level configuration module, which can unify Python code at the user level, thereby shielding many hardware pin differences.

The effect is as follows:

```python
from Maix import GPIO
from fpioa_manager import fm
from board import board_info
print(board_info.LED_R)
fm.register(board_info.LED_R, fm.fpioa.GPIO0, force=True)
led_r = GPIO(GPIO.GPIO0, GPIO.OUT)
led_r.value(0)
```

And this code supports all MaixPy hardware to run at the same time, and the printed board_info.LED_R is not the same, it ensures the consistency of the sample code.

### Board configuration method

Copy the python code corresponding to the following link (such as config_maix_bit.py), put it in the IDE edit box and run it to complete the import of the "your hardware" configuration item (config.json), which will be stored on the flash Configuration file.

After running the configuration code, it will automatically restart. At this time, board_info.BOOT_KEY can be called in the code. In fact, board_info.BOOT_KEY refers to IO 16. The corresponding definition can be seen in config.json. If the resource does not exist, an error will be reported. If there is no hardware defined by LED, an error will be reported when the running LED is on.

```python
from board import board_info
# see board/readme.md to config your sipeed's hardware.
print(board_info.BOOT_KEY, board_info.BOOT_KEY == 16)
```

### Maix Bit

[config_maix_bit.py](https://github.com/sipeed/MaixPy_scripts/tree/master/board/config_maix_bit.py)

### Maix Dock

[config_maix_dock.py](https://github.com/sipeed/MaixPy_scripts/tree/master/board/config_maix_dock.py)

### Maix Go

[config_maix_go.py](https://github.com/sipeed/MaixPy_scripts/tree/master/board/config_maix_go.py)

### Maix Duino

[config_maix_duino.py](https://github.com/sipeed/MaixPy_scripts/tree/master/board/config_maix_duino.py)

### Maix Cube

[config_maix_cube.py](https://github.com/sipeed/MaixPy_scripts/tree/master/board/config_maix_cube.py)

### Maix Amigo

[config_maix_amigo.py](https://github.com/sipeed/MaixPy_scripts/tree/master/board/config_maix_amigo.py)

### Maix Nano

> This has no hardware peripherals... So don't ask why there is no configuration code.

### Create your own hardware

You can use this interface code to adapt to your hardware. For the configuration method, please refer to [MaixPy_scripts/board](https://github.com/sipeed/MaixPy_scripts/tree/master/board) There is a configuration file for your reference.

### How to use board

Import configuration:

```python
from board import board_info
board_info.load({
    'PIN10': 10,
    'BOOT_KEY': 16,
    'WIFI_TX': 6,
    'WIFI_RX': 7,
    'WIFI_EN': 8,
})
print('PIN10:', board_info.PIN10)
print('BOOT_KEY:', board_info.BOOT_KEY)
print('WIFI_TX:', board_info.WIFI_TX)
print('WIFI_RX:', board_info.WIFI_RX)
print('WIFI_EN:', board_info.WIFI_EN)
```

Call result:

```shell
PIN10: 10
BOOT_KEY: 16
WIFI_TX: 6
WIFI_RX: 7
WIFI_EN: 8
```

> That's it.
