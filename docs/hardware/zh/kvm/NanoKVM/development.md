---
title: 二次开发
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2024-9-26
    version: v0.1
    author: BuGu
    content:
      - Release docs
---

NanoKVM除实现KVM功能外还开放了一些数据,用于用户的二次开发,此文档用于描述这些数据的作用,以及开发的注意事项

## 获取推流相关数据

推流和图像参数位于/kvmapp/kvm文件夹下

+ **HDMI 获取的图像原始分辨率**
    + 图像宽度: /kvmapp/kvm/width
    + 图像高度: /kvmapp/kvm/height
    > 示例: 终端查看当前分辨率`echo "$(cat /kvmapp/kvm/width) * $(cat /kvmapp/kvm/height)"` 
    + 注: width/height 仅读取,不可写入,kvm_stream 根据该数据实时修改vi参数,自行修改将导致vi子系统无法解析正确图像
    + 当两参数中有一个或两个全为0时,表明HDMI线缆拔出 或 HDMI 分辨率正在切换
    + width/height 两参数仅在HDMI插入,拔出,或改变分辨率时才能捕获,当 NanoKVM 在开机前插入HDMI线缆,并且HDMI输出非默认1080P分辨率时,vi子系统将无法获取正确的尺寸参数,导致无视频流输出,因此建议用户在第一次开机上电后再插入HDMI,后续每次开机会读取上次关机前保留的HDMI分辨率,故不会受到影响.

+ **Stream 传输分辨率**
    + Stream 传输分辨率不同与 HDMI 获取的分辨率,有时为了减小传输数据量,可以设置一个较小的传输分辨率,NanoKVM会相应的对图像缩放后再传输
    + 传输分辨率: /kvmapp/kvm/res
        + 0   : 自动,将跟随 HDMI 原始分辨率
        + 480 : 以640*480传输
        + 600 : 以800*600传输
        + 720 : 以1280*720传输
        + 1080: 以1920*1080传输 
    + 注: 该参数可读可写
    > 示例: 终端设置 kvm_stream 以 1280*720 分辨率传输: `echo 720 > /kvmapp/kvm/res`

+ **Stream 最大传输帧率**
    + 最大传输帧率: /kvmapp/kvm/fps
    + 范围: 0-60
    + 注: 参数可读可写
    > 示例: 终端限制 kvm_stream 最大以 45 fps 传输: `echo 45 > /kvmapp/kvm/fps`

+ **Stream 当前传输帧率**
    + 当前传输帧率: /kvmapp/kvm/now_fps
    + 范围: 0-60
    + 注: 参数只读
    > 示例: 查看当前stream分辨率: `cat /kvmapp/kvm/now_fps`

+ **Stream 传输流格式**
    + 传输流格式: /kvmapp/kvm/type
        + mjpeg 
        + h264
    + 注: 参数可读可写
    + stream h264 格式开发中,预计10月上线
    > 示例: 终端修改传输格式为MJPEG: `echo mjpeg > /kvmapp/kvm/type`

+ **Stream 传输流质量**
    + 传输流格式: /kvmapp/kvm/qlty
    + 范围: 50-100
    + 注: 参数可读可写,仅针对MJPEG格式调整质量,设置95以上质量时,受限于SG2002 CPU和编码器,传输帧率会变慢,延迟变大.
    > 示例: 终端修改MJPEG质量为60%: `echo 60 > /kvmapp/kvm/qlty`

+ **Stream 帧差检测设置**
    + KVM 捕获的电脑画面并非时刻改变,当画面静止时,可以暂停流的传输来降低流量消耗
    + 帧差检测设置: /etc/kvm/frame_detact
        + 创建文件: 启动帧差检测
        + 删除文件: 关闭帧差检测
    + 帧差计算需要消耗大量CPU资源,所以stream使用 320\*240 的图像计算帧差,并且每100帧检测一次,此时帧差检测带来的CPU消耗约为2%, 当检测到画面静止时, kvm_stream 停止流传输, now_fps降低为0, CPU 开始连续检测图像变化, 当图像改变时可以以最快速度恢复流的传输.
    + 注: 帧差计算尺寸和跳帧数暂不可调
    > 示例: 打开 kvm_stream 帧差检测功能: `touch /etc/kvm/frame_detact`

+ **查看硬件版本**
    + NanoKVM有不同的版本,版本之间硬件有所差异,详情请自行翻阅[原理图](https://cn.dl.sipeed.com/shareURL/KVM/nanoKVM/HDK/02_Schematic),开机脚本将检测硬件差异,并保存在`/etc/kvm/hw`里
        + alpha : 早期内测版 NanoKVM Full
        + beta : 正式版 NanoKVM Full 和 Lite
        + pcie : NanoKVM PCIe

+ **network相关配置**
    + /etc/kvm/server.yaml
    + 详情参考WiKi->KVM->NanoKVM Cube->网络

## 注意事项

+ 用户自己构建的程序请不要放在/kvmapp下,每次更新将会重置文件夹内所有内容