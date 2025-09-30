---
title: 静态 IP
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2024-8-13
    version: v0.1
    author: xwj
    content:
      - Release docs
---

NanoKVM 默认通过 DHCP 获取 IP，这意味着 NanoKVM 的 IP 可能会发生变化。

如果你希望始终使用同一个 IP 来访问 NanoKVM，可以给 NanoKVM 设置一个静态 IP。

下面介绍两种方法设置静态IP：

## 通过路由器设置静态IP

路由器后台往往有设置设备静态IP的功能，如果您可以方便的进入路由器的管理页面，建议使用此方式。

在路由器管理后台可以找到带有`kvm`名字的设备，并直接设置IP。

## 在NanoKVM中设置静态 IP

如果不方便进入路由器后台，也可以直接在NanoKVM中设置，方法如下

### 设置静态IP

在 NanoKVM 中创建文件 `/boot/eth.nodhcp` ，然后按照以下规则进行编辑：

- 一行就是一个自定义 IP，格式为 `addr/netid gw[optional]` ；
- 可以分多行来预设多个静态 IP。

```bash
# 示例
192.168.0.101/24 192.168.0.1  # addr/netid gw
192.168.3.116/22              # addr/netid
```

编辑并保存该文件后，执行 `/etc/init.d/S30eth restart` 命令使配置文件生效。

**注意**，如果所有预设的静态 IP 地址都被 arp 检测到已占用，则静态 IP 会设置失败。
此时会触发 DHCP 来获取 IP 地址。如果仍然获取失败，则会将 IP 强制设置成 `192.168.90.1/24`。

这是为了保证 NanoKVM 总有一个可用的 IP 地址，以便能通过网络来操作 NanoKVM。
如果 NanoKVM 没有分配到可用的 IP 地址，则需要手动修改 TF 卡中的文件，或者重新烧录镜像才能正常使用。

### 取消静态IP设置

删除 `/boot/eth.nodhcp` 文件，即可取消静态 IP。NanoKVM 会重新通过 DHCP 来获取 IP。
