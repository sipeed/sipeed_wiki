
# Linux使用小贴士


## Ubuntu如何开启ssh？

桌面版ubutnu默认没有安装ssh服务器，无法通过ssh远程连接；需要安装服务器来启用ssh。

```bash
sudo apt-get install openssh-server
```

## 如何在ubuntu与windows间传递文件？

最简单的方式：下载WinSCP，即可互传文件。
或者也可以搭建Samba服务器，那样在windows上可以直接访问共享文件夹。

## 如何在ubuntu上搭建samba服务器并设置共享文件夹？

此处仅作最简单的匿名登陆方式介绍（以ubuntu为例）：

- 首先安装samba
```bash
sudo apt-get install samba
```

- 打开samba配置文件
```bash
sudo vim /etc/samba/smb.conf
```

- 编辑内容

```
## Debugging/Accounting ####
# share the dir without passwd

security = user
map to guest = Bad User

# 在文件结尾添加如下行：
[share]

# 更改path为指定目录
path=/your/path
public=yes
writable=yes
```

- 启动Samba服务：
    ```bash
    /etc/init.d/samba start
    ```  

    - 将共享目录赋予权限 `sudo chmod 777 your_path`
    - 注：最好将共享目录的上级目录也赋予权限
