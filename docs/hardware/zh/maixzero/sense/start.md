---
title: M0sense 上手使用
keywords: M0sense
update:
  - date: 2022-11-28
    version: v0.1
    author: wonder
    content:
      - 初次编辑
---

## 初见

通电后板子上的 led 亮起，且屏幕显示出周围环境音的频谱图。

<img src="./assets/start/m0sense_start.jpg" alt="m0sense_start" width="45%">
<img src="./assets/start/m0sense_start_screen.jpg" alt="m0sense_start_screen" width="45%">

## U 盘烧录

对于 M0sense 我们提供了使用虚拟 U 盘拖拽烧录固件的方式。

按住板子上的 BOOT 键后按下 RST 键，就会在电脑上显示一个 U 盘了。

![m0sense_udisk](./assets/start/m0sense_udisk.jpg)

直接将想要烧录的固件拖进 U 盘，成功烧录后 U 盘会自动弹出且板子会自动复位来重新加载新固件。

![m0sense_drag_burn](./assets/start/m0sense_drag_burn.gif)

这边提供了几个 Demo 固件 [点我跳转](https://dl.sipeed.com/shareURL/Maix-Zero/Maix-Zero/7_Example_demos)，可以直接拖拽到 U 盘查看烧录结果，其对应的源码均可在 [github](https://github.com/sipeed/M0sense_BL702_example) 上面获取。

下面是这几个 demo 固件的说明与效果展示

### hello_world.uf2

通过串口软件打开板子串口，可以看到板子打印出的 `Hello,World`

![m0sense_hello_world](./assets/start/m0sense_hello_world.gif) 

### blink_baremetal.uf2

拖拽到 U 盘烧录完后，断电重新连接一下板子，使用串口软件打开串口后 LED 开始闪灯。关闭串口后灯的颜色会维持住。

- 打开串口软件

![m0sense_blink_baremetal_uart](./assets/start/m0sense_blink_baremetal_uart.gif)

- LED 闪灯

![m0sense_blink_baremetal_led](./assets/start/m0sense_blink_baremetal_led.gif) 

### blink_rtos.uf2

这个 demo 效果与上面的一样，只是是基于 RTOS 实现的，上面那个 demo 是裸机程序。

使用串口软件打开串口后才开始闪灯，关闭串口后灯的颜色会保持不变。

- 打开串口软件

![m0sense_blink_baremetal_uart](./assets/start/m0sense_blink_baremetal_uart.gif)

- LED 闪灯

![m0sense_blink_baremetal_led](./assets/start/m0sense_blink_baremetal_led.gif) 

### lcd_flush.uf2

烧录进板子后，板子配套的 lcd 刷屏换颜色。

![m0sense_lcd_flush](./assets/start/m0sense_lcd_flush.gif) 

## SDK 环境搭建