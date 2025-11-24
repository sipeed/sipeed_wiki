---
title: NanoKVM Desk 触摸屏&旋钮
keywords: NanoKVM,  Auxiliary Screen
update:
  - date: 2025-10-10
    version: v0.1
    author: zepan
    content:
      - initial docs
  - date: 2025-10-18
    version: v0.2
    author: bugu
    content:
      - improve docs
---

## 简介
NanoKVM-Pro Desk 配备了1.47inch 320x172的迷你显示屏，除了作为基础配置交互外，它还可以用不同方式显示用户自定义内容，作为副屏使用


## HDMI 副屏
NanoKVM-Pro工作时就是虚拟为显示器，所以可以采集HDMI图像并在自身屏幕上显示，实现HDMI副屏功能。
在UI中选择输出视频源为HDMI即可在小屏上输出采集的视频图像。
作为桌面摆件时，此功能可以作为桌面迷你副屏，性能监控，视频缩略图播放器等功能使用。
![](./../../../assets/NanoKVM/pro/lcd/hdmi.jpg)
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
  <video playsinline controls muted preload src="../../../assets/NanoKVM/pro/lcd/cat.mp4"></video>
  <video playsinline controls muted preload src="../../../assets/NanoKVM/pro/lcd/video.mp4"></video>
</div>

## USB 副屏

目前 USB 副屏功能仅支持 Windows 系统。

1. 下载并解压 USB 副屏驱动程序。 https://github.com/sipeed/NanoKVM-Pro/releases/download/v1.0.5/nanokvmpro_usb_graphic_win.zip

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

   > 如果在安装驱动时遇到"Windows 已找到设备的驱动程序，但在尝试安装它们时遇到错误"或类似错误，可以选择以下方法解决：
   >
   > **方法一：临时禁用驱动程序强制签名**
   > 1. 按住 `Shift` 键，点击 `开始菜单` → `重启`
   > 2. 进入高级启动选项后，选择 `疑难解答` → `高级选项` → `启动设置` → `重启`
   > 3. 重启后按 `F7` 或 `7` 选择 `禁用驱动程序强制签名`
   > 4. 系统启动后重新安装驱动程序
   > 5. 该方法在较新的 Windows 11 版本上可能无法使用
   >
   > **方法二：启用测试模式（需要关闭安全启动）**
   > 1. 进入 BIOS 设置界面，根据主板说明关闭安全启动
   > 2. 以管理员身份打开 `命令提示符` 或 `PowerShell`
   > 3. 执行命令：`bcdedit /set testsigning on`
   > 4. 重启电脑后即可安装未签名驱动
   > 5. 如需关闭测试模式，执行：`bcdedit /set testsigning off` 并重启
   >
   > **注意**：测试模式下桌面右下角会显示"测试模式"水印，这是正常现象。

6. 驱动安装完成后，`显示适配器` 部分会出现一个新的 NanoKVM 显卡设备。

7. 在 Desk 上从屏幕中进入副屏页面，选择 USB，即可将 Desk 用作 USB 副屏。

8. 若需关闭，参考步骤 2 关闭 `Panel`。

9. 再次开启时，部分系统可能需要重新安装 USB 驱动。


## 自定义显示

> 注：此功能需要 NanoKVM-Desk 更新至 `1.1.5` 以及以上的应用版本

NanoKVM Desk 在`1.1.5` 版本中新增了用户自定义APP功能，通过长按屏幕/旋钮，切换到第四页面，可以看到所有的APP，默认预装三个Demo：`coin`、`conway`、`hello`

[hello.py](../../../assets/NanoKVM/pro/lcd/hello.py)
[conway.py](../../../assets/NanoKVM/pro/lcd/conway.py)
[coin.py](../../../assets/NanoKVM/pro/lcd/coin.py)

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
  <video playsinline controls muted preload src="../../../assets/NanoKVM/pro/lcd/doom.mp4"></video>
  <video playsinline controls muted preload src="../../../assets/NanoKVM/pro/lcd/conway.mp4"></video>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
  <video playsinline controls muted preload src="../../../assets/NanoKVM/pro/lcd/pao.mp4"></video>
  <video playsinline controls muted preload src="../../../assets/NanoKVM/pro/lcd/coin.mp4"></video>
</div>

### 如何构建自己的应用

NanoKVM Desk 会在系统 `/userapp` 目录下查找所有的文件夹，并将文件夹名称作为APP名称，建议文件夹名小于8个字符

`User APP` 界面下点击用户自定义用户程序后将会尝试启动文件夹内名为 `main.py` 的 Python 应用

此时小屏使用标准FB驱动，用户可以使用 `/dev/fb0` 来实现自定义的屏幕显示操作。

点击屏幕或按下旋钮将退出应用

