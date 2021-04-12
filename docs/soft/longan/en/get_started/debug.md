Debugging Longan Nano
======

## Connect the debugger
| Development board | Debugger |
| :----: | :----: |
|  JTDO  |  TDO   |
|  JTDI  |  TDI   |
|  JTCK  |  TCK   |
|  JTMS  |  TMS   |
|  3V3   |  3V3   |
|  GND   |  GND   |

## Modify the configuration file
Modify the project configuration file `platformio.ini`, add below

```ini
debug_tool = jlink
```

Select according to the actual debugger model. List of currently supported debuggers

* `jlink`
* `gd-link`
* `ft2232`
* `sipeed-rv-debugger`
* `altera-usb-blaster`
* `um232h`
* `RV-Link`

## One-click debugging

VSCode switch to the left side of the `DEBUG` screen, click the green arrow to debug.

![](../../assets/pio_debug_longan.png).
