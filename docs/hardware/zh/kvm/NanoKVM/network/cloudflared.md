
---
title: 使用 Cloudflare Tunnel（cloudflared）让 NanoKVM 安全远程访问
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2025-11-16
    version: v0.1
    author: Johnnybyzhang
    content:
      - Release docs
---

Cloudflare Tunnel 能让 NanoKVM 通过 **仅出站连接** 安全地接入 Cloudflare，无需公网 IP、端口转发或开放入站防火墙规则。PiKVM 文档主要介绍 systemd 方案，而 NanoKVM 基于 BusyBox `init`，服务管理方式不同。

Cloudflare 未提供官方的 RISC‑V 架构 `cloudflared` 构建，因此在 NanoKVM 上的支持主要依赖社区贡献。

本指南参考了 PiKVM 社区文档，安全性细节不再重复展开。

> **适用对象**：使用 BusyBox/SysV `init` 的 NanoKVM 用户。\
> **范围**：Token 模式隧道、RISC‑V 架构二进制、最简 `init.d` 服务脚本。

---

## 前置准备

- Cloudflare Zero Trust 账户，并创建 **远程托管 Tunnel**（Dashboard → Access → Tunnels → *Create Tunnel*），复制 **Tunnel Token**。
- NanoKVM 终端访问权限。
- RISC‑V 架构的 `cloudflared` 可执行文件（使用 Go 本地编译）。构建细节参考：[https://github.com/cloudflare/cloudflared/issues/621](https://github.com/cloudflare/cloudflared/issues/621)
- （可选）参考 PiKVM 的 Cloudflare Tunnel 文档：[https://docs.pikvm.org/cloudflared/](https://docs.pikvm.org/cloudflared/)

> **安全提示**：Token 可以直接启动隧道，请妥善保管。

---

## 获取 cloudflared 二进制文件

### NanoKVM Pro（ARM 架构）

可直接从 Cloudflare/cloudflared 仓库下载，或使用PiKVM OS，并按照PiKVM的文档操作

### NanoKVM（RISC‑V 架构）

可选择：

- 使用社区自动构建（源码公开透明）：[https://github.com/Johnnybyzhang/cloudflared-riscv/releases](https://github.com/Johnnybyzhang/cloudflared-riscv/releases)
- 按照官方仓库 Issue #621 的方法自行编译

---

## 安装 cloudflared

建议通过 WebUI 挂载外部存储，将二进制文件放入系统可识别的 USB 设备中。

```sh
install -m 0755 /data/cloudflared /usr/sbin/cloudflared
/usr/sbin/cloudflared --version
```

---

## 最小化 Token 配置（推荐）

使用配置文件可避免 Token 暴露在进程列表里。

```sh
mkdir -p /etc/cloudflared
umask 077
cat >/etc/cloudflared/config.yml <<'YAML'
no-autoupdate: true
token: YOUR_TUNNEL_TOKEN_HERE
YAML
chmod 600 /etc/cloudflared/config.yml
```

### 前台一次性测试（便于排错）

```sh
cloudflared tunnel --config /etc/cloudflared/config.yml --no-autoupdate run
```

> **重要**：`--config`、`--logfile`、`--no-autoupdate` 等全局参数必须放在 **run 之前**。

---

## BusyBox `init` 启动服务（非 systemd）

创建一个在网络初始化 **之后** 启动的最简 `init.d` 脚本。以下示例使用 `S45`，位于 `S40network` 之后。

```sh
cat >/etc/init.d/S45cloudflared <<'SH'
#!/bin/sh
PATH=/usr/sbin:/usr/bin:/sbin:/bin
DAEMON="/usr/sbin/cloudflared"
CONF="/etc/cloudflared/config.yml"
LOG="/var/log/cloudflared.log"
PIDFILE="/var/run/cloudflared.pid"

start() {
    [ -x "$DAEMON" ] || { echo "cloudflared 未找到"; exit 1; }
    [ -f "$CONF" ]   || { echo "配置文件缺失：$CONF"; exit 1; }
    mkdir -p /var/run
    printf "启动 cloudflared: "
    # cloudflared 会自行写入日志文件，这里只避免输出到控制台
    "$DAEMON" tunnel --config "$CONF" --logfile "$LOG" --no-autoupdate run >/dev/null 2>&1 &
    echo $! >"$PIDFILE"
    echo "OK"
}

stop() {
    printf "停止 cloudflared: "
    if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
        kill "$(cat "$PIDFILE")" 2>/dev/null || true
        sleep 2
        kill -0 "$(cat "$PIDFILE")" 2>/dev/null && kill -9 "$(cat "$PIDFILE")" 2>/dev/null || true
        rm -f "$PIDFILE"
        echo "OK"
    else
        killall cloudflared 2>/dev/null && echo "OK" || echo "进程未运行"
    fi
}

status() {
    if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
        echo "cloudflared 正在运行（pid $(cat "$PIDFILE")）"
    else
        echo "cloudflared 已停止"; exit 1
    fi
}

case "$1" in
  start) start ;;
  stop) stop ;;
  restart|reload) stop; start ;;
  status) status ;;
  *) echo "用法: $0 {start|stop|restart|status}"; exit 1 ;;
esac
exit 0
SH
chmod +x /etc/init.d/S45cloudflared
```

### 启动与验证

```sh
/etc/init.d/S45cloudflared start
/etc/init.d/S45cloudflared status
tail -n 100 /var/log/cloudflared.log
```

> **为什么终端仍可能看到日志？**\
> 如果你手动执行 `init.d` 脚本，子进程可能继承当前 TTY。示例中的 `>/dev/null 2>&1` 已能避免大部分输出；真正日志请查看 `--logfile` 指定的文件。

---

## 网络与时间

- 仅需 **出站连接**：TCP/443（以及可选的 UDP/7844）
- 请确保系统时间准确（NTP），否则可能无法通过 TLS 验证

---

## 排错提示（如自行编写 init.d 脚本）

- **“flag provided but not defined: -config”** → `--config` 必须放在 `run` 前。
- **无日志输出** → 检查 `/var/log/cloudflared.log` 是否存在并具备权限。
- **无法正常停止** → 建议使用 `--pidfile`；如文件不存在则会执行 `killall` 回退方案。
- **Token 安全** → 避免在命令行直接传入 `--token`。

---

## 卸载 / 禁用

```sh
/etc/init.d/S45cloudflared stop
chmod -x /etc/init.d/S45cloudflared
rm -f /usr/sbin/cloudflared /etc/cloudflared/config.yml /var/log/cloudflared.log /var/run/cloudflared.pid
```

---

## 参考资料

- PiKVM Cloudflare Tunnel 文档：[https://docs.pikvm.org/cloudflared/](https://docs.pikvm.org/cloudflared/)
- cloudflared RISC‑V 构建讨论：[https://github.com/cloudflare/cloudflared/issues/621](https://github.com/cloudflare/cloudflared/issues/621)

