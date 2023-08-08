---
title: Tang Primer 20K 开箱指南
keywords: FPGA, Primer, Tang, 20K
update:
  - date: 2022-09-16
    version: v0.1
    author: wonder
    content:
      - 首次编辑
---

持续施工中

----

Primer 20K 底板有 Lite 和 Dock 两款，这里分开说明一下

## Dock 开箱指南

### 注意事项

首先列出相关注意事项，来避免因为操作不当所产生的问题却花费大量时间但又未解决。

#### 使能核心板

对于 Dock 板，使用的时候需要注意将拨码开关 1 号位开启，以此来使能核心板。

| 使能核心板 | 未使能状态 | 补充说明 |
| --- | --- | --- |
|<img src="./assets/start/switch_1_on.png" alt="switch_1_on" width=100%>|<img src="./assets/start/reset_led_on.png" alt="reset_led_on" width=100%> | 未使能核心板的话板子上的 0、1 号 LED 会一直亮着，且核心板不会正常启动。|

#### 设备不工作

默认的包装盒里已经将核心板组装在底板上面了，但是有时候因为一些必要操作需要取下核心板。
然后再次组装回去后发现设备不再工作了，这个时候我们需要确认一下核心板与底板是否连接好。

正确的连接顺序是先将核心板斜插入到底板中，倾斜角度大概如如下图左图所示。确定从上面看到斜插入的核心板与底板均匀接触，可以从金手指裸露出来的均匀程度来判断。

<img src="./assets/start/edge_view.png" alt="edge_view" width=45%>
<img src="./assets/start/top_view.png" alt="top_view" width=35%>

然后轻压翘起来的那一头，可以清脆的听见核心板被底板插槽固定住的声音。

如果按压时候觉得困难的话，可以尝试将核心板两侧稍微打磨一下，来消除由于生产工艺所带来的尺寸误差。

<img src="./assets/start/clean_core_board.png" alt="clean_core_board" width=20%>

将上图红框的两处侧边稍微打磨一下，来减少配合时的困难。

#### 硬件改版说明

对于 Dock 底板，可以从如下图所指的位置来了解当前自己所使用的板子版本。

![version](./assets/start/dock-version.png)

比如上面这张图的板子的版本号为 V3708

下面是有问题的版本修正：

##### V3708

LED2 与 LED3 的丝印错误，应当为：

| 外设 | 正确引脚 | 错误丝印 |
| ---  | --- | --- |
| LED2 | N16 | B14 |
| LED3 | N14 | N16 |

### 开始使用

对于 Dock 底板，默认固件可进行如下操作：
- 按下 S0 按键，复位 RGB 屏幕、摄像头、HDMI 信号复位，且 3、4、5 号三个 LED 会常亮。
- S2 到 S5 按键及 2 号到 5 号拨码开关控制 0、1、2 三个 LED 灯的状态
- 将 OV5640 摄像头与 4.3寸 RGB 屏幕连接到板子上（连接时注意断开板子电源），屏幕上面会显示摄像头所捕获到的画面。如果屏幕显示有撕裂现象的话，可以按下 S0 按键来同步一下输出画面。

默认固件中，将 3、4 号两个灯设置为时钟检测信号，可以通过这两个灯的状态来鉴别设备是否工作。

### 实战使用

[点一个灯](./examples/led.md)

### 相关问题

使用中碰到问题可以先前往 [常见问题](https://wiki.sipeed.com/hardware/zh/tang/Tang-Nano-Doc/questions.html) 来查看解决方法。

## Lite 开箱说明

### 硬件版本说明

对于 Lite 底板，可以从如下图所指的位置来了解当前自己所使用的板子版本。

![lite-version](./assets/start/lite-version.png)

比如上面这张图的板子的版本号为 3710

下面是有问题的版本修正：

#### 3710

底板 R8 与 P9 之间为 P8 引脚。参考右图左上方，已标明

<div>
<img src="./assets/lite-up.png" alt="lite-up" width=45%>
<img src="./assets/lite-back.png" alt="lite-back" width=45%>
</div>

### 实战使用

[点一个灯](https://wiki.sipeed.com/news/others/20k_lite_start/20k_lite_start.html)

### 相关问题

使用中碰到问题可以先前往 [常见问题](https://wiki.sipeed.com/hardware/zh/tang/Tang-Nano-Doc/questions.html) 来查看解决方法。