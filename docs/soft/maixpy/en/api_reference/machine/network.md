---
title: network
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: network
---


This module is used to initialize various network card drivers. The network card has the functions of connecting routing, disconnecting routing, viewing the connection information of the network card, and checking whether it is connected.

To use `WiFi` please make sure that the antenna is connected

### [esp8285](##network.ESP8285(uart))
On some development boards, a network card module that uses `AT` to interact, such as `esp8285`, is connected to `k210` through a serial port

Pin `8` is the enable pin. You can create a `GPIO` object to control its high and low levels to achieve enable and disable, or you can use it to reset (low first and then high), and you need to wait for a while after reset Time to operate,
You can view the routine [network_espat.py](https://github.com/sipeed/MaixPy_scripts/blob/79a5485ec983e67bb8861305a52418b29e0dc205/network/network_espat.py)

### [esp32](##network.ESP32_SPI(cs,rst,rdy,mosi,miso,sclk))
Currently there is an `esp32` module in the `MaixDuino` development board which is connected to `k210` through `spi`
There is also a separate `TF` plug-in module


## network.ESP8285(uart)

Construct an `ESP8285` network card object. To use this method, you need to pass in a `uart` object. On the `dock` and `GO` currently supported by `MaixPy`, the AT command module is used as the `WiFi`. So the `uart` object is the object that communicates with the `AT` module, you can check the `uart` module routine

Calling this method will initialize `ESP8285` and throw an exception if it fails


### Parameters

* `uart`: UART object communicating with AT module

### return value

* `ESP8285`: NIC object

## ESP8285

### connect(ssid, key)

Connect hotspot (AP/router)

#### Parameters

* `ssid`: the `SSID` of the hotspot
* `key`: hotspot password

#### return value

None, if an error occurs, an exception will be thrown

### 2.2. ifconfig

View wifi connection information, currently network does not support setting network card configuration

```
nic.ifconfig()
```

#### Parameters

no

#### return value

`tuple` type, elements are all strings: `(ip, netmask, gateway, dns_server, dhcp_server, mac, ssid)`, if not found or invalid, the value is `"0"`


### isconnected

Check if wifi is connected

```
nic.isconnected()
```

#### Parameters

no

#### return value

`True`: connected
`False`: disconnect

### disconnect

Disconnect wifi connection

#### Parameters

no

#### return value

no

### scan

Scan the surrounding hotspot information

#### Parameters

no

#### return value

A `list` object, each element contains a string, the string comes from the response of the `AT` module, and the content is the same as described in the `AT command document` of `esp8285`, as follows:
`ecn, ssid, rssi,mac, channel, freq offset, freq cali, pairwise_cipher, group_cipher, bgn, wps`

* `ecn`: Encryption method
  * 0: OPEN
  * 1: WEP
  * 2: WPA_PSK
  * 3: WPA2_PSK
  * 4: WPA_WPA2_PSK
  *5: WPA2_Enterprise (Previously, AT does not support connecting to this encrypted AP)
* `ssid`: string parameter, AP's SSID
* `rssi`: signal strength
* `mac`: string parameter, AP's MAC address
* `channel`: channel number
* `freq offset`: AP frequency offset, unit: kHz. Divide this value by 2.4 to get the ppm value
* `freq cali`: frequency offset calibration value
* `pairwise_cipher`:
  * 0: CIPHER_NONE
  * 1: CIPHER_WEP40
  * 2: CIPHER_WEP104
  * 3: CIPHER_TKIP
  * 4: CIPHER_CCMP
  * 5: CIPHER_TKIP_CCMP
  * 6: CIPHER_UNKNOWN
* `group_cipher`: The definition is the same as `pairwise_cipher`
* `bgn`: bit0 stands for b mode; bit1 stands for g mode; bit2 stands for n mode
         If the corresponding bit is 1, it means the mode is enabled; if the corresponding bit is 0, the mode is not enabled.
* `wps`: 0, WPS is not enabled; 1, WPS is enabled

For example:
```
info_strs = ['4,"ChinaNet-lot0",-79,"c8:50:e9:e8:21:3e",1,-42,0,4,3,7,1', '4,"TOPSTEP2G4 ",-7
0,"f8:e7:1e:0d:0d:f8",1,-57,0,4,4,7,0']
```
This may seem strange, because the information of each AP is a string of characters, and there are integers and strings in the information. The strings are enclosed in double quotes, so after you get this string, you need to process it again. Use again, such as:
```python
def wifi_deal_ap_info(info):
    res = []
    for ap_str in info:
        ap_str = ap_str.split(",")
        info_one = []
        for node in ap_str:
            if node.startswith('"'):
                info_one.append(node[1:-1])
            else:
                info_one.append(int(node))
        res.append(info_one)
    return res

info_strs = ['4,"ChinaNet-lot0",-79,"c8:50:e9:e8:21:3e",1,-42,0,4,3,7,1', '4,"TOPSTEP2G4 ",-70,"f8:e7:1e:0d:0d:f8",1,-57,0,4,4,7,0']

info = wifi_deal_ap_info(info_strs)
print(info)
```

The output is:

```
[[4,'ChinaNet-lot0', -79,'c8:50:e9:e8:21:3e', 1, -42, 0, 4, 3, 7, 1], [4,'TOPSTEP2G4', -70,'f8:e7:1e:0d:0d:f8', 1, -57, 0, 4, 4, 7, 0]]
```

Then for example, we need to get all the `SSID` of `AP` only need to use
```
for ap_info in info:
    print(ap_info[1])
```

### enable_ap(ssid, key, chl=5, ecn=3)

* **Warning: As of November 26, 2020, MaixPy sockets have not yet implemented functions such as listen / bind / accpet. **

Open hotspot

#### Parameters

* `ssid`: SSID
* `key`: password
* `chl`: Channel number of WiFi signal
* `ecn`: Encryption method, including `OPEN``WPA2_PSK`, etc., refer to the constant part of `ESP8285` on this page, the default value is `3`, which is `ESP8285.WPA2_PSK`, for example
```python
nic = network.ESP8285(uart)
nic.enable_ap("maixpy", "12345678", 5, nic.OPEN)
```
or
```
nic.enable_ap("maixpy", "12345678", 5, network.ESP8285.OPEN)
```



### disable_ap()

Turn off hotspot


### Constant

#### OPEN

The hotspot encryption method does not require a password

#### WPA_PSK

The hotspot encryption method is `WPA_PSK`

#### WPA2_PSK

The hotspot encryption method is `WPA2_PSK`

#### WPA_WPA2_PSK

The encryption method of the hotspot is `WPA_WPA2_PSK`

## Routine


Refer to [routines in the network directory](https://github.com/sipeed/MaixPy_scripts/tree/master/network)


## network.ESP32_SPI(cs,rst,rdy,mosi,miso,sclk)

To construct an `ESP32_SPI` network card object, you need to pass in the corresponding `GPIOHS FUNC`

If the number of incoming parameters is incorrect, an error will be returned

**Note** If SPI and SD do not conflict on maixduino, you need to set ESP32_SPI as the hardware SPI configuration.

### Parameters

* `fpioa_func` corresponding to pin function

### return value

* `ESP32_SPI` network card object


## ESP32_SPI

### adc

Read the `adc` value of the `esp32` module

#### Parameters

no

#### return value

`tunple`, the value of `adc` for 5 channels<br>The order is `"PIN36", "PIN39", "PIN34", "PIN35", "PIN32"`

#### Routine

[demo_esp32_read_adc.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_esp32_read_adc.py)


## network.WIZNET5K(spi, cs)

Construct a `WIZNET5K` network card object. To use this method, you need to pass in a `spi` object and a `cs` pin.

Calling this method will initialize `WIZNET5K` and throw an exception if it fails


### Parameters

* `spi`: Responsible for communication with WIZNET5K module
* `cs`: spi communication chip selection footer

### return value

* `WIZNET5K`: NIC object

## WIZNET5K

### dhclient

DHCP dynamically obtain IP

```
nic.dhclient()
```

#### Parameters

no

#### return value

* `True`: Get success
* `False`: Get failed

### ifconfig

```
nic.ifconfig()
```

#### Parameters

* No reference: query network card information
* Incoming `(ip, netmask, gateway, dns_server)` string tuple: configure network card, `ip` ip address, `netmask` subnet mask, `gateway` gateway IP address, `dns_server` DNS service IP address .

#### return value

* No parameters: return `tuple`, the elements are all strings, `(ip, netmask, gateway, dns_server)`, if not found or invalid, the value is `"0"`
* Pass parameter: return `None`

### isconnected

Check if the network is connected

```
nic.isconnected()
```
#### Parameters

no

#### return value

* `True`: already connected
* `False`: disconnect

#### Routine

[network_wiznet5k.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/network_wiznet5k.py)
