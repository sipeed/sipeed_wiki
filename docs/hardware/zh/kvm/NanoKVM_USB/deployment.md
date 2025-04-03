---
title: 本地部署
keywords: NanoKVM, Remote desktop, tool, USB
update:
  - date: 2025-01-15
    version: v0.1
    author: xwj
    content:
      - Release docs
---


首先，在 [Releases](https://cdn.sipeed.com/nanokvm/NanoKVM-USB.zip) 页面下载 `browser` 版本文件，解压后会得到`NanoKVM-USB`文件夹。

## 本机部署

> 如果只需要通过本机访问（localhost），则可以不使用证书。

这里提供了 Node.js 和 Python 的示例。

### Node.js 服务

1. 打开终端，进入上一步骤中的 `NanoKVM-USB` 目录；
2. 执行 `npm install -g http-server` 安装 `http-server`；
3. 执行 `http-server -p 8080 -a localhost` 启动服务。

### Python 服务

1. 打开终端，进入上一步骤中的 `NanoKVM-USB` 目录；
2. 执行 `python -m http.server 8080` 启动服务。

### 在网页中访问

服务启动后，打开浏览器访问 `http://localhost:8080` 即可。

注意只能使用`http`协议，无法使用`https`协议。

## 局域网部署

> 如果需要在局域网内访问，则需要使用证书。

这里提供了 Node.js 和 Python 的示例。相较于本地部署，多了一个生成证书的步骤。

### 生成证书

> 请确保已经安装 `openssl`。

1. 打开终端，进入上一步骤中的 `NanoKVM-USB` 目录；
2. 执行 `openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem`；
3. 终端会提示需要输入信息，可以一直按回车键跳过，也可以按自己的需要输入信息。

完成后会在当前目录生成两个文件：`key.pem` 和 `cert.pem`。

### Node.js 服务

1. 执行 `npm install -g http-server` 安装 `http-server`;
2. 执行 `http-server -p 8080 -S -C cert.pem -K key.pem` 启动服务。

### Python 服务

在 `NanoKVM-USB` 目录中创建 `server.py` 文件，写入以下代码并保存：

```python
import http.server
import ssl

server_address = ('0.0.0.0', 8080)

httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"Serving HTTPS on {server_address[0]}:{server_address[1]}")

httpd.serve_forever()
```

执行 `python server.py` 运行服务。

### 在网页中访问

打开浏览器，输入服务地址，比如`https://127.0.0.1:8080`。

如果打开网址后提示`隐私错误`，需要手动点击访问：

![](./../../../assets/NanoKVM/usb/privacy-error.png)

## 公网部署

> 如果需要在公网访问，建议使用 `Nginx`。

这里给出一份简单的配置示例，详细的配置方式请参考 `Nginx` 文档。

```nginx
server {
    listen 80;
    server_name your_domain.com www.your_domain.com; # 请替换为您的域名
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name your_domain.com www.your_domain.com; # 请替换为您的域名

    root /var/www/your_website; # 请替换为 NanoKVM-USB 目录路径
    index index.html index.htm;

    ssl_certificate /etc/nginx/ssl/your_domain.crt; # 请替换为您的证书文件路径
    ssl_certificate_key /etc/nginx/ssl/your_domain.key; # 请替换为您的私钥文件路径

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```
