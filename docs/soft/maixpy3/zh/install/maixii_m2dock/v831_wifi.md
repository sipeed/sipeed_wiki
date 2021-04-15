---
title: MaixII M2dock wifi 调试
keywords: MaixII, MaixPy3, Python, Python3, M2dock
desc: maixpy doc: MaixII M2dock wifi 调试
---


## V831 WIFI 调试

在 /etc/wpa_supplicant.conf 中新增用户 WIFI 

```text
ctrl_interface=/tmp/wpa_supplicant
update_config=1

network={
    ssid="Sipeed"
    psk="123456789"
}
# 自己可以配置多个 wifi
network={
    ssid="Geek-mi"
    psk="Geek.99110099"
}
```

重启系统（重新上电）之后板子就能自动连接 WIFI

***

## 调试使用

开启 WIFI 网络相关工具包的编译

开启 WIFI， 连接网络过程

1. 挂载网卡

```text
insmod /lib/modules/4.9.118/8189fs.ko
```

2. 开启网口 wlan0

```text
ifconfig wlan0 up
```

3. 添加/修改网络配置文件

```text
vi /etc/wpa_supplicant.conf
```



在 /etc/wpa_supplicant.conf 中新增内容(该步骤可省略)

```text
ctrl_interface=/tmp/wpa_supplicant
update_config=1

network={
    ssid="Sipeed"
    psk="1234567890"
}
# 自己可以配置多个 wifi
network={
    ssid="Geek-mi"
    psk="Geek.99110099"
}
```



4. 启用配置文件，连接网络

```text
wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf
```



5. 启用 DHCP 分配 IP

> 注意：需要先安装好天线

```text
udhcpc -i wlan0
```

6. 测试 ping

```text
ping www.baidu.com
```

### 配置 WIFI 自动连接



在用户自定义路径下新建文件内容如下：

> 文件路径: ` /root/develop/wifi_connect.sh`

```text
mkdir -p /root/develop/ # 创建路径
vim /root/develop/wifi_connect.sh # 创建 sh 文件
chmod +x /root/develop/wifi_connect.sh # 修改脚本权限

```



```text
insmod /lib/modules/4.9.118/8189fs.ko
sleep 1s

ifconfig wlan0 up
sleep 1s

wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf
sleep 3s

killall udhcpc
sleep 1s

udhcpc -i wlan0
```



```text
echo -e  "sh /root/develop/wifi_connect.sh" >> /etc/init.d/rcS
```

```text
# 1. 挂载网卡驱动
insmod /lib/modules/4.9.118/8189fs.ko
sleep 1s
# 2. 开启网口 wlan0
ifconfig wlan0 up
sleep 1s
# 3. 启用配置文件，连接网络
wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf
sleep 3s
# 4. 杀死以前的dhcp进程
killall udhcpc
sleep 1s
# 5. 启用 DHCP 分配 IP
udhcpc -i wlan0
```



```text
# 关闭有线连接
ifconfig eth0 down
# 打开无线连接
ifconfig wlan0 up
# 杀死以前配置进程
killall wpa_supplicant
# 启动wifi配置，使文件生效
wpa_supplicant -B -Dwext -iwlan0 -c/etc/wpa_supplicant.conf
# 启动有点慢，等一下启动完毕
sleep 3s
# 杀死以前的dhcp进程
killall udhcpc
# 启动dhcp获取ip
udhcpc -b -i wlan0
# static ip
# ifconfig wlan0 192.168.134.250 netmask 255.255.255.0
# route add default gw 192.168.134.1

```



## WIFI 带宽/延迟测试

使用 iperf3 测试网络带宽

iperf3,默认端口: 5210



服务端（这里使用 PC）：

```text
iperf3 -s
```

客户端（这里使用 V831）：

```text
iperf3 -c [serve ip] -p [port]
```

测试项目：

- WIFI 吞吐量（带宽测试）

- WIFI 丢包/时延测试
