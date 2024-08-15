---
title: Configuration File
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2024-8-13
    version: v0.1
    author: xwj
    content:
      - Release docs
---

The configuration file is located at `/etc/kvm/server.yaml`.

The default configuration file content:

```yaml
protocol: http
port:
  http: 80
  https: 443
cert:
  crt: server.crt
  key: server.key
```

- **protocol**: Network protocol, either `http` or `https`
- **port**: The port on which the service runs
  - When the protocol is `http`, the service will use the `port.http` port
  - When the protocol is `https`, the service will use the `port.https` port
  - When the protocol is `https`, you need to prefix the address with `https://` in the browser (e.g., `https://192.168.1.210`)
  - If you change the port, please include the port in the browser address. For example, if you change `port.http` to 8080, the browser address will be `192.168.1.210:8080`
  - Do not set the port to 0. If the service detects the port is 0, it will override the current configuration file with the default settings
- **cert**: Service certificate. This parameter must be configured if the protocol is set to `https`
  - **crt**: Path to the certificate file
  - **key**: Path to the private key file

Note: Enabling `https` increases CPU usage, which may cause video stuttering.