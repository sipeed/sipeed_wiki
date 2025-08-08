## ssh 远程登录 root 用户，密码输入正确却登录不成功，要如何使能 root 用户密码登录 SSH？
默认密码：root
*考虑到安全性，使用的默认策略，root 用户只能通过密钥进行远程登录，可以免输密码不仅方便快捷且安全。其所需操作如下：通过串口或桌面登录系统后，手动粘贴个人公钥保存到`/root/.ssh/authorized_keys`文件内，该文件不存在可手动创建。更详细过程可搜索 SSH 密钥登录或直接查看该[教程](https://www.runoob.com/w3cnote/set-ssh-login-key.html)。*

若执意要通过密码登录，可如下操作：
```bash
# 登录进入串口终端，执行一遍下方命令
# 启用 root 用户远程密码登录
echo "PermitRootLogin yes" > /etc/ssh/sshd_config.d/allow-root.conf
systemctl restart sshd
```
开发结束后，避免 root 用户密码意外泄漏导致的各种风险，最好关闭 root 用户远程密码登录，执行下列操作：
```bash
# 登录进入任意终端，执行一遍下方命令
# 关闭 root 用户远程密码登录
rm /etc/ssh/sshd_config.d/allow-root.conf
systemctl restart sshd
```


## Q: 使用 TFCard&eMMC 镜像，根文件系统默认分区太小，如何扩容 eMMC 或者 TFCard？
```bash
# 登录进入任意终端，执行一遍下方命令
# 替换下面的 mmcblkX 为 mmcblk0（eMMC）或 mmcblk1（TFCard）。
# /dev/mmcblkXp2 为第二分区，也是根文件系统分区。 
parted /dev/mmcblkX resizepart 2 100%
resize2fs /dev/mmcblkXp2
sync
```


## Q: 有些大语言模型需要执行 tokenizer 相关 python 脚本，执行报错 ModuleNotFoundError，如何解决？
```bash
# 避免污染系统 python 库，新建虚拟环境
apt install python3-venv
python3 -m venv venv-llm
# 激活该虚拟环境
source venv-llm/bin/activate
# 安装缺失的 python 模块，国内可使用清华镜像源加速
pip install transformers jinja2 -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
# 安装完毕，可继续执行脚本
```
记得每次要执行相关 python 脚本前，要先激活已安装的虚拟环境：
```bash
# 激活该虚拟环境
source venv-llm/bin/activate
```

## Q: 类似 GPIO2_A27 已在设备树被配置成了 I2C3_SCL，那在不使用 I2C3 的时候如何控制 GPIO2_A27 呢？（pinctrl）
```bash
cd /sys/kernel/debug/pinctrl/4250200.pinctrl
grep "GPIO2_A27" pinmux-functions
# output # function 447: GPIO2_A27, groups = [ I2C3_SCL ]
grep "I2C3_SCL" pinmux-pins
# output # pin 87 (I2C3_SCL): device 2024000.i2c function i2c3_scl group I2C3_SCL
echo 2024000.i2c > /sys/bus/platform/drivers/i2c_designware/unbind
grep "I2C3_SCL" pinmux-pins
# output # pin 87 (I2C3_SCL): UNCLAIMED

# echo "<group-name function-name>" > pinmux-select
echo "I2C3_SCL GPIO2_A27" > pinmux-select

gpioset gpiochip2 27=0
gpioset gpiochip2 27=1
```

## Q：MAC 物理地址每次重启随机生成，导致 ip 地址不稳定，请问如何解决？

A：sdcard-20250627.img.xz 开始，第一分区（FAT32）根目录下会有 `config.txt` 文件，内为 uboot 的环境变量配置。添加环境变量 `ethaddr` 和 `eth1addr` 即可持久化修改对应网卡的mac地址：

```
ethaddr=d0:00:00:00:00:01
eth1addr=d0:00:00:00:00:02
```

![](../assets/m4n/set-macaddress.png)