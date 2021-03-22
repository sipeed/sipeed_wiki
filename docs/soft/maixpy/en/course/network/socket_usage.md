---
title: How to use Socket network programming
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: How to use Socket network programming
---


> Big Rat 2020-11-26 edit, so far MaixPy's socket module has not yet implemented interfaces such as listen / bind / accept.

## How to use TCP and UDP clients to connect to the server

Assuming that the basic content of [How to connect MaixPy to the network](./network_config.md) is known, run the sample code directly.

* Warning: Don’t ask: "Why can’t you access the network without a network connection!"

Please confirm the address and port before using the following client code.

### Prepare client code

There are the following types of typical client code:

- TCP client [demo_socket_tcp_client.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_socket_tcp_client.py)
- UDP client [demo_socket_udp_client.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_socket_udp_client.py)
- TCP video transmission client [demo_socket_pic_client.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_socket_pic_client.py)

### Prepare debugging tools (server code)

Commonly used in network debugging assistants, or running the provided Python3 server script on your computer.

- TCP server [demo_socket_tcp_server.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_socket_tcp_server.py)
- UDP server [demo_socket_udp_server.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_socket_udp_server.py)
- TCP image transmission server [demo_socket_pic_server.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_socket_pic_server.py)

First start a network service with a known IP address and port, and wait for MaixPy as a client to send data to the server.

### Examples of typical client code

-TCP

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

-UDP

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

### Other network functions

The following are special function codes.

#### esp32's ping

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

#### ADC of esp32

- [demo_esp32_read_adc.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_esp32_read_adc.py)

```shell
    MicroPython v0.5.1-136-g039f72b6c-dirty on 2020-11-18; Sipeed_M1 with kendryte-k210
    Type "help()" for more information.
    >>>
    raw REPL; CTRL-B to exit
    >OK
    (2370, 3102, 3071)
    2017 2753 0977 2709 0963 0855: adc
    0617 0757 0150 0095 0133 0153: adc
    1319 1478 0955 0939 0698 0619: adc
    2403 3231 3299 3298 1483 0779: adc
    1119 1815 1274 1315 0230 0255: adc
    0951 0951 0295 0283 0319 0399: adc
    2175 2769 2576 2579 1487 1104: adc
    1995 2846 2647 2699 0839 0441: adc
```

> In fact, espAT also obtains ADC in this way, but it can only be used on designated pins.

#### HTTP support

- [demo_http_get_jpg.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_http_get_jpg.py)

#### https support

This function is not compiled by default, but what is provided is the use of HTTP, and HTTP and HTTPS are only the difference of the path url. Note that the IP resolution of https depends on the firmware of the network card and is not completed on the K210.

- [demo_socket_https.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_socket_https.py)

#### scan WIFI AP hotspot of esp32, 82XX

- [demo_esp32_ap_scan.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_esp32_ap_scan.py)

- [demo_espat_ap_scan.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_espat_ap_scan.py)
```python
'''
    >>>
    raw REPL; CTRL-B to exit
    >OK
    SSID: Sipeed_2.4G, ENC: WPA/WPA2 PSK, RSSI: -57
    SSID: ChinaNet-Ffdj, ENC: WPA/WPA2 PSK, RSSI: -58
    SSID: wea_615, ENC:WPA/WPA2 PSK, RSSI: -67
    SSID: ChinaNet-PnAN, ENC: WPA/WPA2 PSK, RSSI: -70
    SSID: wea_613, ENC:WPA/WPA2 PSK, RSSI: -73
    SSID: ChinaNet-TnSG, ENC: WPA/WPA2 PSK, RSSI: -82
    SSID: chipshine_GUEST, ENC:WPA/WPA2 PSK, RSSI: -83
    SSID: ASUS, ENC: WPA/WPA2 PSK, RSSI: -86
    SSID: gta888, ENC: WPA/WPA2 PSK, RSSI: -87
    SSID: huahua, ENC: WPA/WPA2 PSK, RSSI: -88
    >
    MicroPython v0.5.1-136-g039f72b6c-dirty on 2020-11-18; Sipeed_M1 with kendryte-k210
    Type "help()" for more information.
    >>>
'''
```

#### mqtt support

This is the code provided by the official repository of micropython. If it is for commercial use, please configure the socket as non-blocking and add the MQTT keep-alive protocol.

- [demo_socket_mqtt.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_socket_mqtt.py)

#### Update the AT firmware of ESP82XX

> This is a function provided for the AT firmware, so you can understand it naturally.

- [demo_espat_ap_test.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_espat_ap_test.py)

- [espat_upgrade.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/espat_upgrade.py)
