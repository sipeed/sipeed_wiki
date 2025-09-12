---
title: 高级应用
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, ARM, tool, PCIe
update:
  - date: 2025-8-26
    version: v0.1
    author: BuGu
    content:
      - Release docs
  - date: 2025-9-11
    version: v0.2
    author: iawak9lkm
    content:
      - Add new feature description
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

## SSH & mDNS

### SSH

NanoKVM-Pro 出厂默认关闭 SSH，以确保系统安全。若需要启用 SSH 服务或在预览新版本时使用，可以通过以下方式开启：

- **ATX/Desk**：从网页端 `设置` → `设备` → 开启 `SSH`
- **Desk**：从屏幕中点击 `Settings` → `SSH` 开启 `SSH`

默认帐号为 `root`，密码为 `sipeed`。若在 NanoKVM 界面中修改了网页帐号密码，SSH 密码会同步更新。

### mDNS

如需开启或关闭 mDNS，可通过以下方式操作：

- **ATX/Desk**：从网页端 `设置` → `设备` → 开启/关闭 `mDNS`
- **Desk**：从屏幕中点击 `Settings` → `mDNS` 开启/关闭 `mDNS`

## HDMI 输入与环出

> 目前仅支持 Desk 版本屏幕中配置
> ATX/Desk 网页端近期会添加该功能

若暂时无需 HDMI 功能，可关闭以降低功耗。操作方式：

Desk 从屏幕点击 `Settings` → `HDMI` 进入 HDMI 配置页面，有两个选项：

- **INPUT**：关闭后，Desk 停止采集 HDMI 输入信号。
- **LOOP OUT**：关闭后，Desk 停止输出 HDMI 环出信号。

## 屏幕调整

### ATX 版本

目前支持 OLED 屏幕的以下功能：

- 短按 `USR` 按钮可开关 OLED 显示

### Desk 版本

支持 LCD 屏幕的以下功能（均从屏幕中进行配置）：

- 调整背光亮度：`Settings` → `Brightness`
- 待机时钟：`Settings` → `Auto Clock`
  - 关闭时，LCD 常亮
  - 开启后，长时间无操作则切换为时钟显示

## 恢复出厂设置

### 快速恢复

- **ATX**：长按 `USR` 按钮，直至屏幕显示 `Reset` 提示后松开
    > 要求版本 ≥ `1.0.13`
- **Desk**：从屏幕中点击 `Settings` → `Help` 进入 Help 页面，然后连续点击重置按钮，直至显示 `0`，设备进入恢复模式

> **提示**：在设备完成重启并刷新屏幕前，请勿进行其他操作。

### 深度恢复

详见 [FAQ](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM_Pro/faq.html#%E9%95%9C%E5%83%8F%E7%83%A7%E5%BD%95%E6%96%B9%E6%B3%95) 中 `镜像烧录方法` 章节。

## USB 扩展功能

### USB NCM

NCM 功能可通过 USB 模拟网卡，方便用户直接通过 USB 登录 NanoKVM。开启方式如下：

- **ATX/Desk**：从网页端进入 `设置` → `设备` → 开启 `虚拟网卡`
- **Desk**：从屏幕中点击 `Settings` → `USB` 进入 USB 配置页面，开启 `NCM`

### USB 副屏

> **仅支持 NanoKVM-Desk**
> 目前 USB 副屏功能仅支持 Windows 系统。

1. 下载并解压 USB 副屏驱动程序。

2. 在 Desk 上：从屏幕中点击 `Settings` → `USB` 进入 USB 配置页面，开启 `Panel`。

3. 在被控机上：

   - 打开 `设备管理器` → `其他设备`
   - 找到 `NanoKVMPro` → 右键 `属性` → `驱动程序` → `更新驱动程序`
   - 选择 `浏览我的电脑以查找驱动程序` → `让我从计算机上的可用驱动程序列表中选取`
   - 双击 `显示所有设备`
   - 在 `Standard USB Host Controller` / `标准 USB 主机控制器` / `Standard system devices` / `标准系统设备` 中找到 `USB 复合设备 (USB Composite Device)` → 双击安装

   > **注意**：不同版本 Windows 驱动位置可能有所差异，请耐心查找。

4. 完成后，`设备管理器` 的 `其他设备` 下会出现一个新的 `loop input to output` 设备。

5. 右键该设备 → `更新驱动程序` → `浏览我的电脑以查找驱动程序` → `浏览` → 选择 USB 副屏驱动文件夹 → `下一步` → 按提示完成安装。

6. 驱动安装完成后，`显示适配器` 部分会出现一个新的 NanoKVM 显卡设备。

7. 在 Desk 上从屏幕中进入副屏页面，选择 USB，即可将 Desk 用作 USB 副屏。

8. 若需关闭，参考步骤 2 关闭 `Panel`。

9. 再次开启时，部分系统可能需要重新安装 USB 驱动。

## 更新

NanoKVM Pro 会不定时推送新版本的应用，包含新功能和bug修复，您可以在`设置`->`检查更新`中更新应用版本。

![](./../../../assets/NanoKVM/pro/extended/Update.png)

点击下载后会自动下载新应用的安装包，包含`kvmcomm_x.x.x_arm64.deb`、`nanokvmpro_x.x.x_arm64.deb`、`pikvm_x.x.x_arm64.deb`

- `kvmcomm_x.x.x_arm64.deb` 负责驱动 NanoKVM 和 PiKVM 框架中共用的硬件；
- `nanokvmpro_x.x.x_arm64.deb` NanoKVM 应用软件
- `pikvm_x.x.x_arm64.deb` PiKVM 应用软件

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

- 外接其他串口终端设备

```shell
# 网页终端使用 UART1 以 115200 波特率打开串口，使用Ctrl+A+Q退出
picocom -b 115200 /dev/ttyS1
# 网页终端使用 UART2 以 115200 波特率打开串口，使用Ctrl+A+Q退出
# picocom -b 115200 /dev/ttyS2
```

- 仅发送串口指令

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
