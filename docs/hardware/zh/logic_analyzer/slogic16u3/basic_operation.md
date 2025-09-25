---
title:  基础操作
keywords: LogicAnalyzer, SLogic
update:
  - date: 2025-09-25
    version: v0.1
    author: Serika
    content:
      - Release docs
---

SLogic16 U3共有2个功能（SLogic Mode/DFU Mode）。
这篇文档用来指导如何上手使用。

## 硬件概览

### 硬件示意图
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>CSS Indentation</title>
  <style>
    .indent {
      margin-left: 0ch; /* wideof 0 characters */
    }
  </style>
</head>
<body>
  <details class="indent">
    <summary><font color="#4F84FF">点击此处查看SLoigc16 U3的硬件示意图览
</font></summary>
    <img src="./assert/Hardware_OverView.png">
  </details>
</body>
<br>
</html>

**同轴线子板**/**杜邦线组** 的插入方向见上图，连接线上的三角标记 **▴** 对准外壳上的三角标记 **▴** 即可。

其中MODE小孔中有一个隐藏式按键，可以用取卡针捅入后按下。

ACT是**状态指示灯**，具体状态见下方[相应章节](#指示灯颜色与功能)描述。

### 快速开始

首先使用**PC USB** → **USB-A/C to USB-C** → 连接 **SLogic**

将目标设备的待测信号点连接至SLogic任意空闲CH端口，并确保待测设备的GND与SLogic的GND相连接。

> 注意SLogic的GND线需要离待测点的位置越近越好，哪怕更近1cm也可能会增加采样
质量

## MODE按键功能

上电后默认功能是 **SLogic**，正常情况下[ACT指示灯](#指示灯颜色与功能)显示青色。
同时出现一个新的 ***USB3*** 装置：**SLogic16 U3**（逻辑分析仪）

![slogic16_u3](./assert/slogic_u3.png)

**按下MODE按键**切换功能，切换成功后可以看到**指示灯变化：** 红灯慢闪。
同时出现一个新的 ***USB2*** 装置：**SLogic16 DFU** （升级模式）

![slogic16_u2](./assert/slogic_u2.png)

再次按下则切换回**SLogic**，如此往复循环。

## 指示灯颜色与功能

指示灯是一颗3色RGB，每一种颜色代表一种状态，不同状态组合指示当前设备状态

| 颜色       | 蓝色    | 绿色    | 红色      |
| ---------- | ------ | ------- | --------  | 
| 功能       | 电源   | USB LINK | 运行指示  | 

下边表是不同颜色对应的正常运行时候的装置状态

| 状态       | 颜色            | 备注        |
| ---------- | -------------- | ----------- | 
| 正常连接    | 青色           | 蓝+绿       |
| 正在传输    | 青色+红色快闪   | 蓝+绿+红快闪 |
| DFU模式    | 青色+红色慢闪   | 蓝+绿+红慢闪 |

❗下边的指示灯颜色对应的装置的异常状态
| 状态       | 颜色            | 备注        |
| ---------- | -------------- | ----------- | 
| USB连接失败 | 蓝色           | 只亮蓝灯     |

> 注意：任何时候绿灯如果熄灭都意味着USB连接出现问题，请尝试重新连接以解决问题。此时红灯的状态没有意义。

- 装置的异常状态的检查清单
    - 使用的USB线缆不支持USB3（常见于手机充电线）；
    - PC的USB接口不支持USB3；
    - 连接到了Desktop PC 机箱的前面板的USB；
    - 连接到了不兼容的USB hub（请尽量保证SLogic直连PC USB）；
    - 连接到了供电能力不足的USB端口；


## 更新固件

首先[进入DFU MODE](#mode按键功能)。
TBD

## FAQ

TBD