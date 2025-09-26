---
title:  基础操作
keywords: LogicAnalyzer, SLogic, Basic Usage
update:
  - date: 2025-09-25
    version: v0.1
    author: Serika
    content:
      - Release docs
---

SLogic16 U3共有2个功能（SLogic U3 Mode/DFU Mode）。
这篇文档用来指导如何上手使用。

## 硬件概览

### 配件一览

![unboxing_0](./assets/unboxing_0.png)

- **SLoigc16 U3** **主机** x1
- **包装内附件:** （注：杜邦线和同轴线为二选一） 
    - <!DOCTYPE html>
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
          <summary><font color="#4F84FF"><b>2x6P 公对母杜邦线</b> x2
      </font></summary>
          <img src="./assets/Hardware_OverView.png">
        </details>
      </body>
      </html>
    - <!DOCTYPE html>
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
          <summary><font color="#4F84FF"><b>2x4P 同轴线模组</b> x2
      </font></summary>
          <img src="./assets/Hardware_OverView.png">
        </details>
      </body>
      </html>
    - <!DOCTYPE html>
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
          <summary><font color="#4F84FF"><b>逻辑分析仪测试夹</b> x16
      </font></summary>
          <img src="./assets/Hardware_OverView.png">
        </details>
      </body>
      </html>
    - <!DOCTYPE html>
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
          <summary><font color="#4F84FF"><b>0.5m A+C to C USB3 数据线</b> x1
      </font></summary>
          <img src="./assets/Hardware_OverView.png">
        </details>
      </body>
      </html>
    - <!DOCTYPE html>
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
          <summary><font color="#4F84FF"><b>不锈钢取卡针</b> x1
      </font></summary>
          <img src="./assets/Hardware_OverView.png">
        </details>
      </body>
      </html>
    - <!DOCTYPE html>
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
          <summary><font color="#4F84FF"><b>说明卡片</b> x1
      </font></summary>
          <img src="./assets/Hardware_OverView.png">
        </details>
      </body>
      </html>
    - <!DOCTYPE html>
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
          <summary><font color="#4F84FF"><b>拉链收纳包</b> x1
      </font></summary>
          <img src="./assets/Hardware_OverView.png">
        </details>
      </body>
      </html>

> 各批次配件的外观可能存在细微差异，最终样式请以实物为准。

### 连接方式
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
    <img src="./assets/Hardware_OverView.png">
  </details>
</body>
<br>
</html>

#### 主机后端

**同轴线子板**/**杜邦线组** 的插入方向见上图，连接线上的三角标记 **▴** 对准外壳上的三角标记 **▾** 即可。

同轴线的远端有两个接线端子。其中白色的端子和信号源连接，黑色的端子和GND连接。

杜邦线每组只有两个单独的GND，在其连接线上的三角标记和外壳对准插入时，黑色的线就是GND，红色为VCC。

#### 主机前端

**MODE** 小孔中有一个隐藏式按键，可以用取卡针捅入后按下。

**ACT** 是 **状态指示灯**，具体状态见下方[相应章节](#指示灯颜色与功能)描述。

**USB-C** 接口标准是3.2 Gen1 (5Gbps)，使用逻辑分析仪功能需要使用有对应能力的线缆。

### 快速开始

首先，连接 **PC USB** → **USB-A/C to USB-C** →  **SLogic** → **杜邦线**/**同轴线子板**

> 目前SLogic16仅有 **USB3** 模式支持，而DFU模式使用 **USB2** 模式。
> 使用附赠的 **USB-A/C to USB-C** 线缆即可兼容上述两种模式。

将目标设备的待测信号点通过**杜邦线**/**同轴线**连接至 **SLogic** 任意空闲CH端口，并确保待测设备的GND与SLogic的GND相连接。

> 注意，在信号源奈奎斯特频率大于或等于 50 MHz 的情况下，推荐使用同轴线进行采样，以获得更佳的稳定性。

可以根据实际情况决定是否使用 **逻辑分析仪测试夹** 连接至待测信号点。

> 为了提升采样稳定性，SLogic 的 GND 线应尽量靠近待测点，即便仅缩短 1 cm 也可能带来改善。在使用同轴线采样时，建议您在连接每个采样信号 CH 的同时，也连接对应的 GND。

最后启动 [**plusview**]() 开始采集操作。

## MODE按键功能

> Windows环境打开设备管理器或使用 *USB treeview*，Linux/macOS环境使用 *lsusb* 命令，可以找到 "*SLogic16 U3/SLogic DFU*" 设备

装置上电后默认功能是 **逻辑分析仪**，正常情况下[ACT指示灯](#指示灯颜色与功能)显示青色。
同时出现一个新的 **USB3** 装置：**SLogic16 U3**（逻辑分析仪）

<!-- ![slogic16_u3](./assets/slogic_u3.png) -->

**按下MODE按键**切换功能，切换成功后可以看到**指示灯变化：** 红灯慢闪。
同时出现一个新的 **USB2** 装置：**SLogic DFU** （升级模式）

<!-- ![slogic16_u2](./assets/slogic_u2.png) -->

再次按下 **MODE** 则切换回 **SLogic16 U3**，重复按下 **MODE** 再进入**SLogic DFU**，如此往复循环。

## 指示灯颜色与功能

指示灯是一颗3色RGB，每一种颜色代表一种状态，不同状态组合指示当前设备状态

| **颜色**   | <span style="color:blue">蓝灯</span>    | <span style="color:green">绿灯</span> | <span style="color:red">红灯</span> |
| ---------- | -------------------------------------- | ------------------------------------- | ----------------------------------  | 
| **功能**   | 电源                                    | USB LINK 指示                         | 运行状态指示                         | 

- 下边表是不同颜色对应的正常运行时候的装置状态

  | 状态         | 颜色                                 | 备注                                                                      |
  | ----------- | ------------------------------------ | ------------------------------------------------------------------------- | 
  | **正常连接** | <span style="color:cyan">青色</span> | <span style="color:blue">蓝</span> + <span style="color:green">绿</span> |
  | **数据传输** | <span style="color:cyan">青色</span> + <span style="color:red">红色快闪</span> | <span style="color:blue">蓝</span> + <span style="color:green">绿</span> + <span style="color:red">红快闪</span> |
  | **DFU模式**  | <span style="color:cyan">青色</span> + <span style="color:red">红色慢闪</span> | <span style="color:blue">蓝</span> + <span style="color:green">绿</span> + <span style="color:red">红慢闪</span> |

- ⚠下边的指示灯颜色对应的装置的异常状态
  | 状态            | 颜色                               | 备注                                        |
  | -------------- | ---------------------------------- | ------------------------------------------- | 
  | **USB连接失败** | <span style="color:blue">蓝</span> | <span style="color:blue">只亮蓝灯</span>     |

> ⚠注意：任何时候<span style="color:green">绿灯</span>如果熄灭都意味着USB连接出现问题，请尝试重新连接以解决问题。此时<span style="color:red">红灯</span>的状态没有意义。

- 装置的异常状态的检查清单
    - 使用的USB线缆不支持**USB3**（常见于手机充电线）
    - PC的USB接口不支持**USB3**
    - 连接到了Desktop PC 机箱的前面板的USB
    - 连接到了不兼容的**USB hub**（请尽量保证SLogic直连PC USB）
    - 连接到了供电能力不足的**USB端口**
    - 连接线太长（请尽量使用1m以内的连接线）


## 更新固件

> Windows环境打开设备管理器或使用 *USB treeview*，Linux环境使用 *lsusb* 命令，可以找到 "*SLogic DFU*" 设备

首先[进入DFU MODE](#mode按键功能)：上电后按下 **MODE按键**，等待<span style="color:red">红灯慢闪</span> 。

确认"*SLogic DFU*" 设备出现后，使用 [**DFU工具**]() 进行更新。

DFU工具的说明详见[更新固件]()章节。

## 安全 & 注意事項

- **SLogic** 的 ***VCC*** 是电源输出，两个 ***VCC*** 端口共享同一路电源。电源供电能力为：***3.3V @ 500mA MAX***
- **切勿** 将 **SLogic** 的 ***VCC*** 直接和 ***GND*** 短接，以免发生短路过流
- **SLogic** 具备过流保护设计。但为了确保使用安全，我们仍建议您尽量避免发生短路情况，因为主机侧 **USB** 端口的过流保护能力可能存在差异
- 当 **SLogic** 与市电供电的计算机配合使用时，其接地端会与计算机接地端相连。此时，为了保护设备与主机安全，请仅将探头接地端连接到等电位的接地点，**切勿**连接至热地或电位不一致的点

## FAQ

TBD