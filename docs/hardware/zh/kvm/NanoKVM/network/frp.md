---
title: frp
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2024-8-13
    version: v0.1
    author: xwj
    content:
      - Release docs
---

> 注意，直接在公网暴露服务十分危险！建议配置 HTTPS 后使用。

想要使用 frp，你需要自己编写配置文件，可以参考 [frp 文档](https://gofrp.org)。

这里给出一个示例，实现通过 frp [访问内网的 web 服务](https://gofrp.org/zh-cn/docs/examples/vhost-http/)

## 启动 frps 服务

首先你需要一台带有公网 IP 的服务器，然后在该服务上启动 frps 服务。
这里我们假设该服务器 IP 地址为 `20.190.1.1`。你可以将这个 IP 替换为你自己的公网 IP。

1. 下载 [frp](https://github.com/fatedier/frp/releases/download/v0.59.0/frp_0.59.0_linux_riscv64.tar.gzf) 并解压，解压完成后进入该文件夹：

    ```bash
    wget https://github.com/fatedier/frp/releases/download/v0.59.0/frp_0.59.0_linux_riscv64.tar.gz
    tar -xzvf frp_0.59.0_linux_amd64.tar.gz
    cd frp_0.59.0_linux_amd64
    ```

1. 创建配置文件 `frps.yaml`：

    ```yaml
    bindPort: 7000
    vhostHTTPPort: 8080
    ```

1. 运行 frps 服务：

    ```bash
    ./frps -c frps.yaml
    ```

## 启动 frpc 服务

1. 通过 SSH 登录到 NanoKVM；
1. 执行 `frpc -v` 查看版本号，如果没有输出，则需要手动安装 frpc；
    - 下载 [frp](https://github.com/fatedier/frp/releases/download/v0.59.0/frp_0.59.0_linux_riscv64.tar.gzf) 并解压；
    - 将 `frpc` 文件移动到 `/usr/bin/` 目录

1. 创建配置文件 `/etc/kvm/frpc.yaml` ：

    ```yaml
    serverAddr: 20.190.1.1 # 你的公网 IP
    serverPort: 7000
    proxies:
    - name: nanokvm
        type: http
        localPort: 80
        customDomains:
        - 20.190.1.1
    ```

1. 启动 frpc 服务：

    ```bash
    frpc -c /etc/kvm/frpc.yaml
    ```

frps 和 frpc 服务都启动后，在浏览器中输入 `20.190.1.1:8080`，就可以在公网中访问到 NanoKVM 了。

## 配置域名

如果你想给 NanoKVM 配置一个域名，可以修改 `frpc.yaml` 文件：

```yaml
serverAddr: 20.190.1.1 # 你的公网 IP
serverPort: 7000
proxies:
  - name: nanokvm
    type: http
    localPort: 80
    customDomains:
      - www.yourdomain.com # 你的域名
```

然后将域名 [`www.yourdomain.com`](http://www.yourdomain.com) 解析到 `20.190.1.1`。

使用浏览器打开 [`http://www.yourdomain.com:8080`](http://www.yourdomain.com:8080/) 即可访问到 `NanoKVM`。

## 配置 HTTPS

可参考 frp 文档：[为本地 HTTP 服务启用 HTTPS](https://gofrp.org/zh-cn/docs/examples/https2http/)。

1. 配置 `frps.yaml` 文件：

    ```yaml
    bindPort: 7000
    vhostHTTPSPort: 443
    ```

1. 配置 `frpc.yaml` 文件

    ```yaml
    serverAddr: 20.190.1.1           # 你的公网 IP
    serverPort: 7000
    proxies:
    - name: nanokvm
        type: https
        customDomains:
        - yourdomain.com             # 你的域名
        plugin:
        type: https2http
        localAddr: 127.0.0.1:80
        crtPath: ./server.crt        # 证书路径
        keyPath: ./server.key        # 私钥路径
        hostHeaderRewrite: 127.0.0.1
        requestHeaders:
            set:
            x-from-where: frp
    ```

1. 分别启动 frps 和 frpc 服务，然后在浏览器中访问 [`https://yourdomain.com`](https://yourdomain.com) 即可
