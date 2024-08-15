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

> Note: Exposing services directly to the public internet is very dangerous! It is recommended to use HTTPS.

To use frp, you need to create your own configuration file. You can refer to the [frp documentation](https://gofrp.org).

Here is an example to access an [internal web service via frp](https://gofrp.org/zh-cn/docs/examples/vhost-http/).

## Start the frps Service

First, you need a server with a public IP address and start the frps service on it. Let's assume the server IP address is `20.190.1.1`. Replace this IP with your own public IP.

1. Download and extract [frp](https://github.com/fatedier/frp/releases/download/v0.59.0/frp_0.59.0_linux_riscv64.tar.gzf). After extracting, go to the folder:

    ```bash
    wget https://github.com/fatedier/frp/releases/download/v0.59.0/frp_0.59.0_linux_riscv64.tar.gz
    tar -xzvf frp_0.59.0_linux_riscv64.tar.gz
    cd frp_0.59.0_linux_riscv64
    ```

1. Create the configuration file `frps.yaml`:

    ```yaml
    bindPort: 7000
    vhostHTTPPort: 8080
    ```

1. Start the frps service:

    ```bash
    ./frps -c frps.yaml
    ```

## Start the frpc Service

1. SSH into the NanoKVM;
1. Run `frpc -v` to check the version. If there is no output, install frpc manually;
    - Download and extract [frp](https://github.com/fatedier/frp/releases/download/v0.59.0/frp_0.59.0_linux_riscv64.tar.gzf);
    - Move the `frpc` file to the `/usr/bin/` directory.

1. Create the configuration file `/etc/kvm/frpc.yaml`:

    ```yaml
    serverAddr: 20.190.1.1 # Your public IP
    serverPort: 7000
    proxies:
      - name: nanokvm
        type: http
        localPort: 80
        customDomains:
          - 20.190.1.1
    ```

1. Start the frpc service:

    ```bash
    frpc -c /etc/kvm/frpc.yaml
    ```

After both frps and frpc services are started, you can access the NanoKVM via the public internet by entering `20.190.1.1:8080` in your browser.

## Configure Domain

To configure a domain for NanoKVM, modify the `frpc.yaml` file:

```yaml
serverAddr: 20.190.1.1 # Your public IP
serverPort: 7000
proxies:
  - name: nanokvm
    type: http
    localPort: 80
    customDomains:
      - www.yourdomain.com # Your domain
```

Then point the domain [`www.yourdomain.com`](http://www.yourdomain.com) to `20.190.1.1`.

You can now access NanoKVM by opening [`http://www.yourdomain.com:8080`](http://www.yourdomain.com:8080/) in your browser.

## Configure HTTPS

Refer to the frp documentation: [Enable HTTPS for local HTTP services](https://gofrp.org/zh-cn/docs/examples/https2http/).

1. Configure the `frps.yaml` file:

    ```yaml
    bindPort: 7000
    vhostHTTPSPort: 443
    ```

1. Configure the `frpc.yaml` file:

    ```yaml
    serverAddr: 20.190.1.1           # Your public IP
    serverPort: 7000
    proxies:
      - name: nanokvm
        type: https
        customDomains:
          - yourdomain.com             # Your domain
        plugin:
          type: https2http
          localAddr: 127.0.0.1:80
          crtPath: ./server.crt        # Certificate path
          keyPath: ./server.key        # Private key path
          hostHeaderRewrite: 127.0.0.1
          requestHeaders:
            set:
              x-from-where: frp
    ```

1. Start both frps and frpc services, then access [`https://yourdomain.com`](https://yourdomain.com) in your browser.