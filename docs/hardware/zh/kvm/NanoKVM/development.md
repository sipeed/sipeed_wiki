---
title: 二次开发
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2024-9-26
    version: v0.1
    author: BuGu
    content:
      - Release docs
  - date: 2025-4-10
    version: v1.0
    author: BuGu
    content:
      - Update docs
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

+ **查看硬件版本**
    + NanoKVM有不同的版本,版本之间硬件有所差异,详情请自行翻阅[原理图](https://cn.dl.sipeed.com/shareURL/KVM/nanoKVM/HDK/02_Schematic),开机脚本将检测硬件差异,并保存在`/etc/kvm/hw`里
        + alpha : 早期内测版 NanoKVM Full
        + beta : 正式版 NanoKVM Full 和 Lite
        + pcie : NanoKVM PCIe

+ **network相关配置**
    + /etc/kvm/server.yaml
    + 详情参考WiKi->KVM->NanoKVM Cube->网络

+ **USB状态获取**
    + cat /sys/class/udc/4340000.usb/state
        + configured 已连接
        + not attached 未连接

+ **HDMI状态获取**
    + cat /kvmapp/kvm/state
        + 1：HDMI正常
        + 0：HDMI异常

+ **ETH状态获取**
    + cat /sys/class/net/eth0/carrier
        + 1：网线接入
        + 0：网线断开（不准确）

+ **WiFi存在**
    + /etc/kvm/wifi_exist 文件存在即为wifi模块存在

+ **WiFi状态获取**
    + cat /kvmapp/kvm/wifi_state
        + 0：wifi存在但未连接
        + 1：wifi已连接

+ **打开watchdog（实时）**
    + touch /etc/kvm/watchdog 打开
    + rm /etc/kvm/watchdog 关闭

+ **关闭ping功能**
    + touch /etc/kvm/stop_ping 关闭
    + rm /etc/kvm/stop_ping 打开


## USB HID模拟设备

+ 初始化: NanoKVM借助USB Gedget 模拟 USB HID 设备, 在设备开机脚本 `/etc/init.d/S03usbdev` 中完成了键盘,鼠标,触屏的初始化
+ 模拟键盘
    + 设备: /dev/hidg0
    + 报文：8byte：
        + 格式: |0x00|0x00|0xXX|0x00|0x00|0x00|0x00|0x00|
        + 第四位代表普通按键键值,如 F11: 0x44
        + 发送键值后需要及时释放
        + 示例: 按下F11按键 
            ```shell
            echo -ne \\x00\\x00\\x44\\x00\\x00\\x00\\x00\\x00 > /dev/hidg0   # 按下F11键
            echo -ne \\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00 > /dev/hidg0   # 释放
            ```
+ 模拟鼠标
    + 设备: /dev/hidg1
    + 报文：4byte：
        + 格式: |b8 按键|s8 x轴相对位移|s8 y轴相对位移|s8 滚轮|
        + 按键
            + 左键按下：0x01
            + 右键按下：0x12 # 兼容多系统
            + 释放：0x00
            + 示例: 点按左键
                ```shell
                echo -ne \\x01\\x00\\x00\\x00 > /dev/hidg1  # 按下左键
                echo -ne \\x00\\x00\\x00\\x00 > /dev/hidg1  # 释放
                ```
        + 位移 (相对位移)
            + x/y轴相对位移为带符号数，x正值向右移动，y正值向下移动
            + 示例: 右移5格，上移1格
                ```shell
                echo -ne \\x00\\x05\\xff\\x00 > /dev/hidg1
                ```
        + 滚轮
            + 滚轮为带符号数，正值向下移动
            + 示例: 下移1格
                ```shell
                echo -ne \\x00\\x00\\x00\\x01 > /dev/hidg1
                ```
+ 模拟触屏
    + 设备: /dev/hidg2
    + 报文：6byte：
        + 格式: |按键|x轴绝对位置低8位|x轴绝对位置高8位|y轴绝对位置低8位|y轴绝对位置高8位|滚轮|
        + 按键
            + 左键按下：0x01
            + 右键按下：0x10
            + 释放：0x00
            + 示例: 点按左键
                ```shell
                echo -ne \\x01\\x00\\x00\\x00\\x00\\x00 > /dev/hidg2  # 按下左键
                echo -ne \\x00\\x00\\x00\\x00\\x00\\x00 > /dev/hidg2  # 释放
                ```
        + 位移 (绝对位置)
            + x/y均为无符号数，(0x0001,0x0001) 代表左上角, (0x7fff,0x7fff) 代表右下角
            + 示例: 鼠标移动至屏幕正中间
                ```shell
                echo -ne \\x00\\xff\\x3f\\xff\\x3f\\x00 > /dev/hidg2
                ```
        + 滚轮
            + 滚轮为带符号数，正值向下移动
            + 示例: 下移1格
                ```shell
                echo -ne \\x00\\x00\\x00\\x00\\x00\\x01 > /dev/hidg2
                ```
## 注意事项

+ 用户自己构建的程序请不要放在/kvmapp下,每次更新将会重置文件夹内所有内容
+ 模拟键鼠操作可能与前端页面操作冲突