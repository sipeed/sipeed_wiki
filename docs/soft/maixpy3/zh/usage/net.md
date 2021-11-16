---
title: net
keywords: MaixPy3,net, Python3
desc: maixpy doc: net
---

## 连接网络

python 中包含着一个 socket 的标准库，可以进行搭建一个简易的 web 服务器，代码如下：

> ifconfig 用来查看 ip 地址

```python
import socket

HOST, PORT = '', 8888 # 填上开发板的 ip 地址

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port %s ...' % PORT)
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print(request.decode("utf-8"))

    http_response = """\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response.encode("utf-8"))
    client_connection.close()
```

在电脑的浏览器输入开发板的 ip + 端口号，即可看到打印出来的信息


## 更多的使用方法

请自行的去百度 [python socket](https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=baidu&wd=python%20socket&oq=python%25E6%2590%25AD%25E5%25BB%25BA%25E7%25BD%2591%25E9%25A1%25B5%25E6%259C%258D%25E5%258A%25A1%25E5%2599%25A8&rsv_pq=e64708e3000c8483&rsv_t=f79fUMT%2BuI7wekfW8YPY%2F08rmoG%2BK1vvKzxctjM%2F48hbJ9TyBEHjqePwp3Y&rqlang=cn&rsv_enter=1&rsv_dl=ts_0&rsv_sug3=12&rsv_sug1=12&rsv_sug7=100&rsv_sug2=0&rsv_btype=t&prefixsug=python%2520soc&rsp=0&inputT=3909&rsv_sug4=4389c) 的教程，自行学习