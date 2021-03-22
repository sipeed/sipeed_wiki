---
title: network
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: network
---


该模块用于初始化各种网卡驱动，网卡具有连接路由，断开路由，查看网卡连接信息，检查是否连接等功能。

使用`WiFi`请确保已经接上了天线

### [esp8285](##network.ESP8285(uart))
在部分开发板上带了 一个 使用`AT`方式交互的网卡模块，比如`esp8285`，与`k210`通过串口连接

引脚`8`是使能脚，可以创建一个`GPIO`对象来控制它的高低电平来实现使能和失能，也可以用它复位（先低后高），复位后需要等待一小段时间才能操作，
可以查看例程[network_espat.py](https://github.com/sipeed/MaixPy_scripts/blob/79a5485ec983e67bb8861305a52418b29e0dc205/network/network_espat.py)

### [esp32](##network.ESP32_SPI(cs,rst,rdy,mosi,miso,sclk))
目前在`MaixDuino`开发板中有一个 `esp32` 模块通过 `spi` 与`k210`相连
同时也有单独的`TF`插卡式模块


## network.ESP8285(uart)

构造一个`ESP8285`网卡对象，使用该方法需要传入一个`uart`对象，在`MaixPy`目前支持的`dock`和`GO`上，是使用AT指令模块作为`WiFi`。所以该`uart`对象是与`AT`模块通信的对象，可以查看`uart`模块例程

调用此方法会初始化`ESP8285`， 如果失败会抛出异常


### 参数

* `uart`: 与AT模块通信的UART对象

### 返回值

* `ESP8285`: 网卡对象

## ESP8285

### connect(ssid, key)

连接热点（AP/路由器）

#### 参数

* `ssid`: 热点的`SSID`
* `key`: 热点的密码

#### 返回值

无， 如果发生错误会抛出异常

### 2.2. ifconfig

查看wifi连接信息，目前network不支持设置网卡配置

```
nic.ifconfig()
```

#### 参数

无

#### 返回值

`tuple` 类型， 元素都是字符串：`(ip, netmask, gateway, dns_server, dhcp_server, mac, ssid)`， 如果没有查询到或者无效，值为`"0"`


### isconnected

查看wifi是否连接

```
nic.isconnected()
```

#### 参数

无

#### 返回值

`True`: 已经连接
`False`: 断开连接

### disconnect

断开 wifi 连接

#### 参数

无

#### 返回值

无

### scan

扫描周围的热点信息

#### 参数

无

#### 返回值

一个 `list`对象， 每个元素包含了一个字符串， 字符串来自`AT`模块的响应，内容和`esp8285`的`AT指令文档`所描述的相同，如下：
`ecn, ssid, rssi,mac, channel, freq	offset, freq cali, pairwise_cipher, group_cipher, bgn, wps`

* `ecn`：加密⽅式
  * 0：OPEN
  * 1：WEP
  * 2：WPA_PSK
  * 3：WPA2_PSK
  * 4：WPA_WPA2_PSK
  * 5：WPA2_Enterprise（⽬前 AT 不⽀持连接这种加密 AP）
* `ssid`：字符串参数，AP 的 SSID
* `rssi`：信号强度
* `mac`：字符串参数，AP 的 MAC 地址
* `channel`：信道号
* `freq offset`：AP 频偏，单位：kHz。此数值除以 2.4，可得到 ppm 值
* `freq	cali`：频偏校准值
* `pairwise_cipher`:
  * 0：CIPHER_NONE
  * 1：CIPHER_WEP40
  * 2：CIPHER_WEP104
  * 3：CIPHER_TKIP
  * 4：CIPHER_CCMP
  * 5：CIPHER_TKIP_CCMP
  * 6：CIPHER_UNKNOWN
* `group_cipher`: 定义与 `pairwise_cipher` 相同
* `bgn`: bit0 代表 b 模式; bit1 代表 g 模式; bit2 代表 n 模式
         若对应 bit 为 1，表示该模式使能；若对应 bit 为 0，则该模式未使能。
* `wps`：0，WPS 未使能；1，WPS 使能

比如： 
```
info_strs = ['4,"ChinaNet-lot0",-79,"c8:50:e9:e8:21:3e",1,-42,0,4,3,7,1', '4,"TOPSTEP2G4",-7
0,"f8:e7:1e:0d:0d:f8",1,-57,0,4,4,7,0']
```
这看起来可能会比较奇怪，因为每个AP的信息都是一串字符，信息里面还有整型和字符串，字符串用双引号括起来的，所以拿到这个字符串后需要再次处理后再使用，比如：
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

info_strs = ['4,"ChinaNet-lot0",-79,"c8:50:e9:e8:21:3e",1,-42,0,4,3,7,1', '4,"TOPSTEP2G4",-70,"f8:e7:1e:0d:0d:f8",1,-57,0,4,4,7,0']

info = wifi_deal_ap_info(info_strs)
print(info)
```

输出是：

```
[[4, 'ChinaNet-lot0', -79, 'c8:50:e9:e8:21:3e', 1, -42, 0, 4, 3, 7, 1], [4, 'TOPSTEP2G4', -70, 'f8:e7:1e:0d:0d:f8', 1, -57, 0, 4, 4, 7, 0]] 
```

然后比如我们需要获得所有`AP`的`SSID`只需要使用
```
for ap_info in info:
    print(ap_info[1])
```

### enable_ap(ssid, key, chl=5, ecn=3)

* **警告：截止 2020年11月26日前， MaixPy 的 socket 还未实现 listen / bind / accpet 等函数操作。**

打开热点

#### 参数

* `ssid`: SSID
* `key`： 密码
* `chl`： WiFi信号的通道号
* `ecn`： 加密方法， 有`OPEN``WPA2_PSK`等，参考本页`ESP8285`的常量部分， 默认值是`3`， 也就是`ESP8285.WPA2_PSK`，比如
```python
nic = network.ESP8285(uart)
nic.enable_ap("maixpy", "12345678", 5, nic.OPEN)
```
或者
```
nic.enable_ap("maixpy", "12345678", 5, network.ESP8285.OPEN)
```



### disable_ap()

关闭热点


### 常量

#### OPEN

热点的加密方式为不需要密码

#### WPA_PSK

热点的加密方式为 `WPA_PSK`

#### WPA2_PSK

热点的加密方式为 `WPA2_PSK`

#### WPA_WPA2_PSK

热点的加密方式为 `WPA_WPA2_PSK`

## 例程


参考[network目录下的例程](https://github.com/sipeed/MaixPy_scripts/tree/master/network)


## network.ESP32_SPI(cs,rst,rdy,mosi,miso,sclk)

构造一个`ESP32_SPI`网卡对象，需要传入对应的`GPIOHS FUNC`

如果传入参数数量不对，会返回错误

**注意** 想要在 maixduino 上 SPI 和 SD 不冲突，需要设置 ESP32_SPI 为硬件 SPI 配置。

### 参数

* 对应引脚功能的 `fpioa_func`

### 返回值

* `ESP32_SPI` 网卡对象


## ESP32_SPI

### adc

读取`esp32`模块的`adc`值

#### 参数

无

#### 返回值

`tunple`，5个通道的`adc`值<br>顺序是`"PIN36", "PIN39", "PIN34", "PIN35", "PIN32"`

#### 例程

[demo_esp32_read_adc.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/demo_esp32_read_adc.py)


## network.WIZNET5K(spi, cs)

构造一个`WIZNET5K`网卡对象，使用该方法需要传入一个`spi`对象， 一个`cs` pin 脚.

调用此方法会初始化`WIZNET5K`， 如果失败会抛出异常


### 参数

* `spi`: 负责与 WIZNET5K 模块通信
* `cs`: spi 通信片选脚

### 返回值

* `WIZNET5K`: 网卡对象

## WIZNET5K

### dhclient

DHCP 动态获取 IP

```
nic.dhclient()
```

#### 参数

无

#### 返回值

* `True`: 获取成功
* `False`: 获取失败

### ifconfig

```
nic.ifconfig()
```

#### 参数

* 不传参: 查询网卡信息
* 传入`(ip, netmask, gateway, dns_server)`字符串元组: 配置网卡, `ip` ip 地址, `netmask`子网掩码, `gateway`网关 IP 地址, `dns_server` DNS 服务 IP 地址.

#### 返回值

* 不传参: 返回`tuple`，元素都是字符串, `(ip, netmask, gateway, dns_server)`， 如果没有查询到或者无效，值为`"0"`
* 传参: 返回`None`

### isconnected

查看网络是否连接

```
nic.isconnected()
```

#### 参数

无

#### 返回值

* `True`: 已经连接
* `False`: 断开连接

#### 例程

[network_wiznet5k.py](https://github.com/sipeed/MaixPy_scripts/blob/master/network/network_wiznet5k.py)