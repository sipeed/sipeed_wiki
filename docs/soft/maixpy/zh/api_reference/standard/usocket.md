---
title: usocket – 套接字模块
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: usocket – 套接字模块
---


该模块实现了相应CPython模块的子集，如下所述。有关更多信息，请参阅原始CPython文档: [socket](https://docs.python.org/3.5/library/socket.html#module-socket).

该模块提供对BSD套接字接口的访问

> **与CPython的区别** 

> 为了提高效率和一致性，MicroPython中的套接字对象直接实现了`stream`（类文件）接口。在CPython中，您需要使用`makefile（）`方法将套接字转换为类文件对象。 MicroPython仍支持此方法（但是无操作），因此在与CPython兼容的情况下，请务必使用它。

## 套接字地址格式

`usocket`模块的本机套接字地址格式是getaddrinfo函数返回的不透明数据类型，必须用它来解析文本地址（包括数字地址）：

```python
sockaddr = usocket.getaddrinfo('www.micropython.org', 80)[0][-1]
# You must use getaddrinfo() even for numeric addresses
sockaddr = usocket.getaddrinfo('127.0.0.1', 80)[0][-1]
# Now you can use that address
sock.connect(addr)
```

使用`getaddrinfo`是最有效的（在内存和处理能力方面），而且也是使用地址的可移植方式。

但是，`socket`模块（注意与此处描述的本机MicroPython`usocket`模块的区别）提供了与CPython兼容的方式来使用元组指定地址，如下所述。请注意，取决于`MicroPython端口`，可以在内置或需要从`micropython-lib`安装套接字模块（如“MicroPython Unix端口”的情况），并且某些端口仍然只接受元组中的数字地址格式，并要求使用`getaddrinfo`函数来解析域名。

总的来说：

* 编写便携式应用程序时始终使用`getaddrinfo`。
* 如果您的端口支持快速黑客和交互式使用，则下面描述的元组地址可用作快捷方式。

`socket`模块的元组地址格式：

* IPv4：（ipv4_address，port），其中ipv4_address是带有点符号数字IPv4地址的字符串，例如， “8.8.8.8”，端口号和整数端口号在1-65535范围内。请注意，域名不被接受为ipv4_address，应首先使用usocket.getaddrinfo（）解析它们。

* IPv6：（ipv6_address，port，flowinfo，scopeid），其中ipv6_address是带冒号数字IPv6地址的字符串，例如： `“2001：db8 :: 1”`，port是1-65535范围内的整数端口号。 flowinfo必须为0. scopeid是链路本地地址的接口范围标识符。请注意，域名不被接受为ipv6_address，应首先使用`usocket.getaddrinfo（）`解析它们。 IPv6支持的可用性取决于`MicroPython端口`。

## 方法

### usocket.socket(af=AF_INET, type=SOCK_STREAM, proto=IPPROTO_TCP)

使用给定的地址系列，套接字类型和协议号创建一个新套接字。请注意，在大多数情况下不需要指定proto（不推荐使用，因为一些MicroPython端口可能会省略`IPPROTO_ *`常量）。相反，type参数将自动选择所需的协议：

```python
# Create STREAM TCP socket
socket(AF_INET, SOCK_STREAM)
# Create DGRAM UDP socket
socket(AF_INET, SOCK_DGRAM)
```

### usocket.getaddrinfo(host, port, af=0, type=0, proto=0, flags=0)

将 host / port 参数转换为5元组序列，其中包含用于创建连接到该服务的套接字的所有必要参数。参数af，type和proto（与`socket（）`函数具有相同的含义）可用于过滤返回哪种地址。如果未指定参数或为零，则可以返回所有地址组合（需要在用户端进行过滤）。

生成的5元组列表具有以下结构：

```python
(family, type, proto, canonname, sockaddr)
```

以下示例显示如何连接到给定的URL：

```python
s = usocket.socket()
# This assumes that if "type" is not specified, an address for
# SOCK_STREAM will be returned, which may be not true
s.connect(usocket.getaddrinfo('www.micropython.org', 80)[0][-1])
```


建议使用过滤参数：

```python
s = usocket.socket()
# Guaranteed to return an address which can be connect'ed to for
# stream operation.
s.connect(usocket.getaddrinfo('www.micropython.org', 80, 0, SOCK_STREAM)[0][-1])
```

> 与CPython的区别

> 如果此函数出错，CPython会引发`socket.gaierror`异常（`OSError`子类）。 MicroPython没有`socket.gaierror`并直接引发OSError。请注意，`getaddrinfo（）`的错误号形成一个单独的命名空间，可能与`uerrno`模块中的错误号不匹配。为了区分`getaddrinfo（）`错误，它们用负数表示，而标准系统错误是正数（错误号可以使用来自异常对象的`e.args [0]`属性访问）。使用负值是临时细节，可能在将来发生变化。

### usocket.inet_ntop(af, bin_addr)

将给定地址族af的二进制网络地址bin_addr转换为文本表示：


```python
>>> usocket.inet_ntop(usocket.AF_INET, b"\x7f\0\0\1")
'127.0.0.1'
```


### usocket.inet_pton(af, txt_addr)

将给定地址族af的文本网络地址txt_addr转换为二进制表示：

```python
>>> usocket.inet_pton(usocket.AF_INET, "1.2.3.4")
b'\x01\x02\x03\x04'
```


## 常量

### usocket.AF_INET usocket.AF_INET6

解决家庭类型。可用性取决于特定的`MicroPython端口`。

### usocket.SOCK_STREAM usocket.SOCK_DGRAM

套接字类型。

### usocket.IPPROTO_UDP usocket.IPPROTO_TCP

IP协议号。可用性取决于特定的`MicroPython端口`。注意，在调用`usocket.socket（）`时不需要指定它们，因为`SOCK_STREAM`套接字类型会自动选择`IPPROTO_TCP`和`SOCK_DGRAM`  - `IPPROTO_UDP`。因此，这些常量的唯一实际用途是作为`setsockopt（）`的参数。

### usocket.SOL_*

套接字选项级别（`setsockopt（）`的参数）。确切的库存取决于`MicroPython端口`。

### usocket.SO_*

套接字选项（`setsockopt（）`的参数）。确切的库存取决于`MicroPython端口`。


## 类 socket

### 方法

#### socket.close()

标记套接字已关闭并释放所有资源。一旦发生这种情况，套接字对象上的所有未来操作都将失败。如果协议支持，远程端将接收EOF指示。

套接字在被垃圾收集时会自动关闭，但建议你在完成它们之后立即“关闭”它们。

#### (maixpy 未实现)socket.bind(address)

将套接字绑定到地址。套接字必须尚未绑定。

#### (maixpy 未实现)socket.listen([backlog])

使服务器接受连接。如果指定了积压，则必须至少为0（如果低，则将其设置为0）;并指定在拒绝新连接之前系统将允许的未接受连接数。如果未指定，则选择默认的合理值。

#### (maixpy 未实现)socket.accept()

接受连接。套接字必须绑定到一个地址并侦听连接。返回值是一对（conn，address），其中conn是可用于在连接上发送和接收数据的新套接字对象，address是绑定到连接另一端的套接字的地址。

#### socket.connect(address)

连接到地址处的远程套接字。

#### socket.send(bytes)

将数据发送到套接字。套接字必须连接到远程套接字。返回发送的字节数，可能小于数据长度（“短写”）。

#### socket.sendall(bytes)

将所有数据发送到套接字。套接字必须连接到远程套接字。与`send（）`不同，此方法将尝试通过连续发送数据块来发送所有数据。

此方法在非阻塞套接字上的行为未定义。因此，在MicroPython上，建议使用`write（）`方法，它具有相同的“无短写入”策略来阻塞套接字，并将返回在非阻塞套接字上发送的字节数。

#### socket.recv(bufsize)

从套接字接收数据。返回值是表示接收数据的字节对象。一次接收的最大数据量由bufsize指定。

#### socket.sendto(bytes, address)

将数据发送到套接字。套接字不应连接到远程套接字，因为目标套接字由地址指定。

#### socket.recvfrom(bufsize)

从套接字接收数据。返回值是一对（字节，地址），其中bytes是表示接收数据的字节对象，address是发送数据的套接字的地址。

#### socket.setsockopt(level, optname, value)

设置给定套接字选项的值。所需的符号常量在套接字模块中定义（SO_ *等）。该值可以是整数或表示缓冲区的类字节对象。


#### socket.settimeout(value)

注意：并非每个端口都支持此方法，请参阅下文。

阻止套接字操作设置超时。 value参数可以是表示秒的非负浮点数，也可以是None。如果给出非零值，则如果在操作完成之前已经过了超时时间值，则后续的套接字操作将引发“OSError”异常。如果给出零，则套接字处于非阻塞模式。如果给出None，则套接字处于阻塞模式。

并非每个“MicroPython端口”都支持此方法。更便携和通用的解决方案是使用`uselect.poll`对象。这允许同时等待多个对象（而不仅仅是在套接字上，而是在支持轮询的通用`stream`对象上）。例：

```python
# Instead of:
s.settimeout(1.0)  # time in seconds
s.read(10)  # may timeout

# Use:
poller = uselect.poll()
poller.register(s, uselect.POLLIN)
res = poller.poll(1000)  # time in milliseconds
if not res:
    # s is still not ready for input, i.e. operation timed out
```

> 与CPython的区别

> CPython在超时的情况下引发`socket.timeout`异常，这是一个OSError子类。 MicroPython直接引发了一个`OSError`。如果你使用`除了OSError`：来捕获异常，你的代码将在MicroPython和CPython中都有效。

#### socket.setblocking(flag)

设置套接字的阻塞或非阻塞模式：如果flag为false，则套接字设置为非阻塞，否则设置为阻塞模式。

这个方法是某些`settimeout（）`调用的简写：

`sock.setblocking(True)` 相当于`sock.settimeout(None)`
`sock.setblocking(False)` i相当于 `sock.settimeout(0)`

#### socket.makefile(mode='rb', buffering=0)

返回与套接字关联的文件对象。确切的返回类型取决于给makefile（）的参数。支持仅限于二进制模式（'rb'，'wb'和'rwb'）。 CPython的参数：不支持编码，错误和换行符。

> 与CPython的区别

> 由于MicroPython不支持缓冲流，因此忽略缓冲参数的值，并将其视为0（无缓冲）。

> 与CPython的区别

> 关闭makefile（）返回的文件对象也将关闭原始套接字。

#### socket.read([size])

从插槽中读取大小字节。返回一个字节对象。如果没有给出大小，它会读取插座中可用的所有数据，直到EOF;因此，在套接字关闭之前，该方法不会返回。此函数尝试读取所请求的数据（没有“短读取”）。但是，对于非阻塞套接字，这可能是不可能的，然后将返回更少的数据。

#### socket.readinto(buf[, nbytes])

将字节读入buf。如果指定了nbytes，则最多读取多个字节。否则，最多读取len（buf）字节。就像read（）一样，此方法遵循“无短读”策略。

返回值：读取并存储到buf中的字节数。

#### socket.readline()

读一行，以换行符结尾。

返回值：读取的行。


#### socket.write(buf)

将字节缓冲区写入套接字。此函数将尝试将所有数据写入套接字（无“短写”）。但是，对于非阻塞套接字，这可能是不可能的，并且返回值将小于buf的长度。

返回值：写入的字节数。

#### exception usocket.error

MicroPython没有此异常。

> 与CPython的区别

> CPython曾经有一个`socket.error`异常现在已被弃用，它是`OSError`的别名。在MicroPython中，直接使用`OSError`。




## 例程

### 例程 1： 下载图片并显示

> 注意需要设置 WiFi SSID 和 密码

```python
import socket
import network
import gc
import os
import lcd, image

fm.register(board_info.WIFI_RX,fm.fpioa.UART2_TX)
fm.register(board_info.WIFI_TX,fm.fpioa.UART2_RX)
uart = machine.UART(machine.UART.UART2,115200,timeout=1000, read_buf_len=4096)
nic=network.ESP8285(uart)
nic.connect("Sipeed_2.4G","------")

sock = socket.socket()
addr = socket.getaddrinfo("dl.sipeed.com", 80)[0][-1]
sock.connect(addr)
sock.send('''GET /MAIX/MaixPy/assets/Alice.bmp HTTP/1.1
Host: dl.sipeed.com
cache-control: no-cache

''')

img = b""
sock.settimeout(5)
while True:
    data = sock.recv(4096)
    if len(data) == 0:
        break
    print("rcv:", len(data))
    img = img + data

print(len(img))
img = img[img.find(b"\r\n\r\n")+4:]
print(len(img))
print("save to /sd/Alice.bmp")
f = open("/sd/Alice.bmp","wb")
f.write(img)
f.close()
print("save ok")
print("display")
img = image.Image("/sd/Alice.bmp")
lcd.init()
lcd.display(img)
```



### 例程 2： 发送图片

```python

import os
import socket
import network
import gc

fm.register(board_info.WIFI_RX,fm.fpioa.UART2_TX)
fm.register(board_info.WIFI_TX,fm.fpioa.UART2_RX)
uart = machine.UART(machine.UART.UART2,115200,timeout=1000, read_buf_len=4096)
nic=network.ESP8285(uart)
nic.connect("Sipeed_2.4G","-------")

addr = ("192.168.0.183", 3456)
sock = socket.socket()
sock.connect(addr)
sock.settimeout(5)

f = open("/sd/Alice.bmp","rb")
while True:
    img = f.read(2048)
    if not img or (len(img) == 0):
        break
    sock.send(img)
f.close()
sock.close()
```

