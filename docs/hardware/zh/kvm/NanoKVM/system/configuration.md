---
title: 配置文件
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2024-8-13
    version: v0.1
    author: xwj
    content:
      - Release docs
---


配置文件的路径为 `/etc/kvm/server.yaml`。

默认的配置文件内容：

```yaml
protocol: http
port:
  http: 80
  https: 443
cert:
  crt: server.crt
  key: server.key
```

- protocol：网络协议，`http` 或 `https`
- port：服务运行的端口
  - 当 protocol 为 http 时，服务会使用 port.http 端口
  - 当 protocol 为 https 时，服务会使用 port.https 端口
  - 当 protocol 为 https 时，在浏览器中访问时需要加上 `https://` 前缀 (例如：`https://192.168.1.210`）
  - 如果你修改了端口，在浏览器中访问时请加上该端口。例如修改 port.http 为 8080，则在浏览器中的访问地址为 `192.168.1.210:8080`
  - 请勿将端口设置为 0。服务检测到端口为 0 时，会使用默认配置覆盖当前配置文件
- cert：服务证书。如果 protocol 设置为 https，则需要配置该参数
  - crt：证书文件的路径
  - key：私钥文件的路径

注意，开启 https 后会增加 cpu 占用，可能会导致画面卡顿。
