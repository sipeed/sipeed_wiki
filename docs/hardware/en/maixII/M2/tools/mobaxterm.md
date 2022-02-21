---
title: 如何使用 mobaxterm 
keywords: Jupyter, MaixPy3, Python, Python3
desc: maixpy doc: 如何使用 mobaxterm 
---

## mobaxterm 是什么？

这是在 Windows 下使用的全能终端管理软件，对开发与运维人员必备，可以在 [mobaxterm.mobatek.net/download](https://mobaxterm.mobatek.net/download.html) 获取免费版本使用，在国内网站上有中文版。

![](https://mobaxterm.mobatek.net/img/moba/features/feature-terminal.png)

主要通过它提供的下列功能：

- serial 通过串口连接 Linux 系统的终端
- ssh 远程登录 Linux 系统的终端
- ftp 远程访问文件服务上的资源

## 连接 Serial

开源硬件产品大多都会预留串口（Serial）用作 Linux 系统的终端交互接口，下面介绍串口【session】的创建。

![](./asserts/mobaxterm-serial-4.png)

在「session setting」 对话框里选择【serial】，再选好串口号及波特率，点击【OK】就完成连接了。

![](./asserts/mobaxterm-serial-5.png)

同样【session】会保存在左侧的【session】标签页里，方便下次连接。

## 连接 SSH

除了有线串口的方式，还可以通过无线访问 SSH 登录 Linux 系统，如一般的家用路由器。

在 Linux 系统输入 ifconfig 查看自己 ip 地址（192.168.1.185），然后输入自己名称和密码，常见有 root / root 。

> 如果没有设置密码，root 的连接密码是 root 。输入密码的时候是看不到的，在输入结束之后，按回车即可

![](./asserts/mobaxterm_ssh.jpg)

就可以看到 Linux 的登录会话终端了。

![](./asserts/mobaxterm_ssh_view.jpg)

> 以下连接方式只是合适在 MaixII-Dock 上使用的，需要使用 MaixPy3 IDE 版本 0.4.2以上的版本

MaixII-Dock 可以通过 OTG 接口转发到 127.0.0.1 的 22 端口，但是每次使用之前，都需要通过运行 IDE 来进行配置，进行 ssh 端口转发服务的开启。

具体的连接方式和上面的 ssh 方式一样，只需要将 ip 地址修改成 127.0.0.1 即可，默认用户名和密码都是 root。

## 连接 FTP

与 SSH 同理。

![](./asserts/mobaxterm_ftp.png)

进入后就可以看到文件夹了。

![](./asserts/mobaxterm_ftp.jpg)

可以拖拽文件上传和下载。

![](./asserts/mobaxterm_ftp_ud.png)

## 如何进行编程

除了使用串口进行 Python 代码的复制粘贴运行，还可以通过在 FTP 文件管理获取下图的代码编辑器，编辑后保存就会自动同步上传（下图为 C 代码参考，其他代码同理）。

![](https://mobaxterm.mobatek.net/img/moba/features/feature-mobatexteditor.png)

这时候再拿到终端里运行 Python 脚本即可。

```bash
python xxxx.py
```
