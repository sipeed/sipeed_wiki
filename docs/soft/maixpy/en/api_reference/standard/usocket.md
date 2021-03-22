---
title: usocket – socket module
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: usocket-socket module
---


This module implements a subset of the corresponding CPython module, as described below. For more information, please refer to the original CPython documentation: [socket](https://docs.python.org/3.5/library/socket.html#module-socket).

This module provides access to the BSD socket interface

> **Difference from CPython**

> In order to improve efficiency and consistency, the socket object in MicroPython directly implements the `stream` (class file) interface. In CPython, you need to use the `makefile()` method to convert the socket into a file-like object. MicroPython still supports this method (but no operation), so if it is compatible with CPython, be sure to use it.

## Socket address format

The native socket address format of the `usocket` module is the opaque data type returned by the getaddrinfo function, which must be used to parse text addresses (including numeric addresses):

```python
sockaddr = usocket.getaddrinfo('www.micropython.org', 80)[0][-1]
# You must use getaddrinfo() even for numeric addresses
sockaddr = usocket.getaddrinfo('127.0.0.1', 80)[0][-1]
# Now you can use that address
sock.connect(addr)
```

Using `getaddrinfo` is the most effective (in terms of memory and processing power), and it is also a portable way to use addresses.

However, the `socket` module (note the difference from the native MicroPython `usocket` module described here) provides a CPython-compatible way to specify addresses using tuples, as described below. Please note that depending on the `MicroPython port`, the socket module can be built in or needs to be installed from `micropython-lib` (as in the case of "MicroPython Unix port"), and some ports still only accept numeric addresses in tuples Format and requires the use of the `getaddrinfo` function to resolve the domain name.

In general:

* Always use `getaddrinfo` when writing portable applications.
* If your port supports fast hacking and interactive use, the tuple address described below can be used as a shortcut.

The tuple address format of the `socket` module:

* IPv4: (ipv4_address, port), where ipv4_address is a string with a dotted number IPv4 address, for example, "8.8.8.8", the port number and integer port number are in the range of 1-65535. Please note that domain names are not accepted as ipv4_address, they should be resolved first using usocket.getaddrinfo().

* IPv6: (ipv6_address, port, flowinfo, scopeid), where ipv6_address is a string with a colon number IPv6 address, for example: `"2001:db8::1"`, port is an integer port number in the range of 1-65535. flowinfo must be 0. scopeid is the interface scope identifier of the link local address. Please note that domain names are not accepted as ipv6_address, they should be resolved using `usocket.getaddrinfo()` first. The availability of IPv6 support depends on the `MicroPython port`.

## Method

### usocket.socket(af=AF_INET, type=SOCK_STREAM, proto=IPPROTO_TCP)

Create a new socket using the given address series, socket type and protocol number. Please note that in most cases there is no need to specify proto (not recommended because some MicroPython ports may omit the `IPPROTO_ *` constants). Instead, the type parameter will automatically select the required protocol:

```python
# Create STREAM TCP socket
socket(AF_INET, SOCK_STREAM)
# Create DGRAM UDP socket
socket(AF_INET, SOCK_DGRAM)
```

### usocket.getaddrinfo(host, port, af=0, type=0, proto=0, flags=0)

Convert the host / port parameter to a 5-tuple sequence, which contains all the necessary parameters for creating a socket to connect to the service. The parameters af, type and proto (which have the same meaning as the `socket()` function) can be used to filter which address is returned. If the parameter is not specified or is zero, all address combinations can be returned (requires filtering on the user side).

The resulting 5-tuple list has the following structure:

```python
(family, type, proto, canonname, sockaddr)
```

The following example shows how to connect to a given URL:

```python
s = usocket.socket()
# This assumes that if "type" is not specified, an address for
# SOCK_STREAM will be returned, which may be not true
s.connect(usocket.getaddrinfo('www.micropython.org', 80)[0][-1])
```


It is recommended to use filter parameters:

```python
s = usocket.socket()
# Guaranteed to return an address which can be connect'ed to for
# stream operation.
s.connect(usocket.getaddrinfo('www.micropython.org', 80, 0, SOCK_STREAM)[0][-1])
```

> Difference with CPython

> If this function fails, CPython will raise a `socket.gaierror` exception (subclass of `OSError`). MicroPython does not have `socket.gaierror` and directly raises OSError. Please note that the error number of `getaddrinfo()` forms a separate namespace and may not match the error number in the `uerrno` module. In order to distinguish `getaddrinfo()` errors, they are represented by negative numbers, while standard system errors are positive numbers (the error number can be accessed using the `e.args[0]` attribute from the exception object). The use of negative values ​​is a temporary detail and may change in the future.

### usocket.inet_ntop(af, bin_addr)

Convert the binary network address bin_addr of a given address family af into a text representation:


```python
>>> usocket.inet_ntop(usocket.AF_INET, b"\x7f\0\0\1")
'127.0.0.1'
```


### usocket.inet_pton(af, txt_addr)

Convert the text network address txt_addr of a given address family af into binary representation:

```python
>>> usocket.inet_pton(usocket.AF_INET, "1.2.3.4")
b'\x01\x02\x03\x04'
```


## Constant

### usocket.AF_INET usocket.AF_INET6

Address family types. Availability depends on the specific `MicroPython port`.

### usocket.SOCK_STREAM usocket.SOCK_DGRAM

The socket type.

### usocket.IPPROTO_UDP usocket.IPPROTO_TCP

IP protocol number. Availability depends on the specific `MicroPython port`. Note that you do not need to specify them when calling `usocket.socket()`, because `SOCK_STREAM` socket type will automatically select `IPPROTO_TCP` and `SOCK_DGRAM`-`IPPROTO_UDP`. Therefore, the only practical use of these constants is as a parameter to `setsockopt()`.

### usocket.SOL_*

Socket option level (parameter of `setsockopt()`). The exact inventory depends on the `MicroPython port`.

### usocket.SO_*

Socket options (parameters of `setsockopt()`). The exact inventory depends on the `MicroPython port`.


## Class socket

### Method

#### socket.close()

Mark that the socket is closed and release all resources. Once this happens, all future operations on the socket object will fail. If the protocol supports it, the remote end will receive the EOF indication.

Sockets are automatically closed when they are garbage collected, but it is recommended that you "close" them immediately after finishing them.

#### (maixpy ​​not implemented) socket.bind(address)

Bind the socket to the address. The socket must not be bound.

#### (maixpy ​​not implemented) socket.listen([backlog])

Make the server accept connections. If backlog is specified, it must be at least 0 (if low, set it to 0); and specify the number of unaccepted connections that the system will allow before rejecting new connections. If not specified, the default reasonable value is selected.

#### (maixpy ​​not implemented) socket.accept()

Accept the connection. The socket must be bound to an address and listen for connections. The return value is a pair (conn, address), where conn is a new socket object that can be used to send and receive data on the connection, and address is the address of the socket bound to the other end of the connection.

#### socket.connect(address)

Connect to the remote socket at the address.

#### socket.send(bytes)

Send data to the socket. The socket must be connected to the remote socket. Returns the number of bytes sent, which may be less than the data length ("short write").

#### socket.sendall(bytes)

Send all data to the socket. The socket must be connected to the remote socket. Unlike `send()`, this method will try to send all data by continuously sending data blocks.

The behavior of this method on non-blocking sockets is undefined. Therefore, on MicroPython, it is recommended to use the `write()` method, which has the same "no short write" strategy to block the socket and will return the number of bytes sent on the non-blocking socket.

#### socket.recv(bufsize)

Receive data from the socket. The return value is a byte object representing the received data. The maximum amount of data received at one time is specified by bufsize.

#### socket.sendto(bytes, address)

Send data to the socket. The socket should not be connected to the remote socket, because the target socket is specified by the address.

#### socket.recvfrom(bufsize)

Receive data from the socket. The return value is a pair (byte, address), where bytes is the byte object representing the received data, and address is the address of the socket that sends the data.

#### socket.setsockopt(level, optname, value)

Set the value of the given socket option. The required symbolic constants are defined in the socket module (SO_* etc.). The value can be an integer or a byte-like object representing a buffer.
#### socket.settimeout(value)

Note: Not every port supports this method, see below.

Prevent socket operations from setting timeouts. The value parameter can be a non-negative floating point number representing seconds, or it can be None. If a non-zero value is given, if the timeout value has elapsed before the operation is completed, subsequent socket operations will raise an "OSError" exception. If zero is given, the socket is in non-blocking mode. If None is given, the socket is in blocking mode.

Not every "MicroPython port" supports this method. A more portable and universal solution is to use the uselect.poll object. This allows multiple objects to be waited at the same time (not just on sockets, but on generic `stream` objects that support polling). example:

```python
# Instead of:
s.settimeout(1.0) # time in seconds
s.read(10) # may timeout

# Use:
poller = uselect.poll()
poller.register(s, uselect.POLLIN)
res = poller.poll(1000) # time in milliseconds
if not res:
    # s is still not ready for input, i.e. operation timed out
```

> Difference with CPython

> CPython raises `socket.timeout` exception in case of timeout, which is a subclass of OSError. MicroPython directly raises an `OSError`. If you use `except OSError`: to catch exceptions, your code will be valid in both MicroPython and CPython.

#### socket.setblocking(flag)

Set the blocking or non-blocking mode of the socket: if the flag is false, the socket is set to non-blocking, otherwise it is set to blocking mode.

This method is shorthand for certain `settimeout()` calls:

`sock.setblocking(True)` is equivalent to `sock.settimeout(None)`
`sock.setblocking(False)` i is equivalent to `sock.settimeout(0)`

#### socket.makefile(mode='rb', buffering=0)

Returns the file object associated with the socket. The exact return type depends on the parameters given to makefile(). Support is limited to binary mode ('rb','wb' and'rwb'). CPython parameters: encoding, errors and newlines are not supported.

> Difference with CPython

> Since MicroPython does not support buffered streams, the value of the buffer parameter is ignored and treated as 0 (unbuffered).

> Difference with CPython

> Closing the file object returned by makefile() will also close the original socket.

#### socket.read([size])

Read the size bytes from the slot. Return a bytes object. If no size is given, it will read all the data available in the socket until EOF; therefore, the method will not return until the socket is closed. This function attempts to read the requested data (there is no "short read"). However, for non-blocking sockets, this may not be possible, and then less data will be returned.

#### socket.readinto(buf[, nbytes])

Read bytes into buf. If nbytes is specified, at most multiple bytes are read. Otherwise, read at most len ​​(buf) bytes. Just like read(), this method follows the "no short read" strategy.

Return value: The number of bytes read and stored in buf.

#### socket.readline()

Read a line, ending with a newline character.

Return value: the row read.


#### socket.write(buf)

Write the byte buffer to the socket. This function will try to write all data to the socket (no "short write"). However, for non-blocking sockets, this may not be possible, and the return value will be less than the length of buf.

Return value: The number of bytes written.

#### exception usocket.error

MicroPython does not have this exception.

> Difference with CPython

> CPython used to have a `socket.error` exception and is now deprecated. It is an alias of `OSError`. In MicroPython, use `OSError` directly.




## Routine

### Example 1: Download the picture and display it

> Note the need to set WiFi SSID and password

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



### Example 2: Sending pictures

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
