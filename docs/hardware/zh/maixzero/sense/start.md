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

这边提供了几个 Demo 固件 [点我跳转](https://dl.sipeed.com/shareURL/Maix-Zero/Maix-Zero/7_Example_demos)，可以直接拖拽到 U 盘查看烧录结果。

| 固件名称                  | 效果 |
| ------------------------- | ---- |
| blink_baremetal.uf2       |  ![blink_baremetal_uart](./assets/start/blink_baremetal_uart.gif) <video id="video" controls="" preload="none" poster="作者(图片地址)">
<source id="mp4" src="./assets/start/m0sense_.mp4" type="video/mp4">
</video>
|
| blink_rtos.uf2            |      |
| hello_world.uf2           |      |
| lcd_flush.uf2             |      |
| single_button_control.uf2 |      |


