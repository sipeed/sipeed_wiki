---
title: NanoKVM Admin
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, ARM, tool
update:
  - date: 2025-11-20
    version: v0.1
    author: xwj
    content:
      - Release docs
---

## 简介

NanoKVM Admin 是一款用于批量管理 NanoKVM 设备的工具。它旨在通过简洁的 Web 界面，帮助用户集中管理局域网内所有的 NanoKVM 设备。无论是拥有几台设备的家庭实验室用户，还是管理数十台设备的运维人员，NanoKVM Admin 都能让您轻松发现并一键访问您的 KVM 设备。

主要功能：

- 自动发现： 基于 mDNS 协议，一键扫描局域网内的 NanoKVM 设备。
- 手动添加： 支持手动添加特定 IP 地址的设备，适应复杂网络环境。
- 集中管理： 在统一的网页视图中查看所有设备。
- 快捷访问： 点击即可跳转至单台 NanoKVM 的访问页面。

## 安装

在"设置 - 账户"中找到 NanoKVM Admin，点击"安装"并等待安装完成即可。

![install](./../../../assets/NanoKVM/pro/kvmadmin/zh/install.jpg)

安装完成之后，可点击【访问】按钮打开页面。或在浏览器地址栏输入访问地址"NanoKVM-Pro的IP:8999"（例如：`https://192.168.3.102:8999`）。

![visit](./../../../assets/NanoKVM/pro/kvmadmin/zh/visit.jpg)

## 设备添加

NanoKVM Admin 提供了两种添加设备的方式，您可以根据实际情况选择。

### 方式一：mDNS 自动扫描

适用于设备位于同一网段，且路由器支持 mDNS 广播的环境。

1. 确保 NanoKVM 设备均已开启 mDNS 发现功能。
2. 点击【发现设备】按钮。
3. 系统将自动搜索网络中在线的 NanoKVM 设备。
4. 搜索完成后，列表将显示发现的设备信息。

![scan](./../../../assets/NanoKVM/pro/kvmadmin/zh/scan.jpg)

### 方式二：手动添加

适用于跨网段访问，或 mDNS 无法发现设备的情况。

1. 点击【添加设备】按钮。
2. 在弹出的对话框中填写设备信息。
3. 点击【确认】保存。

![manual](./../../../assets/NanoKVM/pro/kvmadmin/zh/manual_add.jpg)

## 设备管理与访问

### 设备仪表盘

添加完成后，所有设备将以列表形式展示在主页仪表盘上。您可以看到：

- IP 地址：设备的 IP 地址，该字段是唯一的并且不可编辑。
- mDNS 地址：设备的 mDNS 地址。
- 在线状态：设备是否在线，服务会周期性地扫描局域网内的设备状态并更新。
- 其他信息：如 MAC 地址、来源等信息。
- 操作按钮：访问、编辑和删除按钮。

![devices](./../../../assets/NanoKVM/pro/kvmadmin/zh/devices.jpg)

### 访问设备

需要控制某台设备时：

- 点击设备 IP 即可通过 IP 地址访问该设备。
- 点击设备 mDNS 即可通过 mDNS 地址访问该设备。
- 点击操作中的“访问”图标即可通过 IP 地址访问设备。

### 编辑与删除

- 修改信息：点击操作中的“编辑”图标，即可修改设备 mDNS 和备注等信息。
- 删除设备：点击操作中的“删除”图标，即可将设备从管理列表中移除。

## 用户管理

点击左侧的【用户列表】即可进入用户管理界面。在这里可以进行用户添加、编辑和删除操作。

![users](./../../../assets/NanoKVM/pro/kvmadmin/zh/users.jpg)

## 服务管理

服务通过 systemctl 运行，可通过以下命令进行操作：`systemctl start/stop/restart kvmadmin.service`。

### 服务信息

- 服务安装位置：`/kvmadmin`
- 服务配置文件：`/etc/kvmadmin/server.yaml`
- SQLite 数据库文件：`/etc/kvmadmin/kvm.db`

### 服务证书

修改配置文件 `/etc/kvmadmin/server.yaml` 中的 `cert.crt` 和 `cert.key` 参数，然后执行以下命令重启服务：

```bash
systemctl restart kvmadmin.service
```

### 卸载服务

在设置页面中点击【卸载】按钮即可卸载服务。该操作会删除所有安装文件和数据，请谨慎操作。

![uninstall](./../../../assets/NanoKVM/pro/kvmadmin/zh/uninstall.jpg)
