---
title: MaixPy 发展历程
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: MaixPy 发展历程
---


写下本篇发展历程， 希望让后来的开发者们了解到 MaixPy 都经历了什么，以及一些重大的改变的原因是什么，以及在何时取得了重大的进步等


代码提交历史可以在 [historic](https://github.com/sipeed/MaixPy/commits/historic) 和 [master](https://github.com/sipeed/MaixPy/commits/master) 分支看到


## 2018 年 9 月

MaixPy 项目启动，契机是 K210 芯片流片完成。

于是大家想着做一套让更多人在嵌入式使用的 AI 开发的易使用的软件套件， 因为 Micropython 的易用性，而且 k210 有 6+2MiB 内存，主频 400MHz，完全能够驾驭 Micropython， 故选择了 Micropython 作为编程语法

基于开发板 Maix dock， 这时取名为 荔枝丹， QQ 群名也叫荔枝丹炼丹群

[xiaohui](https://github.com/xiaoxiaohuixxh) 和 [wipping](https://github.com/wipping) 开始尝试对 Micropython 移植

## 2018 年 12 月

k210 SDK 从 freertos 换成了 standalone SDK, 并且着手片上外设驱动适配

[neucrack](https://github.com/neutree) ，[xel](https://github.com/xelll) 和 [zepan](https://github.com/Zepan) 加入项目组


## 2019 年 2 月

发布第一版固件 [v0.1.1 beta](https://github.com/sipeed/MaixPy/releases/tag/v0.1.1), 支持了基本的外设， 继承了 openmv 的 image sensor lcd API，适配了一些开源的工具比如 upyloader，armpy等, 编写文档 并发布在 maixpy.sipeed.com

另外这时也有了 Maix bit 和 Maix Go 两块新开发板

xiaohui 退出项目组

## 2019 年 3 月

发布第二版固件 [v0.2.4](https://github.com/sipeed/MaixPy/releases/tag/v0.2.4), 增加了 jpeg， wav， kpu， nes， avi， lvgl 等支持


## 2019 年 4 月

适配了 OpenMV IDE 也就是 MaixPy IDE， 在原来软件的基础上只将 USB 通信改成了 k210 支持的 串口通信， 其它功能没有变化

预编译固件开始区分功能分成多个固件， 主要考虑到运行模型内存不足的问题

wipping 退出项目组， zepan 和 xel 专注到其它项目组


## 2019 年 6 月


重构了项目结构， 之前是直接在 micropython 的目录结构中添加代码， 在 port 目录中添加代码， 但是这会有一个问题， 就是更新 micropython 程序变得比较麻烦， 需要将 micropython 和 MaixPy 增加的代码分开， 而且旧的代码结构太混乱， Makefile 写得也不是很好，构建缓慢。
所以有了现在的目录结构， 使用了 cmake + kconfig 对工程进行构建， 同时将各个组件模块化， 并且可以选择是否编译进固件， 编译框架在[这里](https://github.com/Neutree/c_cpp_project_framework)。 但是仍有遗留问题， 目录下面有一些遗留代码没有完全接偶。


## 2019 年 7 月

增加 M5Stick-V 开发板的支持， 由 [Martin Han](https://github.com/MarsTechHAN) 维护


## 2019 年 12 月

[Maixhub](https://www.maixhub.com) 上线， 用于在线模型训练，只需要上传数据集无须编写代码

硬件更新： 上线 M1N 模块， 金手指模块

## 2020 年 4 月

[糖老鸭](https://github.com/QinYUN575) 加入项目组


## 2020 年 5 月

[大佬鼠](https://github.com/junhuanchen) 加入项目组

## 2020 年 6 月

硬件更新： 上线 Maix Cube 开发板

## 2020 年 7 月

为不同板子增加板级配置文件， 放在文件系统中， 开机读取， 主要是由于 Cube 和 Amigo 增加了电源芯片， 在开机时为了能正常使用必须先设置电源芯片

硬件更新： 上线 Maix Amigo 开发板， 增加了外壳

## 2020 年 11 月

重新梳理文档， 更完美的文档和社区

## 2021 年 1 月

稳定 MaixPy 各项功能，补充缺失的文档，迎接 MaixPy3 项目的到来。


