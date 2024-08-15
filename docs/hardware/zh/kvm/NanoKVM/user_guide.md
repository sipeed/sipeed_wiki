---
title: 用户指南
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2024-7-4
    version: v0.1
    author: BuGu
    content:
      - Release docs
---

## 管理页面功能

![](../../assets/NanoKVM/3_user_guide/user1.png)

悬浮栏从左到右依次为：图像设置、屏幕键盘、鼠标样式、镜像挂载、KVM网页终端、开机按钮、电源/HDD状态指示、设置、全屏、隐藏悬浮栏。

### 分辨率、帧率、图像质量设置

+ NanoKVM 支持 1080P、720P、600P、480P 的图像传输，在图像设置->分辨率中可以选择不同的分辨率。越大的分辨率所占用带宽越大、实时帧率越小。
  + 注：此处仅修改图像的传输大小，不会改变 HDMI 输入的图像尺寸，如需修改，请前往主机系统的设置菜单进行设置。

+ 帧率设置选项用于修改传输的最大帧率，可以限制网络带宽的占用，但帧率越低，画面越卡，请根据网络情况合理配置。Full版用户在OLED上可看到视频的实时帧率。

+ 图像质量选项可以修改画面的压缩比例，当您认为画面较卡，延迟较高时，可以适当调低图像质量。

![](../../assets/NanoKVM/3_user_guide/user2.png)

### 虚拟键鼠使用

+ NanoKVM 的 USB 接口模拟出了键鼠设备。打开浏览器页面后，系统将自动捕获键鼠输入，并将操作实时同步到 NanoKVM 连接的主机。用户可以选择隐藏鼠标或改变在画面上显示的样式。
+ 对于不方便使用键盘的用户，我们提供了屏幕键盘，点击悬浮栏的键盘图标即可唤出屏幕键盘。

![](../../assets/NanoKVM/3_user_guide/user3.png)

### ISO镜像挂载

+ Nano KVM的 USB-C 端口除模拟键鼠设备外，还模拟了一个U盘设备，挂载了TF卡内的一部分存储空间，用于装机等需求，该U盘默认格式化为exFAT格式，Full版NanoKVM内置TF卡，模拟出的U盘大小约21G。

首先用户需要下载待安装的镜像（通常以.iso结尾），将 NanoKVM USB-C 插入电脑，直接将下载好的镜像复制到U盘内（可复制多个系统），即可拔出。

按上述步骤连接远程主机与Nano KVM，在浏览器登录系统后，点击光盘图标，选中待安装的系统，即可实现ISO挂载

![](../../assets/NanoKVM/2_unbox/unbox_7.png)

注：

+ 虚拟U盘也可以当作普通U盘，使用常规的烧卡方式烧录镜像。
+ 镜像拷入 NanoKVM 的速度受到 USB2.0 传输速度和 SG2002 写卡速度的限制，可能会比较慢，用户可将TF卡取出，插入电脑，[解除隐藏](https://jingyan.baidu.com/article/e4511cf34faece2b845eaf34.html)TF卡的第三个分区，直接将镜像拷入其中。

### 网页终端

+ 用户点击悬浮栏的`Terminal`图标，即可打开网页终端，无需ssh直接访问 NanoKVM 系统
+ 当 NanoKVM 断网重连或系统重启后，网页终端界面会提示重新登录，账号`root`，密码`root`

![](../../assets/NanoKVM/3_user_guide/user4.png)

### 电源灯，HDD灯

+ 在悬浮栏右侧，有电源和硬盘图标，正常情况下是灰色状态，开机后电源图标变绿。Full版的ATX控制板受延长线芯数限制，只引出电源、重启按键和电源灯。Lite用户可根据原理图自行扩展。

### 设置

+ 切换中英文
+ 关于NanoKVM：点击打开Wiki
+ 检查更新：当有可用更新时，用户可点击更新，约10s左右，OLED上将重新刷一遍KVM状态信息，此时刷新网页即可更新完成。

### 更多功能敬请期待

## 网络延迟测算

主机连接KVM和一个普通屏幕，播放秒表计时视频，拍照捕捉远程桌面和显示屏，计算差值即可估算网络延迟。

## 串口使用

NanoKVM 基于 LicheeRV Nano 构建，RVNano 核心板共有3个串口，UART0默认用于输出系统log，在 NanoKVM Full 版中，引出了 UART1/2，用户可自行拓展功能（第一批内测版仅在外壳处开孔）

![](../../assets/NanoKVM/1_intro/NanoKVM_2.jpg)

点击管理页面的`Terminal`打开网页终端

图标若需使用UART，请先确保对应引脚 Pinmux 正确

``` shell
devmem 0x03001068 32 0x6    # GPIOA 18 UART1 RX
devmem 0x03001064 32 0x6    # GPIOA 19 UART1 TX
devmem 0x03001070 32 0x2    # GPIOA 28 UART2 TX
devmem 0x03001074 32 0x2    # GPIOA 29 UART2 RX
```

串口使用方法如下：

``` shell
stty -F /dev/ttyS1 115200   # 设置UART1波特率为115200
stty -F /dev/ttyS1 raw      # 设置tty为RAW模式
echo -n UUU > /dev/ttyS1    # 发送 UUU(0x55 0x55 0x55)
hexdump -C /dev/ttyS1       # 以HEX格式显示收到的数据
```

## IPMI使用

Todo

## 外网远程访问

Todo

## WOL（wake-on-lan）

Todo

## 异常恢复

+ 登录浏览器界面后，无画面
  1. 进入网页终端，执行 `/etc/init.d/S95webkvm restart` 重启服务。
  2. 如果上述方式无法恢复正常，点击界面上的检查更新，更新应用
+ 更新过程中如果出现断网等异常情况，可能导致更新失败，若旧应用也无法启动时，请参照以下解决方法：
  1. 使用 SSH 连接 NanoKVM，如 `ssh root@192.168.1.2`，密码为 `root`
  2. 执行 `rm -r /kvmapp && cp -r /root/old/ / && mv /old /kvmapp`
  3. 执行 `reboot` 重启系统
+ 尝试断电重启解决未知问题
+ 若上述方法不能解决异常，请在论坛或QQ群提出您的问题，我们会耐心解答
