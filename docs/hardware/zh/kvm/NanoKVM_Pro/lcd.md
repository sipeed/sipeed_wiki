---
title: 自定义副屏
keywords: NanoKVM,  Auxiliary Screen
update:
  - date: 2025-10-10
    version: v0.1
    author: zepan
    content:
      - initial docs
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

6. 驱动安装完成后，`显示适配器` 部分会出现一个新的 NanoKVM 显卡设备。

7. 在 Desk 上从屏幕中进入副屏页面，选择 USB，即可将 Desk 用作 USB 副屏。

8. 若需关闭，参考步骤 2 关闭 `Panel`。

9. 再次开启时，部分系统可能需要重新安装 USB 驱动。


## 自定义显示
NanoKVM-Pro的小屏使用标准FB驱动，用户可以使用/dev/fb0来实现自定义的屏幕显示操作。
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


