# Lichee 86 Panel

## 概述

Lichee RV-86 Panel是为智能家居中控应用场景而设计的开发套件。在硬件上，套件包含了LicheeRV 核心板（全志D1+512MB DDR3)、4英寸 IPS 显示屏+电容触摸屏、WIFI + BT、以太网、双数字硅麦和 GPIO 拓展接口等。
在软件上，我们提供了 Linux 系统（OpenWRT 及 Debian )和阿里 WAFT 开发环境( WAFT 是阿里基于 WebAssembly 和自研的渲染引擎打造的一款面向 AIOT 的高性能应用框架)。

![](./../assets/RV/86_panel_1.png)

![](./../assets/RV/86_2.png)
## 参数
| 项目 | 参数 |
| --- | --- |
| 核心模块 | Sipeed LicheeRV 哪吒计算条 |
| 显示 | 默认搭配为4英寸480\*480 IPS标清电容触摸屏<br>可选升级为4英寸720\*720 IPS高清电容触摸屏<br>预留8英寸1280\*800 IPS电容触摸屏接口 |
| 音频 | 板载1W小扬声器，双路数字硅麦 |
| 网络 | XR829 WIFI+BT无线模块<br>RTL8201F百兆以太网<br>预留板载RJ45以太网接口 |
| USB | 核心板带有USB-C OTG接口 <br>底板预留USB-C HOST 与USB转串口电路 |
| 电源 | 支持5V,12V供电(板载DC-DC ) |
| 扩展引脚 | 双2x8Pin 2.54mm 排针，预留FPCIO引出 | 
| 外壳 | 选配86盒3D打印外壳，图纸开源 |
| 尺寸 | 86x86mm |
| 适用场景 | 智能家居中控，WAFT UI评估 |
| 开发框架 | 支持WAFT (WebAssembly Framework For Things）环境 |
| 系统支持 | 支持 OpenWRT及 Debian系统 |
| 开发资源 | 提供原厂SDK的 Docker开发镜像 |

![](./../assets/RV/86_pin.png)

## 相关链接

[下载站](https://dl.sipeed.com/shareURL/LICHEE/D1/Lichee_RV_86_panel)

[烧录系统](./flash.md)

[相关使用](./user.md)

## 产品技术支持

Lichee RV-86 Panel 可以在多种场景实现客户不同方面的需要，品质和性能在行业内已经有非常好的口碑，专业的技术团队为广大客户解决硬件设计和软件功能上的各种各样问题。专业技术支持和更详细资料请联系商务 <support@sipeed.com>。