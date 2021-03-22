---
title: 如何使用 Socket 网络编程
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 如何使用 Socket 网络编程
---


> 大佬鼠 2020-11-26 编辑，截止目前 MaixPy 的 socket 模块还未能实现 listen / bind / accept 等接口。

## 如何使用 TCP 和 UDP 客户端连接服务器

假设已知 [如何给 MaixPy 连接网络](./network_config.md) 的基础内容，直接运行示例代码。

* 警告：不准问：“没联网为什么不能访问网络的问题！”

请确认 地址 和 端口后再使用以下客户端代码。

### 准备客户端代码

有如下几类典型客户端代码：

- TCP 客户端 [demo_socket_tcp_client.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_socket_tcp_client.py)
- UDP 客户端 [demo_socket_udp_client.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_socket_udp_client.py)
- TCP 图传 客户端 [demo_socket_pic_client.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_socket_pic_client.py)

### 准备调试工具（服务端代码）

常见于网络调试助手，或者自己在电脑上运行提供的 Python3 服务端脚本。

- TCP 服务端 [demo_socket_tcp_server.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_socket_tcp_server.py)
- UDP 服务端 [demo_socket_udp_server.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_socket_udp_server.py)
- TCP 图传 服务端 [demo_socket_pic_server.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_socket_pic_server.py)

先起一个已知 IP 地址和端口的网络服务，等待 MaixPy 作为客户端发送数据过来服务器。

### 典型客户端代码举例

- TCP

```python
import socket
ADDR = ("192.168.0.107", 60000)
sock = socket.socket()
sock.connect(ADDR)
sock.settimeout(1)
while 1:
    sock.send("hello\n")
    #data = sock.recv(10) # old maxipy have bug (recv timeout no return last data)
    #print(data) # fix
    try:
      data = b""
      while True:
        tmp = sock.recv(1)
        print(tmp)
        if len(tmp) == 0:
            raise Exception('timeout or disconnected')
        data += tmp
    except Exception as e:
      print("rcv:", len(data), data)
    #time.sleep(2)

sock.close()
```

- UDP

```python
import socket
ADDR = ("192.168.0.107", 60000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1)
while 1:
    try:
        sock.sendto("hello\n", ADDR)
        data, addr = sock.recvfrom(1024)
    except Exception as e:
        print("receive error:", e)
        continue
    print("addr:", addr, "data:", data)
    time.sleep(2)
sock.close()
'''
>>>
raw REPL; CTRL-B to exit
>OK
network state: True ('192.168.0.186', '255.255.255.0', '192.168.0.1')
addr: ('192.168.0.107', 60000) data: b'HELLO\n'
addr: ('192.168.0.107', 60000) data: b'HELLO\n'
addr: ('192.168.0.107', 60000) data: b'HELLO\n'
'''
```

### 其他网络功能

以下为特殊功能代码。

#### esp32 的 ping

- [demo_esp32_ping.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_esp32_ping.py)

```shell
    ESP32_SPI firmware version: 1.4.0
    try AT connect wifi...
    network state: True ('192.168.0.180', '255.255.255.0', '192.168.0.1')
    ping baidu.com: 40 ms
    >
    MicroPython v0.5.1-136-g039f72b6c-dirty on 2020-11-18; Sipeed_M1 with kendryte-k210
    Type "help()" for more information.
    >>>
```

#### esp32 的 ADC

- [demo_esp32_read_adc.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_esp32_read_adc.py)

```shell
    MicroPython v0.5.1-136-g039f72b6c-dirty on 2020-11-18; Sipeed_M1 with kendryte-k210
    Type "help()" for more information.
    >>> 
    raw REPL; CTRL-B to exit
    >OK
    (2370, 3102, 3071)
    2017 2753 0977 2709 0963 0855  : adc
    0617 0757 0150 0095 0133 0153  : adc
    1319 1478 0955 0939 0698 0619  : adc
    2403 3231 3299 3298 1483 0779  : adc
    1119 1815 1274 1315 0230 0255  : adc
    0951 0951 0295 0283 0319 0399  : adc
    2175 2769 2576 2579 1487 1104  : adc
    1995 2846 2647 2699 0839 0441  : adc
```

> 其实 espAT 也是这样获取 ADC 的，但只能在指定的引脚上。

#### HTTP 的支持

- [demo_http_get_jpg.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_http_get_jpg.py)

#### https 的支持

该功能默认是不被编译的，但所以提供的是 HTTP 的使用方法，而 HTTP 和 HTTPS 只是路径 url 的区别，注意这个 https 的 IP 解析依赖于网卡固件，并不在 K210 上完成。

- [demo_socket_https.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_socket_https.py)

#### esp32、82XX 的 scan WIFI AP 热点

- [demo_esp32_ap_scan.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_esp32_ap_scan.py)

- [demo_espat_ap_scan.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_espat_ap_scan.py)

```python
'''
    >>>
    raw REPL; CTRL-B to exit
    >OK
    SSID:    Sipeed_2.4G     , ENC:WPA/WPA2 PSK , RSSI:        -57
    SSID:   ChinaNet-Ffdj    , ENC:WPA/WPA2 PSK , RSSI:        -58
    SSID:      wea_615       , ENC:WPA/WPA2 PSK , RSSI:        -67
    SSID:   ChinaNet-PnAN    , ENC:WPA/WPA2 PSK , RSSI:        -70
    SSID:      wea_613       , ENC:WPA/WPA2 PSK , RSSI:        -73
    SSID:   ChinaNet-TnSG    , ENC:WPA/WPA2 PSK , RSSI:        -82
    SSID:  chipshine_GUEST   , ENC:WPA/WPA2 PSK , RSSI:        -83
    SSID:        ASUS        , ENC:WPA/WPA2 PSK , RSSI:        -86
    SSID:       gta888       , ENC:WPA/WPA2 PSK , RSSI:        -87
    SSID:       huahua       , ENC:WPA/WPA2 PSK , RSSI:        -88
    >
    MicroPython v0.5.1-136-g039f72b6c-dirty on 2020-11-18; Sipeed_M1 with kendryte-k210
    Type "help()" for more information.
    >>>
'''
```

#### mqtt 支持

这个是来自于 micropython 的官方仓库提供的代码，如果是商业用途，请将 socket 配置为非阻塞且添加 MQTT 保活的协议。

- [demo_socket_mqtt.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_socket_mqtt.py)

#### 更新 ESP82XX 的 AT 固件

> 这是给 AT 固件提供的功能，懂的自然懂。

- [demo_espat_ap_test.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_espat_ap_test.py)

- [espat_upgrade.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/espat_upgrade.py)
