---
title: 更新应用
keywords: NanoKVM Go, Remote desktop, KVM, update
update:
    - date: 2026-07-15
      version: v0.1
      author: Liang Ziyue
      content:
          - 新增 NanoKVM Go 更新应用教程
---

NanoKVM Go 支持在网页控制端中更新应用。更新前请确保设备已经连接网络，并且已经获得 IP 地址。

## 使用前准备

更新前请先确认：

- NanoKVM Go 已正常启动；
- NanoKVM Go 已连接到可访问互联网的网络；
- NanoKVM Go 已通过 DHCP 或静态 IP 获得 IP 地址；
- 电脑与 NanoKVM Go 位于同一可访问网络中；
- 浏览器可以正常打开 NanoKVM Go 的网页控制端。

## 进入控制页面

1. 打开浏览器；
2. 在地址栏输入 NanoKVM Go 的 IP 地址；
3. 进入 NanoKVM Go 网页控制端；
4. 如果页面要求登录，请先完成登录。


## 打开设置页面

在控制页面顶部菜单栏中，点击 `设置` 按钮，进入设置页面。

![NanoKVM Go 设置按钮](../../../../assets/NanoKVM/go/system/nanokvm_go_updating_settings_button.webp)

## 检查更新

进入设置页面后，点击 `检查更新`。

![NanoKVM Go 检查更新页面](../../../../assets/NanoKVM/go/system/nanokvm_go_updating_check_update.webp)

如果检测到可用更新，页面会弹出确认提示。点击 `确定` 开始更新。

![确认更新 NanoKVM Go 应用](../../../../assets/NanoKVM/go/system/nanokvm_go_updating_confirm_update.webp)

## 等待更新完成

点击确定后，保持 NanoKVM Go 通电并保持网络连接，等待应用更新完成。

![NanoKVM Go 应用更新进度](../../../../assets/NanoKVM/go/system/nanokvm_go_updating_progress.webp)

更新过程中请勿断电，也不要刷新或关闭页面。更新完成后，按照页面提示继续操作；如果页面自动刷新或重新进入登录页面，重新登录即可。

## 更新完成

更新完成后，可以继续通过浏览器访问 NanoKVM Go，并正常使用远程控制功能。
