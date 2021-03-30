Zero通过otg与PC共享网络
===================================

.. contents:: 本文目录

在内核选项中勾选上：composite gadget: Serial and Ethernet.
就可以让Zero与PC通过usb共享网络。

**确认usb虚拟网口被使能**

使用usb线连接Zero和PC，在Zero和PC上查看网络接口：

.. code-block:: bash

    zp@ubuntu64:~$ ifconfig 
    ...
    usb0 Link encap:Ethernet HWaddr 66:36:e9:13:fd:44

    root@Lichee:~# ifconfig 
    ...
    usb0 Link encap:Ethernet HWaddr 2e:cf:e1:3f:ad:61

**确认有usb0接口后，手工设置两者在同一网段下：**

.. code-block:: bash

    on PC: sudo ifconfig usb0 192.168.2.1
    on Zero: sudo ifconfig usb0 192.168.2.100

:: 

    Test PC ping Zero:

    zp@ubuntu64:~$ ping 192.168.2.100
    PING 192.168.2.100 (192.168.2.100) 56(84) bytes of data.
    64 bytes from 192.168.2.100: icmp_seq=1 ttl=64 time=2.74 ms
    64 bytes from 192.168.2.100: icmp_seq=2 ttl=64 time=2.19 ms
    ...
    Everything is ok now, let's edit network config(/etc/network/interfaces) to save it:
    On PC add:
    allow-hotplug usb0
    auto usb0
    iface usb0 inet static
    address 192.168.2.1
    netmask 255.255.255.0
    On Zero add:
    allow-hotplug usb0
    auto usb0
    iface usb0 inet static
    address 192.168.2.100
    netmask 255.255.255.0
    gateway 192.168.2.1
    Share Network from PC
    Enable forwarding on your PC:
    echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward > /dev/null
    sudo iptables -P FORWARD ACCEPT
    sudo iptables -A POSTROUTING -t nat -j MASQUERADE -s 192.168.2.0/24
    test Ping google (if you are in china, ping baidu.com please...)
    ping google.com

    If everything goes ok, your Zero is online now~

    You can ssh to Zero on your PC or any PC in the local net.

    zp@ubuntu64:~$ ssh root@192.168.2.100
    root@192.168.2.100's password:
    Linux Lichee 4.10.2-licheepi-zero+ #12 SMP Wed Mar 15 23:22:13 CST 2017 armv7l
    The programs included with the Debian GNU/Linux system are free software;
    the exact distribution terms for each program are described in the
    individual files in /usr/share/doc/*/copyright.
    Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
    permitted by applicable law.
    Last login: Wed Feb 15 23:39:33 2017 from 192.168.2.1
    root@Lichee:~#
    And you can execute any command on Zero via ssh.
    Zero is used as a "headless" board now.
