---
title: How to connect MaixPy to the Internet
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: How to connect MaixPy to the Internet
---


> Big Rat 2020-11-26 Edit

Since it is called AIOT, it can't be without networking. MaixPy now supports W5X00 / EPS32 / ESPAT and other networking methods, as shown below.

- ESP32 needs to be equipped with [dedicated SPI firmware](https://github.com/sipeed/Maixduino_esp32_fimware) to support TCP / UDP client.

- ESPAT works with Espressif[AT firmware (esp-at)](https://github.com/espressif/esp-at), and only supports TCP clients.

- W5X00 can be configured + used by connecting to the Internet cable, and supports TCP/UDP client.

Before using the Socket, please connect the network first. The wired one needs to resolve the DNS and IP address, gateway, and the wireless one needs to fill in the WIFI account (SSID) and password. Do not ask "Bug found!!! How to access No problem with Baidu (I don’t have internet access).

## Computer Network Foundation

> If you don't know these basics, you can't use it.

It is recommended to know the following keywords when applying MaixPy network function:

- What are network and socket?
- What is TCP \ UDP? What is HTTP \ HTTPS \ MQTT \ FTP?

From the perspective of pragmatism, in maixpy ​​(micropython), the content about the network is divided into the most basic two-layer interface.

### network

Responsible for managing the interface of the network card. The network card is a type of hardware interface that sends the network data protocol from the hardware and belongs to the category of hardware.

For example: Usually the main function of a WIFI network card is to connect to a wireless router to help users connect to the Internet, while a wired network card helps users connect to the Internet through a network cable. They will complete gateway configuration, DNS resolution, Ping request and other operations at this layer. If it is used as a server, it will also complete functions such as wireless network distribution and domain name resolution.

### socket

The difference from the network card is that the socket is only responsible for the transmission of the data protocol at the application layer. It is usually encapsulated by the bottom PCB connection block into the common socket socket interface module. It mainly provides the connection transmission method of TCP/IP and UDP. Users can perform network programming based on this interface.

#### What are TCP and UDP?

On the basis of socket, we are divided into two typical transmission interfaces, TCP and UDP. The main emphasis is on whether the communication between the two applications is connected. If the connection is not maintained, the UDP connection method is used. If a long connection with the server is required, then When using TCP connection, please note that UDP and TCP ports are independent of each other and do not need to be confused.

> TCP has a streaming long connection retransmission mechanism, through several types of internal timers and data congestion windows, it can be ensured that user data will not be lost to a certain extent, but there are cases of overtime waiting.

> UDP does not need to be connected, and the data is directly transmitted in the form of broadcast to the upper switch and router, so UDP packets have a certain degree of penetration, and can penetrate data packets outside without configuration in the upper network (actual situation Will be changed).

#### What is HTTP \ HTTPS \ MQTT \ FTP?

Based on this, communication protocols such as HTTP protocol running on port 80, HTTP and other communication protocols transmitted on port 443, FTP file transfer protocol on port 21, and application transfer protocols such as MQTT and WebSocket based on this can be expanded, but they are all Based on the functions completed by the original socket interface, the only difference is the encapsulated application protocol.

### How to network?

Please select the corresponding networking script according to your own network situation, you can run it directly, or upload it to the hardware as a class library to facilitate subsequent socket development. You can use a script similar to the following to complete the network configuration, which is in the sample code Can know the specific usage.

General verification usage:

```python

import network_esp32
print(network_esp32)
print(dir(network_esp32))

from network_esp32 import wifi
print(wifi)

'''ouput
>>> <module'network_esp32' from'network_esp32.py'>
['__class__','__name__','__file__','GPIO','network','time','board_info','fm','wifi']
<class'wifi'>
MicroPython v0.5.1-140-g7bf6445e7-dirty on 2020-11-26; Sipeed_M1 with kendryte-k210
Type "help()" for more information.
>>>
'''

```

Real environment usage:

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

Use Maixduino's esp32 to connect to the network and upload the library [network_esp32.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/network_esp32.py).

```python
# This file is part of MaixPY
# Copyright (c) sipeed.com
#
# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license.php
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
                __class__.nic = network.ESP32_SPI(cs=fm.fpioa.GPIOHS10,rst=fm.fpioa.GPIOHS11,rdy=fm.fpioa.GPIOHS12, mosi=fm.fpioa.GPIOHS13,miso=fm.fpioa.GPIOHS14,sclk= fm.fpioa.GPIOHS15)
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

#### AT firmware of ESP82XX

Use the AT firmware of ESP8266/85 to connect to the Internet and upload the library [network_espat.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/network_espat.py)

> `board_info` is related to the board, and different board configurations are different. [Manual configuration](../../api_reference/builtin_py/board_info.md) is required before use.

```python
# This file is part of MaixPY
# Copyright (c) sipeed.com
#
# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license.php
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
            M1wPower.value(0) # b'\r\n ets Jan 8 2013,rst cause:1, boot mode:(7,6)\r\n\r\nwaiting for host\r\n'

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
            time.sleep_ms(500) # at start> 500ms
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
    network state: True ('192.168.0.165', '255.255.255.0', '192.168.0.1', '0', '0','b0:b9:8a:5b:be:7f','Sipeed_2.4G' )
    >
    MicroPython v0.5.1-136-g039f72b6c-dirty on 2020-11-18; Sipeed_M1 with kendryte-k210
    Type "help()" for more information.
    >>>
    >>>
    >>>
    raw REPL; CTRL-B to exit
    >OK
    network state: True ('192.168.0.165', '255.255.255.0', '192.168.0.1', '0', '0','b0:b9:8a:5b:be:7f','Sipeed_2.4G' )
    >
'''
```

#### WIZNET5K by Spmod

Use Spmod's WIZNET5K network card to connect to the Internet and upload the library [network_wiznet5k.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/network_wiznet5k.py)

> vamoosebbf 2020-12-10 edit

WIZNET5K is a wired network card module, you only need to plug in the network cable when using it, using the SPI protocol, this module is enabled by default in the complete firmware, but not in the minimum firmware.
```python
spi1 = SPI(4, mode=SPI.MODE_MASTER, baudrate=600 * 1000,
            polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=WIZNET5K_SPI_SCK, mosi=WIZNET5K_SPI_MOSI, miso = WIZNET5K_SPI_MISO)

nic = network.WIZNET5K(spi = spi1, cs = WIZNET5K_SPI_CS)
print("Static IP: ", nic.ifconfig())

#dhcp Obtain IP dynamically, because the static IP has been set above, this step can be skipped. It should be noted that if you use DHCP, you must use an infinite loop like the following code, otherwise the acquisition will be unsuccessful
while True:
    if(nic.dhclient()):
        print("DHCP IP:", nic.ifconfig())
        break;

'''output
>>> Static IP: ('192.168.0.117', '255.255.255.0', '192.168.0.1', '8.8.8.8')
init dhcp
DHCP IP: ('192.168.0.165', '255.255.255.0', '192.168.0.1', '8.8.8.8')
'''

```

### Networking performance

Please start using socket network programming after confirming the network and obtaining the IP address, and you have obtained the IP address as follows.

```shell
network state: True ('192.168.0.165', '255.255.255.0', '192.168.0.1', '0', '0','b0:b9:8a:5b:be:7f','Sipeed_2.4G' )
```
