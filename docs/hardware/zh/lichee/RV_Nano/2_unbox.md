---
title: LicheeRV Nano
keywords: riscv, licheerv,nano
update:
  - date: 2024-1-24
    version: v0.1
    author: BuGu
    content:
      - Release docs
  - date: 2024-4-9
    version: v1.0
    author: BuGu
    content:
      - Update docs
---

## LicheeRV Nano 套餐介绍

LicheeRV Nano根据网络分为四个版本：

+ 标准版（B）无网络配件

+ 网口版（E）板载100M网口

+ WiFi版（W）板载WiFi6/BT5.2模块，BT5.2功能默认不启用，如需使用蓝牙功能，需要贴此处4颗0201电阻或使用2B铅笔填涂短接

  ![](./../assets/RV_Nano/unbox/BLE_RES.jpg)

  注：70415及以上版本可使用0402*4的排阻短接

+ WiFi网口版（WE）板载WiFi6/BT5.2模块，同时提供一个网口小板，通过铜柱与排线连接到开发板上

同时我们提供以下六种配件：

+ 摄像头

  ![](./../assets/RV_Nano/unbox/Camera.jpg)

  该摄像头（3754）左右螺丝固定孔不短路，铜柱推荐固定到第5个焊盘上

  ![](./../assets/RV_Nano/unbox/Camera-5.jpg)

+ 3寸屏幕

  ![](./../assets/RV_Nano/unbox/3inch.jpg)

  屏幕分辨率为480*845，带触摸；包装附赠屏幕触摸转接板和排线

+ 5寸屏幕

  ![](./../assets/RV_Nano/unbox/5inch.jpg)

  屏幕分辨率为480*845，不带触摸；排线可直接连接到LicheeRV Nano 31Pin屏幕接口上

+ 7寸屏幕

  ![](./../assets/RV_Nano/unbox/7inch.jpg)

  屏幕分辨率为800*1280，带触摸；排线可直接连接到LicheeRV Nano 31Pin屏幕接口和6Pin触摸接口上

+ 10寸屏幕

  ![](./../assets/RV_Nano/unbox/10inch.jpg)

  屏幕分辨率为800*1280，带触摸；包装附赠触摸转接板和排线，屏幕排线可直接连接到LicheeRV Nano 31Pin屏幕接口

## 安装指南

### WE小板的安装

+ 焊接排线
  1. 按照下图方向焊接排线
  
     ![](./../assets/RV_Nano/unbox/WE1.jpg)
  
  2. 使用万用表检测通断
  
     ![](./../assets/RV_Nano/unbox/WE2.jpg)
  
+ 固定铜柱
  1. 为避免焊接铜柱时烫手，可以先将将铜柱拧到网口小板上
  
     ![](./../assets/RV_Nano/unbox/WE3.jpg)
  
  2. 将铜柱插入第5个焊盘，可以提前在焊盘上涂抹锡膏，提升焊接后铜柱的稳定性
  
     ![](./../assets/RV_Nano/unbox/WE4.jpg)
  
  3. 在底部使用电烙铁焊接
  
     ![](./../assets/RV_Nano/unbox/WE5.jpg)
  
+ 组装
  1. 将排线接入网口小板的FPC座子，并锁紧
  
     ![](./../assets/RV_Nano/unbox/WE6.jpg)
  
  2. 用螺丝将网口小板固定到铜柱上
  
     ![](./../assets/RV_Nano/unbox/WE7.jpg)

### 摄像头的安装

+ 固定铜柱
  1. 与上面固定方法类似：先将铜柱和螺丝拧到摄像头模组上
  
     ![](./../assets/RV_Nano/unbox/CAM1.jpg)
  
  2. 将铜柱插入第5个焊盘，可以提前在焊盘上涂抹锡膏，提升焊接后铜柱的稳定性
  
     ![](./../assets/RV_Nano/unbox/CAM2.jpg)
  
  3. 在底部使用电烙铁焊接
  
     ![](./../assets/RV_Nano/unbox/CAM3.jpg)
  
+ 组装
  1. 根据下图连接摄像头排线
  
     ![](./../assets/RV_Nano/unbox/CAM4.jpg)
  
  2. 螺丝固定
  
     ![](./../assets/RV_Nano/unbox/CAM5.jpg)

### 屏幕的安装

+ 3寸屏幕安装

   ![](./../assets/RV_Nano/unbox/3inch-1.jpg)

   ![](./../assets/RV_Nano/unbox/3inch-2.jpg)

+ 5寸屏幕安装

   ![](./../assets/RV_Nano/unbox/5inch-1.jpg)

+ 7寸屏幕安装

   ![](./../assets/RV_Nano/unbox/7inch-1.jpg)

## 大核作为A53模式启动

LicheeRV Nano的大核支持作为RISC-V（C906）或ARM（A53）启动，在开发板背面，SG2002芯片旁边有丝印圈出的短接电阻，如下图所示，默认贴在C906（RISC-V）一侧

  ![](./../assets/RV_Nano/unbox/A53-1.jpg)

若大核需要作为ARM启动，需要将该电阻挪至另外一边，如下图

  ![](./../assets/RV_Nano/unbox/A53-2.jpg)

需注意，目前A53模式下的SDK视频编解码存在问题，测试镜像点击[这里](https://github.com/sipeed/LicheeRV-Nano-Build/releases/tag/20240326)下载