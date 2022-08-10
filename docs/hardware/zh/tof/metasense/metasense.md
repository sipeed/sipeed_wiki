# MetaSense-A300V

## 概述

MetaSense-A300V 是由 Sipeed 所推出的一款具有 RGB 功能的 3D TOF 摄像机模组。
该模组可以实现免驱的即插即用，实现实时彩色3D显示。

### TOF 简介

TOF 是一种测距的方法，通过测量超声波/微波/光等信号在发射器和反射器之间的 “飞行时间” 来计算出两者之间的距离。能够实现 TOF 测距的传感器就是 TOF 传感器。种类较多，使用较多的是通过红外或者激光进行测距的 TOF 传感器。

## 相关参数

| 条目         | 参数                                                               | 补充 |
| :----------- | :----------------------------------------------------------------- | :--- |
| 外形尺寸     | 模块本体：36\*36\*13.5mm<br>带散热模块：36\*36\*23.5mm                  |      |
| 重量         | 带散热模组约40克                                                   |      |
| 主控参数     | 主频 1.5G<br> 单核 Cortex-A7<br>支持NEON加速,集成浮点协处理器 |      |
| 内存         | 128MB RAM<br>128MB ROM                                             |      |
| 接口         | 1.25mm 串口连接器 \*1 <br>Type-C USB2.0 \*1                        |      |
| 分辨率       | RGB：1600x1200@30fps<br>TOF：320x240@60fps                         |      |
| 视场角       | RGB:120°<br>TOF:55°(H)*72°(H)                                      |      |
| TOF 像素尺寸 | 15um                                                               |      |
| 激光发射器   | 940nm,3W                                                           |      |
| 测量范围     | 0.15-1.5m                                                          |      |
| 测量精度     | <=1%/cm                                                            |      |


## 使用例程

### 流程
- 注意事项
- 例程指南
- 互动配置
### 注意事项

上电前一定要确保网络环境中没有使用 192.168.233.0/24 地址段，MS-A300V 会使用 RNDIS 并设置自己的 ip 地址为 192.168.233.233。Windows 系统需安装驱动才可正常运行。
  
  [点击下载 Windows 驱动](https://dl.sipeed.com/shareURL/TOF/MetaSense/Drivers)
  [点击查看 Windows 安装驱动方法](./install_drivers.md)

### 例程指南

1. 把设备 MS-A300V 使用 Type-c 线与电脑链接, MS-A300V 的风扇会开始工作，产品正面镜头处就会闪烁红灯。

2. 此时可打开浏览器输入 http://192.168.233.233 预览 3D 点云图，上电后有延迟需等待一段时间，系统和程序才会启动完成。
3. 使用网页上位机快速预览 演示图（正面和侧面）：
   
![](assets/tof-1.jpg)
![](assets/tof-2.jpg)
4. 可选预览深度伪彩点云，右上角打开交互面板。第一行取消勾选RGB_Map即可。
![](assets/tof-3.jpg)

### 互动配置
上位机交互面板提供了一系列配置和功能，可以实时预览变动的效果。

![](assets/tof-4.jpg)

现简单说明一下各个控件的功能。
- RGB_Map多选框 开关RGB映射，即关闭时只显示深度伪彩点云，打开时显示RGB映射点云。
- colorMap下拉栏 提供了几个伪彩映射选项(即cmap)，推荐使用jet，RGB_Map关闭时有效。
- deepRangeMax和deepRangeMin滑动条是设定cmap的映射范围的，即只有位于deepRangeMin和deepRangeMax之间的数值（深度值）会通过cmap，RGB_Map关闭时有效。
- NormalPoint多选框 开关显示正常点（TOF成像会有无效点，对应的相反描述），需要打开。
- OE_Points多选框 开关显示OE点，建议关闭。
- UE_Points多选框 开关显示UE点，建议关闭。
- Bad_Points多选框 开关显示无效点，建议关闭。
- SpatialFilter多选框 开关空间滤波，基于下面的SpatialFilterSize值和SpatialFilterType指定的算法进行处理。
- TemporalFilter多选框 开关时间滤波，基于下面的TemporalFilteralpha值做了一个时间上的平均。
- TemporalFilteralpha滑动条 设定时间滤波所需时长，适中即可，可自行尝试体验其它效果。
- SpatialFilterType下拉栏 设定空间滤波算法，提供高斯滤波（Gaussian）和双边滤波（Bilateral），双边滤波性能要求较高，不建议使用。
- SpatialFilterSize滑动条 设定空间滤波所需范围，适中即可，可自行尝试体验其它效果。
- FlyingPointFilter多选框 开关飞点过滤，基于下面的FlyingPointThreshold值作为过滤阈值，超过阈值的将被过滤掉，建议适中配置，否则有效点也会被剔除。
  
## 相关问题

### 无设备显示

要确保设备供电充足：对于台式机建议使用主机背部的 USB 接口；使用 USB hub 的话建议使用带有额外供电的；另外建议使用 USB 3.0 的数据口，因为 USB 2.0 驱动供电可能不足。