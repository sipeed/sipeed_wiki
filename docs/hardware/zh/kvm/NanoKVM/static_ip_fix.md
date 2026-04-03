---
title: NanoKVM 静态IP地址修复
---

## 适用情况

1. NanoKVM 被设置为静态 IP 后，无法通过 DHCP 自动获取地址。

## 问题原因

部分批次的 NanoKVM 出厂时被误配置为静态 IP（`192.168.70.70`），因此无法通过 DHCP 获取动态地址。

## 修复步骤

可根据实际情况选择以下任一方法：

### 方法 1：重新烧录固件

重新烧录 NanoKVM 固件，恢复默认网络配置。
具体操作可参考：[烧录系统](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/flashing.html)。

### 方法 2：可方便拔出 SD 卡

若设备便于取出 SD 卡，可使用读卡器连接电脑，删除 SD 卡第一个分区中的 `eth.nodhcp` 文件。

### 方法 3：不方便拔出 SD 卡（如 Cube 用户）

1. 使用卡针等尖锐物体，插入 USB-C 接口旁的圆形小孔（该孔为 Reset 键）并向下按压。
2. 保持按压状态，同时使用 USB 线将设备连接到电脑。
3. 等待电脑识别出 U 盘设备；当 `boot` 盘符出现后，松开卡针。
4. 删除该分区中的 `eth.nodhcp` 文件。
