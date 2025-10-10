---
title: 屏同步氛围灯带
keywords: NanoKVM, LED Strip
update:
  - date: 2025-10-07
    version: v0.2
    author: zepan
    content:
      - improve docs
  - date: 2025-09-05
    version: v0.1
    author: iawak9lkm
    content:
      - Release docs
---
## 简介
屏同步氛围灯带是NanoKVM-Pro的特色扩展配件。
当你将NanoKVM-Pro用于桌面电脑时，NanoKVM-Pro可以通过捕获的屏幕画面，控制LED灯带按屏幕边缘的色彩显示，实现梦幻的灯光渲染效果！
![ledstrip_pic](../../../assets/NanoKVM/pro/ledstrip/ledstrip_pic.jpg)
 <video playsinline controls muted preload src="../../../assets/NanoKVM/pro/ledstrip/sync_led2.mp4"></video>

> ⚠️ 注意：使用该功能，需要确保输入电源规格 **5V ≥ 3A**

## 套餐配件概览

如果您购买了灯带套餐，您将获得以下配件：

![ledstrip_ov](../../../assets/NanoKVM/pro/ledstrip/ledstrip_ov.jpg)

1. 一分二数据线
2. 灯带转接套件（含 6 个转接件和 3 根直角转接线）
3. 一卷 LED 灯带

---

## 安装步骤

### 确认安装方向

![ledstrip_screen](../../../assets/NanoKVM/pro/ledstrip/ledstrip_screen.jpg)

> 第④段为可选，支持三边模式和四边模式，根据您的需求来选择即可
>
> 灯带采样顺序为：**屏幕左下角 → 左上角 → 右上角 → 右下角 → 左下角** 。
> 安装时请保持一致。绿色端为灯带的 Type-C 接口，另一端通过转接线连接至 NanoKVM-Pro。

### 裁剪灯带

![ledstrip_cut_st0](../../../assets/NanoKVM/pro/ledstrip/ledstrip_cut_st0.jpg)

根据屏幕长宽裁剪灯带。

> 对边的灯珠数量需要保持一致。

示例：屏幕高度 18 颗灯珠，宽度 30 颗灯珠。

* 第①段：18 颗
* 第②段：30 颗
* 第③段：18 颗
* 第④段：30 颗

裁剪时请沿红线位置（触点中间）对半剪开：

![ledstrip_cut_st1](../../../assets/NanoKVM/pro/ledstrip/ledstrip_cut_st1.jpg)

### 打开转接件

在下图右侧为转接件**侧视图**，红框处掰开转接件，效果如左图：

![ledstrip_con_st2](../../../assets/NanoKVM/pro/ledstrip/ledstrip_con_st2.jpg)

### 插入线材

将灯带和直角转接线分别插入转接件两侧，确保金属触点与转接件内的桥接金属对应。闭合转接件后固定。

![ledstrip_con_st3](../../../assets/NanoKVM/pro/ledstrip/ledstrip_con_st3.jpg)

接入另一端直角转接线，**注意灯带箭头方向（信号传输方向）保持一致**。
重复此步骤，直至所有灯带完成连接。

![ledstrip_con_st4](../../../assets/NanoKVM/pro/ledstrip/ledstrip_con_st4.jpg)

### 粘贴灯带

撕开灯带背部的双面胶保护膜，将其牢固粘贴在屏幕背面。
![ledstrip_install](../../../assets/NanoKVM/pro/ledstrip/ledstrip_install.jpg)

### 连接到 NanoKVM-Pro

连接示意如下：

* ① 接 NanoKVM-Pro PWR 接口
* ② 接灯带
* ③ 接电源适配器

> ⚠️ 注意：请确保输入电源规格 **5V ≥ 3A**。

![ledstrip_pwr](../../../assets/NanoKVM/pro/ledstrip/ledstrip_pwr.jpg)

---

## 启用灯带

* 通过 Web 开启
  1. 通过浏览器登录 NanoKVM
  2. 依次进入 **设置 → 设备 → LED 灯带设置**, 开启功能，填写对应的LED数量

    ![ledstrip_setting](../../../assets/NanoKVM/pro/ledstrip/ledstrip_setting.jpg)


* 通过 Desk UI 开启
  1. 进入 `Settings` 页面
  2. 选择 `Ambilight` 进入二级设置页面
  3. 配置灯带数量并开启

---

## 效果展示

 <video playsinline controls muted preload src="../../../assets/NanoKVM/pro/ledstrip/sync_led2.mp4"></video>
