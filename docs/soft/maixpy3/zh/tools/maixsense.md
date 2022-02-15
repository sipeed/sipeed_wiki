---
title: 如何使用 mobaxterm 
keywords: Jupyter, MaixPy3, Python, Python3
desc: maixpy doc: 如何使用 mobaxterm 
---
## 串口连接

使用串口连接软件，以 mobaxterm 为例

![](./assets/mobaxterm-serial-4.png)

在「session setting」 对话框里选择【serial】，再选好串口号及波特率，点击【OK】就完成连接了。

![](./assets/mobaxterm-serial-5.png)

同样【session】会保存在左侧的【session】标签页里，方便下次连接。

## SSH 连接

除了有线串口的方式，还可以通过无线访问 SSH 登录 Linux 系统，如一般的家用路由器。

在 Linux 系统输入 ifconfig 查看自己 ip 地址（192.168.1.185），然后输入自己名称和密码，常见有 root / root 。

> 如果没有设置密码，root 的连接密码是 root 。输入密码的时候是看不到的，在输入结束之后，按回车即可

![](./assets/mobaxterm_ssh.jpg)

就可以看到 Linux 的登录会话终端了。

![](./assets/mobaxterm_ssh_view.jpg)

## MaixPy3 IDE 连接

MaixPy3 IDE 连接 MaixSense 只能使用远程连接，不能使用有线连接，而且每个人的网络环境都存在差异，可能存在连接不上的情况出现。

### 准备
- 烧录好带有 MaixPy3 的 Armbian 系统
- 连接网络进行 MaixPy3更新，确保 MaixPy3 的版本大于 0.3.4。
- 运行 ifconfig 获取开发板的 IP 地址

### 连接
在板子上运行 python -c "import maix.mjpg;maix.mjpg.start()" 启动板子上的远程 RPyc 服务

在 IDE 中新建代码区，运行下面的连接代码
```python
$connect("192.168.43.44") # 此处填入开发板的 IP 地址
import platform
print(platform.uname())
```