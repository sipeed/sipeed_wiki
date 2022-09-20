---
title: MetaSense 系列
---

## MetaSense 是什么?

MetaSense 系列产品搭载 TOF 深度摄像头，目前有 MetaSense-A010 和 MetaSense-A075V 两款产品。
- MS-A010 是一款由 BL702 + 炬佑 100x100 TOF 模组所组成的极致性价比的 TOF 3D 传感器模组，最大支持 100x100 的分辨率和 8 位精度，并且带有 240×135 的 LCD 显示屏可实时预览 color map 后的深度图。
- 而 MS-A075V 是一款具有 RGB 功能的 3D TOF 摄像机模组，该模组可以实现 Linux 免驱的即插即用，实现实时彩色 3D 显示。

<img src="./assets/meta.jpg" alt="summary" width=100%>

购买方式：[众筹预售购买连接](https://igg.me/at/MetaSense )

|              |<p style="white-space:nowrap">MateSense-A010</p> | <p style="white-space:nowrap">MateSense-A075V</p> | 
| :----------- |:----------------------------------------------- | :------------------------------------------------- | 
|              |![me-small](./assets/me_small.jpg)                | ![me-big](./assets/me_big.jpg)                  | 
| 接口         | 1.25mm 串口连接器 \*1<br>Type-C USB2.0 \*1       | 1.25mm 串口连接器 \*1 <br>Type-C USB2.0 \*1         |
| 分辨率       |TOF：100x100@30fps                               | RGB：1600x1200@30fps<br>TOF：320x240@60fps         | 
| 视场角       |RGB：无<br>TOF：70°(H) * 60°(V)                  | RGB：120°<br>TOF：55°(H)*72°(H)                    | 
| <p style="white-space:nowrap">TOF 像素尺寸</p> |                                                 | 15um                                               | 
| 激光发射器   |40nm VCSEL                                       | 940nm,3W                                           | 
| 测量范围     |0.2-2.5m                                         | 0.15-1.5m                                          | 
| 测量精度     |&lt;=1%/cm                                       | &lt;=1%/cm                                         | 


## MetaSense 能做什么？

### 案例：远中近物体实拍

高精度的映射物品摆放距离的差异，点云图可直观感受到更真实的可视化。
<html>
  <img src="./metasense-a010/assets/ms_cloud.jpg" width=48%>
  <img src="./metasense-a075v/assets/mt_cloud.jpg" width=48%>
</html>

### 案例：人流统计

可实时监控人流，进行高精度、大分辨率的统计。
<html>
  <img src="./assets/me_p.jpg" width=48%>
  <img src="./assets/me_pt.jpg" width=48%>
</html>

### 案例：小车避障

可搭载于小车移动并判断画面是否有障碍物，模组自带 LCD 屏幕精准显示距离并做出反应规避障碍物。
![me_car](./assets/me_car.gif)

### 案例：键盘灯跟随

实现超酷炫的键盘灯跟随，实时跟踪手部的位置，再根据手部的位置映射键盘灯。

![ms_lamp](./metasense-a010/assets/ms_lamp.jpg)

### 案例：体积测量

通过 SDK 获取到的模组内参数后，计算粗略点云并累加总体积，达到体积测量的效果。

![mt_volume](./metasense-a075v/assets/mt_volume.jpg)

### 案例：外接 MCU
MS-A010 拥有强大的兼容性，基于串口协议的数据传输。
可外接 K210 bit 这样的单片机开发板或树莓派之类的 linux 开发板来进行二次开发。

![ms_mcu](./metasense-a010/assets/ms_mcu.jpg)

### 案例：接入 ROS1 + ROS2

双支持 ROS 系统，开放 ROS1+ROS2 接入功能包，可快速获得深度数据及深度图。
<html>
  <img src="./assets/me_ross.jpg" height=250 width=49%>
  <img src="./assets/me_rosb.jpg" width=49% height=250>
</html>

## 快速了解 TOF 技术

1. TOF: 是一种距离测量的方法，通过测量发射器和反射器之间的超声波/微波/光等信号的“飞行时间”来计算两者之间的距离。 可以实现TOF测距的是TOF传感器。 最常用的是红外线或激光测距。
2. 物体之间的距离存在差异。 该模块通过捕获的深度值的差异来显示冷色和暖色。冷暖色随着距离的映射而变化，距离越近色调呈暖调（橘红）而越远色调呈冷调（蓝色）。
<html>
  <img src="./assets/tof_two.jpg" height=250 width=49%>
  <img src="./assets/tof.jpg" width=49% height=250>
</html>

## 更多

关于 MS-010 更详细的资料获取：[点击跳转](https://wiki.sipeed.com/hardware/zh/metasense/metasense-a010/metasense-a010.html)
关于 MS-075 更详细的资料获取：[点击跳转](https://wiki.sipeed.com/hardware/zh/metasense/metasense-a075v/metasense-a075v.html)
