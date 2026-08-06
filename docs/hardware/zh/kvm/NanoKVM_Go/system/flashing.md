---
title: 烧录镜像
keywords: NanoKVM Go, Remote desktop, KVM, flashing
update:
    - date: 2026-07-15
      version: v0.1
      author: Liang Ziyue
      content:
          - 新增 NanoKVM Go 烧录镜像教程
---

*NanoKVM Go 出厂时通常已经烧录了镜像，如设备可以正常启动，可以先跳过该步骤。*

## 准备工作

烧录前请先准备：

- NanoKVM Go；
- 取卡针或其他可以按住 Reset 按键的工具；
- USB 数据线；
- Windows 电脑；
- NanoKVM Go 镜像文件；
- ImageUSB 烧录工具。

## 下载镜像

前往 GitHub 下载最新版 NanoKVM Go 镜像。

镜像下载链接：TODO


## 下载烧录工具

下载并安装 [ImageUSB](https://www.osforensics.com/tools/write-usb-images.html)。

![ImageUSB 下载页面](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_imageusb_download.webp)

## 进入烧录模式

1. 断开 NanoKVM Go 的 USB 连接；

2. 使用取卡针按住 NanoKVM Go 的 Reset 按键；

![使用取卡针按住 NanoKVM Go Reset 按键](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_press_reset.webp)

3. 保持按住 Reset 按键，将 USB 数据线插入 NanoKVM Go 的数据接口(Data Port)，并连接到电脑；

![按住 Reset 按键并连接 NanoKVM Go 数据接口](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_connect_data_port.webp)

4. 打开 ImageUSB，等待软件识别到 NanoKVM Go 对应的 USB 设备;

![ImageUSB 识别到 NanoKVM Go 设备](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_device_detected.webp)

5. 识别成功后，松开 Reset 按键。



## 使用 ImageUSB 烧录镜像

1. 在 ImageUSB 中选择 NanoKVM Go 对应的 USB 设备；

![在 ImageUSB 中选择 NanoKVM Go 设备](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_select_device.webp)

2. 选择写入镜像的模式；

![在 ImageUSB 中选择写入镜像模式](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_write_mode.webp)

3. 选择下载好的 NanoKVM Go 镜像文件；

![在 ImageUSB 中选择 NanoKVM Go 镜像文件](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_select_image.webp)

4. 点击写入按钮开始烧录；

![点击 ImageUSB 写入按钮](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_start_write.webp)

5. 根据软件提示确认写入操作；

![确认 ImageUSB 写入操作](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_confirm_write.webp)

6. 等待烧录完成。

![ImageUSB 正在写入镜像](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_write_progress.webp)

7. 烧录成功。

![ImageUSB 烧录完成](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_complete.webp)

烧录完成后，安全弹出 USB 设备，断开 USB 数据线，然后重新连接 NanoKVM Go，等待系统启动。

> 烧录过程中不要断开 USB 连接，也不要关闭 ImageUSB，否则可能导致镜像写入失败。
