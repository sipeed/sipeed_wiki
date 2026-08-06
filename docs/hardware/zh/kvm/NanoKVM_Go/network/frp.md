---
title: frp
keywords: NanoKVM Go, frp, 远程访问, 内网穿透
update:
    - date: 2026-07-14
      version: v0.2
      author: Liang Ziyue
      content:
          - 新增 NanoKVM Go frp 远程访问教程
---

# 配置 frp 远程访问

frp 是一款内网穿透工具，可以将局域网内的 NanoKVM Go 服务转发到具有公网 IP 的服务器。配置完成后，即使 NanoKVM Go 所在网络没有公网 IP，也可以通过公网服务器远程访问它。

frp 由两个组件组成：

- `frps`：服务端，运行在具有公网 IP 的服务器上；
- `frpc`：客户端，运行在 NanoKVM Go 上。

```text
远程电脑或手机
       |
       | 访问 https://公网 IP:8080
       v
公网服务器（frps） <----- frpc 主动连接 ----- NanoKVM Go
```

> NanoKVM Go 网页端目前没有 FRP 配置入口，需要先在网页端开启 SSH，再通过 SSH 手动安装和配置 `frpc`。

> 将 NanoKVM Go 暴露到公网会增加被扫描、撞库和攻击的风险。请先为 NanoKVM Go 设置强密码。本文的基础 TCP 示例会转发 NanoKVM Go 本机的 HTTPS 服务，但设备证书通常是自签名证书，浏览器可能提示证书不受信任。有域名时可以配置可信域名证书；如果不希望暴露公网端口，也可以改用 Tailscale 等虚拟组网方案。

## 准备工作

开始配置前，请准备：

- 一台具有公网 IPv4 地址的 Linux 服务器；
- 已连接互联网的 NanoKVM Go；
- NanoKVM Go 和公网服务器的管理员权限；
- 公网服务器云安全组和系统防火墙的修改权限；
- 一个不容易被猜到的 frp 身份验证 Token。

本文使用以下示例参数：

| 项目 | 示例值 | 用途 |
| --- | --- | --- |
| 公网服务器 IP | `203.0.113.10` | 运行 `frps` |
| frps 通信端口 | `7000` | `frpc` 连接 `frps` |
| NanoKVM Go 公网访问端口 | `8080` | 浏览器访问 NanoKVM Go |
| NanoKVM Go Web 地址 | `127.0.0.1:443` | `frpc` 转发的本地 HTTPS 服务 |
| Token | `replace_with_a_strong_token` | 验证 `frpc` 身份 |

`203.0.113.10` 是文档示例地址，不能直接使用。请将本文中的公网 IP、端口和 Token 替换为自己的实际参数。

## 在公网服务器上安装 frps

### 下载 frp

先查看服务器的 CPU 架构：

```bash
uname -m
```

打开 [frp Releases](https://github.com/fatedier/frp/releases)，选择与服务器架构匹配的 Linux 安装包。常见架构对应关系如下：

| `uname -m` 输出 | frp 安装包架构 |
| --- | --- |
| `x86_64` | `linux_amd64` |
| `aarch64`、`arm64` | `linux_arm64` |
| `armv7l` | `linux_arm_hf` |
| ARMv5 等较旧 ARM 设备 | `linux_arm` |
| `riscv64` | `linux_riscv64` |

本文以 frp `0.70.0` 为例，可以在发布页面中直接下载：

- [frp 0.70.0 发布页面](https://github.com/fatedier/frp/releases/tag/v0.70.0)
- [Linux AMD64 安装包](https://github.com/fatedier/frp/releases/download/v0.70.0/frp_0.70.0_linux_amd64.tar.gz)
- [Linux ARM64 安装包](https://github.com/fatedier/frp/releases/download/v0.70.0/frp_0.70.0_linux_arm64.tar.gz)
- [Linux ARMv7 硬浮点安装包](https://github.com/fatedier/frp/releases/download/v0.70.0/frp_0.70.0_linux_arm_hf.tar.gz)
- [Linux RISC-V 64 安装包](https://github.com/fatedier/frp/releases/download/v0.70.0/frp_0.70.0_linux_riscv64.tar.gz)

大多数云服务器的架构为 `x86_64`。如果 `uname -m` 输出为 `x86_64`，执行以下命令下载并安装：

```bash
wget https://github.com/fatedier/frp/releases/download/v0.70.0/frp_0.70.0_linux_amd64.tar.gz
tar -xzf frp_0.70.0_linux_amd64.tar.gz
cd frp_0.70.0_linux_amd64
sudo install -m 755 frps /usr/local/bin/frps
```

`sudo install -m 755 frps /usr/local/bin/frps` 的作用是将当前目录下的 `frps` 程序复制到 `/usr/local/bin/frps`，并把权限设置为 `755`，也就是所有用户都可以执行，只有文件所有者可以修改。

如果服务器是其他架构，请下载表格中对应的安装包，并将命令中的压缩包名称和解压目录替换为实际名称。公网服务器与 NanoKVM Go 应使用同一个 frp 版本。

确认 `frps` 可以运行：

```bash
/usr/local/bin/frps --version
```

> 建议在公网服务器和 NanoKVM Go 上安装同一版本的 frp，避免因版本差异造成配置不兼容。

### 创建 frps 配置

创建配置目录：

```bash
sudo mkdir -p /etc/frp
```

创建 `/etc/frp/frps.toml`：

```toml
bindPort = 7000

auth.method = "token"
auth.token = "replace_with_a_strong_token"
```

请将 `auth.token` 替换为随机生成的强 Token。可以在公网服务器上使用以下命令生成：

```bash
openssl rand -hex 32
```

frps 和 frpc 配置中的 Token 必须完全一致。Token 只用于验证 frpc，不能代替 NanoKVM Go 自身的登录密码，也不能代替浏览器访问时使用的 HTTPS 证书。

### 启动 frps

先在前台启动，以便直接观察日志：

```bash
sudo /usr/local/bin/frps -c /etc/frp/frps.toml
```

没有报错时，按 `Ctrl+C` 停止测试。前台运行方式适用于所有 Linux 系统，但关闭终端后 frps 也会停止，因此长期使用时还需要将其注册为系统服务。

#### 确认 init 系统

执行以下命令查看 PID 1 对应的程序：

```bash
ps -p 1 -o comm=
```

根据输出选择启动方式：

| 输出示例 | 启动方式 |
| --- | --- |
| `systemd` | 使用 systemd |
| `init`、`sysvinit`，并且存在 `/etc/init.d/` | 使用 SysV init |
| `openrc-init` | 使用 OpenRC |

> 是否可以使用 systemd，应以 PID 1 是否为 `systemd` 为准。系统中存在 `systemctl` 命令，并不表示当前系统已经通过 systemd 启动。

#### 使用 systemd 启动

仅当 `ps -p 1 -o comm=` 输出为 `systemd` 时，才使用本节命令。

创建 `/etc/systemd/system/frps.service`：

```ini
[Unit]
Description=frp server
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/local/bin/frps -c /etc/frp/frps.toml
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

加载服务并设置开机自启：

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now frps
sudo systemctl status frps
```

如果状态为 `active (running)`，表示 frps 已经启动。使用以下命令查看实时日志：

```bash
sudo journalctl -u frps -f
```

#### 使用 SysV init 启动

如果系统使用 SysV init，并且存在 `start-stop-daemon` 命令，可以创建 `/etc/init.d/frps`：

```sh
#!/bin/sh

DAEMON=/usr/local/bin/frps
CONFIG=/etc/frp/frps.toml
PIDFILE=/var/run/frps.pid

case "$1" in
    start)
        if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
            echo "frps is already running"
            exit 0
        fi
        echo "Starting frps"
        start-stop-daemon --start --background --make-pidfile \
            --pidfile "$PIDFILE" --exec "$DAEMON" -- -c "$CONFIG"
        ;;
    stop)
        echo "Stopping frps"
        start-stop-daemon --stop --pidfile "$PIDFILE" --retry TERM/5/KILL/5
        rm -f "$PIDFILE"
        ;;
    restart)
        "$0" stop
        "$0" start
        ;;
    status)
        if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
            echo "frps is running"
        else
            echo "frps is not running"
            exit 1
        fi
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 1
        ;;
esac
```

为脚本添加执行权限：

```bash
sudo chmod +x /etc/init.d/frps
```

在 Debian、Ubuntu 等使用 `update-rc.d` 的 SysV init 系统中，设置开机自启并启动服务：

```bash
sudo update-rc.d frps defaults
sudo service frps start
sudo service frps status
```

如果系统没有 `update-rc.d`，请使用当前发行版提供的 SysV init 服务管理命令。

#### 没有 systemd 的环境

如果出现以下错误：

```text
System has not been booted with systemd as init system (PID 1). Can't operate.
Failed to connect to bus: Host is down
```

说明当前环境不是通过 systemd 启动的，不能继续使用 `systemctl`。可以先使用前台命令测试 frps：

```bash
sudo /usr/local/bin/frps -c /etc/frp/frps.toml
```

如果需要长期运行，请根据当前发行版实际使用的 init 系统添加服务配置。

### 放行公网服务器端口

在云服务器安全组和系统防火墙中放行：

- `7000/tcp`：NanoKVM Go 上的 frpc 连接 frps；
- `8080/tcp`：远程浏览器访问 NanoKVM Go。

不同 Linux 发行版使用的防火墙工具可能不同。先执行：

```bash
command -v ufw
command -v firewall-cmd
```

根据命令输出选择对应的小节。不要在没有安装相关工具的系统中直接执行命令。

#### 使用 UFW

如果 `command -v ufw` 输出了 UFW 的路径，执行：

```bash
sudo ufw allow 7000/tcp
sudo ufw allow 8080/tcp
sudo ufw status
```

如果终端提示 `ufw: command not found`，说明当前系统没有安装 UFW。UFW 不是运行 frps 的必要组件，请继续检查系统是否使用 firewalld、其他防火墙，或者只使用云服务器安全组。

#### 使用 firewalld

如果 `command -v firewall-cmd` 输出了 firewalld 的命令路径，执行：

```bash
sudo firewall-cmd --permanent --add-port=7000/tcp
sudo firewall-cmd --permanent --add-port=8080/tcp
sudo firewall-cmd --reload
sudo firewall-cmd --list-ports
```

#### 使用云服务器安全组

阿里云、华为云、腾讯云、AWS 等云服务器通常还有独立于 Linux 系统的安全组。即使服务器内部没有安装 UFW 或 firewalld，也必须在云服务器管理页面中添加入站规则：

| 协议 | 端口 | 来源 |
| --- | --- | --- |
| TCP | `7000` | NanoKVM Go 所在网络的公网 IP；无法固定时可临时使用任意来源进行测试 |
| TCP | `8080` | 需要访问 NanoKVM Go 的公网 IP；无法固定时可临时使用任意来源进行测试 |

测试完成后，建议将来源范围缩小到实际需要的 IP，不要长期允许所有公网地址访问。

确认 frps 正在监听 `7000` 端口：

```bash
sudo ss -lntp | grep ':7000'
```

还可以确认远程访问端口是否已由 frps 监听：

```bash
sudo ss -lntp | grep ':8080'
```

> `8080` 端口需要在 NanoKVM Go 上的 frpc 成功连接并注册代理后才会出现。

## 在 NanoKVM Go 网页端开启 SSH

NanoKVM Go 网页端没有 FRP 入口，因此需要先开启 SSH，再通过命令行安装 frpc。

### 登录 NanoKVM Go

1. 在浏览器中打开 NanoKVM Go 的局域网地址；
2. 输入账号和密码，登录网页控制端；
3. 确认 NanoKVM Go 当前的局域网 IP 地址。

### 打开 SSH 设置

1. 打开 NanoKVM Go 的设置页面；

![NanoKVM Go 设置页面入口](../../../../assets/NanoKVM/go/network/nanokvm_go_frp_settings_entry.webp)

2. 进入包含 SSH 开关的设置项；开启 SSH 服务；

![NanoKVM Go SSH 开关页面](../../../../assets/NanoKVM/go/network/nanokvm_go_frp_ssh_switch.webp)

### 通过 SSH 登录

在与 NanoKVM Go 位于同一局域网的电脑上打开终端，通过 SSH 登录：

```bash
ssh <SSH用户名>@<NanoKVM-Go局域网IP>

例如: ssh root@192.168.0.225
```

> 首次连接时，终端会询问是否信任设备指纹。确认 IP 地址无误后输入 `yes`，再输入 SSH 密码。用户名是 `root`，密码是 `sipeed`

## 在 NanoKVM Go 上安装 frpc

后续命令均在 NanoKVM Go 的 SSH 终端中执行。

### 确认系统架构

执行：

```bash
uname -m
```

NanoKVM Go 实机执行 `uname -m` 的输出为：

```text
armv7l
```

因此应使用 frp 的 `linux_arm_hf` 安装包。该安装包针对 ARMv7 硬浮点环境构建，不要下载 `linux_arm64`。

### 下载并安装 frpc

NanoKVM Go 的 `/tmp` 通常挂载在内存中的 tmpfs 上，空间较小。建议将安装包下载到根分区中的 `/root` 目录。

执行以下命令下载并安装 frpc：

```bash
cd /root
wget https://github.com/fatedier/frp/releases/download/v0.70.0/frp_0.70.0_linux_arm_hf.tar.gz
tar -xzf frp_0.70.0_linux_arm_hf.tar.gz
cd frp_0.70.0_linux_arm_hf
mkdir -p /usr/local/bin
cp frpc /usr/local/bin/frpc
chmod +x /usr/local/bin/frpc
```

下载或解压失败时，请先确认 NanoKVM Go 可以访问 GitHub，并检查命令中的版本号和文件名是否与 Releases 页面一致。

确认安装结果：

```bash
/usr/local/bin/frpc --version
```

如果 NanoKVM Go 无法直接访问 GitHub，也可以先在电脑上下载安装包，再使用 `scp` 上传到设备的 `/root` 目录：

```bash
scp frp_0.70.0_linux_arm_hf.tar.gz <SSH用户名>@<NanoKVM-Go局域网IP>:/root/
```

### 创建 frpc 配置

创建配置目录：

```bash
mkdir -p /etc/frp
```

创建 `/etc/frp/frpc.toml`：

```toml
serverAddr = "203.0.113.10"
serverPort = 7000

auth.method = "token"
auth.token = "replace_with_a_strong_token"

[[proxies]]
name = "nanokvm-go-web"
type = "tcp"
localIP = "127.0.0.1"
localPort = 443
remotePort = 8080
```

需要修改的参数如下：

| 参数 | 修改内容 |
| --- | --- |
| `serverAddr` | 公网服务器的实际 IP 或域名 |
| `serverPort` | frps 的 `bindPort`，本文为 `7000` |
| `auth.token` | 与 `frps.toml` 完全相同的 Token |
| `localPort` | NanoKVM Go Web 服务的实际监听端口，本文使用 HTTPS 端口 `443` |
| `remotePort` | 公网访问端口，本文为 `8080` |

先检查本地 Web 服务是否可以访问：

```bash
wget --no-check-certificate -S -O /dev/null https://127.0.0.1:443
```

NanoKVM Go 的 HTTP 端口可能会重定向到 HTTPS。若直接访问 `http://127.0.0.1:80` 后看到 `307 Temporary Redirect`，并跳转到 `https://127.0.0.1/`，属于正常现象。由于设备使用的证书通常不是公网可信证书，使用 `wget` 测试时需要加上 `--no-check-certificate`。

如果连接被拒绝，请先确认 NanoKVM Go Web 服务的实际端口，再修改 `localPort`。

### 测试 frpc 连接

在前台启动 frpc：

```bash
/usr/local/bin/frpc -c /etc/frp/frpc.toml
```

日志中出现 `login to server success` 和 `start proxy success` 等成功信息时，表示 frpc 已连接到 frps，并已注册代理。

保持该终端运行，在外部网络的浏览器中访问：

```text
https://203.0.113.10:8080
```

将示例 IP 替换为公网服务器的实际 IP。首次访问时，浏览器可能提示证书不受信任；确认访问的是自己的服务器后，可以继续访问测试。如果可以打开 NanoKVM Go 登录页面，说明 TCP 转发配置正确。完成测试后，返回 SSH 终端并按 `Ctrl+C` 停止 frpc。

![frpc 成功连接 frps](../../../../assets/NanoKVM/go/network/nanokvm_go_frp_frpc_success_log.webp)


### 设置 frpc 开机自启

NanoKVM Go 使用 systemd 管理系统服务。创建 `/etc/systemd/system/frpc.service`：

```ini
[Unit]
Description=frp client for NanoKVM Go
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/local/bin/frpc -c /etc/frp/frpc.toml
Restart=always
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

加载服务并设置开机自启：

```bash
systemctl daemon-reload
systemctl enable --now frpc
systemctl status frpc
```

查看实时日志：

```bash
journalctl -u frpc -f
```

重启 NanoKVM Go 后，再次执行 `systemctl status frpc`，确认服务可以自动启动并重新连接 frps。


## 从外网访问 NanoKVM Go

为了确认访问流量确实经过公网，请将电脑或手机切换到其他网络，例如手机热点或移动数据网络，然后：

1. 在浏览器中访问 `https://<公网服务器IP>:8080`；
2. 使用 NanoKVM Go 的账号和密码登录；
3. 测试远程画面、键盘、鼠标和电源控制；
4. 刷新页面，确认视频和控制功能仍能正常工作。

TCP 代理会原样转发 HTTPS 和 WebSocket 连接，通常不需要单独配置 WebSocket。如果页面能打开但画面或控制功能异常，请查看浏览器开发者工具、frpc 日志和 frps 日志。

## 配置域名和 HTTPS（可选）

基础示例中的 `https://<公网IP>:8080` 使用的是 NanoKVM Go 自身证书，浏览器可能提示证书不受信任。如果有可用域名，可以将域名解析到 frps 服务器，并使用 Nginx 或 Caddy 提供可信 HTTPS 反向代理。

以 Nginx 为例，可以让 Nginx 监听 `443`，再将请求转发到 frp 暴露在服务器本机的 `8080` 端口：

```nginx
server {
    listen 443 ssl;
    server_name kvm.example.com;

    ssl_certificate /path/to/fullchain.pem;
    ssl_certificate_key /path/to/privkey.pem;

    location / {
        proxy_pass https://127.0.0.1:8080;
        proxy_http_version 1.1;
        proxy_ssl_verify off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 3600s;
    }
}
```

配置步骤概括如下：

1. 将域名的 A 记录指向 frps 服务器公网 IP；
2. 在服务器上安装 Nginx 或 Caddy；
3. 为域名申请 TLS 证书；
4. 将 HTTPS 请求反向代理到 `https://127.0.0.1:8080`；
5. 在安全组和防火墙中放行 `443/tcp`；
6. 确认 `https://kvm.example.com` 可以访问后，关闭公网入站的 `8080/tcp`。

配置 HTTPS 后，应通过云安全组和服务器防火墙拒绝 `8080/tcp` 的公网入站流量，仅允许服务器本机的 Nginx 访问该端口。不要在 HTTPS 配置完成后继续将 HTTP 端口公开在互联网中。


## 常见问题

### frpc 无法连接 frps

依次检查：

- `serverAddr` 和 `serverPort` 是否正确；
- frps 是否为 `active (running)`；
- `7000/tcp` 是否已在云安全组和系统防火墙中放行；
- frps 和 frpc 的 Token 是否完全一致；
- 公网服务器和 NanoKVM Go 的 frp 版本是否兼容；
- NanoKVM Go 是否可以访问互联网和公网服务器。

可以在 NanoKVM Go 上测试端口连通性：

```bash
nc -vz <公网服务器IP> 7000
```

如果系统没有 `nc`，也可以直接观察 frpc 的连接日志。

### frpc 已连接，但公网端口无法访问

检查：

- `remotePort` 是否被其他程序或其他 frp 代理占用；
- `8080/tcp` 是否已在云安全组和系统防火墙中放行；
- frpc 日志中是否显示代理启动成功；
- frps 日志中是否出现 `nanokvm-go-web`；
- 浏览器使用的是 `https://`，而不是 `http://`。

在公网服务器上确认端口是否正在监听：

```bash
sudo ss -lntp | grep ':8080'
```

### 页面无法打开或返回连接拒绝

在 NanoKVM Go 上执行：

```bash
wget --no-check-certificate -S -O /dev/null https://127.0.0.1:443
```

如果本地访问也失败，说明 `localIP` 或 `localPort` 不正确，或者 NanoKVM Go Web 服务没有运行。

### 本地测试提示证书不受信任

如果执行 `wget -S -O /dev/null http://127.0.0.1:80` 后看到 `307 Temporary Redirect`，并跳转到 `https://127.0.0.1/`，说明 NanoKVM Go 会自动使用 HTTPS。随后出现以下证书错误通常是正常的：

```text
ERROR: The certificate of '127.0.0.1' is not trusted.
ERROR: The certificate's owner does not match hostname '127.0.0.1'
```

这是因为 NanoKVM Go 使用的证书不是为 `127.0.0.1` 签发的公网可信证书。测试本机 HTTPS 服务时，使用：

```bash
wget --no-check-certificate -S -O /dev/null https://127.0.0.1:443
```

frpc 配置中也应转发 `localPort = 443`。

### 页面能打开，但视频或控制功能异常

检查：

- 浏览器开发者工具中是否存在 WebSocket 连接错误；
- frpc 和 frps 是否频繁断线或重连；
- Nginx/Caddy 是否正确转发 WebSocket Upgrade 请求；
- HTTPS 页面是否加载了 HTTP 资源；
- 公网服务器带宽和 NanoKVM Go 所在网络的上行带宽是否足够。

### 重启后 frpc 没有自动运行

在 NanoKVM Go 上执行：

```bash
systemctl status frpc
journalctl -u frpc -b
```

检查服务是否已启用、配置文件路径是否正确，以及网络就绪后 frpc 能否连接 frps。

## 停用 frp

### 临时停用

如果只是暂时不使用 frp，并希望以后继续使用，可以停止服务并取消开机自启，同时保留程序和配置文件。

在 NanoKVM Go 上停止并禁用 frpc：

```bash
systemctl disable --now frpc
```

如果公网服务器使用 systemd，停止并禁用 frps：

```bash
sudo systemctl disable --now frps
```

如果公网服务器使用 SysV init，停止 frps 并取消开机自启：

```bash
sudo service frps stop
sudo update-rc.d -f frps remove
```

需要恢复 NanoKVM Go 上的 systemd 服务时，执行：

```bash
systemctl enable --now frpc
```

需要恢复公网服务器上的 systemd 服务时，执行：

```bash
sudo systemctl enable --now frps
```

需要恢复公网服务器上的 SysV init 服务时，执行：

```bash
sudo update-rc.d frps defaults
sudo service frps start
```

> 只执行与当前 init 系统对应的命令。如果公网服务器使用其他服务管理器，请使用对应的停止和禁用命令。

### 彻底卸载

frp 是通过手动复制二进制文件安装的，不受 `apt`、`dnf` 等软件包管理器管理。彻底卸载时，需要手动删除服务、程序和配置文件。

在 NanoKVM Go 上先停止 frpc，并删除 systemd 服务文件：

```bash
systemctl disable --now frpc
rm -f /etc/systemd/system/frpc.service
systemctl daemon-reload
```

然后在 NanoKVM Go 上删除 frpc 程序和配置：

```bash
rm -f /usr/local/bin/frpc
rm -f /etc/frp/frpc.toml
rmdir /etc/frp 2>/dev/null || true
```

删除 NanoKVM Go 中下载和解压产生的临时文件：

```bash
rm -f /root/frp_0.70.0_linux_arm_hf.tar.gz
rm -rf /root/frp_0.70.0_linux_arm_hf
```

如果实际下载的是其他版本或架构，请将文件名替换为实际名称。

如果公网服务器使用 systemd，先删除 frps 服务：

```bash
sudo systemctl disable --now frps
sudo rm -f /etc/systemd/system/frps.service
sudo systemctl daemon-reload
```

如果公网服务器使用 SysV init，先删除 frps 服务：

```bash
sudo service frps stop
sudo update-rc.d -f frps remove
sudo rm -f /etc/init.d/frps
```

完成对应的服务清理后，删除 frps 程序和配置：

```bash
sudo rm -f /usr/local/bin/frps
sudo rm -f /etc/frp/frps.toml
sudo rmdir /etc/frp 2>/dev/null || true
```

公网服务器上的 frp 压缩包和解压目录位于此前执行下载命令的目录中。确认目录和文件名无误后，可以将其删除。

### 清理防火墙和其他配置

如果安装并使用了 UFW，删除本文添加的放行规则：

```bash
sudo ufw delete allow 7000/tcp
sudo ufw delete allow 8080/tcp
```

如果安装并使用了 firewalld，执行：

```bash
sudo firewall-cmd --permanent --remove-port=7000/tcp
sudo firewall-cmd --permanent --remove-port=8080/tcp
sudo firewall-cmd --reload
```

最后还需要检查并清理：

- 云服务器安全组中的 `7000/tcp`、`8080/tcp` 等 frp 端口；
- 专门为 NanoKVM Go 创建的 Nginx 或 Caddy 配置；
- 不再使用的 TLS 证书；
- 不再使用的域名 DNS 记录。

> 如果相应防火墙命令不存在，可以跳过该组命令。如果端口、反向代理或证书还被其他服务使用，请不要直接删除对应配置。

## 安全建议

- 为 NanoKVM Go 设置独立的强密码；
- 使用随机生成的强 Token，不要使用本文示例值；
- 不要对公网开放 frps Dashboard；
- 仅开放实际需要的端口，并尽可能通过防火墙限制来源 IP；
- 有域名时，可以配置可信 HTTPS 反向代理；
- 定期更新 NanoKVM Go、frp 和公网服务器系统；
- 定期检查 frpc、frps 和反向代理日志；
- 不再使用时立即停止服务并关闭公网端口。

## 参考资料

- [frp 官方文档](https://gofrp.org/zh-cn/)
- [frp GitHub 仓库](https://github.com/fatedier/frp)
- [frp Releases](https://github.com/fatedier/frp/releases)
