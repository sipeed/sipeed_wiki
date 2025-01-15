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

## Download

Click to download the [Web Files](https://cdn.sipeed.com/nanokvm/NanoKVM-USB.zip) and unzip it. You'll get a folder named `NanoKVM-USB`.

## Generate Certificate

> Make sure you have `openssl` installed.

1. Open the terminal and enter the `NanoKVM-USB` directory in the previous step.
2. Execute `openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem`.
3. The terminal ask you to enter information. You can pressing the Enter key to skip it, or you can enter information as needed.

After completion, two files `key.pem` and `cert.pem` will be generated in the current directory.

## Run Service

Examples are provided here for Node.js and Python.

### Node.js Service

1. Execute `npm install -g http-server` to install `http-server`.
2. Execute `http-server -S -C cert.pem -K key.pem` to run the service.
3. The address of the service can be found from the output log:

```shell
Starting up http-server, serving ./ through https

http-server version: 14.1.1

http-server settings:
CORS: disabled
Cache: 3600 seconds
Connection Timeout: 120 seconds
Directory Listings: visible
AutoIndex: visible
Serve GZIP Files: false
Serve Brotli Files: false
Default File Extension: none

Available on:
  https://127.0.0.1:8080
  https://192.168.3.250:8080
  https://198.18.0.1:8080
Hit CTRL-C to stop the server
```

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

## Visit on browser

Open the browser and enter the address obtained in the previous step. Here we take `https://127.0.0.1:8080` as an example.

After opening the URL, you may be prompted with a "Privacy Error" and need to click to access manually:

![](./../../../assets/NanoKVM/usb/privacy-error.png)
