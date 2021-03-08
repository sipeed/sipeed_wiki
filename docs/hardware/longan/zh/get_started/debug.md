Debug 调试
======

## 连接调试器
| 开发板 | 调试器 |
| :----: | :----: |
|  JTDO  |  TDO   |
|  JTDI  |  TDI   |
|  JTCK  |  TCK   |
|  JTMS  |  TMS   |
|  3V3   |  3V3   |
|  GND   |  GND   |

## 修改配置文件
修改工程配置文件 `platformio.ini`， 在下面添加

```ini
debug_tool = jlink
```

根据实际调试器型号选择。目前支持的调试器列表

* `jlink`
* `gd-link`
* `ft2232`
* `sipeed-rv-debugger`
* `altera-usb-blaster`
* `um232h`
* `rv-link`

## 一键调试

切换到 VS CODE 左侧的 `DEBUG` 界面， 点击绿色箭头即可进行调试。

![](../../assets/pio_debug_longan.png).
