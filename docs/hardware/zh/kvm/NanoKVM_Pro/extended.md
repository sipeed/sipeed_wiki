---
title: 高级应用
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, ARM, tool, PCIe
update:
  - date: 2025-8-26
    version: v0.1
    author: 
    content:
      - Release docs
---

## 切换至PiKVM

NanoKVM Pro除运行 NanoKVM 框架外还适配了PiKVM软件框架。您可以根据需求切换使用

### 切换至PiKVM

NanoKVM Pro 出厂默认使用 NanoKVM 框架，可以在`设置`->`关于`->`切换设备`

![](./../../../assets/NanoKVM/pro/extended/SwitchtoPiKVM.png)

点击后系统将自动重启，并启动为PiKVM框架。此过程约30s，如果长时间不自动切换，请手动刷新网页。

![](./../../../assets/NanoKVM/pro/extended/PiKVMLogin.png)

PiKVM框架下默认帐号密码也是`admin`，`admin`，但两个平台下使用各自的帐号与密码，并不统一，强烈建议登陆后修改。

![](./../../../assets/NanoKVM/pro/extended/PiKVM-Setting.png)

> PiKVM框架下部分功能需要借助网页终端实现：如WiFi配网、Tailscale配置
> NanoKVM更新时，PiKVM框架将同步更新

### 切换至NanoKVM

从PiKVM系统切换回NanoKVM同样简单，只需在`Options`->`Switch to NanoKVM`点击`Switch Now`即可

![](./../../../assets/NanoKVM/pro/extended/SwitchtoNanoKVM.png)

点击后系统将自动重启，并启动为NanoKVM框架。此过程约30s，如果长时间不自动切换，请手动刷新网页

## SSH

NanoKVM Pro为确保安全性，出厂默认SSH处于关闭状态，若需要SSH服务或预览新版本时可以通过`设置`->`设备`打开SSH选项

出厂默认帐号`root`，密码`sipeed`，若在NanoKVM框架下修改网页帐号密码，SSH密码会被同步修改。

## 更新

NanoKVM Pro 会不定时推送新版本的应用，包含新功能和bug修复，您可以在`设置`->`检查更新`中更新应用版本。

![](./../../../assets/NanoKVM/pro/extended/Update.png)

点击下载后会自动下载新应用的安装包，包含`kvmcomm_x.x.x_arm64.deb`、`nanokvmpro_x.x.x_arm64.deb`、`pikvm_x.x.x_arm64.deb`
+ `kvmcomm_x.x.x_arm64.deb` 负责驱动 NanoKVM 和 PiKVM 框架中共用的硬件；
+ `nanokvmpro_x.x.x_arm64.deb` NanoKVM 应用软件
+ `pikvm_x.x.x_arm64.deb` PiKVM 应用软件

打开预览更新功能将会获取到最新的实验版应用，通常包含更新的功能，但稳定性有待验证，建议下载预览更新前先打开SSH功能

您也可以下载特定的版本，并手动安装

```shell
# 以下载 1.0.10 版本为例
# 下载文件
curl -L -o nanokvm_pro_1.0.10.tar.gz https://cdn.sipeed.com/nanokvm/pro/kvmcomm_1.0.10_arm64.deb
curl -L -o nanokvm_pro_1.0.10.tar.gz https://cdn.sipeed.com/nanokvm/pro/nanokvmpro_1.0.10_arm64.deb
curl -L -o nanokvm_pro_1.0.10.tar.gz https://cdn.sipeed.com/nanokvm/pro/pikvm_1.0.10_arm64.deb

sudo apt install ./*1.0.10*
```

## 如何使用串口

NanoKVM Pro 提供两组可用串口 UART1/UART2（ATX版本受限挡板规范尺寸没有引出，仅保留内部焊盘）

+ 外接其他串口终端设备
```shell
# 网页终端使用 UART1 以 115200 波特率打开串口，使用Ctrl+A+Q退出
picocom -b 115200 /dev/ttyS1
# 网页终端使用 UART2 以 115200 波特率打开串口，使用Ctrl+A+Q退出
# picocom -b 115200 /dev/ttyS2
```
+ 仅发送串口指令
```shell
# 设置ttyS1为115200波特率
stty -F /dev/ttyS1 115200

# 发送十六进制数据 0x11, 0x22, 0x33
echo -n -e '\x11\x22\x33' > /dev/ttyS1
```

## 如何修改EDID

EDID（扩展显示识别数据）是显示设备向主机提供的一组数据，包括设备信息、分辨率帧率列表、颜色特性、音频能力等。主机接受到 EDID 后按需调整显示器的设置

NanoKVM Pro 支持修改虚拟显示屏暴露的EDID，您可以克隆显示器的EDID或编写自己的EDID，来达到特殊的屏幕比例、刷新率或颜色特征

> 修改EDID后可能存在无法正常显示的风险，请谨慎修改。如果出现异常，请恢复默认EDID

写入方式：

```shell
# 1. 准备edid文件，一般大小是256Byte，scp 到系统中
ls -l /root/customize.bin
# -rw-r--r-- 1 1000 1000 256 Aug 19 14:44 /root/customize.bin
# 2. 写入EDID
cat /root/customize.bin > /proc/lt6911_info/edid
# 3. 恢复默认EDID：
cat /kvmcomm/edid/e18.bin > /proc/lt6911_info/edid
```