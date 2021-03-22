---
title: 如何给 MaixPy 连接网络
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 如何给 MaixPy 连接网络
---


> 大佬鼠 2020-11-26 编辑

既然叫 AIOT 自然不能少了联网， MaixPy 现在支持 W5X00 / EPS32 / ESPAT 等联网的方法，如下所示。

- ESP32 需要搭配[专用的 SPI 固件](https://github.com/sipeed/Maixduino_esp32_fimware)，支持 TCP / UDP 客户端。

- ESPAT 配合乐鑫[AT 固件（esp-at）](https://github.com/espressif/esp-at)，只支持 TCP 客户端。

- W5X00 接上网线就可以配置+使用了，支持 TCP / UDP 客户端。

在使用 Socket 之前，请先把网络连接好，有线的需要解析 DNS 和 IP 地址、网关，无线的需要填 WIFI 的账号（SSID）和密码，千万不要问出“发现 Bug 了！！！怎么访问不了百度（我没有联网）”的问题。

## 计算机网络基础

> 不会这些基础，你也用不起来。

在应用 MaixPy 网络功能建议知道以下关键词：

- network 和 socket 是什么？
- TCP \ UDP 是什么？ HTTP \ HTTPS \ MQTT \ FTP 又是什么？

从实用主义的角度讲解，在 maixpy (micropython) 中，关于网络的内容分为最基础的以下两层接口。

### network

负责管理网卡的接口，网卡是将网络数据协议从硬件发出的一类硬件接口，属于硬件范畴。

举例来说： 通常 WIFI 网卡主要职能就是连接无线路由器，帮助用户连接互联网，而有线网卡则是借由网线帮助用户连接互联网，它们会在这一层完成网关配置、DNS 解析、Ping 请求等操作，若是作为服务端还会完成无线配网、域名解析等功能。

### socket 

与网卡不同的地方在于 socket 只负责应用层的数据协议的传输，通常由最底层的 PCB 连接块封装成现在常见的 socket 套接字接口模块，它主要提供 TCP/IP 与 UDP 的连接传输方法，用户可以基于该接口进行网络编程。

#### TCP 和 UDP 是什么？

在 socket 的基础上，我们分为 TCP 和 UDP 两个典型传输接口，主要强调的是两个应用之间通信是否保持连接，如果不保持连接，则使用 UDP 连接方式，需要与服务器保持长连接则使用 TCP 连接方式，注意 UDP 和 TCP 端口是彼此独立的存在，不需要混为一谈。

> TCP 拥有流式长连接重传机制，通过内部几类计时器和数据拥堵窗口可以一定程度上保证用户数据不会丢失，但存在超时等待的情况。

> UDP 则不需要连接，直接讲数据以广播的形式向上层交换机、路由器之间传输，所以 UDP 包具有一定的穿透性，可以在上级网络中不经过配置向外穿透数据包（实际情况会被改变）。

#### HTTP \ HTTPS \ MQTT \ FTP 是什么？

而基于此可以拓展出运行在 80 端口的 HTTP 协议，在 443 端口传输的 HTTP 等通信协议，在 21 端口的 FTP 文件传输协议，基于此的还有 MQTT 和 WebSocket 等应用传输协议，但它们都是基于原始 socket 接口完成的功能，不同的只是封装的应用协议。

### 如何联网？

请根据自己的网络情况选择对应的联网脚本，可以直接运行，也可以将其作为类库上传到硬件中，方便后续的 socket 开发，可以使用类似如下的脚本完成网络的配置，这在示例代码中可以得知具体用法。

一般验证用法：

```python

import network_esp32
print(network_esp32)
print(dir(network_esp32))

from network_esp32 import wifi
print(wifi)

'''ouput
>>> <module 'network_esp32' from 'network_esp32.py'>
['__class__', '__name__', '__file__', 'GPIO', 'network', 'time', 'board_info', 'fm', 'wifi']
<class 'wifi'>
MicroPython v0.5.1-140-g7bf6445e7-dirty on 2020-11-26; Sipeed_M1 with kendryte-k210
Type "help()" for more information.
>>> 
'''

```

真实环境用法：

```python

SSID = "Sipeed_2.4G"
PASW = "xxxxxxxx"

def enable_esp32():
    from network_esp32 import wifi
    if wifi.isconnected() == False:
        for i in range(5):
            try:
                # Running within 3 seconds of power-up can cause an SD load error
                # wifi.reset(is_hard=False)
                wifi.reset(is_hard=True)
                print('try AT connect wifi...')
                wifi.connect(SSID, PASW)
                if wifi.isconnected():
                    break
            except Exception as e:
                print(e)
    print('network state:', wifi.isconnected(), wifi.ifconfig())

enable_esp32()

def enable_espat():
    from network_espat import wifi
    if wifi.isconnected() == False:
        for i in range(5):
            try:
                wifi.reset()
                print('try AT connect wifi...')
                wifi.connect(SSID, PASW)
                if wifi.isconnected():
                    break
            except Exception as e:
                print(e)
    print('network state:', wifi.isconnected(), wifi.ifconfig())

#enable_espat()

```

#### Maixduino + ESP32

使用 Maixduino 的 esp32 联网，上传该类库 [network_esp32.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/network_esp32.py) 即可。

```python
# This file is part of MaixPY
# Copyright (c) sipeed.com
#
# Licensed under the MIT license:
#   http://www.opensource.org/licenses/mit-license.php
#

import time, network
from Maix import GPIO
from fpioa_manager import fm

class wifi():

    nic = None

    def reset(force=False, reply=5, is_hard=True):
        if force == False and __class__.isconnected():
            return True
        try:
            # IO map for ESP32 on Maixduino
            fm.register(25,fm.fpioa.GPIOHS10)#cs
            fm.register(8,fm.fpioa.GPIOHS11)#rst
            fm.register(9,fm.fpioa.GPIOHS12)#rdy

            if is_hard:
                print("Use Hareware SPI for other maixduino")
                fm.register(28,fm.fpioa.SPI1_D0, force=True)#mosi
                fm.register(26,fm.fpioa.SPI1_D1, force=True)#miso
                fm.register(27,fm.fpioa.SPI1_SCLK, force=True)#sclk
                __class__.nic = network.ESP32_SPI(cs=fm.fpioa.GPIOHS10, rst=fm.fpioa.GPIOHS11, rdy=fm.fpioa.GPIOHS12, spi=1)
                print("ESP32_SPI firmware version:", __class__.nic.version())
            else:
                # Running within 3 seconds of power-up can cause an SD load error
                print("Use Software SPI for other hardware")
                fm.register(28,fm.fpioa.GPIOHS13, force=True)#mosi
                fm.register(26,fm.fpioa.GPIOHS14, force=True)#miso
                fm.register(27,fm.fpioa.GPIOHS15, force=True)#sclk
                __class__.nic = network.ESP32_SPI(cs=fm.fpioa.GPIOHS10,rst=fm.fpioa.GPIOHS11,rdy=fm.fpioa.GPIOHS12, mosi=fm.fpioa.GPIOHS13,miso=fm.fpioa.GPIOHS14,sclk=fm.fpioa.GPIOHS15)
                print("ESP32_SPI firmware version:", __class__.nic.version())

            # time.sleep_ms(500) # wait at ready to connect
        except Exception as e:
            print(e)
            return False
        return True

    def connect(ssid="wifi_name", pasw="pass_word"):
        if __class__.nic != None:
            return __class__.nic.connect(ssid, pasw)

    def ifconfig(): # should check ip != 0.0.0.0
        if __class__.nic != None:
            return __class__.nic.ifconfig()

    def isconnected():
        if __class__.nic != None:
            return __class__.nic.isconnected()
        return False

if __name__ == "__main__":
    # It is recommended to callas a class library (upload network_espat.py)

    # from network_esp32 import wifi
    SSID = "Sipeed_2.4G"
    PASW = "xxxxxxxx"

    def check_wifi_net(reply=5):
        if wifi.isconnected() != True:
            for i in range(reply):
                try:
                    wifi.reset(is_hard=True)
                    print('try AT connect wifi...')
                    wifi.connect(SSID, PASW)
                    if wifi.isconnected():
                        break
                except Exception as e:
                    print(e)
        return wifi.isconnected()network_espw5k

    if wifi.isconnected() == False:
        check_wifi_net()
    print('network state:', wifi.isconnected(), wifi.ifconfig())

    # The network is no longer configured repeatedly
    import socket
    sock = socket.socket()
    # your send or recv
    # see other demo_socket_tcp.py / udp / http / mqtt
    sock.close()

'''ouput
    MicroPython v0.5.1-136-g039f72b6c-dirty on 2020-11-18; Sipeed_M1 with kendryte-k210
    Type "help()" for more information.
    >>>
    >>>
    >>>
    raw REPL; CTRL-B to exit
    >OK
    Use Hareware SPI for other maixduino
    [esp32_spi] use hard spi(1)
    hard spi
    esp32 set hard spi clk:9159090
    Get version fail
    try AT connect wifi...
    Use Hareware SPI for other maixduino
    [Warning] function is used by unknown(pin:10)
    [Warning] function is used by unknown(pin:6)
    [Warning] function is used by unknown(pin:11)
    [esp32_spi] use hard spi(1)
    hard spi
    esp32 set hard spi clk:9159090
    ESP32_SPI firmware version: 1.4.0
    try AT connect wifi...
    network state: True ('192.168.0.180', '255.255.255.0', '192.168.0.1')
    >
    MicroPython v0.5.1-136-g039f72b6c-dirty on 2020-11-18; Sipeed_M1 with kendryte-k210
    Type "help()" for more information.
    >>>
    >>>
    >>>
    raw REPL; CTRL-B to exit
    >OK
    network state: True ('192.168.0.180', '255.255.255.0', '192.168.0.1')
    >
    MicroPython v0.5.1-136-g039f72b6c-dirty on 2020-11-18; Sipeed_M1 with kendryte-k210
    Type "help()" for more information.
    >>>
'''
```

#### ESP82XX 的 AT 固件

使用 ESP8266/85 的 AT 固件联网，上传该类库 [network_espat.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/network_espat.py) 即可

> `board_info` 与板卡相关，不同板卡配置不同，使用前需要[手动配置](../../api_reference/builtin_py/board_info.md)。

```python
# This file is part of MaixPY
# Copyright (c) sipeed.com
#
# Licensed under the MIT license:
#   http://www.opensource.org/licenses/mit-license.php
#

import time, network
from Maix import GPIO
from machine import UART
from fpioa_manager import fm
from board import board_info

class wifi():

    __is_m1w__ = True
    uart = None
    eb = None
    nic = None

    def init():
        if __class__.__is_m1w__:
            fm.register(0, fm.fpioa.GPIOHS1, force=True)
            M1wPower=GPIO(GPIO.GPIOHS1, GPIO.OUT)
            M1wPower.value(0) # b'\r\n ets Jan  8 2013,rst cause:1, boot mode:(7,6)\r\n\r\nwaiting for host\r\n'

        fm.register(board_info.WIFI_EN, fm.fpioa.GPIOHS0) # board_info.WIFI_EN == IO 8
        __class__.en = GPIO(GPIO.GPIOHS0,GPIO.OUT)

        fm.register(board_info.WIFI_RX,fm.fpioa.UART2_TX) # board_info.WIFI_RX == IO 7
        fm.register(board_info.WIFI_TX,fm.fpioa.UART2_RX) # board_info.WIFI_TX == IO 6
        __class__.uart = UART(UART.UART2, 115200, timeout=1000, read_buf_len=8192)

    def enable(en):
        __class__.en.value(en)

    def _at_cmd(cmd="AT\r\n", resp="OK\r\n", timeout=20):
        __class__.uart.write(cmd) # "AT+GMR\r\n"
        time.sleep_ms(timeout)
        tmp = __class__.uart.read()
        # print(tmp)
        if tmp and tmp.endswith(resp):
            return True
        return False

    def at_cmd(cmd="AT\r\n", timeout=20):
        __class__.uart.write(cmd) # "AT+GMR\r\n"
        time.sleep_ms(timeout)
        tmp = __class__.uart.read()
        return tmp

    def reset(force=False, reply=5):
        if force == False and __class__.isconnected():
            return True
        __class__.init()
        for i in range(reply):
            print('reset...')
            __class__.enable(False)
            time.sleep_ms(50)
            __class__.enable(True)
            time.sleep_ms(500) # at start > 500ms
            if __class__._at_cmd(timeout=500):
                break
        __class__._at_cmd()
        __class__._at_cmd('AT+UART_CUR=921600,8,1,0,0\r\n', "OK\r\n")
        __class__.uart = UART(UART.UART2, 921600, timeout=1000, read_buf_len=10240)
        # important! baudrate too low or read_buf_len too small will loose data
        #print(__class__._at_cmd())
        try:
            __class__.nic = network.ESP8285(__class__.uart)
            time.sleep_ms(500) # wait at ready to connect
        except Exception as e:
            print(e)
            return False
        return True

    def connect(ssid="wifi_name", pasw="pass_word"):
        if __class__.nic != None:
            return __class__.nic.connect(ssid, pasw)

    def ifconfig(): # should check ip != 0.0.0.0
        if __class__.nic != None:
            return __class__.nic.ifconfig()

    def isconnected():
        if __class__.nic != None:
            return __class__.nic.isconnected()
        return False

if __name__ == "__main__":
    # It is recommended to callas a class library (upload network_espat.py) 

    # from network_espat import wifi
    SSID = "Sipeed_2.4G"
    PASW = "xxxxxxxx"

    def check_wifi_net(reply=5):
        if wifi.isconnected() != True:
            for i in range(reply):
                try:
                    wifi.reset()
                    print('try AT connect wifi...', wifi._at_cmd())
                    wifi.connect(SSID, PASW)
                    if wifi.isconnected():
                        break
                except Exception as e:
                    print(e)
        return wifi.isconnected()

    if wifi.isconnected() == False:
        check_wifi_net()
    print('network state:', wifi.isconnected(), wifi.ifconfig())

    # The network is no longer configured repeatedly
    import socket
    sock = socket.socket()
    # your send or recv
    # see other demo_socket_tcp.py / udp / http / mqtt
    sock.close()

'''ouput
    >>>
    raw REPL; CTRL-B to exit
    >OK
    [Warning] function is used by fm.fpioa.GPIOHS1(pin:17)
    [Warning] function is used by fm.fpioa.GPIOHS0(pin:16)
    reset...
    try AT connect wifi... True
    could not connect to ssid=Sipeed_2.4G
    reset...
    try AT connect wifi... True
    network state: True ('192.168.0.165', '255.255.255.0', '192.168.0.1', '0', '0', 'b0:b9:8a:5b:be:7f', 'Sipeed_2.4G')
    >
    MicroPython v0.5.1-136-g039f72b6c-dirty on 2020-11-18; Sipeed_M1 with kendryte-k210
    Type "help()" for more information.
    >>>
    >>>
    >>>
    raw REPL; CTRL-B to exit
    >OK
    network state: True ('192.168.0.165', '255.255.255.0', '192.168.0.1', '0', '0', 'b0:b9:8a:5b:be:7f', 'Sipeed_2.4G')
    >
'''
```

#### Spmod 的 WIZNET5K

使用 Spmod 的 WIZNET5K 网卡联网，上传该类库 [network_wiznet5k.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/network_wiznet5k.py) 即可

> vamoosebbf 2020-12-10 编辑

WIZNET5K 为有线网卡模块, 使用时只需要将网线插好即可, 使用 SPI 协议, 在完整固件中默认使能了此模块, 最小固件中没有.

```python
spi1 = SPI(4, mode=SPI.MODE_MASTER, baudrate=600 * 1000,
            polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=WIZNET5K_SPI_SCK, mosi=WIZNET5K_SPI_MOSI, miso = WIZNET5K_SPI_MISO)

nic = network.WIZNET5K(spi = spi1, cs = WIZNET5K_SPI_CS)
print("Static IP: ", nic.ifconfig())

#dhcp 动态获取 IP, 因为上面已经设置了静态 IP , 这一步可跳过, 要注意的是如果使用 DHCP, 必须像下面代码一样使用死循环, 否则将获取不成功
while True:
    if(nic.dhclient()):
        print("DHCP IP:", nic.ifconfig() )
        break;

'''output
>>> Static IP:  ('192.168.0.117', '255.255.255.0', '192.168.0.1', '8.8.8.8')
init dhcp
DHCP IP: ('192.168.0.165', '255.255.255.0', '192.168.0.1', '8.8.8.8')
'''

```

### 联网表现

请在确认了联网，得到了 IP 地址才开始使用 socket 网络编程喔，就如下获得了 IP 地址。

```shell
network state: True ('192.168.0.165', '255.255.255.0', '192.168.0.1', '0', '0', 'b0:b9:8a:5b:be:7f', 'Sipeed_2.4G')
```
