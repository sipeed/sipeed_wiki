---
title: Development
keywords: NanoKVM, Remote desktop, tool, USB
update:
  - date: 2025-01-15
    version: v0.1
    author: xwj
    content:
      - Release docs
---

Visit the [Releases page](https://github.com/sipeed/NanoKVM-USB/releases) to download the `browser` version file. Then unzip it and you'll get a folder named `NanoKVM-USB`.

## Local deployment

> If only access through the local machine (localhost), certificates can be omitted.

Examples are provided here for Node.js and Python.

### Node.js Service

1. Open the terminal and enter the `NanoKVM-USB` directory in the previous step.
2. Execute `npm install -g http-server` to install `http-server`.
3. Execute `http-server -p 8080 -a localhost` to run the service.

### Python Service

1. Open the terminal and enter the `NanoKVM-USB` directory in the previous step.
2. Execute `python -m http.server 8080` to run the service.

### Visit on browser

After the service is started, open the browser and visit `http://localhost:8080`.

Note that you can only use the `http` protocol, not the `https` protocol.

## Local network deployment

> If access is needed within the local area network, a certificate is required.

Examples are provided here for Node.js and Python. The difference from the above is that a certificate is required.

### Generate Certificate

> Make sure you have `openssl` installed.

1. Open the terminal and enter the `NanoKVM-USB` directory in the previous step.
2. Execute `openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem`.
3. The terminal ask you to enter information. You can pressing the Enter key to skip it, or you can enter information as needed.

After completion, two files `key.pem` and `cert.pem` will be generated in the current directory.

### Node.js Service

1. Execute `npm install -g http-server` to install `http-server`.
2. Execute `http-server -p 8080 -S -C cert.pem -K key.pem` to run the service.

### Python Service

Create a file `server.py` in the `NanoKVM-USB` directory, and save it with the following code:

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

Execute `python server.py` to run the service。

### Visit on browser

Open the browser and enter the service address, such as `https://127.0.0.1:8080`.

After opening the URL, you may be prompted with a "Privacy Error" and need to click to access manually:

![](./../../../assets/NanoKVM/usb/privacy-error.png)

## Public network deployment

> If you need to access it on the public network, it is recommended to use `Nginx`.

Here is a simple configuration example. For detailed configuration methods, please refer to the `Nginx` documentation.

```nginx
server {
    listen 80;
    server_name your_domain.com www.your_domain.com; # Please replace with your domain name
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name your_domain.com www.your_domain.com; # Please replace with your domain name

    root /var/www/your_website; # Please replace with the NanoKVM-USB directory path
    index index.html index.htm;

    ssl_certificate /etc/nginx/ssl/cert.pem; # Please replace it with your certificate file path
    ssl_certificate_key /etc/nginx/ssl/key.pem; # Please replace it with your private key file path

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```
