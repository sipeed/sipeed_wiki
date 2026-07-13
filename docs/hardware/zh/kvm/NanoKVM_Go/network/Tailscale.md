---
title: Tailscale
keywords: Tailscale，远程控制，内网穿透
update:
    - date: 2026-07-13
      version: v0.1
      author: Liang Ziyue
---

# Tailscale

## 一、Tailscale简介

Tailscale 是一款基于 WireGuard 的异地组网工具。它可以将 NanoKVM Go 与电脑、手机等设备加入同一个虚拟局域网，使用户无需公网 IP，也无需在路由器上配置端口转发，即可从外网访问 NanoKVM Go。

加入 Tailscale 网络后，每台设备都会获得一个 `100.x.x.x` 格式的虚拟 IP 地址。只要访问端与 NanoKVM Go 位于同一个 Tailscale 网络（Tailnet），就可以通过该地址访问 NanoKVM Go。

```text
NanoKVM Go ── Tailscale 虚拟网络 ── 外网电脑或手机
```

> 本文将以网页配置方式为主，介绍如何使用 Tailscale 从外网访问 NanoKVM Go。

## 二、使用前准备

开始配置前，请确认：

- NanoKVM Go 已连接互联网；
- 可以在局域网内正常访问 NanoKVM Go；
- NanoKVM Go 的系统和应用版本支持 Tailscale；
- 用于外网访问的电脑或手机可以安装 Tailscale 客户端。
<!-- TODO：补充最低版本要求和版本查看方法。 -->

## 三、注册并登录 Tailscale

NanoKVM Go 和用于远程访问的电脑或手机需要加入同一个 Tailscale 网络（Tailnet）。首次使用时，需要先注册并登录 Tailscale：

1. 访问 [Tailscale 官网](https://tailscale.com/)；



2. 点击 `Get Started` 或 `Log in`；
3. 使用页面支持的账号完成登录；
4. 按照页面提示完成首次授权；
5. 进入 Tailscale 管理后台，并找到 `Machines` 设备列表。

`Machines` 页面用于查看和管理已经加入当前 Tailnet 的设备。完成后续配置后，NanoKVM Go 和访问端都会出现在该页面中。

<!-- TODO：补充官网登录入口、登录方式选择页面和 Machines 页面的截图。 -->

> Tailscale 的套餐、组织管理和高级网络设置并非基础远程访问的必需内容，本文不作展开。

## 四、在 NanoKVM Go 上启用 Tailscale

### 1. 打开 Tailscale 设置

<!-- TODO：补充进入 NanoKVM Go 设置页面的操作和截图。 -->

### 2. 安装或启动 Tailscale

<!-- TODO：补充安装、启动按钮的位置，以及安装完成后的页面状态。 -->

### 3. 登录 Tailscale

<!-- TODO：补充获取登录链接、登录账号及点击 Connect 授权的操作和截图。 -->

### 4. 确认 NanoKVM Go 已上线

<!-- TODO：补充登录成功后的界面，以及在线状态的判断方法。 -->

## 五、在访问端安装并登录 Tailscale

在需要远程访问 NanoKVM Go 的电脑或手机上安装 Tailscale：

1. 从 Tailscale 官方渠道下载并安装客户端；
2. 启动 Tailscale，并点击 `Log in`；
3. 使用注册时的同一账号登录；
4. 确认客户端显示已连接；
5. 检查设备列表中是否可以看到 NanoKVM Go。

如果使用不同账号，需要确保该账号已经被邀请加入 NanoKVM Go 所在的 Tailnet。

| 平台 | 安装方式 |
| --- | --- |
| Windows | 从 Tailscale 官网下载安装程序 |
| macOS | 从 Tailscale 官网或 App Store 安装 |
| Linux | 使用官方安装脚本或软件源安装 |
| Android | 从 Google Play 或其他官方渠道安装 |
| iOS / iPadOS | 从 App Store 安装 |

<!-- TODO：以 Windows 为例补充下载安装、登录和连接成功的截图，并补充各平台官方入口。 -->

## 六、查看 NanoKVM Go 的 Tailscale IP

NanoKVM Go 加入 Tailnet 后，会获得一个 `100.x.x.x` 格式的 Tailscale IP。可以通过 NanoKVM Go 的设置页面或 Tailscale 管理后台查看该地址。

<!-- TODO：补充两种查看方式及对应截图。 -->

## 七、从外网访问 NanoKVM Go

为确保测试使用的是外网连接，建议断开访问端当前的局域网，改用手机热点或移动网络：

1. 确认访问端的 Tailscale 客户端已连接；
2. 在浏览器地址栏输入 NanoKVM Go 的 Tailscale IP；
3. 登录 NanoKVM Go；
4. 测试远程画面、键鼠控制和电源控制等功能。

<!-- TODO：补充完整访问地址示例、登录界面和访问成功截图。 -->

## 八、日常使用与安全建议

- 为 Tailscale 账号启用双重验证；
- 为 NanoKVM Go 设置强密码，并保留设备自身的登录认证；
- 不要在路由器上额外开放 NanoKVM Go 的访问端口；
- 不要将 Tailscale 设备认证链接分享给他人；
- 定期检查 Tailscale 管理后台，移除不再使用的设备；
- 多用户环境建议使用 ACL 或 Grants 限制设备访问权限。

## 九、常见问题

### Tailscale 无法安装或启动

<!-- TODO：补充网络、版本、存储空间和服务状态等排查步骤。 -->

### 登录链接没有生成

<!-- TODO：补充互联网连接、系统时间和 Tailscale 服务的检查方法。 -->

### NanoKVM Go 显示离线

<!-- TODO：补充 Machines 页面状态和设备端状态检查方法。 -->

### 可以看到 Tailscale IP，但无法访问

<!-- TODO：补充访问端连接状态、Tailnet、ACL 和 NanoKVM 服务排查方法。 -->

### 连接成功但画面卡顿

<!-- TODO：补充网络延迟、带宽、画质和帧率相关建议。 -->

### 重启后没有自动连接

<!-- TODO：补充开机启动状态和重新登录方法。 -->

## 十、进阶配置

完成基础配置后，可以根据需要进一步了解：

- 使用 MagicDNS 通过设备名称访问 NanoKVM Go；
- 修改 NanoKVM Go 在 Tailnet 中的设备名称；
- 管理设备密钥过期策略；
- 使用 ACL 或 Grants 精确控制访问权限；
- 判断当前连接是点对点直连还是 DERP 中继；
- 使用 `tailscale status` 等命令检查连接状态；
- 退出当前账号或将 NanoKVM Go 更换到其他 Tailnet。

> 出口节点和子网路由器不是远程访问 NanoKVM Go 的必需配置，普通用户完成前七节即可正常使用。
