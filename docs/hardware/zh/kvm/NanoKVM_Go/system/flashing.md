---
title: 烧录镜像
keywords: NanoKVM Go, Remote desktop, KVM, flashing
---

*NanoKVM Go 出厂时通常已经烧录了镜像，如设备可以正常启动，可以先跳过该步骤。*

## 准备工作

烧录前请先准备：

- NanoKVM Go；
- 取卡针或其他可以按住烧录模式按键的工具；
- USB 数据线；
- 电脑（Windows / macOS / Linux）；
- NanoKVM Go 镜像文件；
- 与电脑系统对应的烧录工具：
  - Windows：balenaEtcher 2.1.6 或 ImageUSB；
  - macOS：balenaEtcher 2.1.6；
  - Linux：balenaEtcher 2.1.6。

## 下载镜像

前往 GitHub 下载最新版 NanoKVM Go 镜像。

镜像下载链接：[NanoKVM-Go Releases](https://github.com/sipeed/NanoKVM-Go/releases)

## 下载烧录工具

balenaEtcher 支持 Windows、macOS 和 Linux，推荐优先使用；ImageUSB 仅支持 Windows，作为 Windows 上的备选。

### balenaEtcher 2.1.6（Windows / macOS / Linux）

请固定使用 balenaEtcher 2.1.6 版本：

下载链接：[balenaEtcher v2.1.6](https://github.com/balena-io/etcher/releases/tag/v2.1.6)

在 Release 页面的 `Assets` 中按系统选择安装包：

- Windows 选择 `balenaEtcher-2.1.6.Setup.exe`；
- macOS 选择 `balenaEtcher-2.1.6-arm64.dmg`（Apple 芯片）或 `balenaEtcher-2.1.6-x64.dmg`（Intel 芯片）；
- Linux 选择 `balena-etcher_2.1.6_amd64.deb`（Debian / Ubuntu）或 `balena-etcher-2.1.6-1.x86_64.rpm`（Fedora / RHEL）。

官网下载页按系统与架构列出安装包，但不能指定版本，所以请从上面的 Release 链接下载 2.1.6。

![balenaEtcher 官网下载页，安装包按系统与架构区分](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_etcher_download.webp)

### ImageUSB（Windows）

ImageUSB 仅支持 Windows。前往官网下载压缩包，解压后直接运行其中的 `imageUSB.exe`，无需安装。

下载链接：[ImageUSB](https://www.osforensics.com/tools/write-usb-images.html)

![ImageUSB 下载页面](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_imageusb_download.webp)

## 进入烧录模式

1. 断开 NanoKVM Go 的 USB 连接，使设备整体处于关机状态；

2. 使用取卡针通过按键孔按住 NanoKVM Go 的烧录模式按键；

![使用取卡针按住 NanoKVM Go 烧录模式按键](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_press_reset.webp)

3. 保持按住烧录模式按键，将连接电脑的 USB 数据线插入 NanoKVM Go 的数据接口(Data Port)；

![按住烧录模式按键并连接 NanoKVM Go 数据接口](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_connect_data_port.webp)

## 使用 balenaEtcher 烧录镜像（Windows / macOS / Linux）

1. 打开 balenaEtcher，点击 `从文件烧录`，选择下载好的 NanoKVM Go 镜像文件；

![balenaEtcher 点击从文件烧录](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_etcher_flash_from_file.webp)

2. 弹出 `找不到分区表` 提示时，点击 `继续`；

![balenaEtcher 找不到分区表提示，点击继续](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_etcher_no_partition_table.webp)

3. 点击 `选择目标磁盘`；

![balenaEtcher 选择目标磁盘](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_etcher_select_target.webp)

4. 在磁盘列表中勾选 NanoKVM Go 对应的磁盘（通常显示为 `Compute Module`），点击 `选定`；

![balenaEtcher 选择 NanoKVM Go 对应的磁盘](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_etcher_choose_disk.webp)

5. 点击 `现在烧录!`，进入烧录界面，等待烧录完成；

![balenaEtcher 烧录进行中](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_etcher_write_progress.webp)

6. 界面显示 `烧录成功！`，即烧录完成。

![balenaEtcher 烧录成功](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_etcher_complete.webp)

## 使用 ImageUSB 烧录镜像（Windows）

1. 打开 ImageUSB，点击 `Refresh Drives`，确认列表中已出现 NanoKVM Go 设备（显示为 `Linux File-Stor Gadget`）；

![点击 ImageUSB 的 Refresh Drives 按钮](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_refresh_drives.webp)

2. 在 `Step 1` 中勾选 NanoKVM Go 对应的 USB 设备；

![在 ImageUSB 中选择 NanoKVM Go 设备](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_select_device.webp)

3. 在 `Step 2` 中选择 `Write image to USB drive`；

![在 ImageUSB 中选择写入镜像模式](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_write_mode.webp)

4. 在 `Step 3` 中点击 `Browse`，选择下载好的 NanoKVM Go 镜像文件；

![在 ImageUSB 中选择 NanoKVM Go 镜像文件](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_select_image.webp)

5. 在 `Step 4` 中点击 `Write` 开始烧录；

![点击 ImageUSB 写入按钮](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_start_write.webp)

6. 弹出确认窗口时点击 `Yes` 确认写入；

![确认 ImageUSB 写入操作](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_confirm_write.webp)

7. 等待烧录完成；

![ImageUSB 正在写入镜像](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_write_progress.webp)

8. 出现 `Imaging Completed!` 提示，即烧录完成。

![ImageUSB 烧录完成](../../../../assets/NanoKVM/go/system/nanokvm_go_flashing_complete.webp)

烧录完成后，安全弹出 USB 设备，断开 USB 数据线，然后重新连接 NanoKVM Go，等待系统启动。

> 烧录过程中不要断开 USB 连接，也不要关闭烧录工具，否则可能导致镜像写入失败。
