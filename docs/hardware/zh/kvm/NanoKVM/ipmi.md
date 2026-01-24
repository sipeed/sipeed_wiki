---
title: IPMI 操作文档
keywords: IPMI, NanoKVM, Remote desktop, PiKVM, RISCV, tool
---

> 💡 在开始操作前，请先将您的系统镜像更新至 [v1.4.2](https://github.com/sipeed/NanoKVM/releases/tag/v1.4.2) 或更高版本。

## 项目概述

本项目提供了一个基于软件的 IPMI 模拟器。它允许用户通过标准的 IPMI 协议远程管理硬件设备的电源状态以及访问串口终端。

核心组件包括：

- **`ipmi_sim`**:  开源的 IPMI 模拟器主程序 (OpenIPMI 项目的一部分)。
- **`ipmi-sim.sh`**: 服务管理脚本，负责启动、停止和监控模拟器进程。
- **`chassis_control.sh`**: 硬件抽象层脚本，通过 GPIO 直接控制物理硬件的电源和复位引脚。
- **`lan.conf`**: IPMI 模拟器的配置文件，定义用户、网络接口和 SOL 串口参数。

---

## 登录设备

在开始安装和配置之前，您需要先登录到 NanoKVM 的系统终端。支持以下两种方式：

### 方式一：网页终端

1. 在浏览器地址栏输入 NanoKVM 的 IP 地址，访问 Web 管理界面。
2. 在菜单栏中找到 **终端** 图标，并点击打开 **网页终端**。

### 方式二：SSH 远程登录

如果您习惯使用命令行工具，可以通过 SSH 进行连接。

1. 打开您电脑上的终端。
2. 执行以下命令（请将 `<IP地址>` 替换为 NanoKVM 的实际 IP）：

   ```bash
   ssh root@<IP地址>
   ```

3. 输入默认密码 `root` 完成登录。

---

## 安装与部署

本服务默认安装在 `/etc/ipmi` 目录下。

### 目录结构

确保您的系统包含以下文件结构：

```text
/etc/ipmi/
├── ipmi-sim.sh        # 服务控制脚本
├── chassis_control.sh # 硬件控制脚本
├── lan.conf           # 配置文件
├── sim.emu            # 模拟器持久化数据
```

---

## 配置指南

### 用户与密码 (`lan.conf`)

默认配置文件包含一个管理员账户。
**为了安全起见，建议在部署前修改默认密码。**

编辑 `/etc/ipmi/lan.conf` 文件末尾的部分：

```text
# User 2: Admin user
#         启用   用户名    密码      权限     会话数  认证方式
user 2    true   "admin"  "admin"  admin    10     md5
```

修改 `"admin"` (第二个) 为您的自定义密码。

### 串口重定向 (SOL)

如果需要通过 IPMI 查看设备串口输出，请在 `lan.conf` 中配置 `sol` 选项：

```text
# 对应设备的物理串口，例如 /dev/ttyS1
sol "/dev/ttyS1" 115200 nortscts
```

---

## 服务管理

使用 `ipmi-sim.sh` 脚本来管理服务。

### 常用命令

| 操作 | 命令 | 说明 |
| :--- | :--- | :--- |
| **启动服务** | `/etc/ipmi/ipmi-sim.sh start` | 启动 IPMI 模拟器后台进程 |
| **停止服务** | `/etc/ipmi/ipmi-sim.sh stop` | 停止运行中的服务 |
| **重启服务** | `/etc/ipmi/ipmi-sim.sh restart` | 先停止再启动 |
| **查看状态** | `/etc/ipmi/ipmi-sim.sh status` | 检查服务是否运行及 PID |
| **开机自启** | `/etc/ipmi/ipmi-sim.sh enable` | 设置服务随系统启动自动运行 |
| **取消自启** | `/etc/ipmi/ipmi-sim.sh disable` | 取消开机自启 |

### 示例

```bash
# 启用开机自启并立即启动服务
/etc/ipmi/ipmi-sim.sh enable
/etc/ipmi/ipmi-sim.sh start
```

---

## 客户端使用说明 (ipmitool)

您可以在任何支持 IPMI 的客户端上使用 `ipmitool` 进行远程管理。

**连接参数说明:**

- `-H`: 目标 IP 地址 (例如 NanoKVM 的 IP)
- `-U`: 用户名 (默认: admin)
- `-P`: 密码 (默认: admin)
- `-I`: 接口类型 (使用 `lanplus` 支持 IPMI 2.0)
- `-C`: 加密套件 (Cipher Suite)。**建议使用 `-C 3`** 以跳过漫长的协议协商过程。

### 支持的命令列表

本项目目前仅支持以下核心 IPMI 命令：

| 类别 | 命令 (ipmitool) | 说明 |
| :--- | :--- | :--- |
| **电源控制** | `power status` | 查看当前电源运行状态 (ON/OFF) |
| | `power on` | 执行开机操作 |
| | `power off` | 执行关机操作 (通常为强制断电，长按电源键) |
| | `power reset` | 执行复位操作 (按下重启键) |
| **串口 (SOL)** | `sol activate` | 启动远程串口会话 |
| | `sol deactivate` | 终止远程串口会话 |
| **管理** | `mc info` | 查看模拟器的 BMC 基本信息 |

### 电源控制

```bash
# 查看电源状态
ipmitool -H <IP> -U admin -P admin -I lanplus power status

# 开机
ipmitool -H <IP> -U admin -P admin -I lanplus power on

# 关机 (直接断电)
ipmitool -H <IP> -U admin -P admin -I lanplus power off

# 重启 (复位)
ipmitool -H <IP> -U admin -P admin -I lanplus power reset
```

### 串口重定向 (SOL)

通过网络连接到设备的串口终端：

```bash
# 激活 SOL 会话
ipmitool -H <IP> -U admin -P admin -I lanplus sol activate

# 退出 SOL 会话
# 按键顺序: ~ + . (波浪号后跟点号)
```

注意：如果 SOL 连接无法建立，请检查 `lan.conf` 中的串口设备路径是否正确，以及是否有其他程序占用了该串口。

### 性能优化说明

默认情况下，`ipmitool` 会尝试与服务器协商加密协议，这可能导致每次执行命令前有数秒的卡顿。
**解决方法**：在命令中显式添加 `-C 3` 参数。

**优化后的常用命令示例：**

```bash
# 1. 快速获取 BMC 信息 (推荐测试命令)
ipmitool -H <IP> -U admin -P admin -I lanplus -C 3 mc info

# 2. 快速查看电源状态
ipmitool -H <IP> -U admin -P admin -I lanplus -C 3 power status

# 3. 快速激活串口
ipmitool -H <IP> -U admin -P admin -I lanplus -C 3 sol activate
```

---

## 故障排查

1. **服务无法启动**
   - 检查端口 623 (UDP) 是否被占用：`netstat -ln | grep 623`
   - 检查日志输出。尝试手动前台运行命令看报错信息。

2. **ipmitool 连接超时**
   - 检查防火墙设置，确保 UDP 623 端口开放。
   - 确认 `ipmi_sim` 进程正在运行 (`ps aux | grep ipmi_sim`).
