---
title: Zero通过otg与PC共享网络
---

## 修改内核

在内核选项中勾选上`Ethernet Gadget`, 就可以让Zero与PC通过usb共享网络。

```
Location:
-> Device Drivers
	-> USB support (USB_SUPPORT [=y])
		-> USB Gadget Support (USB_GADGET [=y])
			<*>   USB Gadget precomposed configurations (Ethernet Gadget (with CDC Ethernet support))
```

## 配置zero网卡

### on zero

#### 打开usb0网卡

`ifconfig usb0 up`

#### 设置usb0 ip

  `usb0 192.168.2.100 netmask 255.255.255.0`

由于usb网卡默认关闭，所以建议将该文件写入开机脚本，上电即可使用ssh连接。

修改/etc/init.d/S40network

```
  start)
        printf "Starting network: "
        /sbin/ifup -a
        /sbin/ifconfig usb0 up
        /sbin/ifconfig usb0 192.168.2.100 netmask 255.255.255.0
        [ $? = 0 ] && echo "OK" || echo "FAIL"
        ;;
  stop)
        printf "Stopping network: "
        /sbin/ifdown -a
        /sbin/ifconfig usb0 down              
        [ $? = 0 ] && echo "OK" || echo "FAIL"
        ;;   
```

### on pc(linux)

`ifconfig -a`

`usb0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500`

如果出现：

`enx1288194be3c3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500`

可以尝试重启ubuntu，然后就可以正确识别。如果还不行，也可以以`enx1288194be3c3`代替`usb0`继续执行后面操作。

#### 为usb网卡分配ip

`ifconfig usb0 192.168.2.1 netmask 255.255.255.0`

然后就可以ping通了

```
lithromantic@ubuntu ~
☺  ping 192.168.2.100                                                          
PING 192.168.2.100 (192.168.2.100) 56(84) bytes of data.
64 bytes from 192.168.2.100: icmp_seq=1 ttl=64 time=1.45 ms
64 bytes from 192.168.2.100: icmp_seq=2 ttl=64 time=1.08 ms
64 bytes from 192.168.2.100: icmp_seq=3 ttl=64 time=0.920 ms
64 bytes from 192.168.2.100: icmp_seq=4 ttl=64 time=0.721 ms
64 bytes from 192.168.2.100: icmp_seq=5 ttl=64 time=0.713 ms
^C
--- 192.168.2.100 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4026ms
rtt min/avg/max/mdev = 0.713/0.976/1.454/0.274 ms
```

```
# ping 192.168.2.1
PING 192.168.2.1 (192.168.2.1): 56 data bytes
64 bytes from 192.168.2.1: seq=0 ttl=64 time=1.227 ms
64 bytes from 192.168.2.1: seq=1 ttl=64 time=0.941 ms
64 bytes from 192.168.2.1: seq=2 ttl=64 time=0.880 ms
64 bytes from 192.168.2.1: seq=3 ttl=64 time=0.953 ms
64 bytes from 192.168.2.1: seq=4 ttl=64 time=1.165 ms
^C
--- 192.168.2.1 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 0.880/1.033/1.227 ms
```

需要注意的是，此时Licheepi Zero只能访问主机ip地址，所以是无法正常上网的。

on pc (Windows)

Windows不能很好的识别Licheepi Zero的usb网络，需要手动安装驱动，详情参考[测试测试 g_serial / g_ether USB Gadget (RNDIS) / 全志 V3S/F1C100s/X3/D1/R329/AIC800 / WhyCan Forum(哇酷开发者社区)](https://whycan.com/t_2401.html)

### SSH连接

在linux中，可以直接在终端中ssh连接

 ```
 lithromantic@ubuntu: ~
 $ ssh root@192.168.2.100        [20:41:18]
 root@192.168.2.100's password: 
 # ls
 badapple.mp4  demo
 ```

如果需要移动文件等操作，可以使用scp，或者在文件管理器中添加`sftp://192.168.2.100` 以文件夹形式打开Licheepi Zero的磁盘。

![image-20210901115013624](https://raw.githubusercontent.com/USTHzhanglu/picture/main/img/image-20210901115013624.png)

![image-20210901115115780](https://raw.githubusercontent.com/USTHzhanglu/picture/main/img/image-20210901115115780.png)

对于windows，如果驱动安装失败，可以通过ssh桥接的方式连接LicheepiZero（需要linux虚拟机）。

参考连接：[烂泥：学习ssh之ssh隧道应用-烂泥行天下 (ilanni.com)](https://www.ilanni.com/?p=10425)

操作如下

![202109011224](https://raw.githubusercontent.com/USTHzhanglu/picture/main/img/202109011224.gif)