---
title: Board
keywords: maixpy, k210, AIOT, Edge_calculation, maixpy_start
desc: maixpy  Board
---

> This documnet has passed in Maixpy 0.5.1-128 version

This is a MaixPy board-config module, it unifies Python code at the user level, masking hardware pin differences.

Here is its example code:

```python
from Maix import GPIO
from fpioa_manager import fm
from board import board_info
print(board_info.LED_R)
fm.register(board_info.LED_R, fm.fpioa.GPIO0, force=True)
led_r = GPIO(GPIO.GPIO0, GPIO.OUT)
led_r.value(0)
```

This code can run on all MaixPy device, while its board_info.LED_R is not all the same, which ensures sample code consistency.

## Board configuration method 

Copy the python code from the following links (like config_maix_bit.py), run it in MaixPy IDE, after this you have imported config.json of your downloaded hardware, this config.json will be stored on flash

1. Maix Bit
[config_maix_bit.py](https://github.com/sipeed/MaixPy-v1_scripts/tree/master/board/config_maix_bit.py)

2. Maix Dock
[config_maix_dock.py](https://github.com/sipeed/MaixPy-v1_scripts/tree/master/board/config_maix_dock.py)

3. Maix Go
[config_maix_go.py](https://github.com/sipeed/MaixPy-v1_scripts/tree/master/board/config_maix_go.py)

4. Maix Duino
[config_maix_duino.py](https://github.com/sipeed/MaixPy-v1_scripts/tree/master/board/config_maix_duino.py)

5. Maix Cube
[config_maix_cube.py](https://github.com/sipeed/MaixPy-v1_scripts/tree/master/board/config_maix_cube.py)

6. Maix Amigo
[config_maix_amigo.py](https://github.com/sipeed/MaixPy-v1_scripts/tree/master/board/config_maix_amigo.py)

7. Maix Nano
> There is no peripheral on this hardware, so here is no config code about it.

Your board will reboot after you run config code, after this you can use board_info.BOOT_KEY in your code. In fact board_info.BOOT_KEY is IO16, and we can know its definition from config.json. An error will occour if its resource doesn't not exist. For example, if there is no LED defined in board config.json, an error will occour if you try to run flash an led.

```python
from board import board_info
# see board/readme.md to config your sipeed's hardware.
print(board_info.BOOT_KEY, board_info.BOOT_KEY == 16)
```

## Custome your own firmware

You can use this interface code to adapt your hardware, refer to [MaixPy_scripts/board](https://github.com/sipeed/MaixPy-v1_scripts/tree/master/board) to see the reference configuration file to know configuration method.

## board usage

import configuration

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

and its result:
```shell
PIN10: 10
BOOT_KEY: 16
WIFI_TX: 6
WIFI_RX: 7
WIFI_EN: 8
```

> This is all
