---
title: 20K 开箱指南
date: 2022-09-16
---

持续施工中

----

Primer 20K 底板有 Lite 和 Dock 两款，这里分开说明一下

## Dock 开箱指南

### 注意事项

首先列出相关注意事项，来避免因为操作不当所产生的问题却花费大量时间但又未解决。

#### 使能核心板

对于 Dock 板，使用的时候需要注意将拨码开关 1 号位开启，以此来使能核心板。
将拨码开关 1 号位拨向下即可。

<img src="./assets/start/switch_1_on.png" alt="switch_1_on" width=20%>
<!-- ![switch_1_on](./assets/start/switch_1_on.png) -->

如果没有将拨码开关 1 号位拨向下，板子上的 0、1 号 LED 会是一直亮着的，且核心板不会正常启动。

<img src="./assets/start/reset_led_on.png" alt="reset_led_on" width=20%>
<!-- ![reset_led_on](./assets/start/reset_led_on.png) -->

#### 设备不工作

默认的包装盒里已经将核心板组装在底板上面了，但是有时候因为一些必要操作需要取下核心板。
然后再次组装回去后发现设备不再工作了，这个时候我们需要确认一下核心板与底板是否连接好。

正确的连接顺序是先将核心板斜插入到底板中，倾斜角度大概如如下图左图所示，确定从上面看到斜插入的核心板与底板接触均匀，可以从金手指裸露出来的均匀程度来判断。

<img src="./assets/start/edge_view.png" alt="edge_view" width=30%>
<img src="./assets/start/top_view.png" alt="top_view" width=25%>

然后轻压翘起来的那一头，可以清脆的听见核心板被底板插槽固定住的声音。

如果按压时候觉得困难的话，可以尝试将核心板两侧稍微打磨一下，来消除由于生产工艺所带来的尺寸误差。

<img src="./assets/start/clean_core_board.png" alt="clean_core_board" width=20%>

将上图红框的两处侧边稍微打磨一下，来减少配合时的困难。

### 开始使用

对于 Dock 底板，默认固件可进行如下操作：
- 按下 S0 按键，复位 RGB 屏幕、摄像头、HDMI 信号复位，且 3、4、5 号三个 LED 会常亮。
- S2 到 S5 按键及 2 号到 5 号拨码开关控制 0、1、2 三个 LED 灯的状态
- 将 OV5640 与 RGB 屏幕连接到板子上（连接时注意断开板子电源），屏幕上面会显示摄像头所捕获到的画面。如果屏幕显示有撕裂现象的话，可以按下 S0 按键来同步一下输出画面。

默认固件中，将 3、4 号两个灯设置为时钟检测信号，可以通过这两个灯的状态来鉴别设备是否工作。


## Lite 开箱指南